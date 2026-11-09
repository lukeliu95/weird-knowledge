---
title: "TypeSafe：别把 Jev 叫决定模型——模型做判断，代码做决定"
author: "allietheicon (@allietheicon)"
url: https://x.com/allietheicon/status/2118508406088847677
source: X
published: 2026-11-06 00:58 UTC
saved: 2026-11-07
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [typesafe-2026-judgments-code-decisions, separation-of-concerns]
---

## 原文

Why don't we at TypeSafe call Jev a decision model?

If you think of Jev's questions as making *decisions*, I believe you'll use it at the wrong layer of abstraction and your reliability will suffer.

I wrote all about this on our site 🧵👇 https://t.co/CfY5W84NqA

https://t.co/AYYJmpOByC

> 原推：https://x.com/allietheicon/status/2118508404192981040
> 链接卡片：Don’t Call It a Decision Model - TypeSafe AI Blog https://typesafe.ai/blog/dont-call-it-a-decision-model

> 媒体：
> - https://video.twimg.com/tweet_video/HWZ0FelbYAEPHz1.mp4

## 溯源

- 核心主张：TypeSafe 主张让模型回答需要理解语义的独立判断题，把已知业务规则、优先级和计算放进代码，再由代码组合这些判断作出最终选择；这能让错误较容易被定位，但不是所有决定都能写成固定规则的证明。
- 源知识：
  - [模型做语义判断，代码组合业务决定](../roots/typesafe-2026-judgments-code-decisions.md) · 关系：直接源自 · 强弱：强。TypeSafe 的原文用退款流程说明：是否在请求退款是语义判断，是否符合已知退款条件是业务规则；应把多个独立判断交给代码组合，而非把整套规则塞进一个模型选择题。这是模型厂商的工程建议，文中没有对照实验来证明普遍收益。
  - [关注点分离](../roots/separation-of-concerns.md) · 关系：相近 · 强弱：弱（模型复核通过）。把语义识别、规则计算和最终分支分开，符合关注点分离的做法；原作者未引用 Dijkstra，因此这里只标相近，不能写成历史继承关系。
- 本质：这条新知识本质上是关注点分离在模型工作流中的应用：让不确定的语义判断和确定的业务规则各自承担明确责任。
- 整理于：2026-11-09（第 10 轮）
