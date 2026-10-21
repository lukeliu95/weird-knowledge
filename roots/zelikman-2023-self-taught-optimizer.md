---
name_zh: "自学优化器（STOP）：递归自我改进的代码生成"
name_en: "Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation"
proposer: "Eric Zelikman, Eliana Lorch, Lester Mackey, Adam Tauman Kalai"
year: "2023"
type: 论文
verified: true
---

# 自学优化器（STOP）：递归自我改进的代码生成（Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation）

## 一句话

让一个调用固定大模型的「改进器」程序去改进自己，脚手架代码一轮轮变好而模型权重不变；模型自己提出了束搜索、遗传算法、模拟退火等策略。

## 原始出处

- Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation, Zelikman 等, 2023, arXiv:2310.02304，https://arxiv.org/abs/2310.02304

## 更底层的源头

- [递归自我改进](recursive-self-improvement.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Dream-RSI：回放里做梦改策略](../clips/2026-10-18-maxforai-dream-rsi-replay-simulator.md) | 相近 | 弱（模型复核通过） |
| [Harness²：agent 不改模型，靠对照试验改自己的运行框架，还学会怎么改得更好](../clips/2026-10-19-xu-harness2-recursive-agent-harnessing.md) | 直接源自 | 强 |
