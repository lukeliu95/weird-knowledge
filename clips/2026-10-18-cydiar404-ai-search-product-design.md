---
title: "Juchats谈AI搜索产品思路"
author: "𝗖𝘆𝗱𝗶𝗮𝗿 (@Cydiar404)"
url: https://x.com/Cydiar404/status/1872593833491587143
source: X
published: 2024-12-27 10:42 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: AI 产品与创业
roots: [retrieval-augmented-generation, edge-2024-graph-rag, learning-to-rank, query-expansion, maya-principle, the-nature-of-the-firm]
---

## 原文

最近看了很多 AI Search 产品，闭源的，开源的，发现很多人对 AI Search 没有完整的定义，最少从产品上看不到任何，能看到的往往都是 AI 驱动了搜索（总结），独特的格式化输出页面，Baseline RAG 又起到的是什么作用呢？快速检索和连接用户提问？以下是 Juchats 的回答，我觉得还是差点意思，我们的搜索会这么做！

核心宗旨：
- 合作共创，哪怕是 AI Search 也逃不掉 Search API，所有内容全部靠爬，非常不现实，合作才是强有力的保障，在 Search API 上面抽丝剥茧，做到细微差异化！

基础路径：Query - Retrieve - Summary

核心闭环：
- 利用大模型特性完成Query拆分，做到更理解用户
- 利用 Baseline RAG 特性，针对所有信息来源 Rerank 检索，提高精准度
- 利用大模型特性完成内容的整理汇总提炼
- 聚合各类数据资源（ETL）开启智能RAG路由，有效区分Search API、Online、ETL，从宽泛到精准逐层检索
- 开启 Baseline RAG + Graph 双模式驱动数据合成

用户体验：
- 保持原有用户搜索体验，做提升体验，不做重构体验
- 快速给到结果，并定位权威结果（增强可信度）
- 降低信息冗余，直接产生内容差异对比

商业模式：
- 新的广告模式，精准搜索，精准反馈，精准广告
- 知识订阅 做 Graph 订阅，按照用户的知识谱图拓展
- 订阅数据源 做 ETL 订阅，完成专业场景闭环

> 媒体：
> - https://pbs.twimg.com/media/GfyAed2boAEOg_l.jpg

## 溯源

- 核心主张：AI 搜索不只是“搜索加总结”，而是一条“理解并拆分查询 → 多来源分层检索并重排 → 汇总提炼”的流水线：数据靠和搜索 API 合作而不是自己全爬，检索用基础 RAG 加知识图谱，体验上做增强而不改变用户习惯，靠精准广告和知识、数据订阅赚钱。
- 源知识：
  - [检索增强生成（RAG）](../roots/retrieval-augmented-generation.md) · 关系：直接源自 · 强弱：强。原文直接把 Baseline RAG 当作核心组件。
  - [从局部到全局：GraphRAG](../roots/edge-2024-graph-rag.md) · 关系：直接源自 · 强弱：强。“Baseline RAG + Graph 双模式”里的“Baseline RAG”正是微软 GraphRAG 论文和博客用来做对比的说法。
  - [排序学习（重排）](../roots/learning-to-rank.md) · 关系：直接源自 · 强弱：强。原文明说“针对所有信息来源 Rerank 检索，提高精准度”“从宽泛到精准逐层检索”，就是先粗召回、再用更准的模型重排的两阶段排序。
  - [查询扩展（查询改写）](../roots/query-expansion.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“利用大模型完成 Query 拆分，做到更理解用户”，是查询改写在大模型时代的做法。
  - [MAYA 原则（最先进但仍可接受）](../roots/maya-principle.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“保持原有用户搜索体验，做提升体验，不做重构体验”，是在用户熟悉的形态上做有限创新，即“最先进但仍可接受”。
  - [企业的性质](../roots/the-nature-of-the-firm.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“所有内容全部靠爬非常不现实，合作才是保障”，是自己做还是向外买的取舍：自己爬的成本高于买 Search API 的交易成本。
- 本质：这条新知识本质上是检索增强生成（RAG / GraphRAG）加经典信息检索“改写查询—多路召回—重排”流水线，在 AI 搜索产品设计场景下的应用。
- 整理于：2026-10-18（第 2 轮）
