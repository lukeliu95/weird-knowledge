---
name_zh: "推理任务下 MoE 的最优稀疏度"
name_en: "Optimal Sparsity of Mixture-of-Experts Language Models for Reasoning Tasks"
proposer: "Taishi Nakamura, Satoki Ishikawa, Masaki Kawamura, Takumi Okamoto, Daisuke Nohara, Jun Suzuki, Rio Yokota"
year: "2025"
type: 论文
verified: true
---

# 推理任务下 MoE 的最优稀疏度（Optimal Sparsity of Mixture-of-Experts Language Models for Reasoning Tasks）

## 一句话

训练损失相同时，激活计算量越大，推理越准；记忆类任务随参数增多而提升，推理类任务则需要合适的每参数 token 数，也就是推理更吃数据。强化学习后训练和增加测试时算力都改变不了这些趋势。

## 原始出处

- Optimal Sparsity of Mixture-of-Experts Language Models for Reasoning Tasks, Nakamura et al., 2025（ICLR 2026 oral），https://arxiv.org/abs/2508.18672

## 更底层的源头

- [混合专家](mixture-of-experts.md) · 关系：直接源自
- [技能的算力最优缩放：知识与推理](roberts-2025-compute-optimal-skills.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [唐杰谈缩放定律：不只是堆参数](../clips/2026-10-18-jietang-scaling-law-beyond-parameters.md) | 直接源自 | 弱（待 Luke 确认） |
