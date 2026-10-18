---
name_zh: "ReST：强化自训练（用自己生成的数据做离线强化学习）"
name_en: "Reinforced Self-Training (ReST) for Language Modeling"
proposer: "Caglar Gulcehre、Tom Le Paine、Srivatsan Srinivasan 等 14 人（Google DeepMind）"
year: "2023"
type: 论文
verified: true
---

# ReST：强化自训练（用自己生成的数据做离线强化学习）（Reinforced Self-Training (ReST) for Language Modeling）

## 一句话

受“分批增长的强化学习”启发：先用当前模型生成一批样本（生长），再按奖励筛选、用离线强化学习改进模型（改进），循环往复；数据离线生成、可以反复使用，所以比在线 RLHF 省算力，论文以机器翻译为例验证。

## 原始出处

- Reinforced Self-Training (ReST) for Language Modeling, Caglar Gulcehre 等, 2023, arXiv:2308.08998，https://arxiv.org/abs/2308.08998

## 更底层的源头

- [强化学习](reinforcement-learning.md) · 关系：直接源自
- [基于人类反馈的强化学习（RLHF）](reinforcement-learning-from-human-feedback.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Terminal-RSI：命令行 agent 拿自己验证过的成功经验反复训练自己，一轮比一轮强](../clips/2026-10-18-yang-terminal-rsi-recursive-self-improving-agents.md) | 直接源自 | 强 |
