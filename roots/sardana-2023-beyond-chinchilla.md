---
name_zh: "超越 Chinchilla 最优：把推理成本算进缩放定律"
name_en: "Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws"
proposer: "Nikhil Sardana, Jacob Portes, Sasha Doubov, Jonathan Frankle"
year: "2023"
type: 论文
verified: true
---

# 超越 Chinchilla 最优：把推理成本算进缩放定律（Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws）

## 一句话

把推理成本算进总成本后，如果预期推理请求很多（约 10 亿次），就应该训练比 Chinchilla 最优更小、训练更久的模型；每个参数配的 token 数推到极端（到 1 万）时，质量仍在提升。

## 原始出处

- Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws, Sardana et al., 2023（ICML 2024），https://arxiv.org/abs/2401.00448

## 更底层的源头

- [训练算力最优的大语言模型（Chinchilla）](hoffmann-2022-compute-optimal.md) · 关系：直接源自
- [全生命周期成本（总拥有成本）](whole-life-cost.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [唐杰谈缩放定律：不只是堆参数](../clips/2026-10-18-jietang-scaling-law-beyond-parameters.md) | 直接源自 | 强 |
