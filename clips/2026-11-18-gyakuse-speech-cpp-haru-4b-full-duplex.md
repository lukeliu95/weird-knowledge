---
title: "speech.cpp v0.11.0 支持全双工对话模型 Haru-4B"
author: "逆瀬川 (@gyakuse)"
url: https://x.com/gyakuse/status/2121877504789287304
source: X
published: 2026-11-15 08:06 UTC
saved: 2026-11-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 语音与数字人
roots: []
---

## 原文

speech.cpp v0.11.0をリリースしました🚀
higurashi-aiさんのHaru-4Bに対応しました。
聞きながら同時に話せる対話モデル(いわゆるFull-Duplex型のモデル)で、手元のMac / Windows / Linuxで会話できます。
動画はOpenAIのgpt-live-1とHaru-4Bに話してもらったものです！
https://t.co/zJA2UFr9CJ

■動作の目安
・速さは公式のMLX版とほぼ同じ（ただ、ちょっとだけ遅いです。speech.cpp はPythonもCUDAもいらないので、簡単に入れて動かしたいときに便利です）
・MacはメモリF16で約11GB、Q8_0で約7GB
・Windows/LinuxはVRAM 8GBならQ8_0で10分までの会話

> 媒体：
> - https://video.twimg.com/amplify_video/2121875924962693120/vid/avc1/1920x1080/6wSt-OhEcVJztECp.mp4?tag=29

## 溯源

