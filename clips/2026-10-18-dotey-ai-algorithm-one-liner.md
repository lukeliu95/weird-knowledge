---
title: "一句话总结 AI 算法的含义"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/1731714223728644268
source: X
published: 2023-12-04 16:36 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 思维与成长
roots: [problem-of-induction, dataset-shift]
---

## 原文

来总发的一句话挺有意思：

今天学习到一句话总结AI算法，mk下——“现在是过去的未来，现在不一定是未来的过去” ​​​

请问怎么解读？ https://t.co/PU97WWpwyF

> 媒体：
> - https://pbs.twimg.com/media/GAhI4aHWUAYEdFq.png

## 溯源

- 核心主张：AI 算法靠过去的数据学规律来预测：过去的规律能解释现在，但现在的规律不一定能延续到未来，所以预测有前提，也会失效。（原帖只有一句话加“怎么解读”，这是对它的解读）
- 源知识：
  - [归纳问题](../roots/problem-of-induction.md) · 关系：相近 · 强弱：弱（模型复核通过）。“现在不一定是未来的过去”说的正是休谟的归纳问题：凭过去的观察推断未来，没有逻辑上的保证；原话没提休谟，这是解读
  - [数据集偏移](../roots/dataset-shift.md) · 关系：相近 · 强弱：弱（模型复核通过）。落到机器学习上，就是训练时的数据（过去）和使用时的数据（未来）分布不一样，模型就会失效
- 本质：这条新知识本质上是休谟归纳问题在机器学习预测场景下的应用：模型默认“未来像过去”，这个假设一旦不成立（数据集偏移），预测就会失准。
- 整理于：2026-10-18（第 2 轮）
