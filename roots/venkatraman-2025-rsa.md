---
name_zh: "递归自聚合（RSA）：让大模型深度思考"
name_en: "Recursive Self-Aggregation Unlocks Deep Thinking in Large Language Models"
proposer: "Siddarth Venkatraman, Vineet Jain, Sarthak Mittal 等（含 Yoshua Bengio、Nikolay Malkin、Moksh Jain）"
year: "2025"
type: 论文
verified: true
---

# 递归自聚合（RSA）：让大模型深度思考（Recursive Self-Aggregation Unlocks Deep Thinking in Large Language Models）

## 一句话

一种受演化方法启发的测试时扩展：维护一群候选推理链，每一步把其中几条交给模型聚合成更好的新解，作为下一轮的候选池，兼得并行采样和串行自我改进的好处。

## 原始出处

- Recursive Self-Aggregation Unlocks Deep Thinking in Large Language Models, Siddarth Venkatraman 等, arXiv:2509.26626, 2025-09-30，https://arxiv.org/abs/2509.26626

## 更底层的源头

- [演化算法](evolutionary-algorithm.md) · 关系：直接源自
- [自洽性（多路径投票）](wang-2022-self-consistency.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Harness²：agent 不改模型，靠对照试验改自己的运行框架，还学会怎么改得更好](../clips/2026-10-19-xu-harness2-recursive-agent-harnessing.md) | 直接源自 | 强 |
