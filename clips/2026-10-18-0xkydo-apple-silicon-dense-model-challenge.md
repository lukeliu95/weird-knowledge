---
title: "Mac 跑稠密模型：持续优化挑战赛"
author: "Kydo (@0xkydo)"
url: https://x.com/0xkydo/status/2088709460701458437
source: X
published: 2026-08-15 19:28 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 模型与本地部署
roots: []
---

## 原文

Apple Silicon is built for MoE models -- huge unified memory, modest bandwidth. Dense models are the opposite: bandwidth-bound, and everyone "knows" Macs are slow at them.  

Today we're changing that. https://t.co/liyzSFqLAa is now improving Qwen3.8 27B from @QwenDevs. Under 16 hours in: +153% over baseline. 2.5x faster than out of the box MTP decode.  

I think that's barely the start. When a belief is that widely held (Mac is slow at dense models), few has gone looking. The low-hanging fruit is still there.  

We've improved based on feedback from the last challenge.

- MTP on day 1. Speculative decoding is the whole game for dense models, and the draft head weights are yours to edit. 
- 8 hidden length, not 1. Laguna's score overfit a single 512-token fixture. Now every run is the median across eight weights. 
- New leaderboard. Ranks total improvement contributed, not who happens to hold the record right now. The old view lives on as the lineage board (better name welcome). 
- Automated review. Every submission gets screened for benchmark gaming before it scores.  

Next up: enabling multiplatform starting with CUDA.

> 媒体：
> - https://video.twimg.com/amplify_video/2088709395383549952/vid/avc1/480x270/XdySr3BTm-Z_2sM9.mp4?tag=29

## 溯源

