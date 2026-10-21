#!/usr/bin/env python3
"""不训练，把 Luke 的行为数据提炼成一份"口味 skill"，判断前先读它，看能不能比冠军准。

Luke 2026-10-21："如果不训练，直接让这些数据成为 memory，类似一个 skill，让模型在调用之前引用这个 skill，是不是也能达到效果。你可以试试。"

做法：
  build   Opus 读点赞样本、常看作者没点的样本、Luke 自己发的帖、确认过的规律，写成 private/luke/taste-skill.md。
          不用 Luke 亲口答过的题，也不用当考题的快照（那是考试用的，先看答案再考就不算数）
  eval    同一批考题上比几种做法：冠军（初版档案 + 8 条相似点赞）、skill + 8 条相似点赞、skill + 相似点赞 + 相似没点、
          Opus 读 skill 直接判。考题两套：T1 已对过答案的首页快照（未来的真实推文），T2 Luke 亲口答过的题（难题）
  refresh 每周一次：用新攒的数据写一版候选 skill（不覆盖当前冠军），和冠军在同一批考题上成对比较；
          未来考题上好的概率到 80%、难题上不变差（好的概率至少 0.5），才换成新冠军
全部数据只在本地和 Opus 之间（Luke 2026-10-20 同意 Opus 看私人资料）。结果记进 private/l1/skill/。
Luke 2026-10-21 定：不做后训练，口味就靠这份 skill 一版一版刻画。
"""
import argparse, collections, datetime as dt, json, random, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import l1_eval as E  # noqa: E402
import l1_probe as P  # noqa: E402
import l1_train as T  # noqa: E402
import opus_judge as OJ  # noqa: E402

SKILL = E.PRIVATE / "luke" / "taste-skill.md"
OUT = E.PRIVATE / "l1" / "skill"


def test_sets():
    liked = T.liked_ids()
    told = {r["id"]: r["label"] for r in T.luke_labels()}
    t1 = {}
    for s in T.scored_snapshots():
        for r in T.jl(s):
            t1.setdefault(r["id"], {"id": r["id"], "author": r.get("author", ""), "text": r["text"],
                                    "label": told.get(r["id"], int(r["id"] in liked)), "snap": s.name})
    # 难题只留最近 50 道当考题；更早的亲口回答拿去提炼 skill（不然 skill 永远学不到他亲口说的）
    told_rows = [r for r in T.luke_labels() if r["id"] not in t1][-50:]
    t2 = {r["id"]: {**r, "text": r["text"][:1200]} for r in told_rows}
    return list(t1.values()), list(t2.values())


def cmd_build(a):
    t1, t2 = test_sets()
    ban = {r["id"] for r in t1 + t2}
    rng = random.Random(21)
    liked = [d for d in E.liked_docs(ban)]
    unliked = [r for r in T.jl(T.EXTRA / "author-unliked.jsonl") if r["id"] not in ban]
    own = T.jl(T.EXTRA / "own-LukeLiu95.jsonl")
    authors = collections.Counter()
    for f in (E.REPO / "clips").glob("*.md"):
        m = re.search(r'^author:.*\(@([A-Za-z0-9_]+)\)', f.read_text().split("\n---", 1)[0], re.M)
        if m:
            authors[m.group(1)] += 1
    parts = [
        "【任务】下面是 Luke 在 X 上的真实行为数据。请写一份给判断模型用的 skill：读完它，判断模型就能预测 Luke 刷到一条内容会不会点赞或想看。"
        "要求：中文；1,500 字以内；具体，带例子；不要空话；写清楚他会点的、他不点的、拿不准时怎么判；"
        "结论要能从下面的数据里看出来，看不出来的不要写；不写他的隐私细节。",
        "【旧档案（2026-10-18 初版，部分暗线已被推翻）】\n" + (E.PRIVATE / "luke" / "profile.md").read_text()[:2500],
        "【他亲口确认过的规律】\n" + (E.PRIVATE / "luke" / "confirmed.md").read_text(),
        "【常看作者和被点赞次数（前 30）】\n" + "，".join(f"@{a} {n}" for a, n in authors.most_common(30)),
        "【他点过赞的推文（随机 150 条，截断）】\n" + "\n".join(f"- {d['text'][:180]}" for d in rng.sample(liked, min(150, len(liked)))),
        "【他常看的作者最近发了、他没点赞的推文（随机 80 条，截断；只能说明大概率刷到过没点）】\n" +
        "\n".join(f"- @{r['author']}：{r['text'][:160]}" for r in rng.sample(unliked, min(80, len(unliked)))),
        "【他自己发的帖（随机 40 条，截断）】\n" + "\n".join(f"- {r['text'][:160]}" for r in rng.sample(own, min(40, len(own)))),
        "【他亲口说过想看 / 不想看的（不当考题的那部分，最值钱）】\n" + ("\n".join(
            f"- {'想看' if r['label'] else '不想看'}：{r['text'][:160]}" for r in T.luke_labels() if r["id"] not in ban) or "（暂时没有）"),
        '只输出 JSON：{"skill": "skill 正文（markdown）"}',
    ]
    out = OJ.ask_json("你是一个擅长从行为数据里归纳个人口味的分析师。只输出 JSON。", "\n\n".join(parts), timeout=900)
    head = f"# Luke 的阅读口味（判断前先读）\n\n> 由 `tools/evolve/l1_skill.py build` 在 {dt.date.today()} 用 Opus 从行为数据提炼；没用 Luke 亲口答过的题和当考题的快照。\n\n"
    target = Path(getattr(a, "out", "") or SKILL)
    target.write_text(head + out["skill"].strip() + "\n")
    print(f"写好 {target}，{len(out['skill'])} 字")
    return target


