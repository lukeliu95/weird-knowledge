---
title: "Qwen3.8-27B 在单张 3090 上从 82 提到 381 token/秒"
author: "FHILY👑 (@Oluwaphilemon1)"
url: https://x.com/Oluwaphilemon1/status/2113065079667118410
source: X
published: 2026-10-22 00:29 UTC
saved: 2026-10-23
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: 模型与本地部署
roots: []
---

## 原文

Qwen3.8-27B reportedly jumped from 82 to 381 tokens/sec on a single RTX 3090 with 24GB VRAM.

That’s a 4.6× increase without changing the GPU or the model.

The developer, TeksEdge, achieved this by optimizing the inference stack rather than upgrading the hardware.

Here’s how the reported performance improved:

Baseline: 82 tokens/sec
Optimized MTP: 114 tokens/sec
DFlash2 + context lookup: 138 tokens/sec
Optimized lookup verification: 381 tokens/sec

Three techniques explain the improvements.

1. Speculative decoding

Normally, a language model generates tokens sequentially, with each new token depending on the previous ones.

Speculative decoding introduces a faster drafting process that proposes multiple tokens for the main model to verify. When several proposals are accepted, the system can generate more output per verification cycle.

In this experiment, optimized MTP increased throughput from 82 to 114 tokens/sec. Adding DFlash2 and context lookup pushed it to 138 tokens/sec.

2. Context lookup

Why generate text from scratch when the same text already exists in the input?

Context lookup identifies sequences that can be reused and proposes them for verification instead of generating every token individually.

The reported implementation processed blocks of up to 16 tokens, accepting roughly 15 per block.

On a 25,000-token document reproduction task, throughput reportedly climbed from around 260 to 382 tokens/sec.

There’s a catch: this technique works particularly well when the output resembles existing text. Open-ended conversations generally offer fewer opportunities for reuse.

3. Prefix caching

Coding agents frequently resend identical system instructions, repository context, and code snippets across multiple requests.

Prefix caching stores reusable computations from previously processed prompts, reducing the work required when those same prefixes appear again.

In TeksEdge’s reported test, time to first token fell from 22.4 seconds to just 0.56 seconds.

That’s approximately a 40× reduction in initial waiting time.

For agents working with large codebases, this can make repeated interactions substantially more responsive.

One important distinction: 381 tokens/sec isn’t ordinary chat performance.

The developer reports around 133 tokens/sec for regular chat. The higher figure comes from a workload that benefits heavily from context reuse and optimized verification.

Those numbers measure different conditions, so they shouldn’t be treated as interchangeable.

The interesting part is that the RTX 3090 didn’t change. The model didn’t change either.

The improvement came from making the inference stack do less redundant work and verify proposed tokens more efficiently.

Local AI performance isn’t determined by GPU specifications alone. The software running on that hardware can make a substantial difference.

Project: TeksEdge’s Qwen3.8-27B RTX 3090 implementation. https://t.co/AlxGxC0hoI

> 媒体：
> - https://video.twimg.com/amplify_video/2090571994471489536/vid/avc1/1920x1080/xrUnHD6qyMiZ1wMn.mp4?tag=29

## 溯源

