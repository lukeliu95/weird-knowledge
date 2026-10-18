#!/usr/bin/env python3
"""L1 点赞预测：生成回顾式测试集（正样本 = 最近点赞，负样本 = 同一批作者没被点赞的推文）。

用法：
  python3 tools/evolve/l1_build.py [--n 100] [--per-author 40]

输出写进私有目录（不进 git）：private/l1/testset-YYYYMMDD.jsonl
只调用 opencli 的只读命令（likes、tweets），不点赞、不发帖。见 docs/2026-10-18-self-evolution-spec.md。
"""
import argparse, collections, datetime as dt, json, random, re, subprocess, time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PRIVATE = REPO / "private"   # gitignored; in a worktree it is a symlink to the main checkout's private/


class RateLimited(Exception):
    pass


def opencli(*args):
    out = subprocess.run(["opencli", "twitter", *args, "-f", "json", "--window", "background"],
                         capture_output=True, text=True, timeout=600)
    try:
        d = json.loads(out.stdout)
    except json.JSONDecodeError:
        return []
    if not d.get("ok"):
        if "429" in json.dumps(d.get("error", "")):
            raise RateLimited()
        return []
    return d.get("data") or []


def author_tweets(h, limit, sleep, since):
    """Fetch once per author and cache, so a rate-limited run can resume on the next loop tick.
    Uses search (from:h since:date) because the UserTweets endpoint allows only ~5 authors per quota window."""
    cache = PRIVATE / "l1" / "cache" / f"{h}.json"
    if cache.exists():
        return json.loads(cache.read_text())
    data = opencli("search", f"since:{since} -filter:nativeretweets -filter:replies", "--from", h,
                   "--product", "live", "--limit", str(limit))
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(data, ensure_ascii=False))
    time.sleep(sleep)
    return data


def front(t, k):
    m = re.search(rf"^{k}:[ \t]*(.*)$", t, re.M)
    v = m.group(1).strip() if m else ""
    return json.loads(v) if v.startswith('"') else v


def clip_text(t):
    body = t.split("## 原文", 1)[-1].split("## 溯源", 1)[0]
    body = re.split(r"^> 媒体：", body, flags=re.M)[0]
    return body.strip()


def tweet_text(tw):
    s = tw.get("text", "")
    q = tw.get("quoted_tweet")
    if q:
        s += "\n\n[引用 @" + q.get("author", "") + "] " + q.get("text", "")
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=100)
    ap.add_argument("--per-author", type=int, default=40)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--neg-from", help="take negatives from a timeline snapshot (private/l1/prospective/snapshot-*.jsonl) instead of per-author fetching")
    ap.add_argument("--sleep", type=float, default=8, help="seconds between authors, to stay under X's rate limit")
    a = ap.parse_args()
    random.seed(a.seed)

    liked_ids, pos = set(), []
    for f in (REPO / "clips").glob("*.md"):
        t = f.read_text()
        m = re.search(r"/status/(\d+)", front(t, "url"))
        if m:
            liked_ids.add(m.group(1))
        if "X 点赞" in front(t, "why") and m:
            h = re.search(r"@(\w+)", front(t, "author"))
            pos.append(dict(id=m.group(1), author=h.group(1) if h else "", published=front(t, "published"),
                            text=clip_text(t)[:1500], label=1, file=f.name))
    try:
        for tw in opencli("likes", "LukeLiu95", "--limit", "200"):   # likes not imported yet still count as liked
            liked_ids.add(str(tw.get("id")))
    except RateLimited:
        print("点赞列表被限流，只用库里已有的点赞去重", flush=True)

    pos.sort(key=lambda r: r["published"], reverse=True)
    pos = pos[: a.n]
    oldest = min(p["published"][:10] for p in pos)

    if a.neg_from:
        snap = [json.loads(l) for l in Path(a.neg_from).read_text().split("\n") if l.strip()]
        snap = [dict(id=r["id"], author=r["author"], published=r["published"], text=r["text"], label=0)
                for r in snap if r["id"] not in liked_ids]
        random.shuffle(snap)
        rows = pos + snap[: len(pos)]
        random.shuffle(rows)
        out = PRIVATE / "l1" / f"testset-tl-{dt.date.today():%Y%m%d}.jsonl"
        out.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
        print(f"{out}: 正样本 {len(pos)}，负样本 {len(rows) - len(pos)}（来自时间线快照）")
        return

    neg_pool = []
    authors = collections.Counter(p["author"] for p in pos if p["author"])
    missing = []
    for h in authors:
        try:
            tweets = author_tweets(h, a.per_author, a.sleep, oldest)
        except RateLimited:
            missing = [x for x in authors if not (PRIVATE / "l1" / "cache" / f"{x}.json").exists()]
            print(f"被 X 限流，还差 {len(missing)} 位作者没抓，下次接着抓", flush=True)
            break
        for tw in tweets:
            tid = str(tw.get("id"))
            if tw.get("is_retweet") or tid in liked_ids or tw.get("text", "").startswith("@"):
                continue
            ts = dt.datetime.strptime(tw["created_at"], "%a %b %d %H:%M:%S %z %Y")
            if ts.strftime("%Y-%m-%d") < oldest:
                continue
            neg_pool.append(dict(id=tid, author=h, published=ts.strftime("%Y-%m-%d %H:%M UTC"),
                                 text=tweet_text(tw)[:1500], label=0))
    # sample negatives in proportion to how often each author appears among the positives
    by_author = collections.defaultdict(list)
    for r in neg_pool:
        by_author[r["author"]].append(r)
    neg = []
    for h, k in authors.most_common():
        random.shuffle(by_author[h])
        neg += by_author[h][:k]
    rest = [r for h in by_author for r in by_author[h] if r not in neg]
    random.shuffle(rest)
    neg += rest[: max(0, len(pos) - len(neg))]
    neg = neg[: len(pos)]

    if missing:
        print("作者没抓全，这次不生成测试集")
        return
    out = PRIVATE / "l1" / f"testset-{dt.date.today():%Y%m%d}.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    rows = pos + neg
    random.shuffle(rows)
    out.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    print(f"{out}: 正样本 {len(pos)}，负样本 {len(neg)}（候选 {len(neg_pool)}，作者 {len(authors)} 个，最早 {oldest}）")


if __name__ == "__main__":
    main()
