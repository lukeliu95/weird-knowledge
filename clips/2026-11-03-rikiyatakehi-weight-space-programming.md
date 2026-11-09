---
title: "权重空间编程：直接改权重，修复小模型推理循环（作者实验）"
author: "Rikiya Takehi (@rikiyatakehi)"
url: https://x.com/rikiyatakehi/status/2117313742891327994
source: X
published: 2026-11-02 17:51 UTC
saved: 2026-11-03
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 模型与本地部署
roots: [takehi-2026-weight-space-programming]
---

## 原文

We asked GPT-6 Astra to edit Qwen3.5-0.8B weights to improve math.
It directly changed only 0.016% of weights, fixing 0.8B's reasoning loops & improving math up to 6x and even instruction following 3x, without gradients or training.

We call this Weight-Space Programming: frontier LLMs can now natively read/write neural network weights! 🧵
Blog: https://t.co/bOWCcFhCVq

> 媒体：
> - https://pbs.twimg.com/media/HWI1oKUWUAAWoZp.jpg

## 溯源

- 核心主张：作者让前沿模型分析、直接修改小模型权重，在所报 Qwen3.5-0.8B 实验里主要通过解除推理循环恢复表现；不用梯度训练不等于不用数据和计算：数学实验使用练习题、Python 和最多 50 次前向反馈。对本来少循环的 Gemma 3 270M，没有显示出同样的数学提升。
- 源知识：
  - [权重空间编程（小模型权重读写实验）](../roots/takehi-2026-weight-space-programming.md) · 关系：直接源自 · 强弱：强。原推就是作者同名研究的发布。作者报告 MATH-500 正确率由 7.9% 到 48.1%，约 6 倍是这个特定设置下的比值；不是所有模型能力普遍提高 6 倍。
- 本质：这条新知识本质上是让模型把已有网络权重当作可读写程序，并利用少量反馈修正特定行为；目前证据支持修复某些已定位故障，不能外推成普遍的无训练能力增长。
- 整理于：2026-11-09（第 10 轮）
