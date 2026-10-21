---
title: "DeepSeek 工程师：手艺在过时"
author: "Max For AI (@MaxForAI)"
url: https://x.com/MaxForAI/status/2099663479095652441
source: X
published: 2026-09-15 00:55 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 思维与成长
roots: [liu-2026-burying-talent-yesterday, deskilling, sheridan-1992-human-supervisory-control, zai-2026-glm-inference-infrastructure, drago-2025-intelligence-curse, matthew-effect]
---

## 原文

昨晚，DeepSeek 的 kernel 工程师shengyu Liu（interestingLSY）写了一篇很猛的长文。

文章的核心其实就一句话：

他正在亲手把自己最擅长、也最热爱的工作，变成一门过时的手艺。

Liu做的是模型底层的 kernel 设计和优化，DeepSeek V4.1 的 Main Attention kernel 就有他的工作。

但他说，仅仅过去一年，AI 已经从只能帮忙查文档、读代码、找 bug，进化到可以自己读 CUDA、PTX、SASS，用专业工具分析每条指令的 stall，再继续优化 kernel。

他的判断是：再过半年到一年，AI 写出来的 kernel 很可能就能达到甚至超过自己。 

最有意思的是，他真正难受的甚至不是失业。

他觉得自己大概率还能留在行业里，只是工作会从「亲手写 kernel」，变成「驾驶 Agent 写 kernel」。

以前可以坐在电脑前一下午，一点点抠性能、想新的优化方法，像速通玩家刷新自己的纪录。

以后这些事情可能都交给 Agent 了。

人还在，效率甚至更高，但那门自己练了很多年的手艺，突然不再重要了。

所以他把这种感觉形容成：

不得不把自己的天赋留在昨天，然后去做一个 Agent 的驾驶员。

但文章后半段，比职业焦虑更有意思。

刘胜与认为，AI 继续发展下去，未来社会可能走向两个极端：共产主义，或者《赛博朋克 2077》。

一种情况是生产力被极大释放，最强的 AI 变成所有人都能低成本使用的基础设施。

另一种情况则是，极少数科技公司控制世界上最强大的 AI。

少数人借助它完成“机械飞升”，其他人只能使用被削弱的模型，甚至阶层流动都会变成一个死循环：

你得先拥有最强 AI，才有机会获得更多资源。
但你得先拥有更多资源，才有资格使用最强 AI。 

所以他直接写道，自己并不相信 Anthropic 或 OpenAI 会主动把最前沿的智能，以开放、便宜的方式提供给所有人。

这也是他为什么选择留在 DeepSeek：

研究更强、更快、更多人用得起的 AI，然后开源出去，至少把世界往《赛博朋克 2077》的反方向拉一点。

而是一个正在亲手推动 AI 变强的人，非常清楚自己可能就是最先被它淘汰掉的那批人。

他的选择也不是停下来。

而是继续往前推。

只是希望当这个东西真的足够强的时候，它不要只属于少数几家公司。

> 媒体：
> - https://pbs.twimg.com/media/HSOAXWTbcAAbKGd.jpg
> - https://pbs.twimg.com/media/HSOAXPkbAAAIzv_.jpg

## 溯源

- 核心主张：AI 很快会在写 kernel 这种顶尖手艺上追平甚至超过人类专家，专家的工作从亲手做变成指挥 Agent 做；如果最强的 AI 被少数公司垄断，社会会走向强者愈强的固化，所以要用开源让 AI 普及。
- 源知识：
  - [刘胜与《我不得不把才华埋葬在昨天》](../roots/liu-2026-burying-talent-yesterday.md) · 关系：直接源自 · 强弱：强。推文是在转述 DeepSeek 工程师刘胜与的随笔《我不得不把才华埋葬在昨天》，“机甲驾驶员”、半年到一年被 AI 追平、拿《赛博朋克 2077》作比、留在 DeepSeek 做开源等内容都出自原文（据 36 氪转载和界面新闻报道）。
  - [去技能化](../roots/deskilling.md) · 关系：相近 · 强弱：弱（模型复核通过）。原本要多年练就的 kernel 优化手艺被 AI 吸收，人的手艺不再重要，和去技能化（技术把熟练工的活变成机器或非熟练者也能做）相近。
  - [人类监督控制](../roots/sheridan-1992-human-supervisory-control.md) · 关系：相近 · 强弱：弱（模型复核通过）。从“亲手写 kernel”变成“驾驶 Agent 写 kernel”（定目标、划边界、评估方案），就是谢里丹说的自动化程度提高后人从操作者变成监督者。
  - [走向递归自我改进：GLM 如何搭建自己的推理基础设施](../roots/zai-2026-glm-inference-infrastructure.md) · 关系：相近 · 强弱：弱（模型复核通过）。同一时期智谱报告让 Agent 承担推理系统的大部分优化、工程师只负责定目标和划边界，和刘胜与描述的转变是同一现象；两者之间没有互相引用。
  - [智能诅咒](../roots/drago-2025-intelligence-curse.md) · 关系：相近 · 强弱：弱（模型复核通过）。“少数公司掌握最强 AI，其他人只能用削弱版、阶层流动停滞”和《智能诅咒》的担忧几乎一致，后者开出的药方也是让 AI 扩散到普通人手里；刘胜与没有引用这篇文章。
  - [马太效应（累积优势）](../roots/matthew-effect.md) · 关系：相近 · 强弱：弱（模型复核通过）。“先有最强 AI 才能拿到更多资源，先有更多资源才能用上最强 AI”的死循环，就是累积优势（富者愈富）的自我强化。
- 本质：这条新知识本质上是自动化让人从操作者变成监督者（去技能化）、以及关键生产要素被少数人垄断时的累积优势与“资源诅咒”，在 AI 写 kernel 和前沿模型开源与否这一场景下的应用。
- 整理于：2026-10-18（第 2 轮）