def qwen_score(rows, mode, profile, skill, pos_index, neg_index):
    """mode：champ＝旧档案；skill＝口味 skill + 相似点赞；skill_neg＝再加相似没点。profile 参数就是 champ 用的那份文字。"""
    out = {}
    for r in rows:
        parts = []
        if mode == "champ":
            parts.append("【Luke 的档案】\n" + profile)
        else:
            parts.append("【Luke 的阅读口味】\n" + skill)
        ex = pos_index.top(r["text"], 8 if mode != "skill_neg" else 6)
        parts.append("【他以前点赞过的相似推文】\n" + "\n\n".join(f"- {e['text'][:400]}" for e in ex))
        if mode == "skill_neg":
            parts.append("【他刷到过、但没有点赞的相似推文】\n" + "\n\n".join(f"- {e['text'][:400]}" for e in neg_index.top(r["text"], 4)))
        parts.append(f"【要判断的内容】作者 @{r.get('author', '')}\n{r['text'][:1200]}")
        parts.append("Luke 会点赞或想看这条吗？A 会，B 不会。只回答一个字母。")
        out[r["id"]] = E.qwen("\n\n".join(parts))
    return out


def opus_score(rows, skill):
    out = {}
    for b in range(0, len(rows), 20):
        batch = rows[b:b + 20]
        body = "\n\n".join(f"[{i}] 作者 @{r.get('author', '')}\n{r['text'][:700]}" for i, r in enumerate(batch))
        res = OJ.ask_json("你在模拟一个具体的人 Luke，判断他会不会点赞或想看。只输出 JSON。",
                          f"【Luke 的阅读口味】\n{skill}\n\n【要判断的内容】\n{body}\n\n"
                          f'按编号输出他会点赞或想看的概率（0 到 1）：{{"编号": 概率}}')
        for i, r in enumerate(batch):
            v = res.get(str(i))
            if v is not None:
                out[r["id"]] = max(0.0, min(1.0, float(v)))
    return out


def summary(name, rows, preds, champ):
    y = {r["id"]: r["label"] for r in rows}
    ids = [i for i in y if i in preds and i in champ]
    if not ids or not (0 < sum(y[i] for i in ids) < len(ids)):
        return {"cond": name, "n": len(ids), "note": "正负样本不全，算不了"}
    y1 = [preds[i] for i in ids if y[i] == 1]
    y0 = [preds[i] for i in ids if y[i] == 0]
    rec = {"cond": name, "n": len(ids), "pos": len(y1), "auc": P.auc(ids, preds, y),
           "mean_p_want": round(sum(y1) / len(y1), 3), "mean_p_skip": round(sum(y0) / len(y0), 3)}
    if name != "champ":
        g, pb = P.paired(ids, champ, preds, y)
        rec.update(gain=round(g, 3), p_better=round(pb, 3))
    return rec


