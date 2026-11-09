---
name_zh: "模型做语义判断，代码组合业务决定"
name_en: "Don't Call It a Decision Model"
proposer: "Allie Laabs（TypeSafe）"
year: "2026"
type: 方法论
verified: true
---

# 模型做语义判断，代码组合业务决定（Don't Call It a Decision Model）

## 一句话

把需要理解语义的问题拆成可观察的模型判断，再由代码执行已知规则、优先级和计算，让最终业务选择更容易检查和修改。

## 原始出处

- Allie Laabs，Don't Call It a Decision Model，TypeSafe 官方博客，2026-11-03；已读正文与退款流程示例。，https://typesafe.ai/blog/dont-call-it-a-decision-model
- Dijkstra，On the role of scientific thought，EWD447，1974；用于核对关注点分离的原意，不是声称 TypeSafe 作者引用过此文。，https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD447.html
- 争议：这是销售相关模型的厂商提出的工程建议，原文没有给出受控对照测评；其设计可以区分判断错与规则错，但不保证任何系统天然可靠，也不表示所有现实决策都能预写成确定规则。

## 更底层的源头

- [关注点分离](separation-of-concerns.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [TypeSafe：别把 Jev 叫决定模型——模型做判断，代码做决定](../clips/2026-11-07-allietheicon-dont-call-jev-a-decision-model.md) | 直接源自 | 强 |
