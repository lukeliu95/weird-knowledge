---
title: "开放权重让 fal 把 H3 推到更远"
author: "Max For AI (@MaxForAI)"
url: https://x.com/MaxForAI/status/2093784370217877553
source: X
published: 2026-08-29 19:34 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 模型与本地部署
roots: [permissionless-innovation, generative-systems, joys-law-management, user-innovation, the-cathedral-and-the-bazaar, permissive-software-license]
---

## 原文

这才是开源真正有意思的地方。

@MiniMax_AI  把 H3 权重开放出来以后， @fal  直接拿去做后训练和推理优化，最后做出了 H3 Max，甚至把实时视频的速度和质量推到了原团队自己都觉得“此前几乎不可能”的程度。

更关键的是，MiniMax 不需要批准，fal 也不需要等官方更新。

一个模型一旦开放权重，它的上限就不再只由原团队决定。

至于 fal 会不会继续把 H3 Max 开源，其实是另一回事。它完全可以不开 recipe、数据和推理系统，只提供商业 API。

但这反而更能说明开源的价值：开源不是要求所有人都把答案免费公开，而是把继续寻找答案的权利交给所有人。

今天是 fal，明天也可能是另一个完全没见过的团队，把同一个模型推到更远的地方。

## 溯源

- 核心主张：模型一旦开放权重，任何团队都不用原团队批准，就能在上面继续做后训练和优化，所以模型的上限不再只由原团队决定。开源的价值不在于要求所有人公开成果，而在于把继续探索的权利交给所有人。（MiniMax H3 和 fal H3 Max 的具体情况没有核实）
- 源知识：
  - [无需许可的创新](../roots/permissionless-innovation.md) · 关系：换了说法 · 强弱：弱（待 Luke 确认）。“MiniMax 不需要批准，fal 也不需要等官方更新”，就是“无需许可的创新”；不过 Thierer 说的“许可”主要指政府监管，这里引申成了原开发团队的许可
  - [生成性系统（生成性）](../roots/generative-systems.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“今天是 fal，明天可能是完全没见过的团队”，对应 Zittrain 说的生成性：平台能让大量互不协调的外部人员做出意想不到的改变
  - [乔伊定律](../roots/joys-law-management.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“模型的上限不再只由原团队决定”，和“最聪明的人大多在别人那里工作”是同一个意思
  - [用户创新](../roots/user-innovation.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。fal 是下游使用方，由它来做后训练和推理优化，改进来自使用者而不是原厂
  - [大教堂与集市](../roots/the-cathedral-and-the-bazaar.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。开放给所有人改，往往比原团队关起门来开发走得更远，这是开源运动的经典论点
  - [宽松型开源许可](../roots/permissive-software-license.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“fal 可以不开 recipe 和数据，只提供商业 API”，正是宽松型许可允许衍生作品闭源的特点（H3 具体用什么许可证没有核实）
- 本质：这条新知识本质上是“知识分散在众人手里”加“无需许可的创新”在开放权重大模型生态上的应用。
- 整理于：2026-10-18（第 1 轮）
