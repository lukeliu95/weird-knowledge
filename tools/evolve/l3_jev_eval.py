#!/usr/bin/env python3
"""只测不接入：拿 L3 的旧选择题，看 TypeSafe Jev 猜"Luke 会选哪个"猜得怎么样，和 Opus 比。

Luke 2026-10-25 选了 A："先用 Jev 测一次，只测不接入。这次允许把 128 道旧选择题和我的原则、口味 skill 发给 TypeSafe，
客户名和 Salesroom 资料不发"。所以发给 Jev 的只有：原则标题、口味 skill、更早的相似旧选择、这道题。
不发 Luke 的档案（profile.md）、确认过的规律（confirmed.md）、别的 agent 问过的题、Salesroom 的任何东西。
发之前去掉客户和人名（先用 Salesroom 的客户名单，再让 Opus 逐题挑出公司名、人名）、密钥、邮箱、电话。

对照组：同样这份去名后的资料交给 Opus，看差距是模型的还是资料的。

用法：
  l3_jev_eval.py scrub              逐题挑出要去掉的名字，存 private/l3/jev-scrub.json（只跑一次，可断点续跑）
  l3_jev_eval.py show <n>           打印前 n 道题实际要发出去的内容，发之前人工看一眼
  l3_jev_eval.py run [--arm jev|opus] [--n 3] [--workers 8]
  l3_jev_eval.py report             和 Opus 全资料版（ask.py backtest 最新一次）对比
"""
import argparse, collections, concurrent.futures as cf, datetime as dt, json, os, re, sys, time, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "mind"))
import l1_eval as E  # noqa: E402
import l3_eval as L  # noqa: E402
import opus_judge as OJ  # noqa: E402

OUT = E.PRIVATE / "l3"
SCRUB = OUT / "jev-scrub.json"
SECRET = re.compile(r"(sk-[A-Za-z0-9_-]{16,}|srk_[A-Za-z0-9_-]{8,}|gh[pousr]_[A-Za-z0-9]{20,}|xox[abp]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16}"
                    r"|Bearer\s+[A-Za-z0-9._-]{16,}|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}|\+?\d[\d -]{8,}\d)")


def questions():
    rows = [json.loads(l) for l in (OUT / "decisions.jsonl").read_text().split("\n") if l.strip()]
    rows = [r for r in rows if r["choice"] in r["options"]]
    for r in rows:
        r["q"] = L.strip_rec(r["question"] if r["kind"] == "ask_tool" else r["question"][-2500:])
        r["opts"] = {k: L.strip_rec(v) or f"选项 {k}" for k, v in r["options"].items()}
    return rows


def customer_names():
    import salesroom as S
    return set(S.all_customer_names())


def scrub_text(t, names):
    import salesroom as S
    for n in sorted(names, key=len, reverse=True):
        t = t.replace(n, "某名字")
    return S.HONORIFIC.sub("某人", SECRET.sub("某号码", t))


SCRUB_SYS = ("你在帮忙去掉文本里的专有名字，以便把题目发给外部服务。只输出一个 JSON 对象：{\"题号\": [\"要去掉的词\", …]}。"
             "要去掉：客户和合作公司的名字、客户的店铺或项目名、人名（包括同事的名字和昵称，但不包括 Luke）、内部产品代号以外能认出具体客户的词。"
             "不用去掉：公开的技术和产品名（Claude、Codex、GitHub、Vercel、Qwen 等）、Luke 自己公司的产品名（GBase 系列）。宁可多挑，不要漏。")


