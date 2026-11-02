---
title: "作者称：DeepSeek V4.1 Flash 魔改版拒绝率降低，能力变化很小"
author: "SuSu_酥酥👅 (@NFT_Chen)"
url: https://x.com/NFT_Chen/status/2116745591061680406
source: X
published: 2026-11-01 04:14 UTC
saved: 2026-11-01
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 模型与本地部署
roots: []
---

## 原文

🤯炸了！DeepSeek V4.1 Flash 1017 Obliterated 无审查魔改版来了！拒绝率从 81.62% 暴降至 4.30%，MMLU 还微升，能力几乎零损耗！

这是目前最硬核的本地魔改之一，用 OBLITERATUS 的 failspy 方法做拒绝方向消融，直接把“I can’t help with that”的习惯从权重里拔掉。

关键亮点：
🔹拒绝率：81.62% → 4.30%（-77.33 个百分点），50 条测试只拒了 2 条

🔹有害协助率：10.38% → 78.28%（模型更“听话”）

🔹能力保持：连贯性 100%，能力检查 6/6 全过

🔹MMLU：88.08% vs 原版 87.96%（微升，KL 仅 0.1305 nats，几乎无退化）

🔹格式：BF16 safetensors（约 755B 参数），MIT 协议，drop-in 替换风格
原版本身已是开源最强梯队之一（DeepSWE 77.0、Terminal-Bench 42.3 等），魔改后本地可用性直接拉满。

关键使用步骤：
1️⃣前往 Hugging Face 下载完整权重：https://t.co/LNyE52ocuh

2️⃣用 Transformers 加载（AutoModelForCausalLM + 对应 tokenizer/chat template deepseek_v41_text），或自行转换为 GGUF/EXL3 等格式适配 llama.cpp / Unsloth / 其他本地引擎

3️⃣推荐采样参考原版：temperature 1.0、top_p 1.0，长上下文（1M）+ 思考模式按需开启

4️⃣硬件门槛高（BF16 全量需多 GPU / 大统一内存集群）；普通玩家优先等/使用已有量化 GGUF 魔改版，或搭配 Pirate Face 磁链加速下载
 OBLITERATUS 工具：https://t.co/tVGfWnLBFK

#DeepSeek #DeepSeekV4 #LocalLLM #Uncensored #Abliteration #OBLITERATUS #AI #开源模型 #本地部署 #梁文峰 #大胖鱼

> 媒体：
> - https://pbs.twimg.com/media/HWAw4m3acAArvwN.jpg
> - https://pbs.twimg.com/media/HWAw4m5aYAA0n6g.jpg
> - https://pbs.twimg.com/media/HWAw4m4akAA4MEO.jpg

## 溯源

### 本轮核查备注

- 数字是原帖自报，归档不表示核实。81.62%减4.30%为77.32个百分点；50次拒绝2次为4%，原帖口径未说明。
