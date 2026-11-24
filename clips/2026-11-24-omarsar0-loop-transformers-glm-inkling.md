---
title: "循环 Transformer：不加参数也能加深推理，GLM 和 Inkling 2 Mini 都在用"
author: "elvis (@omarsar0)"
url: https://x.com/omarsar0/status/2124889845474476538
source: X
published: 2026-11-23 15:36 UTC
saved: 2026-11-24
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

Don't sleep on Loop Transformers. 

Really interesting decision by GLM to move to loop transformers as well. TM's Inkling 2 Mini is also a looped transformer. 

Looped transformers offer parameter efficiency when scaling to deeper networks.

In practical terms, this means adding more reasoning depth (potentially increasing capability) without adding more weights. 

The team didn't pre-train from scratch; they adapted an already pre-trained base model into a Loop Transformer through continued training.

> 媒体：
> - https://pbs.twimg.com/media/HX0ddtjX0AECxBx.jpg

## 溯源

