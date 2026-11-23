---
title: "5 分钟讲清 Claude 参与证明黎曼猜想这件事"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/2124282462343967111
source: X
published: 2026-11-21 23:23 UTC
saved: 2026-11-23
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 学习与研究
roots: [alpoge-2026-rh-lean-proof, riemann-hypothesis, vakil-2026-masullo-grh-announcement, lean-mathlib-2026-rh-verification-statement, buzzard-2026-checked-in-lean]
---

## 原文

2026 年 11 月 20 日，Anthropic 的数学家 Levent Alpöge 宣布，他和 Claude 一起证明了黎曼猜想，交出来的是 1700 万行 Lean 代码。

这期用 5 分钟讲清楚：
黎曼猜想说的是什么，和质数有什么关系；
为什么 160 多年没人证出来；
AI 在里面做了什么；
机器检查全部通过，算不算真的证明了；
银行加密会不会因此失效。

同一天，斯坦福也放出一份纯人工证明草稿，几小时后就有人借助 AI 报告了问题。

两边对照下来：机器说没错，人还没读懂；人写的，正在大改。

（本视频由 Motion Artifact + Opus 5.5 + Gemini 3.8 TTS 制作，https://t.co/FqRzqoi4aq）

> 媒体：
> - https://video.twimg.com/amplify_video/2124281217524596736/vid/avc1/1280x720/6pzeogmsjhXkIovP.mp4?tag=29

## 溯源

- 核心主张：Anthropic 数学家 Alpöge 和 Claude 交出 1700 万行 Lean 代码证明黎曼猜想，机器检查通过但人还没读懂；同一天斯坦福贴出的纯人工证明草稿，几小时内就被人借助 AI 指出问题、正在大改。
- 源知识：
  - [Alpöge 与 Claude 的黎曼猜想 Lean 证明（公告与代码）](../roots/alpoge-2026-rh-lean-proof.md) · 关系：直接源自 · 强弱：强。11 月 20 日、和 Claude 合作、1700 万行 Lean 都对得上 remark.pdf 和 Lean 社区声明；作者在 Anthropic 工作有 TechCrunch 和维基百科佐证。
  - [黎曼猜想](../roots/riemann-hypothesis.md) · 关系：直接源自 · 强弱：强。视频讲解的对象；“160 多年”对得上 1859 年到 2026 年约 167 年。
  - [Vakil 仓促公布 Masullo 的广义黎曼猜想人工证明草稿](../roots/vakil-2026-masullo-grh-announcement.md) · 关系：直接源自 · 强弱：强。“斯坦福同一天放出纯人工证明草稿、几小时后有人借助 AI 报告问题”几乎逐字对应斯坦福教授 Vakil 的博文：11-20 贴出、“all human, with no AI”、约 8 小时后更新“problems ... identified with the assistance of different AI models”。
  - [Lean 与 Mathlib 社区关于黎曼猜想 Lean 证明的联合声明](../roots/lean-mathlib-2026-rh-verification-statement.md) · 关系：直接源自 · 强弱：弱（模型复核通过）。“机器检查全部通过”对应 11-21 的 Lean 社区联合声明；推文没写出处，属推断。
  - [判断“已在 Lean 里检查过”可不可信的四个问题](../roots/buzzard-2026-checked-in-lean.md) · 关系：相近 · 强弱：弱（模型复核通过）。视频提的“机器检查全部通过，算不算真的证明了”正是 Buzzard 博文讨论的问题：Lean 通过要再查四件事，而且 Lean 证明对不等于配套文字稿对、也不等于人读懂；视频没引用它。
- 本质：这条新知识本质上是“机器确认一个证明对”和“人读懂它为什么对”是两回事，在黎曼猜想两份证明同日出现这件事上的对照讲解。
- 整理于：2026-11-23（第 12 轮）
