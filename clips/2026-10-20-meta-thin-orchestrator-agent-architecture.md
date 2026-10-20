---
title: Meta 的瘦编排器模式：编排器只管路由和检查，不做领域推理，14 个专项子 agent 各管一块
author: Plawan Rath, Akhil Jindal, Ashwini Verma（Meta Engineering）
url: https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent-architecture/
source: 网页
published: 2026-10-19
saved: 2026-10-20
why: 探索日报：Luke 想看
related_principles: ["原则 11", "原则 2", "原则 6"]
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [separation-of-concerns, klang-2025-orchestrated-multi-agents, anthropic-2024-building-effective-agents, martin-2025-context-engineering-agents, yan-2025-dont-build-multi-agents, unix-philosophy]
---

## 原文

By Plawan Rath, Akhil Jindal, Ashwini Verma

- Sometimes, giving an AI agent all of the knowledge it needs is the wrong approach. 

- At Meta, we’ve seen notable improvements in efficiency and accuracy by keeping the orchestration layer of our data pipeline agents deliberately thin: It routes work and enforces reliability checks, while specialized agents do the domain reasoning.

- We’re sharing our own process and insights, plus how any team can apply this to their production AI agents.

We built a 1,300-line orchestrator that routes 20+ workflows to 14 specialized AI agents. It performs zero domain work itself. That’s the point.

When we first deployed AI agents to automate data column onboarding across Meta’s recommendation systems — a process spanning three code repositories, three programming languages, and up to six pipeline stages that must stay in sync — we did what most teams do: We built one smart agent that knew everything.

It worked in demos. In production, it started hallucinating.

The fix wasn’t better prompts or a bigger context window. It was giving the central agent less to do. We call this the thin orchestrator pattern: a router that owns sequencing and reliability checks, and leaves every domain decision to specialists.

## The Problem: More Context, Worse Results

Our pipeline is config-as-code: Python configurations drive C++ code generation, which feeds data processing services, which populate analytics systems. Onboarding a single data column requires coordinated changes across configuration registries, backend services, and data pipelines, and each column moves through up to six stages before its data arrives.

Our first approach was a single AI agent loaded with all domain knowledge, configuration schemas, code generation rules, pipeline routing logic, validation requirements, and population patterns for 10+ data sources. 

The agent had everything it needed. That was the problem.

Past a certain context threshold, additional knowledge degraded rather than improved performance. The agent would cross-contaminate concepts, applying field naming conventions from one subsystem to another, or using a code generation pattern meant for one data source when populating from a different one. A preprint from the Windreich Department of Artificial Intelligence and Human Health at Mount Sinai found that orchestrated multiagent systems held 65.3% accuracy at 80-task batches where single agents fell to 16.6%, while reducing token usage up to 65-fold. The authors attribute this to the design’s isolation of tasks, which prevented context interference. We were experiencing the inverse, a single agent drowning in its own knowledge.

We also evaluated an alternative single-agent approach. Its success rate was 70-80% with manual prompt engineering per task: An engineer had to craft a custom system prompt for each specific job. Without that handholding, success dropped to 10-20%. This wasn’t a prompt engineering problem. It was an architectural one.

## The Approach: A Thin Router With Specialist Workers

We split the system into two layers:

- A deterministic orchestrator that performs zero domain work. It classifies intent, gathers required fields, runs reliability checks, and delegates to the right specialist. It never reasons about code, never generates configurations, and never touches the codebase. It’s a router.

- Fourteen specialized subagents, each a complete domain expert with isolated context. A schema management agent knows configuration registries. A population agent knows how to generate code for each of 10 data sources. A validation agent knows build systems and quality checks. No agent sees the full picture. That’s the feature, not the bug.

The orchestrator follows a fixed 7-step protocol for every request:

- Read the relevant subagent’s instruction file.

- Check if the target already exists (prevent duplicates).

- Gather required fields from the user.

- Auto-discover what can be inferred (repository type, existing configurations).

- Reliability gate check for active warnings or required reviewers.

