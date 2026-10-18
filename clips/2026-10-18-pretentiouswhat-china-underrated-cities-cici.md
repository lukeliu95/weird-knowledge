---
title: "用 CICI 指数找被低估的中国城市"
author: "David Fishman (@pretentiouswhat)"
url: https://x.com/pretentiouswhat/status/2072979695855870285
source: X
published: 2026-07-03 09:44 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 其他
roots: [errors-and-residuals, streetlight-effect, hidden-champions]
---

## 原文

My methodology for the CICI was as follows:

Start with a normalized value for their registered hukou population (户籍人口), not current inhabitants (常住人口). That's considering the entire prefecture population, not just the metro downtown, because anyone or any part of a prefecture can contribute to reputation creation.

After that, subtract for anything that gives the prefecture city aura, name-recognition, any kind of notability at all. That includes things like:

- being a provincial capital
- having famous tourist attractions (esp. 5A)
- having a national brand headquarters
- having historical or cultural significance 
- famous cuisine/dishes
- any memes associated with the city
- being the site of a major disaster or scandal (negative reputation is still reputation)
- having anything else that people think of when you mention it

The highest scores after subtracting become the leaders on my CICI. This methodology allows me to find not just the small and obscure cities, but specifically *cities that are far less famous than their population suggests they should be.* The data part of this was AI-assisted.

I haven't been to most of the places on this top 15 list - because I'd typically travel to places that have notable economic or touristic activity - which by definition perform worse in the CICI. 🤔

And look, I know almost every city has a bit of *something*, or else there wouldn't be be a city there at all. It's all relative, and subjective, and for fun, so if you want to disagree with the list, just be nice about it.

All that being said, here my top 15:

## 溯源

- 核心主张：要找“名气远低于体量”的城市，先按户籍人口给出它按体量应有的名气，再减去所有带来名气的因素（省会、5A 景区、名牌总部、历史文化、名菜、梗、灾难丑闻等），剩下分数最高的就是最“隐形”的城市。
- 源知识：
  - [误差与残差](../roots/errors-and-residuals.md) · 关系：换了说法 · 强弱：弱（待 Luke 确认）。CICI 的做法就是“观测值减预期值”：人口代表按体量应有多少名气，减掉实际的名气来源后剩下的差额就是残差，作者要找的正是残差最大的城市（“名气比人口暗示的少得多”）。作者没用这个统计术语，也没做回归，是手工打分的简化版。
  - [路灯效应（醉汉找钥匙）](../roots/streetlight-effect.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。作者承认没去过榜上大多数城市，因为他只会去经济或旅游上有名的地方，而这些地方按定义在 CICI 上得分低：人的注意力只照到亮处，这个指数相当于专门去照暗处。
  - [隐形冠军](../roots/hidden-champions.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。隐形冠军指“在细分市场做到世界前三、公众却几乎没听说过”的公司，和 CICI 一样都是“实际体量远大于名气”的结构；作者没提到这个概念，属于跨领域类比。
- 本质：这条新知识本质上是“残差分析”（观测值减去按体量应得的预期值）在城市知名度排名场景下的应用。
- 整理于：2026-10-18（第 2 轮）
