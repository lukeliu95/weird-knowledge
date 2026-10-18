---
title: "FalkorDB：给LLM用的图数据库"
author: "AIGCLINK (@aigclink)"
url: https://x.com/aigclink/status/1994337578615800116
source: X
published: 2025-11-28 09:28 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: Agent 与 Skill
roots: []
---

## 原文

面向LLM的超高速图数据库：FalkorDB，为LLM提供长期记忆、上下文理解和事实性知识，帮助LLM进行复杂推理

其通过GraphBLAS、稀疏矩阵和线性代数查询，来解决LLM在事实性、上下文理解和实时响应上的痛点

用稀疏矩阵和线性代数替代传统遍历，将整个图结构转化为数学矩阵，稀疏矩阵只存储存在的连接，这极大节省空间和计算资源，查询变成矩阵运算，速度远超遍历

比仅靠向量搜索，图数据库能保留实体间的细腻关系和上下文，提升智能体返回信息的准确性和相关性

做为GraphRAG的“知识缓存”，LLM回答前先要“秒级”拿到相关子图，FalkorDB负责毫秒级把实体-关系子图抽出来塞Prompt

做为智能体/聊天机器人记忆，对话过程中实时写入“用户-意图-实体”三元组，下轮对话立刻可查

#AI记忆 #FalkorDB

> 媒体：
> - https://video.twimg.com/tweet_video/G61O8yPbIAACJEQ.mp4

## 溯源

