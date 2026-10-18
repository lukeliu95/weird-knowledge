---
title: "Tripo Eden：先建地图再渲染"
author: "Santiago (@svpino)"
url: https://x.com/svpino/status/2069846836270211514
source: X
published: 2026-06-24 18:15 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 视频生成
roots: [model-view-controller, single-source-of-truth, piagets-theory-of-cognitive-development, cognitive-map, brooks-2024-video-world-simulators, bitter-lesson]
---

## 原文

The architecture of this new world model is one of the most interesting things I've seen lately:

Let me first explain how most world models work:

They predict and render one frame at a time. If you are navigating in one of these worlds, and you look left, the model draws whatever looks right in the moment.

Every time you change your viewpoint, the model has to imagine what should be there again, so it's very common for these models to "forget" what's in the world. For example, if you put a toy on the table, look away, then look back, the toy might not be there anymore.

Tripo AI is releasing its Project Eden model, which works very differently:

The model builds the world first, and then renders it based on that map.

That map holds the real state of the world: the geometry, every object, where things are, what's already happened. The picture you see on screen gets generated from the map.

This architecture flips the whole thing. Now, you get the following:

1. The world stops forgetting. Leave, come back, and the toy is still on the table because it lives in the map, not in the last frame you saw.

2. You can edit the world, and those changes persist for anyone who enters later.

3. Multiple people and AI agents can coexist in the world and see it from different perspectives.

This is early research, but it's looking really promising. They just raised nearly $200M across two rounds to build it out.

Tripo will be at SIGGRAPH 2026 (July 19–23, Los Angeles Convention Center). If you work in 3D, embodied AI, simulation, or anything spatial, go connect with them there.

> 媒体：
> - https://video.twimg.com/amplify_video/2069846771803815936/vid/avc1/480x270/LX6uCnExYndbbygF.mp4?tag=14

## 溯源

- 核心主张：多数世界模型逐帧预测画面，换个视角就会“忘了”世界里有什么；先建一张记录真实状态（几何、物体、发生过的事）的地图、再从地图渲染画面，世界就能持久、可编辑、多人多视角共享。
- 源知识：
  - [模型-视图-控制器（MVC）](../roots/model-view-controller.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。地图存状态、屏幕上的画面由地图生成、多人从不同视角看同一个世界，对应 MVC 的“模型存数据、视图只负责呈现、同一模型可有多个视图”，作者没提，属推断
  - [单一事实来源](../roots/single-source-of-truth.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“地图保存世界的真实状态，画面从地图生成”，就是让状态只在一处维护、其他地方都从它派生，属推断
  - [皮亚杰认知发展理论](../roots/piagets-theory-of-cognitive-development.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“把玩具放桌上、转头再回来玩具还在”正是皮亚杰感知运动阶段的“客体永久性”测试；逐帧模型像还没形成客体永久性的婴儿，属推断
  - [认知地图](../roots/cognitive-map.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。Tolman 1948 年认为老鼠在迷宫里学到的是一张环境地图，而不是一串“刺激-反应”；Eden 先建地图再行动，逐帧模型更像只会刺激-反应，属推断
  - [视频生成模型是世界模拟器（Sora 技术报告）](../roots/brooks-2024-video-world-simulators.md) · 关系：挑战 · 强弱：弱（待 Luke 确认）。Sora 报告主张客体永久性能“纯粹靠规模”从逐帧生成里自然冒出来（报告也承认只是“经常但不总是”）；Eden 认为逐帧模型天生会忘，改成显式存状态，和这条路线相反
  - [苦涩的教训](../roots/bitter-lesson.md) · 关系：挑战 · 强弱：弱（待 Luke 确认）。苦涩的教训主张少写人为结构、靠规模学；Eden 反过来把几何、物体、事件这些结构显式放进地图，押注“结构优先”，属推断
- 本质：这条新知识本质上是“状态与呈现分离”（MVC、单一事实来源）在 AI 世界模型上的应用：把世界状态存进一张显式地图，画面只是这张地图的一个视图。
- 整理于：2026-10-18（第 2 轮）
