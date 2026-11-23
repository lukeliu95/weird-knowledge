---
title: "agent 找出 Qwen3-TTS 里 417 个神经元，放大后会笑、耳语、插话（作者自测）"
author: "Tensor-Slayer (@TensorSlay)"
url: https://x.com/TensorSlay/status/2121598038821187935
source: X
published: 2026-11-14 13:36 UTC
saved: 2026-11-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 语音与数字人
roots: [zeng-2026-lazarus, takehi-2026-weight-space-programming, dai-2022-knowledge-neurons, turner-2023-activation-addition]
---

## 原文

Reprogramming dormant neurons : Qwen TTS 

Ever wondered why Qwen3-TTS sometimes breathes or laughs out of nowhere? Agent found neurons behind it.

The details: 

Agent found 417 neurons to be specific (about 0.48% of the talker's MLP neurons) and 61 of them are dormant. Amplified together, they give the following effects effect:

1. Breathes as words are spoken
2. Hushed ASMR
3. Natural laughs as language is being spoken
4. Enhanced whispering
5. 2nd speaker appearing.

Comparisons and neuron map repo in the comments below. 

Inspired by recent work on Lazarus by @DimitrisPapail , which reprogrammed dormant neurons.

> 媒体：
> - https://video.twimg.com/amplify_video/2121592953865158656/vid/avc1/1920x1080/Wrvf0QTq8B-1KDsY.mp4?tag=29

## 溯源

- 核心主张：让 agent 在语音模型 Qwen3-TTS 里找出和笑声、耳语、停顿、第二个人插话等行为相关的 417 个 MLP 神经元（其中 61 个平时很少强激活），推理时把它们一起放大，就能让这些“人声小动作”稳定出现，不用重新训练。
- 源知识：
  - [Lazarus：改写沉睡神经元给 AI agent 植入后门](../roots/zeng-2026-lazarus.md) · 关系：直接源自 · 强弱：强。推文明说受 Papailiopoulos 的 Lazarus 启发，仓库 README 致谢也写 arXiv 2611.15118；借的是“沉睡神经元可以单独改写”这个思路，用途从植入后门换成调语音表现力。Lazarus 2026-11-11 挂出，早于推文（11-14）。两边“沉睡”的定义不同，见证据。
  - [权重空间编程（小模型权重读写实验）](../roots/takehi-2026-weight-space-programming.md) · 关系：相近 · 强弱：弱（模型复核通过）。串推回复里有人问“这是不是权重空间编程”，作者答这是最接近的叫法，但他更愿意叫“神经元空间编辑”；两者都是让前沿模型（这里是 Opus）直接分析、改写另一个网络的权重或激活。（主会话：作者是被问到才认可这个叫法，不算明说引用，降为弱，交第二个模型复核）
  - [预训练 Transformer 里的知识神经元](../roots/dai-2022-knowledge-neurons.md) · 关系：相近 · 强弱：弱（模型复核通过）。知识神经元论文先找出“表达某个事实”的少数前馈层神经元，把激活加倍就让模型更倾向说出这个事实；这里把“事实”换成笑、耳语这类语音行为，找神经元再放大的套路一样。作者没引，是推断。
  - [激活工程：用激活加法引导语言模型（ActAdd）](../roots/turner-2023-activation-addition.md) · 关系：相近 · 强弱：弱（模型复核通过）。仓库 reproduce.py 用 forward hook 在推理时往 MLP 输出上加一个固定方向 d_L（乘上所选神经元的激活），不训练、不改别处，这就是激活工程（激活引导）的做法；作者没引，是推断。
- 本质：这条新知识本质上是“改写沉睡神经元”（Lazarus）和激活引导的思路，在语音合成模型表现力控制上的应用，由 agent 自己做神经元搜索。
- 整理于：2026-11-23（第 12 轮）
