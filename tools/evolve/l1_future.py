#!/usr/bin/env python3
"""L1 未来考题：冠军定下以后 Luke 新点的赞，配同一时段刷到没点的，盲打分；再加上日报回答。
见自我优化 spec「2026-10-24 晚：前瞻考题没题了」，Luke 选了 A 加 C。

为什么不只靠首页快照：Luke 点赞的多是"为你推荐"里的热帖，快照只抓得到一小部分，
10-21 到 10-24 他新点的 30 条赞里只有 2 条在快照里，快照考法连续 3 天没题。

用法：
  python3 tools/evolve/l1_future.py update [--neg-foryou 25] [--neg-following 15]
      收新题、给还没打分的打分。每轮都可以跑，没有新题就什么都不做
  python3 tools/evolve/l1_future.py report [--write]
      只算当前冠军上任以后的：A 新点赞配对考，C 日报回答。--write 把成绩追加进 private/l1/metrics.jsonl（周报用）

做法：
- 正样本（A）：点赞对账（private/explore/likes/<时间>.jsonl，每份是最近 100 条点赞，新的排在最前面）里，
  冠军上任以后才第一次出现、而且排在列表最前面那一段的点赞。只认最前面那一段：取消点赞时，列表底部会滑进一条旧赞，不能当成新点的
- 负样本（A）：冠军上任以后的首页快照里没被点赞的，每份按编号哈希固定抽"为你推荐"25 条、关注流 15 条；
  快照满 48 小时才算负样本（他可能还会点），期间被点了赞的改算正样本
- 打分用冠军原样（档案 + k 条相似点赞），相似点赞只从冠军上任时已知的点赞里找，正负样本条件一样。只用本地 Qwen，连不上就留到下一轮
- 正样本来自 Luke 刷到的所有地方，负样本来自快照抽样，两边来源不完全一样，成绩会偏乐观，所以按负样本来源分开报
- 日报（C）：冠军上任以后出的日报里 Luke 答过的条目，日报打分时的概率对他的"想看 / 不想看"。两个打分引擎口径不同，分开算
"""
import argparse, datetime as dt, hashlib, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import l1_eval as E  # noqa: E402
import l1_prospect as P  # noqa: E402
from l1_report import auc_ci  # noqa: E402

LIKES = E.PRIVATE / "explore" / "likes"
PRO = E.PRIVATE / "l1" / "prospective"
ITEMS = E.PRIVATE / "l1" / "future" / "items.jsonl"
EXPLORE_LABELS = E.PRIVATE / "explore" / "labels.jsonl"
FMT = "%Y%m%d-%H%M"


def jl(p):
    return [json.loads(l) for l in p.read_text().split("\n") if l.strip()] if p.exists() else []


def champion():
    return json.loads((E.PRIVATE / "l1" / "champion.json").read_text())


def stamp(p):
    return p.stem[-13:]   # likes pulls are <stamp>.jsonl, snapshots snapshot-<stamp>.jsonl


def likes_after(since):
    """Likes made after `since`, from the reconciliation pulls: {id: row}. Also returns every like id seen in any pull."""
    seen, new, prev = set(), {}, None
    for f in sorted(LIKES.glob("[0-9]*.jsonl")):
        rows = jl(f)
        if prev is not None:
            for r in rows:   # the newest likes come first; stop at the first one already seen
                if str(r["id"]) in seen:
                    break
                if prev >= since:
                    new[str(r["id"])] = {**r, "first_seen": stamp(f)}
        seen |= {str(r["id"]) for r in rows}
        prev = stamp(f)
    return new, seen


def liked_now(since):
    _, seen = likes_after(since)
    return seen | P.liked_ids_in_repo() | {r["id"] for r in E.labels() if r["label"] == 1}


