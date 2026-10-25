---
title: "Wavestone 拆了 11 个编程 agent 的源码：每个都要在同样 7 个子系统上做取舍（推文转述，“90 行外壳覆盖全部 7 个部件”是说错的）"
author: "Arindam Majumder 𝕏 (@Arindam_1729)"
url: https://x.com/Arindam_1729/status/2114026631941574741
source: X
published: 2026-10-24 16:10 UTC
saved: 2026-10-25
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 编程智能体
roots: [barbaste-2026-harness-engineering, harness-engineering, anthropic-2024-building-effective-agents, yao-2022-react, dominant-design]
---

## 原文

this paper should be required reading if you use Claude Code.

Wavestone AI Lab analyzed the source code of 11 coding agents, including Claude Code and Codex.

they found the same 7 building blocks inside capable coding agents.

agent = model + harness

here are the 7 parts, from simplest to most advanced:

→ 1. Loop: A basic while loop to fully replayable execution runs.

→ 2. LLM layer: A single prompt template to multiple provider-specific configurations.

→ 3. Tools: Basic bash commands to dozens of typed tools loaded on demand.

→ 4. Memory: Raw conversation history to persistent notes that survive across sessions.

→ 5. Safety: A simple step limit to rules, reviewer models, and sandboxing.

→ 6. Orchestration: Managing one agent or spawning sub-agents to handle parallel tasks.

→ 7. Extensions: Skills, MCP, and other ways to extend what the agent can do.

want to read the paper? start with these pages:

📄 Page 4: The complete 7-part architecture.

📄 Page 12: Three types of agent loops, including Claude Code and Codex.

📄 Page 67: 18 design rules for building better harnesses.

📄 Page 71: A 90-line harness that covers all 7 components.

here's the insight most people miss:

the model gets the attention.

but the harness determines how the agent uses tools, manages context, handles failures, remembers progress, and completes the task.

that's why switching to a smarter model doesn't automatically fix an unreliable agent.

if you want to build production-grade AI agents, learn the harness, not just the model.

https://t.co/OhmPx0eVhD

> 媒体：
> - https://video.twimg.com/amplify_video/2113049395746725888/vid/avc1/1800x2400/z7jukA9u28_ACQ-c.mp4?tag=29

## 溯源

- 核心主张：agent = 模型 + 外壳；能干的编程 agent 都围绕同样 7 个部件（循环、模型接入、工具、记忆、安全、多 agent 调度、扩展）搭起来，可靠性主要由外壳决定，换更强的模型修不好一个不可靠的 agent。
- 源知识：
  - [外壳工程：11 个编程 agent 的源码解剖](../roots/barbaste-2026-harness-engineering.md) · 关系：直接源自 · 强弱：强。推文就是在转述 Wavestone 这篇 11 个编程 agent 的源码研究，7 个部件、页码、18 条建议、90 行外壳都出自它（库里已有这篇论文本身：clips/2026-10-25-barbaste-harness-engineering-eleven-coding-agents.md）。
  - [外壳工程（agent = 模型 + 外壳）](../roots/harness-engineering.md) · 关系：直接源自 · 强弱：强。“agent = model + harness”和“学外壳、不只学模型”就是外壳工程这个说法的原样复述（Trivedy 2026-03 的公式）。
  - [构建高效的智能体](../roots/anthropic-2024-building-effective-agents.md) · 关系：相近 · 强弱：弱（模型复核通过）。“从最简单的 while 循环起步、按需加复杂度”与 Anthropic 先简单后复杂、少用框架的主张一致；推文本身没有提它，是经论文间接连上的。
  - [ReAct：推理与行动协同](../roots/yao-2022-react.md) · 关系：直接源自 · 强弱：弱（模型复核通过）。推文第 1 个部件“循环”就是 ReAct 的想-调工具-看结果循环；论文第 6.1 节说 11 个系统全是 ReAct 的变体，推文没有点名。
  - [主导设计](../roots/dominant-design.md) · 关系：相近 · 强弱：弱（模型复核通过）。“各家能干的 agent 都长出同样 7 个部件”是一个新品类走向主导设计、结构趋同的说法。
- 本质：这条新知识本质上是外壳工程（agent = 模型 + 外壳）在编程 agent 架构上的一次源码实证的转述，强调可靠性来自外壳而不只来自模型。
- 整理于：2026-10-25（第 8 轮）
