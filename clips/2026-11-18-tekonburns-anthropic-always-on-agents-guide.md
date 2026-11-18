---
title: "Anthropic 常驻 agent 指南的五个要点"
author: "Tekon Burns (@TekonBurns)"
url: https://x.com/TekonBurns/status/2121328737174388847
source: X
published: 2026-11-13 19:45 UTC
saved: 2026-11-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
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

