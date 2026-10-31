---
title: "Bonsai 2 三值量化：Qwen3.8-27B 从 55.6GB 压到 5.9GB"
author: "FHILY👑 (@Oluwaphilemon1)"
url: https://x.com/Oluwaphilemon1/status/2115961874479018293
source: X
published: 2026-10-30 00:19 UTC
saved: 2026-10-31
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

Qwen3.8-27B reportedly shrank from 55.6GB to just 5.9GB while retaining 98.2% of its aggregate benchmark performance.

That’s an approximately 89.4% reduction in model size, according to PrismML, the team behind Bonsai.

Here are the reported numbers:

Original Qwen3.8-27B: 55.6GB
Bonsai 2 compressed version: 5.9GB
Aggregate benchmark performance retained: 98.2%
Previous Bonsai 27B version: approximately 95% retention
Evaluation coverage: 20 benchmarks

The compression technology behind this is ternary quantization.

Traditional model weights use numerical values represented at different levels of precision. Ternary quantization takes a much more aggressive approach, representing weights using three possible values, typically -1, 0 and +1, alongside scaling factors.

This drastically reduces the number of bits needed to store the model.

But shrinking weights is only half the challenge. The real difficulty is preserving the information they contain.

Push quantization too far and the model can lose important distinctions that affect reasoning, coding, instruction following and other tasks.

Bonsai 2 reportedly improves on the previous version in areas such as:

Coding agents
Multimodal reasoning
Long-horizon tool use

The agentic capabilities are particularly interesting.

An AI coding agent might need to inspect an entire codebase, understand dependencies, edit several files, execute tests, interpret errors and repeat the process until the task is complete.

Maintaining those abilities after such aggressive compression is more significant than simply preserving performance on short question-and-answer benchmarks.

Why this matters for local AI

A 5.9GB model is much easier to distribute and store than a 55.6GB version.

It could make larger models more accessible to people running local inference on consumer GPUs, laptops and other memory-constrained systems.

There is an important distinction, though: 5.9GB is the reported model size, not the total memory required to run it. Runtime memory also depends on the KV cache, context length, activations and inference-engine overhead.

The 98.2% figure also represents aggregate performance across 20 benchmarks. It doesn’t mean the compressed model performs identically on every task. Some capabilities may retain more accuracy than others, which is why independent evaluations matter.

Still, moving from approximately 95% retention in the previous Bonsai version to 98.2% with Bonsai 2 is a notable reported improvement.

If independent testing confirms these results, this could make models that previously required substantial hardware much more practical to run locally.

The real test for compression is not how small the model becomes. It’s how much of its useful capability survives the reduction.

## 溯源

