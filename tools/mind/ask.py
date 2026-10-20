#!/usr/bin/env python3
"""问 lukeeMind：别的 agent 交来"问题、选项、背景"，回"Luke 多半选哪个、有多确定、依据是什么、要不要必须交给 Luke"。

方案见 docs/2026-10-20-ask-lukeemind-spec.md。Luke 2026-10-20 定的：先做命令行；放权门槛"某一类满 30 次、一致率 90%、零漏报"。
提问、背景、Luke 的回填只存 private/mind/（本机，不进公开仓库），只交给 Opus 5.5 判断，不交给 Jev 或任何外部接口。

用法：
  ask.py ask --from <谁> --question "…" [--options "A:…|B:…"] [--context-file <背景>] [--client <客户名>]
  ask.py record <id> --luke <字母> [--note "Luke 原话"] [--should-ask yes|no]
  ask.py report                    按类别报一致率、漏报、能不能升级
  ask.py backtest [--n 109]        用 private/l3 的旧选择题回测（只用更早的题做例子）
"""
import argparse, collections, datetime as dt, hashlib, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(REPO / "tools" / "evolve"))
import l1_eval as E  # noqa: E402
import opus_judge as OJ  # noqa: E402

DIR = E.PRIVATE / "mind"
ASKS, LEVELS = DIR / "asks.jsonl", DIR / "levels.json"
GATE = {"n": 30, "agree": 0.9, "misses": 0}   # 升一级的门槛，Luke 2026-10-20 定的

# 必须交给 Luke 的事：和 Codex 的 Lukee 现有规则、Luke 全局规则第 3 节、原则 12 对齐。命中就问，不管模型怎么说
MUST_ASK = {
    "钱": r"报价|价格|定价|折扣|优惠|付款|支付|收费|费用|预算|花钱|采购|発注|見積|値引|請求|pricing|discount|invoice|payment|budget",
    "合同和法律": r"合同|契约|契約|条款|法务|法律|律师|NDA|保密协议|規約|contract|legal|terms",
    "交期和上线": r"交期|交付|上线|发布|发版|部署|合并|merge|上線|リリース|納期|deadline|release|deploy",
    "人事": r"招聘|录用|辞退|裁员|薪资|工资|绩效|面试|採用|人事|給与|hire|fire|salary",
    "凭据和权限": r"密码|密钥|凭据|token|API ?key|权限|管理员|账号共享|パスワード|権限|credential|permission|admin",
    "对外发送": r"发给客户|回复客户|发邮件|群发|对外|公开发布|发帖|客户说|お客様|メール送信|送信|publish|post to|send to",
    "删除和难撤销": r"删除|删掉|清空|重置|覆盖|回滚|不可逆|削除|delete|drop table|force push|reset --hard",
}
CATEGORIES = ["钱", "合同和法律", "交期和上线", "人事", "凭据和权限", "对外发送", "删除和难撤销", "方向取舍",
              "产品和设计", "技术实现", "工作方法和工具", "内容和学习", "其他"]
ALWAYS_LUKE = set(MUST_ASK) | {"方向取舍"}   # 这些类别永远停在 0 级


def now():
    return dt.datetime.now()


def read_jsonl(p):
    return [json.loads(l) for l in p.read_text().split("\n") if l.strip()] if p.exists() else []


def write_jsonl(p, rows):
    p.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))


def parse_options(s):
    opts = {}
    for part in (s or "").split("|"):
        m = re.match(r"\s*([A-Z])\s*[:：]\s*(.+)", part)
        if m:
            opts[m.group(1)] = m.group(2).strip()
    return opts


def rule_flags(text):
    return [k for k, pat in MUST_ASK.items() if re.search(pat, text, re.I)]


def principles():
    t = (E.REPO / "framework.md").read_text()
    return "\n".join(re.findall(r"^### (原则 \d+：.*)$", t, re.M))


def past_decisions(before="", client=""):
    """能当例子的旧选择：L3 抽出来的选择题，加上回填过的提问（只取同一客户或不涉及客户的）。"""
    out = []
    for r in read_jsonl(E.PRIVATE / "l3" / "decisions.jsonl"):
        if r["choice"] in r["options"] and (not before or r["ts"] < before):
            q = r["question"] + ("\n" + "\n".join(f"{k}. {v}" for k, v in r["options"].items()) if r["kind"] == "ask_tool" else "")
            out.append({"id": r["id"], "text": q[-1500:], "choice": r["choice"]})
    for r in read_jsonl(ASKS):
        if r.get("luke") and (not r.get("client") or r.get("client") == client) and (not before or r["at"] < before):
            q = r["question"] + "\n" + "\n".join(f"{k}. {v}" for k, v in r["options"].items())
            out.append({"id": r["id"], "text": q[-1500:], "choice": r["luke"]})
    return out


