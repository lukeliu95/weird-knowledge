---
title: Claude Code 团队审代码的做法：九成代码由 AI 写，多道检查像叠起来的瑞士奶酪片，人只做机器做不好的判断
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/2111384189656252712
source: X
published: 2026-10-17
saved: 2026-10-21
why: 探索日报：Luke 想看
related_principles: ["原则 1", "原则 8", "原则 12"]
status: 已整理
kind: 观点
topic: 编程智能体
roots: [osmani-2026-claude-code-code-review, swiss-cheese-model, fagan-inspection, ironies-of-automation, ibm-1979-computer-accountable]
---

## 原文

Claude Code 团队公开了他们审代码的做法：代码大约九成由 Claude 写，六月到九月合并的修改翻了一倍多，需要撤回的比例反而降了四成多。

这期用一摞带洞的奶酪片讲这套做法：每道检查都会漏，叠起来就很难漏，底下还有一张网兜底。

片中回答五个问题：哪些修改还要人看，AI 审 AI 会不会没完，审查的 AI 漏了怎么办，人不读代码怎么懂代码，出了事算谁的。人不再逐行读代码，时间花在机器做不好的判断上。

视频1: 英文版
视频2: 中文版

> 媒体：
> - https://video.twimg.com/amplify_video/2111381698860425216/vid/avc1/1920x1080/I9MFCvYvzceZ5Iu8.mp4?tag=29
> - https://video.twimg.com/amplify_video/2111381871938490369/vid/avc1/1080x1920/svKRqH9JgGN3Ays6.mp4?tag=29


引用的推文（ClaudeDevs，https://x.com/ClaudeDevs/status/2110866210573386065）：

Code Review is now generally available for Claude Team and Enterprise plans. 

Reviews are now faster, catch more of the bugs that matter, and admins can pick from Quick, Standard, or Deep review levels for each repo. https://t.co/RO4tDC4U1U

> 媒体：
> - https://pbs.twimg.com/media/HUtNPoja4AAs_9b.jpg

## 溯源

- 核心主张：代码大多由 AI 写时，靠多道各自会漏的自动检查叠在一起（再加快速回滚兜底）来保质量，人不再逐行读代码，只按风险审关键改动、做机器做不好的判断并对结果负责；Claude Code 团队这样做后合并量翻倍、撤回比例降了四成多。
- 源知识：
  - [Claude Code 团队怎么审代码（七层检查、少量人工）](../roots/osmani-2026-claude-code-code-review.md) · 关系：直接源自 · 强弱：强。宝玉的视频讲的就是这篇官方博文：九成代码由 Claude 写、六到九月合并量翻倍多、撤回比例降四成多，数字一字不差
  - [瑞士奶酪模型](../roots/swiss-cheese-model.md) · 关系：直接源自 · 强弱：强。作者明说用“一摞带洞的奶酪片”讲这套做法：每道检查都会漏，叠起来很难漏；原博文也写了“每层都会漏，很少有问题能穿过所有层”
  - [Fagan 审查（正式代码审查）](../roots/fagan-inspection.md) · 关系：挑战 · 强弱：弱（模型复核通过）。经典做法是人按流程逐行审查代码；这里人不再逐行读，审查主力换成多个 AI 和自动检查（模型推断，待 Luke 确认）
  - [自动化的反讽](../roots/ironies-of-automation.md) · 关系：相近 · 强弱：弱（模型复核通过）。“人不读代码怎么懂代码”正是自动化反讽的问题：机器接手日常后，人仍要在出事时接手；原博文的办法是需要时让 Claude 写那一块的讲解（模型推断，待 Luke 确认）
  - [“计算机不能被问责，所以不能做管理决策”（IBM 1979 培训资料）](../roots/ibm-1979-computer-accountable.md) · 关系：相近 · 强弱：弱（模型复核通过）。“出了事算谁的”：原博文规定每个上线的改动都有一个人负责，不管是谁敲的代码，和“机器不能被问责”是同一个道理（模型推断，待 Luke 确认）
- 本质：这条新知识本质上是瑞士奶酪模型（纵深防御）在 AI 写代码时代的代码审查流程里的应用：用多道独立、会漏的检查加回滚兜底替代人逐行审，把人留给风险判断和担责。
- 整理于：2026-10-21（第 5 轮）
