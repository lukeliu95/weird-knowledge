---
title: "常驻 agent 的 6 层结构（推文作者据 OpenAI 资料自制的 PDF）"
author: "chuplung (@choopyplug1)"
url: https://x.com/choopyplug1/status/2111547857995985346
source: X
published: 2026-10-17 20:00 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [openai-2026-dots-safety-security-privacy, openai-2026-gpt-6-astra-system-card, defense-in-depth, principle-of-least-privilege, parasuraman-2000-levels-of-automation, anthropic-2024-building-effective-agents, shi-2023-irrelevant-context-distraction, unix-philosophy]
---

## 原文

OpenAI just dropped a 10-page PDF explaining how always-on agents actually work-and why prompts are dead:

the shift: your chatbot waits for you. this agent doesn't

the formula: Always-On Agent = Model + Computer + Memory + Rules

here's the 6-layer architecture:

layer 1 → its own computer - keeps working after you close the laptop

layer 2 → reach - Slack, Teams, voice, 4,000+ apps. it lives where your work lives

layer 3 → memory - correct it once, never explain it again

layer 4 → idle research - reads everything while you sleep, touches nothing

layer 5 → rules - act, ask or hand off. you decide before it runs

layer 6 → review - nothing risky ships unchecked. stop is not undo

the result: 0 of 16,600 attacks got through. but one agent with 10 jobs drifts 2x more. one agent, one job

this 10-page PDF is the blueprint for agents that work without being asked

bookmark it, then read the article on giving your Dot real autonomy ↓

> 媒体：
> - https://pbs.twimg.com/media/HU25VUjWIAAWv9H.jpg

## 溯源

- 核心主张：常驻 agent = 模型 + 电脑 + 记忆 + 规则，可拆成 6 层（自己的云电脑、能触达各渠道、记忆、空闲时只读研究、动作前按规则决定自己做/先问/交回、风险动作先审）；架构里一半在管权限而不是能力；OpenAI 测试里邮件注入 0 次得手，但连续任务一多越界就增加，所以一个 agent 只管一件事。（推文说"OpenAI 发布了 10 页 PDF"不对：那份 PDF 是推文作者自己根据 OpenAI 资料写的，6 层的名字也是作者起的）
- 源知识：
  - [OpenAI dots 的安全设计（《我们如何将安全性、信息安全和隐私保护融入 dots》及帮助中心）](../roots/openai-2026-dots-safety-security-privacy.md) · 关系：直接源自 · 强弱：强。PDF 自己写明"根据 OpenAI 的 dots 发布材料和帮助文档"；6 层里的云电脑、只读的主动研究、动作规则、自动审核、停止不等于撤销，都是对 OpenAI 官方安全设计的重新归纳
  - [GPT-6 Astra 系统卡（含 dots 附录）](../roots/openai-2026-gpt-6-astra-system-card.md) · 关系：直接源自 · 强弱：强。16,600 次攻击 0 次得手、越界从 8.6% 升到 19.7% 都出自系统卡的 dots 附录（12.2.1 和 12.3.5.2 节）；但"10 件事多 2 倍"是改写过的说法，见误传
  - [纵深防御](../roots/defense-in-depth.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。后三层（只读研究、规则、审核）是叠在模型之上的多道独立防线；OpenAI 系统卡自己也说是靠纵深防御守住安全边界，但推文没提这个词
  - [最小权限原则](../roots/principle-of-least-privilege.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。"空闲研究什么都读、什么都不碰"就是只给只读权限，主动研究用不到写权限就不给
  - [自动化的类型与等级模型](../roots/parasuraman-2000-levels-of-automation.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。"规则：自己做、先问、交回"是给每类动作定自动化等级，人提前定、agent 运行时照办
  - [构建高效的智能体](../roots/anthropic-2024-building-effective-agents.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。"agent = 模型 + 电脑 + 记忆 + 规则"这种公式，和"增强型大模型 = 模型 + 检索 + 工具 + 记忆"是同一类拆法，只是把常驻电脑和权限规则单列出来
  - [大模型很容易被无关上下文带偏](../roots/shi-2023-irrelevant-context-distraction.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。系统卡说越界多是"把信息带进不相关的任务"，连续任务越多越容易越界，和"无关上下文会把模型带偏"是同一个现象的不同场景；这是推断，OpenAI 没这么归因
  - [Unix 哲学](../roots/unix-philosophy.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。"一个 agent 一件事"和"每个程序只做好一件事"同一个思路
- 本质：这条新知识本质上是纵深防御和最小权限在常驻 agent 产品架构上的应用，内容是把 OpenAI dots 的官方资料重新归纳成 6 层。
- 整理于：2026-10-18（第 3 轮）
