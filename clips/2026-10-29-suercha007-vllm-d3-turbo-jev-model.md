---
title: "vLLM 开源 Jev 模型 d3-turbo 登顶视觉决策榜"
author: "苏茶 (@Suercha007)"
url: https://x.com/Suercha007/status/2114695683932614899
source: X
published: 2026-10-26 12:28 UTC
saved: 2026-10-29
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

还记得 jev 吗？

vLLM 团队开源了一个新的 Jev 模型 d3-turbo，视觉榜第一被它拿下了。

Jev Decision Index 0.4.1 上，55 个视觉决策模型里它 72.46 分登顶。文本榜 67.31，比 TypeSafe 最新的 Jev 1.14（60.24）和 Cloudflare 的 Clef（54.92）都高，六个分项全部领先。

比上一代强在哪：同样对一张图问 255 个问题，上一代 d3-flash 要 32.94 秒，它 2.12 秒，快 15.5 倍。因为它只读一次，上一代每问一题重读一遍。

问题越多，它越占便宜。只问一两道，它反而不如上一代快。

另外它不止能做选择题。框选、视频目标跟踪都行。问它画面里某个东西在哪，返回一个框加置信度，目标不存在就给 0，不硬编。

26.09B 参数，Apache-2.0，一张 GPU 就能部署。官方还放了个免费在线体验。

https://t.co/eKPjwHdEx8

## 溯源

