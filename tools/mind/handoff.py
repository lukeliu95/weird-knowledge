#!/usr/bin/env python3
"""把 lukeeMind 手里 Luke 的个人画像打成一包，交给 Codex 里的 Lukee 记。

Luke 2026-10-28 选了 A：选择、纠正、补的话、确认过的规律、放权级别这些个人记录交给 Lukee；
口味 skill、点赞预测、兴趣地图留在 lukeeMind（它们决定 lukeeMind 上网学什么）。
交接以后 `ask.py ask` 不再读 private/luke/ 和旧选择，改读 Lukee 用 --profile-file、--choices-file 交进来的。
方案见 docs/2026-10-28-personal-profile-handoff.md。

用法：
  handoff.py export [--out private/handoff/lukee-YYYYMMDD]
"""
import argparse, datetime as dt, json, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[0] / "evolve"))
sys.path.insert(0, str(HERE))
import l1_eval as E  # noqa: E402
import ask as A  # noqa: E402

LUKE, MIND, L3 = E.PRIVATE / "luke", E.PRIVATE / "mind", E.PRIVATE / "l3"


def past_choices():
    """L3 抽出来的旧选择，加上别的 agent 问过、Luke 回填过的题。note 是他字母之外补的原话。"""
    out = []
    for r in A.read_jsonl(L3 / "decisions.jsonl"):
        if r["choice"] in r["options"]:
            q = r["question"] + ("\n" + "\n".join(f"{k}. {v}" for k, v in r["options"].items()) if r["kind"] == "ask_tool" else "")
            out.append({"id": r["id"], "ts": r["ts"], "text": q[-1500:], "choice": r["choice"], "note": A.luke_words(r.get("reply"))})
    for r in A.read_jsonl(MIND / "asks.jsonl"):
        if r.get("luke"):
            q = r["question"] + "\n" + "\n".join(f"{k}. {v}" for k, v in r["options"].items())
            out.append({"id": r["id"], "ts": r["at"], "text": q[-1500:], "choice": r["luke"],
                        "note": A.luke_words(r.get("luke_note")), "client": r.get("client", "")})
    return out


def profile_text():
    """交给 ask.py --profile-file 的那一份：档案、确认过的规律、他认过的拿主意规律。和交接前 ask.py 读的内容一样。"""
    rules = [r for r in A.read_jsonl(MIND / "rules.jsonl") if r.get("status") == "已确认"]
    parts = ["【Luke 的档案】\n" + (LUKE / "profile.md").read_text(),
             "【他确认过的规律】\n" + (LUKE / "confirmed.md").read_text()]
    if rules:
        parts.append("【他拿主意时的规律】（从他以前的回答和纠正里提炼，他确认过；情境对得上才用）\n" +
                     "\n".join(f"- {A.clean_ids(r['rule'])}" + (f"（不适用：{A.clean_ids(r['when_not'])}）" if r.get("when_not") else "")
                               for r in rules))
    return "\n\n".join(parts) + "\n"


README = """# 交给 Lukee 的 Luke 个人画像（{day} 导出）

Luke 2026-10-28 定：个人记录交给 Lukee 记，lukeeMind 只按原则和源知识判断。这一包是 lukeeMind 交接时手里的全部个人记录。

## 问 lukeeMind 时交进去的两份

| 文件 | 是什么 | 怎么用 |
|---|---|---|
| `profile.md` | 档案、确认过的规律、他认过的拿主意规律 | `ask.py ask --profile-file <这份>`。以后 Lukee 改自己那份，交最新的 |
| `choices.jsonl` | Luke 以前的选择，{n} 道，一行一道 | `ask.py ask --choices-file <这份>`。lukeeMind 从里面挑最像的 4 道当例子 |

`choices.jsonl` 每行的字段：`id`、`ts`（时间，ISO 格式）、`text`（题目和选项，已排好）或者 `question` 加 `options`（{{"A": "…"}}）、`choice`（他选的字母）、`note`（他字母之外补的原话，没有就空）、`client`（涉及哪个客户，没有就空）。Lukee 以后记新的选择，按 `question` 加 `options` 的写法往后追加就行。

带客户的选择，lukeeMind 只在 `--client` 是同一个客户时才拿来当例子。

## 原样交出的其他记录（`raw/`）

| 文件 | 是什么 |
|---|---|
| `hypotheses.md` | 关于 Luke 的假设表（没验证的，不当事实用） |
| `interview-guide.md` | 访谈提纲 |
| `cards.jsonl` | 案例卡：从他的回答和纠正里抽的 |
| `rules.jsonl` | 从案例卡提炼的规律，`status` 是"已确认"的才是他认过的 |
| `asks.jsonl` | 别的 agent 问过 lukeeMind 的题、lukeeMind 的回答和 Luke 的回填 |

放权级别：交接时所有类别都是 0 级（lukeeMind 这边没有 levels.json）。以后由 Lukee 记，问的时候用 `--level` 告诉 lukeeMind 这一类现在几级；钱、合同、对外发送这些清单里的类别永远是 0 级。

## 规矩

- 这一包只在这台 Mac Studio 的 `private/` 里，不进任何公开仓库，不交给 Jev 或别的外部接口
- 交给 Opus 之前，客户公司名和带敬称的人名要先去掉
"""


def cmd_export(a):
    day = dt.date.today().strftime("%Y%m%d")
    out = Path(a.out) if a.out else E.PRIVATE / "handoff" / f"lukee-{day}"
    (out / "raw").mkdir(parents=True, exist_ok=True)
    (out / "profile.md").write_text(profile_text())
    choices = past_choices()
    A.write_jsonl(out / "choices.jsonl", choices)
    for src in (LUKE / "hypotheses.md", LUKE / "interview-guide.md", MIND / "cards.jsonl", MIND / "rules.jsonl", MIND / "asks.jsonl"):
        if src.exists():
            shutil.copy2(src, out / "raw" / src.name)
    (out / "README.md").write_text(README.format(day=day, n=len(choices)))
    print(json.dumps({"out": str(out), "choices": len(choices), "profile_chars": len((out / "profile.md").read_text())},
                     ensure_ascii=False))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("export")
    p.add_argument("--out", default="")
    a = ap.parse_args()
    {"export": cmd_export}[a.cmd](a)


if __name__ == "__main__":
    main()
