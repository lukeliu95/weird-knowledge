---
title: "MiMo-V2.6 正在跑强化学习"
author: "Fuli Luo (@_LuoFuli)"
url: https://x.com/_LuoFuli/status/2100296686719610932
source: X
published: 2026-09-16 18:52 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

Nearly half a year of silence. We spent it studying one problem: how far RL can scale.

MiMo-V2.6 is in the middle of its RL run right now. Three things we scaled: compute (~2B tokens per step, 1568 prompts × 16 rollouts, fully async), environments and harnesses (multi-task agentic RL, mixed across multiple harnesses in one run), and grader compute (agentic in-group credit assignment, with test-case and rubric-based rewards). We'll open-source the details piece by piece over the coming weeks.

Streaming the run: https://t.co/ZSxahzJRju

## 溯源

