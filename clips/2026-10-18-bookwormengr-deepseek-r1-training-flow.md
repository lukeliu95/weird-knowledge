---
title: "DeepSeek-R1训练流程图解"
author: "GDP (@bookwormengr)"
url: https://x.com/bookwormengr/status/1884212697023303818
source: X
published: 2025-01-28 12:11 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 模型与本地部署
roots: [guo-2025-deepseek-r1, zelikman-2022-star, reinforcement-learning-from-human-feedback]
---

## 原文

Aravind is right. DeepSeek R1 follows a very intelligent combination of Reasoning Orientated RL and SFT

Below is  DeepSeek R1's training flow diagram. Red blocks are RL and green blocks are SFT. 

They followed very intelligent approach to generate 800K high quality data pair before final SFT. With that quantity of high quality data,  they don't have to steal OpenAI/anyone's data.

Also, note 
1. for the first [model 1] RL happens without any SFT and is purely "reasoning oriented" (correctness)
2. the second [model 4] RL happens with diverse types of rewards (correctness, helpfulness, harmlessness) and is preceded by SFT.

Orignial image by @SirrahChan , improved by me.

> 媒体：
> - https://pbs.twimg.com/media/GiYPvYDagAA8qUs.jpg

## 溯源

- 核心主张：DeepSeek-R1 的训练是推理强化学习和监督微调交替进行：先不经监督微调、只按答对与否做纯推理强化学习（R1-Zero），再经冷启动微调、推理强化学习、拒绝采样自产约 80 万条高质量数据做监督微调，最后用正确性、有用性、无害性多种奖励再做一轮强化学习；有这么多自产数据，就不需要“偷”别家的数据。
- 源知识：
  - [DeepSeek-R1：用强化学习激发推理能力](../roots/guo-2025-deepseek-r1.md) · 关系：直接源自 · 强弱：强。推文画的就是 R1 论文的训练流程；论文 2.3.3 节写明约 60 万条推理数据加约 20 万条非推理数据，共约 80 万条
  - [STaR：用推理自举推理（自学推理者）](../roots/zelikman-2022-star.md) · 关系：相近 · 强弱：弱（模型复核通过）。让模型自己生成推理、只留答对的再拿去微调，正是 STaR 的做法；R1 论文没有引用它，属推断
  - [基于人类反馈的强化学习（RLHF）](../roots/reinforcement-learning-from-human-feedback.md) · 关系：直接源自 · 强弱：强。R1 论文 2.3.4 节写明第二轮强化学习用奖励模型捕捉人类偏好、沿用 DeepSeek-V3 的流程，分别评有用性和无害性，即先微调再做偏好强化学习的 RLHF 路线
- 本质：这条新知识本质上是“强化学习加自举式拒绝采样微调加 RLHF”在训练推理大模型上的组合应用。
- 整理于：2026-10-18（第 2 轮）
