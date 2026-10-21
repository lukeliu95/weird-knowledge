---
title: "ADK 开发者该懂的五种 Agent Skill 设计模式"
author: "Google Cloud Tech (@GoogleCloudTech)"
url: https://x.com/GoogleCloudTech/status/2033953579824758855
source: X Article
published: 2026-03-17 17:08 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [anthropic-2025-agent-skills, software-design-pattern, progressive-disclosure, anthropic-2024-building-effective-agents, separation-of-concerns, fagan-inspection, requirements-elicitation, phase-gate-model]
---

## 原文

# 5 Agent Skill design patterns every ADK developer should know

When it comes to 𝚂𝙺𝙸𝙻𝙻.𝚖𝚍, developers tend to fixate on the format—getting the YAML right, structuring directories, and following the spec. But with more than 30 agent tools (like Claude Code, Gemini CLI, and Cursor) standardizing on the same layout, the formatting problem is practically obsolete.

The challenge now is content design. The specification explains how to package a skill, but offers zero guidance on how to structure the logic inside it. For example, a skill that wraps FastAPI conventions operates completely differently from a four-step documentation pipeline, even though their 𝚂𝙺𝙸𝙻𝙻.𝚖𝚍 files look identical on the outside.

By studying how skills are built across the ecosystem—from Anthropic’s repositories to Vercel and Google's internal guidelines— there are five recurring design patterns that can help developers build agents.

By @Saboo_Shubham_ and @lavinigam

This article covers each one with working ADK code:

- Tool Wrapper: Make your agent an instant expert on any library

- Generator: Produce structured documents from a reusable template

- Reviewer: Score code against a checklist by severity

- Inversion: The agent interviews you before acting

- Pipeline: Enforce a strict multi-step workflow with checkpoints

