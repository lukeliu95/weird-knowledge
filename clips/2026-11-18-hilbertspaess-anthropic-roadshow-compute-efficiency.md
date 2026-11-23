---
title: "发帖人称 Anthropic 路演图显示算法效率超指数提升（图无刻度，仅为示意）"
author: "Jacob Coxon (@hilbertspaess)"
url: https://x.com/hilbertspaess/status/2121331333654086124
source: X
published: 2026-11-13 19:56 UTC
saved: 2026-11-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: AI 产品与创业
roots: [eth-2025-software-intelligence-explosion, recursive-self-improvement, ho-2024-algorithmic-progress-language-models]
---

## 原文

This slide from the Anthropic IPO roadshow was a big factor in my decision to leave. It’s an insane plot and I’m surprised they made it public.

It shows the compute efficiency of pretraining over time. The y-axis is a **log scale**: they are seeing continued superexponential algorithmic progress.

Mythos was not a one-time deviation, but a point on a superexponential. They could already retrain Mythos with a fraction of the compute originally needed.

It doesn’t strictly imply a software-only intelligence explosion- they have been spending more on R+D. But algorithmic improvements do not require ridiculous creative genius and are on the verge of being automated. You do the math.

> 媒体：
> - https://pbs.twimg.com/media/HXB7mp4bQAAKN3a.jpg

## 溯源

- 核心主张：发帖人认为 Anthropic 路演里那张「代码预训练算力乘数随时间变化」的对数轴图在加速上翻，说明预训练的算法效率在超指数提升、重训 Mythos 只需原来一小部分算力；再加上算法改进快要能交给 AI 自动做，暗示可能走向软件智能爆炸。
- 源知识：
  - [自动化 AI 研发会引发软件智能爆炸吗](../roots/eth-2025-software-intelligence-explosion.md) · 关系：直接源自 · 强弱：强。原帖明说「不严格意味着纯软件的智能爆炸」，用的就是 Eth 与 Davidson 2025 报告里的「软件智能爆炸」概念：AI 自动做 AI 研发、软件效率进步反过来加快研究，研究投入翻倍带来的软件翻倍次数 r>1 时越跑越快（报告第 22–28 页）。原帖「算法改进快要能自动化，你自己算」就是这套推演；但它是条件推演，不是观测。
  - [递归自我改进](../roots/recursive-self-improvement.md) · 关系：直接源自 · 强弱：弱（模型复核通过）。「算法改进快要被自动化」即 AI 改进做 AI 的方法；同一段路演视频里 Tom Brown 也说「接近递归自我改进时，Claude 能完全自己发现算力乘数」（Simon Willison 整理的路演文字稿）。原帖没用这个词，是推断。
  - [语言模型的算法进步（达到同样效果所需算力约 8 个月减半）](../roots/ho-2024-algorithmic-progress-language-models.md) · 关系：挑战 · 强弱：弱（模型复核通过）。路演图量的「算力乘数」和 Epoch 测的「达到同样效果所需算力下降」是同一类量（Ho 等 2024 第 2.1 节「有效算力」）。但 Epoch 用 2012–2023 年数据估计约 8 个月减半，按年份切分「没有发现明显加速的强证据」（第 3.1 节，作者说统计功效不足），和「超指数」的读法相反；路演图只有 3 个点加一个箭头、纵轴没刻度、图注说仅为示意，撑不起超指数的结论。
- 本质：这条新知识本质上是「算法效率持续指数进步 + AI 自动做研发 → 软件智能爆炸」这套推演，套在 Anthropic 一张无刻度、注明仅为示意的路演图上的个人解读。
- 整理于：2026-11-23（第 12 轮）
