---
title: "线索评分系统综述：预测型评分有效，但漂亮数字多来自厂商"
author: "Migao Wu, Pavel Andreev, Morad Benyoucef（渥太华大学）"
url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9890437/
source: 论文
published: "2023-02 在线（Information Technology and Management 25(1): 69–98, 2024, DOI 10.1007/s10799-023-00388-w）"
saved: 2026-10-19
why: "补课：第 4 题 问题协商"
related_principles: []
status: 已整理
kind: 观点
topic: 增长与获客
roots: [lead-scoring, decision-tree-learning, positive-unlabeled-learning]
adopted: false
---

## 原文

系统综述，PMC 有免费全文（上面的链接）。按规则只存要点。

- 标题：The state of lead scoring models and their impact on sales performance
- DOI：[10.1007/s10799-023-00388-w](https://doi.org/10.1007/s10799-023-00388-w)
- 被引：39 次（OpenAlex，2026-10-19 查）
- 读了多少：全文

### 内容要点（模型概括，不是原文）

- 方法：检索 6 个数据库共 1,150 条，精读 120 篇，纳入 44 篇（2005–2022 年，含 5 篇灰色文献）（"Methodology"一节、表 2、表 4）
- 评分分两类：传统型（靠销售和市场的经验打分）和预测型（用历史成交数据训练）；预测型里决策树和逻辑回归各 13 篇，最常用（表 3、表 5）
- 只有现有客户名单和潜在客户名单、没有成交标签时，可以用最近邻算法找"和现有客户相似"的潜在客户（"Classification"一节）
- 企业数据普遍有缺失；缺得多时，先对企业官网文本聚类、提取主题，再和不完整的数据一起建模。用官网文本后，转化率从 3.5% 提到 6.4%（"Impact"一节，转引 D'Haen 等）
- 作者指出的问题：传统评分研究普遍没有统计检验；预测评分只从卖方看漏斗，忽略买方怎么决策；模型常基于过时、不平衡的历史数据（"Discussion"一节）

**需要说清楚的边界**

- 只收 2005–2022 年英文文献，可能漏文献（"Limitations"一节）
- 很多吸引人的数字来自灰色文献：如"线索投资回报最多高 70%"转引厂商（Lattice）指南，"转化率平均提高 26%"转引咨询公司（Aberdeen）报告，不是独立研究
- 没有做定量合并，"预测型优于传统型"是定性归纳

## 溯源

- 核心主张：用历史成交数据训练的预测型线索评分比经验打分卡更常被证明有效；只有现有客户名单时可以找相似企业，企业官网文本能补数据缺口；但不少漂亮数字来自厂商。
- 源知识：
  - [线索评分](../roots/lead-scoring.md) · 关系：直接源自 · 强弱：强。就是线索评分的系统综述。
  - [决策树学习](../roots/decision-tree-learning.md) · 关系：相近 · 强弱：强。综述里最常用的算法之一。
  - [正例-未标注学习（PU 学习）](../roots/positive-unlabeled-learning.md) · 关系：相近 · 强弱：弱（模型复核通过）。“只有现有客户和潜在客户名单”正是 PU 情形，综述没用这个词，是推断。
- 本质：这条新知识本质上是“从已知好客户反推相似客户”在 B2B 获客里的实证现状。
- 整理于：2026-10-19（补课第 4 题）
