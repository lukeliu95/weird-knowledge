# 个人画像交接方案

> 2026-10-28 · 状态：Luke 选了 A，lukeeMind 这边已做完；Codex 那边等 Luke 把第六节的文字贴给 Lukee
> 起因：Luke 说"删除 lukeeMind 关于 Salesroom 相关读取业务。保持 lukeeMind 是学习互联网及学科类的基础知识与重要定义的第一性原理，递弱代偿原理的判断思考者。相关个性的内容交给前置的使用 lukeeMind 的 agent 去记录"，选了 A：先删 Salesroom、写新定位、补两个源知识；个人画像先留着不扩充，另写这份交接方案。
> 新定位写在 [AGENTS.md「定位」](../AGENTS.md)。仓库是公开的，这里只列类别和路径，不写画像内容。

## 一、分界线

| 归 lukeeMind（知识） | 归前面的 agent（个人） |
|---|---|
| 新知识、源知识、思考框架、补课 | Luke 的口味、习惯、说话方式 |
| Luke 确认过的原则（它们是从知识里长出来的判断尺子） | Luke 做过的具体选择、纠正、补的话 |
| 第一性原理、递弱代偿这类判断方法 | 客户、会议、同事、项目现场 |
| 探索：上网找值得学的东西 | 放权级别（哪类事可以不问 Luke） |

一句话：lukeeMind 回答"按道理该怎么判断"，前面的 agent 回答"Luke 这个人多半会怎么选"。

## 二、已经做了的（2026-10-28）

| 项 | 做法 |
|---|---|
| Salesroom 脚本、会议数据（47MB）、「客户真实声音」「Luke 在会上怎么判断」 | 挪进废纸篓 `~/.Trash/weird-knowledge-salesroom-20261028/`，Luke 自己清空 |
| `.env` 里的 Salesroom 密钥 | 删掉（主目录和 worktree 两份） |
| 确认过的规律里"会上 7 条判断方式"那一行 | 删掉 |
| `ask.py profile --work` | 去掉 |
| 去名用的客户名单 | 留一份在 `private/mind/scrub-names.json`，只用来在交给外部模型前去掉客户名 |
| 抽选择和纠正（`l3_extract.py`、`l3_corrections.py`）、每周提炼（`distill.py weekly`）、补数据题（`ask.py quiz`） | 暂停，规则里写明了 |

还留着、要说清楚的：`private/` 本地 git 的历史里还有「客户真实声音」「会上判断」的旧版本（会议原文从来没提交过）。要彻底清掉得改写那个本地仓库的历史，Luke 说要再做。

## 三、个人画像现在在哪

| 东西 | 路径（都在 `private/`） | 现在谁在用 |
|---|---|---|
| 档案、确认过的规律、假设表、访谈提纲 | `luke/profile.md`、`luke/confirmed.md`、`luke/hypotheses.md`、`luke/interview-guide.md` | `ask.py` 回答时读 |
| 口味 skill 和点赞预测 | `luke/taste-skill.md`、`l1/` | 探索打分、`ask.py taste` |
| 决定预测的题和成绩 | `l3/` | `ask.py` 找相似旧选择、回测 |
| 别的 agent 问过的题和回填、放权级别 | `mind/asks.jsonl`、`mind/levels.json` | `ask.py` |
| 案例卡和 Luke 认过的规律 | `mind/cards.jsonl`、`mind/rules.jsonl` | `ask.py` 回答时读已认的 |
| 兴趣地图 | `explore/interests.md` | 探索选方向 |

## 四、怎么交（三个选项）

**A（推荐）：个人记录交给 Lukee，口味留在 lukeeMind**

- Codex 里的 Lukee 自己记 Luke 的选择、纠正、补的话和放权级别。lukeeMind 的 `ask.py ask` 加一个 `--profile-file` 口子：Lukee 把它记的画像交进来，lukeeMind 按原则和源知识判断，再参考这份画像
- lukeeMind 这边的档案、确认过的规律、旧选择、案例卡、放权级别，整理成一份交给 Lukee，之后 lukeeMind 不再读自己那份
- 口味 skill、点赞预测、兴趣地图留在 lukeeMind：它们决定 lukeeMind 上网去学什么，属于"学知识"这一边
- 好处：分得干净，Lukee 离 Luke 最近，记得最准；探索不受影响
- 代价：要改 Codex 那边的 Lukee（Luke 同意了才动），回测要重做一遍

**B：全部交出去，包括口味**

- 口味和兴趣地图也给 Lukee，探索时由 Lukee 告诉 lukeeMind 该找什么方向
- 好处：lukeeMind 里完全没有个人数据
- 代价：探索每轮都要先问 Lukee，慢；点赞预测的测试集和冠军要搬家，成本高

**C：不搬，一直冻结**

- 现有画像一直留在 lukeeMind 只读，不扩充；新的个人记录由 Lukee 记在它那边
- 好处：什么都不用改
- 代价：画像会越来越旧，两边各有一半，以后更难理清

