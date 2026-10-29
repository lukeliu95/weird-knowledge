---
title: "RAW-RAG：直接从聊天记录检索胜过复杂记忆系统"
author: "Akshay 🚀 (@akshay_pachaar)"
url: https://x.com/akshay_pachaar/status/2114659720602534014
source: X
published: 2026-10-26 10:05 UTC
saved: 2026-10-29
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
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

