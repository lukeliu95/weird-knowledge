#!/usr/bin/env python3
"""每周提炼：把 Luke 回答时补的话、没按推荐选的题、他说"不对"的纠正做成案例卡；同一方向攒够 3 张卡写成规律草稿，
另一个模型复核后，每周最多 3 条交 Luke 认，认了 lukeeMind 下次回答就用上（ask.py 读 status 为"已确认"的）。

Luke 2026-10-26 选了 B（参照"工单 → AI 草稿 → 客服修改 → 定时蒸馏 → 人审发布 → 下次用上"的知识循环）：
原来只把旧题和他选的字母当例子，他补的话和纠正存下了却没人提炼。这里补上"定时提炼"和"审过才用上"两步。
方案和回测见 docs/2026-10-26-mind-distill-spec.md。数据只在 private/mind/，只交给 Opus 和本地 Qwen，不交给 Jev。

用法：
  distill.py cards                 给还没做卡的回答和纠正做案例卡（人名、公司名换掉）
  distill.py weekly                做卡 → 写草稿 → 复核 → 列出最多 3 条请 Luke 认（还有没答的就先不写新的）
  distill.py pending               再列一遍等 Luke 认的草稿
  distill.py confirm "1 3" [--note "原话"]    认第几条（编号是 pending / weekly 列出来的）
  distill.py reject "2" [--note "原话"]
  distill.py sim --cutoffs 2026-10-02,2026-10-09   回测用：按周模拟，每个时点只用更早的卡写草稿、复核
"""
import argparse, concurrent.futures as cf, datetime as dt, hashlib, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ask as A  # noqa: E402
import salesroom as S  # noqa: E402

E, OJ = A.E, A.OJ
DIR = A.DIR
CARDS, RULES = DIR / "cards.jsonl", DIR / "rules.jsonl"
SIM = DIR / "distill"
L3 = E.PRIVATE / "l3"
NEED = 3          # 一条规律至少要 3 张卡支持
WEEKLY_MAX = 3    # 每周最多交给 Luke 认 3 条（不让他批量确认，见 AGENTS.md 流程二）


def now():
    return dt.datetime.now()


def sources():
    """能做卡的事：他补了话的、没按推荐选的、他说过"不对"的。"""
    out = []
    for r in A.read_jsonl(L3 / "decisions.jsonl"):
        words, against = A.luke_words(r.get("reply")), str(r.get("follows_rec")) == "False"
        if r["choice"] in r["options"] and (words or against):
            out.append(dict(id=r["id"], src="decision", ts=r["ts"], question=r["question"][-1800:], options=r["options"],
                            choice=r["choice"], recommended=r.get("recommended", ""), words=words or r.get("reply", "")))
    for r in A.read_jsonl(L3 / "corrections.jsonl"):
        if r.get("skip"):
            continue
        out.append(dict(id=r["id"], src="correction", ts=r["ts"], question=r["question"][-1800:], options=r["options"],
                        choice=r["choice"], recommended=r.get("recommended", ""), words=(r.get("reply") or "")[:1200]))
    for r in A.read_jsonl(A.ASKS):
        if not r.get("luke") or r.get("from") == "smoke-test":
            continue
        words, against = A.luke_words(r.get("luke_note")), not r.get("agree", True)
        if words or against:
            out.append(dict(id=r["id"], src="ask", ts=r["at"], question=r["question"][-1800:], options=r["options"],
                            choice=r["luke"], recommended=r.get("choice", ""), words=words or r.get("luke_note", "")))
    return out


CARD_PROMPT = """下面是 Luke 以前拿主意的几件事。每件有当时的情况、选项、他选了什么、当时推荐的是哪个（有的话），以及他自己说的话。
请给每件做一张案例卡，中文大白话：
- situation：当时要定什么（一句话，40 字内）
- picked：他选了什么（一句话，把字母换成具体做法）
- words：他的话里，选项之外多出来的意思，尽量照抄原话（120 字内）。人名换成"某同事"或"某客户"，公司名换成"某客户"或"某合作方"。他只是复述了选项、没多说什么，就写空字符串
- lesson：从这件事能看出他在意什么、怎么判断（一句话，这是你的推断）
- category：从这些里选一个：{cats}
- worth：这张卡对以后预判他有没有用。2＝能看出明确的判断方式；1＝有一点；0＝看不出（比如只是选了个日期、点了个继续）

只输出 JSON：{{"cards": [{{"id": "原编号", "situation": "", "picked": "", "words": "", "lesson": "", "category": "", "worth": 0}}]}}

{items}"""


