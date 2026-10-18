---
title: "MiMo-V3 新架构让长上下文更省"
author: "Fuli Luo (@_LuoFuli)"
url: https://x.com/_LuoFuli/status/2102766365190901957
source: X
published: 2026-09-23 14:25 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

MiMo-V3 is getting a new architecture. The core of it, HySparse2, is out today.

Less prefill, a smaller KV cache, better long-context retrieval—and we got all three at once.

Compared with MiMo-V2.6's Hybrid SWA architecture:
• 5.02× lower prefill FLOPs at 1M tokens
• 4.5× smaller KV cache at 1M tokens
• Better MRCRv2 and RULER-v2 scores, plus lower AgentPPL and LongPPL

Why build a new architecture?
Agentic inference is a very different workload. Each round, a short action can return a long observation that needs to be prefilled, while the context keeps growing. That puts prefill cost, KV-cache size, and retrieval accuracy on the critical path at the same time.

HySparse2 tackles all three with two levels of KV sharing:
• KV Bridging: Following YOCO, full-attention layers in the cross-decoder build their K/V from self-decoder hidden states.
• KV Reuse: Within each hybrid block, sparse layers reuse the preceding full-attention layer's KV cache and selection indices.

Two more changes: token-level selection replaces block-level selection, and a forced window of recent tokens replaces the separate SWA branch, so local and global tokens share one KV cache. Since all cross-decoder KV caches now come from the self-decoder, prefill can stop once the self-decoder finishes.

Paper: https://t.co/REeEdd5pL7

> 媒体：
> - https://pbs.twimg.com/media/HS6GT1VWoAAYsNi.jpg

## 溯源

