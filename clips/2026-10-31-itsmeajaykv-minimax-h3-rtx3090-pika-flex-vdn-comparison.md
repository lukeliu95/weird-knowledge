---
title: "RTX 3090 跑 MiniMax H3：Pika H3 Flex 和 VDN-H3 对比"
author: "AJ (@ItsmeAjayKV)"
url: https://x.com/ItsmeAjayKV/status/2116238764695810400
source: X
published: 2026-10-30 18:40 UTC
saved: 2026-10-31
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

Video generation on RTX 3090 is now better !

It's been a while since i tested MiniMax H3, we have so many new LoRA now that i haven't tested in over a month. I can produce video withing 10 steps now, that is huge !

Pika H3 flex and VDN-H3
- Pika H3 flex is a LoRA, which lets the base to finish in 6 steps.
- VDN-H3 is made of LoRAs plus an external linear-attention branch, trained to finish in 8 steps.

Tested on my RTX 3090 + 64GB RAM !

Below is a comparison of 1344x784 video with audio, 5s in duration.

Pika H3 Flex, 6 steps, 666 seconds to render.
VDN-H3, 8 steps, 768 seconds to render

Audio quality is better with VDN, Pika H3 one has some issues.

Video wise, both have done a good job, am not really following prompting rules here, simple easy prompt and difference is noticeable.

Pika H3 saves me a lot of time, will be going with it for rest of tests today. I'll get back to VDN later.

> 媒体：
> - https://video.twimg.com/amplify_video/2116236229369032704/vid/avc1/2560x1440/gyHkDSiQk845_biY.mp4?tag=29

## 溯源

