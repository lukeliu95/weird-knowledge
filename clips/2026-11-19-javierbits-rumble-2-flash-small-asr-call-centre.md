---
title: "0.5B 语音识别模型 Rumble-2-flash 在呼叫中心音频上追平 30B"
author: "Javier Bits • priv/acc (@javierbits)"
url: https://x.com/javierbits/status/2123163121087115711
source: X
published: 2026-11-18 21:15 UTC
saved: 2026-11-19
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 语音与数字人
roots: []
---

## 原文

A 0.5B speech model just matched NVIDIA's 30B on real call-centre audio. 7.86% word error against 7.78%, on 302 hours of noisy helpline calls across 14 accents.

That's Rumble-2-flash 🔥🔥

It also beats Meta's 7B omniASR and Whisper large-v3.

The speed of this model is what surprised me the most, this model is FAST. It reports over 7,000x realtime in full batches, so an hour of audio in about half a second.

This is mind-blowing.

Apache 2.0, native in Transformers and vLLM, no custom runtime, no trust_remote_code.

> 媒体：
> - https://pbs.twimg.com/media/HXb9mrWXYAA9kuV.jpg

## 溯源

