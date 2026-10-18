---
title: "Minima：开源本地化文档问答 RAG"
author: "meng shao (@shao__meng)"
url: https://x.com/shao__meng/status/1891709512001937757
source: X
published: 2025-02-18 04:41 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

Minima - 开源本地化 RAG 系统

概述：开源的基于容器的 RAG 系统，可以完全在本地运行，也可以与 ChatGPT 和 Claude 等集成，项目的主要目标是让用户能够安全地查询自己的本地文档

核心功能

1. 智能文档问答
· 基于用户本地文档（PDF、Word、文本等）进行问答，答案由 AI 生成
· 支持完全本地运行（无需联网），或结合外部 AI 服务（如 ChatGPT、Claude）

2. 三种运行模式本地模式：
· 所有组件（LLM、嵌入模型、重排序模型）均在本地运行，数据完全隔离
· ChatGPT 模式：本地处理文档索引，生成答案时调用 ChatGPT（需联网）
· Claude 模式：与 Anthropic Claude 桌面应用集成，本地索引+Claude 生成答案

3. 核心特性数据隐私：
· 文档索引、检索过程完全本地化，避免敏感数据外传
· 灵活扩展：支持多种开源模型（如 Sentence Transformers、Ollama的LLM）
· 多格式支持：PDF、Excel、Word、Markdown 等常见文档类型

架构设计

1. 模块化容器服务：
· 通过 Docker Compose 组合多个微服务：索引服务：扫描本地文档，生成文本片段和向量嵌入
· 向量数据库：使用 Qdrant 存储向量，支持高效相似性检索
· LLM 服务：本地通过 Ollama 运行模型，或对接外部 API（如 ChatGPT）
· 重排序服务：优化检索结果（如 BAAI/bge-reranker 模型）
· 前端交互：提供 Electron 桌面应用或 Web 界面

2. 关键技术栈嵌入模型：
· 如 sentence-transformers/all-mpnet-base-v2，将文本转为向量
· 向量数据库：Qdrant 用于存储和快速检索向量
· 本地 LLM：通过 Ollama 运行模型（如 qwen2:0.5b）
· 重排序模型：提升检索结果相关性（如 BAAI 系列）

3. 数据流示例：
用户提问 → 向量化查询 → Qdrant 检索 → 重排序 → LLM 生成答案

> 媒体：
> - https://pbs.twimg.com/media/GkCzw-8aAAI_JLJ.jpg

## 溯源

