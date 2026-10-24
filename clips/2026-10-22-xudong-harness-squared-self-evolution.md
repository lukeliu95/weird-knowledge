---
title: "Harness² 解读：没有标准答案时让新旧 harness 同条件对跑定去留，并把\"怎么改好自己\"沉淀成经验"
author: "@Xudong07452910"
url: https://x.com/Xudong07452910/status/2110574383622434939
source: X
published: 2026-10-15 03:32 UTC
saved: 2026-10-22
why: "探索日报：Luke 想看"
related_principles: [原则 1, 原则 5]
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [xu-2026-harness2, a-b-testing, organizational-learning, zhao-2023-expel, lee-2026-meta-harness]
---

## 原文

Agent 自己改 Harness，最难的其实并不是「怎么改」。

而在于没有标准答案时，怎么知道这次改动到底有没有变好。

Google 团队这篇 Harness²，专门研究开放世界里的 Harness 自进化。

它设计了两层递归。

第一层针对当前任务：先提出 Harness 修改，再让新旧版本在相同条件下执行，通过行为差异判断哪些改动值得保留。

也就是说，它不依赖 ground-truth verifier，也能用真实执行结果来指导修改。

第二层更有意思：

每次改 Harness 的过程也会被总结成经验，记录什么问题、用了什么修改、为什么有效，再拿去指导未来的新任务。

所以它积累的，不只是更好的 Harness，还有「怎么改 Harness」这件事本身。

在 WorkBuddy-Bench、JobBench 和法律 Agent Benchmark 上，单轮改进就能稳定提升 GLM-5 和 Gemini 3.5 Flash，最高分别提升 11.5、4.5 和 11.8 个百分点；继续增加递归预算，表现还能进一步上涨。

我更关注第二层递归。

单次把 Agent 调得更好并不难，真正接近长期自进化的，是系统开始积累「过去怎么把自己调好」的经验。

Harness² 往前走的一步，就是让改进机制本身也开始有记忆。

📎 arxiv: https://t.co/bMnlJm3dhA

> 媒体：
> - https://pbs.twimg.com/media/HUldQipXoAAazFx.jpg

## 溯源

- 核心主张：没有标准答案时，agent 改自己的 harness 可以让新旧版本在相同条件下各跑一遍、按行为差异决定留哪些改动；再把每次“遇到什么问题、改了什么、为什么有效”沉淀成经验去指导新任务，让改进机制本身也积累经验，这才更接近长期自进化。
- 源知识：
  - [Harness²：面向开放世界的递归 agent 运行框架改进](../roots/xu-2026-harness2.md) · 关系：直接源自 · 强弱：强。推文就是在解读这篇论文：两层递归、不依赖标准答案的对照试跑、WorkBuddy-Bench / JobBench / LAB 上最多 11.5、4.5、11.8 个点的提升都出自论文摘要。
  - [A/B 测试（在线对照实验）](../roots/a-b-testing.md) · 关系：相近 · 强弱：弱（模型复核通过）。“新旧版本同条件对跑、按结果差异定去留”就是对照实验（A/B 测试）的思路搬到 harness 修改上；推文和论文都没用这个词，是模型推断。
  - [组织学习](../roots/organizational-learning.md) · 关系：相近 · 强弱：弱（模型复核通过）。第一层只改做法（单环学习），第二层沉淀“怎么改做法”的经验（双环学习，Argyris 与 Schön）；推文没提组织学习，是模型推断的类比。
  - [ExpeL：大模型智能体是经验学习者](../roots/zhao-2023-expel.md) · 关系：相近 · 强弱：弱（模型复核通过）。把做过的事提炼成文字经验、新任务时取用，和第二层递归的经验库同构；推文没提 ExpeL，是模型推断。
  - [Meta-Harness：端到端优化模型的运行框架](../roots/lee-2026-meta-harness.md) · 关系：直接源自 · 强弱：弱（模型复核通过）。“让 agent 读以往改动和执行结果去自动改 harness”这条路由 Meta-Harness 开启，Harness² 论文把它当主要对照组；区别是 Meta-Harness 靠固定训练题打分。推文本身没提。
- 本质：这条新知识本质上是“同条件对照试验定去留”加上“连改进方法也一起学”的双环学习，在没有标准答案的 agent 运行框架自进化上的应用。
- 整理于：2026-10-24（第 6 轮）
