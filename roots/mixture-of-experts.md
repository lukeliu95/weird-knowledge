---
name_zh: "混合专家"
name_en: "Mixture of experts"
proposer: "Robert A. Jacobs 等"
year: "1991"
type: 方法论
verified: true
---

# 混合专家（Mixture of experts）

## 一句话

用多个专家网络各管问题空间的一块，由门控决定每个输入交给哪个专家；是集成学习的一种。

## 原始出处

- Wikipedia: Mixture of experts，https://en.wikipedia.org/wiki/Mixture_of_experts
- Adaptive Mixtures of Local Experts, Robert A. Jacobs 等, Neural Computation, 1991，https://openalex.org/W2150884987
- Adaptive Mixtures of Local Experts, Jacobs, Jordan, Nowlan, Hinton, Neural Computation, 1991，https://doi.org/10.1162/neco.1991.3.1.79
- Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer, Shazeer et al., 2017，https://arxiv.org/abs/1701.06538

## 更底层的源头

- [集成学习](ensemble-learning.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Anthropic 六种工作流与智能体](../clips/2026-10-18-eze-is-1-anthropic-workflow-patterns.md) | 相近 | 弱（待 Luke 确认） |
| [唐杰谈缩放定律：不只是堆参数](../clips/2026-10-18-jietang-scaling-law-beyond-parameters.md) | 直接源自 | 强 |
