---
title: "Anthropic 常驻 agent 指南的五个要点"
author: "Tekon Burns (@TekonBurns)"
url: https://x.com/TekonBurns/status/2121328737174388847
source: X
published: 2026-11-13 19:45 UTC
saved: 2026-11-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [hu-2026-building-always-on-agents, hohpe-2003-enterprise-integration-patterns, actor-model, principle-of-least-privilege, parasuraman-2000-levels-of-automation]
---

## 原文

Anthropic just published an engineering guide on how to build always-on agents.

The biggest misconception: an always-on agent does NOT run 24/7. It sleeps almost all day, wakes up for short runs, saves state, and goes back to sleep.

The 5 core pieces I distilled:

1. Event Inbox
Put a database table between webhooks and your agent. Acknowledge webhooks fast, run only one active worker per user so runs never collide, and batch rapid messages together.

2. Timers
Keep timers in a separate table from the inbox. Split them into one-off follow-ups and recurring schedules. A background poller drops due timers into the inbox.

3. Lean Memory + Dreaming
Only store what cannot be looked up again: user instructions, user notes, past messages, and task progress. Load a small index at wakeup, not every file. Run periodic dreaming passes to clean out stale facts.

4. Unattended Permissions
Never put raw API keys inside the agent sandbox — inject them through an outside proxy. Use Deferred Tool Calls to pause risky actions for approval without blocking the worker.

5. Outbox
Queue outgoing replies so your agent paces notifications instead of spamming users at 3 AM.

https://t.co/1zew6WaRbE

## 溯源

- 核心主张：常驻 agent 不是 24 小时在跑，而是睡、醒来短跑、存状态、再睡。五个部件：webhook 和 agent 之间放一张数据库表，每个用户只跑一个 worker，连发的消息合并处理；定时器单独存表，由轮询器投进收件箱；记忆只存查不回来的东西，醒来只读索引，再定期“做梦”清理；密钥由外部代理注入，危险动作用延迟工具调用等批准；发件箱控制发消息的节奏。
- 源知识：
  - [构建常驻智能体（事件收件箱、定时器、记忆、权限、发件箱）](../roots/hu-2026-building-always-on-agents.md) · 关系：直接源自 · 强弱：强。帖子说是 Anthropic 刚发的工程指南并附了链接，五个部件和各条做法都能在原文找到。有几处比原文说得重：“凌晨 3 点刷屏”是帖子自己加的；原文说正式发件箱是可选的，多数 agent 有个直接发送的工具就够；“做梦”也是可选的（原文是 can also add）；用户指令每次都全量加载，不是只读索引。
  - [企业集成模式（持久消息通道、可靠投递、幂等接收者、轮询消费者等）](../roots/hohpe-2003-enterprise-integration-patterns.md) · 关系：相近 · 强弱：弱（模型复核通过）。这套做法就是消息集成的老模式：webhook 和 agent 之间放一张持久化的表，收到就快速确认，按来源编号去重，轮询器把到期的定时器投进收件箱，分别对应持久消息通道、可靠投递、幂等接收者、轮询消费者。原文和帖子都没引用这本书。
  - [actor 模型](../roots/actor-model.md) · 关系：相近 · 强弱：弱（模型复核通过）。“每个用户只跑一个活跃 worker，几次运行就不会撞车”（原文 Event inbox 一节），和 actor 模型里每个 actor 只管自己的状态、逐条处理邮箱、不用加锁是同一机制。原文没提 actor。
  - [最小权限原则](../roots/principle-of-least-privilege.md) · 关系：相近 · 强弱：弱（模型复核通过）。“原始密钥不放进 agent 沙箱，由外部代理注入”（原文 Permissions 一节的 Credential store）：agent 环境只拿到发请求的能力，拿不到密钥本身，是只给完成工作所需最少权限的做法。
  - [自动化的类型与等级模型](../roots/parasuraman-2000-levels-of-automation.md) · 关系：相近 · 强弱：弱（模型复核通过）。“危险动作用延迟工具调用停下来等批准，又不卡住 worker”：按后果给动作分自动化等级，高风险的降到“等人批准”这一级（原文 Permissions 一节）。
- 本质：这条新知识本质上是企业集成模式（持久消息通道、幂等接收、轮询消费者）加最小权限原则，用在常驻 LLM agent 的架构上。内容是对 Anthropic 指南的工程化摘要。
- 整理于：2026-11-23（第 12 轮）
