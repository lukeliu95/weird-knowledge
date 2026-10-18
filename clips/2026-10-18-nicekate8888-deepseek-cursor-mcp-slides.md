---
title: "DeepSeek配Cursor做幻灯片"
author: "nicekate (@nicekate8888)"
url: https://x.com/nicekate8888/status/1889168584183845105
source: X
published: 2025-02-11 04:24 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: 设计与前端
roots: []
---

## 原文

DeepSeek R1 搭配 Cursor MCP 生成了 Sam 最新博文的幻灯片

流程：

Cline 里调用 Together DeepSeek R1（目前  Together 的 R1速度不错）生成 HTML 幻灯片

提示词：[ Sam 的博文]根据上文，生成高质量的幻灯片，html 格式，最佳实践

Cursor 里调用 Replicate MCP 生成图片（目前用的是flux schnell，可以换更好的模型）

如何调用可以看第二条视频

目前缺陷：生成的图片部分精准，部分不合适

> 媒体：
> - https://video.twimg.com/ext_tw_video/1889168244344524802/pu/vid/avc1/480x270/EITGArxOhynCspHJ.mp4?tag=14

## 溯源

