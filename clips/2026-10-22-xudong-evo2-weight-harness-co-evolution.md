---
title: "Evo² 解读：把改权重和改 harness 两条自进化路线接起来，让“改进者”本身也被训练"
author: "@Xudong07452910"
url: https://x.com/Xudong07452910/status/2110217783758012460
source: X
published: 2026-10-14 03:55 UTC
saved: 2026-10-22
why: "探索日报：Luke 想看"
related_principles: [原则 1, 原则 5]
status: 未整理
kind: 观点
topic: Agent 与 Skill
roots: []
---

## 原文

现在很多 Agent 自进化，大致走两条路：

一条改模型权重，一条改 Harness。

这篇 Evo² 直接把两条路接了起来。

系统里，同一个模型同时扮演两个角色：

Proposer 负责修改 Harness，Reflector 负责看执行结果、分析哪里改对了、哪里还需要修。

关键在下一步。

这些 Harness 修改和真实执行结果，会继续拿回来训练 Proposer 和 Reflector。模型变得更会改 Harness，新的 Harness 又产生更好的训练经验，形成一个持续循环。

结果是 Evo² 在 Polyglot 上达到 82.1%，最强 baseline 是 62.6%；SWE-bench Verified 达到 48.3%，相比 baseline 的 41.0% 继续提升。

而且进化出来的 Harness 可以直接迁移到其他 benchmark，不需要重新搜索。固定 GPT-5-mini 权重时，仅靠这套 Harness 进化流程，也把表现从 24.4% 提升到 48.3%。

这篇真正往前推的一步，是让「改进者」本身也进入了学习循环。

以后自进化 Agent 可能会越来越像两个互相促进的系统：

一边积累更好的外部运行结构，一边训练出更会修改这些结构的模型。

当「怎么让自己变强」也开始被持续训练，self-evolution 才真正有了第二层递归。

📎 arxiv: https://t.co/pfHcHHL7BF

> 媒体：
> - https://pbs.twimg.com/media/HUj5-a4WoAADL3g.jpg

## 溯源

