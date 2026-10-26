#!/usr/bin/env python3
"""问 lukeeMind：别的 agent 交来"问题、选项、背景"，回"Luke 多半选哪个、有多确定、依据是什么、要不要必须交给 Luke"。

方案见 docs/2026-10-20-ask-lukeemind-spec.md。Luke 2026-10-20 定的：先做命令行；放权门槛"某一类满 30 次、一致率 90%、零漏报"。
提问、背景、Luke 的回填只存 private/mind/（本机，不进公开仓库），只交给 Opus 5.5 判断，不交给 Jev 或任何外部接口。

用法：
  ask.py ask --from <谁> --question "…" [--options "A:…|B:…"] [--context-file <背景>] [--client <客户名>]
  ask.py record <id> --luke <字母> [--note "Luke 原话"] [--should-ask yes|no]
  ask.py taste --text "…" [--author 名字] [--from 谁]   Luke 会不会想看这条内容（概率 + 最像的三条他点过赞的）
  ask.py profile [--work]          打印 Luke 当前的口味 skill 和原则；--work 再附上 Salesroom 里的客户真实声音、他在会上的判断
  ask.py report                    按类别报一致率、漏报、能不能升级
  ask.py quiz [--n 10]             补数据：列出别的 agent 问过、还没回填 Luke 选了什么的题（最早的先出），不给 lukeeMind 的猜测
  ask.py quiz-answer "1A 2C 3-"    按上一次 quiz 的题号回填（- 表示跳过）
  ask.py backtest [--n 109] [--workers 4] [--sources on|off] [--notes on|off] [--rules off|sim]
                                   用 private/l3 的旧选择题回测（只用更早的题做例子、更早的卡提炼的规律）
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
    # Luke 2026-10-20 试问时定的：替他通知同事、给同事发说明，也要先问他
    "替 Luke 通知同事": r"告诉\S{0,8}|通知\S{0,8}|转告|知会|讲解|给\S{1,8}(讲|说明|发)|发给\S{1,8}|伝えて|連絡して|共有して|let \w+ know|tell \w+",
}
CATEGORIES = ["钱", "合同和法律", "交期和上线", "人事", "凭据和权限", "对外发送", "替 Luke 通知同事", "删除和难撤销", "方向取舍",
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


# 回答里带"背后的道理"：Luke 2026-10-25 选了 A，回测准确率不掉才把默认改成开。
# 2026-10-25 回测：同样 124 题，带 103、不带 102，高确定 34/35 对 33/34，所以默认开
SOURCES_DEFAULT = True   # 10-25 晚改成先挑硬证据后重测：124 题带 104、不带 102
TYPE_LABEL = {"论文": "研究论文", "方法论": "方法"}


def root_info(slug):
    p = E.REPO / "roots" / f"{slug}.md"
    if not p.exists():
        return None
    x = p.read_text()
    g = lambda k: (re.search(rf'^{k}:\s*"?(.*?)"?\s*$', x, re.M) or [None, ""])[1]
    rows = re.findall(r"^\| \[.*?\]\(\.\./clips/.*\| (强|弱[^|]*) \|$", x, re.M)
    one = x.split("## 一句话", 1)[1].split("\n## ", 1)[0].strip().split("\n")[0] if "## 一句话" in x else ""
    label = "厂商调查" if "厂商调查" in one else TYPE_LABEL.get(g("type"), g("type") or "来源")
    return dict(slug=slug, name=g("name_zh"), label=label, line=one,
                strong=sum(r == "强" for r in rows), n=len(rows))


VARIANT_DEFAULT = "full"   # 2026-10-25 Luke 选了 A：精简版和现在的版本各跑两遍旧题，确实更准才换
SOFT_LABELS = {"研究报告": 1, "厂商调查": 2}   # 咨询公司报告、厂商调查排在理论、论文、政府资料后面


def principle_sources(k=2):
    """每条原则在 framework.md 里链到的源知识，先挑硬证据，再按"强关系多、被指向多"挑前 k 个。"""
    t = (E.REPO / "framework.md").read_text().split("\n## 二、")[0]
    parts = re.split(r"\n### (原则 \d+：[^\n]*)", t)
    out = {}
    for head, body in zip(parts[1::2], parts[2::2]):
        info = [r for r in map(root_info, dict.fromkeys(re.findall(r"\(roots/([^)]+)\.md\)", body))) if r]
        out[head] = sorted(info, key=lambda r: (SOFT_LABELS.get(r["label"], 0), -r["strong"], -r["n"]))[:k]
    return out


def principles_with_sources():
    lines = []
    for head, roots in principle_sources().items():
        lines.append(head)
        lines += [f"  背后的道理 [{r['slug']}] {r['name']}（{r['label']}）：{r['line']}" for r in roots]
    return "\n".join(lines)


def attach_sources(evidence):
    """模型只交 slug，道理的名字、类型和一句话由这里从 roots/ 里取，不让模型自己写，免得编。"""
    known = {r["slug"]: r for rs in principle_sources().values() for r in rs}
    texts, used = [], []
    for e in evidence[:3]:
        if isinstance(e, str):
            texts.append(e)
            continue
        point, r = str(e.get("point", "")).strip(), known.get(str(e.get("source", "")).strip())
        if r:
            point += f"。背后的道理：{r['name']}（{r['label']}）：{r['line']}"
            used.append({k: r[k] for k in ("slug", "name", "label")})
        texts.append(point)
    return texts, used


def luke_words(text):
    """Luke 回答里字母之外补的话。只回了一个字母、补数据题的固定说明、提问方替他写的转述，都算没补。"""
    t = re.sub(r"^\s*[A-Z]\s*[:：.、，,]?\s*", "", text or "").strip()
    return "" if len(t) < 8 or t == "每周补数据题" or t.startswith("Luke 只回了") else t


def past_decisions(before="", client=""):
    """能当例子的旧选择：L3 抽出来的选择题，加上回填过的提问（只取同一客户或不涉及客户的）。note 是他补的原话。"""
    out = []
    for r in read_jsonl(E.PRIVATE / "l3" / "decisions.jsonl"):
        if r["choice"] in r["options"] and (not before or r["ts"] < before):
            q = r["question"] + ("\n" + "\n".join(f"{k}. {v}" for k, v in r["options"].items()) if r["kind"] == "ask_tool" else "")
            out.append({"id": r["id"], "text": q[-1500:], "choice": r["choice"], "note": luke_words(r.get("reply"))})
    for r in read_jsonl(ASKS):
        if r.get("luke") and (not r.get("client") or r.get("client") == client) and (not before or r["at"] < before):
            q = r["question"] + "\n" + "\n".join(f"{k}. {v}" for k, v in r["options"].items())
            out.append({"id": r["id"], "text": q[-1500:], "choice": r["luke"], "note": luke_words(r.get("luke_note"))})
    return out


# Luke 2026-10-26 选了 B：例子带上他补的原话，再加上每周从回答和纠正里提炼、他认过的规律（tools/mind/distill.py）。
# 回测准确率不掉才把默认改成开，回测见 docs/2026-10-26-mind-distill-spec.md
# 2026-10-26 回测：同样 128 题各跑两遍，现状 107、105，带原话加按周模拟的规律 108、107，所以默认开
NOTES_DEFAULT = True
RULES_DEFAULT = True


def mind_rules():
    """Luke 认过的拿主意规律。"""
    return [r for r in read_jsonl(DIR / "rules.jsonl") if r.get("status") == "已确认"]


def clean_ids(s):
    """提炼时模型会把案例卡编号写进句子里，交给模型和给人看之前去掉。"""
    s = re.sub(r"\d{8}-\d{6}-[0-9a-f]{6}|\b[0-9a-f]{12}\b", "", s or "")
    return re.sub(r"[（(][\s、，,]*[）)]", "", s).strip()


def render_rules(rules):
    return ("【他拿主意时的规律】（从他以前的回答和纠正里提炼，他确认过；情境对得上才用）\n" +
            "\n".join(f"- {clean_ids(r['rule'])}" + (f"（不适用：{clean_ids(r['when_not'])}）" if r.get("when_not") else "")
                      for r in rules))


SYS = ("你是 lukeeMind，在替一个具体的人 Luke 预判他会怎么选。别的 agent 遇到要替 Luke 拿主意的事来问你。"
       "根据他的档案、原则、确认过的规律和他以前的相似选择，判断他多半选哪个。只输出一个 JSON 对象。")


def taste_skill():
    champ = json.loads((E.PRIVATE / "l1" / "champion.json").read_text())
    return (E.PRIVATE / "luke" / champ["profile"]).read_text()


def build_prompt(question, options, context, examples, with_sources=False, variant="full", notes=False, mrules=()):
    rules = principles_with_sources() if with_sources else principles()
    if variant == "slim":
        # 精简版：只给原则和口味 skill，不给档案和确认过的规律（Jev 测试时发现这样 Opus 反而多对 4 题，待回测确认）
        parts = ["【他确认过的做事原则】\n" + rules, "【Luke 的口味说明】\n" + taste_skill()]
    else:
        profile = (E.PRIVATE / "luke" / "profile.md").read_text()
        confirmed = (E.PRIVATE / "luke" / "confirmed.md").read_text()
        parts = ["【Luke 的档案】\n" + profile, "【他确认过的做事原则】\n" + rules, "【他确认过的规律】\n" + confirmed]
    if mrules:
        parts.append(render_rules(mrules))
    if examples:
        parts.append("【他以前的相似选择】（只看他怎么判断，不要把里面的客户和项目事实搬到这次）\n" +
                     "\n\n".join(f"题：{e['text'][-700:]}\n他选了：{e['choice']}" +
                                 (f"\n他补的话：{e['note'][:200]}" if notes and e.get("note") else "") for e in examples))
    if context:
        parts.append("【这次的背景】\n" + context[:6000])
    if options:
        parts.append("【这次的问题】\n" + question + "\n" + "\n".join(f"{k}. {v}" for k, v in options.items()))
    else:
        parts.append("【这次的问题】\n" + question + "\n（没有给选项：先列出 2～4 个现实的做法，标 A、B、C…，再判断。）")
    evidence = ('"evidence": [{"point": "一句话依据：引用哪条原则、哪次相似选择或档案里的哪一点", '
                '"source": "引用了原则时，从那条原则下面列的「背后的道理」里挑最贴切的一个，填方括号里的英文编号；没有贴切的就填空字符串"}]（最多 3 条），\n'
                if with_sources else
                '"evidence": ["一句话依据：引用哪条原则、哪次相似选择或档案里的哪一点"]（最多 3 条），\n')
    parts.append("输出 JSON，字段：\n"
                 '"options": {"A": "选项原文或你列的做法"}，\n'
                 '"probs": {"A": 概率}（加起来等于 1），\n' + evidence +
                 f'"category": 从这些里选一个：{"、".join(CATEGORIES)}，\n'
                 '"must_ask_luke": true 或 false（碰钱、合同、交期上线、人事、凭据权限、对外发送、替 Luke 通知同事或给同事发说明、删除和难撤销、方向取舍，一律 true），\n'
                 '"must_ask_reason": "一句话"，\n'
                 '"note": "用 Luke 的口气写给他的一句话建议"')
    return "\n\n".join(parts)


def judge(question, options, context="", client="", before="", with_sources=None, variant=None, notes=None, mrules=None):
    with_sources = SOURCES_DEFAULT if with_sources is None else with_sources
    variant = VARIANT_DEFAULT if variant is None else variant
    notes = NOTES_DEFAULT if notes is None else notes
    mrules = (mind_rules() if RULES_DEFAULT else []) if mrules is None else mrules
    pool = past_decisions(before, client)
    examples = []
    if pool:
        idx = E.Index(pool)
        examples = idx.top(question + "\n" + "\n".join(options.values()) + "\n" + context[:500], 4)
    out = OJ.ask_json(SYS, build_prompt(question, options, context, examples, with_sources, variant, notes, mrules))
    evidence, sources = attach_sources(out.get("evidence") or [])
    opts = options or {k: str(v) for k, v in (out.get("options") or {}).items()}
    probs = {k: float((out.get("probs") or {}).get(k, 0) or 0) for k in opts}
    z = sum(probs.values()) or 1
    probs = {k: round(v / z, 3) for k, v in probs.items()}
    choice = max(probs, key=probs.get) if probs else ""
    top = probs.get(choice, 0)
    confidence = "高" if top >= 0.8 else "中" if top >= 0.6 else "低"
    # 规则只看问题和选项：背景里常有"部署、权限、token"这类词，全算进来几乎每题都要问（回测 104 题判了 100 题）
    flags = rule_flags(question + "\n" + "\n".join(opts.values()))
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
                evidence=evidence, sources=sources, category=category, rule_flags=flags,
                must_ask_luke=must, must_ask_reason="；".join(dict.fromkeys(reasons)), opus_must=bool(out.get("must_ask_luke")),
                level=level, act=act,
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


def cmd_taste(a):
    """问口味：用当前冠军（本地 Qwen + 口味 skill + 8 条相似点赞）判 Luke 会不会想看。Qwen 连不上时改用 Opus 读 skill 判。"""
    E.load_env()
    champ = json.loads((E.PRIVATE / "l1" / "champion.json").read_text())
    skill = (E.PRIVATE / "luke" / champ["profile"]).read_text()
    text = Path(a.file).read_text() if a.file else a.text
    idx = E.Index(E.liked_docs(set()))
    ex = idx.top(text, champ.get("k", 8))
    row = {"author": a.author, "text": text}
    try:
        if not OJ.qwen_ok():
            raise RuntimeError("Qwen 连不上")
        p = E.qwen(E.prompt(row, champ["cond"], skill, ex))
        engine = "qwen+skill"
    except Exception:
        out = OJ.ask_json("你在模拟一个具体的人 Luke，判断他会不会想看。只输出 JSON。",
                          f"【Luke 的阅读口味】\n{skill}\n\n【要判断的内容】作者 {a.author}\n{text[:2000]}\n\n"
                          '输出 {"p": 他想看的概率 0 到 1}')
        p, engine = float(out.get("p", 0)), "opus+skill"
    res = {"p": round(p, 3), "verdict": "多半想看" if p >= 0.6 else "多半不想看" if p <= 0.4 else "拿不准",
           "engine": engine, "similar_likes": [e["text"][:120] for e in ex[:3]]}
    DIR.mkdir(parents=True, exist_ok=True)
    with open(DIR / "taste.jsonl", "a") as f:
        f.write(json.dumps({"at": now().isoformat(timespec="seconds"), "from": a.from_, "author": a.author,
                            "text": text[:500], **res}, ensure_ascii=False) + "\n")
    print(json.dumps(res, ensure_ascii=False, indent=1))


def cmd_profile(a):
    """打印 Luke 的画像：口味 skill、12 条原则；加 --work 再附上 Salesroom 会议里的客户真实声音和他在会上的判断（客户资料已去名，只在本机）。"""
    champ = json.loads((E.PRIVATE / "l1" / "champion.json").read_text())
    print((E.PRIVATE / "luke" / champ["profile"]).read_text())
    # 给别的 agent 读的画像不做预测，直接带上每条原则背后的道理，方便它们向人解释
    print("\n---\n他确认过的做事原则（每条后面是背后的道理，括号里是证据类型）：\n" + principles_with_sources())
    if a.work:
        for name in ("luke-in-meetings.md", "customer-voice.md"):
            f = E.PRIVATE / "luke" / name
            if f.exists():
                print("\n---\n" + f.read_text())


def cmd_quiz(a):
    """每周的补数据题：先出别的 agent 真实问过、还没回填的题。不显示 lukeeMind 猜的答案，免得带偏 Luke。"""
    todo = [r for r in read_jsonl(ASKS) if not r.get("luke") and r.get("options") and r.get("from") != "smoke-test"][:a.n]
    (DIR / "quiz-last.json").write_text(json.dumps([r["id"] for r in todo]))
    for i, r in enumerate(todo, 1):
        print(f"{i}. {r['question'].strip()[:220]}（{r['at'][:10]}，{r['from']} 问的）")
        for k, v in r["options"].items():
            print(f"   {k}. {v[:120]}")
    print(f"\n共 {len(todo)} 题。回法：1A 2C 3-（- 表示跳过）")


def cmd_quiz_answer(a):
    ids = json.loads((DIR / "quiz-last.json").read_text())
    rows = read_jsonl(ASKS)
    by = {r["id"]: r for r in rows}
    n = 0
    for num, letter in re.findall(r"(\d+)\s*([A-Za-z-])", a.answers):
        i = int(num) - 1
        if letter == "-" or not (0 <= i < len(ids)) or ids[i] not in by:
            continue
        r = by[ids[i]]
        if letter.upper() not in r["options"]:
            continue
        r.update(luke=letter.upper(), luke_note="每周补数据题", recorded=now().isoformat(timespec="seconds"),
                 agree=letter.upper() == r["choice"])
        n += 1
    write_jsonl(ASKS, rows)
    print(f"回填 {n} 题")


def cmd_backtest(a):
    """用旧选择题回测：去掉推荐标记，只用更早的题做例子，看猜中几道、有没有把"该问 Luke"的事判成不用问。"""
    E.load_env()
    import l3_eval as L
    import concurrent.futures as cf
    rows = [r for r in read_jsonl(E.PRIVATE / "l3" / "decisions.jsonl") if r["choice"] in r["options"]][-a.n:]
    with_sources = SOURCES_DEFAULT if a.sources == "default" else a.sources == "on"
    variant = VARIANT_DEFAULT if a.variant == "default" else a.variant
    notes = NOTES_DEFAULT if a.notes == "default" else a.notes == "on"
    # sim：按周模拟提炼，每题只用它之前最近一次提炼出的规律（distill.py sim 产出，只用更早的案例卡写的）
    snaps = sorted((json.loads(f.read_text()) for f in (DIR / "distill").glob("sim-*.json")), key=lambda s: s["cutoff"]) \
        if a.rules == "sim" else []

    def rules_for(r):
        if a.rules == "off":
            return []
        if a.rules == "default":
            return mind_rules() if RULES_DEFAULT else []
        got = [s["rules"] for s in snaps if s["cutoff"] <= r["ts"][:10]]
        return got[-1] if got else []

    def one(r):
        q = L.strip_rec(r["question"] if r["kind"] == "ask_tool" else r["question"][-2500:])
        opts = {k: L.strip_rec(v) or f"选项 {k}" for k, v in r["options"].items()}
        mr = rules_for(r)
        try:
            return {"id": r["id"], "luke": r["choice"], "rec": r["recommended"], "n_rules": len(mr),
                    **judge(q, opts, before=r["ts"], with_sources=with_sources, variant=variant, notes=notes, mrules=mr)}
        except Exception as e:
            print(f"  {r['id']} 出错：{e}", file=sys.stderr)

    out = []
    with cf.ThreadPoolExecutor(a.workers) as ex:
        for i, res in enumerate(ex.map(one, rows), 1):
            if res:
                out.append(res)
            if i % 10 == 0:
                print(f"  {i}/{len(rows)}", file=sys.stderr, flush=True)
    stamp = now().strftime("%Y%m%d-%H%M")
    DIR.mkdir(parents=True, exist_ok=True)
    tag = f"sources-{'on' if with_sources else 'off'}-{variant}-notes-{'on' if notes else 'off'}-rules-{a.rules}"
    write_jsonl(DIR / f"backtest-{stamp}-{a.label or tag}.jsonl", out)
    n = len(out)
    agree = sum(o["choice"] == o["luke"] for o in out)
    dev = [o for o in out if o["rec"] and o["luke"] != o["rec"]]
    must = [o for o in out if o["must_ask_luke"]]
    ruled = [o for o in out if o.get("n_rules")]
    high = [o for o in out if o["confidence"] == "高"]
    print(json.dumps({"tag": tag, "n": n, "agree": f"{agree}/{n}（{agree / max(n, 1):.0%}）",
                      "luke_against_rec": f"{sum(o['choice'] == o['luke'] for o in dev)}/{len(dev)}",
                      "with_rules": f"{sum(o['choice'] == o['luke'] for o in ruled)}/{len(ruled)}",
                      "high_conf": f"{sum(o['choice'] == o['luke'] for o in high)}/{len(high)}",
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
    p = sub.add_parser("taste")
    p.add_argument("--text", default="")
    p.add_argument("--file", default="")
    p.add_argument("--author", default="")
    p.add_argument("--from", dest="from_", default="unknown")
    p = sub.add_parser("profile"); p.add_argument("--work", action="store_true", help="附上客户真实声音和 Luke 在会上的判断")
    p = sub.add_parser("quiz"); p.add_argument("--n", type=int, default=10)
    p = sub.add_parser("quiz-answer"); p.add_argument("answers")
    p = sub.add_parser("backtest")
    p.add_argument("--n", type=int, default=109)
    p.add_argument("--workers", type=int, default=1)
    p.add_argument("--sources", choices=["on", "off", "default"], default="default", help="依据里带不带背后的道理（源知识）")
    p.add_argument("--variant", choices=["full", "slim", "default"], default="default", help="full：档案加确认过的规律；slim：只给原则和口味 skill")
    p.add_argument("--notes", choices=["on", "off", "default"], default="default", help="例子里带不带 Luke 补的原话")
    p.add_argument("--rules", choices=["off", "sim", "default"], default="default",
                   help="拿主意的规律：off 不带；sim 用 distill.py sim 按周模拟提炼的；default 用 Luke 认过的（RULES_DEFAULT 开着时）")
    p.add_argument("--label", default="", help="结果文件名里的标记，默认按开关自动起")
    a = ap.parse_args()
    {"ask": cmd_ask, "record": cmd_record, "report": cmd_report, "backtest": cmd_backtest,
     "taste": cmd_taste, "profile": cmd_profile, "quiz": cmd_quiz, "quiz-answer": cmd_quiz_answer}[a.cmd](a)


if __name__ == "__main__":
    main()
