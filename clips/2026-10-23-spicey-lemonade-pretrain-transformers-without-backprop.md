---
title: "不用反向传播预训练 Transformer，验证损失反超 Adam"
author: "spicylemonade (@spicey_lemonade)"
url: https://x.com/spicey_lemonade/status/2113375116528877668
source: X
published: 2026-10-22 21:01 UTC
saved: 2026-10-23
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 学习与研究
roots: [rumelhart-1986-backpropagation, salimans-2017-evolution-strategies]
---

## 原文

WE DID IT! We can now pretrain transformers without backprop and even beat backprop+Adam on validation loss with insane speeds.

Now the big question is scale. It’s Ironic, we have reached a breakthrough In AI capability due to inspiration from a safety blog

## 溯源

- 核心主张：不用反向传播、只靠前向计算（零阶优化）也能预训练 Transformer，在小规模实验里验证损失还超过了反向传播加 Adam；能不能扩到大规模还不知道。
- 源知识：
  - [反向传播（用误差反传学习表示）](../roots/rumelhart-1986-backpropagation.md) · 关系：挑战 · 强弱：强。推文的主张就是“不用反向传播”也能预训练，而且在验证损失上超过反向传播加 Adam，直接挑战 1986 年以来训练神经网络的标准做法。
  - [演化策略：强化学习的可扩展替代](../roots/salimans-2017-evolution-strategies.md) · 关系：直接源自 · 强弱：强。这条推文引用的 Samip（Q Labs）推文明说这是零阶优化、方法叫 Dust（引用推文没存进这条新知识的原文，建议补上）；Q Labs 的 Dust 页面把 Salimans 等 2017 列为权重扰动演化策略的源头，Dust 改成在激活上加噪声（节点扰动），按损失变化反推梯度。
- 本质：这条新知识本质上是零阶优化（演化策略、节点扰动：给网络加随机扰动、看损失变化来估计梯度）在 Transformer 预训练上的一次小规模尝试，挑战的是反向传播。Q Labs 页面上的实验只到 2.4 亿参数、两千万 token 以内，“超过反向传播”部分靠外推，作者自己也说算力效率还差几个数量级，回复里有人质疑训练久了会停滞。
- 整理于：2026-10-24（第 6 轮）