- Delegate to the subagent with full context.

- Handle results and surface errors, confirm success.

Steps 1–5 and 7 are deterministic. Only step 6 involves large language model (LLM) reasoning, and it happens inside an isolated subagent with only its domain knowledge loaded.

## What We Built: Workflow Templates, Not New Agents

One architectural insight was separating what needs to happen from how each step is performed. The orchestrator defines phase ordering through workflow templates — deterministic state machines that constrain the LLM’s decision space:

- Column Onboarding: Schema → Validation → Population → Testing

- Event Onboarding: Schema → Population → Validation → Testing → Event Processing

- Pipeline Migration: Assessment → Planning → Population → Validation → Monitoring

Each workflow template reuses the same pool of 14 subagents in different sequences. When we needed to support pipeline migration, a completely new use case, we didn’t build new agents. We wrote a new workflow template that sequenced existing agents differently. Zero new agent code. Full production capability.

Each subagent follows a standardized structure:

- Knowledge sources: which domain files to load at runtime (typically a few thousand tokens each).

- Pre-gathering checklist: what the orchestrator must collect before delegation.

- Step-by-step workflow: the domain-specific execution plan.

- Discovery patterns: how to find relevant code patterns in the monorepo.

- Troubleshooting: error-to-resolution mappings for common failures.

This uniformity means adding a new subagent is templated work, not greenfield engineering. The 15th subagent looks structurally identical to the first.

Knowledge files are loaded on demand at subagent execution time, not embedded in the orchestrator. We maintain 25+ knowledge files organized by workflow domain. When a knowledge file is updated, the next session automatically uses the latest version — no orchestrator changes required. The same knowledge files serve multiple platform implementations of our agent.

## Results

Configuration prep for a new column took three to four days by hand and about a day with our earlier config-driven system. The thin orchestrator system does it in under an hour.

For broader context: About two-thirds of the system’s changes land without significant human edits. It gets there by trading generality for deep domain knowledge, a deliberate architectural choice. The orchestrator is general; the subagents are specialists.

## Why This Works (And Why Heavyweight Orchestrators Don’t)

The conventional approach is to make the orchestrator the smartest component — give it all the context and let it reason about what to do and how to do it. This works until it doesn’t, and it stops working exactly when you need it most — at scale, with complex multi-step workflows, across heterogeneous subsystems.

The thin orchestrator works because it aligns architectural boundaries with computational boundaries:

- Deterministic decisions stay deterministic. “Which subagent handles this?” is a routing decision, not a reasoning task. Don’t use an LLM for it.

- Context isolation prevents cross-contamination. The population agent for data source A never sees data source B’s patterns. It can’t hallucinate the wrong one.

- Failures are contained. If a subagent fails, the orchestrator retries or escalates. The failure doesn’t corrupt the orchestrator’s state or other subagents’ contexts.

- The system improves at every layer independently. A better model improves all 14 subagents simultaneously. A knowledge file update takes effect immediately. A new workflow template unlocks new capabilities without touching agents. No single component carries the full weight.

## How to Apply This to Your AI Agents

This pattern isn’t specific to data pipelines. Any team building production AI agents can benefit:

-  Separate routing from reasoning. If your orchestrator is making domain decisions, it’s doing too much. Routing should be deterministic: keyword matching, intent classification, field gathering. Push all domain reasoning into isolated subagents.

-  Design subagents as structurally uniform specialists. Every subagent should have the same structure: knowledge sources, required inputs, execution steps, error handling. This makes adding new capabilities templated work rather than architecture changes.

-  Use workflow templates, not new agents, to scale. When you need a new use case, first ask: Can I sequence existing agents differently? If you can’t reuse agents across workflows, your agents are too coupled to specific use cases.

-  Load knowledge at runtime, not at build time. Embed knowledge in the orchestrator and every update requires redeployment. Load it on demand and updates take effect immediately, across all platforms.

-  Draw the deterministic/probabilistic boundary explicitly. For every component, decide: Is this a routing decision (deterministic) or a reasoning task (probabilistic)? The orchestrator should be on one side, the subagents on the other. Don’t mix them.