## 五、要 Luke 定的

1. 选 A、B 还是 C
2. `private/` 本地 git 历史里 Salesroom 汇总的旧版本，要不要改写历史彻底清掉
3. 选 A 或 B 的话，Codex 那边的 Lukee 由谁改：这边写好接入说明给 Codex，还是 Luke 自己交代

## 六、Luke 选了 A（2026-10-28）

Luke 的原话："A：个人记录交给 Lukee，口味留在 lukeeMind"。

### lukeeMind 这边做了什么

| 项 | 做法 |
|---|---|
| 交接包 | `tools/mind/handoff.py export` 导出到 `private/handoff/lukee-20261028/`：`profile.md`（档案、确认过的规律、他认过的拿主意规律）、`choices.jsonl`（179 道旧选择）、`raw/`（假设表、访谈提纲、案例卡、规律、问答记录原样），`README.md` 写了格式和规矩。已提交到 `private/` 的本地 git |
| `ask.py ask` | 不再读 `private/luke/profile.md`、`confirmed.md`、`private/mind/rules.jsonl` 和旧选择。改读提问方交进来的 `--profile-file`、`--choices-file`；放权级别用 `--level` 交进来，清单里的类别不管交几级都按 0 级 |
| 没交画像时 | 只按原则（带背后的道理）和口味 skill 判断，回答里 `profile_given` 是 false |
| 放权级别 | lukeeMind 这边不再存。`ask.py report` 只报哪一类够门槛，级别由 Lukee 记、Luke 定 |
| `ask.py record` | 照旧：lukeeMind 要靠回填算自己答得准不准。Luke 的选择以 Lukee 那份为准 |
| 原来的文件 | `private/luke/`、`private/mind/` 里的原件没删，`ask.py` 不再读。口味 skill、点赞预测、兴趣地图照常用 |
| 回测用的题 | `private/l3/decisions.jsonl` 留着当考题，只用来打分，不当回答的依据 |

### 回测

回测前定的标准：交接包交进来的两遍平均猜对数，和交接前原写法差 1 题以内算持平，才算交接没丢东西。

同样 140 道旧选择题（每题只用比它早的旧选择当例子）：

| 写法 | 第 1 遍 | 第 2 遍 | 他没按推荐选的 9 题 | 高确定的猜中 |
|---|---|---|---|---|
| 交接前：lukeeMind 读自己那份（10-28 上午） | 117 | 119 | 2/9、2/9 | 41/42、38/40 |
| 交接后：Lukee 交进来画像和旧选择 | 118 | 116 | 1/9、1/9 | 40/43、41/43 |
| 交接后：什么都不交（只有原则和口味 skill） | 113 | — | 1/9 | 32/34 |

- 交进来的画像和交接前内容一字不差，只是几段的先后顺序变了。平均 117 对 118，差 1 题，算持平，过了
- 什么都不交少对约 5 题。所以 Lukee 每次问都要交画像和旧选择，粘贴文字里写明了
- 他没按推荐选的 9 题，两边都只猜中 1～2 题，差别在误差里。这正是"猜 Luke"最难的地方，交给离他最近的 Lukee 记更多原话，才可能变好

### 可以直接粘贴给 Codex 的 Lukee 的文字

> 从现在起，我的个人记录由你来记，lukeeMind 只负责按原则和道理判断。
> 1. 先读 `/Users/lukeliu/claude/duzhe/private/handoff/lukee-20261028/README.md`，把同一目录里的 `profile.md` 和 `choices.jsonl` 复制到你自己的数据目录，以后由你维护。这些是我的私人资料，不进任何公开仓库，不交给除 lukeeMind 以外的外部服务。
> 2. 要替我拿主意时，这样问 lukeeMind：`python3 /Users/lukeliu/claude/duzhe/tools/mind/ask.py ask --from codex-lukee --question "…" --options "A:…|B:…" --context-file <背景文件> --profile-file <你那份 profile.md> --choices-file <你那份 choices.jsonl> --level <这一类现在几级>`。背景里写清谁问的、前面聊了什么、有什么约束，不放密钥和账号。放权级别由你记，现在全部是 0 级，升不升只听我的。
> 3. 拿到结果后照旧问我，把它的建议和依据一起给我看。我回答后做两件事：调 `ask.py record <id> --luke <我选的> --note "<我的原话>"` 回填；再按 README 里的格式，把这道题（question、options、我选的字母、我补的原话、涉及的客户）追加到你的 `choices.jsonl`。
> 4. 我纠正你、或者亲口说出新的习惯和偏好时，记进你那份 `profile.md` 的「他确认过的规律」，写上日期。你自己推断、我没确认的，不要写进去。
> 5. lukeeMind 的建议不是我的决定，不要对同事和客户说成是我定的。

（第九节旧的粘贴文字里命令少了 `ask` 这个词，照它调会报错，以这一段为准。）
