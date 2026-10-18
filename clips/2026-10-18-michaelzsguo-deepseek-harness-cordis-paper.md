---
title: "DeepSeek Harness 论文"
author: "Michael Guo (@Michaelzsguo)"
url: https://x.com/Michaelzsguo/status/2088373848639152539
source: X
published: 2026-08-14 21:15 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind: 观点
topic: 编程智能体
roots: []
---

## 原文

DeepSeek 发布 Harness 的时候，做了一件很不寻常的事：他们没有像大多数科技公司一样写一篇技术博客，而是直接发了一篇论文，A Programming Paradigm for Spatiotemporal Composability。

别人发布一个 Agent Harness，通常会告诉你有哪些 tools，怎么接 MCP，怎么做 memory，怎么 orchestrate agents。DeepSeek 却在用形式化定义、数学符号和演算体系解释 Cordis 背后的编程范式：effect、coeffect、context transformation、inverse，一个组件如何加入系统、如何撤销，依赖关系如何随着运行时状态动态变化，甚至试图从理论上说明这套 programming model 为什么成立。

非常另类，也非常与众不同，让人耳目一新。

这种气质，和论文作者之一、DeepSeek Harness 负责人崔添翼的背景密不可分。

崔并不是典型的 AI researcher。在加入 DeepSeek 之前，他在 Jane Street 工作了大约九年。

Jane Street 在程序员世界里是一个很特殊的存在。它虽然是一家量化交易公司，却以 functional programming、type system、formal reasoning 和对软件正确性的执着而闻名，甚至长期把 OCaml 这种极少出现在普通互联网公司的函数式语言作为核心生产语言。崔添翼当年放弃 Google offer 选择 Jane Street，其中一个重要原因，就是他希望真正使用 OCaml 和函数式编程。

所以当你今天打开这篇论文，会发现这种思考方式一脉相承：系统最基本的抽象是什么，有哪些不变量，一个 component 加进来以后改变了什么，离开以后这些变化能不能被完整撤销。这正是 Jane Street 式的 formal reasoning 在一套 agent 系统设计上的延伸。

Cordis 很有创造性的把这个问题归纳为两个维度：Temporal composability，一个组件退出时，它产生的副作用能够被完整撤销；Spatial composability，组件只需要声明自己的依赖，runtime 会随着 context 的变化动态管理这些依赖。

如果说 Shigma 孤梦星影带来了 Cordis 这套架构，那么崔添翼为什么会如此自然地接受、推动，甚至把它形式化成论文？

这也许可以从他更早的经历里找到答案。

二十年前，他写过在中国算法竞赛圈影响很大的《背包问题九讲》。背包问题表面上是在研究"有限容量里怎么选择物品"，但真正训练的是另一种能力：如何找到正确的状态表示，把复杂约束转化成统一模型，再通过局部状态转换组合出整个问题的解：状态、转换、依赖、抽象、组合。二十年后，问题从"如何组合一组物品"，变成了"如何组合一个不断变化的软件系统"。对象完全不同，但这种思维方式如出一辙。

于是你再看 DeepSeek Harness 最核心的设计理念：Everything is a Plugin。model 是 plugin，tool 是 plugin，session 是 plugin，甚至 agent loop 本身也是 plugin。系统不再围绕某个固定 agent 构建，而是围绕"如何动态组合这些能力"来构建。

这种视角一石激起千层浪，也让整个行业重新开始审视 Harness 到底应该怎么设计：其中就包括最受欢迎的 Agent Harness 之一 Pi 的作者 Armin Ronacher。他看完之后写道，这是他很久以来第一次在这个领域看到全新的东西，并因此重新审视自己的一些设计选择。

就像当年 R1 推出，让整个行业为之震动，重新思考推理模型的后训练方法，并推动了随后开源模型的飞速发展。这一次 Harness 的推出，同样可能带来一次新的范式革新。

> 媒体：
> - https://pbs.twimg.com/media/HPtadgrXMAA66fW.jpg

## 溯源

