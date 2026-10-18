---
title: "Anthropic：用技能代替独立智能体"
author: "ginobefun (@hongming731)"
url: https://x.com/hongming731/status/1999344809354625161
source: X
published: 2025-12-12 05:05 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [zhang-2025-dont-build-agents-build-skills, feigenbaum-1977-knowledge-engineering, procedural-knowledge, progressive-disclosure, seci-model-of-knowledge-dimensions, modular-programming]
---

## 原文

Anthropic 公司两位 Agent Skills 创建者在 @aiDotEngineer 上的分享非常值得一看，他们提出的智能体开发新范式：不再构建复杂的独立智能体，而是创建可组合的技能。

演讲阐述了当前智能体的核心问题：虽有智力却缺乏领域专业知识，就像高智商数学家去报税，能力强但经验不足。技能本质上就是打包了过程性知识的文件夹，设计极简却强大：支持版本控制、团队共享、渐进式披露，可与 MCP 服务器无缝集成。

文章展示了正在形成的通用智能体架构：模型+运行时环境+技能库+MCP，这种模块化设计让智能体能够按需获取专业知识。最激动人心的是愿景：构建一个组织内外共同演进的知识库，让智能体通过技能持续学习和改进。

> 媒体：
> - https://pbs.twimg.com/media/G78ZA8-agAMAz3e.jpg

## 溯源

- 核心主张：智能体不缺智力，缺的是领域经验；与其为每个领域构建复杂的独立智能体，不如把过程性知识打包成可版本管理、可共享、渐进式披露的技能文件夹，形成“模型 + 运行时 + 技能库 + MCP”的通用架构，让组织的知识持续积累、智能体持续变好。
- 源知识：
  - [别再造智能体，去造技能（AI Engineer 演讲）](../roots/zhang-2025-dont-build-agents-build-skills.md) · 关系：直接源自 · 强弱：强。原文就是在介绍 Anthropic 两位 Agent Skills 创建者在 AI Engineer 大会上的演讲，数学家报税的比喻、技能是文件夹、模型加运行时加 MCP 加技能库的架构都出自这场演讲。
  - [知识原则：智能体的本事主要来自专门知识](../roots/feigenbaum-1977-knowledge-engineering.md) · 关系：换了说法 · 强弱：强。“虽有智力却缺乏领域专业知识”和 Feigenbaum 1977 年的知识原则几乎同义：解决问题的本事主要来自专门知识，和推理方法多通用多强只有次要关系，“智能体必须知识丰富，哪怕方法简单”；演讲没有引用他。
  - [过程性知识（知道怎么做）](../roots/procedural-knowledge.md) · 关系：直接源自 · 强弱：强。原文明说“技能本质上就是打包了过程性知识的文件夹”；Anthropic 的技能文章也写“真正的工作需要过程性知识和组织背景”。
  - [渐进式披露](../roots/progressive-disclosure.md) · 关系：直接源自 · 强弱：强。原文明说技能支持“渐进式披露”。
  - [SECI 知识转化模型](../roots/seci-model-of-knowledge-dimensions.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“构建一个组织内外共同演进的知识库”，把团队做事的经验写成可共享的技能，是 SECI 模型里把默会知识外化、再组合扩散的过程。
  - [模块化编程](../roots/modular-programming.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“不再构建复杂的独立智能体，而是创建可组合的技能”“模块化设计”：一个通用内核，加上可插拔、可单独维护的模块。
- 本质：这条新知识本质上是专家系统时代“本事来自知识而不是推理方法”的知识原则，在大模型通用智能体用可加载的技能文件补足领域专长场景下的应用。
- 整理于：2026-10-18（第 2 轮）