def card_batch(batch, names):
    items = "\n\n".join(
        f"[{x['id']}]（{'他说过不对的纠正' if x['src'] == 'correction' else '回答'}）\n情况：{x['question']}\n"
        + ("选项：" + "；".join(f"{k}. {v}" for k, v in x["options"].items() if v) + "\n" if any(x["options"].values()) else "")
        + f"他选了：{x['choice']}" + (f"（当时推荐 {x['recommended']}）" if x["recommended"] else "") + f"\n他说：{x['words']}"
        for x in batch)
    out = OJ.ask_json("你在整理一个人拿主意的案例，只输出一个 JSON 对象。",
                      S.scrub(CARD_PROMPT.format(cats="、".join(A.CATEGORIES), items=items), names))
    got = {c.get("id"): c for c in out.get("cards", [])}
    rows = []
    for x in batch:
        c = got.get(x["id"])
        if c:
            rows.append(dict(id=x["id"], src=x["src"], ts=x["ts"], choice=x["choice"], recommended=x["recommended"],
                             against=bool(x["recommended"]) and x["recommended"] != x["choice"],
                             **{k: S.scrub(str(c.get(k, "")), names) for k in ("situation", "picked", "words", "lesson")},
                             category=c.get("category") if c.get("category") in A.CATEGORIES else "其他",
                             worth=int(c.get("worth") or 0), made=now().isoformat(timespec="seconds")))
    return rows


def cmd_cards(_=None):
    E.load_env()
    have = {c["id"] for c in A.read_jsonl(CARDS)}
    todo = [x for x in sources() if x["id"] not in have]
    names = S.all_customer_names()
    batches = [todo[i:i + 8] for i in range(0, len(todo), 8)]
    new = 0
    with cf.ThreadPoolExecutor(4) as ex:
        for rows in ex.map(lambda b: _safe(card_batch, b, names), batches):
            with open(CARDS, "a") as f:
                for c in rows or []:
                    f.write(json.dumps(c, ensure_ascii=False) + "\n")
                    new += 1
    print(json.dumps({"todo": len(todo), "new_cards": new, "cards": len(A.read_jsonl(CARDS))}, ensure_ascii=False))


def _safe(fn, *args):
    try:
        return fn(*args)
    except Exception as e:
        print(f"  出错：{e}", file=sys.stderr)


def card_line(c):
    return (f"[{c['id']}] 要定：{c['situation']}｜他选了：{c['picked']}" + ("（没按推荐）" if c.get("against") else "")
            + (f"｜原话：{c['words']}" if c.get("words") else "") + f"｜看出：{c['lesson']}")


DRAFT_PROMPT = """下面是 Luke 拿主意的案例卡。每张：[编号] 要定什么｜他选了什么｜他的原话｜从中看出什么。
请找出被至少 3 张卡共同支持的判断规律，最多 {k} 条，支持的卡越多越好：
- rule：写成"遇到什么情况，他会怎么做"的一句话（50 字内，大白话），要能指导以后的选择，不要空话
- when_not：什么时候不适用（一句话；卡里有反例就照反例写）
- cards：真正支持它的卡的编号（至少 3 张，凑不够就不要写这条）
- category：从这些里选一个：{cats}
和下面「已经有的」意思相同的不要再写，和「他否掉的」意思相同的也不要写。

【已经有的】
{existing}

【他否掉的】
{rejected}

【案例卡】
{cards}

只输出 JSON：{{"rules": [{{"rule": "", "when_not": "", "cards": [""], "category": ""}}]}}"""

