#!/usr/bin/env python3
"""L1 试跑：在已有评测结果上试候选改动，和冠军做成对比较。不重跑模型，几秒钟出结果。

做法照 Harness²（见 docs/2026-10-18-self-evolution-spec.md 第 13～15 条）：
每轮提两个候选，一个通用（不管是谁都会犯的毛病），一个针对 Luke；参数只在开发集上挑，
测试集上和冠军成对比较（同一批题重抽样），给出"候选更好"的概率。

候选：
  dedup   通用：和他已点赞的某条推文几乎一样（检索相似度高于阈值），概率打折。同一件事他一般只点一次
  jev     针对 Luke：本地 Qwen（看过档案和例子）和 Jev（只看推文）按名次加权平均

用法：
  python3 tools/evolve/l1_probe.py <testset.jsonl> --champion <run.jsonl> --jev <run.jsonl>
"""
import argparse, json, random, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import l1_eval as E  # noqa: E402
from l1_report import split  # noqa: E402


def load(p):
    return {r["id"]: r for r in (json.loads(l) for l in Path(p).read_text().split("\n") if l.strip())}


def ranks(d):
    order = sorted(d, key=lambda k: d[k])
    return {k: i / (len(order) - 1) for i, k in enumerate(order)}


def auc(ids, p, y):
    return E.metrics([{"p": p[i], "label": y[i]} for i in ids])["auc"]


def paired(ids, pa, pb, y, n=2000, seed=3):
    """Bootstrap the same test items for both versions; return mean AUC gain and P(gain > 0)."""
    rnd, gains = random.Random(seed), []
    for _ in range(n):
        s = [rnd.choice(ids) for _ in ids]
        if 0 < sum(y[i] for i in s) < len(s):
            gains.append(auc(s, pb, y) - auc(s, pa, y))
    return sum(gains) / len(gains), sum(g > 0 for g in gains) / len(gains)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("testset")
    ap.add_argument("--champion", required=True)
    ap.add_argument("--jev", required=True)
    a = ap.parse_args()
    rows = load(a.testset)
    champ, jev = load(a.champion), load(a.jev)
    y = {i: r["label"] for i, r in rows.items()}
    dev = [i for i in rows if split(i) == "dev"]
    test = [i for i in rows if split(i) == "test"]
    p0 = {i: champ[i]["p"] for i in rows}

    # candidate 1 (generic): near-duplicate of something already liked
    idx = E.Index(E.liked_docs(set(rows)))
    sim = {}
    for i, r in rows.items():
        q = r["text"]
        top = idx.top(q, 1)
        import collections, math
        qv = collections.Counter(E.grams(q))
        qn = math.sqrt(sum((tf * idx.idf.get(g, 0)) ** 2 for g, tf in qv.items())) or 1
        j = idx.docs.index(top[0])
        sim[i] = sum(tf * idx.vecs[j].get(g, 0) * idx.idf.get(g, 0) ** 2 for g, tf in qv.items()) / (qn * idx.norms[j])
    best = None
    for thr in (0.3, 0.4, 0.5, 0.6, 0.7):
        for cut in (0.3, 0.5, 0.8):
            p1 = {i: p0[i] * (1 - cut) if sim[i] > thr else p0[i] for i in rows}
            s = auc(dev, p1, y)
            if best is None or s > best[0]:
                best = (s, thr, cut, p1)
    _, thr, cut, p_dedup = best
    print(f"相似度分布：中位 {sorted(sim.values())[len(sim) // 2]:.2f}，超过 {thr} 的 {sum(v > thr for v in sim.values())} 条（正样本 {sum(v > thr and y[i] for i, v in sim.items())} 条）")

    # candidate 2 (Luke-specific): blend local Qwen (knows Luke) with Jev (generic prior), by rank
    rq, rj = ranks(p0), ranks({i: jev[i]["p"] for i in rows})
    best = None
    for w in (0.5, 0.6, 0.7, 0.8, 0.9):
        p2 = {i: w * rq[i] + (1 - w) * rj[i] for i in rows}
        s = auc(dev, p2, y)
        if best is None or s > best[0]:
            best = (s, w, p2)
    _, w, p_blend = best

    print(f"冠军：开发集 AUC {auc(dev, p0, y)}，测试集 AUC {auc(test, p0, y)}")
    for name, desc, p in (("dedup", f"重复降权（相似度>{thr} 打 {int(cut * 100)}% 折）", p_dedup),
                          ("jev", f"Qwen 和 Jev 按名次加权（Qwen 占 {w}）", p_blend)):
        g, pr = paired(test, p0, p, y)
        print(f"候选 {name}：{desc}：开发集 AUC {auc(dev, p, y)}，测试集 AUC {auc(test, p, y)}，"
              f"成对比较平均 {g:+.3f}，比冠军好的概率 {pr:.0%}")


if __name__ == "__main__":
    main()
