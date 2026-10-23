---
title: "Qwen3.8-27B 无损量化版：24GB 起，EAR 98–99%"
author: "SuSu_酥酥👅 (@NFT_Chen)"
url: https://x.com/NFT_Chen/status/2113228486399902153
source: X
published: 2026-10-22 11:18 UTC
saved: 2026-10-23
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 模型与本地部署
roots: []
---

## 原文

🔥厉害了！27B 砍到 24GB，却几乎和原版一模一样！Qwen3.8-27B 的无损量化版，三档仅 23.7–30.5GB，EAR 高达 98–99%！

主要亮点：
🔹EAR 直接衡量与原版下一 token 概率的重叠，99% 基本等于统计上分不开。

🔹敏感层更高精度，激活保持 BF16，专为最小体积保最高保真。

🔹vLLM + Humming 即开即用，Apache 2.0，GGUF 下周到。

快速上手：
1️⃣装 vLLM + humming-kernels

2️⃣vllm serve kaitchup/Qwen3.8-27B-SLQ-EAR99 --quantization humming --dtype bfloat16 --max-model-len 262144

3️⃣直接调 OpenAI 接口

4️⃣需要工具/推理再加 parser

集合：https://t.co/EQJCsUddyg
 推荐 EAR99：https://t.co/ax2N7QndIv 
#Qwen38 #LocalLLM #vLLM #量化 #开源 #Alibaba #中国模型

> 媒体：
> - https://pbs.twimg.com/media/HVOyGBSbQAA3dcW.jpg
> - https://pbs.twimg.com/media/HVOyGBUakAASZF0.jpg
> - https://pbs.twimg.com/media/HVOyGBPaUAAQAe-.jpg

## 溯源

