#!/usr/bin/env python3
"""后训练第一步：训一个本地小模型预测"Luke 会不会点赞"，在未来的考题上和冠军（本地 Qwen + 档案 + 例子）成对比。

方案见 docs/2026-10-18-self-evolution-spec.md（流程五"用哪个模型"：负样本 1,000 条以上、测试集 500 道以上、
Luke 的标签 100 条以上，先训小模型和冠军比，赢了再考虑给本地 Qwen 做 LoRA）。Luke 2026-10-21 选了：先把流程搭好，到门槛就开训。

小模型故意做得很简单：字的二元组和作者，哈希成特征，用 numpy 做带 L2 的逻辑回归。目的是先看"用 Luke 的行为数据直接训"
能不能在未来考题上赢过"大模型 + 提示词"，赢了再上 LoRA。全部数据在本地，只存 private/l1/train/。

用法：
  l1_train.py ready     三个门槛各差多少
  l1_train.py run       拼数据、训练、在已对答案的快照上和冠军成对比较，记成绩（不够门槛也能跑，但会标"未达门槛"）
"""
import argparse, collections, datetime as dt, glob, json, math, re, sys, zlib
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import l1_eval as E  # noqa: E402
import l1_probe as P  # noqa: E402

PRO = E.PRIVATE / "l1" / "prospective"
EXTRA = E.PRIVATE / "l1" / "extra"
OUT = E.PRIVATE / "l1" / "train"
GATE = {"luke_labels": 100, "test": 500, "negatives": 1000}
DIM = 1 << 18   # 用 crc32 做哈希（Python 自带的 hash 每次运行都变，存下的模型就没法复用）


def jl(p):
    p = Path(p)
    return [json.loads(l) for l in p.read_text().split("\n") if l.strip()] if p.exists() else []


def liked_ids():
    ids = {d["id"] for d in E.liked_docs(set())}
    for f in glob.glob(str(E.PRIVATE / "explore" / "likes" / "2*.jsonl")):
        ids |= {str(r["id"]) for r in jl(f)}
    return ids


def scored_snapshots():
    done = set((PRO / "scored.txt").read_text().split()) if (PRO / "scored.txt").exists() else set()
    return sorted(PRO / s for s in done if (PRO / s).exists())


def luke_labels():
    """Luke 亲口给的：点赞预测里的提问，加上日报里的想看 / 不想看。"""
    rows = [{"id": r["id"], "text": r["text"], "author": r.get("author", ""), "label": r["label"]} for r in E.labels()]
    for r in jl(E.PRIVATE / "explore" / "labels.jsonl"):
        if r.get("source", "digest") == "digest":
            rows.append({"id": r["key"], "text": (r.get("title", "") + "\n" + r.get("text", "")), "author": "", "label": r["label"]})
    return rows


def build():
    liked = liked_ids()
    told = {r["id"]: r["label"] for r in luke_labels()}
    test = {}
    for s in scored_snapshots():   # 考题：已经满 48 小时、对过答案的快照（未来的、真实刷到的推文）
        for r in jl(s):
            test.setdefault(r["id"], {**r, "label": told.get(r["id"], int(r["id"] in liked)), "snap": s.name})
    train = {}
    for d in E.liked_docs(set(test)):                                   # 点赞过的
        train[d["id"]] = {"id": d["id"], "text": d["text"], "author": "", "label": 1, "w": 1.0}
    for r in jl(EXTRA / "bookmarks.jsonl"):                             # 书签：更用心的"留着"
        if r["id"] not in test:
            train[r["id"]] = {**r, "label": 1, "w": 1.5}
    for r in luke_labels():                                              # Luke 亲口说的，权重最高
        if r["id"] not in test:
            train[r["id"]] = {**r, "w": 3.0}
    for f in sorted(PRO.glob("snapshot-*.jsonl")):                      # 刷到但没点：只用不当考题的快照
        if f in scored_snapshots():
            continue
        for r in jl(f):
            if r["id"] not in train and r["id"] not in test:
                train[r["id"]] = {**r, "label": int(r["id"] in liked), "w": 0.7}
    for r in jl(EXTRA / "author-unliked.jsonl"):                        # 常看作者没点的：弱负样本
        if r["id"] not in train and r["id"] not in test:
            train[r["id"]] = {**r, "label": 0, "w": 0.5}
    return list(train.values()), list(test.values())


