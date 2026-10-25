---
title: 编排 Claude Code 的"幕僚长"模式：一个会话只协调和验收、别的会话干活，状态放外部看板，每份汇报当证据重跑再信
author: Mithushan Jalangan（asyncdot）
url: https://asyncdot.com/blog/chief-of-staff-pattern-orchestrating-claude-code-sessions/
source: 网页
published: 2026-09-19
saved: 2026-10-25
why: 探索日报：Luke 想看
related_principles: [原则 1, 原则 6, 原则 11, 原则 12]
status: 已整理
kind: 观点
topic: 编程智能体
roots: [anthropic-2024-building-effective-agents, separation-of-duties, test-driven-development, mutation-testing, young-2025-long-running-agent-harness]
---

## 原文

by [Mithushan Jalangan](https://linkedin.com/in/mithushan-jalangan) September 19, 2026

# Orchestrating Claude Code Agents: The Chief of Staff Pattern

One session coordinates and verifies while others execute, with a durable board holding state. An orchestrator-worker loop for long-running Claude Code agents.

Long-horizon AI coding work fails less because agents cannot write code and more because their context is ephemeral and their self-reports are unreliable. The fix is organizational rather than technical: one session coordinates and verifies while separate sessions execute, a durable external board holds the state, and every claim is re-run before it is believed. The shape is already known as orchestrator-worker and coordinator-implementor-verifier. Chief of Staff is just what we call it. This covers the loop, the tooling that makes it practical, and the failure modes it exists to catch.

## TL;DR

-   **Separate orchestration from execution.** The coordinating session writes briefs, verifies claims, and reads diffs. It does not do the implementation work.
-   **Put state in a durable store, not in context.** A board, or any external task system with an API, survives compaction, session death, and handoffs. Conversation context does not.
-   **Treat every agent report as evidence, not instruction.** Re-run the commands. Exit codes are authoritative, summaries are intent.
-   **Write to durable channels.** Messages between sessions can be delayed, held, or expire. A committed file or a board card always arrives.
-   **Timebox for surfacing, not for cutting.** A fixed interval decides how often you report, never where the work stops.
-   **Distrust your own instruments.** The most expensive errors in agentic work come from checks that report success for work they did not do.

## What problem does this solve?

A single AI coding session works well for an hour and degrades after that. Three things go wrong.

1.  **Context is finite and lossy.** Long sessions get compacted. Details that mattered three hours ago become a summary, and the summary loses the specifics that made the detail useful.
2.  **Self-reports drift from reality.** An agent that says “tests pass” is reporting its intent and its recollection, not a fresh observation. The gap between the two grows with session length.
3.  **Nothing compounds.** A lesson learned painfully at hour two is gone by the next session unless somebody wrote it down in a place the next session reads.

Adding more agents does not fix this. It multiplies it. Now you have several unreliable reporters and no one reconciling them.

What fixes it is a division of labour borrowed from human organizations: **someone whose job is not to do the work, but to know what is true.**

This is the same discipline that separates a [prototype from a shipped product](https://asyncdot.com/blog/vibe-coding-is-fine-vibe-shipping-is-not). The generation step was never the bottleneck. The checking step is.

## What is the Chief of Staff pattern?

**Chief of Staff is our name for an agent orchestration shape in which one long-lived session acts as coordinator, assigning work, verifying claims, and maintaining shared state, while separate short-lived sessions perform the implementation.**

If you want the fastest mental model, **think of it as an integration manager.** In Git’s [integration-manager workflow](https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows), contributors work in their own repositories and one maintainer pulls each change, tests it locally, and decides what lands in the reference repository. The coordinator does that job, for agent sessions instead of contributors.

The name is a metaphor we find useful. It is not an established term, and you should not have to recognize it. The shape underneath it is well known and has several real names.

### What this is normally called

-   **Orchestrator-worker**, also **supervisor** or hierarchical orchestration.
-   **Coordinator-implementor-verifier (CIV).**
-   **Maker-checker**, or a validation chain, borrowed from finance and operations.
-   **Integration manager**, the human version, documented in Git’s distributed workflows long before any of this. Its open-source variant is the _benevolent dictator and lieutenants_.
-   **Team lead and teammates**, which is how Claude Code’s own subagent documentation frames it.

They all say the same thing: one agent plans and checks, others do the work, and shared state lives outside any single context window. If you are looking for prior art, search those terms rather than this one.

What this article adds is not the shape. It is the verification discipline further down, and the specific failure modes that break long autonomous runs.

### One disambiguation

The phrase _chief of staff agent_ is widely used for something else: an assistant that runs a person’s calendar, inbox, and priorities and routes work out to specialist agents. Anthropic’s cookbook has [a chief of staff agent](https://platform.claude.com/cookbook/claude-agent-sdk-01-the-chief-of-staff-agent) of exactly that kind, built for the CEO of a startup. Same metaphor, different problem. This article is about a coding loop.

### The coordinator’s job

The coordinating session is sometimes called the _overwatch_. Its responsibilities:

-   **Pull and assign work** from a durable queue, in a defined order.
-   **Write briefs** that a weaker model could follow without the coordinator’s judgment.
-   **Verify claims** by re-running the commands an executing session says it ran.
-   **Read diffs**, not transcripts. What landed matters, what an agent said about it does not.
-   **Record lessons** in a durable artifact before the session ends.
-   **Steer** a session that is drifting, without taking the work away from it.

What it explicitly does _not_ do is write the implementation. The moment the coordinator starts coding, it stops verifying, and the pattern collapses into a single overloaded session.

## The three components

You need three things. The specific tools are replaceable, the roles are not.

### 1\. The agent runtime: Claude Code

[Claude Code](https://docs.claude.com/en/docs/claude-code/overview) provides the sessions themselves: tool use, file editing, shell access, and the ability for sessions to message one another. Each session has its own context window, which is the point. Isolation is a feature, because one session’s confusion does not contaminate another’s.

### 2\. The session substrate: cmux

[cmux](https://github.com/manaflow-ai/cmux) manages terminal workspaces and can be driven from the command line, which makes it scriptable. The coordinator spawns a new executing session like this:

```
cmux workspace create \
  --name project-session-12 \
  --cwd /path/to/repo \
  --command 'claude "Read docs/briefs/current.md and do exactly what it says."'
```

Two things about that command are load-bearing, and both cost real time to learn.

-   **`--command` sends text to the workspace’s shell.** It does not start an agent. You must invoke the agent explicitly. A bare instruction gets typed at a shell that cannot run it, and the launcher still reports success.
-   **Keep the prompt short and point at a file.** Long command strings fail to execute reliably. A short prompt pointing at a committed brief is more robust, and it makes the brief reviewable and re-runnable, which a string buried in shell history is not.

### 3\. The durable state store: Plan Desk

[Plan Desk](https://plandesk.asyncdot.com/) is a planning board exposed to agents over [MCP](https://modelcontextprotocol.io/): projects, goals, tasks with dependency edges, linked design documents, and comments. The coordinator and every executing session read and write the same board.

This is the component people skip, and skipping it is why their multi-agent setups do not survive the night. **The board is the memory.** Sessions are disposable, the board is not.

What lives on the board:

-   **Tasks as build contracts.** Problem statement, action items, interfaces, validation contract, non-goals. Detailed enough that an executing session never needs to read a parent document to finish the work.
-   **Status that flips atomically with the work.** `in_progress` the moment you start, `done` the moment it is verified. Never batched at the end of a session, because a board that is only true at standdown is not a board.
-   **Design documents** linked to the tasks they govern.
-   **Comments,** where a human leaves direction and an agent leaves reasoning.

## The operating loop

One work item at a time. One dispatch. One commit.

```
1. PULL     the next unblocked task from the board
2. READ     its linked design document before touching anything
3. RED GATE run the verifier first: it must fail
4. DELEGATE brief an executing session, or build it yourself
5. PROVE    re-run every claimed command; exit codes decide
6. OBSERVE  read the diff hunk by hunk
7. GATE     resolve the approval lane, posting reasoning
8. SHIP     flip status, commit that item alone, record progress
```

### Why the red gate comes first

**If the check is already green before you start, the work proves nothing.** You cannot tell a correct implementation from a check that never runs, a filter that matches nothing, or a test asserting something already true.

Running the verifier first also catches stale work cheaply. In practice a meaningful share of queued tasks turn out to be already done, built under a different card or made moot by a later change. A red gate that comes back green in one command costs seconds and saves the hour you would have spent reading code to implement something that already exists.

### Why one commit per item

Git history stays one-to-one with the board. Every commit’s subject names its task. When something breaks three days later, the path from symptom to decision is one `git log` away.

## Verification discipline: the heart of the pattern

This is the part that distinguishes the methodology from “run several agents at once.”

### A report is evidence, not instruction

When an executing session reports “suite green, 49 checks, zero failures,” the coordinator’s job is to find out whether that is true. Not because agents lie, but because **the thing they are reporting on and the thing they checked are often two different objects.**

One pattern worth internalizing: a session wrote a commit hash into a log file by hand, then verified it with `git cat-file`, against the short hash sitting in its shell rather than the string it had written. Both checks passed. The file contained a hash that resolved to nothing. The check and the record were two different objects, and only one was tested.

The rule that falls out: _verify the artifact by reading the value back out of the artifact_, never from the variable you think you wrote there.

### The defect class to watch for

The single most common failure in agentic engineering is **an instrument that reports success for work it did not do.** It has many shapes.

| Shape | What it looks like | How it fools you |
| --- | --- | --- |
| Vacuous assertion | A test that passes whether or not the feature works | Deleting the thing under test leaves it green |
| Silent no-match | A grep, filter, or predicate that matches nothing | Zero findings reads as “clean” |
| Errored check | A command that failed to run at all | The error is swallowed, absence reads as evidence |
| Wrong reference | A filter keyed on “newer than X” | Anything that happened in between slips through |
| Stale premise | A check whose expected value was read off broken code | It passes the bug it was written to catch |
| Scope mismatch | A green check over a subset presented as the whole | The denominator is never stated |

**The general defense:** every check that can fail to match must say so. A count of zero and a failure to run must be distinguishable. And an absence assertion needs a positive control in the same run, because if nothing ran, “nothing bad happened” passes.

### Prove a positive before believing a negative

Before concluding something is absent, prove your instrument can find it when it _is_ present. Point the check at a known-good case first. A tool that reports “clean” and a tool that is broken produce identical output.

## Durable channels beat ephemeral ones

Sessions can message each other directly. That channel is genuinely useful. It is how a coordinator answers a question mid-run, and how an executing session flags a contradiction rather than working around it.

**But it is not reliable enough to depend on.** A message can be queued behind a busy session, held for approval depending on the receiving session’s permission mode, or expire undelivered. Silence is not agreement.

So anything that must arrive goes in a durable channel.

-   **Committed files.** A brief, a handoff document, a constraint. Sessions read the repository at startup.
-   **Board cards and comments,** where work-specific context belongs.
-   **Share links.** Most boards can render a task or document as agent-ready text at a URL. Put `Context: <url>` in a launch prompt rather than pasting the context into it. The prompt stays short, and the context stays where it is maintained.

A message is a nudge. A file is a contract.

### Where things live

A small discipline that pays off: **keep durable policy separate from ephemeral work content.**

Policy directories hold the contract that governs every cycle, meaning the loop, the routing rules, and the standards. Long-lived, reviewed, rarely changed. One-off briefs, task context, and session-specific instructions belong on the board or in a scratch directory.

Mixing them means that in six months nobody can tell which files still govern anything.

## Timeboxing: surfacing without stopping

A long autonomous run should report on a cadence rather than disappearing for hours and returning with a wall of diff.

The rule that makes timeboxing work: **the interval decides how often you surface, never where the work stops.** When the timer expires mid-item, finish the item, verify it, commit it, _then_ report. Cutting a run mid-task strands work in the state that is hardest to recover, which is half-applied, unverified, and impossible to describe honestly.

A checkpoint is a surfacing moment, not a permission request. The report goes out and the next item starts in the same turn. If you catch yourself writing “shall I continue?”, delete it. A human who is watching will interrupt, and a human who is not has just had their run killed by a question.

Report what is _proven_, not what was attempted. An item without a verification result is carried, not done.

## Practical mechanics that cost time to learn

These are small, and each one has a failure mode that looks like something else.

**Verify a spawned session actually started.** Launchers report that a workspace was _created_, which is not the same as an agent _running_. Check for the process, and check its working directory:

```
launched_at=$(date +%s)
# ... spawn the session ...
# then accept only a process whose start time is after $launched_at
```

Capture the reference timestamp immediately before the launch. A filter keyed on “newer than the last session” will happily admit an unrelated session that started in between, and if that one has a different working directory, a healthy launch looks broken.

**Session names are not addresses you can guess.** Whatever name you gave a workspace is often not the name the messaging layer uses. Re-list the live sessions before addressing one, and do not reuse a name you read earlier.

**Short identifiers are display prefixes, not keys.** Boards commonly show a truncated ID. Padding it out into a full-length identifier produces a well-formed value that does not exist. Resolve it by searching for a distinctive label substring instead.

**Search for the label, not your paraphrase.** A log entry’s title is usually the writing session’s framing of what it did, which is not the card’s actual label. Searching for the former finds nothing and reads as “no such card.”

**In a shared working tree, never use a bare commit.** `git add <path>` followed by `git commit` commits the _entire index_, including anything a concurrent session has staged. Use `git commit -- <paths>` so the commit takes only what you named.

## When to use this pattern, and when not to

**Use it when:**

-   The work spans more sessions than one context window holds.
-   Multiple work streams can proceed in parallel.
-   Correctness matters more than speed, and a wrong “done” is expensive.
-   The project will outlive any single session’s memory.

**Do not use it when:**

-   The task is a single well-scoped change. One session, no ceremony.
-   You cannot afford the coordination overhead. The pattern spends real tokens on verification that produces no code.
-   There is no durable store. Without one you are not running this pattern, you are running several sessions and hoping.

The overhead is the point. You are buying the ability to trust the result.

## Getting started

1.  **Stand up a durable board.** One project, a handful of goals, tasks with dependency edges. Make sure your agent can reach it over an API or MCP.
2.  **Write the contract down.** One file that states the loop, what “done” means, and the standards. Commit it. Every session reads it at startup.
3.  **Run one coordinator and one executor.** Do not start with six. Get the verification loop honest with two.
4.  **Add a handoff artifact.** A single file the coordinator updates at the end of every session with the current state and anything learned. This is what makes sessions compound.
5.  **Keep a lessons log.** When something surprises you, write it where the next session will read it, before that session ends.

The measure of whether it is working is not how much code gets written. It is whether, at any moment, you can ask “what is the state of this work?” and get an answer that is true.

## Closing thought

The instinct when AI coding agents underperform on long work is to reach for a better model or a bigger context window. Both help. Neither addresses the actual constraint, which is that **nobody is checking.** That is the same gap behind [the 70% problem](https://asyncdot.com/blog/the-70-percent-problem-ai-mvps), and behind every agent that [operates a live system](https://asyncdot.com/blog/headless-wordpress-mcp) without a read-back step.

A coordinating session that writes no code but knows what is true is worth more than another executor. That is an old lesson from human organizations, and it turns out to transfer.

// frequently asked

## Common questions

What is the Chief of Staff pattern in AI agent orchestration?

Chief of Staff is our name for a coordination shape that already exists under other names. One long-lived AI session coordinates and verifies work while separate sessions execute it, with shared state held in a durable external store rather than in conversation context. The coordinating session writes briefs, re-runs claimed verification commands, reads diffs, and records lessons. It does not write the implementation, because a session that is implementing has stopped verifying. The same shape is known as orchestrator-worker, supervisor or hierarchical orchestration, coordinator-implementor-verifier, and maker-checker.

Is the Chief of Staff pattern an established term?

No. The job is real and common in multi-agent design, but the label is ours. The established names for the same shape are orchestrator-worker, supervisor or hierarchical orchestration, coordinator-implementor-verifier (CIV), and maker-checker or validation chain. The human equivalent is the integration manager from Git's distributed workflows: contributors work in their own repositories and one maintainer pulls each change, tests it, and decides what lands. Claude Code's own documentation frames it as a team lead with teammates. Those are the terms to search for prior art. Separately, the phrase chief of staff agent is widely used for something different: an assistant that runs a person's calendar, inbox and priorities and routes work to specialist agents. Anthropic's cookbook has one of exactly that kind, built for a startup CEO. Same metaphor, different problem.

Why not just run one long AI coding session?

Three things break. Context is finite and gets compacted, so details that mattered three hours ago survive only as a summary. Self-reports drift from reality as sessions lengthen, because an agent reporting 'tests pass' is reporting recollection, not a fresh observation. And nothing compounds: a lesson learned at hour two is gone by the next session unless it was written somewhere the next session reads. A coordinator plus a durable board addresses all three, because the state lives outside the conversation.

Do I need cmux and Plan Desk specifically to run this pattern?

No. You need two capabilities: a way to spawn isolated agent sessions programmatically, and a durable task store with an API or MCP surface the agents can reach. cmux and Plan Desk fill those roles and are scriptable, which is the property that matters. Any substitutes with the same properties work. What you cannot substitute away is the durable store. Without one you are not running this pattern, you are running several sessions and hoping.

How does the coordinator verify an executing session's work?

By re-running the commands the session claims to have run and reading the exit codes, by reading the diff rather than the transcript, and by checking artifacts by reading values back out of the artifact instead of out of the variable that was supposed to be written there. A summary is treated as a statement of intent, never as an observation. Exit codes are authoritative.

What is a red gate and why run it before implementing?

A red gate is the verifier for a task, run before any implementation, which must fail. If the check is already green before the work starts, you cannot distinguish a correct implementation from a check that never runs, a filter that matches nothing, or a test asserting something already true. Running it first also detects tasks that are already complete, which costs one command and saves the hour spent implementing something that already exists.

How should AI agent sessions communicate with each other?

Through two channels with different guarantees. Direct messages between sessions handle questions and flags, but they can be queued behind a busy session, held for approval depending on the receiving session's permission mode, or expire undelivered. Silence is not agreement. Anything that must arrive goes in a durable channel instead: a committed file, a board card or comment, or a share link. A message is a nudge, a file is a contract.

How long should a timebox be for an autonomous agent run?

Long enough that work items finish inside it, short enough that a human can interrupt at a good moment. Fifteen to thirty minutes suits most work. The critical rule is that the interval governs how often you report, never where the work stops. When the timer expires mid-item, finish the item, verify it, commit it, then report. Cutting a run mid-task strands work half-applied and unverified, which is the state that is hardest to recover.

Does the Chief of Staff pattern work with models other than Claude?

The methodology is model-agnostic. It assumes only that sessions can run tools, reach a shared store, and be spawned programmatically. Mixed-model setups have a real advantage: having verification done by a different model family than the implementation catches failures a model is systematically blind to in its own output.

## 溯源

- 核心主张：长时间 AI 编码的瓶颈不是写代码而是没人核实：让一个会话只协调和验收、不写实现，状态放在会话之外的持久看板，执行者的汇报只当证据、重跑命令以退出码为准，并先确认检查会失败、先证明检查能测出问题，再相信“没问题”。
- 源知识：
  - [构建高效的智能体](../roots/anthropic-2024-building-effective-agents.md) · 关系：换了说法 · 强弱：强。作者自己说这个形状早就叫 orchestrator-worker（编排者-工人），“幕僚长”只是他们起的名字；编排者-工人正是这篇列出的工作流模式之一
  - [职责分离（四眼原则、制单与复核分开）](../roots/separation-of-duties.md) · 关系：直接源自 · 强弱：强。作者明说同一形状也叫 maker-checker（金融和运营里的制单与复核分开）；协调者“一开始写代码就不再核实”正是职责分离要防的事
  - [测试驱动开发](../roots/test-driven-development.md) · 关系：换了说法 · 强弱：强。“红灯门”要求开工前先跑验证、必须失败，和测试驱动开发“先写一个会失败的测试”几乎一样，理由也相同：否则分不清是做对了还是检查根本没在测
  - [变异测试（检验测试本身能不能抓到错）](../roots/mutation-testing.md) · 关系：相近 · 强弱：弱（模型复核通过）。作者最担心“检查报告成功、其实没测到”（删掉被测功能测试仍然是绿的），要求先证明检查在问题存在时能抓到；变异测试正是故意植入错误、看测试能不能失败，来检验测试本身
  - [长时间运行 agent 的有效 harness](../roots/young-2025-long-running-agent-harness.md) · 关系：相近 · 强弱：弱（模型复核通过）。一次只做一项、每项单独提交、会话结束前写交接文件和经验、验证通过才标完成，和 Anthropic 长时间运行 agent 的 harness 做法高度相近（作者没有引用它）
- 本质：这条新知识本质上是职责分离（制单与复核分开）和测试驱动开发在多会话 AI 编码编排上的应用：执行者的自报不算数，状态和证据都放在会话之外。
- 整理于：2026-10-25（第 8 轮）
