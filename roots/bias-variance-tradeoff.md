---
name_zh: "偏差-方差权衡"
name_en: "Bias–variance tradeoff"
proposer: "Stuart Geman, Elie Bienenstock, René Doursat（神经网络语境下的“偏差/方差困境”）"
year: "1992"
type: 理论
verified: true
---

# 偏差-方差权衡（Bias–variance tradeoff）

## 一句话

模型越灵活，偏差越小但方差越大；数据少时要靠先验（偏置）压住方差，数据足够多时才能放开让模型自己学。

## 原始出处

- Bias–variance tradeoff，英文维基百科（含 Geman 等认为通用物体识别需要一定“硬连线”，否则训练集要大到不现实），https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff
- Neural Networks and the Bias/Variance Dilemma, Geman, Bienenstock, Doursat, Neural Computation 4(1):1–58, 1992，https://doi.org/10.1162/neco.1992.4.1.1
- 争议：偏差与方差的分解在统计学里更早就有，Geman 等 1992 年的论文把它作为“困境”带进神经网络讨论；他们当时认为物体识别必须预先写入结构，Sora 一类结果则说明数据和算力足够大时这一判断可以被推翻。

## 更底层的源头

- 已追到基础层，或暂未找到更底层的源头

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