REVIEW_PROMPT = """你在复核别人从 Luke 的案例卡里提炼的规律，以挑错为主。逐条判断：
1. support：它引用的卡里，哪些真的支持这条规律（编号）
2. counter：全部卡里，哪些是反例：情境对得上，他却没这么做（编号）
3. 有没有说过头：把一两次的做法说成一贯如此，或者把具体情境说成所有情境
ok 为 true 的条件：真正支持的至少 3 张、反例明显比支持少、而且不过头。说过头但改小了还成立的，在 better 里给改小的说法（50 字内），ok 照样可以是 true。

【要复核的规律】
{rules}

【全部案例卡】
{cards}

只输出 JSON：{{"reviews": [{{"n": 1, "ok": true, "support": [""], "counter": [""], "better": "", "reason": "一句话"}}]}}"""


def existing_text():
    rows = A.read_jsonl(RULES)
    have = [r["rule"] for r in rows if r.get("status") in ("已确认", "待确认", "排队")]
    return (A.principles() + "\n" + (E.PRIVATE / "luke" / "confirmed.md").read_text() + "\n" + "\n".join(have),
            "\n".join(r["rule"] for r in rows if r.get("status") == "否掉") or "（无）")


def review(drafts, cards):
    """复核用另一个模型：本地 Qwen 开着就用它，连不上才用一次独立的 Opus（不看写草稿时的推理）。"""
    text = REVIEW_PROMPT.format(
        rules="\n".join(f"{i}. {d['rule']}（不适用：{d.get('when_not', '')}）引用：{'、'.join(d['cards'])}"
                        for i, d in enumerate(drafts, 1)),
        cards="\n".join(card_line(c) for c in cards))
    if OJ.qwen_ok():
        try:
            return S.qwen_json(text, max_tokens=4000).get("reviews", []), "qwen"
        except Exception as e:
            print(f"  Qwen 复核出错，改用 Opus：{e}", file=sys.stderr)
    return OJ.ask_json("你是严格的复核员，只输出一个 JSON 对象。", text).get("reviews", []), "opus"


def distill(cards, k=6):
    """写草稿、复核，返回留下来的规律。"""
    useful = [c for c in cards if c.get("worth", 0) >= 1]
    existing, rejected = existing_text()
    out = OJ.ask_json("你在提炼一个人拿主意的规律，只输出一个 JSON 对象。", DRAFT_PROMPT.format(
        k=k, cats="、".join(A.CATEGORIES), existing=existing, rejected=rejected,
        cards="\n".join(card_line(c) for c in useful)))
    ids = {c["id"] for c in useful}
    drafts = []
    for d in out.get("rules", []):
        cited = list(dict.fromkeys(i for i in d.get("cards", []) if i in ids))
        if d.get("rule") and len(cited) >= NEED:
            drafts.append(dict(rule=d["rule"].strip(), when_not=str(d.get("when_not", "")).strip(), cards=cited,
                               category=d.get("category") if d.get("category") in A.CATEGORIES else "其他"))
    if not drafts:
        return [], "", 0
    reviews, reviewer = review(drafts, useful)
    kept = []
    for i, d in enumerate(drafts, 1):
        rv = next((x for x in reviews if int(x.get("n", 0) or 0) == i), None)
        if not rv:
            continue
        support = [x for x in rv.get("support", []) if x in d["cards"]]
        counter = [x for x in rv.get("counter", []) if x in ids]
        if rv.get("ok") and len(support) >= NEED and len(counter) < len(support):
            kept.append({**d, "rule": A.clean_ids(rv.get("better") or d["rule"]), "when_not": A.clean_ids(d["when_not"]),
                         "drafted": d["rule"],
                         "support": support, "counter": counter, "review": rv.get("reason", ""), "reviewer": reviewer})
    return kept, reviewer, len(drafts)


def show_pending():
    pend = [r for r in A.read_jsonl(RULES) if r.get("status") == "待确认"]
    (DIR / "rules-pending-last.json").write_text(json.dumps([r["id"] for r in pend]))
    cards = {c["id"]: c for c in A.read_jsonl(CARDS)}
    for i, r in enumerate(pend, 1):
        print(f"{i}. {A.clean_ids(r['rule'])}")
        if r.get("when_not"):
            print(f"   不适用：{A.clean_ids(r['when_not'])}")
        print(f"   依据：{len(r['support'])} 次" + (f"，反例 {len(r['counter'])} 次" if r.get("counter") else ""))
        for cid in r["support"][:2]:
            c = cards.get(cid)
            if c:
                print(f"   · {c['situation']} → {c['picked']}" + (f"（你说：{c['words'][:60]}）" if c.get("words") else ""))
    if pend:
        print(f'\n共 {len(pend)} 条。回法：distill.py confirm "1 3"，reject "2"')
    return pend


