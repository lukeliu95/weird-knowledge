---
title: "单张 5090 跑 Qwen3.8 Flash-Next 解码 150 tok/s：靠 Strata 引擎和 IQ3_S 量化"
author: "Kyle Hessling (@KyleHessling1)"
url: https://x.com/KyleHessling1/status/2105029750419005856
source: X
published: 2026-09-29 20:19 UTC
saved: 2026-10-21
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

Just got 150 tok/s decode with Qwen3.8 Flash-Next on a single 5090. All thanks to Niko1221's Strata engine and the ISTA Lab IQ3_S quant!

1× 5090 + 128 GB DDR5 (non-ideal 4-stick dual-channel), single stream:

150 tok/s decode for programming
130 tok/s median on mixed prompts (~100 on long prose)
4,150 tok/s prefill at 43K
full 262K context, 114 tok/s at 196K depth

5.4× the speed of my best hybrid llama.cpp run.

Per ISTA-DASLab's evals, their IQ3_S quant is at parity with BF16 on AIME25/GPQA/LCB, and it's holding up surprisingly well in my own tests!

Engine: https://t.co/G1YJ8623ks
Quant: https://t.co/IB4RnrwIKf

## 溯源

