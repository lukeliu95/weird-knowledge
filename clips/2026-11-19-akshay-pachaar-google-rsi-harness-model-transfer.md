---
title: "Google 论文：harness 换模型时带上改动记录，接着优化更有效"
author: "Akshay 🚀 (@akshay_pachaar)"
url: https://x.com/akshay_pachaar/status/2123030996899774607
source: X
published: 2026-11-18 12:30 UTC
saved: 2026-11-19
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [yu-2026-self-improvement-memory, chestertons-fence, nygard-2011-architecture-decision-records, after-action-review]
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

- 核心主张：自我改进出来的 harness 换模型或换题库时，只带走了代码，没带走每处改动为什么加、本来想修什么、测下来修没修好的记录，接手的优化器就会重复失败过的实验、乱改看不懂的检查。把这本账（SIM）和 harness 一起交给优化器，继续优化的效果明显更好。
- 源知识：
  - [自我改进记忆（SIM）：换模型、换题库后接着做 harness 递归自我改进](../roots/yu-2026-self-improvement-memory.md) · 关系：直接源自 · 强弱：强。帖子讲的就是这篇 Google 论文（arXiv:2611.18856）。逐项核对：Opus 演化的 harness 搬到 Gemini 后，4 个领域的起点都低于 Gemini 的原始 harness，差 0.60～5.48 分（§4.3.1）；工作空间任务 68.41→84.75 对 68.41→73.42，涨幅约 3.3 倍（图 1、§4.3.1）；10 对编程实验 SIM 赢 9 对（表 3）；同一个检查改了 4 次，其中两次是修死锁（附录 F.3）。要注意：9/10 和“改 4 次”都来自换题库的实验（TB2.1→TB4，模型一直是 Gemini），不是换模型。
  - [切斯特顿的篱笆](../roots/chestertons-fence.md) · 关系：相近 · 强弱：弱（模型复核通过）。没有 SIM 的优化器“删掉看不懂的修复”，还把继承来的检查当成自己第一轮加的（附录 F.3）。这和“看不出篱笆有什么用就别拆”是同一个机制：不知道一条规矩为什么在，就可能拆掉有用的东西。论文的办法是把“为什么”交给后来的优化器（§1、附录 F.6）。论文没引用 Chesterton。
  - [架构决策记录（ADR）](../roots/nygard-2011-architecture-decision-records.md) · 关系：相近 · 强弱：弱（模型复核通过）。ADR 原文说，后来的人不知道一个决策的理由和后果，就只能盲目接受或盲目推翻。SIM 也是把每处改动针对的问题、理由、预期和结果记下来，跟代码一起交接，让优化器决定留、改、换还是删（§3.2–3.3）。机制相同，论文没引用 ADR。
  - [行动后复盘（AAR）](../roots/after-action-review.md) · 关系：相近 · 强弱：弱（模型复核通过）。SIM 要求每次改动在测试前写下“预计能修好哪些题”，测完再记“实际修好了哪些”，失败的也记（§3.2）。这就是复盘里“本来想要什么结果、实际得到什么、差在哪”的对照。论文没提 AAR。
- 本质：这条新知识本质上是“先弄懂为什么再改”（切斯特顿的篱笆）和“把决策理由写下来交接”（架构决策记录）用在 harness 递归自我改进上，换的不是人而是模型和题库。
- 整理于：2026-11-23（第 12 轮）
