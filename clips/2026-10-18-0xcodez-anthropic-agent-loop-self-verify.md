---
title: "Anthropic：让模型验证自己的输出"
author: "Codez (@0xCodez)"
url: https://x.com/0xCodez/status/2067604216529474028
source: X
published: 2026-06-18 13:43 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [cherny-2025-claude-code-best-practices, shihipar-2025-claude-agent-sdk, feedback]
---

## 原文

Anthropic research lead:

"99% of our engineers are running swarms of 300+ self-improving agents.

close the agent loop. Give the model a way to verify its own output"

in a 20-minute session, Anthropic team member explains how to build a model that improves itself.

Claude + loops + plan mode + dynamic workflows -that’s the secret.

Watch the talk, then save the playbook below.

> 媒体：
> - https://video.twimg.com/amplify_video/2067603908357193728/vid/avc1/480x270/VTgcUWTCcOO1OhR7.mp4?tag=28

## 溯源

- 核心主张：要让 agent 可靠地自己干活、越做越好，关键是把回路闭合：给模型一个能自己验证输出的办法（测试、构建、截图对比等），再配合循环、计划模式和动态工作流。（“99% 的工程师在跑 300 多个自我改进 agent”这句引语没有查到出处，待确认。）
- 源知识：
  - [Claude Code 最佳实践（给 Claude 一个验证自己工作的办法）](../roots/cherny-2025-claude-code-best-practices.md) · 关系：直接源自 · 强弱：强。“Give the model a way to verify its own output”和 Claude Code 官方最佳实践（现行版本）的标题“Give Claude a way to verify its work”几乎一字不差，文档还写“the loop closes on its own”，并在同一页讲了 plan mode、/goal 循环和 dynamic workflow，正好对上原文的“loops + plan mode + dynamic workflows”。
  - [用 Claude Agent SDK 构建智能体（收集上下文→行动→验证→重复）](../roots/shihipar-2025-claude-agent-sdk.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。Anthropic 的 Agent SDK 文章把 agent 循环定为“收集上下文→采取行动→验证工作→重复”，“close the agent loop”说的就是补上其中的验证这一步。演讲者没有点名这篇文章，是推断。
  - [反馈](../roots/feedback.md) · 关系：换了说法 · 强弱：强。“close the loop”是控制论里闭环反馈的原词：把输出测出来、和目标比较、再调整下一步。给模型一个验证手段，就是给这个回路装上传感器。
- 本质：这条新知识本质上是反馈控制（闭环）在 AI 编程 agent 场景下的应用：可运行的检查就是回路里的传感器。
- 整理于：2026-10-18（第 2 轮）
