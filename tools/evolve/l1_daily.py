#!/usr/bin/env python3
"""L1 每天的例行事：每小时的循环调用它，大部分时候什么也不做。

1. 最近 6 小时没有快照，就抓一份首页时间线快照，并用当前冠军配置盲测
2. 抓好已满 48 小时、还没对过答案的快照，对答案并记成绩
3. 未来考题：收冠军上任以后的新点赞和快照里没点的，盲打分（tools/evolve/l1_future.py update）
冠军配置写在 private/l1/champion.json（档案、条件、例子数），改进被证实后才更新。

用法：
  python3 tools/evolve/l1_daily.py
"""
import datetime as dt, json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import l1_eval as E  # noqa: E402

DIR = E.PRIVATE / "l1" / "prospective"
CHAMP = E.PRIVATE / "l1" / "champion.json"


def run(*args):
    r = subprocess.run([sys.executable, str(HERE / "l1_prospect.py"), *args], capture_output=True, text=True)
    print((r.stdout + r.stderr).strip()[-600:])
    return r.returncode == 0


def stamp_of(p):
    return dt.datetime.strptime(p.stem.split("snapshot-")[1], "%Y%m%d-%H%M")


def main():
    champ = json.loads(CHAMP.read_text())
    now = dt.datetime.now()
    snaps = sorted(DIR.glob("snapshot-*.jsonl"))
    # 2026-10-21 起每 6 小时一份（原来 20 小时）：Luke 说"需要更多数据就去找，不要等"，快照是考题和"刷到没点"的主要来源
    if not snaps or now - stamp_of(snaps[-1]) > dt.timedelta(hours=6):
        if run("snapshot"):
            snaps = sorted(DIR.glob("snapshot-*.jsonl"))
            run("predict", str(snaps[-1]), "--cond", champ["cond"], "--profile", str(E.PRIVATE / "luke" / champ["profile"]))
    else:
        print(f"最近一份快照 {snaps[-1].name}，不到 6 小时，不抓")
    scored = E.PRIVATE / "l1" / "prospective" / "scored.txt"
    done = set(scored.read_text().split()) if scored.exists() else set()
    for s in snaps:
        if s.name in done or now - stamp_of(s) < dt.timedelta(hours=48):
            continue
        if run("score", str(s)):
            with open(scored, "a") as f:
                f.write(s.name + "\n")
    # 首页快照里几乎没有他后来点赞的（2026-10-24 查明），主力考法改成新点赞配对考
    r = subprocess.run([sys.executable, str(HERE / "l1_future.py"), "update"], capture_output=True, text=True)
    print((r.stdout + r.stderr).strip()[-600:])


if __name__ == "__main__":
    main()
