---
name_zh: "时序差分学习"
name_en: "Temporal difference learning"
proposer: "Richard S. Sutton（形式化）"
year: "1988"
type: 方法论
verified: true
---

# 时序差分学习（Temporal difference learning）

## 一句话

不等最终结果出来，而是用「后一时刻的预测」去修正「前一时刻的预测」，靠相邻两次预测之间的差值来学习。

## 原始出处

- Learning to Predict by the Methods of Temporal Differences, Richard S. Sutton, 1988, Machine Learning，https://doi.org/10.1007/BF00115009
- Reinforcement Learning: An Introduction, Sutton & Barto, 1.6 History of Reinforcement Learning，http://incompleteideas.net/book/first/ebook/node12.html
- 争议：Sutton 1988 自己说这类方法之前已出现在 Samuel 的跳棋程序、Holland 的 bucket brigade 和他自己的 Adaptive Heuristic Critic 里；Sutton & Barto 说 Samuel 1959 是第一个提出并实现含时序差分思想的学习方法的人。

## 更底层的源头

- [效果律](law-of-effect.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Samuel 的跳棋程序：机器靠自己对弈学习，下得比写它的人还好](../clips/2026-10-18-samuel-machine-learning-checkers.md) | 相近 | 强 |
