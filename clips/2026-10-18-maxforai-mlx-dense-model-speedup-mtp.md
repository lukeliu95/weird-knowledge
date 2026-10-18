---
title: "MLX 优化让 Mac 跑稠密模型更快"
author: "Max For AI (@MaxForAI)"
url: https://x.com/MaxForAI/status/2088809554255720651
source: X
published: 2026-08-16 02:06 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

终于又有团队来优化在MLX上跑模型了！

做 MLX 推理优化的 @0xkydo  刚刚宣布，他们正在用 https://t.co/XfYpH0psPy 优化 Qwen3.8 27B。

结果有点夸张：
相比原来的 baseline，整体性能已经提升约 153%。

同时如果打开 Qwen3.8 自带的 MTP，解码速度可以直接做到约 2.5 倍。

更重要的是，Qwen3.8 27B 是 Dense 模型。

一直以来，Apple Silicon 都被认为非常适合跑 MoE。

原因也很简单：Mac 最大的优势是 Unified Memory，可以用相对低的成本获得巨大的统一内存，但内存带宽有限。

MoE 每个 token 只激活一部分参数，因此特别适合这种架构。

Dense 模型每生成一个 token，都需要处理完整模型权重，结果就是模型虽然能塞进 Mac，跑起来却不快。

这几乎已经成了本地模型社区的共识。

但 Kydo 这次证明了：Mac 跑 Dense 慢，可能并不是 Apple Silicon 天生不行，而是过去的软件栈没有把它优化好。

他们这次最大的变化之一，就是第一天直接启用了 MTP。

MTP，也就是 Multi-Token Prediction，可以让模型一次预测多个后续 token，再通过 speculative decoding 加速生成。

对于 Apple Silicon 这种很容易受到内存带宽限制的硬件来说，这个思路尤其有价值：

既然读取一次模型权重很贵，那就尽可能让一次 forward 产生更多有效 token。

而这还只是开始。

他们下一步准备加入多平台支持，第一个就是 CUDA。

如果同样的 MTP + 推理栈优化在 NVIDIA GPU 上也能获得明显收益，那么这件事的意义就不只是「Qwen 在 Mac 上跑快了」。

它可能意味着我们过去看到的很多本地 Dense 模型速度，并不是硬件真正的上限，只是推理软件还没追上模型。

现在模型厂商开始卷 MTP，推理框架开始专门针对 MTP 做优化，本地大模型的性能账可能还得重新算一遍。

期待一波，我会持续关注！！

> 媒体：
> - https://pbs.twimg.com/media/HPzxLE1aIAA0Stm.jpg

## 溯源

