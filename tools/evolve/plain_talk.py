#!/usr/bin/env python3
"""讲人话测试：从论文 Clark 等 2026（AI 写的话为什么难懂）提炼的 6 条写法，加进全局规则前先测有没有用。

Luke 2026-10-27 选了 B：用 20 段真实汇报测，他盲选 10 对，8 对以上选新版才写进全局规则。
做法：从本机会话记录里挑 20 段写给 Luke 的汇报 → 去掉人名、公司名 → 同样内容各重写两遍：
对照组只给现在的说话规矩（全局规则第 2 节），新版再加 6 条 → 数 6 类难读句式、核对有没有丢事实 →
挑 10 对两边都没丢事实的，打乱左右给 Luke 盲选。只比"加没加 6 条"，不拿原文比，免得"重写本身"抢了功劳。
数据只放 private/plain-talk/（汇报里有同事和客户的事），只交给 Opus。方案和结果见 docs/2026-10-27-plain-talk-test.md。

用法：
  plain_talk.py pick [--n 20] [--days 14]   挑汇报
  plain_talk.py run                          去名、重写、数句式、核事实（只做还没做的）
  plain_talk.py pairs [--n 10]               挑 10 对、打乱左右，写出给盲选页面用的 pairs.json
  plain_talk.py score <答案 JSON>            对答案：新版被选中几对，句式少了多少
  plain_talk.py claims [--runs 2]            第二个测试：现规则 vs 加一句"不替原文下结论"，各重写 2 遍，核对谁加的结论多
  plain_talk.py claims-report                只重算第二个测试的数和判定
"""
import argparse, collections, concurrent.futures as cf, datetime as dt, json, random, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import l1_eval as E  # noqa: E402
import opus_judge as OJ  # noqa: E402

DIR = E.PRIVATE / "plain-talk"
SAMPLES, RESULTS = DIR / "samples.jsonl", DIR / "results.jsonl"
PROJECTS = Path.home() / ".claude" / "projects"
SKIP = ("lukee-lark-memory", "codex-worktrees", "salesroom-backfill")   # 别的 agent 驱动的会话，读者不是 Luke

NEW_RULES = """**写法**（从 Clark 等 2026 年的论文提炼：模型为了省字，常用人读着费劲的句式）
- 短，是少说几件事，不是把一句话压紧。"的、把、因为、所以、也就是"这类词该有就有
- 三个以上的名词不连着写："口味 skill 冠军配置"写成"现在用来猜你口味的那一版说明"
- 名词不当动词用：不写"PR 一下""闭环它"，写"开一个 PR""把这一步接回流程里"
- 不拟人：不写"这个坑会咬人"，写"这里容易出错"
- 修饰语长了就拆句：不写"被你上周否掉的那个要花钱的方案"，写"那个方案要花钱，你上周否掉了"
- 自己起的名字少用；非用不可，第一次出现时用一句话说它是什么"""

FEATURES = {
    "omit": "省掉连接的词：该用\"的、把、因为、所以、但是、也就是\"把意思连起来却省掉了，读者要自己补（如\"回测没掉才默认开\"）",
    "stack": "名词堆叠：三个及以上名词（含英文词）直接连在一起，中间没有\"的\"或动词（如\"口味 skill 冠军配置\"）",
    "verb": "名词当动词：把名词或英文名词当动作用（如\"PR 一下\"\"闭环它\"\"日历一下\"）",
    "animate": "拟人：没有生命的东西做只有人或动物才做的事（如\"这个坑会咬人\"\"数据在说话\"）",
    "long": "长修饰：一个名词前面的修饰语超过 15 个字左右，或者主语和它的动词之间隔了 15 个字以上",
    "coined": "生造词：作者自己起的名字或少见的搭配，第一次出现时没有解释（如\"按周模拟提炼\"\"案例卡\"）",
}


