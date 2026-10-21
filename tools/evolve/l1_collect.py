#!/usr/bin/env python3
"""给点赞预测（L1）多攒训练数据：都来自 Luke 在 X 上的真实行为，只读，不点赞、不发帖。

Luke 2026-10-21："你既然知道需要更多数据，那就去找更多数据，不要等待。"
数据只存 private/l1/extra/（是对 Luke 的画像，不进公开仓库），不导进 clips/。

用法：
  l1_collect.py bookmarks              拉 @LukeLiu95 的全部书签（强正样本：比点赞更用心的"留着"）
  l1_collect.py own [--days 180]       拉 Luke 自己发的帖（@LukeLiu95、@simprr）：他写什么，最能说明他关心什么
  l1_collect.py authors [--max 5]      他常点赞的作者最近 30 天发了什么、他没点哪些（弱负样本：大概率刷到过却没点）。
                                       X 会限流，每次只抓几位，按作者缓存，下次接着抓
  l1_collect.py stats                  各类数据攒了多少
"""
import argparse, collections, datetime as dt, json, re, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import l1_eval as E  # noqa: E402

DIR = E.PRIVATE / "l1" / "extra"
OWN_ACCOUNTS = ("LukeLiu95", "simprr")


def oc(*args, timeout=900):
    r = subprocess.run(["opencli", "twitter", *args, "-f", "json", "--window", "background"],
                       capture_output=True, text=True, timeout=timeout)
    try:   # opencli 有时在 JSON 后面打印"有新版本"的提示，只取第一个 JSON 对象
        out = r.stdout[r.stdout.index("{"):] if "{" in r.stdout else r.stdout
        d, _ = json.JSONDecoder().raw_decode(out)
    except Exception:
        raise RuntimeError((r.stderr or r.stdout)[-300:])
    if not d.get("ok", True):
        raise RuntimeError(str(d.get("error"))[:300])
    return d.get("data", d if isinstance(d, list) else [])


def row(tw, source):
    text = tw.get("text", "")
    if tw.get("quoted_tweet"):
        text += "\n\n[引用 @" + tw["quoted_tweet"].get("author", "") + "] " + tw["quoted_tweet"].get("text", "")
    return {"id": str(tw.get("id")), "author": tw.get("author", ""), "text": text, "created_at": tw.get("created_at", ""),
            "source": source}


def write_merge(path, rows):
    old = {json.loads(l)["id"]: json.loads(l) for l in path.read_text().split("\n") if l.strip()} if path.exists() else {}
    for r in rows:
        old.setdefault(r["id"], r)
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in old.values()))
    return len(old)


def liked_ids():
    ids = set()
    for f in (E.REPO / "clips").glob("*.md"):
        m = re.search(r"/status/(\d+)", f.read_text().split("\n---", 1)[0])
        if m:
            ids.add(m.group(1))
    return ids


def cmd_bookmarks(_):
    DIR.mkdir(parents=True, exist_ok=True)
    out, resume = DIR / "bookmarks.raw.jsonl", DIR / "bookmarks.resume.json"
    subprocess.run(["opencli", "twitter", "bookmarks", "--all", "--output-file", str(out), "--resume-file", str(resume),
                    "-f", "json", "--window", "background"], capture_output=True, text=True, timeout=3600)
    raw = [json.loads(l) for l in out.read_text().split("\n") if l.strip()] if out.exists() else []
    n = write_merge(DIR / "bookmarks.jsonl", [row(t, "bookmark") for t in raw])
    print(json.dumps({"bookmarks": n}, ensure_ascii=False))


def cmd_own(a):
    DIR.mkdir(parents=True, exist_ok=True)
    until = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=a.days)).strftime("%Y-%m-%dT%H:%M:%SZ")
    res = {}
    for acc in OWN_ACCOUNTS:
        try:
            data = oc("collection", acc, "--until", until, "--limit", "3000", timeout=1800)
            items = data.get("posts", []) if isinstance(data, dict) else data
            res[acc] = write_merge(DIR / f"own-{acc}.jsonl", [row(t, f"own:{acc}") for t in items if isinstance(t, dict)])
        except Exception as e:
            res[acc] = f"出错：{e}"
        time.sleep(30)
    print(json.dumps(res, ensure_ascii=False))


def top_authors(n=40):
    c = collections.Counter()
    for f in (E.REPO / "clips").glob("*.md"):
        m = re.search(r'^author:.*\(@([A-Za-z0-9_]+)\)', f.read_text().split("\n---", 1)[0], re.M)
        if m:
            c[m.group(1)] += 1
    return [a for a, _ in c.most_common(n)]


def cmd_authors(a):
    DIR.mkdir(parents=True, exist_ok=True)
    state_f = DIR / "authors.state.json"
    state = json.loads(state_f.read_text()) if state_f.exists() else {}
    liked = liked_ids()
    until = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
    today = dt.date.today().isoformat()
    todo = [x for x in top_authors() if state.get(x, {}).get("date") != today][: a.max]
    got = {}
    for i, au in enumerate(todo):
        try:
            data = oc("collection", au, "--until", until, "--limit", "400", timeout=900)
            items = data.get("posts", []) if isinstance(data, dict) else data
            tws = [t for t in items if isinstance(t, dict) and not t.get("is_retweet")
                   and str(t.get("author", "")).lower() == au.lower()]
            neg = [row(t, f"author-unliked:{au}") for t in tws if str(t.get("id")) not in liked]
            write_merge(DIR / "author-unliked.jsonl", neg)
            state[au] = {"date": today, "tweets": len(tws), "unliked": len(neg)}
            got[au] = len(neg)
        except Exception as e:
            got[au] = f"停：{e}"
            state_f.write_text(json.dumps(state, ensure_ascii=False, indent=1))
            break   # 多半是限流，下次接着抓
        state_f.write_text(json.dumps(state, ensure_ascii=False, indent=1))
        if i < len(todo) - 1:
            time.sleep(a.sleep)
    print(json.dumps(got, ensure_ascii=False))


def cmd_stats(_):
    out = {}
    for f in sorted(DIR.glob("*.jsonl")):
        if not f.name.endswith(".raw.jsonl"):
            out[f.stem] = sum(1 for l in f.read_text().split("\n") if l.strip())
    print(json.dumps(out, ensure_ascii=False))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("bookmarks")
    p = sub.add_parser("own"); p.add_argument("--days", type=int, default=180)
    p = sub.add_parser("authors"); p.add_argument("--max", type=int, default=5); p.add_argument("--sleep", type=int, default=90)
    sub.add_parser("stats")
    a = ap.parse_args()
    {"bookmarks": cmd_bookmarks, "own": cmd_own, "authors": cmd_authors, "stats": cmd_stats}[a.cmd](a)


if __name__ == "__main__":
    main()
