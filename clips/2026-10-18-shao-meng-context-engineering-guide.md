---
title: "上下文工程：智能体的核心实践指南"
author: "meng shao (@shao__meng)"
url: https://x.com/shao__meng/status/1971011884125159800
source: X
published: 2025-09-25 00:40 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [martin-2025-context-engineering-agents, context-engineering, anthropic-2025-effective-context-engineering, shi-2023-irrelevant-context-distraction, packer-2023-memgpt-llm-os]
---

## 原文

上下文工程 (Context Engineering)：AI Agent 的核心实践指南 —— 感谢 @akshay_pachaar 如此直观的可视化讲解。理论 + 手绘图形化展示 + 实战建议，可能是我见过最佳展示方式了！

什么是上下文工程？
· 核心定义：上下文工程是管理 AI Agent 输入信息的艺术与科学，帮助 LLM 在正确时机获取“正确信息”。它超越传统提示工程，聚焦于优化上下文窗口，以减少噪声、提升效率。
· 为什么重要？：现代 AI Agent 面临海量数据挑战。良好的上下文工程能避免 LLM “迷失”在无关信息中，提高任务准确性和成本控制。

AI Agent 的6种上下文类型
总结 AI Agent 常见的上下文需求，按功能分类，便于开发者快速定位：

· 写作上下文（Writing Context）：生成新内容，如任务指令或响应。示例：为 Agent 编写脚本，帮助其规划多步行动。
· 阅读上下文（Reading Context）：从外部源拉取信息，如知识库或数据库。示例：查询用户历史记录以个性化响应。
· 压缩上下文（Compression Context）：精简冗余信息，减少 token 消耗。示例：去除重复数据，节省 LLM 计算成本。
· 隔离上下文（Isolation Context）：为子任务或 Multi Agents 协作划分独立空间。示例：让 Agent A 处理规划，Agent B 执行，避免干扰。
· 检索上下文（Retrieval Context）：从长时记忆中动态拉取相关片段。示例：基于查询从向量数据库中召回文档。
· 工具调用上下文（Tool Calling Context）：集成外部工具，如 API 调用。示例：Agent 调用天气 API 时，提供精确参数。

这些类型并非孤立，而是互连，形成 Agent 的“上下文管道”。

4个基本阶段：从输入到输出的闭环
上下文工程拆解为4阶段，强调可操作性：
· 写入阶段（Writing）：构建初始上下文，包括长时记忆（跨会话知识）和短时记忆（当前状态）。目标：为 Agent 提供清晰的任务框架。
· 阅读阶段（Reading）：将外部内容注入窗口，如从数据库或工具中读取。示例：拉取用户偏好块，确保 Agent “读懂”需求。
· 压缩阶段（Compression）：优化输入，移除多余或重复部分。示例：用 LLM 摘要生成“精简版”上下文，降低 token 使用率（线程提及这可显著节省成本）。
· 隔离阶段（Isolation）：分割上下文，支持 Multi Agents 协作或子任务。示例：为每个 Agent 分配独立“泡泡”，便于并行处理。

这些阶段形成循环：写入→阅读→压缩→隔离→输出反馈。

> 媒体：
> - https://pbs.twimg.com/media/G1pwcT2asAAbNv1.jpg
> - https://pbs.twimg.com/media/G1pws3yaAAUmzHs.jpg
> - https://pbs.twimg.com/media/G1pwv1eaYAAA4mL.jpg

## 溯源

- 核心主张：上下文工程是管理 agent 输入信息的方法：通过写入、读取（选取）、压缩、隔离四类手段，让模型在每一步只拿到正确且必要的信息，从而减少噪声、提高准确率、控制成本。
- 源知识：
  - [智能体的上下文工程（写入、选取、压缩、隔离）](../roots/martin-2025-context-engineering-agents.md) · 关系：直接源自 · 强弱：强。文中“写入、阅读、压缩、隔离”四个阶段，与 Lance Martin（LangChain）提出的 write、select、compress、isolate 四类策略一一对应，连示例（草稿本、长短期记忆、给每个子 agent 独立上下文）都一样；原帖只致谢了画图的 Akshay Pachaar。
  - [上下文工程](../roots/context-engineering.md) · 关系：直接源自 · 强弱：强。“管理输入信息的艺术与科学，帮助模型在正确时机获取正确信息”，几乎就是 Karpathy 那句“用恰好正确的信息填满上下文窗口的精细艺术与科学”。
  - [AI 智能体的上下文工程](../roots/anthropic-2025-effective-context-engineering.md) · 关系：相近 · 强弱：弱（模型复核通过）。Anthropic 把上下文当有限的注意力预算，靠压缩、结构化笔记和子 agent 保持上下文干净，思路相同；它比原帖晚 4 天发布，不是原帖的来源。
  - [大模型很容易被无关上下文带偏](../roots/shi-2023-irrelevant-context-distraction.md) · 关系：相近 · 强弱：弱（模型复核通过）。“避免模型迷失在无关信息中、提高准确性”有实验依据：题目里掺入无关信息后，模型准确率会大幅下降。
  - [MemGPT：让大模型像操作系统一样管理内存](../roots/packer-2023-memgpt-llm-os.md) · 关系：相近 · 强弱：弱（模型复核通过）。把上下文分成长时记忆和短时记忆、按需读入和压缩，与 MemGPT 把上下文窗口当内存、外部存储当硬盘来换入换出的做法相近。
- 本质：这条新知识本质上是“容量有限的工作记忆要精挑细选放什么”（提高信噪比、分层存储）在大模型 agent 上下文窗口管理场景下的应用。
- 整理于：2026-10-18（第 2 轮）
