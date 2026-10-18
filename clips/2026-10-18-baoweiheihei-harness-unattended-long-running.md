---
title: "外层harness让智能体连跑数小时"
author: "heihei (@baoweiheihei)"
url: https://x.com/baoweiheihei/status/2037840982180557273
source: X
published: 2026-03-28 10:35 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind: 观点
topic: Agent 与 Skill
roots: []
---

## 原文

我这边现在能稳定无人值守跑 4 到 8 个小时。

这里真正难的其实不是“持续跑”，而是任务不要随着时间变长越跑越偏，而是能一轮一轮往更好的方向收敛。

我的做法不是把一个 agent 一直挂着，而是在模型外面放一层 harness：每一轮只推进一小步，先产出候选，再做真实执行和独立评估，好的保留，差的淘汰，再把可继承的状态写成 handoff 交给下一轮。

所以时间拉长后，增长的不是漂移，而是有效迭代次数；最后跑起来的不是一段长对话，而是一套会持续收敛的 autonomous coding system。

这个方向我非常推荐看：
https://t.co/JNOigPaw6A
https://t.co/PsXaHt1w4K
https://t.co/GggyNX116L

## 溯源

