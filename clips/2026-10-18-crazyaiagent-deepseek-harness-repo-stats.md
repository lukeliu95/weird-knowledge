---
title: "DeepSeek 仓库开发数据拆解"
author: "狂热AI (@CrazyAIAgent)"
url: https://x.com/CrazyAIAgent/status/2088104421993632002
source: X
published: 2026-08-14 03:24 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 编程智能体
roots: [specification-driven-development, lehmans-laws-of-software-evolution, open-closed-principle, hum-2025-sora-android-codex]
---

## 原文

1. dsh   deepseek的harness，从零开始到仓库开源，用了64天，产出 12293 个 commit，日均 192 个，PR 编号最大到 #2521，平均每天 39 个 PR，效率拉满。。

2. deepseek内部大概是一个6～8人的团队在全职做这个，cui tianyi 一个人贡献了42.6%的代码量，绝对的 dsh 之父

3.  cui tianyi的每日跨度中位数是 15.6 小时（10:36 到次日 01:54），68% 的工作日超过 12 小时，比996都猛

4. 这个代码仓库提交静默期中位数只有5.8h，几乎所有的周六日都不歇着，一直有人在提交代码

5. 从提交记录看， deepseek 早上10点上班😁。

6. 这个团队重度使用 codex，没错，dsh 是用codex写出来的，重度使用 codex cloud。 

8 . dsh 仓库践行了绝对的spec编程，markdown文件比代码文件还多

9. 从第一天起，dsh就规划了一切皆插件的机制

10. 安排给codex最多的任务是simplifications，也就是清理多余的代码，怎么删代码在 dsh 自己的 harness 上占比很大。截止开源时这个库有 85 万行、其中 57 万行是源码，开发过程中删掉了 73.5 万行

## 溯源

- 核心主张：DeepSeek 的 harness（dsh）由 6～8 人重度使用 Codex 在 64 天内做成，做法是规格文档先行、一切皆插件，并把最多的 agent 任务用在简化和删代码上（开发中删掉 73.5 万行）。
- 源知识：
  - [规格驱动开发](../roots/specification-driven-development.md) · 关系：直接源自 · 强弱：强。作者明说 dsh“践行了绝对的 spec 编程，markdown 文件比代码文件还多”。
  - [雷曼软件演化定律](../roots/lehmans-laws-of-software-evolution.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。雷曼第二定律：系统演化时复杂度会上升，除非专门投入工作去维持或降低；dsh 把最多的 Codex 任务安排给简化、删掉 73.5 万行，正是这份专门投入。
  - [开闭原则](../roots/open-closed-principle.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“从第一天起一切皆插件”就是对扩展开放、对修改封闭：新功能以插件加进来，不改核心。
  - [OpenAI：用 Codex 28 天做出 Sora 安卓版](../roots/hum-2025-sora-android-codex.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。同类案例：OpenAI 4 人 28 天用 Codex 做出 Sora 安卓版，同样靠先写规范文档、让 agent 出计划再实现。
- 本质：这条新知识本质上是规格驱动开发和雷曼定律（复杂度要靠专门投入去压）在小团队用编码 agent 高速开发场景下的应用。
- 整理于：2026-10-18（第 2 轮）
