---
name_zh: "ReST-EM：超越人类数据，扩展自我训练来解题"
name_en: "Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models"
proposer: "Avi Singh、John D. Co-Reyes、Rishabh Agarwal 等（Google DeepMind）"
year: "2023"
type: 论文
verified: true
---

# ReST-EM：超越人类数据，扩展自我训练来解题（Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models）

## 一句话

在能自动判对错的任务（数学、写代码）上，让模型自己生成答案、用对/错二元反馈过滤、拿留下的答案微调，重复几轮；作者把这个做法解释为期望最大化（EM）算法，发现效果随模型变大而变好，明显超过只用人类数据微调。

## 原始出处

- Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models, Avi Singh 等, 2023, arXiv:2312.06585（TMLR 接收），https://arxiv.org/abs/2312.06585

## 更底层的源头

- [ReST：强化自训练（用自己生成的数据做离线强化学习）](gulcehre-2023-rest.md) · 关系：直接源自
- [期望最大化算法（EM 算法）](expectation-maximization-algorithm.md) · 关系：直接源自
- [STaR：用推理自举推理（自学推理者）](zelikman-2022-star.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Terminal-RSI：命令行 agent 拿自己验证过的成功经验反复训练自己，一轮比一轮强](../clips/2026-10-18-yang-terminal-rsi-recursive-self-improving-agents.md) | 直接源自 | 强 |
