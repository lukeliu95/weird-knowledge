#!/usr/bin/env python3
"""补数据：从这台 Mac 上的 Claude Code 和 Codex 会话里，抽 Luke 纠正 agent 的地方（"不对""错了""改成……"），改写成选择题。

Luke 2026-10-25 选了 C（先不训练，先补"他自己拿主意"的数据）。他 10-19 同意过读这台 Mac 上的会话、只抽他的选择；
纠正也是他的选择：agent 原来的做法是他不要的，他改成的是他要的。结果只放 private/l3/（会话里有工作内容）。

两步：
1. 用规则找纠正（确定的事用代码）：agent 说完话后，Luke 的回复开头是"不对、错了、改成……"这类词
2. 交给 Opus 改写成两选一的题：情境、A、B，哪个是 Luke 要的随机放；不是对做法的纠正（只是追加要求、闲聊）就跳过

用法：
  python3 tools/evolve/l3_corrections.py          抽新的纠正、改写，追加进 private/l3/corrections.jsonl
  python3 tools/evolve/l3_corrections.py --dry    只数一数找到多少处，不调 Opus
"""
import argparse, hashlib, json, random, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import l3_extract as X  # noqa: E402
import opus_judge as OJ  # noqa: E402

OUT = X.OUT / "corrections.jsonl"
COR = re.compile(r"^(不对|错了|不是|不要|别再|别这样|改成|应该|重新|重来|不行|理解错|你理解|没必要|搞错|有问题|太长|太复杂|"
                 r"我说的是|我要的是|你没有|为什么不|还是不对|这不是)")


def find():
    files = [("claude", f) for f in (X.HOME / ".claude" / "projects").glob("*/*.jsonl")]
    files += [("codex", f) for f in (X.HOME / ".codex" / "sessions").rglob("*.jsonl")]
    files += [("codex", f) for f in (X.HOME / ".codex" / "archived_sessions").rglob("*.jsonl")]
    out, seen = [], set()
    for src, f in files:
        try:
            turns = X.claude_turns(f) if src == "claude" else X.codex_turns(f)
        except Exception:
            continue
        prev = None
        for role, text, ts in turns:
            if role == "assistant":
                prev = text
                continue
            if role == "user" and prev:
                t = text.strip()
                k = (ts[:16], t[:30])   # Luke 常把同一句连发几遍
                if COR.search(t[:15]) and k not in seen:
                    seen.add(k)
                    out.append(dict(id=hashlib.sha1((str(f) + ts + t[:50]).encode()).hexdigest()[:12], ts=ts, source=src,
                                    file=str(f), before=prev[-2500:], reply=t[:1500]))
            prev = None
    return out


SYS = ("你在把一段工作对话改写成一道两选一的题，用来检验别人能不能猜中 Luke 的判断。只输出 JSON。"
       "如果 Luke 的回复是在纠正 agent 的做法或判断（agent 做了或打算做 X，Luke 要的是 Y），输出："
       '{"question": "一两句话的情境，不提谁对谁错，不写客户和人名", "luke": "Luke 要的做法，一句话", "agent": "agent 原来的做法，一句话"}；'
       '如果只是追加新要求、提问、闲聊，或者看不出 agent 原来怎么做，输出 {"skip": true}。')


def convert(r):
    out = OJ.ask_json(SYS, f"【agent 刚说的话（末尾）】\n{r['before']}\n\n【Luke 的回复】\n{r['reply']}")
    if out.get("skip") or not out.get("luke") or not out.get("agent"):
        return None
    luke_first = random.Random(r["id"]).random() < 0.5   # 按编号固定随机，免得 Luke 要的总在 A
    opts = {"A": out["luke"], "B": out["agent"]} if luke_first else {"A": out["agent"], "B": out["luke"]}
    return dict(id=r["id"], kind="correction", question=out["question"], options=opts, recommended="",
                choice="A" if luke_first else "B", reply=r["reply"][:300], ts=r["ts"], source=r["source"], file=r["file"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    found = find()
    old = [json.loads(l) for l in OUT.read_text().split("\n") if l.strip()] if OUT.exists() else []
    done = {r["id"] for r in old} | {r["id"] for r in old if r.get("skip")}
    new = [r for r in found if r["id"] not in done]
    print(f"会话里找到纠正 {len(found)} 处，没改写过的 {len(new)} 处")
    if a.dry or not new:
        return
    kept = 0
    with open(OUT, "a") as fh:
        for r in new:
            try:
                q = convert(r)
            except Exception as e:
                print(f"  {r['id']} 出错：{e}", file=sys.stderr)
                continue
            row = q or {"id": r["id"], "skip": True, "ts": r["ts"]}   # 跳过的也记下，下次不再问 Opus
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
            kept += bool(q)
    print(f"改写成题 {kept} 道，跳过 {len(new) - kept} 处")


if __name__ == "__main__":
    main()
