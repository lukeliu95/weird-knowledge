#!/usr/bin/env python3
"""L3 对照试验：决定预测时让 Opus 一层层翻 Luke 的知识库（渐进式披露），和现在的做法比。

起因：Luke 2026-10-25 问，能不能让库里的知识用渐进式披露的方式参与思考。现在 ask.py 和 l3_eval.py 的 q2
只给原则标题、口味档案和 4 道相似旧题，roots/ 和 clips/ 一条都不读。

两个版本，同一批题、同样按批交给 Opus、同样的输出（概率 + 依据）：
  base  l3_eval.py 的 q2：档案 + 13 条原则标题 + 4 道之前答过的相似题（推荐标记去掉）
  pd    base 再加"可以翻资料"：每题可以先要材料、看完再答，最多翻 2 轮，第 3 轮必须答
          第 0 层  原则标题（本来就有）
          第 1 层  P<n>：原则正文（证据、矛盾、没想清楚的问题，里面链到源知识和新知识）
          第 2 层  root:<slug>：源知识（一句话、原始出处、更底层的源头、指向它的新知识前 8 条）
          第 3 层  clip:<文件名>：新知识（标题、为什么存、原文开头、溯源）
          检索     search:<关键词>：在全部源知识里找最像的 5 条
  must  同 pd，但第 1 轮每题都必须先翻至少 1 项再答（试跑时 pd 让 Opus 自己决定，6 道题一项都没翻）
档案和原则标题每批只放一次（l3_eval 是每题重复一遍），两个版本一样，所以 base 在这里重跑，不和 10-20 的成绩直接比。
材料里"Luke 选了 X"这类话会删掉，免得翻到某道题本身的答案。

用法：
  python3 tools/evolve/l3_disclose.py run --arm base|pd|must [--limit N] [--tag x]
  python3 tools/evolve/l3_disclose.py compare <base.jsonl> <pd.jsonl> [--noise <base2.jsonl>]
"""
import argparse, collections, concurrent.futures as cf, datetime as dt, json, math, random, re, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import l1_eval as E  # noqa: E402
import l3_eval as L3  # noqa: E402
import opus_judge as OJ  # noqa: E402
from l1_report import split  # noqa: E402

RUNS = L3.DIR / "runs"
BUDGET = 100_000   # 一次调用的正文上限（字）：超了会被截断且不报错（经验库 10-24）
ROUNDS = 3

SYS = "你在模拟一个具体的人：Luke。AI 助手给他出了几道选择题。估计他选每个选项的概率，并给出依据。只输出一个 JSON 对象。"
FMT = ('输出格式：{"题号": {"probs": {"A": 概率, "B": 概率}, "evidence": ["一句话依据"]}}。每题概率加起来等于 1；'
       'evidence 最多 3 条，每条写明出自哪里（原则 N、相似题、档案，或你翻到的材料编号）。')
PD_HELP = """【可以翻资料】
上面的原则只有标题。Luke 的知识库是一棵树，你可以按需往下翻：
- P<n>：第 n 条原则的正文（证据、矛盾、没想清楚的问题），里面用〔root:…〕〔clip:…〕标出它连着的源知识和新知识
- root:<slug>：一条源知识（理论、方法论、论文）：一句话、原始出处、更底层的源头、指向它的新知识
- clip:<文件名>：一条 Luke 存下的新知识：标题、他为什么存、原文开头、溯源
- search:<关键词>：在 957 条源知识里检索，回最像的 5 条
拿不准、或者想给依据找到出处时就翻；有把握的直接答。某题要先翻，就只写 {"open": ["P11", "root:galls-law", "search:冷邮件 回信率"]}，每题每轮最多 4 项，不写 probs。
材料只帮你理解 Luke 怎么想，不要把里面的客户、项目事实搬到题目里。"""

FW = (E.REPO / "framework.md").read_text()
LINK = re.compile(r"\[([^\]]+)\]\((?:\.\./)?(?:(roots|clips)/)?([^)/\s]+?)\.md\)")
KIND = {"roots": "root", "clips": "clip"}


