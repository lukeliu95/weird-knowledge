---
title: "Agent 循环工程晚宴讨论要点"
author: "Jerry Liu (@jerryjliu0)"
url: https://x.com/jerryjliu0/status/2082673383255216356
source: X
published: 2026-07-30 03:43 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [young-2025-long-running-agent-harness, sheridan-1992-human-supervisory-control, ironies-of-automation, law-of-amplification, dellacqua-2023-jagged-technological-frontier, you-arent-gonna-need-it]
---

## 原文

Yesterday I cohosted a dinner with @dexhorthy with a wonderful group of founders, to talk about agent loops and loop engineering.

Some interesting insights:
* Most of our group was *not* actively using /loop in Codex/Claude Code
* You can build long-running autonomous agent loops through multi-agent handoffs, event triggers, or….just stacks of cron jobs (?)
* Almost everyone believes that no one will be reviewing code in 1-2 years.
* The more interesting question is whether we’d be reviewing *anything* in 1-2 years.
* AI is still a bit of a skill issue. Humans are responsible for maximizing AI output and reducing slopification.
* Will human intellect provide alpha as models get better, or will the playing field be leveled? Most people think it will be leveled a bit, but there is a need for humans to provide alignment, guardrails, judgment, creativity.
* The minimum amount of context you need for AI could be just the codebase with some documentation. Any research/plan files are for one-off tasks and not meant to be maintained. Having a self-organizing wiki is nice but adds complexity.

If you missed this one, we’ll be hosting more dinners like this on a regular cadence! If you have thoughts on what we should talk about, let us know :) (e.g. continual learning, RL envs, competitive differentiation vs. Anthropic, etc.)

> 媒体：
> - https://pbs.twimg.com/media/HOckY6Ca8AAS5A7.jpg

## 溯源

- 核心主张：长时间自主运行的 agent 循环，用多 agent 交接、事件触发甚至一堆定时任务就能搭起来；人的角色会从审代码转向提供对齐、护栏、判断和创意；AI 需要的最少上下文只是代码库加文档，计划类文件用完即弃。
- 源知识：
  - [长时间运行 agent 的有效 harness](../roots/young-2025-long-running-agent-harness.md) · 关系：相近 · 强弱：弱（模型复核通过）。Anthropic 的长时 harness 靠会话之间交接进度记录让 agent 连续工作，和“用多 agent 交接搭长循环”是同一思路；原帖没有引用。
  - [人类监督控制](../roots/sheridan-1992-human-supervisory-control.md) · 关系：相近 · 强弱：弱（模型复核通过）。“没人审代码，但人要提供对齐、护栏和判断”，就是监督控制里人从动手操作者变成定计划、看执行、必要时介入的角色转换。
  - [自动化的反讽](../roots/ironies-of-automation.md) · 关系：挑战 · 强弱：弱（模型复核通过）。“1～2 年内没人再审代码”和 Bainbridge 的警告相反：自动化越多，人平时越缺练习，却要在关键时刻接手，所以人的监督能力反而更关键。
  - [技术放大定律](../roots/law-of-amplification.md) · 关系：相近 · 强弱：弱（模型复核通过）。“AI 还是使用者的水平问题，人负责把 AI 产出做到最好、减少垃圾产出”，和“技术只放大使用者已有的能力”一致。
  - [在参差不齐的技术边界上航行（BCG 顾问实验）](../roots/dellacqua-2023-jagged-technological-frontier.md) · 关系：相近 · 强弱：弱（模型复核通过）。“多数人认为人和人之间的差距会被拉平一点”，和 BCG 顾问实验里原本水平低的人提升最多的结果相近。
  - [YAGNI（你不会需要它）](../roots/you-arent-gonna-need-it.md) · 关系：相近 · 强弱：弱（模型复核通过）。“研究和计划文件只服务一次性任务、不必维护，自组织 wiki 增加复杂度”，就是 YAGNI：不为将来可能用到而提前搭建和维护。
- 本质：这条新知识本质上是人类监督控制（人从操作者变成定目标、设护栏、做判断的监督者）在 AI 编程 agent 长时间自主运行场景下的应用，同时对“自动化的反讽”提出了偏乐观的挑战。
- 整理于：2026-10-18（第 2 轮）
