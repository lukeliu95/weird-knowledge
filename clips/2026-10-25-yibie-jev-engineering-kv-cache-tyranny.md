---
title: KV cache 的暴政：今天的 agent 只能"只追加对话"，由此带来路由失效、工具挤占上下文、压缩丢信息、子 agent 少等六个毛病（《Jev 工程学：为 coding agent 而作》中译介绍）
author: yibie (@yibie)
url: https://x.com/yibie/status/2102260699133059554
source: X
published: 2026-09-22 04:56 UTC
saved: 2026-10-25
why: 探索日报：Luke 想看
related_principles: [原则 11]
status: 未整理
kind: 观点
topic: 编程智能体
roots: []
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

（整理时填写，存的时候留空）
