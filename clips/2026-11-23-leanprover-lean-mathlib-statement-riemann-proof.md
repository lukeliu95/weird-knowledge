---
title: "Lean FRO 和 Mathlib 发声明：验证了黎曼猜想的 Lean 证明"
author: "Lean (@leanprover)"
url: https://x.com/leanprover/status/2124159121645801562
source: X
published: 2026-11-21 15:12 UTC
saved: 2026-11-23
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 学习与研究
roots: [lean-mathlib-2026-rh-verification-statement, alpoge-2026-rh-lean-proof, buzzard-2026-checked-in-lean, lean-proof-assistant, riemann-hypothesis, de-bruijn-criterion]
---

## 原文

The Lean FRO and Mathlib Initiative have released a joint statement on the Lean verification of the Riemann Hypothesis.

On November 20, Levent Alpöge released a proof of the Riemann Hypothesis as a Lean library of 17 million lines of code. Over the past day, the Lean and Mathlib communities worked together to verify it. The statement certifies the proof as correct and describes how it meets all necessary verification criteria.

Congratulations to Levent on this achievement, and thank you to everyone in the community who contributed to the verification.

Full statement: https://t.co/edxEbkodw7

> 媒体：
> - https://pbs.twimg.com/media/HXqGwBnaUAA8Pvd.png

## 溯源

- 核心主张：Lean 与 Mathlib 社区发联合声明（Lean FRO、Mathlib Initiative 背书）：Alpöge 11 月 20 日发布的 1700 万行 Lean 库，黎曼猜想的陈述和证明都正确，满足判断 Lean 证明可信的全部标准。
- 源知识：
  - [Lean 与 Mathlib 社区关于黎曼猜想 Lean 证明的联合声明](../roots/lean-mathlib-2026-rh-verification-statement.md) · 关系：直接源自 · 强弱：强。推文就是这份声明的转发，t.co 短链接指向声明全文；声明原话是“certify that both the statement and the proof of the Riemann Hypothesis are correct”。
  - [Alpöge 与 Claude 的黎曼猜想 Lean 证明（公告与代码）](../roots/alpoge-2026-rh-lean-proof.md) · 关系：直接源自 · 强弱：强。被验证的对象就是 Alpöge 11-20 在 alpo.ge 发布的 remark.pdf 和 14 个 Lean 压缩包；声明开头就写明。
  - [判断“已在 Lean 里检查过”可不可信的四个问题](../roots/buzzard-2026-checked-in-lean.md) · 关系：直接源自 · 强弱：强。推文说“meets all necessary verification criteria”，声明正文明说指的是 Buzzard 11-12 博文里的四条标准，并逐条对照：陈述对、能编译、证明的正是这条陈述、内核检查有效。
  - [Lean 证明助手](../roots/lean-proof-assistant.md) · 关系：直接源自 · 强弱：强。证明以 Lean 库发布，由 Lean 官方内核和其他检查器复查。
  - [黎曼猜想](../roots/riemann-hypothesis.md) · 关系：直接源自 · 强弱：强。被证明的命题就是黎曼猜想，用的是 Mathlib 里由 Lean 和数论专家审过的 RiemannHypothesis 定义。
  - [德布鲁因准则（证明要能被小而独立的程序复查）](../roots/de-bruijn-criterion.md) · 关系：相近 · 强弱：弱（模型复核通过）。声明的关键做法是把证明导出成“惰性”文件，交给官方内核和几个用不同语言独立写的检查器（con-leche、con-ron 等）复查，这正是“证明要能被小而独立的程序复查”的德布鲁因准则；声明没点这个名字，属推断。
- 本质：这条新知识本质上是德布鲁因准则（证明交给多个独立的小检查器复查）和 Buzzard 四问，在“AI 参与生成的超大规模数学证明”这一场景下的一次完整应用。
- 整理于：2026-11-23（第 12 轮）
