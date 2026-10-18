---
name_zh: "从闭源大模型 API 里偷出推理过程（加密思维链的跨模型重放）"
name_en: "Stealing Reasoning Traces from Proprietary LLM APIs"
proposer: "Alexander Panfilov、David Schmotz、Ilia Shumailov、Luca Beurer-Kellner、Joachim Schaeffer、Ameya Prabhu、Jonas Geiping、Maksym Andriushchenko"
year: "2026"
type: 论文
verified: true
---

# 从闭源大模型 API 里偷出推理过程（加密思维链的跨模型重放）（Stealing Reasoning Traces from Proprietary LLM APIs）

## 一句话

厂商把模型的隐藏推理加密后交给客户端，但同一家的加密块在会话、用户、模型之间都通用；把强模型的加密块注入同家更弱、防护更松的模型，就能让它原样解出明文，可用来偷推理做蒸馏、从公开日志里挖出个人信息和密钥、看到被拒答案背后的危险内容，还能做隐形的提示注入。

## 原始出处

- Stealing Reasoning Traces from Proprietary LLM APIs, Panfilov et al., arXiv 2608.09867, 2026，https://arxiv.org/abs/2608.09867
- Simon Willison 对这篇论文的介绍，2026-08-11，https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/
- 争议：论文自己说是在 Matthew Green 2026 年 5 月博文《Let's talk about encrypted reasoning》的基础上做的：加密块能跨会话重放是 Green 先公开的，跨模型解密和规模化攻击是这篇论文的新贡献。论文说厂商在收到披露后已在服务器端修补。

## 更底层的源头

- [通过预测 API 窃取机器学习模型（模型窃取攻击）](tramer-2016-stealing-ml-models.md) · 关系：直接源自
- [重放攻击](replay-attack.md) · 关系：直接源自
- [知识蒸馏](knowledge-distillation.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [论文从闭源模型里偷出隐藏思维链](../clips/2026-10-18-maxforai-stealing-hidden-chain-of-thought.md) | 直接源自 | 强 |
