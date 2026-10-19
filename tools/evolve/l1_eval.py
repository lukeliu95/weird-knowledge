#!/usr/bin/env python3
"""L1 点赞预测：用判断引擎给测试集打分，记录一致率和校准度。

用法：
  python3 tools/evolve/l1_eval.py <testset.jsonl> --cond c0|c1|c2 [--engine qwen|jev] [--profile private/luke/profile.md] [--tag 说明]

条件：
  c0  不给任何档案
  c1  给 Luke 档案
  c2  给 Luke 档案 + 检索到的相似点赞（排除测试集里的条目）
  c3  c2 再加检索到的"刷到但没点"的推文做对照（取自时间线快照，排除测试集）

私密内容（档案、点赞例子）只发给本地 Qwen；jev 只能配 c0（只有公开的推文文本）。
结果写进 private/l1/runs/ 和 private/l1/metrics.jsonl。
"""
import argparse, collections, datetime as dt, json, math, os, re, sys, urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PRIVATE = REPO / "private"   # gitignored; in a worktree it is a symlink to the main checkout's private/


def load_env():
    for line in (PRIVATE.parent / ".env").read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k, v)


def post(url, body, key):
    req = urllib.request.Request(url, json.dumps(body).encode(), {"Content-Type": "application/json", "Authorization": f"Bearer {key}"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.load(r)


# ---------- retrieval: character-bigram tf-idf over liked clips ----------
def grams(s):
    s = re.sub(r"https?://\S+", " ", s.lower())
    s = re.sub(r"\s+", " ", s)
    return [s[i:i + 2] for i in range(len(s) - 1)]


class Index:
    def __init__(self, docs):
        self.docs = docs
        df = collections.Counter()
        self.vecs = []
        for d in docs:
            c = collections.Counter(grams(d["text"]))
            self.vecs.append(c)
            df.update(c.keys())
        n = len(docs)
        self.idf = {g: math.log(n / (1 + v)) + 1 for g, v in df.items()}
        self.norms = [math.sqrt(sum((tf * self.idf[g]) ** 2 for g, tf in v.items())) or 1 for v in self.vecs]

    def top(self, text, k):
        q = collections.Counter(grams(text))
        qn = math.sqrt(sum((tf * self.idf.get(g, 0)) ** 2 for g, tf in q.items())) or 1
        scores = []
        for i, v in enumerate(self.vecs):
            s = sum(tf * v.get(g, 0) * self.idf.get(g, 0) ** 2 for g, tf in q.items())
            scores.append((s / (qn * self.norms[i]), i))
        scores.sort(reverse=True)
        return [self.docs[i] for _, i in scores[:k]]


def liked_docs(exclude):
    out = []
    for f in (REPO / "clips").glob("*.md"):
        t = f.read_text()
        m = re.search(r"/status/(\d+)", t.split("\n---", 1)[0])
        if not m or m.group(1) in exclude or "X 点赞" not in t.split("\n---", 1)[0]:
            continue
        body = t.split("## 原文", 1)[-1].split("## 溯源", 1)[0]
        body = re.split(r"^> 媒体：", body, flags=re.M)[0].strip()
        out.append({"id": m.group(1), "text": body[:600]})
    return out


# ---------- engines ----------
SYS = "你在模拟一个具体的人：Luke。判断他在 X 上刷到这条推文时会不会点赞。只回答一个字母：A 表示会点赞，B 表示不会。"


def skipped_docs(exclude):
    """Tweets that showed up on Luke's home timeline but were never liked (weak negatives)."""
    liked = {d["id"] for d in liked_docs(set())}
    out, seen = [], set()
    for f in sorted((PRIVATE / "l1" / "prospective").glob("snapshot-*.jsonl")):
        for l in f.read_text().split("\n"):
            if l.strip():
                r = json.loads(l)
                if r["id"] not in exclude and r["id"] not in liked and r["id"] not in seen:
                    seen.add(r["id"])
                    out.append({"id": r["id"], "text": r["text"][:600]})
    return out


def prompt(row, cond, profile, examples, negatives=()):
    parts = []
    if cond in ("c1", "c2", "c3"):
        parts.append("【Luke 的档案】\n" + profile)
    if cond in ("c2", "c3"):
        parts.append("【他以前点赞过的相似推文】\n" + "\n\n".join(f"- {e['text'][:400]}" for e in examples))
    if cond == "c3" and negatives:
        parts.append("【他刷到过、但没有点赞的相似推文】\n" + "\n\n".join(f"- {e['text'][:400]}" for e in negatives))
    if cond == "c0":
        parts.append("你对 Luke 只知道一点：他是 X 用户。")
    parts.append(f"【要判断的推文】作者 @{row['author']}\n{row['text'][:1200]}")
    parts.append("Luke 会点赞这条推文吗？A 会，B 不会。只回答一个字母。")
    return "\n\n".join(parts)


def qwen(text):
    d = post(os.environ["QWEN_BASE_URL"] + "/chat/completions", {
        "model": "qwen3.8-27b-coder390-mlx-mixed4-mtp",
        "messages": [{"role": "system", "content": SYS}, {"role": "user", "content": text}],
        "max_tokens": 1, "temperature": 0, "logprobs": True, "top_logprobs": 10,
        "chat_template_kwargs": {"enable_thinking": False}}, os.environ["QWEN_API_KEY"])
    top = d["choices"][0]["logprobs"]["content"][0]["top_logprobs"]
    p = collections.defaultdict(float)
    for t in top:
        k = t["token"].strip().upper()
        if k in ("A", "B"):
            p[k] += math.exp(t["logprob"])
    a, b = p["A"] or 1e-6, p["B"] or 1e-6
    return a / (a + b)


def jev(row):
    d = post("https://api.typesafe.ai/v1/systemone", {
        "model": "jev-latest", "state": f"作者 @{row['author']}\n{row['text'][:1200]}",
        "questions": {"like": {"type": "choice", "instructions": "一位关注 AI 的 X 用户刷到这条推文时，会不会点赞",
                               "criteria": {"like": "会点赞", "skip": "不会点赞"}}}}, os.environ["TYPESAFE_API_KEY"])
    return d["answers"]["like"]["probabilities"]["like"], d.get("usage", {}).get("input_tokens", 0)


# ---------- metrics ----------
def metrics(rows):
    pos = [r["p"] for r in rows if r["label"] == 1]
    neg = [r["p"] for r in rows if r["label"] == 0]
    auc = sum((p > n) + 0.5 * (p == n) for p in pos for n in neg) / (len(pos) * len(neg))
    acc = sum((r["p"] >= 0.5) == (r["label"] == 1) for r in rows) / len(rows)
    brier = sum((r["p"] - r["label"]) ** 2 for r in rows) / len(rows)
    bins = collections.defaultdict(list)
    for r in rows:
        bins[min(int(r["p"] * 10), 9)].append(r)
    ece = sum(len(b) / len(rows) * abs(sum(x["p"] for x in b) / len(b) - sum(x["label"] for x in b) / len(b)) for b in bins.values())
    return dict(n=len(rows), auc=round(auc, 3), acc=round(acc, 3), brier=round(brier, 3), ece=round(ece, 3),
                mean_p_pos=round(sum(pos) / len(pos), 3), mean_p_neg=round(sum(neg) / len(neg), 3))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("testset")
    ap.add_argument("--cond", default="c1", choices=["c0", "c1", "c2", "c3"])
    ap.add_argument("--kneg", type=int, default=4)
    ap.add_argument("--engine", default="qwen", choices=["qwen", "jev"])
    ap.add_argument("--profile", default=str(PRIVATE / "luke" / "profile.md"))
    ap.add_argument("--k", type=int, default=8)
    ap.add_argument("--tag", default="")
    a = ap.parse_args()
    if a.engine == "jev" and a.cond != "c0":
        sys.exit("jev 只能配 c0：档案和点赞例子是私密内容，不发给外部接口")
    load_env()
    rows = [json.loads(l) for l in Path(a.testset).read_text().split("\n") if l.strip()]
    profile = Path(a.profile).read_text() if a.cond != "c0" else ""
    ids = {r["id"] for r in rows}
    index = Index(liked_docs(ids)) if a.cond in ("c2", "c3") else None
    nindex = Index(skipped_docs(ids)) if a.cond == "c3" else None
    tokens = 0
    for i, r in enumerate(rows, 1):
        if a.engine == "jev":
            r["p"], t = jev(r)
            tokens += t
        else:
            ex = index.top(r["text"], a.k) if index else []
            neg = nindex.top(r["text"], a.kneg) if nindex else []
            r["p"] = qwen(prompt(r, a.cond, profile, ex, neg))
        if i % 25 == 0:
            print(f"  {i}/{len(rows)}", file=sys.stderr, flush=True)
    m = metrics(rows)
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M")
    run = PRIVATE / "l1" / "runs" / f"{stamp}-{a.engine}-{a.cond}.jsonl"
    run.parent.mkdir(parents=True, exist_ok=True)
    run.write_text("".join(json.dumps({k: r[k] for k in ("id", "author", "label", "p")}) + "\n" for r in rows))
    rec = dict(time=stamp, testset=Path(a.testset).name, engine=a.engine, cond=a.cond,
               profile=Path(a.profile).name if a.cond != "c0" else "", tag=a.tag, **m)
    if a.engine == "jev":
        rec["jev_input_tokens"] = tokens
        rec["jev_cost_usd"] = round(tokens / 1e6 * 0.042, 5)
    with open(PRIVATE / "l1" / "metrics.jsonl", "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(json.dumps(rec, ensure_ascii=False))


if __name__ == "__main__":
    main()