![Image](https://pbs.twimg.com/media/HDoDgs6XAAYtw04.jpg)

## Pattern 1: The Tool Wrapper

A Tool Wrapper gives your agent on-demand context for a specific library. Instead of hardcoding API conventions into your system prompt, you package them into a skill. Your agent only loads this context when it actually works with that technology.

![Image](https://pbs.twimg.com/media/HDoDoIeXAAUmQoy.jpg)

It is the simplest pattern to implement. The 𝚂𝙺𝙸𝙻𝙻.𝚖𝚍 file listens for specific library keywords in the user's prompt, dynamically loads your internal documentation from the  𝚛𝚎𝚏𝚎𝚛𝚎𝚗𝚌𝚎𝚜/ directory, and applies those rules as absolute truth. This is the exact mechanism you use to distribute your team's internal coding guidelines or specific framework best practices directly into your developers' workflows.

Here is an example of a Tool Wrapper that teaches an agent how to write FastAPI code. Notice how the instructions explicitly tell the agent to load the 𝚌𝚘𝚗𝚟𝚎𝚗𝚝𝚒𝚘𝚗𝚜.𝚖𝚍 file only when it starts reviewing or writing code:

## Pattern 2: The Generator

While the Tool Wrapper applies knowledge, the Generator enforces consistent output. If you struggle with an agent generating different document structures on every run, the Generator solves this by orchestrating a fill-in-the-blank process.

![Image](https://pbs.twimg.com/media/HDoEJdZbEAEdYMo.jpg)

It leverages two optional directories: 𝚊𝚜𝚜𝚎𝚝𝚜/ holds your output template, and 𝚛𝚎𝚏𝚎𝚛𝚎𝚗𝚌𝚎𝚜/ holds your style guide. The instructions act as a project manager. They tell the agent to load the template, read the style guide, ask the user for missing variables, and populate the document. This is practical for generating predictable API documentation, standardizing commit messages, or scaffolding project architectures.

In this technical report generator example, the skill file does not contain the actual layout or the grammar rules. It simply coordinates the retrieval of those assets and forces the agent to execute them step by step:

## Pattern 3: The Reviewer

The Reviewer pattern separates what to check from how to check it. Rather than writing a long system prompt detailing every code smell, you store a modular rubric inside a 𝚛𝚎𝚏𝚎𝚛𝚎𝚗𝚌𝚎𝚜/𝚛𝚎𝚟𝚒𝚎𝚠-𝚌𝚑𝚎𝚌𝚔𝚕𝚒𝚜𝚝.𝚖𝚍 file.

![Image](https://pbs.twimg.com/media/HDoEa51XEAIKSnO.jpg)

When a user submits code, the agent loads this checklist and methodically scores the submission, grouping its findings by severity. If you swap out a Python style checklist for an OWASP security checklist, you get a completely different, specialized audit using the exact same skill infrastructure. It is a highly effective way to automate PR reviews or catch vulnerabilities before a human looks at the code.

The following code reviewer skill demonstrates this separation. The instructions remain static, but the agent dynamically loads the specific review criteria from an external checklist and forces a structured, severity-based output:

## Pattern 4: Inversion

Agents inherently want to guess and generate immediately. The Inversion pattern flips this dynamic. Instead of the user driving the prompt and the agent executing, the agent acts as an interviewer.

![Image](https://pbs.twimg.com/media/HDoEo5XbEAUaaFG.jpg)

Inversion relies on explicit, non-negotiable gating instructions (like "DO NOT start building until all phases are complete") to force the agent to gather context first. It asks structured questions sequentially and waits for your answers before moving to the next phase. The agent refuses to synthesize a final output until it has a complete picture of your requirements and deployment constraints.

To see this in action, look at this project planner skill. The crucial element here is the strict phasing and the explicit gatekeeping prompt that stops the agent from synthesizing the final plan until all user answers are collected:

## Pattern 5: The Pipeline

For complex tasks, you cannot afford skipped steps or ignored instructions. The Pipeline pattern enforces a strict, sequential workflow with hard checkpoints.

The instructions themselves serve as the workflow definition. By implementing explicit diamond gate conditions (such as requiring user approval before moving from docstring generation to final assembly), the Pipeline ensures an agent cannot bypass a complex task and present an unvalidated final result.

![Image](https://pbs.twimg.com/media/HDoE195bEAABitY.jpg)

This pattern utilizes all optional directories, pulling in different reference files and templates only at the specific step where they are needed, keeping the context window clean.

In this documentation pipeline example, notice the explicit gate conditions. The agent is explicitly forbidden from moving to the assembly phase until the user confirms the generated docstrings in the previous step:

## Choosing the right agent skill pattern

Each pattern answers a different question. Use this decision tree to find the right one for your use-case:

![Image](https://pbs.twimg.com/media/HDoFWovXAAsbb8C.jpg)

## And finally, patterns compose

These patterns are not mutually exclusive. They compose.

A Pipeline skill can include a Reviewer step at the end to double-check its own work. A Generator can rely on Inversion at the very beginning to gather the necessary variables before filling out its template. Thanks to ADK's 𝚂𝚔𝚒𝚕𝚕𝚃𝚘𝚘𝚕𝚜𝚎𝚝 and progressive disclosure, your agent only spends context tokens on the exact patterns it needs at runtime.

Stop trying to cram complex and fragile instructions into a single system prompt. Break your workflows down, apply the right structural pattern, and build reliable agents.

## Get started today

The Agent Skills specification is open-source and natively supported across ADK. You already know how to package the format. Now you know how to design the content. Go build smarter agents with Google Agent Development Kit.

## 溯源

- 核心主张：SKILL.md 的格式已经统一，真正的难点是技能里面的内容怎么设计；常见五种模式：工具包装（用到某个库时才加载它的规范）、生成器（模板加风格指南填空）、评审者（检查清单和检查流程分开，按严重程度出结果）、反转（智能体先采访用户，问齐了才动手）、流水线（多步流程加硬性检查点）；这些模式可以互相组合，配合渐进式披露只在需要时占用上下文。
- 源知识：
  - [用 Agent Skills 让智能体胜任真实工作](../roots/anthropic-2025-agent-skills.md) · 关系：直接源自 · 强弱：强。文章讨论的就是 Anthropic 提出、后来成为开放标准的 Agent Skills（SKILL.md 加 references/、assets/ 目录），并明说研究了 Anthropic 的技能仓库。
  - [软件设计模式](../roots/software-design-pattern.md) · 关系：直接源自 · 强弱：强。标题就叫“design patterns”，按“每种模式回答一类问题、模式之间可以组合”的方式来写，沿用了软件设计模式的说法和写法。
  - [渐进式披露](../roots/progressive-disclosure.md) · 关系：直接源自 · 强弱：强。原文明说靠 ADK 的 SkillToolset 和“progressive disclosure”，让智能体只为运行时真正需要的模式花上下文。
  - [构建高效的智能体](../roots/anthropic-2024-building-effective-agents.md) · 关系：相近 · 强弱：弱（模型复核通过）。流水线模式“步骤之间设关口”和评审者模式，对应 Anthropic《构建高效的智能体》里带关口检查的提示链和评估-优化循环；文章没有引用这篇。
  - [关注点分离](../roots/separation-of-concerns.md) · 关系：相近 · 强弱：弱（模型复核通过）。评审者模式“把查什么和怎么查分开”，生成器把模板和风格指南放进外部文件，换一份清单就变成另一种审查，是关注点分离。
  - [Fagan 审查（正式代码审查）](../roots/fagan-inspection.md) · 关系：相近 · 强弱：弱（模型复核通过）。评审者模式对照外部清单逐项检查、按严重程度分组输出，和 Fagan 审查对照标准逐项查缺陷、按主要和次要分级的做法相近。
  - [需求获取（需求诱导）](../roots/requirements-elicitation.md) · 关系：相近 · 强弱：弱（模型复核通过）。反转模式让智能体按阶段提结构化问题，问齐需求和部署约束才动手，是需求获取（访谈式收集需求）的做法。
  - [阶段-关口模型（Stage-Gate）](../roots/phase-gate-model.md) · 关系：相近 · 强弱：弱（模型复核通过）。流水线模式在步骤之间设“菱形关口”，用户确认前不许进入下一阶段，和阶段-关口模型“过了关口才能进下一阶段”的结构一样。
- 本质：这条新知识本质上是软件设计模式的思路（给反复出现的问题起名字、给出可复用的解法），加上关注点分离和渐进式披露，在编写智能体技能文件场景下的应用。
- 整理于：2026-10-18（第 2 轮）
