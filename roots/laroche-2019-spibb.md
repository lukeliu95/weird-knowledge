---
name_zh: "带基线自举的安全策略改进（SPIBB）"
name_en: "Safe Policy Improvement with Baseline Bootstrapping"
proposer: "Romain Laroche, Paul Trichelair, Rémi Tachet des Combes"
year: "2019"
type: 论文
verified: true
---

# 带基线自举的安全策略改进（SPIBB）（Safe Policy Improvement with Baseline Bootstrapping）

## 一句话

只有一批旧数据、不能再试错时，训练出的新策略要保证不比收集数据的旧策略差：数据里证据不足、不确定性高的地方，就沿用旧策略的做法，只在有把握的地方改。

## 原始出处

- Safe Policy Improvement with Baseline Bootstrapping, Romain Laroche, Paul Trichelair, Rémi Tachet des Combes, ICML 2019, PMLR 97: 3652–3661，https://proceedings.mlr.press/v97/laroche19a.html
- 同上，arXiv:1712.06924，https://arxiv.org/abs/1712.06924
- 争议：“改进不能比现有策略差”的安全策略改进思路更早已有，例如 Thomas 等 2015 的高置信离线策略评估（Designer-RSI 两篇并引）；SPIBB 是其中用“不确定处沿用基线”实现的一种。

## 更底层的源头

- [强化学习](reinforcement-learning.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [模型不动，只让技能库从用户请求里长：设计 agent 的技能从 76 个长到 139 个](../clips/2026-10-20-du-designer-rsi-procedural-memory.md) | 直接源自 | 强 |
