---
title: "Harness² 解读：没有标准答案时让新旧 harness 同条件对跑定去留，并把\"怎么改好自己\"沉淀成经验"
author: "@Xudong07452910"
url: https://x.com/Xudong07452910/status/2110574383622434939
source: X
published: 2026-10-15 03:32 UTC
saved: 2026-10-22
why: "探索日报：Luke 想看"
related_principles: [原则 1, 原则 5]
status: 未整理
kind: 观点
topic: Agent 与 Skill
roots: []
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

