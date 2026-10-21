---
title: "Pi 作者：代码即真相，Bash 够用"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/2089127369596383363
source: X
published: 2026-08-16 23:09 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 编程智能体
roots: [zechner-2025-dont-need-mcp, ronacher-2025-code-is-all-you-need, unix-philosophy, single-source-of-truth, retrieval-augmented-generation]
---

## 原文

Pi 两位作者的见解：

1. 代码即真相，代码不需要记忆系统，不需要 RAG，模型很擅长理解代码结构

2. Bash 工具足够用，Bash 类似于编程语言，可以任意组合；大部分时候没必要 MCP，skill + 脚本足够。 https://t.co/QGCxp2zhWb

> 媒体：
> - https://video.twimg.com/amplify_video/2089125823294881792/vid/avc1/480x270/MHOu4Bt_XfeeN0nl.mp4?tag=29

## 溯源

- 核心主张：编程 agent 直接读代码就够，不需要另建记忆系统或 RAG；Bash 本身像编程语言一样可以任意组合，多数时候 skill 加脚本就能替代 MCP。
- 源知识：
  - [Mario Zechner：也许你根本不需要 MCP](../roots/zechner-2025-dont-need-mcp.md) · 关系：直接源自 · 强弱：强。Pi 作者 Mario Zechner 的原文写「智能体会跑 Bash、会写代码，而 Bash 和代码可以组合」，所以多数场景不需要 MCP，与推文第 2 点几乎一致
  - [Armin Ronacher：工具——代码就是你需要的一切](../roots/ronacher-2025-code-is-all-you-need.md) · 关系：相近 · 强弱：弱（模型复核通过）。Ronacher 主张让模型写代码和脚本、而不是靠 MCP；推文说的「两位作者」推断为 Zechner 和 Ronacher，没有核对视频
  - [Unix 哲学](../roots/unix-philosophy.md) · 关系：相近 · 强弱：弱（模型复核通过）。「Bash 类似编程语言，可以任意组合」就是 Unix 用管道把只做一件事的小工具组合起来的思路
  - [单一事实来源](../roots/single-source-of-truth.md) · 关系：相近 · 强弱：弱（模型复核通过）。「代码即真相，不需要记忆系统」相当于把代码当作唯一事实来源，不另建可能过期的副本
  - [检索增强生成（RAG）](../roots/retrieval-augmented-generation.md) · 关系：挑战 · 强弱：强。推文明说代码不需要 RAG，直接反对「先给模型建检索库再回答」这一主流做法
- 本质：这条新知识本质上是 Unix 哲学（小工具可自由组合）和单一事实来源在编程 agent 工具设计场景下的应用，同时挑战了「agent 必须配 RAG 和专用协议」的主流做法。
- 整理于：2026-10-18（第 1 轮）
