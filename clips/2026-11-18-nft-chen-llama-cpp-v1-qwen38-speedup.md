---
title: "llama.cpp v1.0.0 发布，Qwen3.8-27B 推理提速近一倍"
author: "SuSu_酥酥👅 (@NFT_Chen)"
url: https://x.com/NFT_Chen/status/2121538580300574883
source: X
published: 2026-11-14 09:39 UTC
saved: 2026-11-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

🔥哇塞！本地AI新高度！llama.cpp v1.0.0正式落地，Qwen 3.8-27B 推理翻倍加速！ 

v1 核心亮点是MoE offloading + 智能LRU缓存，大MoE即使放不下VRAM也能高速跑。结合Qwen3.8-27B（Dense + 内置MTP），性能提升直接拉满！

Qwen3.8-27B 关键性能亮点（llama.cpp v1.0.0）：
🔹MTP投机解码正式升级（NextN API进主头）：单卡RTX 5090上从~74 tok/s飙到134 tok/s（约1.8x），质量100%保留，代码/数学场景更炸。

🔹FP8 / 量化KV缓存：用--cache-type-k/v q4_0或f8_e4m3，内存更低、速度反而更快（实测比f16还快），消费级16GB卡轻松开到64K-256K上下文。

🔹Unsloth Dynamic V3.1 GGUF：同体积精度更高5-10%，12-19GB卡即可流畅跑多模态+长上下文。

🔹整体更稳：新Web UI、Server安全加固、更好MoE专家缓存，本地部署体验质变。

快速使用：
1️⃣更新到llama.cpp v1.0.0（或最新binary）。

2️⃣下载模型：hf download unsloth/Qwen3.8-27B-GGUF（推荐UD-Q4_K_M或XL）。

3️⃣启动示例：
llama-server -m Qwen3.8-27B-UD-Q4_K_M.gguf -ngl 99 -fa on -c 32768 \
  --cache-type-k q4_0 --cache-type-v q4_0 \
  --spec-type draft-mtp --spec-draft-n-max 

Release：https://t.co/raarR83Dik
 官方博客：https://t.co/gsr8yAbeFT

#llamacpp #Qwen3827B #LocalAI #Unsloth #本地大模型 #AI #阿里巴巴

> 媒体：
> - https://pbs.twimg.com/media/HXE4F0JaEAAmzAM.jpg
> - https://pbs.twimg.com/media/HXE4F0HbEAAEmGI.jpg

## 溯源

