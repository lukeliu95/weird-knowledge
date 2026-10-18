---
title: "智谱CogView4：会写汉字的文生图"
author: "Orange AI (@oran_ge)"
url: https://x.com/oran_ge/status/1896787355815862582
source: X
published: 2025-03-04 04:58 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 图像生成
roots: []
---

## 原文

2025年AI行业的一个大主题是开源，上周DeepSeek连续六天开源直接引爆了开源的热潮，也唤醒了智谱的开源基因，直接把2025定位开源年，要和开源社区一起往前冲。

智谱2025开源年第一弹是 CogView4-6B：业界首个能生成汉字的开源文生图模型。

以前的文生图模型，基本都是使用英文作为提示词，如果用户输入中文，那就先翻译成英文再传给模型。

这次智谱把模型的 T5 encoder 换成了自家的 GLM-4 encoder，支持了中英双语输入，也让模型具备了输出汉字的能力。

同时也大幅提升了模型对中文提示词的理解，比如古诗文中的意境。（prompt：野径云俱黑，江船火独明）

除了汉字输出能力，模型在权威的 DPG-Bench 中综合评分排名第一，在开源文生图模型中达到 SOTA。

除此之外，CogView4-6B 还支持输入任意长度超复杂提示词，能够生成任意分辨率的图像。

> 媒体：
> - https://pbs.twimg.com/media/GlK8L-9a0AAyUWW.jpg
> - https://pbs.twimg.com/media/GlK8L_nWYAAtbpw.jpg
> - https://pbs.twimg.com/media/GlK8OWEXkAAr99D.jpg
> - https://pbs.twimg.com/media/GlK8PozWIAAVHyq.jpg

## 溯源

