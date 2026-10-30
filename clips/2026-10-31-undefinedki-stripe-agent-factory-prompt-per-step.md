---
title: "Stripe 内部的 agent 工厂：一步一提示词，agent 盯 agent"
author: "Yarchi (@undefinedKi)"
url: https://x.com/undefinedKi/status/2115891841488867723
source: X
published: 2026-10-29 19:41 UTC
saved: 2026-10-31
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

This is a goldmine for anyone building with agents.

Stripe just shared their internal AI agent setup. Same task: 20 days with plain Claude Code, 4 days with theirs. And you can copy it.

The setup is a "factory" for work they keep repeating. Every step lives in its own saved prompt, one agent builds while a second one watches it, and after every run the prompts get better. A payment integration used to take up to 6 months. Now it takes 2-6 weeks.

Here's how it works:

1. One prompt per step. They studied 125+ past integrations and turned every step into a reusable prompt. They have 100+ of them now.

2. An agent that watches the agent. While one agent builds, a second one reads its transcript and notes where it got lost, what it had to re-learn and which tools failed. Engineers use that to fix the prompt.

3. Prompts that update themselves. After every run the agents leave learning logs, decision logs and review comments. Another agent turns them into prompt fixes, and some get applied in one click.

4. Code runs the agents, not an LLM. They first used an AI orchestrator. It was slow, expensive, and sometimes did the work itself instead of delegating. So they rewrote it as plain code.

5. Agents test their own work. They run test payments in sandboxes before any human reviews the PR.

To copy it: save every prompt that worked, have a second agent review the transcript, and fix the prompt instead of fixing the output.

> 媒体：
> - https://pbs.twimg.com/media/HV0oSkPXUAAmqvu.jpg

## 溯源

