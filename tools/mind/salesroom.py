#!/usr/bin/env python3
"""接 Salesroom 的会议数据，给 lukeeMind 两样东西：客户现场的真实声音，和 Luke 在会上的判断。

Luke 2026-10-23 选了 C：两个都做。会议是公司销售团队和真实客户的对话，属于客户资料：
- 原始会议只存 private/salesroom/meetings/（本机，不进任何 git，private 仓库也不提交原文）
- 逐场抽取只用本地 Qwen（数据不出这台机器）；Qwen 连不上就跳过，下次再抽，不改用外部模型
- 汇总给 Opus 之前把客户名换成"行业＋规模"的代号；永远不交给 Jev 或任何外部接口
密钥在 .env 的 SALESROOM_API_KEY，不写进代码和日志。

用法：
  salesroom.py sync [--since 2026-10-01]   翻页拉会议，以后只拉更新过的
  salesroom.py extract [--limit 30]        本地 Qwen 逐场抽：客户原话（痛点、顾虑、决策流程、信号、价格、竞品）和 Luke 的判断
  salesroom.py synthesize                  去掉客户名后，用 Opus 汇成两份：客户真实声音、Luke 的会上判断
  salesroom.py stats
"""
import argparse, collections, datetime as dt, json, os, re, sys, urllib.parse, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(REPO / "tools" / "evolve"))
import l1_eval as E  # noqa: E402
import opus_judge as OJ  # noqa: E402

DIR = E.PRIVATE / "salesroom"
MEET, EXT = DIR / "meetings", DIR / "extract"
STATE = DIR / "state.json"
VOICE = E.PRIVATE / "luke" / "customer-voice.md"
JUDGE = E.PRIVATE / "luke" / "luke-in-meetings.md"
LUKE_PAT = re.compile(r"Luke|ルーク|劉|刘|リュウ|仙升", re.I)


def get(path, params):
    url = os.environ["SALESROOM_BASE_URL"].rstrip("/") + path + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Authorization": "Bearer " + os.environ["SALESROOM_API_KEY"],
                                               "User-Agent": "weird-knowledge-research-bot"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)


def cmd_sync(a):
    E.load_env()
    MEET.mkdir(parents=True, exist_ok=True)
    st = json.loads(STATE.read_text()) if STATE.exists() else {}
    since = a.since + "T00:00:00Z" if a.since else st.get("updated_since", "2026-10-01T00:00:00Z")
    started = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    cursor, n, new, pages = None, 0, 0, 0
    while True:
        params = {"updated_since": since, "limit": 100}
        if cursor:
            params["cursor"] = cursor
        d = get("/api/export/meetings", params)
        pages += 1
        for m in d.get("items", []):
            f = MEET / f"{m['meetingId']}.json"
            new += not f.exists()
            f.write_text(json.dumps(m, ensure_ascii=False))
            n += 1
        cursor = d.get("nextCursor")
        if not cursor or not d.get("items") or pages > 200:
            break
    st.update(updated_since=started, last_sync=started)
    STATE.write_text(json.dumps(st, ensure_ascii=False, indent=1))
    print(json.dumps({"pages": pages, "fetched": n, "new": new, "total": len(list(MEET.glob("*.json")))}, ensure_ascii=False))


def qwen_json(prompt, max_tokens=1800):
    d = E.post(E.os.environ["QWEN_BASE_URL"] + "/chat/completions", {
        "model": "qwen3.8-27b-coder390-mlx-mixed4-mtp",
        "messages": [{"role": "system", "content": "你是 B2B 销售分析员，只输出一个 JSON 对象，不要多余的字。"},
                     {"role": "user", "content": prompt}],
        "max_tokens": max_tokens, "temperature": 0, "chat_template_kwargs": {"enable_thinking": False}},
        E.os.environ["QWEN_API_KEY"])
    text = d["choices"][0]["message"]["content"]
    i = text.find("{")
    obj, _ = json.JSONDecoder().raw_decode(text[i:])
    return obj


PROMPT = """下面是一场日本 B2B 销售会议的会议纪要（Salesroom 自动生成），{luke_hint}

请抽出两部分，用中文写，客户原话保留日语原文（每句不超过 60 字）。**不写任何人名和公司名**：人用角色代替（客户方负责人、决策者、现场担当、我方销售、我方技术），公司用"客户""合作伙伴""竞品 A"代替：

1. customer：客户这一方
   - industry：客户的行业，size：规模（看得出来就写，看不出来写"不明"）
   - role_of_meeting：这场会处在哪个阶段（初次接触 / 需求确认 / 提案 / 报价 / 试用 / 签约 / 运营支持 / 合作伙伴 / 其他）
   - pains：客户说出的痛点（最多 5 条，每条带一句原话 quote）
   - concerns：客户的顾虑或反对（价格、安全、效果、内部说服、人手……，最多 5 条，带原话）
   - decision：决策流程和角色（谁拍板、要不要稟議、预算时间、还要谁同意）
   - signals：成交或推进的信号，以及冷淡、拖延的信号（分开写）
   - price：提到的价格、预算数字（原样）
   - competitors：提到的竞品或现有做法
   - next_steps：约定的下一步

2. luke：Luke（刘，Sparticle 增长负责人）在会上的判断。只有纪要里能明确看出是他说的、他定的，才写；看不出来就给空数组
   - judgments：每条写 situation（当时的情况）、what（他说了或决定了什么）、why（纪要里能看出的理由，看不出写空）

只输出 JSON：{{"customer": {{...}}, "luke": {{"present": true/false, "judgments": [...]}}}}

会议标题：{title}
日期：{date}

纪要：
{summary}"""


