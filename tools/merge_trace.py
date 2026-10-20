#!/usr/bin/env python3
"""把 subagent 交回的溯源结果合并进仓库。见 AGENTS.md「流程二：整理」。

用法：
  python3 tools/merge_trace.py --input <溯源结果目录> --round N [--date 2026-10-18] [--dry]

溯源结果目录里每个 out-*.json 的格式：
  {"clips": [{"file", "core_claim", "roots": [{"slug", "relation", "strength", "why"}], "essence", "no_source"}],
   "roots": [{"slug", "name_zh", "name_en", "proposer", "year", "type", "one_line", "sources": [{"text", "url"}],
              "dispute", "verified", "deeper": [{"slug", "relation"}]}]}

做的事：
- 源知识按 slug 去重，出处合并；roots/ 里没有的新建，已有的只补「指向它的新知识」的行（不改已写好的内容）
- 每条新知识写好「溯源」部分，status 改成 已整理，roots 填上 slug
"""
import argparse
import datetime
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROOTS = ROOT / "roots"
CLIPS = ROOT / "clips"


def load(input_dir):
    clips, roots = [], {}
    for f in sorted(Path(input_dir).glob("out-*.json")):
        d = json.loads(f.read_text())
        clips += d["clips"]
        for r in d["roots"]:
            # existing roots may come back with only slug and names; fill the rest so pooling below works
            for k, v in dict(verified=True, sources=[], deeper=[], dispute="", proposer="", year="", type="理论", one_line="").items():
                if r.get(k) is None:
                    r[k] = v
            old = roots.get(r["slug"])
            if not old:
                roots[r["slug"]] = r
                continue
            # same theory found by two subagents: keep the verified one, pool sources and deeper links
            keep, other = (old, r) if old["verified"] or not r["verified"] else (r, old)
            urls = {s.get("url") for s in keep["sources"]}
            keep["sources"] += [s for s in other["sources"] if s.get("url") not in urls]
            seen = {x["slug"] for x in keep["deeper"]}
            keep["deeper"] += [x for x in other["deeper"] if x["slug"] not in seen]
            if other.get("dispute") and other["dispute"] not in keep.get("dispute", ""):
                keep["dispute"] = "；".join(x for x in (keep.get("dispute"), other["dispute"]) if x)
            roots[r["slug"]] = keep
    return clips, roots


def clip_title(path):
    m = re.search(r'^title:\s*"?(.*?)"?\s*$', path.read_text(), re.M)
    return m.group(1) if m else path.stem


def root_file(r, pointers):
    lines = [
        "---",
        f"name_zh: {json.dumps(r['name_zh'], ensure_ascii=False)}",
        f"name_en: {json.dumps(r['name_en'], ensure_ascii=False)}",
        f"proposer: {json.dumps(r['proposer'], ensure_ascii=False)}",
        f"year: {json.dumps(str(r['year']), ensure_ascii=False)}",
        f"type: {r['type']}",
        f"verified: {'true' if r['verified'] else 'false'}",
        "---",
        "",
        f"# {r['name_zh']}（{r['name_en']}）",
        "",
        "## 一句话",
        "",
        r["one_line"] + ("" if r["verified"] or "待确认" in r["one_line"] else "（待确认）"),
        "",
        "## 原始出处",
        "",
    ]
    lines += [f"- {s['text']}" + (f"，{s['url']}" if s.get("url") else "") for s in r["sources"]] or ["- 没查到（待确认）"]
    if r.get("dispute"):
        lines.append(f"- 争议：{r['dispute']}")
    lines += ["", "## 更底层的源头", ""]
    lines += [f"- [{x['name_zh']}]({x['slug']}.md) · 关系：{x['relation']}" for x in r["deeper_named"]] or ["- 已追到基础层，或暂未找到更底层的源头"]
    lines += ["", "## 指向它的新知识", "", "| 新知识 | 关系 | 强弱 |", "|---|---|---|"]
    lines += pointers
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--round", required=True, type=int)
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()

    clips, roots = load(args.input)
    for r in roots.values():
        r["deeper_named"] = [{**x, "name_zh": roots[x["slug"]]["name_zh"]} for x in r["deeper"] if x["slug"] in roots]

    # pointer rows per root, from this round's clips
    rows = {slug: [] for slug in roots}
    for c in clips:
        path = ROOT / c["file"]
        for x in c["roots"]:
            weak = "（待 Luke 确认）" if x["strength"] == "弱" else ""
            rows[x["slug"]].append(f"| [{clip_title(path)}](../{c['file']}) | {x['relation']} | {x['strength']}{weak} |")

    new_roots = updated_roots = 0
    for slug, r in roots.items():
        f = ROOTS / f"{slug}.md"
        if f.exists():
            text = f.read_text()
            add = [row for row in rows[slug] if row.split("](../")[1].split(")")[0] not in text]
            if add and not args.dry:
                f.write_text(text.rstrip("\n") + "\n" + "\n".join(add) + "\n")
            updated_roots += bool(add)
        else:
            if not args.dry:
                ROOTS.mkdir(exist_ok=True)
                f.write_text(root_file(r, rows[slug]))
            new_roots += 1

    for c in clips:
        path = ROOT / c["file"]
        text = path.read_text()
        out = ["## 溯源", "", f"- 核心主张：{c['core_claim']}", "- 源知识："]
        if c["roots"]:
            for x in c["roots"]:
                r = roots[x["slug"]]
                weak = "（待 Luke 确认）" if x["strength"] == "弱" else ""
                why = f"。{x['why'].replace('（待 Luke 确认）', '')}" if x.get("why") else ""
                out.append(f"  - [{r['name_zh']}](../roots/{x['slug']}.md) · 关系：{x['relation']} · 强弱：{x['strength']}{weak}{why}")
        else:
            out.append("  - 没找到已知的源头（待查）")
        out += [f"- 本质：{c['essence']}", f"- 整理于：{args.date}（第 {args.round} 轮）", ""]
        head = text[: text.rindex("\n## 溯源")] if "\n## 溯源" in text else text.rstrip("\n")
        new = head.rstrip("\n") + "\n\n" + "\n".join(out)
        slugs = ", ".join(x["slug"] for x in c["roots"])
        new = re.sub(r"^status: .*$", "status: 已整理", new, count=1, flags=re.M)
        new = re.sub(r"^roots: .*$", f"roots: [{slugs}]", new, count=1, flags=re.M)
        if not args.dry:
            path.write_text(new)

    print(f"新知识 {len(clips)} 条已整理；源知识新建 {new_roots} 个、补行 {updated_roots} 个"
          f"（其中未核实 {sum(1 for r in roots.values() if not r['verified'])} 个）")


if __name__ == "__main__":
    main()
