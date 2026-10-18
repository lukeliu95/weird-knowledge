---
title: "Gemini 2.5 配 aider 重构代码"
author: "LinearUncle (@LinearUncle)"
url: https://x.com/LinearUncle/status/1909396677074780529
source: X
published: 2025-04-08 00:03 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

吹一次gemini 2.5 pro.

1200行的AI早期产生的屎山代码文件，gemini 2.5 pro + aider重构后拆分成7个子组件，原文件骤降到127行.

总共花费15分钟，一共3个prompt迭代（重构，fix lint, fix一个界面问题）。

细看aider截图，context发送高达22k，本质上是gemini 100万上下文+强大的coding能力双双发挥了作用。

无解的是这个模型还是免费的，完全不心疼。

> 媒体：
> - https://pbs.twimg.com/media/Gn-HqqjbwAELYr0.jpg
> - https://pbs.twimg.com/media/Gn-Hu-5a4AA5_b7.png

## 溯源

