---
title: "吴恩达：自我改进循环将取代提示"
author: "Movez (@0xMovez)"
url: https://x.com/0xMovez/status/2068763235587694769
source: X
published: 2026-06-21 18:29 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [ng-2024-agentic-design-patterns, madaan-2023-self-refine, karpathy-2026-autoresearch]
---

## 原文

Andrew Ng:

"100% of my tasks are now done by AI agents - hype has exceeded my expectations. Loops is next step.

in 3-6 months, everyone will be using self-improving loops. No more prompting."

In a 30-minute talk, Andrew Ng explains how to build self-improving agentic systems from scratch.

Worth more than a $500 agentic course.

> 媒体：
> - https://video.twimg.com/amplify_video/2068762224630390784/vid/avc1/480x270/KiMoLcl61Dd1Xhdu.mp4?tag=28

## 溯源

- 核心主张：人手写提示、一次出结果的用法会被“自我改进循环”取代：让 agent 多轮生成、检查、改进，直到达标。（“我 100% 的任务由 agent 完成”“3 到 6 个月后人人用循环、不再写提示”这些引语没有查到吴恩达本人的原话，待确认。）
- 源知识：
  - [吴恩达：智能体设计模式（反思、工具使用、规划、多智能体协作）](../roots/ng-2024-agentic-design-patterns.md) · 关系：直接源自 · 强弱：弱（待 Luke 确认）。吴恩达 2024 年在 The Batch 连载《智能体设计模式》，主张多轮迭代的智能体工作流胜过一次写完的零样本提示，并以“反思”为第一个模式；这条帖子说的“自我改进循环取代提示”就是这一主张的延续。帖子里的演讲和引语没能核实，所以标弱。
  - [自我改进：用自我反馈迭代改写](../roots/madaan-2023-self-refine.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“self-improving loops”最基本的形式就是 Self-Refine：模型生成、自己给反馈、再改写，循环到满意为止；吴恩达的“反思”模式也推荐这篇论文。帖子没有引用。
  - [autoresearch（自动做研究的循环）](../roots/karpathy-2026-autoresearch.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。2026 年流行的“循环”做法以 Karpathy 的 autoresearch 为代表：agent 改代码、跑固定实验、看指标，变好就留、变差就丢，整夜无人值守。帖子说的“Loops is next step”和这股潮流同期，但没有提到它，是推断。
- 本质：这条新知识本质上是吴恩达的智能体工作流（反思模式），也就是“生成-反馈-改进”循环，在取代人工写提示这个场景下的应用。
- 整理于：2026-10-18（第 2 轮）
