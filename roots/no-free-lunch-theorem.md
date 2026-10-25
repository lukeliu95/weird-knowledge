---
name_zh: "没有免费午餐定理（优化）"
name_en: "No free lunch theorems for optimization"
proposer: "David H. Wolpert、William G. Macready"
year: "1997"
type: 定律
verified: true
---

# 没有免费午餐定理（优化）（No free lunch theorems for optimization）

## 一句话

把所有可能的问题平均起来，任何两个优化算法表现一样；一个算法在某一类问题上更好，必然在其余问题上付出代价。所以不存在通吃的算法，只能按问题的结构去匹配方法。

## 原始出处

- No Free Lunch Theorems for Optimization，D. H. Wolpert、W. G. Macready，IEEE Transactions on Evolutionary Computation 1(1)，1997，https://doi.org/10.1109/4235.585893
- The Lack of A Priori Distinctions Between Learning Algorithms，David H. Wolpert，Neural Computation 8(7)，1996（监督学习版），https://doi.org/10.1162/neco.1996.8.7.1341
- No free lunch theorem，维基百科，https://en.wikipedia.org/wiki/No_free_lunch_theorem
- 争议：Wolpert 1996 年先在机器学习（监督学习）里推出同类结论，1997 年与 Macready 合写的是优化版；两者常被统称为“没有免费午餐定理”。

## 更底层的源头

- [归纳问题](problem-of-induction.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [agent 的外壳代码按"类继承"分家：按任务的共同毛病长出一族专用外壳，先跑一遍通用版看出毛病再挑；比只练一个全局外壳分数高、搜索快](../clips/2026-10-25-li-object-oriented-harness.md) | 相近 | 弱（模型复核通过） |
