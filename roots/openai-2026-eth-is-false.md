---
name_zh: "《指数时间假说是假的》公开稿及 Lean 范围说明"
name_en: "The Exponential Time Hypothesis is False"
proposer: "OpenAI内部模型产出；Impagliazzo、Paturi、Williams等组织外部核验"
year: "2026"
type: 论文
verified: true
---

# 《指数时间假说是假的》公开稿及 Lean 范围说明（The Exponential Time Hypothesis is False）

## 一句话

2026-10-25公开稿声称给出固定k的k-SAT及计数的次指数时间算法；Lean范围说明写明了形式化的计数、时间和空间界，外部社区核验仍在进行。

## 原始出处

- 公开稿，2026-10-25；本轮核对官方链接，未独立验证证明。，https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf
- Lean范围说明378.md：时间为(L+1)的多项式乘以2的O_k(n(loglog n)^2/sqrt(log n))次方，空间为(L+1)的多项式；稿件另给更尖锐时间界。，https://raw.githubusercontent.com/openai/math/main/lean/docs/378.md
- 2026-10-26官方发布与外部工作组安排。，https://openai.com/index/building-scientific-understanding-with-academic-communities/
- 争议：verified表示查到原始发布及形式化范围。本轮未运行Lean、未独立审稿。次指数不等于多项式，不意味着实用规模可快速求解；原来以ETH为前提的条件定理不会因此成为逻辑错误。

## 更底层的源头

- [指数时间假说（ETH）](exponential-time-hypothesis.md) · 关系：挑战
- [Lean 证明助手](lean-proof-assistant.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [通俗解释 OpenAI 的 ETH 反驳声称：次指数不等于实用可解，外部核验仍在进行](../clips/2026-10-29-rishabhkio-why-3sat-result-matters.md) | 直接源自 | 强 |
