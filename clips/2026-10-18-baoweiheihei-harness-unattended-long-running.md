---
title: "外层harness让智能体连跑数小时"
author: "heihei (@baoweiheihei)"
url: https://x.com/baoweiheihei/status/2037840982180557273
source: X
published: 2026-03-28 10:35 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [young-2025-long-running-agent-harness, rajasekaran-2026-harness-design, karpathy-2026-autoresearch, evolutionary-algorithm, cybernetics]
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

- 核心主张：让 agent 长时间无人值守又不跑偏，关键不是一直挂着，而是在模型外面加一层循环：每轮只走一小步，产出候选、真实运行、独立评估、留好汰差，再把状态交接给下一轮，于是时间越长有效迭代越多、结果越收敛。
- 源知识：
  - [长时间运行 agent 的有效 harness](../roots/young-2025-long-running-agent-harness.md) · 关系：直接源自 · 强弱：强。作者推荐的第一个链接就是这篇：每轮只做一个功能，用进度文件和 git 交接给下一轮，端到端测试后才算完成。
  - [长时间应用开发的 harness 设计](../roots/rajasekaran-2026-harness-design.md) · 关系：直接源自 · 强弱：强。作者推荐的第二个链接：生成者和独立评估者分开，评估者跑真实应用打分，用文件交接。
  - [autoresearch（自动做研究的循环）](../roots/karpathy-2026-autoresearch.md) · 关系：直接源自 · 强弱：强。作者推荐的第三个链接：agent 改代码、跑固定时长的实验，指标变好就留、变差就丢，可以通宵无人值守。
  - [演化算法](../roots/evolutionary-algorithm.md) · 关系：相近 · 强弱：弱（模型复核通过）。「先产出候选，好的保留，差的淘汰，再进入下一轮」就是变异加选择的演化算法循环。
  - [控制论](../roots/cybernetics.md) · 关系：相近 · 强弱：弱（模型复核通过）。靠真实执行和独立评估把结果反馈回来纠偏，让系统收敛而不漂移，是控制论负反馈闭环的思路。
- 本质：这条新知识本质上是「变异-选择」的演化循环加上负反馈闭环（控制论）在长时间无人值守 AI 编程 harness 上的应用。
- 整理于：2026-10-18（第 1 轮）