def rules_now():
    t = (Path.home() / ".claude" / "CLAUDE.md").read_text()
    return t.split("\n## 2. ", 1)[1].split("\n## 3. ", 1)[0]


def text_of(content):
    if isinstance(content, str):
        return content
    return "\n".join(b.get("text", "") for b in content or [] if isinstance(b, dict) and b.get("type") == "text")


def cmd_pick(a):
    """每段汇报 = Luke 下一次开口之前，助手最后写的那段文字。"""
    since = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=a.days)).isoformat()
    cands = []
    for f in PROJECTS.glob("*/*.jsonl"):
        if any(s in f.parent.name for s in SKIP) or f.stat().st_size < 20000:
            continue
        last = None
        for line in f.open():
            try:
                r = json.loads(line)
            except ValueError:
                continue
            if r.get("isSidechain"):
                continue
            if r.get("type") == "assistant":
                t = text_of((r.get("message") or {}).get("content"))
                if t.strip():
                    last = (t.strip(), r.get("timestamp", ""))
            elif r.get("type") == "user" and r.get("turnOrigin") == "human":
                t = text_of((r.get("message") or {}).get("content"))
                if last and t.strip() and not t.lstrip().startswith("<") and last[1] >= since:
                    body = last[0]
                    zh = len(re.findall(r"[一-鿿]", body))
                    if 300 <= len(body) <= 1800 and zh / len(body) > 0.35 and "```" not in body:
                        cands.append({"id": f"{f.stem[:8]}-{len(cands)}", "project": f.parent.name, "ts": last[1], "text": body})
                last = None
    rnd = random.Random(20261027)
    rnd.shuffle(cands)
    picked, per_proj, per_sess = [], collections.Counter(), set()
    for c in cands:
        sess = c["id"].split("-")[0]
        if per_proj[c["project"]] < 4 and sess not in per_sess:
            picked.append(c)
            per_proj[c["project"]] += 1
            per_sess.add(sess)
        if len(picked) >= a.n:
            break
    DIR.mkdir(parents=True, exist_ok=True)
    E_write(SAMPLES, picked)
    print(json.dumps({"candidates": len(cands), "picked": len(picked), "projects": dict(per_proj)}, ensure_ascii=False))


def E_write(p, rows):
    p.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))


def read(p):
    return [json.loads(l) for l in p.read_text().split("\n") if l.strip()] if p.exists() else []


def scrub(text):
    return OJ.ask_json("你在给一段文字去掉真名，只输出一个 JSON 对象。",
                       "把下面这段文字里的人名换成\"某同事\"（Luke 本人和\"你\"不换），客户和合作方的公司名换成\"某客户\"\"某合作方\"。"
                       "其余一个字都不要改，格式、标点、表格、英文都照原样。\n只输出 JSON：{\"text\": \"…\"}\n\n" + text)["text"]


def rewrite(text, rules):
    return OJ.ask_json("你在给 Luke 写汇报，只输出一个 JSON 对象。",
                       f"【和 Luke 说话的规矩】\n{rules}\n\n下面是一段已经写好的、给 Luke 的汇报。请按上面的规矩重写一遍："
                       "事实、数字、结论、要他做的决定都不能变，不能删掉信息，也不能加新信息；格式（表格、列表、分段）可以改。\n"
                       "只输出 JSON：{\"text\": \"重写后的汇报\"}\n\n" + text)["text"]