def cmd_eval(a):
    E.load_env()
    if not SKILL.exists():
        sys.exit("先跑 build")
    skill = SKILL.read_text()
    profile = (E.PRIVATE / "luke" / "profile.md").read_text()
    t1, t2 = test_sets()
    results = {}
    for tname, rows in (("T1 未来快照", t1), ("T2 Luke 亲口答过的", t2)):
        ban = {r["id"] for r in t1 + t2}
        pos_index = E.Index(E.liked_docs(ban))
        negs = [{"id": r["id"], "text": r["text"][:600]} for r in T.jl(T.EXTRA / "author-unliked.jsonl") if r["id"] not in ban]
        neg_index = E.Index(negs)
        champ = {}
        if tname.startswith("T1"):   # 冠军在快照上已有预测，直接用
            for s in {r["snap"] for r in rows}:
                for f in T.PRO.glob(s.replace("snapshot", "pred").replace(".jsonl", "") + "-c2-*.jsonl"):
                    champ.update({x["id"]: x["p"] for x in T.jl(f)})
        missing = [r for r in rows if r["id"] not in champ]
        champ.update(qwen_score(missing, "champ", profile, skill, pos_index, neg_index))
        preds = {"champ": champ}
        for mode in a.modes:
            if mode == "skill_opus":
                preds[mode] = opus_score(rows, skill)
            else:
                preds[mode] = qwen_score(rows, mode, profile, skill, pos_index, neg_index)
            print(tname, mode, "完成", flush=True)
        results[tname] = [summary(k, rows, v, champ) for k, v in preds.items()]
        OUT.mkdir(parents=True, exist_ok=True)
        stamp = dt.datetime.now().strftime("%Y%m%d-%H%M")
        (OUT / f"preds-{stamp}-{tname[:2]}.json").write_text(json.dumps(preds))
    with open(OUT / "metrics.jsonl", "a") as f:
        f.write(json.dumps({"time": dt.datetime.now().strftime("%Y%m%d-%H%M"), "results": results}, ensure_ascii=False) + "\n")
    print(json.dumps(results, ensure_ascii=False, indent=1))


def cmd_refresh(_):
    """生成候选 skill → 当前冠军（skill + 8 条相似点赞）和候选在同一批考题上比 → 过门槛才换。"""
    E.load_env()
    OUT.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M")
    cand = OUT / f"candidate-{stamp}.md"
    cmd_build(argparse.Namespace(out=str(cand)))
    champ_skill, cand_skill = SKILL.read_text(), cand.read_text()
    t1, t2 = test_sets()
    ban = {r["id"] for r in t1 + t2}
    pos_index = E.Index(E.liked_docs(ban))
    res = {}
    for tname, rows in (("T1", t1), ("T2", t2)):
        a_ = qwen_score(rows, "skill", "", champ_skill, pos_index, None)
        b_ = qwen_score(rows, "skill", "", cand_skill, pos_index, None)
        y = {r["id"]: r["label"] for r in rows}
        ids = [i for i in y if i in a_ and i in b_]
        if ids and 0 < sum(y[i] for i in ids) < len(ids):
            g, pb = P.paired(ids, a_, b_, y)
            res[tname] = {"n": len(ids), "auc_champion": P.auc(ids, a_, y), "auc_candidate": P.auc(ids, b_, y),
                          "gain": round(g, 3), "p_better": round(pb, 3)}
    adopt = res.get("T1", {}).get("p_better", 0) >= 0.8 and res.get("T2", {}).get("p_better", 0.5) >= 0.5
    rec = {"time": stamp, "candidate": cand.name, "results": res, "adopted": adopt}
    with open(OUT / "refresh.jsonl", "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    if adopt:
        (OUT / f"retired-{stamp}.md").write_text(champ_skill)
        SKILL.write_text(cand_skill)
        cp = E.PRIVATE / "l1" / "champion.json"
        c = json.loads(cp.read_text())
        c.update(profile="taste-skill.md", since=stamp, test_auc=res["T1"]["auc_candidate"],
                 hard_auc=res.get("T2", {}).get("auc_candidate"), why=f"skill 每周重提炼：{cand.name} 赢了上一版")
        cp.write_text(json.dumps(c, ensure_ascii=False, indent=1))
    print(json.dumps(rec, ensure_ascii=False, indent=1))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("build"); p.add_argument("--out", default="")
    sub.add_parser("refresh")
    p = sub.add_parser("eval"); p.add_argument("--modes", nargs="+", default=["skill", "skill_neg", "skill_opus"])
    a = ap.parse_args()
    {"build": cmd_build, "eval": cmd_eval, "refresh": cmd_refresh}[a.cmd](a)


if __name__ == "__main__":
    main()
