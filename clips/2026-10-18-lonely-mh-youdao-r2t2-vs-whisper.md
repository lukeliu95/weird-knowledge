---
title: "有道 R2T2 对比 Whisper"
author: "Lonely (@Lonely__MH)"
url: https://x.com/Lonely__MH/status/2102631279686824086
source: X
published: 2026-09-23 05:28 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 语音与数字人
roots: []
---

## 原文

🎉见证历史！国产开源大模型直接登顶 Hugging Face 双榜第一！

刚刷到网易有道开源的实时流式语音大模型：Confucius4-R2T2 ，基于 Qwen3-ASR-1.7B 微调

另外顺带把流式翻译模型 T3PO 一起开源了

刚发布就同时斩获 HF ASR 与 Translation 两大细分垂类的 Trending 榜一，太燃了🔥

为了测测到底有多硬核，我把 R2T2（1.7B / GGUF 约 2.2GB）直接部署在自己的 MacBook Pro M2 上，跟行业老大哥 OpenAI Whisper-Large 做了对比

视频画面反差极其强烈（重点看 0:21 秒高能👇）

🔥几个比较有意思的点：

1. 前缀稳定（独创 Stable Prefix 只增不改）
增量重识别下，已输出文本基本只追加、不回改。 
50 秒英文音频、2.5 秒步进：已出文本被改写 Whisper 16 次，R2T2 1 次；等效退格 1137 vs 39 字符。

2. 截断处不补全
音频切在半句时，只输出有声学证据的部分，不靠语言模型先验去猜后文。 
中文改口指令：Whisper 出现繁体和错字，R2T2 零改写。对下游 LLM / Agent 来说，前缀可以直接消费

3. 端侧可部署
1.7B，Q8_0 GGUF 约 2.2GB，llama.cpp + Metal 在 16GB M2 Pro 上本地推理。 
官方 vLLM 方案需要 N 卡，Mac 走 GGUF 即可。

模型👉🏻  https://t.co/tIRbqpI6Nf

代码👉🏻  https://t.co/YQkxGi7px3

适合本地部署，做语音输入法、实时字幕、会议助手

有需要的，可以试试。

以上。

> 媒体：
> - https://video.twimg.com/amplify_video/2102631173809938432/vid/avc1/386x270/vREq1LvfeFEC7htY.mp4?tag=29

## 溯源

