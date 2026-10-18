---
title: "DeepSeek-R1训练流程图解"
author: "GDP (@bookwormengr)"
url: https://x.com/bookwormengr/status/1884212697023303818
source: X
published: 2025-01-28 12:11 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind: 观点
topic: 模型与本地部署
roots: []
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

