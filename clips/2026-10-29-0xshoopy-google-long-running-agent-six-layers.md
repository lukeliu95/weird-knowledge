---
title: "推文归纳的长程 agent 六层结构（Google 9 页 PDF 出处待核实）"
author: "Shoopy (@0xShoopy)"
url: https://x.com/0xShoopy/status/2114790479028216132
source: X
published: 2026-10-26 18:45 UTC
saved: 2026-10-29
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: Agent 与 Skill
roots: []
---

## 原文

Google just dropped a 9-page PDF on building agents that run for days - 6 layers to an agent that waits in line, survives a crash and never charges you twice:

the formula: Long-Running Agent = Trigger + Runner + State + Resumable Workflow + Human Gate + Guards

here's how to build your own in 6 layers:

layer 1 → trigger - the model can't set a timer. a scheduler hits a /wake endpoint and the agent runs again

layer 2 → runner - adk web is a dev tool. your server owns the runner, the sessions and the storage

layer 3 → state - session in a real database, preferences under user:, facts in memory. a restart loses nothing

layer 4 → resumable workflow - kill the server mid-queue. it resumes at the same node. finished steps never run twice

layer 5 → human gate - the agent asks for a budget and waits for a yes. the pause survives restarts too

layer 6 → guards - re-check the seat before buying, one idempotency key per order. a retry never charges twice

most agents die when the request ends. this is how you build one that doesn't.

the workflow in layer 4 is a graph. how to design the whole agent system that way is in my article below

> 媒体：
> - https://pbs.twimg.com/media/HVk-okmWUAA6kld.png

## 溯源

### 本轮核查备注

- 查到同主题 Google Codelabs，但原帖所称9页PDF和六层公式的官方原件未确认；恢复机制也不自动保证外部付款副作用只执行一次。