def relink(t, bare):
    """把 markdown 链接换成可以直接要的编号：[名字](../roots/x.md) → 名字〔root:x〕。同目录的裸链接按 bare 算。"""
    return LINK.sub(lambda m: f"{m.group(1)}〔{KIND.get(m.group(2), bare)}:{m.group(3)}〕", t)


def noleak(t):
    return re.sub(r"[，,；;]?[^，,；;。\n（）()]*选了[^，,；;。\n（）()]*", "", t)


def fm(t):
    m = re.match(r"---\n(.*?)\n---", t, re.S)
    out = {}
    for line in (m.group(1).split("\n") if m else []):
        k, _, v = line.partition(":")
        out[k.strip()] = v.strip().strip('"')
    return out


def section(t, name):
    m = re.search(rf"^## {re.escape(name)}\s*\n(.*?)(?=^## |\Z)", t, re.M | re.S)
    return m.group(1).strip() if m else ""


def principle(n):
    m = re.search(rf"^### 原则 {n}：.*?(?=^### |^## |\Z)", FW, re.M | re.S)
    return relink(noleak(m.group(0)), "root")[:4000] if m else None


def root(slug):
    f = E.REPO / "roots" / f"{slug.removesuffix('.md')}.md"
    if not f.exists():
        return None
    t = f.read_text()
    h = fm(t)
    rows = [l for l in section(t, "指向它的新知识").split("\n") if l.startswith("| [")]
    body = (f"{h.get('name_zh')}（{h.get('name_en')}），{h.get('proposer')}，{h.get('year')}\n"
            f"一句话：{section(t, '一句话')}\n原始出处：\n{section(t, '原始出处')[:800]}\n"
            f"更底层的源头：\n{section(t, '更底层的源头')}\n"
            f"指向它的新知识（共 {len(rows)} 条，列前 8 条）：\n" + "\n".join(rows[:8]))
    return relink(noleak(body), "root")[:3000]


def clip(name):
    f = E.REPO / "clips" / f"{name.removesuffix('.md')}.md"
    if not f.exists():
        return None
    t = f.read_text()
    h = fm(t)
    body = (f"{h.get('title')}｜{h.get('author')}｜发布 {h.get('published')}｜Luke 为什么存：{h.get('why')}\n"
            f"原文开头：\n{section(t, '原文')[:1500]}\n溯源：\n{section(t, '溯源')[:800]}")
    return relink(noleak(body), "clip")[:3000]


_RIDX = None


def search(kw):
    global _RIDX
    if _RIDX is None:
        docs = []
        for f in sorted((E.REPO / "roots").glob("*.md")):
            t = f.read_text()
            h = fm(t)
            docs.append({"id": f.stem, "text": f"{h.get('name_zh')}（{h.get('name_en')}）：{section(t, '一句话')[:120]}"})
        _RIDX = E.Index(docs)
    return "\n".join(f"root:{d['id']} — {d['text']}" for d in _RIDX.top(kw, 5))


def open_item(it):
    it = str(it).strip()
    m = re.fullmatch(r"(?:[Pp]|原则)\s*(\d+)", it)
    if m:
        return principle(m.group(1))
    kind, _, arg = it.partition(":")
    f = {"root": root, "clip": clip, "search": search}.get(kind.strip().lower())
    return f(arg.strip()) if f and arg.strip() else None


def block(r, ex, mats):
    s = ""
    if ex:
        s += "【他以前答过的相似题】\n" + "\n\n".join(f"题：{L3.render(e)[-600:]}\n他选了：{e['choice']}" for e in ex) + "\n\n"
    s += f"【这道题】\n{L3.render(r)}\n选项：{'/'.join(r['options'])}"
    if mats:
        s += "\n\n【你为这道题翻到的材料】\n" + "\n\n".join(f"〈{k}〉\n{v}" for k, v in mats)
    return s


def batches(blocks, base, cap=10):
    out, cur, size = [], [], base
    for qid, b in blocks:
        if cur and (len(cur) >= cap or size + len(b) > BUDGET):
            out.append(cur)
            cur, size = [], base
        cur.append((qid, b))
        size += len(b) + 20
    return out + [cur] if cur else out


