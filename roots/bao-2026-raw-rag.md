---
name_zh: "Raw-RAG：原始对话检索应成为复杂记忆系统的对照基线"
name_en: "Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought"
proposer: "Zhengye Bao、Shengtao Zhang、Haokai Zhang、Shiqi Lou、Muning Wen、Minnan Luo"
year: "2026"
type: 论文
verified: true
---

# Raw-RAG：原始对话检索应成为复杂记忆系统的对照基线（Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought）

## 一句话

在研究测试的离线对话记忆任务中，对原始记录做密集检索、重排后再回答已很强；保留上下文中的关系和时间顺序可能比先拆成孤立事实更重要，复杂记忆系统应先证明能胜过这一基线。

## 原始出处

- Bao等，arXiv:2610.30755v1，2026-10-22；核对正文第3—6节、预算控制和附录F边界，https://arxiv.org/html/2610.30755v1
- arXiv登记页：作者、提交日期及全文链接，https://arxiv.org/abs/2610.30755
- 争议：四个公开对话基准的七组模型设置里六组领先被比较的记忆系统，不等于击败所有方案或全上下文。部分诊断同时受证据长度、组织方式和读者能力影响；不覆盖交互、多模态、权威状态维护、隐私删除等运行要求，原始记录也有存储与隐私成本。

## 更底层的源头

- [检索增强生成（RAG）](retrieval-augmented-generation.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [RAW-RAG：四个对话记忆基准中，原始记录检索胜过多种复杂记忆系统](../clips/2026-10-29-akshay-pachaar-raw-rag-beats-agent-memory.md) | 直接源自 | 强 |
