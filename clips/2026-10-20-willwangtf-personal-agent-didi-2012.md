---
title: Personal Agent 像 2012 年的滴滴：是上游模型厂补贴下游的出口，要能自己后训练小模型降本
author: @willwangtf
url: https://x.com/willwangtf/status/2104795771099119641
source: X
published: 2026-09-29
saved: 2026-10-20
why: 探索日报：Luke 想看
related_principles: ["原则 3", "原则 9"]
status: 已整理
kind: 观点
topic: AI 产品与创业
roots: [didi-kuaidi-subsidy-war-2014, commoditize-your-complement, knowledge-distillation, porters-five-forces, transaction-cost]
---

## 原文

Personal Agent 这一波特别像 2012 年的滴滴，它会是上游模型厂商往下游进行补贴战的一个出口。  

腾讯已经布局了 Manus 和 Today。在接下来，他们可能会掀起其他云厂商和上游一起去 either 自己做，或者补贴下游这样的应用方来铺 Personal Agent。

因为 Personal Agent 赛道是一个非常贵的赛道，吃这些 context 需要非常多的 token 和钱，所以这不是一个创业公司靠自己的钱可以搞定的。接下来也会看到 Instinct、Rabbit OS 3 以及 Elys上游的云厂商或者模型公司合纵连横的局面。  我一直在想，这一波中国的创业机会很特别，它不是经典意义上的 copy to China，因为做这些应用的人大概率都是要做全球竞争的。比如 如果按照主要用户和付费来源的话，Manus 是 copy to LatAm，Genspark 是 copy to Japan Korea，并没有直接都 copy to China，因为在中国他们都没办法做这些产品。

Personal Agent 这件事情，目前大家应该是站在差不多的起跑线  

当然，在这一波浪潮里很重要的一个点，是中国“硬”的部分反而是很原创的。从消费电子角度来讲，Plaud 也好、Looki 也好，Vonder也好，Nirva也好，都是原创的产品，并没有说 copy from US，甚至大部分都比大厂和国外的公司上得早，这里面会有一些很有意思的东西，并且在个人助理或者极致个性化方面，会和软件玩家殊途同归  

所以这个战局需要一个软硬件都有能力下功夫、同时能拉着上游模型厂商一起搞补贴的团队，且又需要是一个能够自己 post-train 小模型去不断降本，并且把定价权拉在自己手里的模型团队才行

## 溯源

- 核心主张：个人 agent 很吃 token、很贵，创业公司自己烧不起，会像当年滴滴打车大战一样，由上游模型厂和云厂商出钱补贴下游应用来铺量；能赢的团队要软硬件都强、能拉上游一起补贴，并且能自己后训练小模型持续降本，把定价权握在自己手里。
- 源知识：
  - [滴滴与快的打车补贴大战](../roots/didi-kuaidi-subsidy-war-2014.md) · 关系：直接源自 · 强弱：强。作者明说“特别像 2012 年的滴滴”：当年腾讯、阿里分别投滴滴和快的，2014 年两边烧钱补贴打车，背后是巨头在抢移动支付入口。
  - [把互补品商品化](../roots/commoditize-your-complement.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。上游卖 token 的厂商补贴下游 agent 应用，是让互补品变便宜来拉动自家核心产品需求，和当年巨头补贴打车来推微信支付、支付宝同一个逻辑；作者没用这个词，是推断。
  - [知识蒸馏](../roots/knowledge-distillation.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“自己 post-train 小模型去不断降本”的主流做法就是把大模型能力蒸馏、后训练进小模型；推断。
  - [波特五力模型](../roots/porters-five-forces.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“把定价权拉在自己手里”本质是降低上游供应商（模型厂）的议价能力，这是五力模型里的供应商议价力；推断。
  - [交易成本](../roots/transaction-cost.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。自己训模型而不是一直买上游 API，是“自己做还是从市场买”的纵向整合选择，交易成本理论解释何时值得自己做；推断。
- 本质：这条新知识本质上是“把互补品商品化”（上游补贴下游来拉动自家产品需求）在大模型 token 生意上的应用，借了 2014 年腾讯、阿里补贴打车之战的样板，再加上用自训小模型做纵向整合、夺回定价权的竞争判断。
- 整理于：2026-10-21（第 4 轮）