def count(texts):
    """数难读句式。几段一起交给同一次判断，不告诉它哪段是哪个版本。"""
    defs = "\n".join(f"- {k}：{v}" for k, v in FEATURES.items())
    keys = {f"T{i}": k for i, k in enumerate(texts, 1)}
    body = "\n\n".join(f"===== {t} =====\n{texts[k]}" for t, k in keys.items())
    out = OJ.ask_json("你是中文可读性审校员，只输出一个 JSON 对象。",
                      f"下面有 {len(keys)} 篇文字，用 ===== T1 ===== 这样的标记分开。逐篇找出下面这几类难读的写法，"
                      f"每处都摘出原文片段（10～30 字），全部列出，拿不准的不算。\n{defs}\n\n"
                      '只输出 JSON，键是篇号：{"T1": {"omit": ["片段"], "stack": [], "verb": [], "animate": [], "long": [], "coined": []}}\n\n'
                      + body)
    res = {}
    for t, k in keys.items():
        v = out.get(t)
        if isinstance(v, dict):
            res[k] = {f: len(v.get(f) or []) for f in FEATURES} | {"examples": {f: v.get(f) or [] for f in FEATURES}}
    return res


def check(src, a, b):
    out = OJ.ask_json("你在核对改写有没有走样，只输出一个 JSON 对象。",
                      "下面是原文和两个改写版本。分别判断两个版本有没有丢掉、改错原文里的事实、数字、结论、要读者做的决定，或者加了原文没有的内容。"
                      "措辞、格式、顺序的变化不算。\n"
                      '只输出 JSON：{"X_ok": true, "X_issues": ["…"], "Y_ok": true, "Y_issues": ["…"]}\n\n'
                      f"【原文】\n{src}\n\n【版本 X】\n{a}\n\n【版本 Y】\n{b}")
    return out


def one(s, now_rules):
    src = scrub(s["text"])
    ctrl = rewrite(src, now_rules)
    new = rewrite(src, now_rules + "\n\n" + NEW_RULES)
    ck = check(src, ctrl, new)
    return {"id": s["id"], "project": s["project"], "source": src, "control": ctrl, "new": new,
            "control_ok": bool(ck.get("X_ok")), "new_ok": bool(ck.get("Y_ok")),
            "control_issues": ck.get("X_issues", []), "new_issues": ck.get("Y_issues", [])}


def cmd_run(_):
    E.load_env()
    done = {r["id"] for r in read(RESULTS)}
    todo = [s for s in read(SAMPLES) if s["id"] not in done]
    now_rules = rules_now()
    with cf.ThreadPoolExecutor(4) as ex:
        futs = {ex.submit(one, s, now_rules): s["id"] for s in todo}
        for fu in cf.as_completed(futs):
            try:
                r = fu.result()
            except Exception as e:
                print(f"  {futs[fu]} 出错：{e}", file=sys.stderr)
                continue
            with open(RESULTS, "a") as f:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    # 数句式：三个版本打乱后每 3 段一起数
    rows = read(RESULTS)
    items = [(f"{r['id']}|{v}", r[v]) for r in rows if "counts" not in r for v in ("source", "control", "new")]
    random.Random(7).shuffle(items)
    batches = [dict(items[i:i + 3]) for i in range(0, len(items), 3)]
    got = {}
    with cf.ThreadPoolExecutor(4) as ex:
        for res in ex.map(lambda b: _safe(count, b), batches):
            got.update(res or {})
    for r in rows:
        if "counts" not in r:
            c = {v: got.get(f"{r['id']}|{v}") for v in ("source", "control", "new")}
            if all(c.values()):
                r["counts"] = c
    E_write(RESULTS, rows)
    print(summary(rows))


def _safe(fn, *args):
    try:
        return fn(*args)
    except Exception as e:
        print(f"  出错：{e}", file=sys.stderr)


def rate(c, text):
    """每 1000 字出现几次。"""
    return sum(int(c.get(k, 0) or 0) for k in FEATURES) * 1000 / max(len(text), 1)


def summary(rows):
    ok = [r for r in rows if r.get("counts")]
    out = {"samples": len(rows), "counted": len(ok),
           "facts_ok": {"control": sum(r["control_ok"] for r in rows), "new": sum(r["new_ok"] for r in rows)}}
    for v in ("source", "control", "new"):
        out[f"per_1000_chars_{v}"] = round(sum(rate(r["counts"][v], r[v]) for r in ok) / max(len(ok), 1), 2)
        out[f"by_feature_{v}"] = {k: sum(int(r["counts"][v].get(k, 0) or 0) for r in ok) for k in FEATURES}
        out[f"chars_{v}"] = round(sum(len(r[v]) for r in ok) / max(len(ok), 1))
    return json.dumps(out, ensure_ascii=False, indent=1)


