---
title: "Stripe 内部的 agent 工厂：一步一提示词，agent 盯 agent"
author: "Yarchi (@undefinedKi)"
url: https://x.com/undefinedKi/status/2115891841488867723
source: X
published: 2026-10-29 19:41 UTC
saved: 2026-10-31
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [stripe-2026-payment-method-factory, anthropic-2024-building-effective-agents]
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

- 核心主张：Stripe 把重复支付接入拆成可复用提示，用观察 agent 找执行损耗，工程师修提示，再按日志和评审持续维护；可预测编排改由代码承担。单个前端 API 接入任务由两名工程师分别做约 20 天和 4 天，整体接入周期从最长半年降至 2–6 周是另一口径；这是公司案例，不能当随机对照或通用提效倍数。
- 源知识：
  - [Stripe 支付接入工厂（可复用提示、观察员与代码编排）](../roots/stripe-2026-payment-method-factory.md) · 关系：直接源自 · 强弱：强。官方原件写明两种时间口径、观察员和代码编排；提示改动是 agent 提议后经工程判断，非所有改动自动无审更新。
  - [构建高效的智能体](../roots/anthropic-2024-building-effective-agents.md) · 关系：相近 · 强弱：弱（模型复核通过）。确定路径由代码编排、开放判断交给模型，与 Anthropic 区分工作流和 agent 的方法相近；Stripe 未明说引用该文。
- 本质：这条新知识本质上是把重复经验做成可维护工作流，用执行反馈改进提示，并把确定协调交给代码。
- 整理于：2026-11-03（第 9 轮）
