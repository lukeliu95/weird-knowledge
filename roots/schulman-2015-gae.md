---
name_zh: "广义优势估计（GAE）"
name_en: "High-Dimensional Continuous Control Using Generalized Advantage Estimation"
proposer: "John Schulman、Philipp Moritz、Sergey Levine、Michael Jordan、Pieter Abbeel"
year: "2015"
type: 论文
verified: true
---

# 广义优势估计（GAE）（High-Dimensional Continuous Control Using Generalized Advantage Estimation）

## 一句话

估计“这一步比平均水平好多少”（优势）时，用价值函数把后面多步的时序差分误差按指数加权加起来，用一个参数 λ 在“偏差小但噪声大”和“噪声小但有偏差”之间调节；做法类似 TD(λ)，能大幅降低策略梯度的噪声。

## 原始出处

- High-Dimensional Continuous Control Using Generalized Advantage Estimation, John Schulman 等, 2015, arXiv:1506.02438，https://arxiv.org/abs/1506.02438

## 更底层的源头

- [时序差分学习](temporal-difference-learning.md) · 关系：直接源自
- [强化学习](reinforcement-learning.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Terminal-RSI：命令行 agent 拿自己验证过的成功经验反复训练自己，一轮比一轮强](../clips/2026-10-18-yang-terminal-rsi-recursive-self-improving-agents.md) | 直接源自 | 强 |
