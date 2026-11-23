---
title: "Kevin Roose 首次公开 Amodei 2017 年 OpenAI 内部文档《Big Blob of Compute》节选"
author: "Kevin Roose (@kevinroose)"
url: https://x.com/kevinroose/status/2107269612115202549
source: X
published: 2026-10-06 00:40 UTC
saved: 2026-11-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 历史与冷知识
roots: [amodei-2017-big-blob-of-compute, bitter-lesson, neural-scaling-law]
---

## 原文

On the eve of The AGI Chronicles (which comes out tomorrow!) I'm publishing an excerpt from "Big Blob of Compute," a 2017 internal research document by Dario Amodei, back when he was a researcher at OpenAI. 

It's never been published before, but BBOC is, in my mind, the essay that started the AI race. It described Amodei's hypothesis that scaling up AI models was the best way, by far, to make them smarter. GPT-2 was an experiment to test the hypothesis, and when it worked, OpenAI went all-in on scaling, which led to the race we have today.

It's a fascinating historical artifact that deserves to see the light of day. And it's taken on mythical proportions inside the AI industry, which is now spending trillions of dollars building the "big blobs" that Amodei thought would be necessary to get to AGI.

Enjoy! And please pre-order the book if you do! 

https://t.co/dGBzcI6Mrl

## 溯源

- 核心主张：Kevin Roose 公开 Dario Amodei 2017 年在 OpenAI 写的内部文档节选：造出智能主要靠一大块结构很少的算力，加上足够的参数、经验、合适的经验分布和训练目标，复杂的算法巧思作用不大；Roose 认为这份文档推动 OpenAI 押注扩大规模（GPT-2 是检验），引出今天的 AI 竞赛。
- 源知识：
  - [大块算力假说](../roots/amodei-2017-big-blob-of-compute.md) · 关系：直接源自 · 强弱：强。这条推文就是在发布这份文档。节选 PDF 第 1–2 节给出 BBOC 的定义和 7 个旋钮；Amodei 本人 2026-02-13 在 Dwarkesh 播客里也确认 2017 年写过这份文档、至今仍持这个假说。
  - [苦涩的教训](../roots/bitter-lesson.md) · 关系：相近 · 强弱：强。Roose 在文章里明说类似想法后来由 Sutton《苦涩的教训》普及，Amodei 在 Dwarkesh 播客里也说两者「基本是同一个假说」；节选第 1 节「人为规定计算怎么分工的算法往往很差」和苦涩的教训几乎同一个意思。BBOC（2017）早于 Sutton（2019），所以只能算相近，不能写成源自。
  - [神经网络规模定律](../roots/neural-scaling-law.md) · 关系：相近 · 强弱：弱（模型复核通过）。BBOC 是定性的「算力、参数、经验够了就会变好」，规模定律是后来的定量版本（Hestness 等 2017 年 12 月、Kaplan 等 2020，后者 Amodei 是作者之一）。时间上 BBOC 不晚于它们，不能写成直接源自；节选文末作者还明说这不等于「把现有算法放大就能到 AGI」。
- 本质：这条新知识本质上是「通用学习方法加足够算力胜过人工巧思」这一路想法（后来的苦涩的教训、规模定律）在 2017 年 OpenAI 内部的早期表述；「它开启了 AI 竞赛」是 Roose 的判断。
- 整理于：2026-11-23（第 12 轮）
