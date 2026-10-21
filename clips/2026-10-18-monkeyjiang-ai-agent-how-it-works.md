---
title: "一张图看懂 AI Agent 怎么工作"
author: "猴哥🐒 (@monkeyjiang)"
url: https://x.com/monkeyjiang/status/1875456381287067976
source: X
published: 2025-01-04 08:17 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [xi-2023-rise-llm-based-agents, intelligent-agent]
---

## 原文

都在讲什么是ai agent，但都不知到ai agent是怎么工作的，看完这张图你就知道了！ https://t.co/eNUMX3vnd1

> 媒体：
> - https://pbs.twimg.com/media/Ggb1oPqXsAA9Dlr.jpg

## 溯源

- 核心主张：AI Agent 的工作方式是：感知部分接收文字、图片、语音等环境信息，大脑部分靠记忆和知识做决策与规划，行动部分输出文字、调用工具或控制实体设备，结果再作用回环境，形成循环。
- 源知识：
  - [大语言模型智能体的兴起与潜力（综述）](../roots/xi-2023-rise-llm-based-agents.md) · 关系：直接源自 · 强弱：强。帖子配图里的英文标注（Inputs、Storage、Memory、Knowledge、Decision Making、Tools、Embodiment）和“明天会下雨吗、下雨就递伞”的例子，就是这篇综述图 2 的“大脑—感知—行动”框架，作者只加了中文注解，没有标出处。
  - [智能体](../roots/intelligent-agent.md) · 关系：换了说法 · 强弱：弱（模型复核通过）。“感知环境、思考、行动作用于环境”就是教科书里智能体的定义，只是把大脑换成了大语言模型。
- 本质：这条新知识本质上是经典智能体“感知—决策—行动”循环在大语言模型 agent 场景下的图解，图直接取自 Xi 等 2023 年的综述。
- 整理于：2026-10-18（第 2 轮）
