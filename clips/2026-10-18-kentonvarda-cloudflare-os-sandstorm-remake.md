---
title: "Cloudflare OS 个人应用平台"
author: "Kenton Varda (@KentonVarda)"
url: https://x.com/KentonVarda/status/2084990137180590572
source: X
published: 2026-08-05 13:09 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: Agent 与 Skill
roots: []
---

## 原文

Today we are releasing Cloudflare OS, a chatbot with connectors, just like every other tech company is doing.

Except actually, it's different. This is a remake of Sandstorm[.]io, my startup from 10 years ago, except this time built on Cloudflare Workers (the platform I've spent the last 9 years building) and deeply leveraging AI. This is more or less the culmination of my secret 10-year master plan.

This is a full-on personal app vibe coding platform, in which the sandbox is so secure that you can pretty much go wild -- the AI cannot introduce a significant security bug. We believe a company's security team can feel comfortable giving non-technical users permission to vibe code and then sleep soundly at night.

How is that possible? It's the Sandstorm security model, revisited. A "Gadget" is the same thing as a Sandstorm "Grain": a fine-grained app instance. For example, if you have a document editor app, each document runs as a separate instance of the app, in a separate sandbox (one "Gadget").

This means two things, both of which I think are Big Deals:
1. The platform can manage all access control, by controlling who can access the Gadget at all. There is no way the Gadget can accidentally leak itself to an attacker -- even an attacker who has access to other Gadgets based on the same app.
2. Since everyone is running their own copy of the code, everyone can freely *modify* their copy of the code.

Think about #2 a bit more.

What if, when you wanted a new feature in the software you are using, you could just prompt your agent to add it?

This doesn't work in the cloud Software-as-a-Service model, because you are not running your own copy of the app.

Sandstorm tried to change that 10 years ago, but the world wasn't ready, because not enough people had the skills or patience to actually modify their software. AI has changed that. Now you just ask the agent -- the same agent that you are using to help you interact with the Gadget can also modify the code of the Gadget.

And it is so fun.

https://t.co/qzwdrAQhtK

## 溯源

