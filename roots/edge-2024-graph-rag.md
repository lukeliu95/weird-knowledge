---
name_zh: "从局部到全局：GraphRAG"
name_en: "From Local to Global: A Graph RAG Approach to Query-Focused Summarization"
proposer: "Darren Edge 等（微软研究院）"
year: "2024"
type: 论文
verified: true
---

# 从局部到全局：GraphRAG（From Local to Global: A Graph RAG Approach to Query-Focused Summarization）

## 一句话

先用大模型从文档里抽出实体关系建成知识图谱，并给关系紧密的实体群预先写好摘要，再据此回答问题；对“整个资料库讲了什么”这类全局问题，比只按片段检索的基础 RAG 答得更全面。

## 原始出处

- From Local to Global: A Graph RAG Approach to Query-Focused Summarization, Darren Edge et al., arXiv 2404.16130, 2024，https://arxiv.org/abs/2404.16130
- GraphRAG: Unlocking LLM discovery on narrative private data, Jonathan Larson & Steven Truitt, Microsoft Research Blog, 2024-02-13（用“baseline RAG”做对比），https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/

## 更底层的源头

- [检索增强生成（RAG）](retrieval-augmented-generation.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Juchats谈AI搜索产品思路](../clips/2026-10-18-cydiar404-ai-search-product-design.md) | 直接源自 | 强 |
