#!/usr/bin/env python3
"""弱关系复核：溯源时模型推断出来的"弱"关系，交给另一个模型（Opus 5.5）逐条复核，Luke 只抽查。

Luke 2026-10-21 定的：882 处"待 Luke 确认"不可能人工一条条认。改成抽查验收：
第二个模型逐条判"关系成不成立"；随机抽 10 条判成立的给 Luke 看，他认 9 条以上，这套复核就算靠得住，整批写回。
只涉及公开内容（新知识的标题和核心主张、源知识的一句话），可以交给 Opus。

用法：
  relation_review.py review [--workers 4]   复核全部"弱（待 Luke 确认）"，结果追加进 docs/reviews/relation-review.jsonl（可断点续跑）
  relation_review.py sample [--n 10]        随机抽 n 条"成立"的，写成抽查单
  relation_review.py apply                  Luke 抽查通过后：成立的改成"弱（模型复核通过）"，不成立的从新知识和源知识里删掉
"""
import argparse, collections, concurrent.futures as cf, json, random, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(HERE))
import opus_judge as OJ  # noqa: E402

OUT = REPO / "docs" / "reviews" / "relation-review.jsonl"
PENDING = "弱（待 Luke 确认）"
PAT = re.compile(r"\[([^\]]+)\]\(\.\./roots/([^)]+?)\.md\)(.*?)强弱：弱（待 Luke 确认）(.*)$")

# Luke 2026-10-21 亲口确认过的 3 处，给复核模型当标准样例
EXAMPLES = [
    ("范冰《前线部署工程师》：灯塔客户、先登陆后扩张", "跨越鸿沟：先拿下一个细分市场当滩头堡，靠同行推荐再向相邻市场扩张", "相近", "成立"),
    ("HubSpot Japan 调查：日本买方先自己用 AI 查、见销售前已列好候选", "稟議制：日本企业的决策要起案人写书面材料层层传阅盖章", "相近", "成立"),
    ("模拟客户从不走开：大模型扮的客户在不会买的人那里系统性地偏，拿它评估会高估效果", "古德哈特定律：指标一旦被拿来当目标，就不再是好指标", "相近", "成立"),
]


def front(t, k):
    m = re.search(rf"^{k}:[ \t]*(.*)$", t.split("\n---", 1)[0], re.M)
    return m.group(1).strip().strip('"') if m else ""


def root_line(slug):
    f = REPO / "roots" / f"{slug}.md"
    if not f.exists():
        return ""
    t = f.read_text()
    m = re.search(r"^## 一句话\s*\n+(.+)$", t, re.M)
    return (front(t, "name_zh") + "：" + (m.group(1).strip() if m else "")).strip("：")


def collect():
    rows = []
    for f in sorted((REPO / "clips").glob("*.md")):
        t = f.read_text()
        if "## 溯源" not in t:
            continue
        trace = t.split("## 溯源", 1)[1]
        claim = re.search(r"核心主张：(.*)", trace)
        for l in trace.split("\n"):
            m = PAT.search(l)
            if not m:
                continue
            rel = re.search(r"关系：([^·]+?)\s*·", m.group(3))
            rows.append(dict(id=f"{f.stem}::{m.group(2)}", clip=f.name, slug=m.group(2), title=front(t, "title"),
                             claim=claim.group(1).strip() if claim else "", relation=rel.group(1).strip() if rel else "",
                             reason=m.group(4).strip("。 "), root=root_line(m.group(2)) or m.group(1)))
    return rows


SYS = ("你在复核一个知识库的溯源。每一项是：一条新知识（标题和核心主张）、一个源知识（理论或论文的一句话）、"
       "溯源时写的关系和理由。判断这个关系成不成立。只输出 JSON。")


def judge(batch):
    ex = "\n".join(f"- 新知识：{a}\n  源知识：{b}\n  关系：{c} → {d}" for a, b, c, d in EXAMPLES)
    items = "\n\n".join(f"[{i}] 新知识：{r['title']}\n核心主张：{r['claim']}\n源知识：{r['root']}\n写的关系：{r['relation']}\n理由：{r['reason'][:300]}"
                        for i, r in enumerate(batch))
    prompt = (f"关系的含义：直接源自＝作者明说或明显在用这个理论；换了说法＝本质是老理论换了新名词；相近＝作者自己想的，但和这个理论很像；"
              f"挑战＝和经典说法相反。\n判定标准：一个懂行的人看了，会同意这条新知识确实和这个源知识有写的这种关系，就算成立；"
              f"只是沾边、牵强、关系方向写反了，就算不成立。\n\nLuke 确认过的样例：\n{ex}\n\n要复核的：\n{items}\n\n"
              f'按编号输出 JSON：{{"编号": {{"verdict": "成立" 或 "不成立", "better_relation": "如果成立但关系写错了，填对的关系，否则空字符串", "why": "一句话"}}}}')
    out = OJ.ask_json(SYS, prompt)
    res = []
    for i, r in enumerate(batch):
        v = out.get(str(i)) or {}
        if v.get("verdict") in ("成立", "不成立"):
            res.append({**r, "verdict": v["verdict"], "better_relation": v.get("better_relation", ""), "why": v.get("why", "")})
    return res


