---
title: "NVIDIA 优化 vLLM：Kimi K3 每用户每秒 423 个 token"
author: "SemiAnalysis (@SemiAnalysis_)"
url: https://x.com/SemiAnalysis_/status/2111627094878790023
source: X
published: 2026-10-18 01:15 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 模型与本地部署
roots: []
---

## 原文

BREAKING NEWS🚨: NVIDIA has just achieved 423 tok/s/user 🚀 on the 2.8T Parameter Kimi K3 model via a new upstream vLLM optimization. 1.68x Faster on the Same Hardware!

This was done by NVIDIA CentML's Benjamin, who wrote NVIDIA's new decode-specialized kernels in Cute DSL via aggressive Megakernel fusion. This is a 12,000 LoC Megakernel and is the future of advanced AI-assisted kernel generation. NVIDIA is already working on DeepSeekv4.1 and other models for vLLM too.

Someone should give this NVIDIA 10x engineer a raise for this great new major feature!

> 媒体：
> - https://pbs.twimg.com/media/HU4Bpw9XoAIjPm2.jpg

## 溯源

