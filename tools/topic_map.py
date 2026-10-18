#!/usr/bin/env python3
"""生成 framework.md 里的「主题地图」：按 topic × 发布年份统计全部新知识（含已归档）。

用法：
  python3 tools/topic_map.py          写进 framework.md 的 <!-- topic-map:begin --> 和 <!-- topic-map:end --> 之间
  python3 tools/topic_map.py --print  只打印
"""
import argparse
import collections
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BEGIN, END = "<!-- topic-map:begin -->", "<!-- topic-map:end -->"
EARLY = 2023   # older papers and books go into one 更早 column


def field(front, key):
    m = re.search(rf'^{key}:\s*"?(.*?)"?\s*$', front, re.M)
    return m.group(1) if m else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--print", action="store_true")
    args = ap.parse_args()

    items = []
    for f in sorted((ROOT / "clips").glob("*.md")):
        m = re.match(r"---\n(.*?)\n---\n", f.read_text(), re.S)
        if not m:
            continue
        fr = m.group(1)
        year = re.match(r"(\d{4})", field(fr, "published"))
        y = year.group(1) if year else "未知"
        if y != "未知" and int(y) < EARLY:
            y = "更早"
        items.append({"file": f.name, "title": field(fr, "title"), "topic": field(fr, "topic") or "未分类",
                      "kind": field(fr, "kind") or "未分类", "status": field(fr, "status"),
                      "year": y, "published": field(fr, "published")})

    present = {i["year"] for i in items}
    years = (["更早"] if "更早" in present else []) + sorted(y for y in present if y.isdigit()) + (["未知"] if "未知" in present else [])
    by_topic = collections.defaultdict(list)
    for i in items:
        by_topic[i["topic"]].append(i)
    order = sorted(by_topic, key=lambda t: -len(by_topic[t]))

    out = [f"共 {len(items)} 条新知识（含已归档）。数字是每年存下的条数；按发布年份算，不是保存日期。", ""]
    out.append("| 主题 | " + " | ".join(years) + " | 合计 | 观点 / 工具 / 教程 |")
    out.append("|---|" + "---|" * (len(years) + 2))
    for t in order:
        g = by_topic[t]
        cy = collections.Counter(i["year"] for i in g)
        ck = collections.Counter(i["kind"] for i in g)
        out.append(f"| {t} | " + " | ".join(str(cy.get(y, "")) for y in years)
                   + f" | {len(g)} | {ck.get('观点', 0)} / {ck.get('工具', 0)} / {ck.get('教程', 0)} |")
    out += ["", "**每个主题的代表**（先选已溯源的，再选观点类，最后按发布时间取最新）", ""]
    rank = {"已整理": 0, "未整理": 1, "已归档": 2}
    for t in order:
        g = sorted(by_topic[t], key=lambda i: (rank.get(i["status"], 3), i["kind"] != "观点", i["published"]), reverse=False)
        top = g[:3] if g and rank.get(g[0]["status"], 3) == 0 else sorted(by_topic[t], key=lambda i: i["published"], reverse=True)[:3]
        out.append(f"- **{t}**：" + "、".join(f"[{i['title']}](clips/{i['file']})" for i in top))
    block = "\n".join(out)

    if args.print:
        print(block)
        return
    fw = ROOT / "framework.md"
    text = fw.read_text()
    if BEGIN not in text:
        raise SystemExit(f"framework.md 里没有 {BEGIN} … {END} 标记")
    text = text[: text.index(BEGIN) + len(BEGIN)] + "\n" + block + "\n" + text[text.index(END):]
    fw.write_text(text)
    print(f"主题地图已更新：{len(order)} 个主题，{len(items)} 条")


if __name__ == "__main__":
    main()
