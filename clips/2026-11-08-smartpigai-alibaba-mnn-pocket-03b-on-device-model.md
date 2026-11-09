---
title: "阿里 MNN-Pocket-0.3B：173MB 的端侧小模型"
author: "Smartpig (@Smartpigai)"
url: https://x.com/Smartpigai/status/2119011734199709779
source: X
published: 2026-11-07 10:19 UTC
saved: 2026-11-08
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 模型与本地部署
roots: []
---

## 原文

不是，别人还在卷千亿参数，阿里反手把一个 AI 大模型塞进了 173MB？？？

最近看到阿里 MNN 团队开源的 MNN-Pocket-0.3B，这次真把端侧 AI 玩出点东西了。

模型只有 3 亿参数，但官方公布的数据挺猛：

173MB：INT4 量化后的模型体积
466 tokens/s：iPad Pro M5 上使用 Metal 的解码速度
32K 上下文：支持较长文本输入
中英双语：11 项评测平均分 50.00，在官方对比中超过部分 5 亿参数级模型

不过，我觉得真正值得关注的不是它有多小，而是它从模型架构到推理引擎，都在为端侧部署做优化。

28 层 Transformer，GQA 只保留 2 个 KV Heads，减少 KV Cache 开销。

再配合 INT4（W4A16）量化感知训练（QAT），把模型压到 173MB，11 项评测平均分仅从 50.00 降到 49.59。

这意味着它不是简单把大模型强行压缩，而是在模型质量、内存占用和推理速度之间做了一次比较完整的工程优化。

更有意思的是，项目还提供了一个 MNN-Pocket-0.3B-Dec 版本，使用 LoRA Adapter + Pointer Head，尝试在一次前向传播中完成决策，而不是逐 Token 生成。

这个方向很适合研究端侧 Agent 的轻量决策能力。

当然，3 亿参数不可能替代 Claude、GPT 这种前沿模型，复杂推理和长代码生成也不是它的强项。

但为什么手机上的简单意图识别、信息提取、设备控制，都要请求云端的大模型？

有些任务，本来就应该在本地完成。

我觉得端侧 AI 很可能会走向一种分工：小模型负责高频、低延迟的本地任务，大模型负责复杂推理。

MNN-Pocket 正好展示了这条路线的潜力。

Apache 2.0 开源，支持 MNN、Transformers 和 llama.cpp。

权重：https://t.co/v8RH5ycq8e

> 媒体：
> - https://pbs.twimg.com/media/HWg97V8a0AEnMo4.jpg

## 溯源

