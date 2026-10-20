---
title: "ZCode 的 Gen UI：agent 用 visualize skill 生成可交互界面"
author: "极客杰尼 (@seekjourney)"
url: https://x.com/seekjourney/status/2112098606543188111
source: X
published: 2026-10-19 08:28 UTC
saved: 2026-10-20
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

看了下 ZCode 最新的 Gen UI 实现，思路还挺简单的。

Agent 通过 visualize Skill 生成 HTML + JS，ZCode 负责在对话中渲染，用户可以直接操作滑块、图表和表单。

普通交互由 JS 完成，需要继续推理时再调用 Agent。

特别推荐看看这个 visualize Skill，设计思路很清晰。

Skill：https://t.co/BaQEfxrlhc

> 媒体：
> - https://pbs.twimg.com/media/HU-uZp9bIAANcT_.jpg

## 溯源

