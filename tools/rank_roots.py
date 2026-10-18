#!/usr/bin/env python3
"""给 framework.md 的「知识底座」和「待查」算数。见 AGENTS.md「流程二」第三步。

用法：
  python3 tools/rank_roots.py [--top 15]

打印：
- 知识底座排名：每个源知识被几条新知识指向（直接 / 连同间接）。
  直接 = 「指向它的新知识」表格的行数；间接 = 顺着「更底层的源头」往下传，能走到它的新知识（去重）
- 挑战：关系是“挑战”的行
- 没核实的源知识（verified: false）
- 没找到源头的新知识（「溯源」里写了“没找到已知的源头”）
"""
import argparse
import collections
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\.md\)")


def section(text, title):
    m = re.search(rf"^## {title}\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(1) if m else ""


def field(text, key):
    m = re.search(rf"^{key}:[ \t]*(.*)$", text, re.M)
    if not m:
        return ""
    v = m.group(1).strip()
    return json.loads(v) if v.startswith('"') else v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=15)
    args = ap.parse_args()

    roots, direct, deeper, challenges = {}, collections.defaultdict(set), {}, []
    for f in sorted((ROOT / "roots").glob("*.md")):
        t = f.read_text()
        roots[f.stem] = {"name": field(t, "name_zh"), "verified": field(t, "verified") != "false"}
        deeper[f.stem] = [Path(p).name for _, p in LINK.findall(section(t, "更底层的源头"))]
        for row in section(t, "指向它的新知识").splitlines():
            m = LINK.search(row)
            if row.startswith("| [") and m:
                clip = Path(m.group(2)).name
                direct[f.stem].add(clip)
                cells = [c.strip() for c in row.strip("|").split("|")]
                if cells[1] == "挑战":
                    challenges.append((m.group(1), clip, f.stem, cells[2]))

    # walk down the deeper chain from each root; every clip pointing at a root also reaches what lies below it
    reach = collections.defaultdict(set)
    for s in roots:
        seen, todo = set(), [s]
        while todo:
            x = todo.pop()
            if x in seen or x not in roots:
                continue
            seen.add(x)
            todo += deeper[x]
        for x in seen:
            reach[x] |= direct[s]

    def reached(slug):
        return reach[slug]

    rank = sorted(roots, key=lambda s: (-len(reached(s)), -len(direct[s]), s))
    print(f"## 知识底座（共 {len(roots)} 个源知识）\n")
    print("| 排名 | 源知识 | 被几条新知识指向（直接 / 连同间接） | 更底层的源头 |")
    print("|---|---|---|---|")
    for i, s in enumerate(rank[: args.top], 1):
        ds = "、".join(f"[{roots[d]['name']}](roots/{d}.md)" for d in deeper[s] if d in roots) or "已到基础层"
        print(f"| {i} | [{roots[s]['name']}](roots/{s}.md) | {len(direct[s])} / {len(reached(s))} | {ds} |")

    print("\n直接被指向最多：" + "、".join(
        f"{roots[s]['name']}（{len(direct[s])}）" for s in sorted(roots, key=lambda s: -len(direct[s]))[:8]))

    print(f"\n## 挑战（{len(challenges)} 条）\n")
    for title, clip, slug, strength in challenges:
        print(f"| [{title}](clips/{clip}.md) | [{roots[slug]['name']}](roots/{slug}.md) | {strength} |")

    print("\n## 没核实的源知识\n")
    for s, r in roots.items():
        if not r["verified"]:
            print(f"- [{r['name']}](roots/{s}.md)")

    print("\n## 没找到源头的新知识\n")
    for f in sorted((ROOT / "clips").glob("*.md")):
        t = f.read_text()
        if "没找到已知的源头" in section(t, "溯源"):
            print(f"- [{field(t, 'title')}](clips/{f.name})")


if __name__ == "__main__":
    main()
