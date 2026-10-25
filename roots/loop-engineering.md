---
name_zh: "循环工程（设计会提示 agent 的循环）"
name_en: "Loop engineering"
proposer: "Peter Steinberger 提出口号，Addy Osmani 命名并整理成做法"
year: "2026"
type: 方法论
verified: true
---

# 循环工程（设计会提示 agent 的循环）（Loop engineering）

## 一句话

不再由人一轮轮提示编程 agent，而是设计一个替人提示的循环：定好触发、目标、校验和停止规则，让它自己找活、分活、检查、记下进度再决定下一步；它位于外壳工程的上一层。

## 原始出处

- Loop Engineering，Addy Osmani，2026-06-07（引 Steinberger：“You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents.”），https://addyosmani.com/blog/loop-engineering/
- Stop Hand-Holding Your Coding Agent: Engineering the Loops that Replace Step-by-Step Prompting，Sandeco Macedo，arXiv:2607.00038，2026（第一份学术处理），https://arxiv.org/abs/2607.00038
- 争议：口号出自 Steinberger 2026 年 6 月在 X 上的帖子（据 Osmani 博文和 Barbaste 等 2026 文献 [31] 转引，原帖本次未直接打开）；Osmani 几天后命名为 loop engineering。Boris Cherny 同期也有类似说法。早一年的 Ralph 循环、Simon Willison 的“Designing agentic loops”（2025）是更早的实践。

## 更底层的源头

- [外壳工程（agent = 模型 + 外壳）](harness-engineering.md) · 关系：直接源自
- [Ralph Wiggum 循环](ralph-wiggum-technique.md) · 关系：相近
- [自主计算的愿景（监控-分析-计划-执行循环）](kephart-2003-autonomic-computing.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [别再一步步提示 coding agent，去设计提示它的"循环"：循环规格 = 触发、目标、校验、停止规则、记忆；手工编码 50 个真实循环，校验做得最成熟，自动触发、复用 skill、长期记忆最薄](../clips/2026-10-25-macedo-loop-engineering-stop-hand-holding.md) | 直接源自 | 强 |