def cmd_scrub(a):
    done = json.loads(SCRUB.read_text()) if SCRUB.exists() else {}
    rows = [r for r in questions() if r["id"] not in done]
    for i in range(0, len(rows), 15):
        batch = rows[i:i + 15]
        text = "\n\n".join(f"【{r['id']}】\n{r['q']}\n" + "\n".join(f"{k}. {v}" for k, v in r["opts"].items()) for r in batch)
        out = OJ.ask_json(SCRUB_SYS, text)
        for r in batch:
            done[r["id"]] = [w for w in (out.get(r["id"]) or []) if isinstance(w, str) and len(w) >= 2]
        SCRUB.write_text(json.dumps(done, ensure_ascii=False, indent=1))
        print(f"  {min(i + 15, len(rows))}/{len(rows)}", file=sys.stderr)
    print(f"挑出名字的题 {sum(bool(v) for v in done.values())}/{len(done)}，共 {sum(len(v) for v in done.values())} 个词")


def build(r, rows, names, per_q):
    words = names | set(per_q.get(r["id"], []))
    pool = [x for x in rows if x["ts"] < r["ts"]]
    ex = []
    if pool:
        idx = E.Index([{"id": x["id"], "text": x["q"] + "\n" + "\n".join(x["opts"].values()), "x": x} for x in pool])
        ex = [d["x"] for d in idx.top(r["q"] + "\n" + "\n".join(r["opts"].values()), 4)]
    for x in ex:
        words |= set(per_q.get(x["id"], []))
    sc = lambda t: scrub_text(t, words)
    import ask as A
    parts = ["【Luke 确认过的做事原则】\n" + A.principles(),
             "【Luke 的口味说明】\n" + (E.PRIVATE / "luke" / json.loads((E.PRIVATE / "l1" / "champion.json").read_text())["profile"]).read_text()]
    if ex:
        parts.append("【他以前的相似选择】\n" + "\n\n".join(
            f"题：{sc(x['q'][-700:])}\n" + "\n".join(f"{k}. {sc(v[:200])}" for k, v in x["opts"].items()) + f"\n他选了：{x['choice']}" for x in ex))
    parts.append("【这次的问题】\n" + sc(r["q"]))
    return "\n\n".join(parts), {k: sc(v) for k, v in r["opts"].items()}


