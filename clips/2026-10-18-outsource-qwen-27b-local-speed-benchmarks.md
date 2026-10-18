---
title: "本地跑 Qwen3.8 的提速实测"
author: "Eric ⚡️ Building... (@outsource_)"
url: https://x.com/outsource_/status/2088743329760469374
source: X
published: 2026-08-15 21:43 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

How to run Qwen 3.8 27b (Opus 4.6) At Home 🏆 
Pushing 30+ tk/s on Mac M2 Max // 97 tk/s on 4090

TL;DR: Using Codex + GPT‑5.6 SOL at xHigh reasoning, I stress-tested the new Qwen3.8‑27B across my local hardware and nearly doubled its speed through native speculative
decoding.

Hardware:

• MacBook Pro: M2 Max, 96GB unified memory
• PC: RTX 4090 24GB + 64GB RAM

The headline results:

🍎 M2 Max
BF16: 13–20 tok/s
Ollama MLX NVFP4 + native MTP: 31.5 tok/s
Medium reasoning: 24.6 tok/s

🟢 RTX 4090
No speculation: 44.9 tok/s
Optimized llama.cpp + MTP: 86.5 tok/s general
Coding workload: 97.3 tok/s

What Codex tested:

• BF16, MLX, NVFP4 and dynamic GGUF quants
• Ollama, MTPLX, oMLX, llama.cpp, vLLM and SGLang
• Unsloth UD‑Q4/Q5, Q4_K_M, Atomic and AutoRound
• MTP depths 1–8
• Full, Q8, Q4 and FP8 KV caches
• Short prompts through 262K context
• Coding, reasoning, tools and vision
• Quant quality against the BF16 reference

The biggest lessons:

1. Native MTP integration matters more than simply enabling an MTP flag.

Ollama’s adaptive MLX implementation reached 81–86% acceptance on the Mac. On the 4090, properly tuned MTP nearly doubled the raw autoregressive speed.

2. More speculation is not always faster.

The sweet spot was depth 2 on the Mac and depth 3–4 on the 4090. Going deeper added verification work and reduced performance.

3. Extra RAM increases capacity not decode speed.

The M2’s 96GB makes huge contexts possible, but memory bandwidth remains the bottleneck. PC system RAM and SSD offloading also didn’t help 4090 throughput.

4. Four-bit quantization was the practical winner.

Our best Q4 model scored 14/22 in the extended quality suite versus 15/22 for Q5, while delivering better speed and substantially more context headroom.

5. “Supports 262K context” does not mean it stays fast there.

The 4090 still produced 48 tok/s at 131K, but dropped to 4.1 tok/s at 262K. The practical sweet spot is 32K–131K depending on the workload.

Next step: fine-tuning.

We’ll build a specialized Qwen3.8‑27B using LoRA/QLoRA for coding, agents, tool use and structured reasoning—then export it back into optimized MLX and GGUF formats
while preserving vision and MTP.

The goal isn’t just another quant.

It’s a faster, stronger, locally deployable “Qwen” model around real workflows.

Two local machines. One frontier-class model. Zero cloud inference.

> 媒体：
> - https://video.twimg.com/amplify_video/2088741318835019776/vid/avc1/480x270/X7Xgcwk6VX4vRpKy.mp4?tag=29
> - https://pbs.twimg.com/media/HPyzLewXIAAOY9X.jpg
> - https://video.twimg.com/amplify_video/2088741369481224192/vid/avc1/480x270/Uab6S5CY4IE0it5n.mp4?tag=29
> - https://pbs.twimg.com/media/HPyzO_aWAAAOW0J.jpg

## 溯源