def cmd_pairs(a):
    rows = [r for r in read(RESULTS) if r["control_ok"] and r["new_ok"]]
    rnd = random.Random(1027)
    rnd.shuffle(rows)
    pairs, key = [], {}
    sides = [True] * (a.n // 2) + [False] * (a.n - a.n // 2)   # 新版左右各一半，免得 Luke 看出位置规律
    rnd.shuffle(sides)
    for i, (r, new_left) in enumerate(zip(rows[:a.n], sides), 1):
        pairs.append({"n": i, "left": r["new"] if new_left else r["control"], "right": r["control"] if new_left else r["new"]})
        key[str(i)] = {"id": r["id"], "new": "left" if new_left else "right"}
    (DIR / "pairs.json").write_text(json.dumps(pairs, ensure_ascii=False, indent=1))
    (DIR / "key.json").write_text(json.dumps(key, ensure_ascii=False, indent=1))
    print(json.dumps({"valid": len(rows), "pairs": len(pairs), "new_on_left": sum(v["new"] == "left" for v in key.values())}))


def cmd_score(a):
    ans = json.loads(Path(a.answers).read_text())   # {"1": "left", "2": "right", ...}
    key = json.loads((DIR / "key.json").read_text())
    picks = {n: ans.get(n) for n in key}
    new = sum(picks[n] == key[n]["new"] for n in key)
    answered = sum(bool(v) for v in picks.values())
    res = {"answered": answered, "picked_new": new, "pass": new >= 8, "detail": {n: (picks[n], key[n]["new"]) for n in key}}
    (DIR / "score.json").write_text(json.dumps(res, ensure_ascii=False, indent=1))
    print(json.dumps(res, ensure_ascii=False))


# ---- 第二个测试：加一句"原文和证据没说的结论，不替它下"，看加结论的毛病少不少（Luke 2026-10-27 选了单独测）----
CLAIMS = DIR / "claims.jsonl"
NUM_RULE = '给数字时接着说"这意味着什么"。'
NO_CLAIM = "原文和证据没说的结论，不替它下。"
KINDS = ("加结论", "改错意思", "丢了内容", "加了别的内容")


def check_typed(src, a, b):
    out = OJ.ask_json("你在核对改写有没有走样，只输出一个 JSON 对象。",
                      "下面是原文和两个改写版本。分别列出每个版本相对原文的每一处走样，并标类型：\n"
                      "- 加结论：替原文下了它没下的判断、推论或推荐，或者把话说重、说满（如把\"测试通过\"说成\"能正常用\"，把转述说成已确认的事实）\n"
                      "- 改错意思：事实、数字、对象、范围被改错\n"
                      "- 丢了内容：原文的事实、数字、结论、要读者做的决定被删掉\n"
                      "- 加了别的内容：加了原文没有的解释、理由、选项等，但不是结论\n"
                      "措辞、格式、顺序的变化不算。不影响事实和决定的小出入标 minor: true。ok 表示这个版本整体没走样。\n"
                      '只输出 JSON：{"X_ok": true, "X_issues": [{"type": "加结论", "minor": false, "what": "…"}], "Y_ok": true, "Y_issues": []}\n\n'
                      f"【原文】\n{src}\n\n【版本 X】\n{a}\n\n【版本 Y】\n{b}")
    return out


def claims_one(r, run, now_rules, fix_rules, x_is_now):
    now, fix = rewrite(r["source"], now_rules), rewrite(r["source"], fix_rules)
    x, y = (now, fix) if x_is_now else (fix, now)
    ck = check_typed(r["source"], x, y)
    side = {"now": "X" if x_is_now else "Y", "fix": "Y" if x_is_now else "X"}
    row = {"id": r["id"], "run": run, "x_is": "now" if x_is_now else "fix"}
    for arm, text in (("now", now), ("fix", fix)):
        row[arm] = {"text": text, "ok": bool(ck.get(f"{side[arm]}_ok")), "issues": ck.get(f"{side[arm]}_issues") or []}
    return row


def cmd_claims(a):
    E.load_env()
    now_rules = rules_now()
    assert NUM_RULE in now_rules, "全局规则里找不到要改的那一句"
    fix_rules = now_rules.replace(NUM_RULE, NUM_RULE + NO_CLAIM, 1)
    done = {(r["id"], r["run"]) for r in read(CLAIMS)}
    rnd = random.Random(2610271)
    todo = [(r, run, rnd.random() < 0.5) for run in range(1, a.runs + 1) for r in read(RESULTS)]
    todo = [t for t in todo if (t[0]["id"], t[1]) not in done]
    with cf.ThreadPoolExecutor(4) as ex:
        futs = {ex.submit(claims_one, r, run, now_rules, fix_rules, xn): (r["id"], run) for r, run, xn in todo}
        for fu in cf.as_completed(futs):
            try:
                row = fu.result()
            except Exception as e:
                print(f"  {futs[fu]} 出错：{e}", file=sys.stderr)
                continue
            with open(CLAIMS, "a") as f:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
    cmd_claims_report(a)


def _has(issues, kind):
    return any(isinstance(i, dict) and i.get("type") == kind and not i.get("minor") for i in issues)


def cmd_claims_report(_):
    rows = read(CLAIMS)
    st = {}
    for arm in ("now", "fix"):
        xs = [r[arm] for r in rows]
        st[arm] = {"n": len(xs), "drift": sum(not x["ok"] for x in xs),
                   **{k: sum(_has(x["issues"], k) for x in xs) for k in KINDS},
                   "chars": round(sum(len(x["text"]) for x in xs) / max(len(xs), 1))}
    n, c_now, c_fix = st["now"]["n"], st["now"]["加结论"], st["fix"]["加结论"]
    rnd = random.Random(0)   # 两边加结论的比例各取 Beta(1+k, 1+n-k)，看加一句以后更少的概率
    p_better = sum(rnd.betavariate(1 + c_fix, 1 + n - c_fix) < rnd.betavariate(1 + c_now, 1 + n - c_now) for _ in range(20000)) / 20000
    gate = {"1_reproduced": c_now >= 4, "2_half": c_fix * 2 <= c_now, "3_p80": p_better >= 0.8,
            "4_no_new_harm": st["fix"]["drift"] <= st["now"]["drift"] and st["fix"]["chars"] >= 0.9 * st["now"]["chars"]}
    res = {"stats": st, "p_fix_fewer_claims": round(p_better, 3), "gate": gate, "pass": all(gate.values())}
    (DIR / "claims-score.json").write_text(json.dumps(res, ensure_ascii=False, indent=1))
    print(json.dumps(res, ensure_ascii=False, indent=1))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("pick"); p.add_argument("--n", type=int, default=20); p.add_argument("--days", type=int, default=14)
    sub.add_parser("run")
    p = sub.add_parser("pairs"); p.add_argument("--n", type=int, default=10)
    p = sub.add_parser("score"); p.add_argument("answers")
    p = sub.add_parser("claims"); p.add_argument("--runs", type=int, default=2)
    sub.add_parser("claims-report")
    a = ap.parse_args()
    {"pick": cmd_pick, "run": cmd_run, "pairs": cmd_pairs, "score": cmd_score,
     "claims": cmd_claims, "claims-report": cmd_claims_report}[a.cmd](a)


if __name__ == "__main__":
    main()
