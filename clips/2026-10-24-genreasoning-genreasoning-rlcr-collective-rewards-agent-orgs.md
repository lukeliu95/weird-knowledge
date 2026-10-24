---
title: "RLCR：用集体奖励把模型训练成会分工的智能体组织"
author: "General Reasoning (@GenReasoning)"
url: https://x.com/GenReasoning/status/2113590771722952908
source: X
published: 2026-10-23 11:18 UTC
saved: 2026-10-24
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [collective-intelligence, division-of-labour, the-mythical-man-month, alchian-1972-team-production, blackboard-system]
---

## 原文

Introducing Reinforcement Learning from Collective Rewards (RLCR).

RLCR is a recipe that trains language models as agent organisations, which share a message board and workspace. We use it to train Avalon-M1-Mini (120B) and study its behaviour.

We find a number of interesting results, including:

🛠️ Learnt organisational hierarchies and divisions of labour
🕵️ Increased collective verification, through hires of verifiers and testers
👥 The rise of collective thinking, where agents think more about other agents and how to help them

We believe RLCR can provide a laboratory for studying collective intelligence and multi-agent safety.

Blog post and technical report 👇

> 媒体：
> - https://video.twimg.com/amplify_video/2113576707059855360/vid/avc1/1920x1080/TkzPBTJiHIvY9P_-.mp4?tag=29

## 溯源

- 核心主张：只给整个 agent 团队一个共同奖励、不区分每个人的贡献，用强化学习训练共享留言板和工作区的 agent 组织，组织就会自己长出层级和分工、主动雇验证者和测试员、更多地考虑怎么帮队友，可以当研究集体智能和多 agent 安全的实验场。
- 源知识：
  - [集体智能](../roots/collective-intelligence.md) · 关系：直接源自 · 强弱：强。原推明说 RLCR 是研究集体智能的实验室；技术报告把“组织随通信算力变强”称为集体版的长推理。
  - [分工](../roots/division-of-labour.md) · 关系：直接源自 · 强弱：强。原推报告“学会了组织层级和分工”，技术报告明引 Smith 1776《国富论》的分工论。
  - [《人月神话》（准备扔掉一个）](../roots/the-mythical-man-month.md) · 关系：相近 · 强弱：强。技术报告明引 Brooks《人月神话》的外科手术团队；训练后 CEO 从按模块拆活转向“构建—测试—评审”流水线、主程成为主要建造者和信息枢纽，和 Brooks 以主刀为核心的分工组织相近。
  - [生产、信息成本与经济组织（团队生产理论）](../roots/alchian-1972-team-production.md) · 关系：相近 · 强弱：弱（模型复核通过）。共同奖励下个人贡献无法计量，团队生产理论预言会出现偷懒、于是要设专门的监督者；RLCR 里雇评审类角色的比例从 13% 升到 26%、有同行评审的组织从 42% 升到 64%，正对应这个预言；报告引的是 Alchian 1950 而不是这篇，是模型推断。
  - [黑板系统](../roots/blackboard-system.md) · 关系：相近 · 强弱：弱（模型复核通过）。多个专家 agent 通过一块共享留言板和工作区读写进展来协作，和人工智能里的黑板系统架构相近；报告没提黑板系统，是模型推断。
- 本质：这条新知识本质上是团队生产与分工的组织经济学在“只奖励整体”的多 agent 强化学习里的重演：只奖励整体时，组织会自己演化出分工、层级和监督。
- 整理于：2026-10-24（第 6 轮）
