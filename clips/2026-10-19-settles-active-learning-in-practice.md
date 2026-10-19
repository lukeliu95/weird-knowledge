---
title: "主动学习在实际使用中的六个问题：一批样本要彼此不同，问“这个条件要不要”可能更省时间"
author: "Burr Settles（卡内基梅隆大学）"
url: https://proceedings.mlr.press/v16/settles11a.html
source: 论文
published: "2011（JMLR Workshop and Conference Proceedings / PMLR 16: 1–18，没有 DOI）"
saved: 2026-10-19
why: "补课：第 4 题 问题协商"
related_principles: []
status: 已整理
kind: 观点
topic: 学习与研究
roots: [active-learning-machine-learning, sampling-bias, optimal-experimental-design]
adopted: false
---

## 原文

综述论文，免费公开（[PDF](http://proceedings.mlr.press/v16/settles11a/settles11a.pdf)）。按规则只存要点。

- 标题：From Theories to Queries: Active Learning in Practice
- 被引：223 次（OpenAlex，2026-10-19 查）
- 读了多少：全文

### 内容要点（模型概括，不是原文）

- 主动学习（让模型挑最拿不准的样本去问人）在论文里效果很好，真实项目里却"好坏参半"：一份标注项目调查里只有 20% 的人用过，不用的人里 21% 认为它省不了总时间（§1）
- 一次问一批时，不能只挑信息量最高的前 N 条，它们往往几乎一样；一批里的样本要既有信息量又彼此不同（§2.1）
- 标注的人会出错、会累，同一条样本对不同人难度不同（§2.2）
- 每条标注的成本不一样，按"不确定性除以成本"来挑，在多个任务上并没比随机好（§2.3.2）
- 可以不问"这条是不是"，改问"这个特征重不重要"。作者转述 Raghavan 等 2006：给特征打标签只要给文档打标签约五分之一的时间（§2.4.2）
- 主动学习挑出的训练集是被当时的模型带偏的，以后换模型就不一定合用（§2.6）

**需要说清楚的边界**

- 2011 年的综述，结论多来自自然语言处理和生物实验，不是人做商业决策
- "五分之一时间"是转述 Raghavan 等 2006，原文没读，未核实
- 常见误传："主动学习一定省标注"。原文的立场是：实验室假设下大体成立，真实项目里不一定

## 溯源

- 核心主张：主动学习在真实项目里不一定省事：一批要问的样本要彼此不同，标注的人会出错，按成本挑也不一定比随机好；改问“这个条件要不要”可能比问“这一条是不是”更省人。
- 源知识：
  - [主动学习](../roots/active-learning-machine-learning.md) · 关系：直接源自 · 强弱：强。就是主动学习的实践综述。
  - [抽样偏差](../roots/sampling-bias.md) · 关系：相近 · 强弱：强。§2.6 明说主动学习挑出的标注集不是随机样本。
  - [最优实验设计](../roots/optimal-experimental-design.md) · 关系：相近 · 强弱：强。§2.1 用实验设计的思路挑一批样本。
- 本质：这条新知识本质上是主动学习从实验室走到真实场景时的修正清单。
- 整理于：2026-10-19（补课第 4 题）
