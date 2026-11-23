---
title: "四个神经元怎么学会追光：《Watch a Brain Learn》图解"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/2122106906814935475
source: X
published: 2026-11-15 23:18 UTC
saved: 2026-11-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 学习与研究
roots: [braitenberg-1984-vehicles, williams-1992-reinforce, reinforcement-learning, salimans-2017-evolution-strategies, kasdin-2025-dopamine-song-learning, law-of-effect]
---

## 原文

四个神经元，怎么学会追光

学骑车的时候，没人能把“怎么骑车”直接刻进你脑子里，通常学自行车的人，摔了好多次后，然后突然就学会了。那是什么让大脑学会骑车的呢？

Myriad 系列第二章《Watch a Brain Learn》，作者是物理学家出身的科学记者 Aatish Bhatia 和神经科学家 Arkarup Banerjee。他们造了一只只有四个神经元的小东西，让我们亲眼看它学会一件事。

这期把原文的配套动画用原文的数据重画出来：三个数字怎么决定它是怕光、冲撞还是爱上光；把三个数字变成一个立方体，学习就成了立方体里的一条路；没人教，它只靠奖励和惩罚，从两千多种接法里找到那不到百分之二的好答案。

最后换个奖励，它又学会了逃跑、装死和战斗，再回到鸣禽、AI 和你的大脑。

《Watch a Brain Learn》文章地址：https://t.co/5PN0tiwKkf

> 媒体：
> - https://video.twimg.com/amplify_video/2122105849111822337/vid/avc1/1920x1080/AjFfqc6ucdro-xFG.mp4?tag=29
> - https://video.twimg.com/amplify_video/2122105849069846529/vid/avc1/1080x1920/-RH-doDxIyNSVTtp.mp4?tag=29

## 溯源

- 核心主张：一个只有 4 个神经元、3 个可调数字的布赖滕贝格式小生物，没人示范，只靠“每次随机改一点，比平时好就顺着改，比平时差就反着改”的奖惩，就能自己学会追光；换一种奖励就学出逃跑、装死或冲撞，鸣禽靠多巴胺学唱是同一个道理。
- 源知识：
  - [布赖滕贝格小车（《Vehicles：合成心理学实验》）](../roots/braitenberg-1984-vehicles.md) · 关系：直接源自 · 强弱：强。原文附录 How the spark moves 写明 spark 受神经科学家 Valentino Braitenberg 启发；两只眼睛同侧直连、交叉连到两侧鳍的接法就是布赖滕贝格小车，第一章 Let's Build a Brain 已用它做出怕光、冲撞、爱上光。
  - [REINFORCE：联结主义强化学习的统计梯度算法](../roots/williams-1992-reinforce.md) · 关系：直接源自 · 强弱：强。原文附录 How the spark learns 写明学习用的是 Williams 1992 年 REINFORCE 的一个变体：随机扰动加在权重上（权重扰动），这一次的奖励和最近平均奖励比，好就顺着改、差就反着改，改多少和好多少成正比。
  - [强化学习](../roots/reinforcement-learning.md) · 关系：直接源自 · 强弱：强。原文副标题就是 A visual explanation of reinforcement learning，正文结尾说这个过程叫强化学习。
  - [演化策略：强化学习的可扩展替代](../roots/salimans-2017-evolution-strategies.md) · 关系：相近 · 强弱：强。原文附录明说“类似的想法叫演化策略，OpenAI 2017 年用它教 AI 玩 Atari”；两者都是给参数加随机扰动、按结果好坏估计改进方向。
  - [自然行为靠多巴胺强化来学（幼年斑胸草雀学唱）](../roots/kasdin-2025-dopamine-song-learning.md) · 关系：直接源自 · 强弱：强。原文讲鸣禽“唱得更像记忆中的成年歌声就有一阵多巴胺，远了就下降”，直接链到这篇 Nature 论文；论文发现多巴胺对应“这一遍比最近几遍好多少”，和 spark 的“比平时好多少”是同一种算法。
  - [效果律](../roots/law-of-effect.md) · 关系：相近 · 强弱：弱（模型复核通过）。“带来奖励的改动留下、带来惩罚的改动反着来”就是效果律的思路；原文没提 Thorndike，是推断。
- 本质：这条新知识本质上是强化学习（REINFORCE 式的随机扰动加奖励比较）在布赖滕贝格小车这种最简神经回路上的可视化演示。
- 整理于：2026-11-23（第 12 轮）
