---
title: "Wavestone 拆了 11 个编程 agent 的源码：能干的 agent 都有同样 7 个部件"
author: "Arindam Majumder 𝕏 (@Arindam_1729)"
url: https://x.com/Arindam_1729/status/2114026631941574741
source: X
published: 2026-10-24 16:10 UTC
saved: 2026-10-25
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind: 观点
topic: 编程智能体
roots: []
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

