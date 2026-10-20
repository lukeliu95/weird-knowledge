---
title: "网易 LobsterAI《中国办公 Agent 用户行为报告》的反直觉结论"
author: "向阳乔木 (@vista8)"
url: https://x.com/vista8/status/2112029104060948920
source: X
published: 2026-10-19 03:52 UTC
saved: 2026-10-20
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: AI 产品与创业
roots: [status-quo-bias, principle-of-least-effort, handa-2025-anthropic-economic-index]
---

## 原文

我去，读了网易 LobsterAI 刚刚发布的《中国办公 Agent 用户行为报告》

不少结论太反直觉了，跟 X 上大家 Agent 用法不一样。

比如：
① 微信竟然是最大办公 Agent 入口
② 办公 Agent 的最大场景还是（泛）编程
③ 73.6% 普通用户仅用一个模型

下面展开说说：
很多人把办公 Agent 接到微信、飞书、QQ 等 IM 里用，微信占比最高 77%，飞书 14.3%排第二，然后是 QQ。

微信跟国人绑定太紧了，也最顺手，上午 7-11点给 Agent 派活很多，看起来像上班路上用？

交给 Agent 的工作中，泛编程/IT 最多，是最大的使用场景。另外，设计/影视/创作使用量上升飞快，感觉这两大类任务都是模型能力的甜点区。

从报告里看，感觉普通用户不怎么切模型，默认给啥用啥，73.6% 普通用户只用一个模型。

普通用户人均使用 1.6 个模型，重度用户是 2.4 个。
最常见两种组合：DeepSeek Flash 系列 + GLM 5.3 Flash（14.0%），DeepSeek Flash 系列 + V4 Pro（12.4%）

梁圣 DeepSeek 缓存有黑科技，性价比一直超高。
这数据用的是 V4.1 Flash 旧版，新上的 V4.1-Flash-1017 能力又大幅提升，接近GPT 5.6 sol，感觉又要杀疯了。

还有一些有趣的观察，见第二条

> 媒体：
> - https://pbs.twimg.com/media/HU9uq4GbMAALA0Q.jpg
> - https://pbs.twimg.com/media/HU9usNqasAEL8gI.jpg
> - https://pbs.twimg.com/media/HU9uuHrakAAw6KB.jpg
> - https://pbs.twimg.com/media/HU9uvlVaoAAW9Q_.jpg

## 溯源

- 核心主张：网易有道自家办公 Agent（LobsterAI）的用户数据显示：通过聊天软件派活的用户里微信占 77%，泛编程/IT 是最大使用场景，多数普通用户只用一个模型；普通用户的用法由默认设置和手边最顺的渠道决定，而不是由模型榜单决定。（厂商调查：网易有道卖的就是 LobsterAI 这款开源桌面办公 agent，有免费和付费用户；数据只来自自家用户。9 月版的样本量媒体报道没写；第一期 9 月 7 日的报告称基于百万级真实用户数据，产品 2 月上线以来累计超 100 万用户。报告原件没找到，数字按新浪等媒体转述核对）
- 源知识：
  - [现状偏差](../roots/status-quo-bias.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“默认给啥用啥”、73.6% 普通用户只用一个模型，是维持默认选项的表现；而且产品的默认模型很可能就是份额最高的 DeepSeek Flash（推断，没查到 LobsterAI 的默认设置）
  - [最省力原则](../roots/principle-of-least-effort.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。微信本来就天天开着，在里面发一句话派活最省事，所以成为聊天渠道里的首选；切模型要重新配置，普通人不愿多花这份力气
  - [哪些经济任务在用 AI 做（Anthropic 经济指数第一篇）](../roots/handa-2025-anthropic-economic-index.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。推文觉得“编程是最大场景”反直觉，但 Anthropic 2025 年对 400 多万段 Claude 对话的分析也发现软件开发和写作合计占近一半、软件开发最多，编程居首并不意外
- 本质：这条新知识本质上是默认效应（现状偏差）和最省力原则在中国普通用户使用办公 Agent 场景下的应用。
- 整理于：2026-10-21（第 4 轮）
