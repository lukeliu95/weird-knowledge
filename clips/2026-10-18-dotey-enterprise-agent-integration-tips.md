---
title: "给公司业务接入智能体的五点思考"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/1974520194807591020
source: X
published: 2025-10-04 17:01 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [anthropic-2024-building-effective-agents, anthropic-2025-writing-effective-tools, anthropic-2025-effective-context-engineering, ronacher-2025-code-is-all-you-need, yan-2025-dont-build-multi-agents, koomen-2025-ai-horseless-carriages]
---

## 原文

如果你在为公司现有业务集成 AI Agent，或者迁移到 AI Agent，我自己的一点思考供参考：

1. 如果你流程的路径很确定并且效率很高，那么也许你只需要在原有流程上集成一些 AI 功能就可以，并不一定要变成 Agent

通常 Agent 没有固定流程，依赖于用户的输入来由 LLM 决策调用什么工具

2. 为 Agent 去重新设计新的工具而不是让 Agent 去用现有的工具

通常公司内部已经有一些成熟的工具，但这些工具是为人设计的而不是 Agent 设计的，当你去做 Agent，要重新为 Agent 做新的工具，什么工具是最适合 Agent 就去打造什么工具，但不是因为你有什么工具所以让 Agent 去用什么工具。

另外 Agent 的工具要融入上下文管理：
- 描述要清晰具体，让 LLM 知道什么场景该使用什么工具
- 输入参数要明确：即让 LLM 知道该传什么参数，又要让工具有足够的数据可以执行
- 输出结果要清晰明了，不要有太多无关上下文内容，因为工具输出的结果会加入 Agent 的上下文，有些很长的输出可以保存到外部文件按需读取

3. 不要为了 MCP 而用 MCP

MCP 很流行，但它的优势是让你的工具可以兼容不同的模型，不同的 AI 平台，如果你的工具只有你自己的 Agent 用，没必要做成 MCP，普通的命令行、脚本、API 都可以。你看 Claude Code 的十几个工具没有一个是 MCP。

4. 工具数量不要太多，基于功能可以适当拆分子智能体

由于工具的描述、输入和输出都占用上下文空间，所以工具数量不能太大，否则会影响 Agent 的能力。

如果你的工具实在太多，可以考虑按照功能拆分成子智能体，让一个子智能体负责某些特定功能的任务，它可以拥有自己的工具集，主 Agent 则负责调度这些子 Agent，为子 Agent 提供独立的上下文，并收集子 Agent 返回的结果。

如果子 Agent 或者工具的结果之间有依赖关系，不要并行执行任务，否则会搞乱上下文

5. 需要为 Agent 重新设计交互

你的软件也许已经有一套交互方式了，但当你去做 Agent 的时候，要重新思考什么是最佳交互方式。

Agent 的交互和传统的软件交互是不一样的，通常以对话为主，用户可以通过对话框输入文本信息，上传文档、图片等作为上下文一部分，信息则更像聊天对话，实时可以看到 AI 返回文本、工具调用结果等。

还可以是有一个主要工作区，类似于传统的软件交互，侧边栏是 Agent 聊天对话。

在 Agent 交互方面，ChatGPT、Claude、Cursor、Notion、Gemini 等产品都有很多交互可以参考，多借鉴前沿主流的 Agent 交互方式

## 溯源

- 核心主张：给现有业务接 AI 时：流程确定且高效就只在原流程里加 AI 功能，不必做成 agent；要为 agent 重新设计工具（描述清楚、参数明确、输出精简，长输出存文件按需读）；工具只给自己的 agent 用就不必做成 MCP；工具不能太多，多了就按功能拆子 agent 并给独立上下文，有依赖的任务不要并行；交互方式也要为 agent 重新设计。
- 源知识：
  - [构建高效的智能体](../roots/anthropic-2024-building-effective-agents.md) · 关系：换了说法 · 强弱：强。第 1 点“Agent 没有固定流程，由 LLM 决策调用什么工具”几乎就是该文对智能体的定义（模型自己决定过程和工具使用，区别于走预设路径的工作流）；“流程确定就不必做成 Agent”对应它“先找最简单的方案，可能根本不需要 agent”；第 2 点对应它附录里的“智能体-计算机接口（ACI）”。
  - [为智能体写好用的工具（并借助智能体来写）](../roots/anthropic-2025-writing-effective-tools.md) · 关系：换了说法 · 强弱：强。第 2、4 点和该文几乎一致：常见错误是把现有软件功能或 API 原样包成工具；工具不是越多越好；描述要清楚、参数命名无歧义、只返回高信号信息。该文早约三周发表，作者没有引用。
  - [AI 智能体的上下文工程](../roots/anthropic-2025-effective-context-engineering.md) · 关系：相近 · 强弱：弱（模型复核通过）。“工具输出会进入上下文，长输出存到外部文件按需读取”“拆子 agent 并给独立上下文”，对应上下文工程里的即时检索、结构化笔记和子 agent 架构。
  - [Armin Ronacher：工具——代码就是你需要的一切](../roots/ronacher-2025-code-is-all-you-need.md) · 关系：相近 · 强弱：弱（模型复核通过）。第 3 点“工具只给自己的 Agent 用就没必要做 MCP，命令行、脚本、API 都可以”，和 Ronacher 主张让模型写脚本、少用 MCP 一致；作者没有引用。
  - [别做多智能体](../roots/yan-2025-dont-build-multi-agents.md) · 关系：相近 · 强弱：弱（模型复核通过）。“子 Agent 或工具的结果之间有依赖关系就不要并行，否则会搞乱上下文”，和 Cognition 的“行动里暗含决策，决策冲突就出坏结果”是同一个道理。
  - [AI 时代的「没有马的马车」](../roots/koomen-2025-ai-horseless-carriages.md) · 关系：相近 · 强弱：弱（模型复核通过）。第 5 点“要为 Agent 重新设计交互，不要沿用原有软件的交互方式”，和 Koomen 批评 AI 应用照搬旧软件做法（没有马的马车）一致。
- 本质：这条新知识本质上是“先用最简单的方案、为使用者重新设计接口、上下文是稀缺资源”这几条 agent 工程原则在企业业务改造中的应用。
- 整理于：2026-10-18（第 2 轮）
