---
title: "Tripo Eden：先建地图再渲染"
author: "Santiago (@svpino)"
url: https://x.com/svpino/status/2069846836270211514
source: X
published: 2026-06-24 18:15 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind: 观点
topic: 视频生成
roots: []
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

