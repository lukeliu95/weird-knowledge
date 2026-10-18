---
name_zh: "IMPALA：可扩展的分布式深度强化学习"
name_en: "IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures"
proposer: "Lasse Espeholt 等（DeepMind）"
year: "2018"
type: 论文
verified: true
---

# IMPALA：可扩展的分布式深度强化学习（IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures）

## 一句话

把负责采样的“演员”和负责更新参数的“学习者”拆开并行跑，采样用的策略会落后于最新策略，用 V-trace 做离策略修正来保持训练稳定。

## 原始出处

- IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures, Espeholt et al., 2018 (arXiv 1802.01561)，https://arxiv.org/abs/1802.01561

## 更底层的源头

- [强化学习](reinforcement-learning.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [MiMo-V2.6 的强化学习之路](../clips/2026-10-18-luofuli-mimo-v2-6-scaling-rl.md) | 相近 | 弱（待 Luke 确认） |