def feats(r):
    s = re.sub(r"https?://\S+", " ", (r.get("text") or "").lower())
    s = re.sub(r"\s+", " ", s)[:1500]
    idx = collections.Counter(zlib.crc32(("g:" + s[i:i + 2]).encode()) % DIM for i in range(len(s) - 1))
    if r.get("author"):
        idx[zlib.crc32(("a:" + r["author"].lower()).encode()) % DIM] += 3
    n = math.sqrt(sum(v * v for v in idx.values())) or 1
    return {k: v / n for k, v in idx.items()}


def fit(rows, l2=1e-4, epochs=8, lr=0.5):
    w = np.zeros(DIM)
    b = 0.0
    pos = sum(r["w"] for r in rows if r["label"] == 1)
    neg = sum(r["w"] for r in rows if r["label"] == 0) or 1
    cw = {1: (pos + neg) / (2 * pos), 0: (pos + neg) / (2 * neg)}   # 正负样本不平衡，按类别加权
    X = [feats(r) for r in rows]
    rng = np.random.default_rng(7)
    for ep in range(epochs):
        for i in rng.permutation(len(rows)):
            x, y = X[i], rows[i]["label"]
            z = b + sum(w[k] * v for k, v in x.items())
            p = 1 / (1 + math.exp(-max(min(z, 30), -30)))
            g = (p - y) * rows[i]["w"] * cw[y]
            step = lr / (1 + ep)
            for k, v in x.items():
                w[k] -= step * (g * v + l2 * w[k])
            b -= step * g
    return w, b


def predict(w, b, r):
    z = b + sum(w[k] * v for k, v in feats(r).items())
    return 1 / (1 + math.exp(-max(min(z, 30), -30)))


def cmd_ready(_):
    train, test = build()
    n_luke = len(luke_labels())
    n_neg = sum(1 for r in train if r["label"] == 0)
    st = {"luke_labels": n_luke, "test": len(test), "negatives": n_neg}
    print(json.dumps({k: f"{v}/{GATE[k]}" for k, v in st.items()} | {"ready": all(st[k] >= GATE[k] for k in GATE)}, ensure_ascii=False))
    return st


def cmd_run(_):
    st = cmd_ready(_)
    train, test = build()
    if not test or not any(r["label"] for r in test):
        sys.exit("还没有对过答案、又有点赞的考题")
    w, b = fit(train)
    small = {r["id"]: predict(w, b, r) for r in test}
    y = {r["id"]: r["label"] for r in test}
    # 冠军在同一批考题上的预测（快照对应的 c2 预测文件）
    champ = {}
    for s in {r["snap"] for r in test}:
        for f in PRO.glob(s.replace("snapshot", "pred").replace(".jsonl", "") + "-c2-*.jsonl"):
            champ.update({x["id"]: x["p"] for x in jl(f)})
    ids = [i for i in small if i in champ]
    res = {"time": f"{dt.datetime.now():%Y%m%d-%H%M}", "train": len(train), "train_pos": sum(r["label"] for r in train),
           "test": len(test), "test_pos": sum(y.values()), "paired": len(ids), "gate": st,
           "ready": all(st[k] >= GATE[k] for k in GATE)}
    if ids and 0 < sum(y[i] for i in ids) < len(ids):
        res["auc_small"] = P.auc(ids, small, y)
        res["auc_champion"] = P.auc(ids, champ, y)
        gain, prob = P.paired(ids, champ, small, y)
        res["gain"], res["p_better"] = round(gain, 3), round(prob, 3)
        # 两个排名平均一下：小模型和冠军看的东西不一样，合起来可能更好
        rs, rc = P.ranks({i: small[i] for i in ids}), P.ranks({i: champ[i] for i in ids})
        mix = {i: (rs[i] + rc[i]) / 2 for i in ids}
        res["auc_mix"] = P.auc(ids, mix, y)
        g2, p2 = P.paired(ids, champ, mix, y)
        res["mix_gain"], res["mix_p_better"] = round(g2, 3), round(p2, 3)
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / "metrics.jsonl", "a") as f:
        f.write(json.dumps(res, ensure_ascii=False) + "\n")
    np.savez_compressed(OUT / f"small-{res['time']}.npz", w=w, b=b)
    print(json.dumps(res, ensure_ascii=False, indent=1))
    if res.get("p_better", 0) >= 0.8 or res.get("mix_p_better", 0) >= 0.8:
        print("比冠军好的概率到 80%：按流程五可以采用；" + ("已达门槛" if res["ready"] else "但还没达到数据门槛，先当苗头，不换冠军"))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("ready")
    sub.add_parser("run")
    a = ap.parse_args()
    {"ready": cmd_ready, "run": cmd_run}[a.cmd](a)


if __name__ == "__main__":
    main()
