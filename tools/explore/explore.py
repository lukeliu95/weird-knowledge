#!/usr/bin/env python3
"""探索循环：选方向、收候选、打分、出日报、记回答。方案见 docs/2026-10-19-explore-loop-spec.md。

确定的事在这里用代码做；去网上找内容交给侦察兵 subagent（tools/explore/SCOUT.md），判断新方向交给主会话。
数据都在 private/explore/：兴趣地图和打分是对 Luke 的画像，不进公开仓库。

用法：
  explore.py init                      读 interests.md，建或更新 arms.json（保留已有计数）
  explore.py status                    状态 JSON：候选池、没答的日报、要不要降速
  explore.py pick [--n 3]              抽签选这一轮的方向和侦察兵，给每个侦察兵写一份任务段落
  explore.py ingest <round>            收 inbox/<round>-*.json：去重、进候选池、记线索
  explore.py score [--limit 300]       给没打分的候选打分：Jev 分类（只发公开内容）、本地 Qwen 打"想不想看"
  explore.py digest [--size 10]        出一份日报：6 条最可能想看 + 2 条最拿不准 + 2 条新方向，顺序打乱
  explore.py learn <digest> <letters>  记 Luke 的回答：letters 是想看的字母，如 ACF；都不想看写 -
  explore.py report                    命中率：按槽位、方向、侦察兵；预测器在这些回答上的成绩
"""
import argparse, collections, datetime as dt, json, random, re, sys, urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
DIR = REPO / "private" / "explore"
sys.path.insert(0, str(REPO / "tools" / "evolve"))
import l1_eval as E  # noqa: E402

ARMS, POOL, LEADS, ROUNDS, LABELS = (DIR / n for n in ("arms.json", "pool.jsonl", "leads.jsonl", "rounds.jsonl", "labels.jsonl"))
SCOUTS = ("x", "paper", "community", "ja")
THROTTLE_UNANSWERED = 4   # 没答的日报到这个数（方案 B 每天 2 份，约 2 天），就停派侦察兵
MAX_UNANSWERED = 3        # 没答的日报到这个数，就不再出新日报，免得越堆越多
POOL_CAP = 500            # 没展示过的候选到这个数，就先停找


def now():
    return dt.datetime.now()


def read_jsonl(p):
    # 推文里有 U+2028 这类字符，按 \n 切，不用 splitlines
    return [json.loads(l) for l in p.read_text().split("\n") if l.strip()] if p.exists() else []


def write_jsonl(p, rows):
    p.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))


def append_jsonl(p, row):
    with open(p, "a") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


