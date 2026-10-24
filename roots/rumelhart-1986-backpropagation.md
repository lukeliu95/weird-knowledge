---
name_zh: "反向传播（用误差反传学习表示）"
name_en: "Learning representations by back-propagating errors"
proposer: "David E. Rumelhart、Geoffrey E. Hinton、Ronald J. Williams"
year: "1986"
type: 论文
verified: true
---

# 反向传播（用误差反传学习表示）（Learning representations by back-propagating errors）

## 一句话

把输出误差按链式法则从后往前逐层传回，算出每个连接权重该怎么调，让多层网络的隐藏层自己学出有用的内部表示；这成了此后训练神经网络（包括今天的大模型）的标准方法。

## 原始出处

- Learning representations by back-propagating errors, David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams, Nature 323(6088): 533–536, 1986，https://doi.org/10.1038/323533a0
- Backpropagation, 英文维基百科（历史一节），https://en.wikipedia.org/wiki/Backpropagation
- 争议：多次独立发现，发明权有争议：Kelley 1960、Bryson 1961 在最优控制里已有前身；Linnainmaa 1970 首次发表“自动微分的反向模式”；Werbos 1974 年博士论文提出、1982 年以标准方式用于多层感知机；Parker 1985、LeCun 1987 也各自提出。Rumelhart 等 1986 年的 Nature 论文让它广为人知（以上据维基百科）。

## 更底层的源头

- 已追到基础层，或暂未找到更底层的源头

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [不用反向传播预训练 Transformer，验证损失反超 Adam](../clips/2026-10-23-spicey-lemonade-pretrain-transformers-without-backprop.md) | 挑战 | 强 |
