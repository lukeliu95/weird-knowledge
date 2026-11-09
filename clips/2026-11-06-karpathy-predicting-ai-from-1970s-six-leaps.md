---
title: "要在 1970 年代猜中今天的 AI，得连跳六步"
author: "Andrej Karpathy (@karpathy)"
url: https://x.com/karpathy/status/2118048337018712423
source: X
published: 2026-11-04 18:30 UTC
saved: 2026-11-06
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 学习与研究
roots: [information-theory, moores-law, neural-scaling-law]
---

## 原文

There are a few notable counter-examples (e.g. HAL) but this is basically right for a lot of pre-2000 sci-fi.

I think getting AI right from e.g. somewhere in the ~1970s would require a fairly complicated set of inferences, probably the biggest things would be:

Image the world in 50 years.
1. "Digital knowledge work / computing". The vast majority of knowledge work (which makes up a very large fraction of the economy) goes digital. As computers get cheaper, much of society’s work happens on screens, over billions of machines in homes and offices.
2. "Internet". Similar to ARPANET (and see Licklider’s “Intergalactic Computer Network” (1963)), this creates demand for a global network of computers where people work, argue, teach, joke, and socialize.
3. "Big data". This creates a very large, compounding repository of digital information, with traces of how people reason, how they create, what they know etc.
4. "Statistical learning". Trying to program intelligence by hand is extremely difficult. But Shannon's n-gram approximations of English (1948) show examples of how language has statistical structure that can be "learned". You could imagine doing so over extensions of cybernetic computing (e.g. in the style of Rosenblatt's Perceptron 1958). So instead of programming thought, we could fit a statistical model to the record.
5. "LLMs". This might lead to something along the lines of ELIZA (1966), but with enough data (per 1-3), and enough compute (see Moore's law 1965), the imitation might become of extreme hight fidelity to the point that it's economically extremely useful.
6. "Scaling laws". These networks may demand a huge amount of data / computing resources and expertise to train. It's plausible that the more of each you have, the better your ELIZA gets. The economics concentrate, where a few organizations build a few minds and then deploy copies of them digitally.

Something like that. Basically, it's a lot of leaps. You have to start with computers, to internet, to big data, to big compute (Moore's law), which then allow large-scale statistical learning approach based on neural networks, and then posit scaling laws, and then imagine the form factor of language models as a lot more sophisticated ELIZA. And you'd have to short everything else, most predominantly I think the idea that we'd figure out how to program robots by hand.

## 溯源

- 核心主张：Karpathy 用数字化、互联网、数据、统计学习、算力增长和缩放规律回顾性解释：从1970年代想象今天的AI，需要串起多次推断；这不是经过事前检验的预测成绩，也不是这些环节必然导向今天大模型的定理。
- 源知识：
  - [信息论](../roots/information-theory.md) · 关系：直接源自 · 强弱：强。帖子明确点名Shannon1948年的英语n-gram近似；原著第3节确实展示从字符频率到字词转移的统计生成，不把它写成Shannon已预测现代LLM。
  - [摩尔定律](../roots/moores-law.md) · 关系：直接源自 · 强弱：强。帖子明确引用Moore1965作为算力增长背景；已核对原论文重印，1965讨论的是约每年倍增，后来的两年口径不能倒写回1965。
  - [神经网络规模定律](../roots/neural-scaling-law.md) · 关系：直接源自 · 强弱：强。帖子直接列出Scaling laws这一环节；Kaplan2020等是本库核对该概念的代表研究，不表示Karpathy在原帖点名引用了该篇论文，也不把测试损失的经验规律等同通用智能必然出现。
- 本质：这条内容本质上是把语言统计建模、硬件增长与神经模型经验缩放规律连成一条回顾性技术解释；各节点有史料，整条因果链仍是作者的推论。
- 整理于：2026-11-09（第 10 轮）
