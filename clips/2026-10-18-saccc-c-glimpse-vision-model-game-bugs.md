---
title: "Glimpse 视觉模型找游戏 bug"
author: "Sac (@Saccc_c)"
url: https://x.com/Saccc_c/status/2111148336954888249
source: X
published: 2026-10-16 17:32 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 模型与本地部署
roots: []
---

## 原文

Jev过后，强烈建议大家狠狠关注这个刚发布的大模型Glimpse，成功帮助我在小王子游戏开发和维护阶段大幅提高bug排查效率，绝对的vibe coding开发验收神器！！

该模型由Elorian AI（@ElorianAI）打造，主打视觉理解与推理，这意味着其能最原生、最直接的理解图片和视频中各元素的位置、结构与空间关系，并以此来分析问题

这次我有幸提前拿到了 Glimpse 的内测机会。结合当下的场景，我第一时间就想到用它来检查小王子游戏中的各种潜在 bug：只要提供实际游玩的录屏，Glimpse 就能根据画面判断游戏设计是否合理，并为我梳理出各类潜在bug

这极大程度地解决了我在开发维护阶段「验收容易遗漏」的痛点

因为一直是我一个人测试游戏，难免会漏掉一些 bug；而且我在实践中发现，就算用 Astra、Opus 做验收审查，也总有部分细节问题难以发现

而 Glimpse 凭借超强的视觉推理能力，基本能一次捕获录屏中绝大部分细节问题，并按视频时间戳清晰罗列出来，方便我逐一核验

下面视频中，我也用酒馆章节的实机画面做了实测，效果真的惊艳！

在没有任何游戏上下文的情况下，Glimpse 梳理出的bug问题是 Astra 的 3 倍。更实用的是，点击时间戳就能在右侧直接跳到对应画面查看

Glimpse现在也开放了API，我们完全可以将其接入Codex、CC来完善开发后的验收审查流程

当然，除了 vibe coding 验收，我认为 Glimpse 还非常适合视频生成、图片生成等视觉相关的场景：借助强大的多模态理解能力，帮助规范和约束提示词，降低 AIGC 视频和图片生成的抽卡概率！从商业角度看，完全值得大家关注起来！！

> 媒体：
> - https://video.twimg.com/amplify_video/2111145864135847936/vid/avc1/480x270/2CQL2zVx9BRRhTfb.mp4?tag=29
> - https://pbs.twimg.com/media/HUxMAC7bwAA2c_c.jpg

## 溯源

