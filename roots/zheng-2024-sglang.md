---
name_zh: "SGLang 与 RadixAttention（跨调用复用 KV 缓存）"
name_en: "SGLang: Efficient Execution of Structured Language Model Programs"
proposer: "Lianmin Zheng、Liangsheng Yin、Zhiqiang Xie 等（UC Berkeley、Stanford 等）"
year: "2023（NeurIPS 2024）"
type: 论文
verified: true
---

# SGLang 与 RadixAttention（跨调用复用 KV 缓存）（SGLang: Efficient Execution of Structured Language Model Programs）

## 一句话

多次调用大模型的程序（agent、多轮对话、少样本）大量共享前缀；RadixAttention 把算过的 KV 缓存存进基数树、按前缀复用并按最近最少使用淘汰，吞吐最多提高 6.4 倍。前缀一变，之后的缓存就用不上。

## 原始出处

- SGLang: Efficient Execution of Structured Language Model Programs，Lianmin Zheng 等，arXiv:2312.07104，2023，https://arxiv.org/abs/2312.07104
- 同上，Advances in Neural Information Processing Systems 37（NeurIPS 2024），pp. 62557–62583，DOI 10.52202/079017-2000，https://doi.org/10.52202/079017-2000
- 争议：前缀 KV 缓存复用不是这一篇独有：vLLM 的 PagedAttention（Kwon 等 2023）等推理系统也做前缀共享，各家 API 的“提示缓存”计价也基于同一机制；这里选 SGLang 是因为它专门讲跨调用的前缀复用。

## 更底层的源头

- [存储层次（缓存）](memory-hierarchy.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [KV cache 的暴政：今天的 agent 只能"只追加对话"，由此带来路由失效、工具挤占上下文、压缩丢信息、子 agent 少等六个毛病（《Jev 工程学：为 coding agent 而作》中译介绍）](../clips/2026-10-25-yibie-jev-engineering-kv-cache-tyranny.md) | 相近 | 弱（模型复核通过） |
