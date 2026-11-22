---
title: "NVIDIA 论文：推理一次转成 CPU 代码，同类题便宜 16～291 倍"
author: "Rohan Paul (@rohanpaul_ai)"
url: https://x.com/rohanpaul_ai/status/2124177125247013266
source: X
published: 2026-11-21 16:24 UTC
saved: 2026-11-23
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
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

