#!/usr/bin/env python3
"""L3 回答预测的测试集：从这台 Mac 上的 Claude Code 和 Codex 会话里，抽出"agent 给了 A / B / C 选项、Luke 选了哪个"。

Luke 2026-10-19 同意读这台 Mac 上的会话，只抽他的选择，结果只放 private/l3/（会话里有工作内容，永远不进公开仓库）。
只用规则抽（确定的事用代码）：选项要有 2 个以上字母，Luke 的回复要能明确对上一个字母或"按你推荐"；对不上的不收。

用法：
  python3 tools/evolve/l3_extract.py            抽一遍，写 private/l3/decisions.jsonl，打印统计
"""
import collections, hashlib, json, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "private" / "l3"
HOME = Path.home()

OPT = re.compile(r"(?m)^[ \t]*(?:[-*][ \t]*)?(?:\*\*)?(?:方案|选项)?[ \t]*([A-E])(?:[ \t]*[（(]推荐[)）])?(?:\*\*)?(?:[ \t]*[：:．.、)）]|[ \t]+(?=[\u4e00-\u9fff]))")
REC = [re.compile(r"([A-E])[ \t]*(?:\*\*)?[（(]推荐[)）]"), re.compile(r"推荐[ \t]*(?:方案|选)?[ \t:：]*\**([A-E])\b"),
       re.compile(r"([A-E])[ \t]*(?:\*\*)?[ \t]*（我?推荐")]
FOLLOW = re.compile(r"(按|照|听)(你|您)?(的)?(推荐|建议|说的)|按推荐|就按你")
SKIP_USER = ("<", "[SYSTEM", "Another Claude session", "# AGENTS.md", "Base directory for this skill", "Caveat:", "[Request interrupted")


def clean_user(t):
    t = (t or "").strip()
    if not t or t.startswith(SKIP_USER) or "<environment_context>" in t or "<task-notification>" in t:
        return None
    return t


def claude_turns(f):
    turns = []
    for line in f.read_text(errors="ignore").split("\n"):
        if not line.strip():
            continue
        try:
            d = json.loads(line)
        except Exception:
            continue
        if d.get("isSidechain") or d.get("isMeta"):
            continue
        m = d.get("message") if isinstance(d.get("message"), dict) else {}
        c = m.get("content")
        ts = d.get("timestamp", "")
        if d.get("type") == "user":
            if isinstance(c, str):
                t = clean_user(c)
                if t:
                    turns.append(("user", t, ts))
            elif isinstance(c, list):
                for b in c:
                    if b.get("type") == "text":
                        t = clean_user(b.get("text"))
                        if t:
                            turns.append(("user", t, ts))
                    elif b.get("type") == "tool_result":
                        r = b.get("content")
                        r = " ".join(x.get("text", "") for x in r if isinstance(x, dict)) if isinstance(r, list) else str(r or "")
                        if "have been answered" in r or "User has answered" in r:
                            turns.append(("ask_answer", r, ts))
        elif d.get("type") == "assistant" and isinstance(c, list):
            for b in c:
                if b.get("type") == "text" and b.get("text", "").strip():
                    turns.append(("assistant", b["text"], ts))
                elif b.get("type") == "tool_use" and b.get("name") == "AskUserQuestion":
                    turns.append(("ask", json.dumps(b.get("input", {}), ensure_ascii=False), ts))
    return turns


def codex_turns(f):
    turns = []
    with open(f, errors="ignore") as fh:
        for line in fh:
            if '"role":"user"' not in line.replace(" ", "") and '"role":"assistant"' not in line.replace(" ", ""):
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            p = d.get("payload") or {}
            if d.get("type") != "response_item" or p.get("type") != "message":
                continue
            txt = "\n".join(c.get("text", "") for c in p.get("content", []) if isinstance(c, dict))
            if p.get("role") == "user":
                t = clean_user(txt)
                if t:
                    turns.append(("user", t, d.get("timestamp", "")))
            elif txt.strip():
                turns.append(("assistant", txt, d.get("timestamp", "")))
    return turns


def recommended(text):
    for r in REC:
        m = r.search(text)
        if m:
            return m.group(1)
    return ""


