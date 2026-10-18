---
title: "EvoOntology 让智能体查数更准"
author: "Ren (@Ryrenz)"
url: https://x.com/Ryrenz/status/2111104895164043364
source: X
published: 2026-10-16 14:40 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: Agent 与 Skill
roots: []
---

## 原文

🧬 人大刚开源了 EvoOntology，装进 Claude Code 或 Codex，Agent 查数据会越用越准。

论文拿下了 Hugging Face Daily Papers 当日第一。

用 AI 查过公司数据的人都踩过这个坑：问一句“上季度复购率多少”，Agent 先把表结构翻一遍，再猜 uid 和 user_id 哪个才对，“复购”怎么算也靠猜。猜错了，算出来的数还挺像那么回事。

常见的补救是写一份数据字典塞进 prompt。论文专门测了这招：同样的语义信息整段塞进上下文，Claude-Sonnet-5 的得分不升反降，掉了 15 分。

EvoOntology 的做法是让 Agent 自己维护这本说明书：

1️⃣ 先从你要问的问题出发，把指标定义、表之间的关系、业务约束整理成一层本体，每一条都拿真实数据验证过才入库
2️⃣ 用的时候通过 MCP 按需查，这一步需要哪个概念就取哪个，不往上下文里硬塞
3️⃣ 每次跑完任务，它会看 Agent 在哪一步出了错，只改出问题的那一小块。新版本要在同样的模型、同样的数据上跑赢旧版才会上线，跑不赢就继续用旧版

同一个 Claude-Sonnet-5 换成这种用法，得分涨了 8.8 分，和整段塞 prompt 一来一回差了将近 24 分。GPT-5.5 在 DDR-Bench 上更夸张，涨了 26.7 分。

Claude Code 和 Codex 都有现成插件，不用 clone 仓库，也不用另配 Python 环境。

模型权重一个没动，变强的是 Agent 手里那本数据说明书。

GitHub：https://t.co/cv161pt0Cl
论文：https://t.co/nB6GRVHsEo

## 溯源