def cmd_update(a):
    ch = champion()
    since = ch["since"]
    items = jl(ITEMS)
    have = {(r["id"], r["champ"]) for r in items}
    new_likes, _ = likes_after(since)
    liked = liked_now(since)
    add = []
    for i, r in new_likes.items():
        if (i, since) not in have:
            add.append(dict(id=i, champ=since, role="pos", src=r["first_seen"], feed="like",
                            author=r.get("author", ""), text=r.get("text", "")[:1500]))
            have.add((i, since))
    sampled = {r["src"] for r in items if r["role"] == "neg" and r["champ"] == since}
    for s in sorted(PRO.glob("snapshot-*.jsonl")):
        if stamp(s) < since or stamp(s) in sampled:   # each snapshot is sampled once
            continue
        rows = [r for r in jl(s) if r["id"] not in liked and (r["id"], since) not in have]
        for feed, n in (("for-you", a.neg_foryou), ("following", a.neg_following)):
            pick = sorted((r for r in rows if r.get("feed") == feed), key=lambda r: hashlib.md5(r["id"].encode()).hexdigest())[:n]
            add += [dict(id=r["id"], champ=since, role="neg", src=stamp(s), feed=feed, author=r.get("author", ""), text=r["text"])
                    for r in pick]
            have |= {(r["id"], since) for r in pick}
    items += add
    ITEMS.parent.mkdir(parents=True, exist_ok=True)
    save = lambda: ITEMS.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in items))  # noqa: E731
    save()
    todo = [r for r in items if r["champ"] == since and r.get("p") is None]
    print(f"冠军 {since}：新收 {len(add)} 道题（正 {sum(r['role'] == 'pos' for r in add)}），待打分 {len(todo)} 道")
    if todo:
        E.load_env()
        profile = (E.PRIVATE / "luke" / ch["profile"]).read_text()
        # 相似点赞只从冠军上任时已知的里找：去掉之后新点的赞、之后日报里答的，以及考题本身
        frozen = set(new_likes) | {r["key"][2:] for r in jl(EXPLORE_LABELS) if r.get("digest", "") >= since} | {r["id"] for r in items}
        index = E.Index(E.liked_docs(frozen)) if ch["cond"] in ("c2", "c3") else None
        done = 0
        for r in todo:
            try:
                r["p"] = E.qwen(E.prompt(r, ch["cond"], profile, index.top(r["text"], ch.get("k", 8)) if index else []))
            except Exception as e:   # 本地 Qwen 连不上：不换引擎（概率口径不同），留到下一轮
                print(f"Qwen 打分出错，打了 {done} 道先停：{e}")
                break
            r["scored_at"] = f"{dt.datetime.now():{FMT}}"
            done += 1
            if done % 20 == 0:
                save()
        save()
        print(f"打分 {done} 道")


def summary(name, rows):
    pos = sum(r["label"] for r in rows)
    if not 0 < pos < len(rows):
        return dict(name=name, n=len(rows), n_pos=pos, note="正负样本不全，算不出")
    m = E.metrics(rows)
    lo, hi = auc_ci(rows)
    return dict(name=name, n=len(rows), n_pos=pos, auc=m["auc"], auc_ci90=[lo, hi], mean_p_pos=m["mean_p_pos"], mean_p_neg=m["mean_p_neg"])


def cmd_report(a):
    ch = champion()
    since = ch["since"]
    now = dt.datetime.now()
    liked = liked_now(since)
    items = [r for r in jl(ITEMS) if r["champ"] == since and r.get("p") is not None]
    pos = [r for r in items if r["role"] == "pos" or r["id"] in liked]
    neg = [r for r in items if r["role"] == "neg" and r["id"] not in liked
           and now - dt.datetime.strptime(r["src"], FMT) >= dt.timedelta(hours=48)]
    lab = lambda rs, y: [{"id": r["id"], "p": r["p"], "label": y} for r in rs]  # noqa: E731
    out = [summary("A 新点赞 vs 全部没点的", lab(pos, 1) + lab(neg, 0)),
           summary("A 新点赞 vs 为你推荐里没点的", lab(pos, 1) + lab([r for r in neg if r["feed"] == "for-you"], 0)),
           summary("A 新点赞 vs 关注流里没点的", lab(pos, 1) + lab([r for r in neg if r["feed"] == "following"], 0))]
    digest = [r for r in jl(EXPLORE_LABELS) if r.get("source", "digest") == "digest" and r.get("digest", "") >= since and r.get("p") is not None]
    for sc in sorted({r.get("scorer", "qwen") for r in digest}):
        sub = [r for r in digest if r.get("scorer", "qwen") == sc]
        out.append({**summary(f"C 日报回答（{sc} 打分）", [{"id": r["key"], "p": r["p"], "label": r["label"]} for r in sub]),
                    "digests": len({r["digest"] for r in sub}), "engine": sc})
    if not digest:
        out.append(dict(name="C 日报回答", n=0, n_pos=0, note="冠军上任以后还没有答过的日报"))
    print(f"冠军 {ch['profile']}（上任 {since}），未来考题成绩：")
    for o in out:
        print(json.dumps(o, ensure_ascii=False))
    if a.write:
        with open(E.PRIVATE / "l1" / "metrics.jsonl", "a") as f:
            for o in out:
                f.write(json.dumps(dict(time=f"{now:{FMT}}", testset=o["name"], engine=o.get("engine", "qwen"), cond=ch["cond"],
                                        profile=ch["profile"], tag="future", champ=since,
                                        **{k: v for k, v in o.items() if k not in ("name", "engine")}),
                                   ensure_ascii=False) + "\n")
        print("已追加进 private/l1/metrics.jsonl")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("update"); p.add_argument("--neg-foryou", type=int, default=25); p.add_argument("--neg-following", type=int, default=15)
    p = sub.add_parser("report"); p.add_argument("--write", action="store_true")
    a = ap.parse_args()
    if a.cmd == "report":
        cmd_report(a)
        return
    # 改题库的命令排队执行：每小时的循环和手动跑可能同时读改写 items.jsonl
    import fcntl
    ITEMS.parent.mkdir(parents=True, exist_ok=True)
    with open(ITEMS.parent / ".lock", "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        cmd_update(a)


if __name__ == "__main__":
    main()
