---
name_zh: "近端策略优化（PPO）"
name_en: "Proximal Policy Optimization Algorithms"
proposer: "John Schulman、Filip Wolski、Prafulla Dhariwal、Alec Radford、Oleg Klimov（OpenAI）"
year: "2017"
type: 论文
verified: true
---

# 近端策略优化（PPO）（Proximal Policy Optimization Algorithms）

## 一句话

一类策略梯度强化学习方法：和环境交互采一批数据，再用一个“截断”的替代目标做多轮小批量更新，防止每次把策略改得太猛；保留了 TRPO（信赖域策略优化）的稳定性但简单得多，后来成了大模型强化学习（如 RLHF）最常用的算法之一。

## 原始出处

- Proximal Policy Optimization Algorithms, John Schulman 等, 2017, arXiv:1707.06347，https://arxiv.org/abs/1707.06347
- Proximal policy optimization, Wikipedia，https://en.wikipedia.org/wiki/Proximal_policy_optimization
- 争议：PPO 是同一作者 2015 年 TRPO 的简化版，“限制每步改动幅度”的思路不是这篇首创，这篇的贡献是用截断目标把它做得简单好用。

## 更底层的源头

- [强化学习](reinforcement-learning.md) · 关系：直接源自
- [广义优势估计（GAE）](schulman-2015-gae.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Terminal-RSI：命令行 agent 拿自己验证过的成功经验反复训练自己，一轮比一轮强](../clips/2026-10-18-yang-terminal-rsi-recursive-self-improving-agents.md) | 直接源自 | 强 |