def cmd_extract(a):
    E.load_env()
    if not OJ.qwen_ok():
        sys.exit("本地 Qwen 连不上：客户资料不交给外部模型，这次先不抽")
    EXT.mkdir(parents=True, exist_ok=True)
    todo = [f for f in sorted(MEET.glob("*.json"), key=lambda f: f.stat().st_mtime, reverse=True)
            if not (EXT / f.name).exists() or (EXT / f.name).stat().st_mtime < f.stat().st_mtime][: a.limit]
    ok = bad = 0
    for f in todo:
        m = json.loads(f.read_text())
        text = (m.get("summary") or "") + "\n" + (m.get("transcript") or "")
        hint = "纪要里提到了 Luke（刘），请特别留意他说了什么、定了什么。" if LUKE_PAT.search(text) else "纪要里没有看到 Luke（刘）。"
        try:
            out = qwen_json(PROMPT.format(luke_hint=hint, title=m.get("title", ""), date=m.get("date", ""),
                                          summary=(m.get("summary") or "")[:9000]))
            out.update(meetingId=m["meetingId"], date=m.get("date"), customer_id=(m.get("customer") or {}).get("id"),
                       customer_name=(m.get("customer") or {}).get("name"), luke_mentioned=bool(LUKE_PAT.search(text)))
            (EXT / f.name).write_text(json.dumps(out, ensure_ascii=False))
            ok += 1
        except Exception as e:
            bad += 1
            print(f"  {f.stem} 抽取失败：{str(e)[:120]}", file=sys.stderr)
    print(json.dumps({"extracted": ok, "failed": bad, "remaining": len([f for f in MEET.glob('*.json') if not (EXT / f.name).exists()])},
                     ensure_ascii=False))


HONORIFIC = re.compile(r"[\u4e00-\u9fff\u3040-\u30ffA-Za-z]{1,8}(?:氏|さん|様|さま|部長|課長|社長|会長|専務|常務)")


def all_customer_names():
    names = set()
    for f in MEET.glob("*.json"):
        n = (json.loads(f.read_text()).get("customer") or {}).get("name")
        if n and len(n) >= 2:
            names.add(n)
    return sorted(names, key=len, reverse=True)


def scrub(s, names):
    """交给 Opus 前最后一道清洗：所有客户公司名、带敬称的人名都换掉。"""
    for n in names:
        s = s.replace(n, "某客户")
    return HONORIFIC.sub("某人", s)


def anonymize(rows):
    """客户名换成"行业＋规模＋编号"的代号，名字和 id 都不出本机。"""
    names = all_customer_names()
    code, out = {}, []
    for r in rows:
        c = r.get("customer") or {}
        key = r.get("customer_id") or r.get("customer_name") or r["meetingId"]
        if key not in code:
            code[key] = f"{c.get('industry') or '行业不明'}·{c.get('size') or '规模不明'}·{len(code) + 1:03d}"
        s = json.dumps({k: v for k, v in r.items() if k not in ("customer_id", "customer_name", "meetingId")}, ensure_ascii=False)
        if r.get("customer_name"):
            s = s.replace(r["customer_name"], code[key])
        s = scrub(s, names)
        out.append({"client": code[key], **json.loads(s)})
    return out


