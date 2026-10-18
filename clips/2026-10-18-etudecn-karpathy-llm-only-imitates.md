---
title: "Karpathy：LLM 只想模仿"
author: "淘沙者(TheSandPicker) (@Etudecn)"
url: https://x.com/Etudecn/status/2074871421482959214
source: X
published: 2026-07-08 15:01 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 模型与本地部署
roots: [language-model, imitation-learning, stochastic-parrot, eliza-effect]
---

## 原文

Andrej Karpathy 把大模型说透了。

“LLM 压根没想成功，它只想模仿。”
他最近在微软 Build 大会有个 42 分钟的演讲，把模型到底怎么“想”的掰开揉碎了讲。
没有野心，不追求“正确”，就是重复训练时见过的模式。
最绝的是这个对比：一个 80 层 Transformer 处理一个 token 的算力，跟你大脑处理一个念头的能耗差不多。
这不是什么提示词魔法，这是理解模型的底层逻辑。
比网上那些卖 500 美金的神棍课值钱多了。
想停止把 AI 当人一样许愿，开始把它当工具一样使用？这个演讲是必修课。
看了没？没看赶紧去。

> 媒体：
> - https://video.twimg.com/amplify_video/2074869960363716608/vid/avc1/480x270/IFxJGLZID6sWSk_d.mp4?tag=28

## 溯源

- 核心主张：大模型的训练目标是模仿训练数据里见过的模式，不是追求把事做对，所以要把它当工具用、把要求说清楚，而不是像对人一样许愿。（帖子把 2023 年的 State of GPT 演讲说成“最近”。“一个 token 的算力约等于大脑一个念头的能耗”这个对比，在演讲摘要里没查到；演讲的原意是每个 token 只经过大约 80 层计算，待确认）
- 源知识：
  - [语言模型](../roots/language-model.md) · 关系：直接源自 · 强弱：强。“只想模仿”说的就是预训练目标：在海量文本上预测下一个 token。演讲内容摘要记录了“transformer 默认会模仿各种水平的解法”
  - [模仿学习（行为克隆）](../roots/imitation-learning.md) · 关系：换了说法 · 强弱：弱（待 Luke 确认）。“只模仿、不求成功”正是模仿学习（行为克隆）的特点：去拟合示范，而不是直接优化成败。原文没用这个术语，属推断
  - [随机鹦鹉](../roots/stochastic-parrot.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“没有野心、不追求正确、只重复见过的模式”和“随机鹦鹉”的说法很像；但 Karpathy 的重点是怎么用好模型，不是否定它的理解能力
  - [ELIZA 效应](../roots/eliza-effect.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“停止把 AI 当人一样许愿”，针对的是人习惯把人类特质投射到程序上
- 本质：这条新知识本质上是“最大似然训练就是在模仿训练数据的分布”在理解和使用大模型上的应用。
- 整理于：2026-10-18（第 1 轮）
