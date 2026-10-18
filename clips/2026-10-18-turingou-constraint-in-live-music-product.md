---
title: "与Claude Code讨论艺术与约束"
author: "郭宇 guoyu.eth (@turingou)"
url: https://x.com/turingou/status/2046104851957108972
source: X
published: 2026-04-20 05:53 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: AI 产品与创业
roots: [rule-of-least-power, acar-2019-creativity-constraints, overchoice, anthropic-2024-building-effective-agents, varda-2025-code-mode]
---

## 原文

我最近做了个很有意思的现场音乐产品。但是在做的过程中，我和 cc 有着反复的讨论，这个讨论很有意思，我决定记录分享下来。

很多现场音乐会使用 web 技术做音乐可视化，我的想法是使用 dynamic worker 可以验证 llm 到音乐生成和可视化的思路，而且这正是 v8 这种小隔离环境擅长做的事情。但实际上使用下来，会发现：

使用 codex/cc 可以 one shot 做出完成度较高的可视化内容，但使用 API 调用 llm 却很难 one shot 做到。因为这本质上要求我们在 API 层面实现复杂的 cli tool use，这就回到今年以来的最大选题困境，也是我不押注 cloudflare 那条“应该由 llm 写代码交给 sandbox 执行，而不是在 sandbox 中执行 llm cli” 的原因。

这种技术选型的困境是，一方面我们依赖大量的 skill 上下文导致 context 变的很大，在单一 llm 调用，甚至严格要求 cpu 运行时间的环境中不太合适，另外一方面，单一 API 调用导致的错误率非常高（缺少 agentic loop 的天然问题）

做到最后，cc 无法在这种技术架构下实现批量生产高完成度的产品，要求我将 dynamic worker 这种技术选项删除，完全走受控制的路线（llm 输出 json 这种传统的方式），而且他提供了一个产品上的说服思路，以下是它的原话：

「艺术家在 TD/Notch 做出精彩不是因为工具"自由"——恰恰相反，TD 节点比裸 WebGL更约束。但节点本身是作品级封装（feedback loop / particle GPU / volumetric / post-FX chain）。艺术家的"自由"表现为在高级原语之间的组合。所以 Recipe 路径的本质不是 "限制 LLM"，而是"把 LLM 的工作台从锤子钉子换成 TouchDesigner"——LLM 的语义自由度不变（从 prompt 到风格决策），但手里的原语变强」

换句话说，cc 认为艺术性表达的本质在于约束而不是发散。产品应当尽可能的引导用户思考，而不是让用户在一个无尽的空间中自由探索。这个反馈把一个技术选型的问题突然变成了一个哲学问题，是很有意思的对话实践。

## 溯源

- 核心主张：让大模型在受控的高级原语之间做组合（输出 JSON 配方），比让它在没有约束的环境里直接写代码更可靠；表达力来自“强原语 + 约束”，而不是无限自由。
- 源知识：
  - [最小能力原则](../roots/rule-of-least-power.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。放弃让模型写任意代码、改成输出 JSON 配方，正是“选够用的最弱语言”；作者没有提这条原则。
  - [约束下的创造力与创新（倒 U 型关系）](../roots/acar-2019-creativity-constraints.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“艺术性表达的本质在于约束而不是发散”，和这篇综述“约束与创造力呈倒 U 型、适度约束最好”的结论相近。
  - [选择过载](../roots/overchoice.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“产品应当引导用户，而不是让用户在无尽空间里自由探索”接近选择过载的说法。
  - [构建高效的智能体](../roots/anthropic-2024-building-effective-agents.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。作者把单次 API 调用错误率高归因于“缺少 agentic loop”，和 Anthropic 区分“工作流”与“靠环境反馈循环的智能体”一致。
  - [Cloudflare Code Mode：让模型写代码放进沙箱执行](../roots/varda-2025-code-mode.md) · 关系：挑战 · 强弱：强。作者点名不押注 Cloudflare“由大模型写代码交给沙箱执行”的路线（Dynamic Workers），最后还删掉了沙箱执行代码这个选项，回到让模型输出 JSON，正好和 Code Mode“写代码胜过结构化调用”的主张相反。
- 本质：这条新知识本质上是「最小能力原则」和「约束促进创造力」在大模型生成类产品架构选型上的应用。
- 整理于：2026-10-18（第 2 轮）
