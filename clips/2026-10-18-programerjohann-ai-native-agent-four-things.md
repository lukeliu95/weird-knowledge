---
title: "什么才是 AI Native：别写死步骤"
author: "johann.GPT (@ProgramerJohann)"
url: https://x.com/ProgramerJohann/status/1974325208317374954
source: X
published: 2025-10-04 04:06 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind: 观点
topic: Agent 与 Skill
roots: []
---

## 原文

Anthropic 这个文章，挺有意思的，很久之前其实我们就在讨论什么才是 AI Native，在我们对比 Cursor 和 Cline 的做法的时候，我们发现 Cline 从一开的做法，就是和 Anthropic 是一致的。  

以前模型能力不行，我们要在 prompt 里写死每一步："先做 A，再做 B，然后做 C"；  

现在模型更聪明了，我们只需要说"这是你的目标，这些是你的工具，自己看着办"，让 Agent 自主决策。

里面的关键是做好四件事：写清晰的 prompt、设计高效的工具、用即时检索代替预加载、管理好有限的 context 窗口（通过压缩、笔记或拆分  sub agent 等方式）。

> 媒体：
> - https://pbs.twimg.com/media/G2Y2Rtab0AA-KRk.jpg

## 溯源

