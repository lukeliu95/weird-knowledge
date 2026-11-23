---
title: "Hugging Face 开源 256M 视频理解模型 SmolVLM2"
author: "明子206 (@mingzi206)"
url: https://x.com/mingzi206/status/2122894386161918301
source: X
published: 2026-11-18 03:27 UTC
saved: 2026-11-19
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 模型与本地部署
roots: []
---

## 原文

让 AI 边看视频边理解，门槛终于被一脚踹到了地板上！

Hugging Face 刚开源了目前全世界体积最小的视频多模态模型：SmolVLM2-256M

很多人以为给 AI 装上“眼睛”去读长视频，动不动要吞几十 GB 显存。这个仅有 256M（约 0.25B）参数的小家伙，直接把配置要求杀到了极限：

· 只要 1.38GB 显存：无论是轻薄本、手机端、树莓派还是几年前的老旧显卡，不到 1.5G 显存就能直接在本地完成视频推理！
· 专职“看视频”而非“生成视频”：吃进一段视频、一组连续帧或游戏屏幕录屏，它能实时用自然语言理解剧情、描述动作、做视觉问答（VQA）以及 OCR 文字提取。
· 跑分扎实的小钢炮：Video-MME 达到 33.7，MLVU 达 40.6，对于一个只有 256M 的模型来说，这理解能力相当凶悍。
· 开箱即用全免费：Apache 2.0 纯开源协议，GGUF 量化版也已经就绪，拉进 Ollama 或者 llama.cpp 就能单机离线跑。

拿来做实时游戏画面的屏幕助手、本地监控动作识别，或者挂在低算力边缘设备上，简直是神仙底座。

想在千元机或轻薄本上折腾“视频视觉 Agent”的兄弟，这个微型模型建议先存一份备用！

👉 模型地址与 GGUF 入口见评论区一楼

#AI #开源 #HuggingFace #大模型 #多模态

> 媒体：
> - https://pbs.twimg.com/media/HXYJH-9aMAE4ygu.jpg

## 溯源

