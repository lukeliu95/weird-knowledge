---
title: "OpenAI Dots 放权指南：动作分进 6 个权限区，每周按证据升降"
author: "chuplung (@choopyplug1)"
url: https://x.com/choopyplug1/status/2106470038488092746
source: X Article
published: 2026-10-03 19:42 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

# OpenAI Dots: How to Give Your Dot Real Autonomy Without Handing Over Your Accounts

> A step-by-step permission system for an always-on agent: what runs alone, what waits for you, what stays read-only, and what always comes back to your hands.

OpenAI launched dots on September 29: always-on agents on GPT-6 Astra, each with its own cloud computer and access to over 4,000 apps.

The hard part is not what a dot can do. It's deciding what it should do without you.

This guide builds that decision, step by step, on one real responsibility, from the first action list to a weekly review that earns your dot more freedom.


![Image](https://pbs.twimg.com/media/HTujqoKXsAAzdDD.jpg)

## 01. Know what you can change, and what you can't

Before you write a single rule, know where the walls are. Some are OpenAI's. The rest are yours.

Fixed by OpenAI: built-in safety requirements, take-overs for changing a password or transferring money, Auto-review before certain actions, and read-only tools for proactive research.

Yours: which apps you connect and their permissions, access to your local computer (off by default), Custom Rules, and the instructions in each task.

Your rules can tighten freely, but only loosen inside the box OpenAI drew.

![Image](https://pbs.twimg.com/media/HTukM6qWYAAkzz4.jpg)

That's good news. You don't design for password resets or bank transfers. You design the space inside the box.

If your dot only reads and summarizes, the defaults are enough. You need your own system the moment your dot can:

- Send something: email, Slack posts, replies to customers.

- Change something others rely on: shared docs, calendars, code.

- Hold more than one responsibility at once.

![Image](https://pbs.twimg.com/media/HTunAo9WkAAtG-2.jpg)

From here on, Official marks what OpenAI documents. Everything else, the zones, templates, thresholds and review rules, is our framework. OpenAI didn't publish it. Adapt it.

## 02. List every action before you permit any

Most people connect apps first and fix permissions after the first surprise. The few start with a list of every action.

One responsibility runs through this guide: keep the customer feedback summary current, from #feedback in Slack and support emails in Gmail.

The line that matters is "Who besides me would see the result."

It surfaces the helpful-looking extras: replying to a customer "to confirm the bug," tagging a teammate, editing a shared roadmap doc, opening a GitHub issue.

![Image](https://pbs.twimg.com/media/HTun-FkWYAAbiYx.jpg)

## 03. Put every action in a permission zone

A list isn't a policy. Each action needs a zone: a clear answer to "what happens when the dot wants to do this?"

Our framework uses six: Watch, Draft, Ask, On request, Free, and Yours. Watch and Draft need no rule, just read-only app permissions and the instruction "draft, don't send."

The safest permission is the one the dot never had.

![Image](https://pbs.twimg.com/media/HTuoPEbXEAAhN4x.jpg)

To pick a zone, ask four questions in order. The first "yes" decides.

1. Does it touch money, credentials, access, or permanent deletion? Yours.

2. Will anyone other than you see the result? Ask, or On request for one fixed, repeated message.

3. Is it hard to undo in one step? Ask.

4. Is it new, with no clean history yet? Draft.

5. None of the above? Free.

Here's the feedback inventory sorted, as an optional YAML record. It's our author-built representation, not something Dots reads. It keeps your zones portable and becomes the source for the rules in the next steps.

Look at what's in Free: almost nothing. That's the point. Free is not the default. Free is what's left after every reason to stop has been ruled out.

## 04. Write the scope before you write a rule

Rules say what kind of action is allowed. Scope says for which job, from which sources, for how long.

In UK AISI testing reported in the GPT-6 Astra system card, the model behind dots went out of scope in 60 of 499 simulated cyber challenges when scope was ambiguous. With explicit scope: 2 of 500.

A model evaluation, not a dots test. The lesson still holds: an explicit boundary does work an implied one can't.

![Image](https://pbs.twimg.com/media/HTuoox_XgAAXSyY.jpg)

So every responsibility gets a six-field scope brief.

NEVER turns "it seemed useful" into "explicitly out of scope." EXPIRES gives an always-on job an end date.

Keep one brief per responsibility, so jobs don't leak into each other.

## 05. Turn the boundaries into Custom Rules

Scope lives in a task. Custom Rules hold across everything your dot does.

Official: four behaviors, set under Customize → Custom rules. "Pre-approved" means you explicitly requested the action in your prompt, not a whitelist.

A starter set as a Markdown policy doc. The format is ours; you still enter each rule by hand.

The key is in the phrasing. Write each action like a lawyer, not like a friend.

"Be careful with email" gives the dot nothing to match against. "Sending any email to a recipient other than me" does. A rule that half-matches a new action is where surprises come from.

![Image](https://pbs.twimg.com/media/HTupuw3X0AAJpZP.jpg)

Reads are missing on purpose. They're controlled by which apps you connect, not by rules.

And OpenAI says the dot can make mistakes even while following rules. So the best rule is still a permission the dot never had.

## 06. Make every approval narrow and temporary

Approvals are where autonomy grows, and where it quietly leaks.

Official: password changes and money transfers always come back to you. Recurring messages can be approved in advance.

That advance approval is the risky one. "Post updates in Slack" quietly means every channel, every update, forever.

![Image](https://pbs.twimg.com/media/HTup-iwWwAAczAR.jpg)

Our rule: every standing approval names who, what, when, and until. Here it is for the weekly summary post.

OUTSIDE does the work. It turns the approval from a door into a fence: anything it doesn't name falls back to Ask.

OpenAI's docs suggest the same habit for schedules: a time zone, an end date, and a confirmation from the dot.

An approval without an end date is not an approval. It's a policy you forgot to review.

## 07. Decide how your dot hands work back

A hand-off is the moment your dot stops and gives the next step to you.

OpenAI fixed the most sensitive ones. You add the rest, and decide what a hand-off looks like when it lands.

Skip this and you get one of two failures. The dot asks about everything and you start approving blindly. Or it asks about nothing.

Three triggers should always stop the work: ambiguity, novelty, and conflict.

![Image](https://pbs.twimg.com/media/HTuqSdDW4AEfPlL.jpg)

Send this once, as a standing instruction.

Item 4 matters most: "default: do nothing." Silence should freeze an action, not unlock it.

That's what catches the classic case. A customer writes "please just refund me." It's novel, it touches money, and it isn't in the inventory. The dot stops, recommends, and waits.

![Image](https://pbs.twimg.com/media/HTuqiUeXUAA42Ub.jpg)

Official: content the dot encounters while working, like an email or a web page, doesn't grant permission on its own. Your escalation rules reinforce that from your side.

Instructions come from you, not from inside the inbox.

## 08. Run it on one real responsibility you can survive

Don't test this on the thing your quarter depends on.

Pick something useful, repeating, and cheap to fix if the dot gets it wrong. The feedback summary fits: real value, low blast radius.

For the first week, every write stays in Draft, even actions you zoned higher. You're not testing the dot yet. You're testing whether your system describes reality.

![Image](https://pbs.twimg.com/media/HTuqzjNXAAAoeoj.jpg)

The "Would have done" list is the real output of the week: a zero-risk preview of what your dot does with more freedom.

![Image](https://pbs.twimg.com/media/HTuq9sSWcAAS4nL.jpg)

Read it with one question: "Would I have been surprised?"

Yes means a tighter zone, a sharper rule, or a new line in NEVER. No means a promotion candidate.

## 09. Review the week in fifteen minutes

Autonomy that's never reviewed only ever grows. Nothing pulls it back.

Official: in the desktop app, your dot's profile shows Activity, with tasks under In progress, Scheduled, and Completed.

Activity shows what happened. It doesn't show what nearly happened. So add a self-audit.

Read item 5 first. Schedules and standing approvals pile up quietly and outlive the reason they were created.

Then read the flags. "Not sure I was allowed" is your best early signal. It marks where your scope stopped matching reality, before that gap becomes a mistake.

![Image](https://pbs.twimg.com/media/HTutQi-WYAAA7Su.jpg)

## 10. Promote and demote on evidence, not mood

Each week, every action moves up a zone, down a zone, or stays. The thresholds are ours: tune them, but keep the asymmetry.

- Draft → Ask: two weeks of drafts you sent with only cosmetic edits.

- Ask → On request: you approved the same action unchanged every time for two weeks.

- On request → Free: only for actions only you see, or that undo in one step.

- One zone down: one surprise, an action you didn't expect, even if harmless.

- Straight to Yours: any mistake that reached another person.

Trust is promoted by evidence and demoted by surprise.

![Image](https://pbs.twimg.com/media/HTurZWLX0AAoTxU.jpg)

Then make exactly one change per week: one promotion or one demotion, plus a NEVER line for any new near-miss and a delete for any standing approval past its use.

Change three things at once and you won't know which one broke.

Log each move as a small JSON record. It's our author-built audit record, not an OpenAI schema.

In a month, that log is a record of exactly what your dot has proven it can handle.

## 11. Know what every stop button actually stops

Learn these before something goes wrong, not during.

Official: the controls are separate, and they don't overlap the way people assume.

![Image](https://pbs.twimg.com/media/HTuti8BX0AA42Pn.png)

The trap is treating Pause as an off switch. It isn't.

A full stop is three moves: Pause the dot, stop running tasks in Activity, and pause anything under Scheduled. Then ask for every action from the last 24 hours, and fix what can be fixed.

Write that down now, while nothing is on fire.

# What The Hype Skips

The marketing story is "set it and let it work." The real failure doesn't look like an agent going rogue.

It looks like a chain of small, reasonable gaps, where every layer is aimed at a slightly different one.

![Image](https://pbs.twimg.com/media/HTut1ovWQAAJKhb.jpg)

No single layer failed. That's why this system stacks scope, rules, approvals, and hand-offs instead of trusting any one of them.

Three limits worth knowing up front:

- Memories can't be edited one by one. Clearing them means deleting the dot, so connect fewer apps than you're tempted to.

- Rules are followed, not guaranteed. OpenAI says the dot can make mistakes while following them. Review consequential work.

- Availability is limited. At launch: Pro outside the EEA, Switzerland and the UK, Business Premium, and an Enterprise beta that admins must turn on.

# Conclusion

A dot's power is that it keeps working when you don't. That's exactly why its permissions need to be designed, not discovered.

The whole system fits on one page: list the actions, sort them into zones, scope every job, encode the rules, narrow every approval, and decide how work comes back to you.

Then let evidence do the rest. A week in Draft shows what your dot would do. A weekly review shows what it nearly did. One change at a time turns both into trust you can explain.

Most people will hand their dot the keys on day one and spend the next month cleaning up. The few will earn the same autonomy step by step, and know exactly why every permission exists.

Start with one responsibility, everything in Draft, and one change per week.

## Autonomy is not a setting. It's a promotion.

## 溯源

