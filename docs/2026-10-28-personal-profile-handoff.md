# 个人画像交接方案（草稿，等 Luke 定）

> 2026-10-28 · 状态：草稿，Luke 认了才搬
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
