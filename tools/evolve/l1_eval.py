#!/usr/bin/env python3
"""L1 点赞预测：用判断引擎给测试集打分，记录一致率和校准度。

用法：
  python3 tools/evolve/l1_eval.py <testset.jsonl> --cond c0|c1|c2 [--engine local|jev] [--profile private/luke/profile.md] [--tag 说明]

条件：
  c0  不给任何档案
  c1  给 Luke 档案
  c2  给 Luke 档案 + 检索到的相似点赞（排除测试集里的条目）
  c3  c2 再加检索到的"刷到但没点"的推文做对照（取自时间线快照，排除测试集）

私密内容（档案、点赞例子）只发给本地模型（.env 的 LOCAL_MODEL，2026-11-23 起是 Inkling 2 Mini）；jev 只能配 c0（只有公开的推文文本）。
结果写进 private/l1/runs/ 和 private/l1/metrics.jsonl。
"""
import argparse, collections, datetime as dt, json, math, os, re, sys, urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import opus_judge as OJ  # noqa: E402

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


def labels():
    """Luke's own answers from the "ask" step (private/l1/labels.jsonl): the strongest labels we have."""
    f = PRIVATE / "l1" / "labels.jsonl"
    return [json.loads(l) for l in f.read_text().split("\n") if l.strip()] if f.exists() else []


def liked_docs(exclude):
    out = [{"id": r["id"], "text": r["text"][:600]} for r in labels() if r["label"] == 1 and r["id"] not in exclude]
    for f in (REPO / "clips").glob("*.md"):
        t = f.read_text()
        m = re.search(r"/status/(\d+)", t.split("\n---", 1)[0])
        if not m or m.group(1) in exclude or m.group(1) in {d["id"] for d in out} or "X 点赞" not in t.split("\n---", 1)[0]:
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
    out = [{"id": r["id"], "text": r["text"][:600]} for r in labels() if r["label"] == 0 and r["id"] not in exclude]
    seen = {r["id"] for r in out}
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


def local_top(system, text):
    """问本地模型一道选择题，返回答案第一个字的前 10 个候选：{字: 对数概率}。模型名见 opus_judge.local_model()。
    Inkling 的服务只给第一个生成字的概率，而对话接口下第一个字总是角色标记 <|message_model|>，
    所以按它的对话模板（模型目录里的 chat_template.jinja）自己拼好前缀走 completions，思考强度设 0；Qwen 走原来的对话接口。"""
    model = OJ.local_model()
    base, key = os.environ["QWEN_BASE_URL"], os.environ["QWEN_API_KEY"]
    if OJ.local_name(model) == "inkling":
        d = post(base + "/completions", {
            "model": model, "max_tokens": 1, "temperature": 0, "logprobs": 10,
            "prompt": f"<|message_system|><|content_text|>{system}<|end_message|>"
                      "<|message_system|><|content_text|>Thinking effort level: 0<|end_message|>"
                      f"<|message_user|><|content_text|>{text}<|end_message|>"
                      "<|message_model|><|content_text|>"}, key)
        top = d["choices"][0]["logprobs"]["top_logprobs"][0]
    else:
        d = post(base + "/chat/completions", {
            "model": model,
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": text}],
            "max_tokens": 1, "temperature": 0, "logprobs": True, "top_logprobs": 10,
            "chat_template_kwargs": {"enable_thinking": False}}, key)
        top = {}
        for t in d["choices"][0]["logprobs"]["content"][0]["top_logprobs"]:
            top[t["token"]] = max(top.get(t["token"], -1e9), t["logprob"])
    if d.get("model") and d["model"] != model:
        raise RuntimeError(f"本地端口挂的是 {d['model']}，不是 LOCAL_MODEL={model}")
    return top


# Inkling 的概率过于自信（一半想看的给到 0.999 以上，不想看的大多压在 0.01 以下），排序是对的，但刻度不能和 Qwen 直接比。
# 打分出口按任务做一次单调换算，换到 Qwen 的刻度：p = sigmoid(a·(log P(A) − log P(B)) + b)。只拉伸刻度、不改谁高谁低（AUC 不变），
# 下游门槛照旧。a、b 按"换算后落在门槛以上的比例和 Qwen 一样"两点对齐：
#   like（点赞预测、问口味的提示词）对齐 0.6 和 0.4；explore（探索打分的提示词）对齐 0.6（好内容）和 0.5（最拿不准的中心）。
# 2026-11-23 用 600 道未来考题、300 条随机候选上两边的分数拟合，对半验证，见 docs/2026-11-23-local-model-inkling.md。换模型要重新拟合
RESCALE = {("inkling", "like"): (0.260, -2.018), ("inkling", "explore"): (0.256, -2.809)}


def local_ab(system, text, task="like"):
    """问本地模型一道 A/B 题，返回选 A 的概率（按 task 换算到 Qwen 的刻度）。前 10 个候选字里没有 A 也没有 B 就报错，
    不记成 0.5（2026-11-22 端口换了模型，每道题都被记成 0.5）。调用方出错时按各自的规矩兜底或停下。
    直接用两个字的对数概率相减，不先换成概率再夹到 [1e-6, 1-1e-6]：那样会把 0.99999999 和 0.9999999999 压成同一个分。"""
    top = local_top(system, text)
    p = collections.defaultdict(float)
    for tok, lp in top.items():
        k = tok.strip().upper()
        if k in ("A", "B"):
            p[k] += math.exp(lp)
    if not p:
        raise RuntimeError(f"本地模型没回 A 或 B（候选是 {list(top)[:5]}）")
    floor = math.exp(min(top.values()))   # 只出现了一个字时，另一个按前 10 里最小的概率算（它的上限）
    x = math.log(p["A"] or floor) - math.log(p["B"] or floor)
    a, b = RESCALE.get((OJ.local_name(), task), (1.0, 0.0))
    return 1 / (1 + math.exp(-(a * x + b)))


def local(text):
    return local_ab(SYS, text)


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
    ap.add_argument("--engine", default="local", choices=["local", "jev"])
    ap.add_argument("--profile", default=str(PRIVATE / "luke" / "profile.md"))
    ap.add_argument("--k", type=int, default=8)
    ap.add_argument("--tag", default="")
    a = ap.parse_args()
    if a.engine == "jev" and a.cond != "c0":
        sys.exit("jev 只能配 c0：档案和点赞例子是私密内容，不发给外部接口")
    load_env()
    engine = a.engine if a.engine == "jev" else OJ.local_name()   # 记真实的模型名，成绩按它分开算
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
            r["p"] = local(prompt(r, a.cond, profile, ex, neg))
        if i % 25 == 0:
            print(f"  {i}/{len(rows)}", file=sys.stderr, flush=True)
    m = metrics(rows)
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M")
    run = PRIVATE / "l1" / "runs" / f"{stamp}-{engine}-{a.cond}.jsonl"
    run.parent.mkdir(parents=True, exist_ok=True)
    run.write_text("".join(json.dumps({k: r[k] for k in ("id", "author", "label", "p")}) + "\n" for r in rows))
    rec = dict(time=stamp, testset=Path(a.testset).name, engine=engine, cond=a.cond,
               profile=Path(a.profile).name if a.cond != "c0" else "", tag=a.tag, **m)
    if a.engine == "jev":
        rec["jev_input_tokens"] = tokens
        rec["jev_cost_usd"] = round(tokens / 1e6 * 0.042, 5)
    with open(PRIVATE / "l1" / "metrics.jsonl", "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(json.dumps(rec, ensure_ascii=False))


if __name__ == "__main__":
    main()
