---
title: "Harrison Chase：agent 里很多步骤是是非题不是生成，交给决策模型给带校准的概率，大模型只做难的"
author: "Harrison Chase (@hwchase17)"
url: https://x.com/hwchase17/status/2108777335650476163
source: X
published: 2026-10-10 04:31 UTC
saved: 2026-10-22
why: "探索日报：Luke 想看"
related_principles: [原则 11, 原则 3, 原则 12]
status: 未整理
kind: 观点
topic: Agent 与 Skill
roots: []
---

## 原文

good framing from @ch3nweiii - a lot of agent steps are yes/no calls, not generation

Jev answers those as typed questions with calibrated probabilities, so the frontier model sticks to the hard work

where those calls sit in a harness: https://t.co/xZMxbATLHd

https://t.co/Z3DGL8hTdS

> 链接卡片：What Is Jev? A Guide to TypeSafe AI’s System One Model（https://www.langchain.com/blog/building-a-harness-with-jev）

### 引用的推文（@ch3nweiii，https://x.com/ch3nweiii/status/2108664035109470637）

whoever built this realized we've been using our smartest AI for the dumbest possible jobs

your $20-$200/mo frontier model is researching, writing code, planning…

and then you're paying that same brain to decide YES / NO.

Jev flips that.

it's a tiny decision model that sits in front of the expensive stuff and takes the boring forks:

-> which agent goes next?
-> is this worth researching?
-> reply or ignore?
-> publish, wait or escalate?
-> BUY / SELL / HOLD?
-> click this or keep looking?

then I saw the numbers people are posting and the whole architecture started making a lot more sense.

~1,000 papers classified for around $0.08
~500 emails sorted for around $0.035

browser-agent loops shown at around 7 seconds for ~$0.0039

and at the quoted pricing, roughly 10,000 ~1K-token decisions comes out around $0.42.

that's not because Jev got smarter than Claude.

it's because nobody asked it to be Claude.

the setup is stupidly simple:

-> big LLM gets the hard thinking, research and writing
-> Jev gets the thousands of tiny decisions between those steps
-> code actually clicks, saves, sends and runs

and suddenly you start seeing these little decisions everywhere.

> your inbox.
> X feed.
> support queue.
> meetings.
> leads.
> video clips.
> browser agents.
> even paper-trading loops.

that's the part I think most agent builders are missing.

the expensive model doesn't need to touch every step just because it's able to touch every step.

> let Claude think.
> let Jev decide what deserves Claude.
> let code do the actual work.

I broke down how to wire Jev into your agent + the exact router setup in the article below

> 媒体：
> - https://video.twimg.com/amplify_video/2108653012562399232/vid/avc1/1080x1350/gqMpC5vx2F14gZXO.mp4?tag=29

## 溯源