def jev(state, opts):
    q = {"pick": {"type": "choice", "instructions": "Luke 多半会选哪一个", "criteria": {k: v[:600] for k, v in opts.items()}}}
    req = urllib.request.Request("https://api.typesafe.ai/v1/systemone",
                                 json.dumps({"model": "jev-latest", "state": state, "questions": q}).encode(),
                                 {"Content-Type": "application/json", "Authorization": f"Bearer {os.environ['TYPESAFE_API_KEY']}"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        d = json.load(resp)
    a = d["answers"]["pick"]
    return dict(choice=a["choice"], confidence=a["confidence"], raw=a, tokens=d.get("usage", {}).get("input_tokens", 0))


OPUS_SYS = "你在替一个具体的人 Luke 预判他会怎么选。只输出 JSON：{\"probs\": {\"A\": 概率, …}}，概率加起来等于 1。"


def opus(state, opts):
    out = OJ.ask_json(OPUS_SYS, state + "\n\n【选项】\n" + "\n".join(f"{k}. {v}" for k, v in opts.items()))
    probs = {k: float((out.get("probs") or {}).get(k, 0) or 0) for k in opts}
    z = sum(probs.values()) or 1
    ch = max(probs, key=probs.get)
    return dict(choice=ch, confidence=round(probs[ch] / z, 3), raw=probs, tokens=0)


def cmd_show(a):
    E.load_env()
    rows, names, per_q = questions(), customer_names(), json.loads(SCRUB.read_text())
    for r in rows[-a.n:]:
        state, opts = build(r, rows, names, per_q)
        print("=" * 60, r["id"], "\n", state[-2500:], "\n选项：", json.dumps(opts, ensure_ascii=False)[:800])


def cmd_run(a):
    E.load_env()
    if not SCRUB.exists():
        sys.exit("先跑 scrub")
    rows, names, per_q = questions(), customer_names(), json.loads(SCRUB.read_text())
    todo = rows[-a.n:] if a.n else rows

    def one(r):
        state, opts = build(r, rows, names, per_q)
        t0 = time.time()
        for k in range(3):
            try:
                res = (jev if a.arm == "jev" else opus)(state, opts)
                break
            except Exception as e:
                if k == 2:
                    print(f"  {r['id']} 出错：{e}", file=sys.stderr)
                    return None
                time.sleep(3)
        return {"id": r["id"], "luke": r["choice"], "rec": r["recommended"], "seconds": round(time.time() - t0, 2),
                "chars": len(state), **res}

    out = []
    with cf.ThreadPoolExecutor(a.workers) as ex:
        for i, res in enumerate(ex.map(one, todo), 1):
            if res:
                out.append(res)
            if i % 20 == 0:
                print(f"  {i}/{len(todo)}", file=sys.stderr, flush=True)
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M")
    (OUT / f"jev-eval-{stamp}-{a.arm}.jsonl").write_text("".join(json.dumps(o, ensure_ascii=False) + "\n" for o in out))
    print(json.dumps(summary(out), ensure_ascii=False, indent=1))


def summary(out):
    n = len(out)
    ok = [o["choice"] == o["luke"] for o in out]
    hi = [o for o in out if o["confidence"] >= 0.8]
    bins = collections.defaultdict(list)
    for o in out:
        bins[min(int(o["confidence"] * 10), 9) / 10].append(o["choice"] == o["luke"])
    # Jev 另给每个选项的概率，它的 confidence 和最大概率不是一回事，两种都看
    top = lambda o: max(((o.get("raw") or {}).get("probabilities") or {}).values(), default=o["confidence"])
    hp = [o for o in out if top(o) >= 0.8]
    return {"n": n, "agree": f"{sum(ok)}/{n}（{sum(ok) / max(n, 1):.0%}）",
            "high_conf(>=0.8)": f"{sum(o['choice'] == o['luke'] for o in hi)}/{len(hi)}",
            "top_prob(>=0.8)": f"{sum(o['choice'] == o['luke'] for o in hp)}/{len(hp)}",
            "calibration": {f"{k:.1f}": f"{sum(v)}/{len(v)}" for k, v in sorted(bins.items())},
            "avg_seconds": round(sum(o["seconds"] for o in out) / max(n, 1), 2),
            "input_tokens": sum(o.get("tokens", 0) for o in out)}


def cmd_report(a):
    latest = lambda pat: max(OUT.glob(pat), default=None, key=lambda p: p.stat().st_mtime)
    full = max((E.PRIVATE / "mind").glob("backtest-*-sources-on.jsonl"), key=lambda p: p.stat().st_mtime)
    arms = {"Jev（去名后的资料）": latest("jev-eval-*-jev.jsonl"), "Opus（同样去名后的资料）": latest("jev-eval-*-opus.jsonl"),
            "Opus（全资料，lukeeMind 现在的做法）": full}
    data = {k: {json.loads(l)["id"]: json.loads(l) for l in p.read_text().split("\n") if l.strip()} for k, p in arms.items() if p}
    ids = set.intersection(*(set(v) for v in data.values()))
    for k, v in data.items():
        # ask.py backtest 记的 confidence 是"高/中/低"，换成最大概率再比
        sub = [{**v[i], "seconds": v[i].get("seconds", 0),
                "confidence": max(v[i]["probs"].values()) if isinstance(v[i]["confidence"], str) else v[i]["confidence"]} for i in ids]
        print(k, json.dumps(summary(sub), ensure_ascii=False))
    print("共同题", len(ids))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("scrub")
    p = sub.add_parser("show"); p.add_argument("n", type=int)
    p = sub.add_parser("run"); p.add_argument("--arm", choices=["jev", "opus"], default="jev")
    p.add_argument("--n", type=int, default=0); p.add_argument("--workers", type=int, default=8)
    sub.add_parser("report")
    a = ap.parse_args()
    {"scrub": cmd_scrub, "show": cmd_show, "run": cmd_run, "report": cmd_report}[a.cmd](a)


if __name__ == "__main__":
    main()
