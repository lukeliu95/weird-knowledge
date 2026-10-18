---
title: "Agent 智能体是模型能力的放大器"
author: "WaytoAGI｜通往AGI之路 (@WaytoAGI)"
url: https://x.com/WaytoAGI/status/1750759723429953948
source: X
published: 2024-01-26 05:57 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [davidson-2023-ai-capabilities-without-retraining, intelligence-amplification, law-of-amplification, karpathy-2023-state-of-gpt, reinforcement-learning-from-human-feedback]
---

## 原文

《Agent智能体：模型能力的放大器》分享自Agently创始人莫欣，讨论了大型语言模型及其在创建AI代理中的应用。它概述了利用大量数据训练、特殊对齐和优化来构建这些模型的过程，以更好地满足人类需求。

https://t.co/yNvbvbbjkr https://t.co/3gZxxrEVtH

> 媒体：
> - https://pbs.twimg.com/media/GEvyjH9bcAASS26.jpg

## 溯源

- 核心主张：Agent 是模型能力的放大器：先靠海量数据训练、对齐和优化做出大模型，再在模型之上搭 agent，把模型的能力放大出来去满足人的需求。
- 源知识：
  - [不重新训练也能大幅提升 AI 能力（训练后增强）](../roots/davidson-2023-ai-capabilities-without-retraining.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。Epoch 等的研究把工具调用、提示方法、脚手架等训练后增强折算成等效训练算力，部分方法相当于多用 5～20 倍算力，为“agent 放大模型能力”提供了量化证据；原分享没有引用，且分享正文没能查到，只依据标题和摘要判断。
  - [智力放大](../roots/intelligence-amplification.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“放大器”的说法沿用了 Ashby 1956 年“放大智力”的思路：工具不取代智力而是放大它；这里被放大的对象从人换成了模型。
  - [技术放大定律](../roots/law-of-amplification.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。技术放大定律说技术只放大已有的能力；“agent 是模型能力的放大器”含有同样的意思：底座模型不行，agent 也放大不出来。这是推断。
  - [State of GPT 演讲](../roots/karpathy-2023-state-of-gpt.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。摘要里“海量数据训练、特殊对齐和优化”的造模型流程，和 Karpathy 讲的预训练、监督微调、奖励模型、强化学习四步一致。
  - [基于人类反馈的强化学习（RLHF）](../roots/reinforcement-learning-from-human-feedback.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“特殊对齐，以更好地满足人类需求”指的就是 RLHF 一类方法。
- 本质：这条新知识本质上是“智力放大”思想在大模型应用场景下的应用：模型提供底层智力，agent 用工具、流程和记忆把它放大成能完成任务的能力。
- 整理于：2026-10-18（第 2 轮）
