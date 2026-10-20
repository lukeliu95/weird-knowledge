#!/usr/bin/env python3
"""L3 回答预测：给本地 Qwen 看一道 agent 问 Luke 的选择题（去掉"推荐"标记），看它能不能猜中 Luke 选了哪个。

为什么去掉推荐：Luke 九成跟着推荐走，带着推荐考等于考"会不会认推荐"。要让 lukee 能替别的 agent 出主意，
它得在没人推荐时，自己给出 Luke 会选的那一个。
数据只在本地：题目来自 private/l3/decisions.jsonl（l3_extract.py 抽的），只发给本地 Qwen。

条件：
  q0  只给题目
  q1  加 Luke 档案和他确认过的原则
  q2  q1 再加 4 道他以前答过的相似题（只取这道题之前的，防止偷看未来）

用法：
  python3 tools/evolve/l3_eval.py [--cond q0|q1|q2|all]
"""
import argparse, collections, datetime as dt, json, math, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import l1_eval as E  # noqa: E402

DIR = E.PRIVATE / "l3"
SYS = "你在模拟一个具体的人：Luke。一个 AI 助手给他出了一道选择题，判断他会选哪个选项。只回答一个字母。"
STRIP = [re.compile(r"[（(]\s*(推荐|Recommended)\s*[)）]"), re.compile(r"[^。\n]*推荐[^。\n]*[。]?"),
         re.compile(r"(?i)\(recommended\)")]


def strip_rec(t):
    for r in STRIP:
        t = r.sub("", t)
    return t


def principles():
    t = (E.REPO / "framework.md").read_text()
    return "\n".join(re.findall(r"^### (原则 \d+：.*)$", t, re.M))


def render(r):
    if r["kind"] == "ask_tool":
        body = r["question"] + "\n" + "\n".join(f"{k}. {v}" for k, v in r["options"].items())
    else:
        body = r["question"][-2500:]
    return strip_rec(body)


def prompt(r, cond, profile, examples):
    parts = []
    if cond in ("q1", "q2"):
        parts += ["【Luke 的档案】\n" + profile, "【他确认过的做事原则】\n" + principles()]
    if cond == "q2" and examples:
        parts.append("【他以前答过的相似题】\n" + "\n\n".join(f"题：{render(e)[-600:]}\n他选了：{e['choice']}" for e in examples))
    letters = "".join(r["options"].keys())
    parts.append(f"【这道题】\n{render(r)}")
    parts.append(f"Luke 会选哪个？只回答一个字母（{'/'.join(letters)}）。")
    return "\n\n".join(parts)


def qwen_dist(text, letters):
    d = E.post(E.os.environ["QWEN_BASE_URL"] + "/chat/completions", {
        "model": "qwen3.8-27b-coder390-mlx-mixed4-mtp",
        "messages": [{"role": "system", "content": SYS}, {"role": "user", "content": text}],
        "max_tokens": 1, "temperature": 0, "logprobs": True, "top_logprobs": 20,
        "chat_template_kwargs": {"enable_thinking": False}}, E.os.environ["QWEN_API_KEY"])
    p = collections.defaultdict(float)
    for t in d["choices"][0]["logprobs"]["content"][0]["top_logprobs"]:
        k = t["token"].strip().upper()
        if k in letters:
            p[k] += math.exp(t["logprob"])
    z = sum(p.values()) or 1
    return {k: p[k] / z for k in letters}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cond", default="all")
    a = ap.parse_args()
    E.load_env()
    rows = [json.loads(l) for l in (DIR / "decisions.jsonl").read_text().split("\n") if l.strip()]
    rows = [r for r in rows if r["choice"] in r["options"]]   # 选了"其他"的不考
    profile = (E.PRIVATE / "luke" / json.loads((E.PRIVATE / "l1" / "champion.json").read_text())["profile"]).read_text()
    conds = ["q0", "q1", "q2"] if a.cond == "all" else [a.cond]
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M")
    summary = {}
    for cond in conds:
        hits, nll, out = 0, 0.0, []
        for i, r in enumerate(rows):
            ex = []
            if cond == "q2" and i:
                idx = E.Index([{"id": j, "text": render(x)} for j, x in enumerate(rows[:i])])
                ex = [rows[d["id"]] for d in idx.top(render(r), 4)]
            dist = qwen_dist(prompt(r, cond, profile, ex), "".join(r["options"].keys()))
            pred = max(dist, key=dist.get)
            hits += pred == r["choice"]
            nll += -math.log(max(dist.get(r["choice"], 0), 1e-6))
            out.append({"id": r["id"], "choice": r["choice"], "rec": r["recommended"], "pred": pred, "dist": dist})
        n = len(rows)
        summary[cond] = {"n": n, "acc": round(hits / n, 3), "nll": round(nll / n, 3)}
        (DIR / "runs").mkdir(parents=True, exist_ok=True)
        (DIR / "runs" / f"{stamp}-{cond}.jsonl").write_text("".join(json.dumps(o, ensure_ascii=False) + "\n" for o in out))
        print(cond, summary[cond], flush=True)
    n = len(rows)
    first = sum(r["choice"] == "A" for r in rows) / n
    rand = sum(1 / len(r["options"]) for r in rows) / n
    withrec = [r for r in rows if r["recommended"]]
    rec = sum(r["choice"] == r["recommended"] for r in withrec) / len(withrec) if withrec else 0
    base = {"random": round(rand, 3), "always_A": round(first, 3), "follow_rec(有推荐的题)": round(rec, 3)}
    print("对照", base)
    with open(DIR / "metrics.jsonl", "a") as f:
        f.write(json.dumps({"time": stamp, **summary, "baselines": base}, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