# ---------- 去重用的键 ----------
def key_of(url):
    url = (url or "").strip()
    m = re.search(r"(?:x|twitter)\.com/[^/]+/(?:status|article)/(\d+)", url)
    if m:
        return "x:" + m.group(1)
    m = re.search(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", url)
    if m:
        return "arxiv:" + m.group(1)
    u = urllib.parse.urlsplit(url)
    q = [(k, v) for k, v in urllib.parse.parse_qsl(u.query) if not k.lower().startswith("utm_") and k.lower() not in ("ref", "ref_src", "source", "s", "t")]
    host = u.netloc.lower().removeprefix("www.")
    return "url:" + host + u.path.rstrip("/") + ("?" + urllib.parse.urlencode(q) if q else "")


def known_keys():
    keys = set()
    for f in (REPO / "clips").glob("*.md"):
        m = re.search(r"^url:\s*(\S+)", f.read_text().split("\n---", 1)[0], re.M)
        if m:
            keys.add(key_of(m.group(1)))
    keys |= {r["key"] for r in read_jsonl(POOL)}
    skip = REPO / ".skip_ids"
    if skip.exists():
        keys |= {"x:" + l.strip() for l in skip.read_text().split("\n") if l.strip()}
    return keys


# ---------- 兴趣地图 ----------
def parse_interests():
    rows = []
    for line in (DIR / "interests.md").read_text().split("\n"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 6 and cells[1] in ("core", "adjacent"):
            rows.append(dict(id=cells[0], group=cells[1], name=cells[2], desc=cells[3],
                             keywords=[k.strip() for k in cells[4].split(";") if k.strip()],
                             scouts=[s.strip() for s in cells[5].split(",") if s.strip() in SCOUTS]))
    return rows


def load_arms():
    return json.loads(ARMS.read_text())


def save_arms(a):
    ARMS.write_text(json.dumps(a, ensure_ascii=False, indent=1))


def cmd_init(_):
    old = load_arms() if ARMS.exists() else {"directions": {}, "scouts": {}}
    arms = {"directions": {}, "scouts": {s: old["scouts"].get(s, {"shown": 0, "hit": 0}) for s in SCOUTS}}
    for d in parse_interests():
        c = old["directions"].get(d["id"], {})
        arms["directions"][d["id"]] = {**d, "shown": c.get("shown", 0), "hit": c.get("hit", 0),
                                       "added": c.get("added", now().strftime("%Y-%m-%d"))}
    gone = set(old["directions"]) - set(arms["directions"])
    for g in gone:   # 从地图上删掉的方向，计数留着备查
        arms.setdefault("retired", {})[g] = old["directions"][g]
    save_arms(arms)
    print(f"兴趣地图：{len(arms['directions'])} 个方向" + (f"，退役 {len(gone)} 个" if gone else ""))


def draw(arm, rng):
    return rng.betavariate(arm["hit"] + 1, arm["shown"] - arm["hit"] + 1)


def top_authors(n=15):
    c = collections.Counter()
    for f in (REPO / "clips").glob("*.md"):
        m = re.search(r'^author:.*\(@([A-Za-z0-9_]+)\)', f.read_text().split("\n---", 1)[0], re.M)
        if m:
            c[m.group(1)] += 1
    return [a for a, _ in c.most_common(n)]


def cmd_pick(a):
    arms, rng = load_arms(), random.Random()
    rid = now().strftime("%Y%m%d-%H%M")
    groups = ["core"] * (a.n - 1) + ["adjacent"]
    chosen, used_x = [], False
    for g in groups:
        pool = [(draw(d, rng), k) for k, d in arms["directions"].items() if d["group"] == g and k not in {c["direction"] for c in chosen}]
        if not pool:
            continue
        _, did = max(pool)
        d = arms["directions"][did]
        options = [s for s in d["scouts"] if not (s == "x" and used_x)] or [s for s in d["scouts"] if s != "x"] or ["community"]
        scout = max(options, key=lambda s: draw(arms["scouts"][s], rng))
        used_x |= scout == "x"
        chosen.append(dict(slot=g, direction=did, scout=scout))
    since = (now() - dt.timedelta(days=30)).strftime("%Y-%m-%d")
    for i, c in enumerate(chosen, 1):
        d = arms["directions"][c["direction"]]
        c["out"] = str(DIR / "inbox" / f"{rid}-{i}.json")
        c["brief"] = str(DIR / "inbox" / f"{rid}-{i}.brief.md")
        lines = [f"# 这一轮的任务（{rid} 第 {i} 个侦察兵）", "",
                 f"- 轮次 round：{rid}", f"- 方向 direction：{c['direction']}（{d['name']}）", f"- 方向说明：{d['desc']}",
                 f"- 可以用的关键词（自己再扩展）：{'; '.join(d['keywords'])}",
                 f"- 侦察兵 scout：{c['scout']}", f"- 优先这个日期之后的内容：{since}",
                 f"- 输出文件 out：{c['out']}"]
        reader = DIR / "reader.md"
        if reader.exists():
            lines.append(f"- 读者：{reader.read_text().strip()}")
        if c["scout"] == "x":
            lines.append(f"- 他常看的作者（可以 from: 搜，也可以看他们最近在聊什么）：{', '.join('@' + x for x in top_authors())}")
        if c["slot"] == "adjacent":
            lines.append("- 这是一个新方向：他以前很少看。找这个领域里最容易让一个 AI 产品人眼前一亮的入门级好东西，不要太偏门")
        Path(c["brief"]).write_text("\n".join(lines) + "\n")
    append_jsonl(ROUNDS, {"round": rid, "at": now().isoformat(timespec="seconds"), "plan": chosen})
    print(json.dumps({"round": rid, "scouts": chosen}, ensure_ascii=False, indent=1))


# ---------- 收候选 ----------
def cmd_ingest(a):
    keys = known_keys()
    pool = read_jsonl(POOL)
    added = dup = bad = nleads = 0
    notes = []
    for f in sorted((DIR / "inbox").glob(f"{a.round}-*.json")):
        try:
            d = json.loads(f.read_text())
        except Exception as e:
            bad += 1
            notes.append(f"{f.name} 读不了：{e}")
            continue
        for it in d.get("items", []):
            if not it.get("url"):
                bad += 1
                continue
            k = key_of(it["url"])
            if k in keys:
                dup += 1
                continue
            keys.add(k)
            pool.append(dict(key=k, url=it["url"], title=it.get("title", ""), author=it.get("author", ""),
                             published=it.get("published", ""), source=it.get("source", ""), snippet=it.get("snippet", "")[:1200],
                             what=it.get("what", ""), why=it.get("why", ""), direction=d.get("direction", ""),
                             scout=d.get("scout", ""), round=a.round, found=now().isoformat(timespec="seconds"), status="new"))
            added += 1
        for l in d.get("leads", []):
            append_jsonl(LEADS, {**l, "round": a.round, "direction": d.get("direction", "")})
            nleads += 1
        if d.get("notes"):
            notes.append(f"{d.get('scout')}: {d['notes']}")
    write_jsonl(POOL, pool)
    rec = {"round": a.round, "ingested": added, "dup": dup, "bad": bad, "leads": nleads, "notes": notes}
    append_jsonl(ROUNDS, {"round": a.round, "at": now().isoformat(timespec="seconds"), "ingest": rec})
    print(json.dumps(rec, ensure_ascii=False))


# ---------- 打分 ----------
SYS = "你在模拟一个具体的人：Luke。判断他看到这条内容时，会不会想点开看、会不会点赞或收藏。只回答一个字母：A 表示想看，B 表示不想看。"


def positives():
    """点赞过的、在探索日报里说想看的：都当"他喜欢的例子"。"""
    docs = E.liked_docs(set())
    docs += [{"id": r["key"], "text": (r.get("title", "") + "\n" + r.get("text", ""))[:600]} for r in read_jsonl(LABELS) if r["label"] == 1]
    return docs


def explore_prompt(r, profile, examples):
    return "\n\n".join([
        "【Luke 的档案】\n" + profile,
        "【他以前点赞过、说想看的相似内容】\n" + "\n\n".join(f"- {e['text'][:400]}" for e in examples),
        f"【要判断的内容】来源：{r['source']}　作者：{r['author']}\n标题：{r['title']}\n{r['snippet'][:1200]}\n（一句话说明：{r['what']}）",
        "Luke 会想看这条吗？A 想看，B 不想看。只回答一个字母。"])


def qwen_p(text):
    d = E.post(E.os.environ["QWEN_BASE_URL"] + "/chat/completions", {
        "model": "qwen3.8-27b-coder390-mlx-mixed4-mtp",
        "messages": [{"role": "system", "content": SYS}, {"role": "user", "content": text}],
        "max_tokens": 1, "temperature": 0, "logprobs": True, "top_logprobs": 10,
        "chat_template_kwargs": {"enable_thinking": False}}, E.os.environ["QWEN_API_KEY"])
    p = collections.defaultdict(float)
    for t in d["choices"][0]["logprobs"]["content"][0]["top_logprobs"]:
        k = t["token"].strip().upper()
        if k in ("A", "B"):
            p[k] += E.math.exp(t["logprob"])
    a_, b_ = p["A"] or 1e-6, p["B"] or 1e-6
    return round(a_ / (a_ + b_), 4)


def cmd_score(a):
    E.load_env()
    import jev_classify as JC
    pool = read_jsonl(POOL)
    todo = [r for r in pool if r["status"] == "new" and "p" not in r][: a.limit]
    if not todo:
        print("没有要打分的候选")
        return
    champ = json.loads((E.PRIVATE / "l1" / "champion.json").read_text())
    profile = (E.PRIVATE / "luke" / champ["profile"]).read_text()
    index = E.Index(positives())
    jev_tokens = fails = 0
    for i, r in enumerate(todo, 1):
        text = f"{r['title']}\n{r['snippet']}"
        if "kind" not in r:
            try:   # 只发公开内容：作者和原文片段
                j = JC.ask(r["author"], text)
                r.update(kind=j["kind"], kind_conf=j["kind_conf"], topic=j["topic"], topic_conf=j["topic_conf"])
                jev_tokens += j["tokens"]
            except Exception:
                pass
        try:
            r["p"] = qwen_p(explore_prompt(r, profile, index.top(text, champ.get("k", 8))))
            r["scored"] = now().isoformat(timespec="seconds")
        except Exception as e:
            fails += 1
            if fails >= 3:
                print(f"本地 Qwen 连续出错，先停：{e}", file=sys.stderr)
                break
        if i % 25 == 0:
            print(f"  {i}/{len(todo)}", file=sys.stderr, flush=True)
            write_jsonl(POOL, pool)
    write_jsonl(POOL, pool)
    n = sum("p" in r for r in todo)
    print(f"打分 {n}/{len(todo)} 条；Jev 输入 {jev_tokens} token，约 {jev_tokens / 1e6 * 0.042:.4f} 美元")


# ---------- 日报 ----------
def digests():
    return [json.loads(f.read_text()) for f in sorted((DIR / "digests").glob("*.json")) if not f.name.endswith(".page.json")]


def cmd_digest(a):
    open_ = [d for d in digests() if not d.get("answered")]
    if len(open_) >= MAX_UNANSWERED:
        print(json.dumps({"skipped": True, "reason": f"还有 {len(open_)} 份日报没答", "open": [d["stamp"] for d in open_]}, ensure_ascii=False))
        return
    arms = load_arms()
    pool = read_jsonl(POOL)
    cand = [r for r in pool if r["status"] == "new" and "p" in r]
    picked = []

    def take(rows, n, slot, cap=2):
        # cap：同一个方向在这个槽位里最多几条；整份日报里同一方向最多 4 条
        for r in rows:
            if sum(1 for p in picked if p["slot"] == slot) >= n:
                break
            same = [p for p in picked if p["row"]["direction"] == r["direction"]]
            if any(p["row"] is r for p in picked) or sum(p["slot"] == slot for p in same) >= cap or len(same) >= 4:
                continue
            picked.append({"row": r, "slot": slot})

    n_top = a.size - 4
    take(sorted(cand, key=lambda r: -r["p"]), n_top, "top")
    take(sorted(cand, key=lambda r: abs(r["p"] - 0.5)), 2, "uncertain", cap=1)
    adj = [r for r in cand if arms["directions"].get(r["direction"], {}).get("group") == "adjacent"]
    take(sorted(adj, key=lambda r: -r["p"]), 2, "new", cap=1)
    if len(picked) < a.size:   # 某一类不够，就用预测分最高的补齐
        take(sorted(cand, key=lambda r: -r["p"]), sum(p["slot"] == "top" for p in picked) + a.size - len(picked), "top", cap=3)
    if not picked:
        print(json.dumps({"skipped": True, "reason": "候选池里没有打过分的新候选"}, ensure_ascii=False))
        return
    random.shuffle(picked)
    stamp = now().strftime("%Y%m%d-%H%M")
    items = []
    for letter, p in zip("ABCDEFGHIJKLMNOPQRST", picked):
        r = p["row"]
        r["status"], r["digest"] = "shown", stamp
        items.append(dict(letter=letter, key=r["key"], slot=p["slot"], direction=r["direction"],
                          direction_name=arms["directions"].get(r["direction"], {}).get("name", r["direction"]),
                          scout=r["scout"], p=r["p"], url=r["url"], title=r["title"], author=r["author"],
                          source=r["source"], published=r["published"], what=r["what"], why=r["why"],
                          kind=r.get("kind", ""), topic=r.get("topic", "")))
    d = {"stamp": stamp, "created": now().isoformat(timespec="seconds"), "answered": False, "items": items}
    (DIR / "digests" / f"{stamp}.json").write_text(json.dumps(d, ensure_ascii=False, indent=1))
    write_jsonl(POOL, pool)
    md = [f"# lukee 日报 {stamp}", "", "想看哪几条？回字母就行（例：ACF；都不想看回 -）。", ""]
    for it in items:
        md += [f"**{it['letter']}. {it['title']}**", f"{it['what']}", f"{it['source']} · {it['author']} · {it['published'] or '日期未知'} · {it['url']}", ""]
    (DIR / "digests" / f"{stamp}.md").write_text("\n".join(md))
    # 给日报网页的数据库文档：不放预测分和方向，免得影响 Luke 的判断
    page = {"stamp": stamp, "created": d["created"],
            "items": [{k: it[k] for k in ("letter", "slot", "url", "title", "author", "source", "published", "what")} for it in items]}
    (DIR / "digests" / f"{stamp}.page.json").write_text(json.dumps(page, ensure_ascii=False))
    print("\n".join(md))
    print(f"\n网页数据：{DIR / 'digests' / f'{stamp}.page.json'}（ArtifactData set，collection digests，doc_id {stamp}）")


# ---------- 记回答 ----------
def cmd_learn(a):
    f = DIR / "digests" / f"{a.digest}.json"
    d = json.loads(f.read_text())
    if d.get("answered"):
        sys.exit(f"日报 {a.digest} 已经记过回答了")
    want = set() if a.letters.strip() == "-" else set(a.letters.strip().upper())
    letters = {it["letter"] for it in d["items"]}
    if want - letters:
        sys.exit(f"日报里没有这些字母：{''.join(sorted(want - letters))}")
    arms = load_arms()
    pool = {r["key"]: r for r in read_jsonl(POOL)}
    at = now().isoformat(timespec="seconds")
    wanted = []
    for it in d["items"]:
        y = int(it["letter"] in want)
        it["label"] = y
        for grp, k in (("directions", it["direction"]), ("scouts", it["scout"])):
            if k in arms[grp]:
                arms[grp][k]["shown"] += 1
                arms[grp][k]["hit"] += y
        r = pool.get(it["key"], {})
        r.update(status="answered", label=y)
        append_jsonl(LABELS, dict(key=it["key"], url=it["url"], label=y, slot=it["slot"], direction=it["direction"],
                                  scout=it["scout"], p=it["p"], digest=a.digest, at=at, title=it["title"],
                                  text=r.get("snippet", "")[:600]))
        if it["key"].startswith("x:"):   # 推文的回答也是点赞预测（L1）最强的标签
            append_jsonl(E.PRIVATE / "l1" / "labels.jsonl", {"id": it["key"][2:], "author": it["author"].lstrip("@"),
                                                              "text": r.get("snippet", ""), "label": y,
                                                              "source": f"explore-{a.digest}", "asked_p": it["p"]})
        if y:
            wanted.append({k: it[k] for k in ("letter", "url", "title", "author", "source", "published", "what", "direction")})
    d.update(answered=True, answered_at=at, answer=a.letters)
    f.write_text(json.dumps(d, ensure_ascii=False, indent=1))
    write_jsonl(POOL, list(pool.values()))
    save_arms(arms)
    promote = [k for k, v in arms["directions"].items() if v["group"] == "adjacent" and v["hit"] >= 3]
    print(json.dumps({"wanted": wanted, "hit": f"{len(want)}/{len(d['items'])}",
                      "promote_to_core": promote}, ensure_ascii=False, indent=1))


# ---------- 状态和报告 ----------
def cmd_status(_):
    pool = read_jsonl(POOL)
    ds = digests()
    open_ = [x["stamp"] for x in ds if not x.get("answered")]
    last = max((x.get("answered_at", "") for x in ds), default="")
    new = [r for r in pool if r["status"] == "new"]
    throttle = len(open_) >= THROTTLE_UNANSWERED or len(new) >= POOL_CAP
    rounds = read_jsonl(ROUNDS)
    picks = [r for r in rounds if "plan" in r]
    done = {r["round"] for r in rounds if "ingest" in r}
    busy = bool(picks) and picks[-1]["round"] not in done and \
        now() - dt.datetime.fromisoformat(picks[-1]["at"]) < dt.timedelta(minutes=50)
    print(json.dumps({"busy": busy, "pool_new": len(new), "pool_unscored": sum("p" not in r for r in new), "pool_total": len(pool),
                      "digests": len(ds), "unanswered": open_, "last_answer": last, "labels": len(read_jsonl(LABELS)),
                      "throttle": throttle,
                      "why": ("没答的日报太多" if len(open_) >= THROTTLE_UNANSWERED else "候选池满了" if len(new) >= POOL_CAP else "")},
                     ensure_ascii=False))


def rate(rows):
    return f"{sum(r['label'] for r in rows)}/{len(rows)}（{sum(r['label'] for r in rows) / len(rows):.0%}）" if rows else "无"


def cmd_report(_):
    rows = read_jsonl(LABELS)
    print(f"回答 {len(rows)} 条，想看 {rate(rows)}")
    for field in ("slot", "direction", "scout"):
        g = collections.defaultdict(list)
        for r in rows:
            g[r[field]].append(r)
        print(f"\n按 {field}：")
        for k, v in sorted(g.items(), key=lambda kv: -len(kv[1])):
            print(f"  {k}: {rate(v)}")
    if rows and 0 < sum(r["label"] for r in rows) < len(rows):
        m = E.metrics([{"p": r["p"], "label": r["label"]} for r in rows])
        print(f"\n预测器在这些回答上：AUC {m['auc']}，准确率 {m['acc']}，校准误差 {m['ece']}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init")
    sub.add_parser("status")
    p = sub.add_parser("pick"); p.add_argument("--n", type=int, default=3)
    p = sub.add_parser("ingest"); p.add_argument("round")
    p = sub.add_parser("score"); p.add_argument("--limit", type=int, default=300)
    p = sub.add_parser("digest"); p.add_argument("--size", type=int, default=10)
    p = sub.add_parser("learn"); p.add_argument("digest"); p.add_argument("letters")
    sub.add_parser("report")
    a = ap.parse_args()
    DIR.mkdir(parents=True, exist_ok=True)
    (DIR / "inbox").mkdir(exist_ok=True)
    (DIR / "digests").mkdir(exist_ok=True)
    globals()["cmd_" + a.cmd](a)


if __name__ == "__main__":
    main()
