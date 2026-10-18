#!/usr/bin/env python3
"""把分类结果写进 clips/ 的 frontmatter。见 AGENTS.md「流程二 · 第零步：条数多时先分类」。

用法：
  python3 tools/apply_kinds.py --input <分类结果目录或文件> [--dry]

分类结果：JSON 数组，每条 {"id": 推文编号, "kind": "观点|工具|教程", "topic": "固定主题之一", "value": 0-3}；
也可以用 {"file": "clips/xxx.md", ...} 直接指定文件（给不是推文的条目用）。

- 填上（或改写）kind、topic 两行
- kind 是 工具 或 教程、或者是溯源价值 1 分的观点，且 status 还是 未整理 的，status 改成 已归档
- 已整理的条目只更新 kind、topic，不动 status
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLIPS = ROOT / "clips"
KINDS = {"观点", "工具", "教程"}
TOPICS = {"编程智能体", "Agent 与 Skill", "提示词与写作", "图像生成", "视频生成", "语音与数字人", "模型与本地部署",
          "AI 产品与创业", "增长与获客", "设计与前端", "学习与研究", "思维与成长", "历史与冷知识", "日本", "其他"}
NORMAL = {t.replace(" ", ""): t for t in TOPICS}


def set_field(front, key, value):
    line = f"{key}: {value}"
    if re.search(rf"^{key}:.*$", front, re.M):
        return re.sub(rf"^{key}:.*$", line, front, count=1, flags=re.M)
    # keep the template order: status, kind, topic
    anchor = r"^(kind:.*)$" if key == "topic" and re.search(r"^kind:", front, re.M) else r"^(status:.*)$"
    return re.sub(anchor, rf"\1\n{line}", front, count=1, flags=re.M)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()

    src = Path(args.input)
    items = []
    for f in ([src] if src.is_file() else sorted(src.glob("*.json"))):
        items += json.loads(f.read_text())

    by_id = {}
    for f in CLIPS.glob("*.md"):
        m = re.search(r"(?:status|article)/(\d{15,20})", f.read_text())
        if m:
            by_id[m.group(1)] = f

    done, archived, missing = 0, 0, []
    for it in items:
        kind, topic = it["kind"], NORMAL.get(it["topic"].replace(" ", ""))
        if kind not in KINDS or not topic:
            sys.exit(f"bad kind/topic: {it}")
        path = ROOT / it["file"] if "file" in it else by_id.get(str(it.get("id")))
        if not path or not path.exists():
            missing.append(it.get("id") or it.get("file"))
            continue
        text = path.read_text()
        m = re.match(r"---\n(.*?)\n---\n", text, re.S)
        front = set_field(set_field(m.group(1), "kind", kind), "topic", topic)
        low_value = kind == "观点" and it.get("value") == 1
        if (kind in ("工具", "教程") or low_value) and re.search(r"^status: 未整理$", front, re.M):
            front = re.sub(r"^status: 未整理$", "status: 已归档", front, count=1, flags=re.M)
            archived += 1
        if not args.dry:
            path.write_text(f"---\n{front}\n---\n" + text[m.end():])
        done += 1
    print(f"{'将' if args.dry else '已'}更新 {done} 条，其中归档 {archived} 条；找不到对应条目 {len(missing)} 条 {missing[:5]}")


if __name__ == "__main__":
    main()