def cmd_weekly(_):
    E.load_env()
    cmd_cards()
    rows = A.read_jsonl(RULES)
    pend = [r for r in rows if r.get("status") == "待确认"]
    queue = sorted([r for r in rows if r.get("status") == "排队"], key=lambda r: -len(r["support"]))
    if len(pend) < WEEKLY_MAX and not queue:
        kept, reviewer, n = distill(A.read_jsonl(CARDS))
        stamp = now().isoformat(timespec="seconds")
        for d in kept:
            d.update(id=hashlib.sha1(d["rule"].encode()).hexdigest()[:8], status="排队", made=stamp)
        rows += kept
        queue = sorted(kept, key=lambda r: -len(r["support"]))
        print(json.dumps({"drafts": n, "kept": len(kept), "reviewer": reviewer}, ensure_ascii=False))
    for r in queue[:max(0, WEEKLY_MAX - len(pend))]:
        r["status"] = "待确认"
    A.write_jsonl(RULES, rows)
    show_pending()


def decide(a, status):
    ids = json.loads((DIR / "rules-pending-last.json").read_text())
    pick = {ids[int(n) - 1] for n in re.findall(r"\d+", a.nums) if 0 < int(n) <= len(ids)}
    rows = A.read_jsonl(RULES)
    for r in rows:
        if r["id"] in pick:
            r.update(status=status, decided=now().isoformat(timespec="seconds"), luke_note=a.note)
    A.write_jsonl(RULES, rows)
    ok = [r for r in rows if r.get("status") == "已确认"]
    (DIR / "rules.md").write_text("# Luke 拿主意时的规律\n\n> distill.py 每周从他的回答和纠正里提炼，他认过的才在这里，lukeeMind 回答时会用上。\n\n"
                                  + "\n".join(f"- {A.clean_ids(r['rule'])}（不适用：{A.clean_ids(r.get('when_not')) or '未写'}；依据 {len(r['support'])} 次；"
                                              f"{r['decided'][:10]} 认的）" for r in ok) + "\n")
    print(json.dumps({status: len(pick), "confirmed_total": len(ok)}, ensure_ascii=False))


def cmd_sim(a):
    """回测用：每个时点只用更早的卡提炼，结果存 private/mind/distill/sim-<时点>.json，ask.py backtest --rules sim 读。"""
    E.load_env()
    SIM.mkdir(parents=True, exist_ok=True)
    cards = A.read_jsonl(CARDS)

    def one(cut):
        before = [c for c in cards if c["ts"][:10] < cut]
        kept, reviewer, n = distill(before)
        (SIM / f"sim-{cut}.json").write_text(json.dumps(
            {"cutoff": cut, "n_cards": len(before), "drafts": n, "reviewer": reviewer, "rules": kept}, ensure_ascii=False, indent=1))
        return {"cutoff": cut, "cards": len(before), "drafts": n, "kept": len(kept), "reviewer": reviewer}

    with cf.ThreadPoolExecutor(4) as ex:
        for res in ex.map(lambda c: _safe(one, c), a.cutoffs.split(",")):
            print(json.dumps(res, ensure_ascii=False))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("cards")
    sub.add_parser("weekly")
    sub.add_parser("pending")
    for name in ("confirm", "reject"):
        p = sub.add_parser(name)
        p.add_argument("nums")
        p.add_argument("--note", default="")
    p = sub.add_parser("sim")
    p.add_argument("--cutoffs", required=True)
    a = ap.parse_args()
    {"cards": cmd_cards, "weekly": cmd_weekly, "pending": lambda _: show_pending(),
     "confirm": lambda x: decide(x, "已确认"), "reject": lambda x: decide(x, "否掉"), "sim": cmd_sim}[a.cmd](a)


if __name__ == "__main__":
    main()
