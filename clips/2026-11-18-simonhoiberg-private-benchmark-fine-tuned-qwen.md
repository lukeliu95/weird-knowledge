---
title: "作者称：微调 Qwen 在自家任务上追平前沿模型，靠私有测试集验证（未公开细节）"
author: "Simon Høiberg (@SimonHoiberg)"
url: https://x.com/SimonHoiberg/status/2121592470630711632
source: X
published: 2026-11-14 13:13 UTC
saved: 2026-11-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 模型与本地部署
roots: [zhang-2024-gsm1k, goodharts-law, dwork-2015-reusable-holdout]
---

## 原文

Our fine-tuned Qwen models now match GPT-6 and Opus 5.5.

And we didn't take a lab's word for it. We tested them on our own private benchmark, built from real work in my company that no model has ever seen.

Serious AI-native companies keep a private benchmark library.

Now, whenever a local model passes, GPT-6 loses that job 👇

> 媒体：
> - https://video.twimg.com/ext_tw_video/2121592427161042944/pu/vid/avc1/1280x720/Bg51dnnDquxa_FhR.mp4?tag=12

## 溯源

- 核心主张：判断便宜的本地微调模型能不能接手一项工作，不要信模型厂公布的分数，要用公司自己真实工作做成、任何模型都没见过的私有测试集来测；作者称自家微调的 Qwen 在这些任务上追平了 GPT-6 和 Opus 5.5（作者在回复里补充：只限它被训练的那些工作，不是通用能力）。
- 源知识：
  - [GSM1k：用没公开的新题检验大模型数学成绩是不是背出来的](../roots/zhang-2024-gsm1k.md) · 关系：相近 · 强弱：弱（模型复核通过）。Scale AI 的 GSM1k 新出了一套和 GSM8K 同风格、保证不在训练数据里的题，并故意不公开以防污染，测出部分模型掉分最多 8%（摘要、第 1 节「不打算公开」）。这和「用模型没见过的私有题检验真实能力」是同一个机制；原帖没有引用。
  - [古德哈特定律](../roots/goodharts-law.md) · 关系：相近 · 强弱：弱（模型复核通过）。公开测试集被各家当成目标去优化后，分数和真实能力的关系变弱，所以作者「不信实验室的话」，改用不会被刷的私有题。这是古德哈特定律在模型评测上的应用；原帖没提这个词。
  - [可复用的留出集（自适应数据分析中的泛化与留出集复用）](../roots/dwork-2015-reusable-holdout.md) · 关系：相近 · 强弱：弱（模型复核通过）。私有测试集就是一份不给模型训练用的留出集。Dwork 等指出，反复看留出集结果再改，留出集本身也会被过拟合；企业私有测试集若被反复用来挑模型、调微调数据，也有同样风险。原帖没谈这一点，是推断。
- 本质：这条新知识本质上是「评测要用没被训练数据污染、没被当成目标刷过的留出题」这一原则，在企业判断能否用本地小模型替换前沿模型时的应用。
- 整理于：2026-11-23（第 12 轮）
