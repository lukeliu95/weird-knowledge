---
title: "V4-Flash GB300 吞吐实测"
author: "Alex Ziskind (@digitalix)"
url: https://x.com/digitalix/status/2089886524254847425
source: X
published: 2026-08-19 01:25 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

Been benchmarking DeepSeek-V4-Flash on a single DGX Station GB300 and the numbers are pretty wild:

286 tok/s single stream
4,553 tok/s at 32 concurrent
WikiText-2 ppl 5.128
Biggest surprise: switching to dspark speculative decoding with 7 draft tokens gave +34% over MTP-3. https://t.co/uWpu3FqrNP

> 媒体：
> - https://pbs.twimg.com/media/HQDErrZWUAANxxk.jpg

## 溯源

