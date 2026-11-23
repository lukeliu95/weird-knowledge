---
title: "NVIDIA 论文：推理一次转成 CPU 代码，同类题每次调用便宜 16～291 倍（构建要花 12～84 倍）"
author: "Rohan Paul (@rohanpaul_ai)"
url: https://x.com/rohanpaul_ai/status/2124177125247013266
source: X
published: 2026-11-21 16:24 UTC
saved: 2026-11-23
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 模型与本地部署
roots: [belcak-2026-cpu-arc, memoization, explanation-based-learning, chen-2023-frugalgpt]
---

## 原文

New NVIDIA paper finds that once an LLM has reasoned through a problem, the solution can run as CPU code for rephrased and re-numbered versions of it.

that answers similar questions 16x to 291x cheaper.

LLMs re-solve every problem from scratch, even when only wording or numbers change. Agents sending the same instructions with new data pay for that repeated reasoning each time.

Their method has Claude Opus 4.5 turn a reasoning trace into small Python functions, with changeable inputs as parameters. At run time they execute on a CPU, calling a fine-tuned 1B model only for small text jobs like extracting values.

The cache matched or beat the source model's accuracy on 7 of 8 math and science benchmarks, scoring 93.3% versus 83.3% on AIME '25. It handled at least 90% of rephrased or re-numbered variants.

If your agent runs the same prompt on new inputs all day, cache the reasoning as code and use the LLM only on misses.

> 媒体：
> - https://pbs.twimg.com/media/HXqXimdagAEb5ZJ.png

## 溯源

- 核心主张：大模型把一道题想通之后，可以把推理改写成带参数的小程序在 CPU 上跑，换说法、换数字的同类题直接复用，只有没命中时才再调大模型；NVIDIA 论文称这样调用成本便宜 16～291 倍，准确率在 8 个测试里 7 个不低于原模型。
- 源知识：
  - [CPU-ARC：把推理过程缓存成可在 CPU 上复用的代码](../roots/belcak-2026-cpu-arc.md) · 关系：直接源自 · 强弱：强。推文转述的就是这篇论文。数字核对原文：16～291 倍（摘要、表 2、第 3.6 节）、AIME ’25 93.3% 对 83.3%（表 2）、8 个里 7 个不低于原模型（第 3.6 节）、改写题至少 90% 处理对（最低 90.8%，第 3.6 节）、Opus 4.5 建缓存、微调 Llama 3.2 1B 做抽取（第 3.4 节）都对得上。推文没提构建一次要花原模型 12～84 倍。
  - [记忆化（备忘函数）](../roots/memoization.md) · 关系：相近 · 强弱：弱（模型复核通过）。论文自己把方法定位为「缓存」：先查缓存、没命中再调大模型（图 1）。这是记忆化（算过一次就存结果，下次同样输入直接取）的推广：从「同样输入」扩到「换说法、换数字但解法相同」的一类题，存的是带参数的解法而不只是答案。论文没有引用 Michie。
  - [基于解释的学习（解释泛化）](../roots/explanation-based-learning.md) · 关系：相近 · 强弱：弱（模型复核通过）。从一道已解出的题和它的推理过程，归纳出对一整类题都成立的带参数规则，是基于解释的学习（EBL/EBG）的核心做法；论文第 1 节的观察 O2（推理可复用于单个实例以外的一类题）和第 2 节的「等推理（equirational）」参数集合就是这个意思。论文没有引用 EBL 文献，是推断。
  - [FrugalGPT：用级联大模型省钱又提效](../roots/chen-2023-frugalgpt.md) · 关系：相近 · 强弱：弱（模型复核通过）。先走便宜的路（CPU 代码加 1B 小模型），失败才落回昂贵的大模型（论文图 1 的门控调用），和 FrugalGPT 的级联省钱思路相同；区别是这里便宜的那一层是缓存出来的程序，不是另一个模型。
- 本质：这条新知识本质上是「记忆化 + 从一个解过的例子推广出可复用的带参数规则」，配上「先走便宜路径、失败再调大模型」的级联，用在大模型重复推理的成本上。
- 整理于：2026-11-23（第 12 轮）