The strongest argument for a thin orchestrator is the failure mode of the alternative. When a heavyweight orchestrator hallucinates, the error spreads to everything downstream: it routes to the wrong agent, gathers the wrong fields, or skips reliability checks. A thin orchestrator leaves little room for hallucination because its routing and reliability steps don’t rely on LLM reasoning. It follows a fixed protocol. The creativity happens downstream, in isolated, domain-scoped contexts where hallucination risk is minimized and failures are contained.

## What’s Next

We’re scaling this architecture to handle an increase in data columns across new pipeline domains. The compositional thesis predicts this will work because scaling means adding workflow templates and knowledge files, not rebuilding agents. We’re also exploring how the system can continuously improve from production usage, using automated feedback loops to identify failure patterns and propose targeted improvements to subagent knowledge, with human review always gating any changes.

The counterintuitive lesson: the most important component in our AI agent system is the one that does the least work. Keep your orchestrator thin and your specialists deep, and the whole system becomes more reliable.

## Acknowledgements

This work was a team effort. Some other people who contributed to this effort include:  Mani Bhushan, Rahul Maliakkal, Jae Ha, Chakrapani Kumar, Vivek Tiwari, and Amanda Yin.

## 溯源

- 核心主张：生产环境里，一个装满全部领域知识的大 agent 会串味、出幻觉；更可靠的做法是让编排器只做确定性的路由、收集字段和可靠性检查，不做任何领域推理，把每处领域判断交给上下文互相隔离、按需加载知识文件的专项子 agent，新用途靠新的流程模板重新编排已有子 agent。
- 源知识：
  - [关注点分离](../roots/separation-of-concerns.md) · 关系：换了说法 · 强弱：弱（待 Luke 确认）。“把路由和推理分开”“把确定和不确定的边界画清楚、不要混”就是关注点分离换到 agent 系统上的说法；文章没提这个词。
  - [临床规模负载下，编排式多 agent 比单 agent 更能保住准确率](../roots/klang-2025-orchestrated-multi-agents.md) · 关系：直接源自 · 强弱：强。文章明引西奈山医院这项研究当证据：80 个任务一批时，编排式多 agent 准确率 65.3%，单 agent 跌到 16.6%，token 最多省 65 倍，作者归因于任务隔离避免了上下文互相干扰。
  - [构建高效的智能体](../roots/anthropic-2024-building-effective-agents.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。Anthropic 区分“工作流”（代码预设路径）和“智能体”（模型自己决定），并列出路由、编排-工人等模式；Meta 的“确定的编排器 + 只在第 6 步用模型推理的子 agent”就是这两种的组合。文章没引。
  - [智能体的上下文工程（写入、选取、压缩、隔离）](../roots/martin-2025-context-engineering-agents.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。上下文工程四类做法里的“隔离”（把上下文拆给子 agent）和“选取”（需要时再把知识拉进窗口）正是 Meta 的上下文隔离和知识文件按需加载。文章没引。
  - [别做多智能体](../roots/yan-2025-dont-build-multi-agents.md) · 关系：挑战 · 强弱：弱（待 Luke 确认）。Cognition 的《别做多智能体》主张子 agent 必须共享完整上下文、否则决策互相冲突；Meta 反过来说“没有哪个 agent 看到全貌，这是特性不是缺陷”，隔离反而防止串味。两者可以部分调和：Meta 靠确定性流程模板串行编排，避开了并行子 agent 各自拍板的冲突。
  - [Unix 哲学](../roots/unix-philosophy.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。每个子 agent 只做好一件事、结构统一，新需求靠流程模板把现成子 agent 按新顺序串起来，像用管道组合小工具；文章没提。
- 本质：这条新知识本质上是关注点分离和模块化（Unix 哲学）在多 agent 系统上的应用：确定的事交给确定的代码，需要判断的事各自隔离上下文，避免无关信息互相干扰。
- 整理于：2026-10-21（第 4 轮）
