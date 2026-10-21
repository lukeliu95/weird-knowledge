---
name_zh: "惰性学习（对照：积极学习）"
name_en: "Lazy learning"
proposer: "无单一提出者；David W. Aha 1997 年主编《Lazy Learning》专辑并写导言"
year: "1997"
type: 方法论
verified: true
---

# 惰性学习（对照：积极学习）（Lazy learning）

## 一句话

先把训练数据原样存着，等查询来了才针对这个查询做局部的泛化（如 k 近邻）；和“积极学习”相对，后者在收到查询前就把数据泛化成一个固定模型。适合数据不断更新、每次查询只关心少数属性的场景。

## 原始出处

- Lazy learning, 英文维基百科，https://en.wikipedia.org/wiki/Lazy_learning
- Editorial, David W. Aha, in Lazy Learning (Springer, 1997, pp. 7–10；同为 Artificial Intelligence Review 第 11 卷专辑)，https://doi.org/10.1007/978-94-017-2053-3_1
- 争议：维基没写这个术语的提出者；k 近邻、基于实例的学习、案例推理等做法都早于“惰性学习”这个统称，1997 年 Aha 主编的专辑是较早集中使用这个名字的文献，是否首提待确认。

## 更底层的源头

- [案例推理（基于案例的推理）](case-based-reasoning.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [agent 的记忆先存原始轨迹，等新任务来了再现场整理，比事先提炼成反思或 skill 更好用](../clips/2026-10-20-zhou-just-in-time-memory.md) | 相近 | 弱（模型复核通过） |
