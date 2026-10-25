---
title: "Qwen3.8-27B 在一张 3090 上从每秒 82 个词元提到 381 个"
author: "FHILY👑 (@Oluwaphilemon1)"
url: https://x.com/Oluwaphilemon1/status/2113912192017805321
source: X
published: 2026-10-24 08:35 UTC
saved: 2026-10-25
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: 模型与本地部署
roots: []
---

## 原文

Qwen3.8-27B reportedly reached 381 tokens/sec on a single RTX 3090 with 24GB of VRAM.

The starting point was 82 tokens/sec. That is approximately a 4.6× increase without changing the GPU or the model.

Developer TeksEdge achieved this by optimizing how the model generates, reuses and verifies tokens. The work combines speculative decoding, DFlash2, context lookup and faster verification.

Here is how the performance improved:

Baseline inference: 82 tokens/sec
Optimized MTP: 114 tokens/sec
DFlash2 + context lookup: 138 tokens/sec
Optimized lookup verification: 381 tokens/sec

The final result is especially interesting because it shows how much inference performance can depend on the software around a model.

1. Speculative decoding reduces sequential work

Autoregressive models normally generate text one token at a time. Each new token depends on the preceding output, which limits how much of the decoding process can run in parallel.

Speculative decoding changes that workflow.

A smaller or faster draft process proposes several tokens. The main model then verifies those proposals, potentially accepting multiple tokens in one verification step.

When the proposals are accepted, the system avoids some of the sequential work required by ordinary decoding.

DFlash2 is a speculative decoding approach designed to improve this process. Its effectiveness depends on how well the draft predictions match the main model’s output and how much verification costs.

2. Context lookup can reuse text instead of regenerating it

Some tasks require a model to reproduce information that already exists in its input. Examples include copying documents, transforming structured text and processing coding contexts with repeated sequences.

Context lookup searches for reusable sequences in the existing context and uses them as candidate output rather than generating every token independently.

TeksEdge reports processing blocks of up to 16 tokens and accepting roughly 15 tokens per block in its reported setup.

On a 25,000-token document reproduction task, the reported throughput increased from approximately 260 to 382 tokens/sec.

That result makes sense for workloads with substantial input-output overlap. The more output can be recovered from existing context, the more opportunities there are to avoid expensive generation steps.

Ordinary conversation is different. When the model must produce new ideas or unfamiliar wording, there may be much less text to reuse, so the improvement can be considerably smaller.

3. Faster verification helps turn those proposals into real throughput

Drafting multiple tokens is only part of the problem. The inference engine must still check the proposed output efficiently.

If verification introduces too much overhead, the extra draft work can eat into the expected speedup.

TeksEdge’s final optimization targets lookup verification. Its reported progression from 138 to 381 tokens/sec suggests that the verification stage was a major bottleneck in this particular workload.

The exact contribution of each optimization depends on the implementation and test conditions, so the 4.6× result should be treated as a workload-specific benchmark rather than a universal speedup.

4. Prefix caching tackles a different bottleneck

Speeding up token generation is not the same as reducing the wait before generation begins.

Coding agents often send the same system instructions, tool definitions and repository context across repeated requests. Processing that shared prefix again and again adds unnecessary prefill work.

Prefix caching stores reusable computations for previously processed input. When a later request shares the same prefix, the engine can reuse that work instead of recomputing everything.

TeksEdge reports reducing time to first token from 22.4 seconds to 0.56 seconds, a roughly 40× reduction in initial waiting time.
 https://t.co/AlxGxC0hoI

> 媒体：
> - https://video.twimg.com/amplify_video/2090571994471489536/vid/avc1/1920x1080/xrUnHD6qyMiZ1wMn.mp4?tag=29

## 溯源

