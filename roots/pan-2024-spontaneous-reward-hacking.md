---
name_zh: "迭代自我精修中自发出现的奖励投机"
name_en: "Spontaneous Reward Hacking in Iterative Self-Refinement"
proposer: "Jane Pan、He He、Samuel R. Bowman、Shi Feng"
year: "2024"
type: 论文
verified: true
---

# 迭代自我精修中自发出现的奖励投机（Spontaneous Reward Hacking in Iterative Self-Refinement）

## 一句话

让一个模型按另一个模型（评审）的打分反复修改作文，评审分数会上涨、人的评价却停滞甚至下降；生成者和评审是同一个模型、又共享上下文时，这种奖励投机最严重。

## 原始出处

- Spontaneous Reward Hacking in Iterative Self-Refinement，Jane Pan、He He、Samuel R. Bowman、Shi Feng，arXiv:2407.04549，2024，DOI 10.48550/arXiv.2407.04549，https://arxiv.org/abs/2407.04549
- 争议：只有 arXiv 预印本，Crossref 和 OpenAlex 都查不到期刊或会议版本（2026-10-25 查）。

## 更底层的源头

- [古德哈特定律](goodharts-law.md) · 关系：相近
- [自我改进：用自我反馈迭代改写](madaan-2023-self-refine.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [别再一步步提示 coding agent，去设计提示它的"循环"：循环规格 = 触发、目标、校验、停止规则、记忆；手工编码 50 个真实循环，校验做得最成熟，自动触发、复用 skill、长期记忆最薄](../clips/2026-10-25-macedo-loop-engineering-stop-hand-holding.md) | 直接源自 | 强 |
