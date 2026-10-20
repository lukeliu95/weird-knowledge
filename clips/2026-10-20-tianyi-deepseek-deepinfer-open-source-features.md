---
title: "DeepSeek 开源推理框架 DeepInfer 的功能清单"
author: "Tianyi Cui (@tianyi)"
url: https://x.com/tianyi/status/2112471106426900677
source: X
published: 2026-10-20 09:08 UTC
saved: 2026-10-20
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 模型与本地部署
roots: []
---

## 原文

DeepSeek just open sourced its high-performance, large-scale inference framework DeepInfer in Apache-2.0 license.

https://t.co/W2cfi6O9LO

Supported features:

- Optimized kernels, model and sampler runtime
- Parallelism: Attention DP / balanced CP, MoE EP + EPLB
- DSpark and confidence-scheduled verification
- SWA bounded replay
- Asynchronous scheduling (zero-overhead batch scheduler)
- Batch-invariant inference
- Deterministic sampling
- Structured output

## 溯源