def choice_of(reply, letters, rec):
    r = reply.strip()
    if len(r) > 80:
        head = r[:40]
    else:
        head = r
    m = re.match(r"^[ \t]*(?:选|就|用|方案|我选)?[ \t]*([A-E])(?![A-Za-z])", head)
    if m and m.group(1) in letters:
        return m.group(1)
    m = re.search(r"(?:选|方案)[ \t]*([A-E])(?![A-Za-z])", head)
    if m and m.group(1) in letters:
        return m.group(1)
    if FOLLOW.search(head) and rec:
        return rec
    return ""


def options(text):
    letters = []
    for m in OPT.finditer(text):
        if m.group(1) not in letters:
            letters.append(m.group(1))
    # 要从 A 开始、连续
    seq = [l for l in "ABCDE"][:len(letters)]
    return letters if len(letters) >= 2 and sorted(letters) == seq else []


def extract(turns, source, path):
    out = []
    pending_asst = []
    for i, (role, text, ts) in enumerate(turns):
        if role == "assistant":
            pending_asst.append(text)
            continue
        if role == "ask":
            try:
                q = json.loads(text)
            except Exception:
                continue
            nxt = next((t for t in turns[i + 1:i + 4] if t[0] == "ask_answer"), None)
            if not nxt:
                continue
            for qq in q.get("questions", []):
                labels = [o.get("label", "") for o in qq.get("options", [])]
                ans = re.search(re.escape(qq.get("question", "")) + r'"?\s*=\s*"([^"]+)"', nxt[1])
                if not labels or not ans:
                    continue
                pick = ans.group(1)
                letters = "ABCD"[:len(labels)]
                ch = next((letters[k] for k, l in enumerate(labels) if l and l == pick), "其他")
                rec = next((letters[k] for k, l in enumerate(labels) if "推荐" in l or "Recommended" in l), "")
                descs = [o.get("description", "") for o in qq.get("options", [])]
                out.append(dict(kind="ask_tool", question=qq.get("question", ""),
                                options={letters[k]: (l + ("：" + descs[k] if descs[k] else "")) for k, l in enumerate(labels)},
                                recommended=rec, reply=pick[:200], choice=ch, ts=ts))
            pending_asst = []
            continue
        if role == "user":
            asst = "\n".join(pending_asst)[-4000:]
            pending_asst = []
            letters = options(asst)
            if not letters:
                continue
            rec = recommended(asst)
            ch = choice_of(text, letters, rec)
            # "A，B，通过" 这类一句话回好几道题的，对不上是哪道，不收
            if not ch or len(re.findall(r"(?<![A-Za-z])[A-E](?![A-Za-z])", text[:30])) > 1:
                continue
            out.append(dict(kind="text", question=asst, options={l: "" for l in letters}, recommended=rec,
                            reply=text[:300], choice=ch, ts=ts))
    for r in out:
        r["source"], r["file"] = source, str(path)
        r["follows_rec"] = bool(r["recommended"]) and r["choice"] == r["recommended"]
        r["id"] = hashlib.sha1((r["file"] + r["ts"] + r["reply"][:50]).encode()).hexdigest()[:12]
    return out


def main():
    files = [("claude", f) for f in (HOME / ".claude" / "projects").glob("*/*.jsonl")]
    files += [("codex", f) for f in (HOME / ".codex" / "sessions").rglob("*.jsonl")]
    files += [("codex", f) for f in (HOME / ".codex" / "archived_sessions").rglob("*.jsonl")]
    rows, seen = [], set()
    for src, f in files:
        try:
            turns = claude_turns(f) if src == "claude" else codex_turns(f)
        except Exception as e:
            print(f"跳过 {f.name}：{e}", file=sys.stderr)
            continue
        for r in extract(turns, src, f):
            k = (r["ts"][:16], r["reply"][:30])
            if k in seen:   # Luke 常把同一句连发几遍
                continue
            seen.add(k)
            rows.append(r)
    rows.sort(key=lambda r: r["ts"])
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "decisions.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    c = collections.Counter((r["source"], r["kind"]) for r in rows)
    withrec = [r for r in rows if r["recommended"]]
    print(f"会话文件 {len(files)} 个，抽到选择 {len(rows)} 条：{dict(c)}")
    if withrec:
        print(f"有推荐项的 {len(withrec)} 条，跟推荐走 {sum(r['follows_rec'] for r in withrec)} 条（{sum(r['follows_rec'] for r in withrec) / len(withrec):.0%}）")
    print(f"时间范围：{rows[0]['ts'][:10] if rows else ''} ～ {rows[-1]['ts'][:10] if rows else ''}")


if __name__ == "__main__":
    main()
