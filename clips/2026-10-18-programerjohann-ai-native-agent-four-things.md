---
title: "什么才是 AI Native：别写死步骤"
author: "johann.GPT (@ProgramerJohann)"
url: https://x.com/ProgramerJohann/status/1974325208317374954
source: X
published: 2025-10-04 04:06 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [anthropic-2025-effective-context-engineering, anthropic-2024-building-effective-agents, bitter-lesson, mission-type-tactics]
---

## 原文

Anthropic 这个文章，挺有意思的，很久之前其实我们就在讨论什么才是 AI Native，在我们对比 Cursor 和 Cline 的做法的时候，我们发现 Cline 从一开的做法，就是和 Anthropic 是一致的。  

以前模型能力不行，我们要在 prompt 里写死每一步："先做 A，再做 B，然后做 C"；  

现在模型更聪明了，我们只需要说"这是你的目标，这些是你的工具，自己看着办"，让 Agent 自主决策。

里面的关键是做好四件事：写清晰的 prompt、设计高效的工具、用即时检索代替预加载、管理好有限的 context 窗口（通过压缩、笔记或拆分  sub agent 等方式）。

> 媒体：
> - https://pbs.twimg.com/media/G2Y2Rtab0AA-KRk.jpg

## 溯源

- 核心主张：模型够强以后，不该再在提示里写死每一步，而是给目标和工具、让 Agent 自己决定；配套要做好四件事：清晰的提示、高效的工具、用即时检索代替预先加载、管好有限的上下文窗口。
- 源知识：
  - [AI 智能体的上下文工程](../roots/anthropic-2025-effective-context-engineering.md) · 关系：直接源自 · 强弱：强。原帖说的“Anthropic 这个文章”是 2025-09-29 的《Effective context engineering for AI agents》，四件事（提示写在合适高度、工具、just-in-time 检索、压缩/笔记/子 Agent）和原文一一对应，原文也写了“越聪明的模型越不需要规定死的工程”。
  - [构建高效的智能体](../roots/anthropic-2024-building-effective-agents.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“写死步骤 vs 自己看着办”几乎就是该文“工作流（预设代码路径）vs 智能体（模型自己决定流程和工具）”的区分；原帖没引用这篇（推断，待 Luke 确认）。
  - [苦涩的教训](../roots/bitter-lesson.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“别把人想好的步骤写死，交给更强的模型”和 Sutton“能随算力扩展的通用方法终将胜过人工内置的知识”是同一个道理（推断，待 Luke 确认）。
  - [任务式指挥](../roots/mission-type-tactics.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“只交代目标和资源、怎么做让执行者临场决定”和任务式指挥一致（推断，待 Luke 确认）。
- 本质：这条新知识本质上是“苦涩的教训”和任务式指挥在 AI Agent 设计上的应用：执行者能力够强时，给目标和资源比给步骤更好；同时要像管理工作记忆一样管理有限的上下文。
- 整理于：2026-10-18（第 1 轮）
