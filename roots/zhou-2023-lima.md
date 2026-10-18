---
name_zh: "LIMA：对齐少即是多（表层对齐假说）"
name_en: "LIMA: Less Is More for Alignment"
proposer: "Chunting Zhou、Pengfei Liu、Puxin Xu 等 15 人（Meta 等）"
year: "2023"
type: 论文
verified: true
---

# LIMA：对齐少即是多（表层对齐假说）（LIMA: Less Is More for Alignment）

## 一句话

只用 1000 条精心挑选的问答给 65B 的 LLaMa 做监督微调、不做强化学习，效果就很强；作者据此认为大模型的知识几乎都在预训练时学到，后训练只需少量数据教它用什么样的格式说话（表层对齐假说）。

## 原始出处

- LIMA: Less Is More for Alignment, Chunting Zhou 等, 2023, arXiv:2305.11206，https://arxiv.org/abs/2305.11206
- 争议：“后训练只教格式”这一结论后来受到质疑：大规模强化学习（如 DeepSeek-R1）带来的推理和 agent 能力提升，被不少人看作后训练分量远不止于此的证据，目前仍有争论。

## 更底层的源头

- [迁移学习（机器学习）](transfer-learning.md) · 关系：相近
- [内在维度解释了语言模型微调为什么有效](aghajanyan-2020-intrinsic-dimensionality.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [GLM 5.3 只靠后训练大涨，被 SemiAnalysis 嘉宾称为警钟](../clips/2026-10-18-nft-chen-glm-5-3-post-training-wake-up-call.md) | 相近 | 弱（待 Luke 确认） |
