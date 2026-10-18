#!/usr/bin/env python3
"""把一份 X 点赞（或书签）导出写成 clips/ 里的新知识，一条一个文件。见 AGENTS.md「流程三：批量存」。

用法：
  python3 tools/import_x_likes.py --likes <likes.jsonl> --titles <标题目录> [--articles <长文目录>] [--saved 2026-10-18] [--why "X 点赞（批量导入）"] [--dry]

  likes.jsonl  opencli twitter likes --all --output-file 导出的文件（每行一条：id、author、name、text、created_at、url、media_urls）
  标题目录     里面若干 *.json，每个是 [{"id": ..., "title": "中文短标题", "slug": "english-file-name"}]，由读过原文的模型写；
               按文件名排序读取，后读的覆盖先读的
  长文目录     只有链接的帖子多半是 X 长文：用 opencli twitter article <链接> -f json 抓到的 <推文编号>.json 放这里，
               有正文的会按 X 长文存全文

已经在 clips/ 里的推文（按推文编号判断）会跳过，所以同一个列表可以反复导入，只会补上新增的。
Luke 明确不要的条目，把推文编号一行一个写进仓库根目录的 .skip_ids（已被 .gitignore 排除，不会公开），导入时也会跳过。
"""
import argparse
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLIPS = ROOT / "clips"
SKIP = ROOT / ".skip_ids"   # local only (gitignored): ids Luke chose not to keep


def existing_ids():
    ids = set()
    for f in CLIPS.glob("*.md"):
        ids |= set(re.findall(r"(?:status|article)/(\d{15,20})", f.read_text()))
    return ids


def published(created_at):
    try:
        d = datetime.datetime.strptime(created_at, "%a %b %d %H:%M:%S %z %Y")
        return d.strftime("%Y-%m-%d %H:%M UTC")
    except (TypeError, ValueError):
        return "未知"


def q(value):
    # JSON strings are valid YAML double-quoted scalars, so colons and quotes stay safe.
    return json.dumps(value, ensure_ascii=False)


def render(row, meta, saved, why, article=None):
    text = (row.get("text") or "").rstrip()
    media = row.get("media_urls") or []
    source = "X"
    if article:
        source = "X Article"
        body = f"# {article['title']}\n\n{article['content'].rstrip()}"
    else:
        body = text if text else "（只有图片或视频，没有文字）"
        if media:
            body += "\n\n> 媒体：\n" + "\n".join(f"> - {u}" for u in media)
    author = f"{row.get('name') or row['author']} (@{row['author']})"
    return f"""---
title: {q(meta['title'])}
author: {q(author)}
url: {row['url']}
source: {source}
published: {published(row.get('created_at'))}
saved: {saved}
why: {q(why)}
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

{body}

## 溯源

"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--likes", required=True)
    ap.add_argument("--titles", required=True)
    ap.add_argument("--articles", default="")
    ap.add_argument("--saved", default=datetime.date.today().isoformat())
    ap.add_argument("--why", default="X 点赞（批量导入）")
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()

    rows = [json.loads(line) for line in open(args.likes) if line.strip()]
    titles = {}
    for f in sorted(Path(args.titles).glob("*.json")):
        for item in json.loads(f.read_text()):
            titles[str(item["id"])] = item

    articles = {}
    if args.articles:
        for f in Path(args.articles).glob("*.json"):
            d = json.loads(f.read_text())
            d = d[0] if isinstance(d, list) else d
            if (d.get("content") or "").strip():
                articles[f.stem] = d

    have = existing_ids()
    skip = set(SKIP.read_text().split()) if SKIP.exists() else set()
    todo = [r for r in rows if str(r["id"]) not in have and str(r["id"]) not in skip]
    missing = [r["id"] for r in todo if str(r["id"]) not in titles]
    if missing:
        sys.exit(f"{len(missing)} 条没有标题，先补上：{missing[:5]}…")

    taken = {f.name for f in CLIPS.glob("*.md")}
    written = 0
    for r in todo:
        meta = titles[str(r["id"])]
        handle = re.sub(r"[^a-z0-9]+", "-", r["author"].lower()).strip("-") or "x"
        slug = re.sub(r"[^a-z0-9-]+", "", meta["slug"].lower()).strip("-") or "post"
        name = f"{args.saved}-{handle}-{slug}.md"
        if name in taken:
            name = f"{args.saved}-{handle}-{slug}-{str(r['id'])[-6:]}.md"
        taken.add(name)
        if not args.dry:
            (CLIPS / name).write_text(render(r, meta, args.saved, args.why, articles.get(str(r["id"]))))
        written += 1
    n_art = sum(1 for r in todo if str(r["id"]) in articles)
    n_skip = sum(1 for r in rows if str(r["id"]) in skip and str(r["id"]) not in have)
    print(f"列表 {len(rows)} 条，库里已有 {len(rows) - len(todo) - n_skip} 条，按 .skip_ids 跳过 {n_skip} 条，{'将' if args.dry else '已'}写入 {written} 条（其中 X 长文 {n_art} 篇）")


if __name__ == "__main__":
    main()