def done_ids():
    return {json.loads(l)["id"] for l in OUT.read_text().split("\n") if l.strip()} if OUT.exists() else set()


def cmd_review(a):
    todo = [r for r in collect() if r["id"] not in done_ids()]
    print(f"待复核 {len(todo)} 处", flush=True)
    batches = [todo[i:i + 20] for i in range(0, len(todo), 20)]
    n = 0
    with cf.ThreadPoolExecutor(max_workers=a.workers) as ex, open(OUT, "a") as f:
        futs = {ex.submit(judge, b): b for b in batches}
        for fu in cf.as_completed(futs):
            try:
                for r in fu.result():
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
                    n += 1
                f.flush()
            except Exception as e:
                print(f"一批出错（下次重跑会补上）：{e}", file=sys.stderr)
    rows = [json.loads(l) for l in OUT.read_text().split("\n") if l.strip()]
    c = collections.Counter(r["verdict"] for r in rows)
    print(f"这次复核 {n} 处；累计 {len(rows)} 处：{dict(c)}；建议改关系 {sum(bool(r['better_relation']) for r in rows)} 处")


def cmd_sample(a):
    rows = [json.loads(l) for l in OUT.read_text().split("\n") if l.strip()]
    ok = [r for r in rows if r["verdict"] == "成立"]
    pick = random.Random(a.seed).sample(ok, min(a.n, len(ok)))
    md = ["# 弱关系复核抽查单", "", f"从 {len(ok)} 处判成「成立」的里随机抽 {len(pick)} 处。每处回「认」或「不认」，或者只回不认的编号。", ""]
    for i, r in enumerate(pick, 1):
        md += [f"**{i}. {r['title']}**", f"- 源知识：{r['root']}", f"- 关系：{r['better_relation'] or r['relation']}",
               f"- 复核理由：{r['why']}", ""]
    (REPO / "docs" / "reviews" / "relation-review-sample.md").write_text("\n".join(md))
    print("\n".join(md))


def cmd_apply(_):
    rows = [json.loads(l) for l in OUT.read_text().split("\n") if l.strip()]
    verdict = {r["id"]: r for r in rows}
    kept = dropped = changed = 0
    for f in sorted((REPO / "clips").glob("*.md")):
        t = f.read_text()
        if PENDING not in t:
            continue
        head, trace = t.split("## 溯源", 1)
        lines, drop_slugs = [], []
        for l in trace.split("\n"):
            m = PAT.search(l)
            r = verdict.get(f"{f.stem}::{m.group(2)}") if m else None
            if not r:
                lines.append(l)
                continue
            if r["verdict"] == "不成立":
                drop_slugs.append(r["slug"])
                dropped += 1
                continue
            l = l.replace(PENDING, "弱（模型复核通过）")
            if r["better_relation"] and r["better_relation"] != r["relation"]:
                l = l.replace(f"关系：{r['relation']}", f"关系：{r['better_relation']}", 1)
                changed += 1
            lines.append(l)
            kept += 1
        if drop_slugs:   # 新知识 frontmatter 的 roots 里也去掉
            head = re.sub(r"^roots: \[(.*)\]$", lambda m: "roots: [" + ", ".join(
                s for s in [x.strip() for x in m.group(1).split(",")] if s and s not in drop_slugs) + "]", head, count=1, flags=re.M)
        f.write_text(head + "## 溯源" + "\n".join(lines))
        for slug in drop_slugs:   # 源知识「指向它的新知识」表里删掉这一行
            rf = REPO / "roots" / f"{slug}.md"
            if rf.exists():
                rf.write_text("\n".join(x for x in rf.read_text().split("\n") if not (f.stem in x and x.startswith("|"))))
    for rf in (REPO / "roots").glob("*.md"):   # 源知识表里留下的，状态跟着改
        t = rf.read_text()
        if PENDING in t:
            new = []
            for x in t.split("\n"):
                m = re.search(r"\(\.\./clips/([^)]+?)\.md\)", x)
                r = verdict.get(f"{m.group(1)}::{rf.stem}") if m else None
                if r and r["verdict"] == "成立" and PENDING in x:
                    x = x.replace(PENDING, "弱（模型复核通过）")
                    if r["better_relation"] and r["better_relation"] != r["relation"]:
                        x = x.replace(f"| {r['relation']} |", f"| {r['better_relation']} |", 1)
                new.append(x)
            rf.write_text("\n".join(new))
    print(f"写回：保留 {kept} 处（其中改了关系 {changed} 处），删掉 {dropped} 处")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("review"); p.add_argument("--workers", type=int, default=4)
    p = sub.add_parser("sample"); p.add_argument("--n", type=int, default=10); p.add_argument("--seed", type=int, default=21)
    sub.add_parser("apply")
    a = ap.parse_args()
    {"review": cmd_review, "sample": cmd_sample, "apply": cmd_apply}[a.cmd](a)


if __name__ == "__main__":
    main()
