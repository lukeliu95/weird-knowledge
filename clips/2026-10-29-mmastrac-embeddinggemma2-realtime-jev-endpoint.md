---
title: "用 EmbeddingGemma2 做毫秒级实时 Jev 判断接口"
author: "Matt Mastracci (@mmastrac)"
url: https://x.com/mmastrac/status/2115098609356284223
source: X
published: 2026-10-27 15:09 UTC
saved: 2026-10-29
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

It's been a while since I showed any Jev stuff but I've been cooking on a way to use @GoogleDeepMind's EmbeddingGemma2 as an insanely fast real-time /v1/systemone endpoint (20ms on text, 100ms on images).

It's trainable in real-time, can distill an upstream teacher model, and is multi-modal by default. Hard to believe a @googlegemma model of this size can do so well with the right harness!

> 媒体：
> - https://video.twimg.com/amplify_video/2115097299861082112/vid/avc1/2502x1370/RkHepUnlDTN218Wk.mp4?tag=29

## 溯源

