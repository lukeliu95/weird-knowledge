---
title: "吴恩达讲做产品的三个循环"
author: "Andrew Ng (@AndrewYNg)"
url: https://x.com/AndrewYNg/status/2071988145667928442
source: X
published: 2026-06-30 16:04 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: AI 产品与创业
roots: [human-in-the-loop, cybernetics, test-driven-development, lean-startup, the-use-of-knowledge-in-society]
---

## 原文

“Loop engineering” is a hot buzzphrase after mentions of it by Boris Cherny (Claude Code’s creator) and Peter Steinberger (OpenClaw's creator) went viral on social media. Loops are now a key part of how we get AI agents to iterate at length to build software. In this letter, I’d like to share my 3 key loops, shown in the image below, for building 0-to-1 products. These loops guide not just how I build software, but also how I decide what software to build.

Agentic coding loop: Given a product specification and optionally a set of evals (that is, a dataset against which to measure performance), we can have an AI agent write code, test its work, and keep iterating until the code is bug-free and meets its specification. This idea of closing the loop took off around the end of last year, and it has been a game changer in enabling coding agents to work longer productively without human intervention. For example, over the weekend, I was building an app for my daughter to practice typing, and my coding agent could easily work for around an hour, using a web browser to check what it had built multiple times before getting back to me, without needing my intervention.

The engineering loop executes quickly. Every few minutes, the coding agent might build and test a new version of the software. I hear frequently from developers who are finding new ways to engineer more effective engineering loops. This is an active area of invention!

Developer feedback loop: In this loop, a developer examines the current product and steers the coding agent to improve it. Last year, a lot of developers (including me) were acting as the QA (quality assurance) function for our coding agents, manually finding bugs and then asking the agent to fix them. But with coding agents much more able to test their own code, the amount of time we need to spend on this function has decreased significantly. This allows us to make higher-level product decisions, such as what key features to offer, where the UI needs improvement, and so on.

The developer-feedback loop operates over time intervals between tens of minutes and hours — that's how frequently a developer might review a product and give feedback. In the case of the typing app, I changed my mind a few times about the visual design, what cat costumes she can unlock as she learns (she loves cats), and the user flow for a grown-up to log in and steer the child's learning experience.

When a developer has a clear vision for what to build, it is still a lot of work to translate that vision into a specification for a coding agent to implement. Further, after the developer has seen an implementation, they might update (or perhaps clarify) the spec to steer it toward what they want. If you find that the system repeatedly runs into certain problems, building a set of evals for the agent becomes useful.

AI-native teams are increasingly using AI to help shape product direction, for example, automating the gathering and analysis of usage data, summarizing written and verbal customer feedback, or carrying out competitive analysis. However, for pretty much all the products I’m involved in, I see humans as having a significant context advantage over current AI systems — we know a lot more than the AI system about the users and the context the product has to operate in — and thus humans play a critical role. Many people describe this human contribution as “taste,” but I prefer to think of it as humans having a context advantage, since that gives us a clearer path to helping AI systems get better. This also speaks to why this step can’t be automated: So long as the human knows something the AI does not, human-in-the-loop is needed to to inject that knowledge into the system.

External feedback loop: This includes a wide range of tactics like asking a few friends for feedback, launching to alpha testers, or putting the code into production with A/B testing. These tactics are usually slow, rarely taking less than hours and sometimes taking days or even weeks. This data informs the developer vision, which in turn continues to drive the detailed product spec, which in turn drives the coding agent.

With coding agents speeding up software development, more engineers are starting to play a partial product management role. For many engineers who are growing into this role, the hardest part is shaping the product vision and striking a balance between building (bridging the gap between vision and spec) and getting user feedback to evolve the vision. It is important to do both!

I will write more about how to do this in future posts, but for now, I find it encouraging that engineers are playing an expanded role (just as product managers and designers now do more engineering).

[Original text: The Batch]

> 媒体：
> - https://pbs.twimg.com/media/HMEtxp3bsAARJdi.jpg

## 溯源

- 核心主张：用 AI 做 0 到 1 的产品，靠三个时间尺度不同、层层嵌套的反馈循环推动：agent 写代码自测（分钟级）、开发者看产品后改 spec 引导（小时级）、外部用户反馈修正产品愿景（天到周级）；只要人掌握 AI 不知道的用户和场景信息，人就必须留在环里。
- 源知识：
  - [人在环中](../roots/human-in-the-loop.md) · 关系：直接源自 · 强弱：强。原文明确使用 human-in-the-loop 一词，并论证只要人知道 AI 不知道的东西，就需要人在环里注入这些知识。
  - [控制论](../roots/cybernetics.md) · 关系：相近 · 强弱：弱（模型复核通过）。三个 loop 都是“输出回到输入、据此调整”的闭环反馈，“loop engineering”本质是给反馈控制换了个新名字；作者没有提控制论，是推断。
  - [测试驱动开发](../roots/test-driven-development.md) · 关系：相近 · 强弱：弱（模型复核通过）。给定 spec 和 evals，让 agent 写代码、跑测试、迭代到通过为止，和 TDD“先写会失败的测试、再写到通过”的循环很像；作者未提 TDD。
  - [精益创业](../roots/lean-startup.md) · 关系：相近 · 强弱：弱（模型复核通过）。外部反馈循环（找朋友试用、alpha 测试、A/B 测试 → 修正愿景 → 改 spec）和精益创业的“构建-测量-学习”循环几乎同构；作者未引用。
  - [《知识在社会中的运用》](../roots/the-use-of-knowledge-in-society.md) · 关系：相近 · 强弱：弱（模型复核通过）。作者说人的作用是“上下文优势”（比 AI 更了解用户和场景），这和哈耶克说的“具体时间地点的知识分散在个人手里、无法集中”很像；作者未引用。
- 本质：这条新知识本质上是“闭环反馈控制 + 人在环中”在 AI 编程时代产品开发流程上的应用：按时间尺度把反馈分层，快的循环交给机器，需要上下文的循环由人把机器缺的信息注入进去。
- 整理于：2026-10-18（第 1 轮）
