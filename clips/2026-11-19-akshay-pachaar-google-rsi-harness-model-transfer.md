---
title: "Google 论文：自我优化出来的 harness 换了模型就失效"
author: "Akshay 🚀 (@akshay_pachaar)"
url: https://x.com/akshay_pachaar/status/2123030996899774607
source: X
published: 2026-11-18 12:30 UTC
saved: 2026-11-19
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

Brilliant paper from Google on RSI.

(bookmark it)

Recursive self-improvement (RSI) lets an optimizer agent improve an agent harness on its own. It reads failure traces, edits the prompts, tools and completion checks, and keeps whatever scores better on a benchmark.

This works until the model underneath changes. A harness evolved on Claude Opus, moved to Gemini, scored below Gemini's plain starting harness in every domain Google tested.

When the harness moves to a new model, the only thing carried over is the evolved harness code, meaning the prompts, checks and rules the optimizer added. The record of how each piece got there stays behind, including which failure it targeted and whether it fixed that failure when tested.

So the optimizer working on the new model inherits a set of changes with no reasons attached. It ends up retrying experiments that already failed, or removing fixes it doesn’t understand.

Google's fix is Self-Improvement Memory (SIM), a log kept for the optimizer itself. Each entry is a recurring problem, like an agent declaring a task done before its commands ran, and every fix attempted under it stores:

1. The edit and the reasoning behind it
2. The tasks it was predicted to fix, written down before testing
3. The tasks it actually fixed, failures included
4. The model and benchmark it was tested on

The whole log goes into the optimizer's prompt every round, and new attempts get appended as optimization continues.

The paper shows the difference on one inherited check that stops the agent from finishing early. With SIM, the optimizer read why the check existed and extended it.

Without SIM, it rewrote the same check four times, twice to fix deadlocks it had created itself.

On the Opus-to-Gemini workspace tasks, the run with SIM improved about 3x more from the same starting score. It also finished ahead in 9 of 10 independent coding runs.

The paper is at https://t.co/ZLdo7FK7qk

I also wrote an article on a related idea, covering how to make an agent harness diagnose its own failures.

It's built on @Cometml's Opik, which is 100% open source. It goes beyond reading trace logs to finding why a failure happened and stopping it from recurring.

That diagnosis step produces the kind of root causes SIM stores.

The article is quoted below.

> 媒体：
> - https://pbs.twimg.com/media/HXaFcMkbcAIyiz0.jpg

## 溯源

