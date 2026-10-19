---
title: "“随机缺失”不是“缺得很随机”：数据为什么缺，决定了能不能当它不存在"
author: "Shaun Seaman, John Galati, Dan Jackson, John Carlin"
url: https://doi.org/10.1214/13-STS415
source: 论文
published: "2013-05（Statistical Science 28(2): 257–268, DOI 10.1214/13-STS415）；所澄清的源头是 Rubin 1976（Biometrika 63(3): 581–592）"
saved: 2026-10-19
why: "补课：第 4 题 问题协商"
related_principles: []
status: 已整理
kind: 观点
topic: 学习与研究
roots: [missing-data-mechanisms, sampling-bias, closed-world-assumption]
adopted: false
---

## 原文

全文 13 页，arXiv 有免费版（[1306.2812](https://arxiv.org/abs/1306.2812)）。按规则只存要点。

- 标题：What Is Meant by "Missing at Random"?
- 源头：Rubin, Inference and Missing Data, Biometrika 63(3): 581–592, 1976, DOI [10.1093/biomet/63.3.581](https://doi.org/10.1093/biomet/63.3.581)（被引 9,907 次，OpenAlex）
- 被引：224 次（OpenAlex，2026-10-19 查）
- 读了多少：Seaman 等全文；Rubin 1976 只读了摘要（出版社页面有防机器人验证，没有绕过）

### 内容要点（模型概括，不是原文）

- Rubin 的结论（摘要）：分析时忽略"数据为什么缺"，一般只有在"随机缺失（MAR）"等条件下才恰当
- "随机缺失"的意思不是"缺得很随机"，而是：在已观测到的值相同的条件下，某个值缺不缺，和这个值本身是多少无关（§2）
- 文献里 MAR 有两种定义：只针对这一次实际出现的缺失（Rubin 原意），还是针对所有可能的缺失（后来多数人用的）；很多人用后者却引 Rubin 1976（§3）
- Rubin 1976 原文没有提"完全随机缺失（MCAR）"，他用的是"随机观测"（§3）
- "可以忽略缺失机制"常被误读成"数据缺了可以不管"（§1）

**需要说清楚的边界**

- 统计方法论文章，偏数学，不讨论企业数据
- 常见误传：MCAR / MAR / MNAR 三分法整套是 Rubin 1976 提出的。至少 MCAR 不是；MNAR 这个叫法最早出自谁没查到

## 溯源

- 核心主张：数据缺失的原因如果和缺掉的值本身有关，直接忽略缺失去分析就会得出偏的结论；“随机缺失”有严格的意思，不是“缺得很随机”。
- 源知识：
  - [缺失数据机制（随机缺失与可忽略性）](../roots/missing-data-mechanisms.md) · 关系：直接源自 · 强弱：强。就是对缺失数据机制定义的澄清。
  - [抽样偏差](../roots/sampling-bias.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。都是“看到的数据不是全体的随机样本”，原文没这样联系，是推断。
  - [封闭世界假设（及开放世界假设）](../roots/closed-world-assumption.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。一个是逻辑上“未知不等于假”，一个是统计上“缺失不能随便忽略”，原文没联系，是推断。
- 本质：这条新知识本质上是“看到的数据被什么筛过”这一问题在缺失值上的统计版本。
- 整理于：2026-10-19（补课第 4 题）
