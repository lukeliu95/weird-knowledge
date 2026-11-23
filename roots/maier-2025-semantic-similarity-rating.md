---
name_zh: "语义相似度打分（SSR）：大模型复现真人购买意向"
name_en: "LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings"
proposer: "Benjamin F. Maier 等 9 人（7 人来自 PyMC Labs，Robbie Dow、Kli Pappas 来自 Colgate-Palmolive）"
year: "2025"
type: 论文
verified: true
---

# 语义相似度打分（SSR）：大模型复现真人购买意向（LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings）

## 一句话

让大模型按人口属性扮演顾客，先写对新品概念的自由感想，再按和几句参考语句的语义相似度换算成 1～5 分的分布；在 57 个美国个护新品概念调查（9,300 名真人）上，各概念平均购买意向的排序相关达到真人重测上限的约 90%，分布形状也像真人；直接让模型打数字只会扎堆在 3 分。

## 原始出处

- LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings, Maier et al., arXiv:2510.08338, 2025-10（v3 2025-10-27），https://arxiv.org/abs/2510.08338
- HTML 全文 v3，https://arxiv.org/html/2510.08338v3
- 争议：数据由「一家领先的个护公司」提供，论文没点名；作者在第 5 节说它「不是对真人调研的全面替代」，参考语句是在这 57 个调查上手工调的，换领域效果未知

## 更底层的源头

- [硅基抽样：用语言模型模拟人群样本（算法保真度）](argyle-2023-out-of-one-many.md) · 关系：直接源自
- [用大模型做市场调研（支付意愿模拟）](brand-2023-using-gpt-market-research.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [PyMC Labs 与高露洁论文：大模型扮演顾客，购买意向排序达真人重测信度的九成](../clips/2026-11-22-howtoprompt-colgate-llm-synthetic-consumer-ssr.md) | 直接源自 | 强 |
