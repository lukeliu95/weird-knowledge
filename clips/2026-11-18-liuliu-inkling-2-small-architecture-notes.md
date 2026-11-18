---
title: "Inkling 2 Small 模型结构里的几个新做法"
author: "Liu Liu (@liuliu)"
url: https://x.com/liuliu/status/2121330134112428216
source: X
published: 2026-11-13 19:51 UTC
saved: 2026-11-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

Am I in the wrong twittersphere and why nobody talks about Inkling 2 Small? You can download it since yesterday, and it has some interesting bits. People analyze Chinese models for interesting bits such as DeepSeek Sparse Attention / HCA / Attention Residual / mHC / iHC, but why not Inkling 2 Small? Anyway, here are some interesting findings:
1. Attention Residuals: Inkling 2 Small uses Attention Residuals, the model itself is still not on the very deep side (Hy4 is 78 layers) and Inkling 2 Small is 48. The attnres covers 8 blocks (each of 6 layers).
2. new sink / gated attention. We've seen the sigmoid gated attention before (from Qwen 3 days?), but I don't think I see the new attention sink before. It is per-head projected value (so it is per-token per-head), not just per-head constant.
3. Of course, it carries over what already there in Inkling: relative biases, short conv (canon layer from Physics of Language Models days?), soft caps with tanh (hmm, this is not in Inkling 1, but pretty normal nowadays to avoid activation blow-up I think) etc.
Did I miss anything @cHHillee?
https://t.co/GCXOVALCRX

## 溯源

