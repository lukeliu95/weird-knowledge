---
title: "Evo² 解读：把改权重和改 harness 两条自进化路线接起来，让“改进者”本身也被训练"
author: "@Xudong07452910"
url: https://x.com/Xudong07452910/status/2110217783758012460
source: X
published: 2026-10-14 03:55 UTC
saved: 2026-10-22
why: "探索日报：Luke 想看"
related_principles: [原则 1, 原则 5]
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [xu-2026-evo2, zhang-2025-darwin-godel-machine, zelikman-2022-star, anthony-2017-expert-iteration, recursive-self-improvement]
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

- 核心主张：agent 自进化不必在“改权重”和“改 harness”两条路里二选一：让同一个模型既当提议者改 harness、又当反思者看执行结果，再拿这些改动和真实结果去训练它，模型越来越会改 harness，新 harness 又产出更好的训练经验，“改进者”本身进入学习循环；进化出的 harness 还能直接迁移到别的基准。
- 源知识：
  - [Evo²：权重与运行框架共同进化，让“进化者”自己也进化](../roots/xu-2026-evo2.md) · 关系：直接源自 · 强弱：强。推文解读这篇论文：Proposer / Reflector 双角色、Polyglot 82.1% 对 62.6%、SWE-bench Verified 48.3% 对 41.0%、固定 GPT-5-mini 权重从 24.4% 升到 48.3% 都出自论文摘要。
  - [达尔文哥德尔机：自我改进 agent 的开放式演化](../roots/zhang-2025-darwin-godel-machine.md) · 关系：相近 · 强弱：强。DGM 是 Evo² 的对照组之一（同在 Polyglot 和 SWE-bench Verified 上比），代表“只改 agent 自己的代码、不动权重”那条路；Evo² 在此之上把权重也拉进循环。
  - [STaR：用推理自举推理（自学推理者）](../roots/zelikman-2022-star.md) · 关系：相近 · 强弱：强。Evo² 第 1、2 节引了 STaR，代表“用自己生成的成功经验更新权重”那条路；Evo² 训练 Proposer 和 Reflector 也是从自己的改动记录里回收可用轨迹再做 SFT。
  - [专家迭代（ExIt）](../roots/anthony-2017-expert-iteration.md) · 关系：相近 · 强弱：弱（模型复核通过）。“模型更会改 harness → 新 harness 产出更好的训练经验 → 再训练模型”和专家迭代里“搜索产出更好的示范 → 网络学会 → 网络再引导搜索”同构；论文没引，是模型推断。
  - [递归自我改进](../roots/recursive-self-improvement.md) · 关系：相近 · 强弱：弱（模型复核通过）。推文说的“让怎么变强本身也被持续训练”“第二层递归”，论文标题叫 Evolving the Evolver，都是递归自我改进的说法；推文没用这个词。
- 本质：这条新知识本质上是递归自我改进在 agent 上的一种做法：把专家迭代式的互相抬升（外部结构产出数据、数据再训练改进者）用到“负责改 harness 的模型”身上。
- 整理于：2026-10-24（第 6 轮）