def call(header, batch, footer):
    body = header + "\n\n" + "\n\n".join(f"===== 题 {k} =====\n{b}" for k, (_, b) in enumerate(batch)) + "\n\n" + footer
    for attempt in range(3):
        try:
            obj, meta = OJ.ask_json_meta(SYS, body)
            break
        except Exception as e:   # 偶尔超时或没给 JSON，歇一下重试
            if attempt == 2:
                raise
            print("重试：", str(e)[:120], flush=True)
            time.sleep(10)
    return {qid: obj.get(str(k)) or {} for k, (qid, _) in enumerate(batch)}, meta, len(body)


def norm(probs, letters):
    p = {k: float((probs or {}).get(k, 0) or 0) for k in letters}
    z = sum(p.values())
    return {k: v / z for k, v in p.items()} if z else {k: 1 / len(letters) for k in letters}


def load_rows():
    rows = [json.loads(l) for l in (L3.DIR / "decisions.jsonl").read_text().split("\n") if l.strip()]
    return [r for r in rows if r["choice"] in r["options"]]


def cmd_run(a):
    E.load_env()
    pd, must = a.arm in ("pd", "must"), a.arm == "must"
    rows = load_rows()
    profile = (E.PRIVATE / "luke" / json.loads((E.PRIVATE / "l1" / "champion.json").read_text())["profile"]).read_text()
    ex = []
    for i, r in enumerate(rows):   # 只取这道题之前答过的，防止偷看未来（同 l3_eval q2）
        idx = E.Index([{"id": j, "text": L3.render(x)} for j, x in enumerate(rows[:i])]) if i else None
        ex.append([rows[d["id"]] for d in idx.top(L3.render(r), 4)] if idx else [])
    todo = list(range(len(rows)))
    if a.limit:
        todo = todo[::max(1, len(todo) // a.limit)][:a.limit]
    header = "【Luke 的档案】\n" + profile + "\n\n【他确认过的做事原则】\n" + L3.principles() + ("\n\n" + PD_HELP if pd else "")
    last = ROUNDS if pd else 1
    mats = collections.defaultdict(list)
    cost = collections.defaultdict(float)
    secs = collections.defaultdict(float)
    result, calls, pending = {}, [], todo
    t0 = time.time()
    for rnd in range(1, last + 1):
        if not pending:
            break
        bs = batches([(i, block(rows[i], ex[i], mats[i])) for i in pending], len(header) + 600)

        def footer(n):
            s = FMT + f"\n按题号 0～{n - 1} 输出。"
            if must and rnd == 1:
                s += f"\n这是第 1 轮：每题都必须先写 open（1～4 项），不要写 probs。最多 {last} 轮，第 {last} 轮每题都必须给 probs。"
            elif pd:
                s += ("\n这是最后一轮：每题都必须给 probs，不能再 open。" if rnd == last else
                      f"\n要先翻资料的题写 open。这是第 {rnd} 轮，最多 {last} 轮，第 {last} 轮每题都必须给 probs。")
            return s

        with cf.ThreadPoolExecutor(3) as pool:
            outs = list(pool.map(lambda b: call(header, b, footer(len(b))), bs))
        nxt = []
        for b, (res, meta, chars) in zip(bs, outs):
            calls.append({"round": rnd, "n": len(b), "chars": chars, **meta})
            for qid, _ in b:
                cost[qid] += (meta.get("cost_usd") or 0) / len(b)
                secs[qid] += (meta.get("duration_ms") or 0) / 1000 / len(b)
                d = res.get(qid) or {}
                if d.get("probs"):
                    result[qid] = {"dist": norm(d["probs"], list(rows[qid]["options"])), "evidence": (d.get("evidence") or [])[:3],
                                   "round": rnd}
                elif rnd < last:
                    done = {k for k, _ in mats[qid]}
                    for it in [x for x in (d.get("open") or []) if str(x) not in done][:4]:
                        mats[qid].append((str(it), open_item(it) or "（没找到这一项）"))
                    nxt.append(qid)
        print(f"第 {rnd} 轮：{len(bs)} 次调用，答了 {sum(1 for q in pending if q in result)} 题，要翻资料 {len(nxt)} 题", flush=True)
        pending = nxt
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M")
    name = f"{stamp}-disclose-{a.arm}{'-' + a.tag if a.tag else ''}"
    out = []
    for i in todo:
        r, res = rows[i], result.get(i)
        dist = res["dist"] if res else {k: 1 / len(r["options"]) for k in r["options"]}
        out.append({"id": r["id"], "split": split(r["id"]), "choice": r["choice"], "rec": r["recommended"],
                    "pred": max(dist, key=dist.get), "dist": dist, "evidence": res["evidence"] if res else [],
                    "round": res["round"] if res else None, "missing": not res, "opened": [k for k, _ in mats[i]],
                    "cost_usd": round(cost[i], 5), "secs": round(secs[i], 1)})
    RUNS.mkdir(parents=True, exist_ok=True)
    (RUNS / f"{name}.jsonl").write_text("".join(json.dumps(o, ensure_ascii=False) + "\n" for o in out))
    (RUNS / f"{name}.meta.json").write_text(json.dumps({"arm": a.arm, "n": len(out), "wall_secs": round(time.time() - t0),
                                                         "calls": calls}, ensure_ascii=False, indent=1))
    hits = sum(o["pred"] == o["choice"] for o in out)
    print(f"{name}：{hits}/{len(out)} = {hits / len(out):.3f}，没答 {sum(o['missing'] for o in out)} 题，"
          f"花费 ${sum(o['cost_usd'] for o in out):.2f}，用时 {round(time.time() - t0)} 秒")
    print(RUNS / f"{name}.jsonl")


# ---------- 比较 ----------

def load(p):
    return {o["id"]: o for o in (json.loads(l) for l in Path(p).read_text().split("\n") if l.strip())}


def nll(o):
    return -math.log(max(o["dist"].get(o["choice"], 0), 1e-6))


def paired(ids, A, B, f, n=4000, seed=7):
    """同一批题重抽样，两个版本一起算；返回平均差和"B 比 A 好"的概率（f 越大越好）。"""
    rnd, gains = random.Random(seed), []
    for _ in range(n):
        s = [rnd.choice(ids) for _ in ids]
        gains.append(sum(f(B[i]) - f(A[i]) for i in s) / len(s))
    return sum(gains) / len(gains), sum(g > 0 for g in gains) / len(gains), sum(g >= 0 for g in gains) / len(gains)


CITE_KB = re.compile(r"(?:root|clip):[\w.\-]+|P\d+")


def cites(o):
    ev = " ".join(o["evidence"])
    return {"principle": bool(re.search(r"原则\s*\d+|P\d+", ev)), "kb": bool(re.search(r"(?:root|clip):", ev)),
            "ids": re.findall(r"(root|clip):([\w.\-]+)", ev)}


def meta_of(p):
    m = Path(str(p).removesuffix(".jsonl") + ".meta.json")
    return json.loads(m.read_text()) if m.exists() else {}


def cmd_compare(a):
    A, B = load(a.base), load(a.cand)
    ids = [i for i in A if i in B]
    acc = lambda o: float(o["pred"] == o["choice"])  # noqa: E731
    negnll = lambda o: -nll(o)  # noqa: E731
    subsets = {"全部": ids, "开发集": [i for i in ids if A[i]["split"] == "dev"], "测试集": [i for i in ids if A[i]["split"] == "test"],
               "跟推荐走": [i for i in ids if A[i]["rec"] and A[i]["choice"] == A[i]["rec"]],
               "不跟推荐走": [i for i in ids if A[i]["rec"] and A[i]["choice"] != A[i]["rec"]],
               "没有推荐": [i for i in ids if not A[i]["rec"]]}
    print("| 题 | 题数 | base 猜对 | pd 猜对 | base NLL | pd NLL |")
    print("|---|---|---|---|---|---|")
    for k, s in subsets.items():
        if s:
            print(f"| {k} | {len(s)} | {sum(acc(A[i]) for i in s):.0f} ({sum(acc(A[i]) for i in s) / len(s):.3f}) | "
                  f"{sum(acc(B[i]) for i in s):.0f} ({sum(acc(B[i]) for i in s) / len(s):.3f}) | "
                  f"{sum(nll(A[i]) for i in s) / len(s):.3f} | {sum(nll(B[i]) for i in s) / len(s):.3f} |")
    for k in ("测试集", "全部"):
        s = subsets[k]
        g1, p1, q1 = paired(s, A, B, acc)
        g2, p2, _ = paired(s, A, B, negnll)
        print(f"{k} 成对比较：猜对率 {g1:+.3f}，pd 更好的概率 {p1:.0%}（不变差 {q1:.0%}）；NLL {-g2:+.3f}，pd 更好的概率 {p2:.0%}")
    if a.noise:
        C = load(a.noise)
        s = [i for i in ids if i in C]
        print(f"噪音（base 重跑一次）：猜对 {sum(acc(A[i]) for i in s):.0f} vs {sum(acc(C[i]) for i in s):.0f}，"
              f"预测不同 {sum(A[i]['pred'] != C[i]['pred'] for i in s)} 题；pd 和 base 预测不同 {sum(A[i]['pred'] != B[i]['pred'] for i in s)} 题")
    print("\n依据：")
    for name, X in (("base", A), ("pd", B)):
        cs = [cites(X[i]) for i in ids]
        cited = [c for x in cs for c in x["ids"]]
        exist = sum((E.REPO / ("roots" if k == "root" else "clips") / f"{v.removesuffix('.md')}.md").exists() for k, v in cited)
        opened = sum(1 for i in ids if X[i].get("opened"))
        print(f"  {name}：引了原则 {sum(c['principle'] for c in cs)}/{len(ids)} 题，引了源知识或新知识 {sum(c['kb'] for c in cs)}/{len(ids)} 题"
              f"（共 {len(cited)} 处，真实存在 {exist} 处）；翻过资料 {opened} 题，没答 {sum(X[i]['missing'] for i in ids)} 题")
    items = [it for i in ids for it in B[i].get("opened", [])]
    kinds = collections.Counter("原则" if re.match(r"(?:[Pp]|原则)\s*\d", it) else it.split(":")[0] for it in items)
    print(f"  pd 翻了什么：共 {len(items)} 项，{dict(kinds)}；最常翻的：{collections.Counter(items).most_common(8)}")
    op = [i for i in ids if B[i].get("opened")]
    if op:
        print(f"  翻过资料的 {len(op)} 题：base 猜对 {sum(acc(A[i]) for i in op):.0f}，pd 猜对 {sum(acc(B[i]) for i in op):.0f}")
    print("\n花费（按 API 价折算，订阅不另收钱）：")
    for name, p, X in (("base", a.base, A), ("pd", a.cand, B)):
        m = meta_of(p)
        calls = m.get("calls", [])
        print(f"  {name}：{len(calls)} 次调用，${sum(X[i]['cost_usd'] for i in ids):.2f}（每题 ${sum(X[i]['cost_usd'] for i in ids) / len(ids):.3f}），"
              f"每题约 {sum(X[i]['secs'] for i in ids) / len(ids):.1f} 秒（调用时间平摊），整轮 {m.get('wall_secs')} 秒")
    diff = [i for i in ids if A[i]["pred"] != B[i]["pred"]]
    print("\n两个版本猜得不一样的题：")
    for i in diff:
        print(f"  {i} [{A[i]['split']}] Luke 选 {A[i]['choice']}（推荐 {A[i]['rec']}）：base {A[i]['pred']}，pd {B[i]['pred']}，pd 翻了 {B[i].get('opened')}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--arm", required=True, choices=["base", "pd", "must"])
    r.add_argument("--limit", type=int, default=0)
    r.add_argument("--tag", default="")
    c = sub.add_parser("compare")
    c.add_argument("base")
    c.add_argument("cand")
    c.add_argument("--noise", default="")
    a = ap.parse_args()
    {"run": cmd_run, "compare": cmd_compare}[a.cmd](a)


if __name__ == "__main__":
    main()
