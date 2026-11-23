---
title: "帖子称黎曼猜想 Lean 证明“零报错、没人看得懂”（夸大：是社区背书，人还没完全读懂）"
author: "Rachel (@RachelRifx)"
url: https://x.com/RachelRifx/status/2124320264771285107
source: X
published: 2026-11-22 01:53 UTC
saved: 2026-11-23
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 学习与研究
roots: [lean-mathlib-2026-rh-verification-statement, sutherland-2026-rh-lean-verification-files, alpoge-2026-rh-lean-proof, riemann-hypothesis]
---

## 原文

人类数学史真的被彻底改写了：

麻省理工和 Lean 官方刚正式确认，Claude 写出的那 1700 万行“黎曼猜想”证明代码，居然 0 报错、100% 通过了最严苛的计算机逻辑验证。

一个困扰人类 160 年的世纪难题被解开了，但全地球没有一个人类能看懂它是怎么解开的。

## 溯源

- 核心主张：帖子称 MIT 和 Lean 官方确认 Claude 写的 1700 万行黎曼猜想证明零报错、百分之百通过机器验证，但全世界没有一个人看得懂。
- 源知识：
  - [Lean 与 Mathlib 社区关于黎曼猜想 Lean 证明的联合声明](../roots/lean-mathlib-2026-rh-verification-statement.md) · 关系：直接源自 · 强弱：强。“Lean 官方确认”“0 报错”对应 Lean 与 Mathlib 社区的联合声明（Lean FRO、Mathlib Initiative 背书，原话“compiles without errors or build failures”）。
  - [Sutherland（MIT）整理的黎曼猜想 Lean 证明核验文件页](../roots/sutherland-2026-rh-lean-verification-files.md) · 关系：直接源自 · 强弱：弱（模型复核通过）。帖子没给出处。“麻省理工确认”最可能指 MIT 数学家 Andrew Sutherland 个人整理、挂在 math.mit.edu 的核验页（Lean 声明也链接了它）。这是个人核验，不是 MIT 机构声明；帖子发出时（11-22 01:53 UTC）该页还有两项检查在跑，“100% 通过”说早了。
  - [Alpöge 与 Claude 的黎曼猜想 Lean 证明（公告与代码）](../roots/alpoge-2026-rh-lean-proof.md) · 关系：直接源自 · 强弱：强。“1700 万行”出自这次发布。但不是“Claude 写出的”，Alpöge 写的是“和 Claude 一起”；“没人看得懂”是把作者自己说的“还没吃透周边的数学”“不发 25 万页不可读的文字稿”放大成了“全地球没人能懂”。
  - [黎曼猜想](../roots/riemann-hypothesis.md) · 关系：直接源自 · 强弱：强。“困扰人类 160 年的世纪难题”即黎曼猜想（1859 年提出）。
- 本质：这条新知识本质上是 Lean 社区对黎曼猜想形式化证明的认证，在转述中被放大（安上 MIT 的名义、说成“100% 通过”“无人能懂”）的一个版本。
- 整理于：2026-11-23（第 12 轮）
