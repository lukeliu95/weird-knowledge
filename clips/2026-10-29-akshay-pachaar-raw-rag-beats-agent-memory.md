---
title: "RAW-RAG：四个对话记忆基准中，原始记录检索胜过多种复杂记忆系统"
author: "Akshay 🚀 (@akshay_pachaar)"
url: https://x.com/akshay_pachaar/status/2114659720602534014
source: X
published: 2026-10-26 10:05 UTC
saved: 2026-10-29
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [bao-2026-raw-rag, retrieval-augmented-generation]
---

## 原文

RAG is so back!

A new paper shows that straightforward retrieval from chat history can outperform much more complex agent memory systems.

The approach, RAW-RAG, retrieves relevant passages from the original conversation, reranks them, and passes the evidence to an LLM.

Across four benchmarks, it ranked first among the compared memory systems in six of seven benchmark–model settings.

The interesting part is why.

An answer can depend on several connected statements, including what changed, when it changed, and which earlier facts it affects. Turning conversations into isolated memories can break those connections.

RAW-RAG supplied enough evidence to answer more often. Even improved access to the transformed memory stores left an accuracy gap compared with raw evidence.

Preserving the original conversation keeps more of those relationships available for retrieval.

For these memory tasks, that makes simple RAG a baseline that more elaborate systems should have to beat.

paper: https://t.co/HDpy6bkICv

On a related note, I wrote about how observations in agent memory connect facts across conversations to surface patterns an agent can act on. If you’re building agents, you might find that article useful. It’s quoted below.

> 媒体：
> - https://pbs.twimg.com/media/HVjF2KTa0AASAB4.jpg

## 溯源

- 核心主张：在所测试的离线对话记忆基准中，直接检索原始对话并重排，通常胜过被比较的复杂记忆系统；保留答案之间的关系和时间顺序是重要原因之一。
- 源知识：
  - [Raw-RAG：原始对话检索应成为复杂记忆系统的对照基线](../roots/bao-2026-raw-rag.md) · 关系：直接源自 · 强弱：强。原论文四个基准、七组设置中六组领先的描述与帖子一致；第6节和附录F把适用范围限于已测试任务。
  - [检索增强生成（RAG）](../roots/retrieval-augmented-generation.md) · 关系：直接源自 · 强弱：强。帖子和原论文直接使用原始对话检索、重排、读者生成的流程；原论文第2.2节明确引用 Lewis 等2020。
- 本质：这条新知识本质上是检索增强生成在长期对话记忆中的应用：先保留原始证据并建立强对照，再判断额外记忆加工是否值得。
- 整理于：2026-11-03（第 9 轮）