def cmd_synthesize(_):
    rows = anonymize([json.loads(f.read_text()) for f in sorted(EXT.glob("*.json"))])
    if not rows:
        sys.exit("还没有抽取结果")
    cust = [{"client": r["client"], "date": r.get("date"), **(r.get("customer") or {})} for r in rows]
    # 一次塞不下（首次全量约 67 万字），先分批归纳、再合成，免得只看到前四分之一（2026-10-24 踩过）
    chunks, cur = [], []
    for c in cust:
        cur.append(c)
        if len(json.dumps(cur, ensure_ascii=False)) > 140000:
            chunks.append(cur[:-1]); cur = [c]
    if cur:
        chunks.append(cur)
    partials = []
    for i, ch in enumerate(chunks, 1):
        part = OJ.ask_json(
            "你是日本 B2B 市场的销售研究员。只输出 JSON。",
            f"下面是第 {i}/{len(chunks)} 批会议里抽出的客户方信息（客户名已换成代号）。按主题归纳："
            "痛点、顾虑和反对、决策和稟議、推进信号、冷淡信号、价格和预算、竞品和现有做法。每个主题列出规律，"
            "每条写 pattern（一句话）、clients（出现在这批里的客户代号列表）、quotes（1～2 句日语原话）。只写看得出来的。\n\n"
            + json.dumps(ch, ensure_ascii=False) + '\n\n只输出 JSON：{"themes": {"主题": [{"pattern": "", "clients": [], "quotes": []}]}}',
            timeout=900)
        partials.append(part.get("themes", {}))
        print(f"  第 {i}/{len(chunks)} 批归纳完", file=sys.stderr, flush=True)
    voice = OJ.ask_json(
        "你是日本 B2B 市场的销售研究员。只输出 JSON。",
        f"下面是 {len(chunks)} 批会议各自归纳的规律（同一个客户代号在各批里指同一家客户）。请合成一份给 agent 用的「客户真实声音」："
        "中文，2,500 字以内；按主题写（痛点、顾虑和反对、决策和稟議、推进信号、冷淡信号、价格和预算、竞品和现有做法），"
        "相同的规律合并，每条注明一共出现在几家客户（按客户代号去重计数）、附 1～2 句日语原话；按出现客户数从多到少排；"
        "最后写「对获客和写邮件的启发」3～5 条，标明是推断。只写数据里看得出来的，不编。\n\n"
        + json.dumps(partials, ensure_ascii=False) + '\n\n只输出 JSON：{"md": "正文"}', timeout=1200)
    head = (f"# 客户真实声音（Salesroom 会议）\n\n> {dt.date.today()} 由 `tools/mind/salesroom.py synthesize` 生成：本地 Qwen 逐场抽取，"
            f"去掉客户名后交给 Opus 汇总。共 {len(rows)} 场会议、{len({r['client'] for r in rows})} 家客户。客户资料，只在本机。\n\n")
    VOICE.write_text(head + voice["md"].strip() + "\n")
    # 纪要里根本没提到 Luke 却抽出"他的判断"的，多半是模型张冠李戴，不用（2026-10-24 首次全量：5 场）
    lk = [{"client": r["client"], "date": r.get("date"), **(r.get("luke") or {})} for r in rows
          if (r.get("luke") or {}).get("judgments") and r.get("luke_mentioned")]
    if lk:
        judge = OJ.ask_json(
            "你在归纳一个具体的人 Luke 在销售会议上的判断方式。只输出 JSON。",
            "下面是 Luke（Sparticle 增长负责人）在客户会议上明确说过或定过的事（客户名已换成代号）。请写「Luke 在会上怎么判断」：中文，1,200 字以内；"
            "归纳他反复用的判断方式（先问什么、怎么回应顾虑、怎么定价和让步、什么时候推进什么时候放手），每条附 1～2 个例子；只写看得出来的，不编。\n\n"
            + json.dumps(lk, ensure_ascii=False)[:120000] + '\n\n只输出 JSON：{"md": "正文"}', timeout=900)
        JUDGE.write_text(f"# Luke 在会上怎么判断（Salesroom 会议）\n\n> {dt.date.today()} 生成，来自 {len(lk)} 场他明确发言的会议。客户资料，只在本机。\n\n"
                         + judge["md"].strip() + "\n")
    print(json.dumps({"meetings": len(rows), "clients": len({r['client'] for r in rows}), "luke_meetings": len(lk),
                      "voice": str(VOICE), "judge": str(JUDGE) if lk else ""}, ensure_ascii=False))


def cmd_stats(_):
    ms = [json.loads(f.read_text()) for f in MEET.glob("*.json")]
    ex = list(EXT.glob("*.json")) if EXT.exists() else []
    dates = sorted(m.get("date", "") for m in ms)
    print(json.dumps({"meetings": len(ms), "extracted": len(ex), "clients": len({(m.get('customer') or {}).get('id') for m in ms}),
                      "date_range": [dates[0], dates[-1]] if dates else [],
                      "luke_mentioned": sum(bool(LUKE_PAT.search((m.get('summary') or '') + (m.get('transcript') or ''))) for m in ms)},
                     ensure_ascii=False))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("sync"); p.add_argument("--since", default="")
    p = sub.add_parser("extract"); p.add_argument("--limit", type=int, default=30)
    sub.add_parser("synthesize")
    sub.add_parser("stats")
    a = ap.parse_args()
    {"sync": cmd_sync, "extract": cmd_extract, "synthesize": cmd_synthesize, "stats": cmd_stats}[a.cmd](a)


if __name__ == "__main__":
    main()
