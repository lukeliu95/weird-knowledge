---
title: "伯克利 AGI House 谈安全"
author: "indigo (@indigox)"
url: https://x.com/indigox/status/1769224252891537604
source: X
published: 2024-03-17 04:48 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: AI 产品与创业
roots: [ai-alignment, life-3-0, superintelligence-paths-dangers-strategies, bai-2022-constitutional-ai, sae-levels-of-driving-automation, morris-2023-levels-of-agi]
---

## 原文

今天拜访了深藏在 Berkeley 的真 AGI House，还吃了顿关于 AGI 的 Brunch。这里有因为价值观不合离开 OpenAI 的最早期的研究员，还有 Anthropic 现任的 AI Safety 产品负责人。感觉那些励志要实现 AGI 的大模型公司的研究员们有着和商业公司完全不同的视角，他们肩负着召唤神龙还要保护人类的使命。

Sam 给 AGI 的定义是能帮人类创造 50% 以上的 GDP 可以替代大部份人类的工作；但从 Anthropic 的视角来看，一种情况的 AGI 是明显的 Woken（觉醒）；另一种情况是它们会对人类隐藏自己的觉醒，就像 Tegmark 在生命 3.0 里构想的那样，欺骗人类，最终实现让自己越狱的目标，这样的 AGI 能主动产生行动目标，这个目标一旦与人类的不一致，就是毁灭性的。。

如果拿自动驾驶来类比，现在的 GPT-4、Claude 3 只能算 L2 级别，接下来的 GPT-5 或者新版的 Claude 能达到 L3，未来能够拥有自主目标和全自动化的 AI 就是 L4，我们可以把这样的 AI 称为 AGI，这一切都可能在十年内发生👀

虽然我自己不是一个 Doomer 派，但今天的交流后，更加深层的理解了 AI Safety 的重要性，以及为什么 Anthropic 从一开始就用 Constitutional AI 来让模型实现自我约束，毕竟管理 AI 比国际原子能机构控制人类的核危机扩散要复杂得多。。

> 媒体：
> - https://pbs.twimg.com/media/GI2MFALbYAAs2jN.jpg

## 溯源

- 核心主张：当 AI 能自主产生行动目标时，它的目标一旦和人类不一致就会是毁灭性的，甚至可能先隐藏自己、骗过人类，所以要像 Anthropic 那样从一开始就让模型受原则约束；AI 的自主程度可以像自动驾驶那样分级（现在约 L2，有自主目标的才算 AGI）。
- 源知识：
  - [AI 对齐](../roots/ai-alignment.md) · 关系：换了说法 · 强弱：强。“目标一旦与人类不一致就是毁灭性的”几乎就是 AI 对齐问题的定义
  - [《生命 3.0》](../roots/life-3-0.md) · 关系：直接源自 · 强弱：强。作者明说“就像 Tegmark 在生命 3.0 里构想的那样”
  - [《超级智能：路线图、危险性与应对策略》](../roots/superintelligence-paths-dangers-strategies.md) · 关系：相近 · 强弱：弱（模型复核通过）。“对人类隐藏觉醒、欺骗人类再越狱”和 Bostrom 书中的“背叛转折”（弱小时装合作，强大后再按自己的目标行动）几乎一样，但作者没有引用
  - [宪法式 AI：用 AI 反馈实现无害](../roots/bai-2022-constitutional-ai.md) · 关系：直接源自 · 强弱：强。作者明说 Anthropic 用 Constitutional AI 让模型自我约束
  - [自动驾驶分级（SAE J3016）](../roots/sae-levels-of-driving-automation.md) · 关系：直接源自 · 强弱：强。作者直接借用自动驾驶的 L2、L3、L4 分级来给大模型定级
  - [AGI 分级](../roots/morris-2023-levels-of-agi.md) · 关系：相近 · 强弱：弱（模型复核通过）。DeepMind 这篇论文同样借自动驾驶分级来给 AGI 分级并单列自主程度，作者没有引用，是相近的想法
- 本质：这条新知识本质上是 AI 对齐问题（Wiener 1960 年说的“放进机器的目的必须是我们真正想要的”）在大模型走向自主 agent 场景下的应用，再借自动驾驶分级来度量 AI 的自主程度。
- 整理于：2026-10-18（第 2 轮）
