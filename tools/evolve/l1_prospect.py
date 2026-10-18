#!/usr/bin/env python3
"""L1 前瞻测试：先给首页时间线上的推文打分，过几天再看 Luke 实际点了哪些。考题来自未来，模型不可能背过。

用法：
  python3 tools/evolve/l1_prospect.py snapshot [--limit 100] [--from-files a.json b.json]
      抓 following 和 for-you 两个时间线（只读），存成 private/l1/prospective/snapshot-时间.jsonl
  python3 tools/evolve/l1_prospect.py predict <snapshot> --cond c0|c1|c2
      用 l1_eval 的同一套引擎和提示词打分（不知道答案），存 pred-*.jsonl
  python3 tools/evolve/l1_prospect.py score <snapshot>
      抓最近的点赞（只读），给快照打标签，算每份预测的成绩，追加进 private/l1/metrics.jsonl

局限：时间线上没被点赞的推文，可能只是 Luke 没刷到，所以负样本是"弱负样本"。
"""
import argparse, datetime as dt, json, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import l1_eval as E  # noqa: E402

DIR = E.PRIVATE / "l1" / "prospective"


def fetch(kind, limit):
    out = subprocess.run(["opencli", "twitter", *kind, "-f", "json", "--window", "background", "--limit", str(limit)],
                         capture_output=True, text=True, timeout=900)
    d = json.loads(out.stdout)
    if not d.get("ok"):
        raise SystemExit(f"opencli 失败：{d.get('error')}")
    return d["data"]


def text_of(tw):
    s = tw.get("text", "")
    if tw.get("quoted_tweet"):
        s += "\n\n[引用 @" + tw["quoted_tweet"].get("author", "") + "] " + tw["quoted_tweet"].get("text", "")
    return s


def liked_ids_in_repo():
    ids = set()
    for f in (E.REPO / "clips").glob("*.md"):
        import re
        m = re.search(r"/status/(\d+)", f.read_text().split("\n---", 1)[0])
        if m:
            ids.add(m.group(1))
    return ids


def snapshot(a):
    feeds = []
    if a.from_files:
        for p in a.from_files:
            feeds.append((Path(p).stem, json.load(open(p))["data"]))
    else:
        for t in ("following", "for-you"):
            feeds.append((t, fetch(["timeline", "--type", t], a.limit)))
    seen, rows, already = set(), [], liked_ids_in_repo()
    for feed, data in feeds:
        for tw in data:
            tid = str(tw.get("id"))
            if tw.get("is_retweet") or tid in seen or tid in already:
                continue
            seen.add(tid)
            rows.append(dict(id=tid, author=tw.get("author", ""), published=tw.get("created_at", ""),
                             feed=feed, text=text_of(tw)[:1500]))
    DIR.mkdir(parents=True, exist_ok=True)
    out = DIR / f"snapshot-{dt.datetime.now():%Y%m%d-%H%M}.jsonl"
    out.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    print(f"{out}: {len(rows)} 条（去掉了转推和已经点过赞的）")


def predict(a):
    E.load_env()
    rows = [json.loads(l) for l in Path(a.snapshot).read_text().split("\n") if l.strip()]
    profile = Path(a.profile).read_text() if a.cond != "c0" else ""
    index = E.Index(E.liked_docs({r["id"] for r in rows})) if a.cond == "c2" else None
    for r in rows:
        ex = index.top(r["text"], a.k) if index else []
        r["p"] = E.qwen(E.prompt(r, a.cond, profile, ex))
    out = Path(a.snapshot).with_name(Path(a.snapshot).stem.replace("snapshot", "pred") + f"-{a.cond}-{Path(a.profile).stem if a.cond != 'c0' else 'none'}.jsonl")
    out.write_text("".join(json.dumps({"id": r["id"], "p": r["p"]}) + "\n" for r in rows))
    print(f"{out}: {len(rows)} 条预测，平均概率 {sum(r['p'] for r in rows) / len(rows):.3f}")


def score(a):
    rows = {json.loads(l)["id"]: json.loads(l) for l in Path(a.snapshot).read_text().split("\n") if l.strip()}
    liked = {str(t.get("id")) for t in fetch(["likes", "LukeLiu95"], a.likes_limit)} | liked_ids_in_repo()
    pos = sum(i in liked for i in rows)
    print(f"快照 {len(rows)} 条，其中后来被点赞 {pos} 条")
    if pos == 0:
        return
    stem = Path(a.snapshot).stem.replace("snapshot", "pred")
    for pf in sorted(Path(a.snapshot).parent.glob(stem + "-*.jsonl")):
        preds = [json.loads(l) for l in pf.read_text().split("\n") if l.strip()]
        rs = [dict(p=x["p"], label=int(x["id"] in liked)) for x in preds]
        m = E.metrics(rs)
        rec = dict(time=f"{dt.datetime.now():%Y%m%d-%H%M}", testset=Path(a.snapshot).name, engine="qwen",
                   cond=pf.stem.split("-")[-2], profile=pf.stem.split("-")[-1], tag="prospective", **m)
        with open(E.PRIVATE / "l1" / "metrics.jsonl", "a") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(json.dumps(rec, ensure_ascii=False))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("snapshot"); s.add_argument("--limit", type=int, default=100); s.add_argument("--from-files", nargs="*")
    p = sub.add_parser("predict"); p.add_argument("snapshot"); p.add_argument("--cond", default="c1", choices=["c0", "c1", "c2"])
    p.add_argument("--profile", default=str(E.PRIVATE / "luke" / "profile.md")); p.add_argument("--k", type=int, default=8)
    c = sub.add_parser("score"); c.add_argument("snapshot"); c.add_argument("--likes-limit", type=int, default=300)
    a = ap.parse_args()
    {"snapshot": snapshot, "predict": predict, "score": score}[a.cmd](a)


if __name__ == "__main__":
    main()
