---
title: "开源模型自我验证跑赢闭源模型"
author: "Jacky Kwok (@jackyk02)"
url: https://x.com/jackyk02/status/2089421448784023553
source: X
published: 2026-08-17 18:37 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 模型与本地部署
roots: [kwok-2026-llm-as-a-verifier, cobbe-2021-training-verifiers, snell-2024-test-time-compute, zheng-2023-llm-as-a-judge]
---

## 原文

Scaling self-verification with DeepSeek V4 Flash beats Claude Fable 5 on Terminal-Bench 2.1, while being 11x cheaper 💰

As open-source models become more capable, they can now generate large numbers of high-quality candidate solutions and verify their own outputs at very low cost.

For example, we find that sampling just 5 solutions with DeepSeek V4 Flash and ranking them using the same model with LLM-as-a-Verifier can lead to a significant boost in accuracy (79% → 88%), outperforming closed frontier models on Terminal-Bench.

Try it out today: https://t.co/UhudjKDaYI

More on verification scaling in my previous post.

> 媒体：
> - https://pbs.twimg.com/media/HP8c7DyaYAAjGdm.jpg

## 溯源

- 核心主张：让便宜的开源模型对同一任务生成几个候选解，再用同一个模型当验证器打分、挑出最好的，准确率能从 79% 提到 88%，用大约十一分之一的成本超过闭源前沿模型。（数字是作者自己报的，没有独立验证）
- 源知识：
  - [大模型当验证器](../roots/kwok-2026-llm-as-a-verifier.md) · 关系：直接源自 · 强弱：强。推文点名 LLM-as-a-Verifier，这是作者本人 2026 年 7 月论文里的框架
  - [训练验证器来解数学应用题](../roots/cobbe-2021-training-verifiers.md) · 关系：直接源自 · 强弱：强。“生成多个候选解，由验证器排序选最优”就是 Cobbe 等 2021 年提出的做法，作者的论文也引用了它
  - [测试时算力的最优扩展](../roots/snell-2024-test-time-compute.md) · 关系：相近 · 强弱：强。“便宜模型多花推理算力，能胜过更强的模型”，和 Snell 等“测试时算力可以胜过大 14 倍的模型”几乎是同一句话；作者的论文也把它列为基础文献
  - [用大模型当裁判](../roots/zheng-2023-llm-as-a-judge.md) · 关系：直接源自 · 强弱：强。LLM-as-a-Verifier 的名字和思路都来自 LLM-as-a-judge，作者在论文引言里引用了它并做对比
- 本质：这条新知识本质上是“先生成、再验证”在用推理算力换准确率、以小博大场景下的应用：多做几份再挑出对的，因为判断对错往往比一次做对容易。
- 整理于：2026-10-18（第 1 轮）