SYS = ("你是 lukeeMind，在替一个具体的人 Luke 预判他会怎么选。别的 agent 遇到要替 Luke 拿主意的事来问你。"
       "根据他的档案、原则、确认过的规律和他以前的相似选择，判断他多半选哪个。只输出一个 JSON 对象。")


def build_prompt(question, options, context, examples):
    profile = (E.PRIVATE / "luke" / "profile.md").read_text()
    confirmed = (E.PRIVATE / "luke" / "confirmed.md").read_text()
    parts = ["【Luke 的档案】\n" + profile, "【他确认过的做事原则】\n" + principles(), "【他确认过的规律】\n" + confirmed]
    if examples:
        parts.append("【他以前的相似选择】（只看他怎么判断，不要把里面的客户和项目事实搬到这次）\n" +
                     "\n\n".join(f"题：{e['text'][-700:]}\n他选了：{e['choice']}" for e in examples))
    if context:
        parts.append("【这次的背景】\n" + context[:6000])
    if options:
        parts.append("【这次的问题】\n" + question + "\n" + "\n".join(f"{k}. {v}" for k, v in options.items()))
    else:
        parts.append("【这次的问题】\n" + question + "\n（没有给选项：先列出 2～4 个现实的做法，标 A、B、C…，再判断。）")
    parts.append("输出 JSON，字段：\n"
                 '"options": {"A": "选项原文或你列的做法"}，\n'
                 '"probs": {"A": 概率}（加起来等于 1），\n'
                 '"evidence": ["一句话依据：引用哪条原则、哪次相似选择或档案里的哪一点"]（最多 3 条），\n'
                 f'"category": 从这些里选一个：{"、".join(CATEGORIES)}，\n'
                 '"must_ask_luke": true 或 false（碰钱、合同、交期上线、人事、凭据权限、对外发送、删除和难撤销、方向取舍，一律 true），\n'
                 '"must_ask_reason": "一句话"，\n'
                 '"note": "用 Luke 的口气写给他的一句话建议"')
    return "\n\n".join(parts)


def judge(question, options, context="", client="", before=""):
    pool = past_decisions(before, client)
    examples = []
    if pool:
        idx = E.Index(pool)
        examples = idx.top(question + "\n" + "\n".join(options.values()) + "\n" + context[:500], 4)
    out = OJ.ask_json(SYS, build_prompt(question, options, context, examples))
    opts = options or {k: str(v) for k, v in (out.get("options") or {}).items()}
    probs = {k: float((out.get("probs") or {}).get(k, 0) or 0) for k in opts}
    z = sum(probs.values()) or 1
    probs = {k: round(v / z, 3) for k, v in probs.items()}
    choice = max(probs, key=probs.get) if probs else ""
    top = probs.get(choice, 0)
    confidence = "高" if top >= 0.8 else "中" if top >= 0.6 else "低"
    flags = rule_flags(question + "\n" + "\n".join(opts.values()) + "\n" + context[:3000])
    category = out.get("category") if out.get("category") in CATEGORIES else "其他"
    reasons = []
    if flags:
        reasons.append("碰到了" + "、".join(flags))
    if out.get("must_ask_luke"):
        reasons.append(out.get("must_ask_reason") or "模型判断要问")
    if confidence == "低":
        reasons.append("lukeeMind 拿不准")
    if category in ALWAYS_LUKE:
        reasons.append(f"「{category}」永远交给 Luke")
    level = json.loads(LEVELS.read_text()).get(category, 0) if LEVELS.exists() else 0
    must = bool(reasons)
    act = "follow" if (not must and level >= 1 and confidence == "高") else "ask_luke"
    return dict(choice=choice, options=opts, probs=probs, confidence=confidence,
                evidence=(out.get("evidence") or [])[:3], category=category, rule_flags=flags,
                must_ask_luke=must, must_ask_reason="；".join(dict.fromkeys(reasons)), level=level, act=act,
                note=out.get("note", ""), examples=[e["id"] for e in examples])


def cmd_ask(a):
    E.load_env()
    options = parse_options(a.options)
    context = Path(a.context_file).read_text() if a.context_file else ""
    res = judge(a.question, options, context, a.client)
    rid = now().strftime("%Y%m%d-%H%M%S-") + hashlib.sha1(a.question.encode()).hexdigest()[:6]
    DIR.mkdir(parents=True, exist_ok=True)
    with open(ASKS, "a") as f:
        f.write(json.dumps({"id": rid, "at": now().isoformat(timespec="seconds"), "from": a.from_, "client": a.client,
                            "question": a.question, "context": context, **res, "luke": "", "luke_note": ""},
                           ensure_ascii=False) + "\n")
    print(json.dumps({"id": rid, **{k: v for k, v in res.items() if k != "examples"}}, ensure_ascii=False, indent=1))


