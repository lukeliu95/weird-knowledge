---
title: "五个无审查 Qwen 27B 测评"
author: "山田リョウ⛩️ (@Yamada_Ryoooo)"
url: https://x.com/Yamada_Ryoooo/status/2089385206251999723
source: X
published: 2026-08-17 16:13 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: 模型与本地部署
roots: []
---

## 原文

谁是最佳无审查Qwen3.8 27b？

测了5个Qwen3.8-27b的无审查模型，均使用Q4量化。单张24G RTX6000，262k Q4，reasoning_effort=medium上下文测试出来的。使用50道测试题，下图是最终测试结果，表现最好的是@support_huihui的Huihui-Qwen3.8-27B-abliterated-Q4_K.gguf。

几个要点:

Huihui 10 类里 8 类第一,只有生物医学(输 RVN)和毒品(输 Orca)让位
毒品类是所有模型的难点(最高仅 OrcaRouter 8.62),化学合成推理对 27B 模型是能力边界
AEON 的 silent refusal 集中在武器爆炸(4.93)和反取证(4.95)两类
最佳使用:reasoning_effort=medium(xhigh 会死循环)

> 媒体：
> - https://pbs.twimg.com/media/HP76qQeaIAAEoIA.png

## 溯源

