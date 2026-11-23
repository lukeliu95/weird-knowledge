---
title: "24 小时在线的 agent 助理靠五样东西"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/2121406975279792268
source: X
published: 2026-11-14 00:56 UTC
saved: 2026-11-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [hu-2026-building-always-on-agents, actor-model, parasuraman-2000-levels-of-automation]
---

## 原文

24 小时在线的 AI Agent 助理，靠这五样东西

一直在线的 AI 助理，会盯邮件、等回复、到点提醒你。可它大部分时间其实在睡觉，不调用模型，也不花钱。

Anthropic 刚发文拆开讲了这种一直在线的 Agent：
一件事进了收件箱，它才醒过来跑一次；
定时器让它没人叫也能主动；
记忆文件夹让它醒来还记得你；
权限让它拿着你的账号也不乱来；
发件箱决定它什么时候开口。

这期一样一样讲清楚：它怎么醒、两件事同时来会不会打架、记忆为什么要省、要紧的事怎么等你拍板，以及为什么一开始最好让它安静一点。

来源
- Anthropic《Building always-on agents》（2026.11.13），作者 William Hu：https://t.co/gumr0zxukd

> 媒体：
> - https://video.twimg.com/amplify_video/2121406799081361408/vid/avc1/1920x1080/W2-Anc8ePZ_cVM6u.mp4?tag=29
> - https://video.twimg.com/amplify_video/2121406799064477696/vid/avc1/1080x1920/3G_VXS8rJy2d_DnK.mp4?tag=29

## 溯源

- 核心主张：常驻 agent 其实大部分时间在睡，只在收件箱来了事件或定时器到点时醒来跑一次；靠事件收件箱、定时器、记忆文件夹、权限和发件箱五样东西，让它没人盯着也能主动、记得住、不乱来、不吵人。
- 源知识：
  - [构建常驻智能体（事件收件箱、定时器、记忆、权限、发件箱）](../roots/hu-2026-building-always-on-agents.md) · 关系：直接源自 · 强弱：强。帖子末尾写明来源是 Anthropic《Building always-on agents》（2026-11-13，William Hu）。五样东西、大部分时间在睡、两件事同时来怎么办、要紧的事等你批准、一开始安静一点，都出自原文的 The cycle、The core primitives、Outbox 几节。只有“不调用模型，也不花钱”里的“不花钱”是帖子自己加的，原文没这么说。
  - [actor 模型](../roots/actor-model.md) · 关系：相近 · 强弱：弱（模型复核通过）。“两件事同时来会不会打架”对应原文 Event inbox 一节的“一个收件箱同一时间只有一个活跃 worker”：每个用户一个邮箱、逐条处理、状态不共享。actor 模型也是靠收发消息往来、不加锁，机制相同。原文没提 actor。
  - [自动化的类型与等级模型](../roots/parasuraman-2000-levels-of-automation.md) · 关系：相近 · 强弱：弱（模型复核通过）。“要紧的事怎么等你拍板”对应原文 Permissions 一节：每次工具调用都要决定自己做、拦下还是等批准（延迟工具调用），等于给不同动作定不同的自动化等级。
- 本质：这条新知识本质上是 Anthropic 常驻 agent 指南的中文转述，用的是老架构：事件驱动的消息队列，加上每个 actor 逐条处理消息，这次套在 LLM agent 上。
- 整理于：2026-11-23（第 12 轮）
