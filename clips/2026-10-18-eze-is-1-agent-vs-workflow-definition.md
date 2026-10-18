---
title: "多数 Agent 其实只是工作流"
author: "一泽Eze (@eze_is_1)"
url: https://x.com/eze_is_1/status/1982740850070425826
source: X
published: 2025-10-27 09:27 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind: 观点
topic: Agent 与 Skill
roots: []
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