def cmd_record(a):
    rows = read_jsonl(ASKS)
    hit = [r for r in rows if r["id"] == a.id]
    if not hit:
        sys.exit(f"没有这个编号：{a.id}")
    r = hit[0]
    r.update(luke=a.luke.upper(), luke_note=a.note, recorded=now().isoformat(timespec="seconds"),
             agree=a.luke.upper() == r["choice"])
    if a.should_ask:
        r["should_ask"] = a.should_ask == "yes"
        r["miss"] = r["should_ask"] and not r["must_ask_luke"]   # 漏报：本该交给 Luke，却判成不用问
    write_jsonl(ASKS, rows)
    print(json.dumps({"id": r["id"], "lukeeMind": r["choice"], "luke": r["luke"], "agree": r["agree"],
                      "miss": r.get("miss", False)}, ensure_ascii=False))


def cmd_report(_):
    rows = [r for r in read_jsonl(ASKS) if r.get("luke")]
    allq = read_jsonl(ASKS)
    print(f"提问 {len(allq)} 次，回填 {len(rows)} 次")
    levels = json.loads(LEVELS.read_text()) if LEVELS.exists() else {}
    g = collections.defaultdict(list)
    for r in rows:
        g[r["category"]].append(r)
    for cat, rs in sorted(g.items(), key=lambda kv: -len(kv[1])):
        n, agree, misses = len(rs), sum(r["agree"] for r in rs), sum(r.get("miss", False) for r in rs)
        ok = cat not in ALWAYS_LUKE and n >= GATE["n"] and agree / n >= GATE["agree"] and misses <= GATE["misses"]
        print(f"  {cat}：{n} 次，一致 {agree}/{n}（{agree / n:.0%}），漏报 {misses}，现在 {levels.get(cat, 0)} 级"
              + ("，够升级了，请 Luke 定" if ok else ""))


def cmd_backtest(a):
    """用旧选择题回测：去掉推荐标记，只用更早的题做例子，看猜中几道、有没有把"该问 Luke"的事判成不用问。"""
    E.load_env()
    import l3_eval as L
    rows = [r for r in read_jsonl(E.PRIVATE / "l3" / "decisions.jsonl") if r["choice"] in r["options"]][-a.n:]
    out = []
    for i, r in enumerate(rows, 1):
        q = L.strip_rec(r["question"] if r["kind"] == "ask_tool" else r["question"][-2500:])
        opts = {k: L.strip_rec(v) or f"选项 {k}" for k, v in r["options"].items()}
        try:
            res = judge(q, opts, before=r["ts"])
        except Exception as e:
            print(f"  第 {i} 题出错：{e}", file=sys.stderr)
            continue
        out.append({"id": r["id"], "luke": r["choice"], "rec": r["recommended"], **res})
        if i % 10 == 0:
            print(f"  {i}/{len(rows)}", file=sys.stderr, flush=True)
    stamp = now().strftime("%Y%m%d-%H%M")
    DIR.mkdir(parents=True, exist_ok=True)
    write_jsonl(DIR / f"backtest-{stamp}.jsonl", out)
    n = len(out)
    agree = sum(o["choice"] == o["luke"] for o in out)
    dev = [o for o in out if o["rec"] and o["luke"] != o["rec"]]
    must = [o for o in out if o["must_ask_luke"]]
    print(json.dumps({"n": n, "agree": f"{agree}/{n}（{agree / max(n, 1):.0%}）",
                      "luke_against_rec": f"{sum(o['choice'] == o['luke'] for o in dev)}/{len(dev)}",
                      "must_ask_luke": len(must), "by_category": dict(collections.Counter(o["category"] for o in out)),
                      "confidence": dict(collections.Counter(o["confidence"] for o in out))}, ensure_ascii=False, indent=1))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("ask")
    p.add_argument("--from", dest="from_", default="unknown")
    p.add_argument("--question", required=True)
    p.add_argument("--options", default="")
    p.add_argument("--context-file", default="")
    p.add_argument("--client", default="")
    p = sub.add_parser("record")
    p.add_argument("id")
    p.add_argument("--luke", required=True)
    p.add_argument("--note", default="")
    p.add_argument("--should-ask", choices=["yes", "no"], default="")
    sub.add_parser("report")
    p = sub.add_parser("backtest")
    p.add_argument("--n", type=int, default=109)
    a = ap.parse_args()
    {"ask": cmd_ask, "record": cmd_record, "report": cmd_report, "backtest": cmd_backtest}[a.cmd](a)


if __name__ == "__main__":
    main()
