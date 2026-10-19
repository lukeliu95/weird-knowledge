---
name_zh: "主动学习"
name_en: "Active learning (machine learning)"
proposer: "没有单一提出者（Angluin 1988 成员查询；Lewis & Gale 1994 不确定性抽样；Settles 2009 综述）"
year: "1988–2009"
type: 方法论
verified: true
---

# 主动学习（Active learning (machine learning)）

## 一句话

让学习算法自己挑出最有信息量的样本去问人要标签（比如模型最拿不准、相关概率最接近 0.5 的样本），用更少的标注达到同样的准确率。

## 原始出处

- Active Learning Literature Survey, Burr Settles, 2009（University of Wisconsin–Madison TR 1648），https://research.cs.wisc.edu/techreports/2009/TR1648.pdf
- A Sequential Algorithm for Training Text Classifiers, David D. Lewis & William A. Gale, 1994，https://doi.org/10.1007/978-1-4471-2099-5_1
- Active learning (machine learning), Wikipedia，https://en.wikipedia.org/wiki/Active_learning_(machine_learning)
- 争议：没有公认的单一提出者：Settles 综述说它也叫「查询学习」，在统计学里叫「最优实验设计」；最早研究的场景之一是 Angluin 1988 的成员查询，不确定性抽样出自 Lewis & Gale 1994。Settles 是综述作者，不是首创者。

## 更底层的源头

- [最优实验设计](optimal-experimental-design.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [AIDE：让用户给样本打"相关/不相关"，用主动学习猜出他真正想查的数据](../clips/2026-10-18-dimitriadou-aide-active-learning-data-exploration.md) | 直接源自 | 强 |
| [主动学习在实际使用中的六个问题：一批样本要彼此不同，问“这个条件要不要”可能更省时间](../clips/2026-10-19-settles-active-learning-in-practice.md) | 直接源自 | 强 |
