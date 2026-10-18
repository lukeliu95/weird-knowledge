---
title: "谈用 Claude 做智能体：少搭脚手架"
author: "Alex Albert (@alexalbert__)"
url: https://x.com/alexalbert__/status/1973804629273293041
source: X
published: 2025-10-02 17:37 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [bitter-lesson, anthropic-2024-building-effective-agents, anthropic-2025-effective-context-engineering, shihipar-2025-claude-agent-sdk]
---

## 原文

Had a great conversation with @brada and @katelyn_lesse about what we're seeing as devs build agents with Claude. We covered:
- How reducing scaffolding improves performance 
- The evolution of agentic frameworks 
- Building on the Claude Agent SDK
- Best practices for managing context
- And more!

> 媒体：
> - https://video.twimg.com/amplify_video/1973801617607798784/vid/avc1/480x270/GjmAUKMG9eR1zU-E.mp4?tag=21

## 溯源

- 核心主张：用 Claude 做 agent 时，少搭人工写死的脚手架反而效果更好；更好的做法是在通用的 agent 底座（Claude Agent SDK）上开发，把精力放在管好上下文上。（原文只是对谈提纲，具体论证在视频里。）
- 源知识：
  - [苦涩的教训](../roots/bitter-lesson.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“减少脚手架能提升效果”和苦涩的教训一致：长期看，依靠模型通用能力的方法会胜过把人的流程和知识写死进系统的方法。对谈提纲没有提到 Sutton，是推断。
  - [构建高效的智能体](../roots/anthropic-2024-building-effective-agents.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。Anthropic 2024 年这篇文章主张从最简单的方案起步，并提醒框架会多加一层抽象、遮住底层提示，建议先直接调用模型接口；和“少搭脚手架”“agent 框架的演变”意思相近。提纲没有点名这篇文章。
  - [AI 智能体的上下文工程](../roots/anthropic-2025-effective-context-engineering.md) · 关系：直接源自 · 强弱：弱（待 Luke 确认）。“managing context 的最佳实践”正是 Anthropic 在这次对谈三天前（2025-09-29）发表的上下文工程文章的主题，文中也说模型越强越该放手让它自主行动；同一家公司的人在讲同一套做法。提纲没有直接链接这篇文章，所以标弱。
  - [用 Claude Agent SDK 构建智能体（收集上下文→行动→验证→重复）](../roots/shihipar-2025-claude-agent-sdk.md) · 关系：直接源自 · 强弱：强。原文明确列出“Building on the Claude Agent SDK”；Anthropic 在 2025-09-29 发布《Building agents with the Claude Agent SDK》，核心是给 agent 一台电脑、按“收集上下文→行动→验证”循环工作，并用子 agent 和压缩管理上下文。
- 本质：这条新知识本质上是苦涩的教训（通用方法胜过手工写死的知识）在 agent 工程框架设计场景下的应用。
- 整理于：2026-10-18（第 2 轮）
