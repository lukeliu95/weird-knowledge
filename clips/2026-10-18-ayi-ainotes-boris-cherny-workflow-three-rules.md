---
title: "Claude Code之父的三条心得"
author: "AYi (@AYi_AInotes)"
url: https://x.com/AYi_AInotes/status/2040082908120264802
source: X
published: 2026-04-03 15:04 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 编程智能体
roots: [cherny-2026-claude-code-setup-thread, cherny-2025-claude-code-best-practices, compounding-engineering, feedback, whole-life-cost, organizational-learning]
---

## 原文

一定要用最贵最聪明的 AI 大模型！一定要用 Claude opus 4.6！
这个创造了Claude Code的男人Boris Cherny大神，完整公开了自己的工作流，并给了我们 2026 年最顶级实用的建议！

核心就三件事，但每一件都跟大多数人的直觉相反：

第一，永远选最贵最聪明的模型
听着像烧钱，实际上反过来，聪明模型一次想清楚，笨模型来回试错烧掉的token远超差价。
他的原话："计划做得好，代码自然好。"

第二，整个团队维护一个纯文本知识库
不是Notion，不是花哨的文档系统，就是一个txt文件。Claude每犯一次错，记一笔，每周更新好几次，这个文件就是团队的长期记忆，Claude不会在同一个地方摔倒两次。

第三，永远让Claude看到自己代码的运行结果
能跑代码，能看浏览器渲染，
他的比喻很准："你让一个画家蒙着眼睛画画，
画完不让他看，然后怪他画得丑？"

最后别忘了给世界最强的大模型 Claude Code 装上眼睛和手脚，
目前最好用的爬虫工具 Xcrawl，原贴有详细 skills 教程和讲解👇

> 媒体：
> - https://video.twimg.com/amplify_video/2040080320217927680/vid/avc1/480x270/0BOmyEzhnD8tDdzf.mp4?tag=21

## 溯源

- 核心主张：用 AI 写代码要做三件事：用最强的模型（少返工，总体反而更快更省）；团队共同维护一份记录 AI 犯过的错的规则文件，让它不在同一个地方摔倒两次；让 AI 能运行并看到自己代码的结果。
- 源知识：
  - [Boris Cherny 公开自己的 Claude Code 用法（串推）](../roots/cherny-2026-claude-code-setup-thread.md) · 关系：直接源自 · 强弱：强。三条都出自 Boris Cherny 2026-01-02 的串推：第 3 条说用 Opus 4.5 带思考，因为要纠偏的少、总体更快；第 4 条说团队共用一份进 git 的 CLAUDE.md，Claude 做错就记一笔；第 13 条说给 Claude 验证自己工作的办法，质量能提高 2 到 3 倍。转述有走样：原文是 Opus 4.5 不是 4.6，理由是更快而不是更省 token，文件是 CLAUDE.md 不是 txt，画家比喻原串推里没有。
  - [Claude Code 最佳实践（给 Claude 一个验证自己工作的办法）](../roots/cherny-2025-claude-code-best-practices.md) · 关系：直接源自 · 强弱：强。第三条“让 Claude 看到运行结果”和“先把计划做好”，就是 Boris Cherny 2025 年《Claude Code 最佳实践》里的“给它明确的验证目标、先探索和规划再写代码”。
  - [复合工程](../roots/compounding-engineering.md) · 关系：直接源自 · 强弱：强。Boris 串推第 5 条明说：在代码评审时让 Claude 把教训补进 CLAUDE.md，“是我们版本的 @danshipper 的 Compounding Engineering”。
  - [反馈](../roots/feedback.md) · 关系：直接源自 · 强弱：强。Boris 原话用的就是“feedback loop”（反馈回路）：Claude 有了这个回路，最终质量能提高 2 到 3 倍；蒙眼作画的比喻说的就是没有反馈的开环。
  - [全生命周期成本（总拥有成本）](../roots/whole-life-cost.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。第一条“贵模型一次想清楚，便宜模型来回试错反而更费”，是按总成本而不是单价算账；作者没提这个概念，是推断。
  - [组织学习](../roots/organizational-learning.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。第二条把每次犯错沉淀成团队共享的长期记忆，是组织学习的做法；是推断。
- 本质：这条新知识本质上是闭环反馈和组织学习在 AI 编程智能体上的应用：让智能体看到结果来自我纠错，把每次犯错沉淀成团队共享的规则文件，并按总成本而不是单价选模型。
- 整理于：2026-10-18（第 2 轮）
