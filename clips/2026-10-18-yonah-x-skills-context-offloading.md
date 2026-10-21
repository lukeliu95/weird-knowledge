---
title: "Agent Skills 是上下文卸载"
author: "汉松 (@Yonah_x)"
url: https://x.com/Yonah_x/status/1979030811656573183
source: X
published: 2025-10-17 03:44 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [anthropic-2025-agent-skills, ji-2025-manus-context-engineering, progressive-disclosure, unix-philosophy, kiss-principle, virtual-memory, packer-2023-memgpt-llm-os, varda-2025-code-mode]
---

## 原文

Claude 的 Agent Skills 本质上是一种“上下文卸载”，把冗长的技能信息移出上下文，按需加载。巧的是最近 Manus 的 Peak 也分享一些“上下文卸载”的技巧。Manus 有很多工具，但是并不会把这些工具的完整定义告诉模型。那它怎么知道有哪些工具，又怎么调用它们呢？想象一下，给你一台新电脑，你怎么知道有哪些工具能用？普通用户会打开应用程序的列表，程序员会 `ls /usr/bin` 看一下有哪些命令可以用。

同样的，Manus 的解法是在系统提示词中，告诉模型在某个特定文件夹里，有许多预装的命令行实用工具。那些最常用的工具（ls、grep、cat、less、more等），就默认内置在系统提示里面的。不需要告诉模型如何使用这些工具，只需要列出工具名，然后告诉它可以使用 --help 参数来了解如何使用工具。最妙的是这些 shell 操作模型都是学过的，所以它的泛化能力很强，要加新的工具只需要往文件夹里面放一个命令就行。

我发现 Manus 真的是把 Unix 哲学贯彻到底了：KISS（Keep It Simple, Stupid）。

> 媒体：
> - https://pbs.twimg.com/media/G3bqREpWkAAE-Qx.png

## 溯源

- 核心主张：智能体不必把所有工具或技能的完整说明塞进上下文：常驻上下文里只放名字和简介，细节用到时再加载（上下文卸载）；并且尽量借用模型训练时已熟悉的约定（shell 命令、--help），这样泛化好，新增能力只要往文件夹里放一个文件。
- 源知识：
  - [用 Agent Skills 让智能体胜任真实工作](../roots/anthropic-2025-agent-skills.md) · 关系：直接源自 · 强弱：强。作者明说讲的是 Claude 的 Agent Skills；Anthropic 官方文章写明启动时只预载每个技能的名字和简介，判断用得上才读完整的 SKILL.md，正是「把冗长的技能信息移出上下文，按需加载」。
  - [Manus 的上下文工程（季逸超的博文与研讨会）](../roots/ji-2025-manus-context-engineering.md) · 关系：直接源自 · 强弱：强。作者明说参考了 Manus 的 Peak 最近分享的「上下文卸载」技巧；Lance Martin 对这次研讨会的总结写到，Manus 把大部分动作卸载到沙箱里的预装工具和标准 shell 命令上，而不是塞进函数调用层。
  - [渐进式披露](../roots/progressive-disclosure.md) · 关系：换了说法 · 强弱：弱（模型复核通过）。「上下文卸载、按需加载」就是交互设计里的渐进式披露，只是读者从人换成了模型；Anthropic 自己称它为 Agent Skills 的核心设计原则，作者换了个名字。
  - [Unix 哲学](../roots/unix-philosophy.md) · 关系：直接源自 · 强弱：强。作者原话「Manus 真的是把 Unix 哲学贯彻到底了」；小工具放在一个目录里、靠统一的命令行约定去发现和组合，是 Unix 的做法。
  - [KISS 原则（保持简单）](../roots/kiss-principle.md) · 关系：直接源自 · 强弱：强。作者原话点名 KISS（Keep It Simple, Stupid）。
  - [虚拟内存](../roots/virtual-memory.md) · 关系：相近 · 强弱：弱（模型复核通过）。小而贵的上下文只放常用部分，其余放在外面、需要时再调入，和虚拟内存用分页把快慢两层存储组合起来的思路一样；作者没有提。
  - [MemGPT：让大模型像操作系统一样管理内存](../roots/packer-2023-memgpt-llm-os.md) · 关系：相近 · 强弱：弱（模型复核通过）。MemGPT 明确把上下文窗口当主存、外部存储当慢存储，按需换入换出；「上下文卸载」是同一类做法。
  - [Cloudflare Code Mode：让模型写代码放进沙箱执行](../roots/varda-2025-code-mode.md) · 关系：相近 · 强弱：弱（模型复核通过）。「这些 shell 操作模型都是学过的，所以泛化能力很强」，和 Code Mode 的理由一样：模型在训练里见过的代码和命令远多于专门的工具调用格式，借用熟悉的形式更可靠。
- 本质：这条新知识本质上是「渐进式披露 / 分页调入」（常驻区只放目录，细节用到时再取）在大模型智能体上下文管理场景下的应用，再加上借用模型已学过的 Unix 约定来换取泛化。
- 整理于：2026-10-18（第 2 轮）
