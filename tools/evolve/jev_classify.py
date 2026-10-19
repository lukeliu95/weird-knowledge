#!/usr/bin/env python3
"""用 TypeSafe Jev 给新知识分类：kind（观点 / 工具 / 教程）、topic（15 个固定主题）、观点的溯源价值（1～3）。

只发公开内容（推文原文、作者），不发 Luke 的任何私人资料。每条约 0.00004 美元。

用法：
  python3 tools/evolve/jev_classify.py eval [--n 200]
      从已经分好类的条目里抽样，比较 Jev 和现有分类的一致率，并按置信度分档，结果写进 private/jev/
  python3 tools/evolve/jev_classify.py run [--min-conf 0.9] [--apply]
      给 kind 为空的条目分类；置信度够高的才写回文件（--apply），其余列出来留给 Claude 读原文判断
"""
import argparse, collections, datetime as dt, json, os, random, re, sys, urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PRIVATE = REPO / "private"

KIND = {"opinion": ("观点", "有一个能剥出来的主张、方法、规律、原理或史实（含冷知识、带道理的案例）"),
        "tool": ("工具", "产品、模型、开源项目、硬件的发布或推荐"),
        "tutorial": ("教程", "教程、提示词、操作技巧、实测记录")}
TOPICS = ["编程智能体", "Agent 与 Skill", "提示词与写作", "图像生成", "视频生成", "语音与数字人", "模型与本地部署",
          "AI 产品与创业", "增长与获客", "设计与前端", "学习与研究", "思维与成长", "历史与冷知识", "日本", "其他"]
TOPIC_HINT = {"编程智能体": "用 AI 写代码、Claude Code / Codex 等编程 agent", "Agent 与 Skill": "智能体、skill、MCP、工作流、多智能体",
              "提示词与写作": "提示词技巧、用 AI 写作", "图像生成": "生图模型和用法", "视频生成": "视频生成模型和用法",
              "语音与数字人": "语音合成、语音识别、数字人", "模型与本地部署": "大模型发布、评测、本地运行、推理加速",
              "AI 产品与创业": "做 AI 产品、商业模式、创业、公司动态", "增长与获客": "营销、获客、涨粉、销售",
              "设计与前端": "界面设计、前端、设计系统", "学习与研究": "论文、学习方法、研究", "思维与成长": "心态、方法论、个人成长",
              "历史与冷知识": "历史、冷知识、文化趣闻", "日本": "日本的生活、社会、商业", "其他": "以上都不贴切"}
VALUE = ["1：段子、感想、没正文，勉强算观点", "2：有道理但比较零散", "3：主张清楚，很可能追到公认的理论或史料"]


def load_env():
    for line in (REPO / ".env").read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k, v)


def front(t, k):
    m = re.search(rf"^{k}:[ \t]*(.*)$", t.split("\n---", 1)[0], re.M)
    v = m.group(1).strip() if m else ""
    return json.loads(v) if v.startswith('"') else v


def body(t):
    b = t.split("## 原文", 1)[-1].split("## 溯源", 1)[0]
    return re.split(r"^> 媒体：", b, flags=re.M)[0].strip()


def ask(author, text):
    q = {
        "kind": {"type": "choice", "instructions": "这条内容属于哪一类（看它主要在做什么）",
                 "criteria": {k: f"{v[0]}：{v[1]}" for k, v in KIND.items()}},
        "topic": {"type": "choice", "instructions": "这条内容最贴切的主题（只选一个）",
                  "criteria": {f"t{i:02d}": f"{t}：{TOPIC_HINT[t]}" for i, t in enumerate(TOPICS)}},
        "value": {"type": "score", "instructions": "如果它是观点类，它的主张能不能追到一个公认的理论、方法论或史料（溯源价值）",
                  "criteria": VALUE},
    }
    req = urllib.request.Request("https://api.typesafe.ai/v1/systemone",
                                 json.dumps({"model": "jev-latest", "state": f"作者：{author}\n\n{text[:2500]}", "questions": q}).encode(),
                                 {"Content-Type": "application/json", "Authorization": f"Bearer {os.environ['TYPESAFE_API_KEY']}"})
    with urllib.request.urlopen(req, timeout=120) as r:
        d = json.load(r)
    a = d["answers"]
    return dict(kind=KIND[a["kind"]["choice"]][0], kind_conf=a["kind"]["confidence"],
                topic=TOPICS[int(a["topic"]["choice"][1:])], topic_conf=a["topic"]["confidence"],
                value=a["value"]["score"] + 1, value_conf=a["value"]["confidence"],
                tokens=d.get("usage", {}).get("input_tokens", 0))


def evaluate(a):
    files = [f for f in sorted((REPO / "clips").glob("*.md")) if front(f.read_text(), "kind") in ("观点", "工具", "教程")
             and front(f.read_text(), "topic") in TOPICS]
    random.Random(11).shuffle(files)
    rows, tokens = [], 0
    for f in files[: a.n]:
        t = f.read_text()
        r = ask(front(t, "author"), body(t))
        tokens += r["tokens"]
        rows.append(dict(file=f.name, kind_old=front(t, "kind"), topic_old=front(t, "topic"), **r))
    out = PRIVATE / "jev" / f"classify-eval-{dt.datetime.now():%Y%m%d-%H%M}.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    print(f"{len(rows)} 条，Jev 输入 {tokens} token，约 {tokens / 1e6 * 0.042:.4f} 美元；明细 {out}")
    for field in ("kind", "topic"):
        agree = sum(r[field] == r[f"{field}_old"] for r in rows) / len(rows)
        print(f"\n{field} 和现有分类一致：{agree:.1%}")
        for lo in (0.0, 0.7, 0.8, 0.9, 0.95):
            s = [r for r in rows if r[f"{field}_conf"] >= lo]
            if s:
                print(f"  置信度 ≥ {lo}: {len(s)} 条（{len(s) / len(rows):.0%}），一致 {sum(r[field] == r[f'{field}_old'] for r in s) / len(s):.1%}")
    conf = collections.Counter((r["kind_old"], r["kind"]) for r in rows)
    print("\nkind 对照（现有 → Jev）：", dict(conf))


def run(a):
    todo = [f for f in sorted((REPO / "clips").glob("*.md")) if not front(f.read_text(), "kind")]
    auto, review = [], []
    for f in todo:
        t = f.read_text()
        r = ask(front(t, "author"), body(t))
        ok = r["kind_conf"] >= a.min_conf and r["topic_conf"] >= a.min_conf
        (auto if ok else review).append((f, r))
        if ok and a.apply:
            t = re.sub(r"^kind:.*$", f"kind: {r['kind']}", t, count=1, flags=re.M)
            t = re.sub(r"^topic:.*$", f"topic: {r['topic']}", t, count=1, flags=re.M)
            f.write_text(t)
    print(f"待分类 {len(todo)} 条：自动分好 {len(auto)} 条{'（已写回）' if a.apply else '（未写回）'}，要人看 {len(review)} 条")
    for f, r in review:
        print(f"  {f.name}: {r['kind']}({r['kind_conf']:.2f}) / {r['topic']}({r['topic_conf']:.2f})")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("eval"); e.add_argument("--n", type=int, default=200)
    r = sub.add_parser("run"); r.add_argument("--min-conf", type=float, default=0.9); r.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    load_env()
    {"eval": evaluate, "run": run}[a.cmd](a)


if __name__ == "__main__":
    main()
