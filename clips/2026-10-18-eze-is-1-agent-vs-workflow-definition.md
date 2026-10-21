---
title: "多数 Agent 其实只是工作流"
author: "一泽Eze (@eze_is_1)"
url: https://x.com/eze_is_1/status/1982740850070425826
source: X
published: 2025-10-27 09:27 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [anthropic-2024-building-effective-agents, occams-razor, galls-law, observability-software, intelligent-agent]
---

## 原文

大家经常聊的 Agent，很多时候其实只是一个 Workflow。这两个概念混用，会导致产品设计和技术选型上走很多弯路。

Anthropic 给了一个很清晰的划分，核心区别在于：
系统执行任务时，是由代码预设路径（Code-Driven），还是由LLM自己动态决定下一步（LLM-Driven）。前者是 Workflow，后者才是 Agent，官方表述是这样的：
 - 工作流 Workflow：把 LLMs 和工具通过代码，预编排好执行路径的规则流程。
 - AI 代理 Agent：由 LLMs 自主指导其执行过程和工具使用的自主系统。
两者没有优劣，Anthropic 将其统称为 agentic systems，智能系统。

Anthropic 分享了他们与数十个团队、客户合作构建智能体后，总结下来的实用建议：
1.优先解决问题：
以解决问题为目标出发，没有硬性规定和优劣，可以选用多种类型进行组合。

2.最小化设计原则：
先从简单提示与优秀模型开始，实验并构筑第一个版本的「Agent」。只有智能不足时，才考虑调优工程，添加更多步骤与 Context 指引。如无必要，无增实体。

3.保持 Agent 的可解释性：
不可解释的 Agent 无法维护，无法维护就无法针对生产环境的各类问题进行工程调优。所以，Agent 的每一步规划步骤都应该保持透明。

## 溯源

- 核心主张：由代码预设执行路径的是工作流，由模型自己决定下一步的才是 Agent；搭建时应从最简单的方案起步、确有必要才加复杂度，并让每一步规划保持透明。
- 源知识：
  - [构建高效的智能体](../roots/anthropic-2024-building-effective-agents.md) · 关系：直接源自 · 强弱：强。作者明说引用 Anthropic 的划分，工作流和 Agent 的定义、三条建议都与原文一致。
  - [奥卡姆剃刀](../roots/occams-razor.md) · 关系：直接源自 · 强弱：强。作者原文写了「如无必要，无增实体」，就是奥卡姆剃刀的流行表述。
  - [加尔定律](../roots/galls-law.md) · 关系：相近 · 强弱：弱（模型复核通过）。「先用简单提示做出第一版，智能不足时再加步骤」与加尔定律「从能运转的简单系统演化」一致。
  - [可观测性（软件）](../roots/observability-software.md) · 关系：相近 · 强弱：弱（模型复核通过）。「不可解释就无法维护、无法针对生产问题调优」，与软件可观测性「能从外部看清内部状态才能排障」是同一个道理。
  - [智能体](../roots/intelligent-agent.md) · 关系：相近 · 强弱：弱（模型复核通过）。经典 AI 教科书的 agent 定义更宽（恒温器也算），Anthropic 用「谁决定下一步」即自主程度来划线，口径更窄，是在经典定义里切出一类。
- 本质：这条新知识本质上是奥卡姆剃刀（简约原则）和可观测性原则在大模型系统架构选型上的应用。
- 整理于：2026-10-18（第 1 轮）
