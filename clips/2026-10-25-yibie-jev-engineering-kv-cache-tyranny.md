---
title: KV cache 的暴政：今天的 agent 只能"只追加对话"，由此带来路由失效、工具挤占上下文、压缩丢信息、子 agent 少等六个毛病（《Jev 工程学：为 coding agent 而作》中译介绍）
author: yibie (@yibie)
url: https://x.com/yibie/status/2102260699133059554
source: X
published: 2026-09-22 04:56 UTC
saved: 2026-10-25
why: 探索日报：Luke 想看
related_principles: [原则 11]
status: 已整理
kind: 观点
topic: 编程智能体
roots: [ji-2025-manus-context-engineering, zheng-2024-sglang, chen-2023-frugalgpt, martin-2025-context-engineering-agents, yan-2025-dont-build-multi-agents]
---

## 原文

TypeSafe 创始人 Diogo Almeida 的设计笔记，有人汇编成了一份 12 页的工作笔记：《Jev 工程学：为 coding agent 而作》。

我把它全文翻译了，保留原章节结构和全部 7 张插图。

https://t.co/QR14ekayOM

这份笔记从一个挑衅性的问题开始：如果语言模型没有 KV cache，你会怎么设计 coding agent？

这个问题之所以有杀伤力，是因为 KV cache 是今天所有 agent 被建成「只追加对话记录」的根本原因——改早期上下文就失效、必须重新处理后面全部。这个经济事实塑造了几乎每个设计决策，却通常没人说出来。

笔记把它叫「KV cache 的暴政」，然后指出了当前 agent 不加审视就继承的六个症状：

路由失效（不是便宜模型弱，是上下文被重新处理）
工具挤占上下文（因为必须提前声明 schema）
compaction 丢信息（因为在问题已知之前压缩）
子 agent 稀少（因为传状态很难）
重启（把好状态和坏状态一起丢掉）
电池之争（只因为每个内置永久消耗上下文）

这里有一个对比：用 Opus（$5/$25）和 Sonnet（$3/$15）标价，代入一个合理会话形态，纯 Opus 是 4.15，而那条本该省钱的路由路径是 6.19——留在前沿模型上的成本，大约是路由路径的三分之二。

还有一张表：写代码在总 token 占比里排倒数第二（4-10%），读取和搜索占了近三分之二。

#Agent工程 #上下文工程 #开源

（推文附的链接卡片：[GitHub - yibie/jev-engineering-zh: 《Jev 工程学：为 coding agent 而作》完整中文翻译 — 保留原结构与 7 张插图](https://github.com/yibie/jev-engineering-zh)）

## 溯源

- 核心主张：KV 缓存“改了前面就要重算后面”的经济性，让今天的 agent 都被建成只追加的对话记录，并由此带来路由反而更贵、工具定义挤占上下文、压缩丢信息、子 agent 少、重启丢状态等六个默认设计问题。
- 源知识：
  - [Manus 的上下文工程（季逸超的博文与研讨会）](../roots/ji-2025-manus-context-engineering.md) · 关系：相近 · 强弱：强。Manus 把 KV 缓存命中率当最重要的指标，要求前缀稳定、上下文只追加、工具用遮蔽而不增删；Jev 笔记是同一诊断的反面：把这些做法称为“KV 缓存的暴政”，主张跳出它。
  - [SGLang 与 RadixAttention（跨调用复用 KV 缓存）](../roots/zheng-2024-sglang.md) · 关系：相近 · 强弱：弱（模型复核通过）。笔记的前提是前缀 KV 缓存复用：共享前缀可直接复用，改动早期内容会让之后的缓存全部失效；SGLang 的 RadixAttention 是这一机制的代表性论文，笔记没有引用。
  - [FrugalGPT：用级联大模型省钱又提效](../roots/chen-2023-frugalgpt.md) · 关系：挑战 · 强弱：弱（模型复核通过）。FrugalGPT 主张把问题先交给便宜模型来省钱；笔记算出在长会话里换模型要把上下文重新处理一遍，路由路径（6.19）反而比一直用 Opus（4.15）贵。
  - [智能体的上下文工程（写入、选取、压缩、隔离）](../roots/martin-2025-context-engineering-agents.md) · 关系：相近 · 强弱：弱（模型复核通过）。六个症状正好落在上下文工程的“选取（工具按需加载）、压缩（compaction）、隔离（子 agent）”几类做法上，笔记批评的是这些做法今天的默认实现。
  - [别做多智能体](../roots/yan-2025-dont-build-multi-agents.md) · 关系：相近 · 强弱：弱（模型复核通过）。“子 agent 少是因为传状态难”与 Cognition 的论点一致：多 agent 必须共享完整轨迹，否则会出互相冲突的决定。
- 本质：这条新知识本质上是 KV 缓存（前缀计算复用）的成本结构在 agent 上下文设计上的应用：缓存经济性决定了只追加的对话形态，进而决定路由、工具、压缩和子 agent 的取舍。
- 整理于：2026-10-25（第 8 轮）
