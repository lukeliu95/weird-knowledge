---
title: "开源类Perplexity的AI搜索"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/1877118831866306872
source: X
published: 2025-01-08 22:22 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: Agent 与 Skill
roots: []
---

## 原文

感谢安替老师推荐的开源项目 Gemini Search:

这是一个类似 Perplexity 的 AI 搜索工具。它的核心特点是使用了 Google 最新的 Gemini 2.0 Flash 模型,并结合 Google 搜索 API （所以每次搜索是有成本的，约 ¥0.25/次）来提供基于实时网络资源的 AI 问答服务。

主要功能包括:

1. 实时网络搜索集成 - 系统可以获取并分析最新的网络信息

2. AI 回答能力 - 使用 Gemini 2.0 Flash 模型生成答案，这是 Google 最新推出的大语言模型

3. 源引用功能 - 所有回答都会提供相关的网络来源和引用，增加可信度

4. 对话连续性 - 支持在同一会话中进行后续提问和对话

5. 现代化界面 - 采用了类似 Perplexity 的清爽设计风格

技术栈:

- 前端采用 React + Vite 构建,使用 TypeScript 确保代码质量,并用 Tailwind CSS 实现界面样式

- 后端使用 Express.js 框架,同样采用 TypeScript 开发

- AI 对话能力通过调用 Gemini 2.0 Flash API 实现

- 搜索功能则整合了 Google Search API

这个项目的一个重要特点是结合了 AI 问答和实时网络搜索，可以提供既有深度又有时效性的回答。同时,通过提供源引用，让用户可以验证答案的可靠性，这是很多 AI 问答系统所欠缺的功能。

> 媒体：
> - https://video.twimg.com/tweet_video/GgzdPFoXUAA78D8.mp4

## 溯源

