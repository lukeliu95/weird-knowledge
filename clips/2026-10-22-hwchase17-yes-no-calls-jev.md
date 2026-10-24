---
title: "Harrison Chase：agent 里很多步骤是是非题不是生成，交给决策模型给带校准的概率，大模型只做难的"
author: "Harrison Chase (@hwchase17)"
url: https://x.com/hwchase17/status/2108777335650476163
source: X
published: 2026-10-10 04:31 UTC
saved: 2026-10-22
why: "探索日报：Luke 想看"
related_principles: [原则 11, 原则 3, 原则 12]
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [dual-process-theory, chen-2023-frugalgpt, anthropic-2024-building-effective-agents, guo-2017-calibration, comparative-advantage]
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

- 核心主张：agent 里大量步骤其实是是非题、选择题，不需要生成；把这些交给一个便宜的小决策模型直接给出带校准的概率，贵的大模型只做真正难的思考，真正的动作交给代码执行。
- 源知识：
  - [双过程理论（系统一 / 系统二）](../roots/dual-process-theory.md) · 关系：直接源自 · 强弱：强。推文链到的 LangChain 文章标题就把 Jev 叫作“系统一模型”：快速直接给判断的是系统一，逐字生成、费力推理的大模型是系统二。
  - [FrugalGPT：用级联大模型省钱又提效](../roots/chen-2023-frugalgpt.md) · 关系：相近 · 强弱：弱（模型复核通过）。“便宜的模型挡在前面，判断哪些值得交给贵的模型”就是 FrugalGPT 的级联和路由，只是从问答搬到了 agent 每一步的分岔口。推文没引它。
  - [构建高效的智能体](../roots/anthropic-2024-building-effective-agents.md) · 关系：相近 · 强弱：弱（模型复核通过）。该文的“路由”工作流就是先给输入分类、简单的交给小模型、难的交给大模型；Harrison 说的“这些判断在 harness 里放在哪”讲的就是这种位置。
  - [现代神经网络的校准（温度缩放）](../roots/guo-2017-calibration.md) · 关系：相近 · 强弱：弱（模型复核通过）。卖点是“带校准的概率”：模型说八成把握时真的约八成对，才能拿概率定门槛、决定要不要升级给大模型；Guo 等 2017 是指出现代神经网络失准、并用温度缩放修正的经典论文。推文只用了“校准”这个词，没引它。
  - [比较优势](../roots/comparative-advantage.md) · 关系：相近 · 强弱：弱（模型复核通过）。被引推文说“不是 Jev 比 Claude 聪明，而是没人要它当 Claude”：大模型做是非题也许更准，但机会成本高，让它专做相对最擅长的难事、把小判断交出去整体更划算，这就是比较优势。
- 本质：这条新知识本质上是“级联加路由”（便宜的先判、值得的才交给贵的）在 agent 每一步分岔口上的应用，用“系统一 / 系统二”做比喻，靠概率校准来定交接的门槛。
- 整理于：2026-10-24（第 6 轮）
