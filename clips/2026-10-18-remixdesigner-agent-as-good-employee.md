---
title: "自然语言 Agent 应像好员工的七点"
author: "Jimmy Cheung (@remixdesigner)"
url: https://x.com/remixdesigner/status/1886804029570998695
source: X
published: 2025-02-04 15:48 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [test-driven-development, horvitz-1999-mixed-initiative-user-interfaces, principal-agent-problem, gulf-of-execution, seci-model-of-knowledge-dimensions]
---

## 原文

一点点浅陋想法（可能你们早有更细节的想法或已实现）：

自然语言 Agent 从理念上更像是一个员工，老板表达需求，员工前去执行（完成代理任务）。

而老板喜欢的员工有哪些特点？
1. 在收到命令之前，会理解后用通过执行计划复述老板的意图，让老板知晓任务已清晰传递！
2. 知道老板喜欢放心的员工，但也喜欢关注整体流程和关键节点是否按预期执行，所以在任务执行过程中会通过合适的呈现方式展示整体脉络和当前进展。
3. 在向老板 Showcase 前会先完成自测和确认，所以会通过类似 Test-Driven 的理念开展工作，在设计任务的同时设计每个单元的测试方案和验收标准。
4. 不厌烦过程中的反复调整，并始终保留全部记录，防止回到某个节点重头开始。
5. 对于不合理的要求敢于说不，从而通过沟通更深入理解需求背后的意图或获得更合理的需求。
6. 形成 SOP 之后，可以轻松移植或赋能到其他任务，完成传帮带。
7. 即使有能力，也擅于互相借助同事的领域资源，不重复造轮子。
...

## 溯源

- 核心主张：自然语言 agent 应该像老板放心的好员工：动手前先用计划复述意图，过程中展示进度，交付前先自测并定好验收标准，保留全部记录，敢对不合理要求说不，把做法沉淀成可复用的 SOP，善用现成资源不重复造轮子。
- 源知识：
  - [测试驱动开发](../roots/test-driven-development.md) · 关系：直接源自 · 强弱：强。作者明说要“通过类似 Test-Driven 的理念开展工作”，设计任务时同时设计每个单元的测试方案和验收标准。
  - [混合主导用户界面的原则](../roots/horvitz-1999-mixed-initiative-user-interfaces.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。Horvitz 的混合主导界面原则里有“考虑对用户目标的不确定”“用对话消除关键不确定”“支持人机协作修正结果”“像善意助手那样合乎社交期待”“记住近期交互”，和第 1、2、4 点高度对应；作者没有引用。
  - [委托-代理问题](../roots/principal-agent-problem.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。把 agent 当员工、老板提需求员工执行，就是委托—代理关系；复述意图、展示进度、保留记录，都是在减少委托人和代理人之间的信息不对称。
  - [执行鸿沟与评估鸿沟](../roots/gulf-of-execution.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“用合适的方式展示整体脉络和当前进展”，是在缩小诺曼说的评估鸿沟，让人看得懂系统现在处在什么状态。
  - [SECI 知识转化模型](../roots/seci-model-of-knowledge-dimensions.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“形成 SOP 后移植到其他任务、传帮带”，是把做事经验从默会知识外化成显性知识再传给别人，对应 SECI 里的外化和组合。
- 本质：这条新知识本质上是混合主导界面原则（agent 先消除对用户意图的不确定、让人看得见进度并随时纠正）加上测试驱动开发，在“把 agent 当员工来要求”场景下的应用。
- 整理于：2026-10-18（第 2 轮）
