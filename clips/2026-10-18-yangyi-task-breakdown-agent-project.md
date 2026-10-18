---
title: "AI 编程像人一样拆解任务的神仙项目"
author: "Yangyi (@yangyi)"
url: https://x.com/yangyi/status/1914687827117518991
source: X
published: 2025-04-22 14:28 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 编程智能体
roots: [user-story, work-breakdown-structure, hierarchical-task-network, boehm-1981-software-engineering-economics, garbage-in-garbage-out]
---

## 原文

我只能称之为神仙项目
但凡是做AI Coding的，在工程上绝对会想办法按照这个思路做封装的

以前任务做不好，大多数是PRD写不好
PRD写好之后，还需要的是把任务拆解好
就像人在执行工作时，也会有依赖项，也会有epic和story

所有Agent都应该和人一样设计就对了  这个项目就用来做这个的！ https://t.co/SLTOSJGhgL

> 媒体：
> - https://pbs.twimg.com/media/GpJWSmla4AQf2xk.jpg

## 溯源

- 核心主张：AI 编程任务做不好，多半是需求文档（PRD）没写好；PRD 写好之后，还要像人一样把任务拆成带依赖关系的 epic 和 story，所以 agent 应该照人的工作方式来设计。
- 源知识：
  - [用户故事（含 Epic 与 Story 层级）](../roots/user-story.md) · 关系：直接源自 · 强弱：强。作者明说“就像人在执行工作时，也会有依赖项，也会有 epic 和 story”，epic 和 story 就是敏捷开发里用户故事的层级
  - [工作分解结构（WBS）](../roots/work-breakdown-structure.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。配图是按编号分层（4.1、4.2……）并标出依赖的任务表，和工作分解结构“逐层拆成可管理、可核对的工作单元”是同一做法，作者没点名
  - [分层任务网络规划（HTN）](../roots/hierarchical-task-network.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。AI 规划里的分层任务网络，把复合任务逐层分解成可直接执行的子任务，并加上先后约束；配图里的子任务和依赖列与之对应，属推断
  - [《软件工程经济学》（错误越晚修越贵）](../roots/boehm-1981-software-engineering-economics.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“任务做不好大多是 PRD 写不好”与 Boehm 的结论（需求阶段的错误代价最大、越晚修越贵）相近，属推断
  - [垃圾进，垃圾出](../roots/garbage-in-garbage-out.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。需求输入差，代码输出就差，是“垃圾进，垃圾出”在 AI 编程上的说法，属推断
- 本质：这条新知识本质上是软件工程里“需求先行、分层拆解”（用户故事、工作分解结构）在 AI 编程智能体做任务规划这个场景下的应用。
- 整理于：2026-10-18（第 2 轮）
