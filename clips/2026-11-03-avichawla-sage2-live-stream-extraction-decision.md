---
title: "Sage2：在实时对话流上边抽取边决策的模型"
author: "Avi Chawla (@_avichawla)"
url: https://x.com/_avichawla/status/2117311150488752445
source: X
published: 2026-11-02 17:41 UTC
saved: 2026-11-03
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

Another big breakthrough after Jev!

Jev answers a fixed question over a fixed input, so a live chat requires re-reading the full transcript on every update.

Devs just built Sage2, which pairs an extraction model and a decision model on the same live stream.

Usually, in a live conversation, the details and the decisions keep changing.

New details show up gradually, and several questions stay open the whole time.

- The extraction stage turns each new message into structured fields in 150 ms, each tied to the exact source span it came from. Those fields then become decision options.

- The decision model scores them as text streams in, and returns typed answers with probabilities, so the full loop from raw text to action runs in about 200 ms.

This gives a fully reactive automation over a live chat, with no re-reading of the transcript.

Sage2 is built by @levantolabs, the team that shipped the first decision model, before Jev.

The video below depicts the model live in action on a broadband support chat, and I worked with the team to put this together.

More details below.

> 媒体：
> - https://video.twimg.com/amplify_video/2117311092397690880/vid/avc1/1638x1080/fGk4V67aKWzUiL4s.mp4?tag=16

## 溯源

