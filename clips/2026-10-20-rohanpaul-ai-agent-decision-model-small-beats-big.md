---
title: "agent 每步的选择题交给小决策模型（UIUC 等，推文误作普林斯顿和谷歌），模拟网店里 4B 模型完成率 91.5%"
author: "Rohan Paul (@rohanpaul_ai)"
url: https://x.com/rohanpaul_ai/status/2112107486098473471
source: X
published: 2026-10-19 09:04 UTC
saved: 2026-10-20
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [chen-2023-frugalgpt, geifman-2017-selective-classification, ross-2011-dagger, knowledge-distillation, dual-process-theory]
---

## 原文

New Princeton Univ +  Google paper finds that the decision model most accurate on isolated questions solved only 69.5% of agent tasks, while a 4B model trained on agent states solved 91.5%.

Agent harnesses call a big LLM at every step, which makes long tasks slow and costly. Yet most of those calls just pick from a list, like which tool to use next.

Their harness asks a fast decision model each multiple-choice question and uses its answer only above a confidence threshold fitted on the agent's own runs. They also trained AgentDecision-4B on states the agent actually reaches, including after its own mistakes.

On tasks like their training data, 4B models trained this way made agents 81.1% to 89.0% cheaper and up to 2.5x faster. Success stayed within 3 points, while handing over every tool choice with no threshold lowered success by 19.0 points.

To hand routine agent choices to a small model, train it and set its confidence threshold on your agent's own runs.

– arxiv. org/abs/2610.21412

Title: "JevAgentHarness: Benchmarking, Deploying and Training Decision Models That Share Control with LLMs"

> 媒体：
> - https://pbs.twimg.com/media/HU-owJPbsAA_oce.jpg

## 溯源

- 核心主张：agent 每一步的大模型调用多数其实是选择题（比如下一步用哪个工具），可以交给又快又便宜的小决策模型；但要在 agent 自己的运行记录上为每类选择拟合置信度门槛、低于门槛仍交给大模型，并用 agent 真实会走到的状态（包括犯错之后的状态）训练小模型，才能省钱提速而基本不掉成功率。
- 源知识：
  - [FrugalGPT：用级联大模型省钱又提效](../roots/chen-2023-frugalgpt.md) · 关系：直接源自 · 强弱：强。论文把“路由和级联”（Chen 等 2024，即 FrugalGPT）列为最接近的前作：便宜的模型先答，可靠就用、不可靠再交给贵的；JevAgentHarness 的级联模式就是把它搬到 agent 每一步的选择上。
  - [深度神经网络的选择性分类（带拒答选项）](../roots/geifman-2017-selective-classification.md) · 关系：直接源自 · 强弱：强。论文第 8 节明说决策模型“拿不准就交回”像选择性分类和学会交回（Geifman 与 El-Yaniv 2017；Mozannar 与 Sontag 2020）；附录 A 的门槛规则也是“接受的期望损失小于交回的就接受”。
  - [DAgger：把模仿学习化为无悔在线学习（在自己会走到的状态上学）](../roots/ross-2011-dagger.md) · 关系：直接源自 · 强弱：强。论文第 5 节为了让训练数据包含“犯错之后的状态”（占 30.9%），明引 Ross 等 2011（DAgger）；在 agent 自己会走到的状态上训练，正是 DAgger 治“训练时只见过专家走的路”的办法。不同在于这里用脚本重放开发时见过的错误来造这些状态，不是让学生模型自己去跑。
  - [知识蒸馏](../roots/knowledge-distillation.md) · 关系：直接源自 · 强弱：强。AgentDecision-4B 的监督微调以 Jev 为“老师”：Jev 把正确答案排第一时，目标是标准答案（占 0.3）和 Jev 各选项概率（占 0.7）的混合软标签，否则只用标准答案（第 5 节）；这是标准的“老师带学生”式知识蒸馏，摘要原话是“用 Jev 的答案当标签”。
  - [双过程理论（系统一 / 系统二）](../roots/dual-process-theory.md) · 关系：相近 · 强弱：强。论文第 1 节明说决策模型直接给选项打分，像卡尼曼说的快而直觉的系统一，而大模型逐字生成像慢而费力的系统二；只是类比。
- 本质：这条新知识本质上是“级联加拒答选项”（便宜的先判、拿不准就交回贵的）在 agent 每一步工具选择上的应用，再加上 DAgger 式的“在自己会走到的状态上训练”。
- 整理于：2026-10-21（第 4 轮）
