---
title: "ComfyUI 插件让 H3 出长视频"
author: "huangserva (@servasyy_ai)"
url: https://x.com/servasyy_ai/status/2098953042557272240
source: X
published: 2026-09-13 01:52 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 视频生成
roots: []
---

## 原文

又给你们挖到一个宝!
H3 能出任意时长的视频了, 一张 4090 就能跑。

准确说,是有人用 ComfyUI 插件做出来的 : ComfyUI-MiniMaxH3-TimelineDirector。

思路是把目标时长拆成多段, 一次执行里逐段生成再缝合:同一个种子, 上一段 AV Latent 的尾部直接接到下一段开头,重叠帧自动去掉,音画一起合并。

官方 demo 一次跑出 52 秒 / 1263 帧 / 24fps。

但是有三个坑:

H3 原生不支持长视频,底层还是分段续接
作者自己承认长链会漂移,只建议同镜头对照测试
你填 48 帧重叠,实际会被对齐成 39 帧

GPL-3.0 开源。用得好记得给⭐️👇
https://t.co/sXda9Efvuh

## 溯源

