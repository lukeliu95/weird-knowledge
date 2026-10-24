---
name_zh: "演化策略：强化学习的可扩展替代"
name_en: "Evolution Strategies as a Scalable Alternative to Reinforcement Learning"
proposer: "Tim Salimans、Jonathan Ho、Xi Chen、Szymon Sidor、Ilya Sutskever（OpenAI）"
year: "2017"
type: 论文
verified: true
---

# 演化策略：强化学习的可扩展替代（Evolution Strategies as a Scalable Alternative to Reinforcement Learning）

## 一句话

不算梯度，只给参数加随机扰动、看结果好坏来估计改进方向（演化策略，一种黑箱优化、零阶优化）；用共享随机数让并行工人之间只传标量，能扩到上千个工人，在 MuJoCo 和 Atari 上和主流强化学习方法有竞争力。

## 原始出处

- Evolution Strategies as a Scalable Alternative to Reinforcement Learning, Tim Salimans, Jonathan Ho, Xi Chen, Szymon Sidor, Ilya Sutskever, arXiv:1703.03864, 2017（DOI 10.48550/arXiv.1703.03864），https://arxiv.org/abs/1703.03864
- Dust（Q Labs，2026-10）：把本文列为权重扰动演化策略的源头，https://qlabs.sh/research/dust
- 争议：演化策略本身是 1960–70 年代德国 Rechenberg 和 Schwefel 一派提出的（见演化算法词条）；本文的贡献是把它大规模并行化，当作强化学习的替代。

## 更底层的源头

- [演化算法](evolutionary-algorithm.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [不用反向传播预训练 Transformer，验证损失反超 Adam](../clips/2026-10-23-spicey-lemonade-pretrain-transformers-without-backprop.md) | 直接源自 | 强 |
