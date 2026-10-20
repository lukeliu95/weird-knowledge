---
title: "包月 AI 是陷阱：Grok Bot 五个员工配 Kimi K3 的搭法"
author: "slash1s (@slash1sol)"
url: https://x.com/slash1sol/status/2092987091273613457
source: X Article
published: 2026-08-27 14:46 UTC
saved: 2026-10-20
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

# Flat-Rate AI Is a Trap. I Run 5 Workers for $3/Million Tokens: The Exact Setup

> Grok Bot will hand you an office in one evening: five named workers, one shared cloud computer, logins that stay signed in. The one thing it does not hand you is the brain behind the desks. That part you pick yourself, and this is the build where the brain is @Kimi_Moonshot  K3.

## 5 workers · 1 shared computer · 1 engine · 1,048,576 tokens of working memory

![Image](https://pbs.twimg.com/media/HQrdkJUXYAAqWka.jpg)

Everyone on your timeline is hiring this week.

Since Grok Bot shipped, the screenshots are everywhere: rosters of named workers, each with a job title, all living on one cloud computer with its own browser, files and terminal. They sign into real tools, hand work to each other in group chats, and keep going after the laptop closes. The office part of this is genuinely solved, and it took an app to do it.

Here is the part the screenshots skip. A desk is furniture. What decides whether the roster produces anything worth reading is the engine that answers every time a worker starts thinking, and that one choice outweighs every charter you will ever write.

> So treat them as two separate decisions. Grok Bot is the best office an agent has ever had. @Kimi_Moonshot  K3 is the brain I would put behind every desk in it. The rest of this article is that build: why K3, how to install it once for the whole floor, and how five seats run on it without you in the room.

# The detail that makes the whole build cheap

One fact about Grok Bot does the heavy lifting: every worker on your account shares one computer. Files, browser sessions, terminal, logins -- one machine, many screens.

Most people read that as a security footnote, and it is one: keep anything you would not hand to the whole staff off that machine. But read it as an installer instead. Anything you set up on that computer once is set up for everyone you will ever hire. Install an engine tonight and the worker you create in October arrives already thinking with it.

> You are not configuring five agents. You are wiring a building. One installation, one config in the folder that survives updates, and the whole floor changes what it thinks with.

# Why the brain is K3

![Image](https://pbs.twimg.com/media/HQrdp4uXEAARP_l.jpg)

Translate the spec sheet into office terms and the pick makes itself.

The million-token context is the worker who actually read the whole binder. A term of documents, a full codebase, a night of logs in one sitting -- and a worker that started reading at midnight still remembers instruction one at 4am, because nothing got compacted away mid-shift.

Native vision matters more here than in a chat window, because workers live inside browsers. Screenshots and screen recordings stop being attachments nobody opens and become working input the engine reads directly.

The tooling is open. Kimi Code CLI is free and MIT licensed, the K3 weights are published, and the model id is one string: kimi-k3. An engine you can inspect is an engine you can trust with your logins.

> And the meter fits an office better than a seat does. $3 per million tokens in, $0.30 when the context repeats, $15 per million out. An office re-reads the same charters, files and histories all day long, so most of an office's day is the cheap kind of token. Five workers, one bill, and the bill tracks work done instead of desks bought.

# The install

You will look for an engine picker in the app. Stop looking -- the route is simpler and slightly funnier: the workers install their own brain. The shared computer takes instructions, so you never open a terminal yourself. You hire someone into one.

Hand your first worker this:

Two doors exist because Kimi sells access two ways: the Kimi Code console and the pay-as-you-go platform. Different base URL, same model. Use the door your key came from, and send the key through the secure request, never the chat box -- a password typed into a message lives in that transcript forever.

> Three errors cover almost every failed first evening: a key from the wrong door, a plan without K3 on it, or a plan that caps context at 256K. Each one names itself in the error message. Fix the door, not the config.

# The roster

Five seats, each defined by what it owns and where it stops. The second half of every card matters more than the first.

- SCOUT owns the outside world: pages, feeds, filings. It comes back with a list and a source on every line, never a summary. 

- CLERK owns the inbox and the forms; drafts pile into a queue, and nothing is sent until a human presses send. 

- LEDGER owns the money week: what renews, what it costs, where each number was read -- and it is forbidden from cancelling anything, ever, because a cancel is not reversible. 

- BUILDER owns deliverables: the report, the deck, the sheet. When a job outgrows one desk -- analyze a hundred of something -- BUILDER hands it to Kimi Agent Swarm and comes back with the finished artifact instead of a promise. 

- CHIEF owns the gate: everything one-way -- sending, money, publishing, deleting -- stops in CHIEF's ask queue, and CHIEF stops at you.

A charter is four sentences, written once. It is not a prompt. A prompt says what to do today; a charter says what the seat owns, what finished looks like, and where the seat stops.

> The stopline is the line people leave empty, and it is the only line that lets you close the laptop. A worker never told what counts as one-way decides for itself, and it decides generously.

# The handoff

![Image](https://pbs.twimg.com/media/HQreLz6XwAABlX_.jpg)

Two workers, and ferrying results between them quietly becomes your third job -- unless the routing lives in their descriptions instead of your attention. Grok Bot routes group work by what each worker's description says it owns. So a group opens with a goal, not a checklist, and the pieces find their owners. Put an @ in front of a name only when you want that one and nobody else.

One rule turns the group from a chat into a pipeline: nothing moves between desks without a source. Every number carries where it was read and when. A handoff missing that bounces back to the desk it came from -- SCOUT fixes its inputs, CLERK does not repair them downstream.

> The rule sounds like paperwork until you notice what it removes: re-checking the numbers by hand, because you cannot tell a retrieved figure from a confident invention. That silent tax is what usually eats the time a roster saves. With the rule, an unsourced number is a bounce, not a judgment call.

# The shift

![Image](https://pbs.twimg.com/media/HQreSerXkAAFzWw.jpg)

Everything so far still starts with you. You open the app, you type the job, and work happens because you showed up -- which is the old job with better staff. The last move is putting the day itself on a schedule.

Run each job once by hand first and correct it until you would sign it. Only then does it get a shift. A schedule is one sentence naming the owner, the time, the input, the deliverable, the stop, and the fallback:

> Then one habit keeps the roster honest: on Friday, ask each worker to rate its own routines and suggest one improvement, and delete the weakest routine. A roster nobody reviews quietly turns into a pile of old habits with names attached.

# What it costs, honestly

![Image](https://pbs.twimg.com/media/HQreecKWcAEZvEA.jpg)

The office is a flat cost -- Grok Bot comes bundled with the subscription tiers that carry it. The brain is a meter: $3 per million tokens in, $0.30 when context repeats, $15 per million out, billed on your own key.

> A meter beats a seat while you are building, testing and running a normal week, and it loses at industrial volume. That crossover is real, not marketing, and it lands in a different place for every tier and every workload. Run your month against your own numbers before you move anything. The point of this build is not that metered is always cheaper. It is that the engine becomes a decision you made instead of a default you inherited.

# When not to hire

> If your list is three one-off jobs, a single chat window does them tonight and a roster is theater. A job earns a desk when it comes back every week, needs its own memory, and hands pieces of itself to somebody else. Hire for those, keep the rest as saved routines, and stop adding seats the moment a new one has nothing to own.

# The point

Grok Bot solved the office: the desks, the logins, the handoffs, the part that keeps working after you leave. It left open the only decision that decides the output -- who does the thinking.

> Install the brain once, on the computer they all share, and every worker you ever hire walks in already smarter. Five desks. One engine. A bill that tracks work instead of headcount.

1. Hire the desks. 

2. Install the brain. 

3. Then clock out.

By slash1s (@slash1sol)

## 溯源

