---
name_zh: "LoRA：大语言模型的低秩适配"
name_en: "LoRA: Low-Rank Adaptation of Large Language Models"
proposer: "Edward J. Hu、Yelong Shen、Phillip Wallis、Zeyuan Allen-Zhu、Yuanzhi Li、Shean Wang、Lu Wang、Weizhu Chen"
year: "2021"
type: 论文
verified: true
---

# LoRA：大语言模型的低秩适配（LoRA: Low-Rank Adaptation of Large Language Models）

## 一句话

微调大模型时把原来的权重冻住，只在旁边加一对很小的低秩矩阵来学“改动量”，可训练参数和显存大幅减少，效果和全量微调相当。

## 原始出处

- LoRA: Low-Rank Adaptation of Large Language Models, Hu et al., arXiv 2106.09685, 2021，https://arxiv.org/abs/2106.09685

## 更底层的源头

- [内在维度解释了语言模型微调为什么有效](aghajanyan-2020-intrinsic-dimensionality.md) · 关系：直接源自
- [低秩近似](low-rank-approximation.md) · 关系：直接源自
- [迁移学习（机器学习）](transfer-learning.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [开源工具让普通人也能微调 27B 模型](../clips/2026-10-18-minlibuilds-open-source-27b-finetune-unsloth.md) | 直接源自 | 强 |
