---
title: "作者称：用筛选客服案例加 LoRA，让本地 Qwen 接近 Opus（未给对照评测）"
author: "Simon Høiberg (@SimonHoiberg)"
url: https://x.com/SimonHoiberg/status/2120132843669979347
source: X
published: 2026-11-10 12:33 UTC
saved: 2026-11-11
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 模型与本地部署
roots: [hu-2021-lora, knowledge-distillation]
---

## 原文

You can now get Opus 5.5 quality out of Qwen 3.8 27B.

You just have to teach it the job first.

We let a frontier model work through thousands of realistic support cases, keep only the ones that meet our standard, and train a small LoRA on Qwen with them.

Now it runs on our own hardware. No API bill, no rate limits, and nobody can change the deal on us 👇

> 媒体：
> - https://video.twimg.com/ext_tw_video/2120132759221932033/pu/vid/avc1/1280x720/kJ0CyJ5zyJncr8tf.mp4?tag=12

## 溯源

- 核心主张：作者称让前沿模型生成数千个客服案例，按自定标准筛选，再用 LoRA 微调本地 Qwen；这是教师输出训练和低秩适配的组合。“达到 Opus 5.5 质量”未附可核对的留出测试集、指标或对照结果，只能保留为作者对特定客服任务的自述。
- 源知识：
  - [LoRA：大语言模型的低秩适配](../roots/hu-2021-lora.md) · 关系：直接源自 · 强弱：强。原文明说训练 LoRA；Hu 等2021年论文第4.1节定义冻结原权重、学习低秩更新矩阵的适配方法。该机制不保证微调后整体能力等于教师模型。
  - [知识蒸馏](../roots/knowledge-distillation.md) · 关系：直接源自 · 强弱：弱（模型复核通过）。用前沿模型的输出教较小模型，符合教师向学生迁移能力的思路；但原帖只说筛选生成案例，未提供2015年论文所用温度软目标或损失函数，不能当成那套具体算法的直接复现。
- 本质：这条新知识本质上是教师生成并筛选任务示例，再通过低秩适配把特定做法迁移到本地模型；本地推理省掉外部逐次调用账单，也仍有硬件、训练、运维和能力验证成本。
- 整理于：2026-11-14（第 11 轮）

### 第11轮核查边界

- 原帖的数千案例和接近Opus效果是作者自述；未读附带视频或取得留出测试集、训练配置与对照指标。LoRA及教师案例方法可解释机制，不能证明效果等同。

出处和阅读范围见[本轮证据记录](../docs/reviews/2026-11-14-round-11-evidence.md)。
