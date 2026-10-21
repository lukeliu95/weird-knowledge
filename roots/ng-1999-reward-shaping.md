---
name_zh: "奖励塑形（势函数塑形下的策略不变性）"
name_en: "Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping"
proposer: "Andrew Y. Ng、Daishi Harada、Stuart Russell"
year: "1999"
type: 论文
verified: true
---

# 奖励塑形（势函数塑形下的策略不变性）（Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping）

## 一句话

奖励太稀疏时可以额外加“塑形奖励”帮智能体更快学会；只要塑形奖励写成状态势函数之差，最优策略就不会被改变，其他形式的塑形可能把智能体带偏。

## 原始出处

- Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping, Ng, Harada, Russell, ICML 1999, pp. 278–287，https://mlanthology.org/icml/1999/ng1999icml-policy/
- Shaping (psychology), Wikipedia（“塑形”最早是 Skinner 训练鸽子的方法），https://en.wikipedia.org/wiki/Shaping_(psychology)
- 争议：“塑形”这个概念来自 Skinner 的动物训练；这篇的贡献是给出不改变最优策略的塑形条件，不是第一次提出塑形。

## 更底层的源头

- [强化学习](reinforcement-learning.md) · 关系：直接源自
- [操作性条件反射](operant-conditioning.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [智谱让 GLM-5.3 自己优化推理系统](../clips/2026-10-18-dotey-glm-5-3-optimizes-own-inference.md) | 相近 | 弱（模型复核通过） |
| [Terminal-RSI：命令行 agent 拿自己验证过的成功经验反复训练自己，一轮比一轮强](../clips/2026-10-18-yang-terminal-rsi-recursive-self-improving-agents.md) | 直接源自 | 强 |
