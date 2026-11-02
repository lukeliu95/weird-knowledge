---
title: "Liquid d1 小模型在 5060 Ti 上比赢 Qwen 和 InternVL"
author: "irony.aditya (@0xironyAditya)"
url: https://x.com/0xironyAditya/status/2116809688700551647
source: X
published: 2026-11-01 08:28 UTC
saved: 2026-11-02
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

decision models are made for text
is what i thought until i tried @liquidai's d1 series on 5060ti, specifically d1-2B and d1-Omni-2B, both around 2B

- route a scanned document to 1 of 16 types:
d1-2B 88.8%, Qwen3.5-2B 55.0%, InternVL3.5-2B 56.2%

- flag violence:
d1-Omni-2B 97.3%, Qwen 83.6%, InternVL 87.7%

- spot a defective part:
d1-2B 70.8%, Qwen 64.6%, InternVL 52.1%

- 0.13 s per question for d1, vs 0.26 s (Qwen) and 0.64 s (InternVL)

one 5060 Ti, BF16. not quite apples to apples: d1 are decision models, the others are general chat models, but as far as i know nothing else this small does decisions on images

credit to Liquid: 2B, 4 GB of GPU memory, and a d1 model came first in every round

> 媒体：
> - https://video.twimg.com/amplify_video/2116803706134138881/vid/avc1/1920x1080/_y6MLKxRsJ3wctn-.mp4?tag=29

## 溯源

