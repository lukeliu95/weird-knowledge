#!/usr/bin/env python3
"""L1 成绩表：把每次评测按开发集 / 测试集分开算成绩。

改档案只看开发集的错题，是否保留改动看测试集（避免把答案背进档案）。
分法固定：推文编号的 md5 是偶数进开发集，奇数进测试集。

用法：
  python3 tools/evolve/l1_report.py [--since 20261019]
"""
import argparse, glob, hashlib, json, random, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import l1_eval as E  # noqa: E402


def split(tid):
    return "dev" if int(hashlib.md5(tid.encode()).hexdigest(), 16) % 2 == 0 else "test"


def auc_ci(rows, n=1000, seed=1):
    """90% bootstrap interval of AUC, so a change smaller than the noise is not mistaken for progress."""
    rnd = random.Random(seed)
    vals = []
    for _ in range(n):
        s = [rnd.choice(rows) for _ in rows]
        if 0 < sum(r["label"] for r in s) < len(s):
            vals.append(E.metrics(s)["auc"])
    vals.sort()
    return vals[int(0.05 * len(vals))], vals[int(0.95 * len(vals))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", default="")
    a = ap.parse_args()
    metas = {}
    for l in (E.PRIVATE / "l1" / "metrics.jsonl").read_text().split("\n"):
        if l.strip():
            m = json.loads(l)
            metas[(m["time"], m["engine"], m["cond"])] = m
    print("| 时间 | 引擎 | 条件 | 档案 | 开发集 AUC | 开发集准确率 | 测试集 AUC | 测试集 AUC 90% 区间 | 测试集准确率 | 测试集校准误差 |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for f in sorted(glob.glob(str(E.PRIVATE / "l1" / "runs" / "*.jsonl"))):
        stem = Path(f).stem
        t, engine, cond = stem[:13], stem.split("-")[2], stem.split("-")[3]
        if t < a.since:
            continue
        meta = metas.get((t, engine, cond), {})
        if meta.get("tag") == "smoke":
            continue
        rows = [json.loads(l) for l in Path(f).read_text().split("\n") if l.strip()]
        d = E.metrics([r for r in rows if split(r["id"]) == "dev"])
        test = [r for r in rows if split(r["id"]) == "test"]
        s = E.metrics(test)
        lo, hi = auc_ci(test)
        print(f"| {t} | {engine} | {cond} | {meta.get('profile', '') or '无'}{(' ' + meta['tag']) if meta.get('tag') not in (None, '', 'baseline') else ''} | {d['auc']} | {d['acc']} | {s['auc']} | {lo}～{hi} | {s['acc']} | {s['ece']} |")


if __name__ == "__main__":
    main()
