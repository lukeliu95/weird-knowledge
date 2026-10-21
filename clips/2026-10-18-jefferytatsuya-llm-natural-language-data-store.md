---
title: "用自然语言让 LLM 承担业务数据存储"
author: "Jeffery Kaneda　金田達也 (@JefferyTatsuya)"
url: https://x.com/JefferyTatsuya/status/1823188750169710838
source: X
published: 2024-08-13 02:44 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: AI 产品与创业
roots: [create-read-update-and-delete, natural-language-user-interface, business-rules-engine, codd-1970-relational-model, dijkstra-1979-natural-language-programming]
---

## 原文

这会是一个重大的变革。

现在各种SaaS软件，其核心就是多个表格的增删改查而已。

https://t.co/xAddzsxUtf通过自然语言，无需理解下层的数据操作，LLM来承担任意业务的数据存储。人的工作是把业务的逻辑写成规则，给到agent来处理数据就好。

传统的SaaS，以及以上的No code，得抓紧拥抱这个技术。

## 溯源

- 核心主张：SaaS 的核心就是多张表的增删改查，未来用户用自然语言、不必懂底层数据操作，由大模型 agent 按人写好的业务规则处理数据，传统 SaaS 和无代码工具会被冲击。
- 源知识：
  - [增删改查（CRUD）](../roots/create-read-update-and-delete.md) · 关系：直接源自 · 强弱：强。作者明说 SaaS 的核心是“增删改查”，就是在用 CRUD 这个概念
  - [自然语言界面（自然语言数据库接口）](../roots/natural-language-user-interface.md) · 关系：换了说法 · 强弱：强。“用自然语言、无需理解下层数据操作就能管数据”和 1960、70 年代起的自然语言数据库接口目标几乎一字不差，只是换成了大模型来实现
  - [业务规则引擎](../roots/business-rules-engine.md) · 关系：相近 · 强弱：弱（模型复核通过）。“人把业务逻辑写成规则，交给 agent 去处理数据”和业务规则引擎把规则从代码里分离、由引擎执行的做法很像
  - [大型共享数据库的关系模型](../roots/codd-1970-relational-model.md) · 关系：相近 · 强弱：弱（模型复核通过）。Codd 论文第一句就说用户不该被迫知道数据在机器里怎么组织，和“无需理解下层的数据操作”同理
  - [论“自然语言编程”之愚蠢](../roots/dijkstra-1979-natural-language-programming.md) · 关系：挑战 · 强弱：弱（模型复核通过）。Dijkstra 认为用自然语言给机器下指令反而更难、更容易出错，和“用自然语言替代数据操作”的乐观判断相反
- 本质：这条新知识本质上是自然语言数据库接口（不懂底层也能增删改查）加业务规则引擎（人写规则、引擎执行）在大模型 agent 场景下的重新表述。
- 整理于：2026-10-18（第 2 轮）
