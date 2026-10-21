---
title: Claude 5 代模型的上下文工程新规矩：系统提示删掉八成，少写规则和例子，按需加载
author: Thariq Shihipar（Anthropic）
url: https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/
source: 网页（claude.dev 博客，Anthropic 官方）
published: 2026-07-24
saved: 2026-10-21
why: 探索日报：Luke 想看
related_principles: [原则 2, 原则 11, 原则 1]
status: 已整理
kind: 观点
topic: 编程智能体
roots: [anthropic-2025-effective-context-engineering, progressive-disclosure, kaplow-1992-rules-versus-standards, affordance, brown-2020-few-shot-learners]
---

## 原文

# The new rules of context engineering for Claude 5 generation models

We removed over 80% of Claude Code's system prompt for more advanced models. How to apply the lessons we learned to your own context engineering in Claude Code and with your own agents.

I’ve written previously about how to best [prompt the newest generation of Claude 5 models](https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns) and work with them iteratively to discover what you want to build.

But when you send a message to Claude, the prompt is only a small part of the context it gets. Much of your context is assembled from your system prompt, Skills, CLAUDE.md files, memory, and other sources. We call this [context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), and it makes a big impact on the results you generate when using Claude Code or in building your own agents.

Unlike a prompt, context is used generally across many requests, so it cannot be as specific. How do you build these general prompts and guidance for Claude, especially when you don’t know what a user’s prompt might be?

This can be surprisingly difficult as Claude’s own capabilities evolve. Most recently, we noticed a large jump in the way we prompt the newest generation of Claude models. We removed over 80% of Claude Code’s system prompt for models like Claude Opus 5 and Claude Fable 5 with no measurable loss on our coding evaluations.

Here’s what we’ve learned about prompting this new class of models, and how you can utilize it to update your context engineering. We’ve put these best practices in `claude doctor`; use the command `/doctor` in Claude Code to rightsize your skills, and CLAUDE.md files.

## UNHOBBLING CLAUDE

Overall, we found that we were overconstraining Claude Code, both through our system prompt and in our CLAUDE.md files and skills.

For example, when we read transcripts of our own internal usage of Claude Code, we see several conflicting messages in a single request like “leave documentation as appropriate,” or “DO NOT add comments” as our system prompt, skills, and user requests clash with each other.

![One assembled context holding a system prompt line “leave documentation as appropriate”, a skill line “do not add comments”, and a user request “just make it work like the old one”.](https://claude.dev/media/a0c1f3923f1e92004785e35257d3feed5081264767d0a99fa5eb397e2fb6f2e2.png)

Generally, Claude can interpret the user’s intent to get to the right answer, but Claude must think more carefully about these overlapping and conflicting messages before deciding what to do.

And while these constraints were once needed to avoid worst case scenarios, we have since found we can delete many of them and let the model use surrounding context and judgement instead.

Additionally, Claude Code now has many more tools. Claude used to rely on CLAUDE.md as a source of memory, information, and guidance. Now we have memory, artifacts, and skills, which Claude can use to create new ways of loading and sharing context across sessions.

## THEN AND NOW

There were a number of previous context engineering best practices that had become myths. Including:

![Six old rules struck through, each pointing to its replacement: give Claude rules → give Claude judgement; give Claude examples → design interfaces; put it all upfront → use progressive disclosure; repeat yourself → simple tool descriptions; memory in CLAUDE.md files → auto-memory; simple specs → rich references.](https://claude.dev/media/aaa82d5934e084f1e509ac1679c26d0d2338d6c995c1c2f349fc12b8a0fd1a9c.png)

### Then: Give Claude rules

### Now: Let Claude use judgement

When we first rolled out Claude Code, we needed to be sure that Claude avoided worst case scenarios, such as deleting files. This meant we would give particularly strong guidance that might not always be true. For example, in the system prompt we used to say:

*In code: default to writing no comments. Never write multi-paragraph docstrings or multi-line comment blocks — one short line max. Don't create planning, decision, or analysis documents unless the user asks for them — work from conversation context, not intermediate files.*

But for a certain subset of prompts, this guidance would be wrong. In the case of documentation, the user may have their own preferences, or specific parts of very complex code might need multi-line comment blocks.

Still, without these guardrails for older models, the comments Claude wrote would be incorrect in many cases and we had to accept this tradeoff. But newer models have better judgement and can handle these decisions well without explicit rules.

In the new system prompt we say: *Write code that reads like the surrounding code: match its comment density, naming, and idiom.*

### Then: Give Claude examples

### Now: Design interfaces

The number one rule for tool usage was to give Claude examples on how to use them. With our newest models, we’ve found that giving examples actually constrains them to a certain exploration space.

![Before: a TodoWrite tool description of about 9,100 characters of when-to-use lists and worked examples. After: a short description, “Create and update a task list for the current session”, with a status enum of pending, in_progress and completed and one rule, only one task in_progress at a time.](https://claude.dev/media/8bb6f9365532bb8b19443ad00f230444087a452f776232d05045f1c6c63c3de8.png)

Instead of using examples, think more about the design of your tools, scripts and files- what parameters does Claude have and how can they be more expressive?

For example, in the Todo tool example, just listing status as an enumeration between pending, in_progress, and completed, hints to Claude about how to use it. The instruction on keeping one item in_progress helps define our requested behavior.

### Then: Put it all upfront

### Now: Use progressive disclosure

Because Claude Code was focused on coding, our system prompt included detailed information on how to do code review and verification. These were not always needed, but when they were, it was crucial information.

Since then, Claude Code has gotten very competent at using progressive disclosure- loading the right context at the right times. For example, we moved verification and code review into their own skills that Claude Code could selectively call.

But progressive disclosure is not just for skills, we also use it for tools. Some of our tools are ‘deferred loading,’ which means the agent must search for their full definitions using ToolSearch before using them. This allows us to have more tools (such as our Task tools) that don’t take up context until they’re needed.

The same can be applied to your own CLAUDE.md and Skill.md files. A common myth is that you want to make these a central repository for every known practice that you *might* run into, because Claude would not find it otherwise. Instead, [consider having a tree of files that can be loaded at the right time](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code).

### Then: Repeat yourself

### Now: Simple tool descriptions

Earlier Claude models could sometimes need repeated instructions or be more likely to listen to instructions at the end of their context window than at the start. This meant our system prompt would sometimes have references to tools in the main system prompt as well as instructions in the tool description.

We found we could delete these repeat examples and put instructions on how to use tools in the tool descriptions rather than the system prompt.

### Then: Memory in CLAUDE.md files

### Now: Auto-memory

We used to encourage users to save things to Claude’s memory, by using the # hotkey to write to their `CLAUDE.md` automatically. Instead, Claude now automatically saves memories that are relevant to the work and to you.

### Then: Simple specs

### Now: Rich references

In plan mode, Claude Code has heavily relied on markdown files with plans. Storing these files as plans helped Claude refer to them when needed. Another similar best practice was to store specs in the codebase for Claude to refer to while working across longer projects.

But we’ve found that Claude can handle increasingly more complicated references. Instead of simple markdown files, Claude can reference HTML artifacts created by our new artifacts feature.

You may also give Claude references in the form of code. A spec may also be a detailed test suite, or a function in a different codebase that Claude might port.

Rubrics are another form of references. Rubrics allow Claude to try and verify your taste in a particular field (e.g. what does a good API design look like) by using [dynamic workflows](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code) and spinning up verifier agents with those rubrics.

## APPLYING THIS TO YOUR CONTEXT

Pulling this all together, what does this look like when you assemble your context?

![The context window drawn as a stack: your prompt on top, then references such as @-mentioned files, specs, mockups, codebases and artifacts, then the system prompt, CLAUDE.md files, skills and memory.](https://claude.dev/media/6c6b396594b664244e31fe5ba0c37619accc4777be823e699906c7a641dfcc60.png)

### System prompt

A system prompt is heavily tied to the product context. It tells Claude what product it’s operating in and what it’s doing. For Claude Code, you will likely never modify this, but if you are building your own agent harness, this is where you should spend a lot of time.

### CLAUDE.md

Keep your CLAUDE.md lightweight and briefly describe what your repo is for, but spend most of the tokens on gotchas inside of the codebase. For example, you may organize your code to keep types in one monolithic file and nowhere else. Avoid stating ‘the obvious’ things Claude should know by looking at your file system or your repo.

Use progressive disclosure heavily, for example if you have several unique instructions on how to verify your work, create a verification skill and reference it from your CLAUDE.md.

### Skills

Think of skills as lightweight guides to let Claude find information when needed. Avoid making them overconstrained, except in highly important areas.

For long skills, try and use progressive disclosure as much as possible- divide it into many files and split them out.

It’s best when skills encode particular opinions, knowledge, or best practices that are particular to you, your team, or product.

### References

You can @ mention files to include them as references. References allow Claude to refer to in-depth information about the current plan.

This might be in specs files, mockups, or even entire codebases. Generally you should prefer files that are in code as it provides clear, high-fidelity instructions to Claude in a language it knows very well. For example, a HTML mockup of a design will generally produce better results than a description of the design or a screenshot.

## TRY SIMPLIFYING

Across your system prompt, skills, and CLAUDE.md files, you may need to simplify just like we did. We rolled out a new command called `claude doctor`, which will help you do this automatically as well. For more details on prompting more advanced models specifically, check out our [Fable field guide](https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns).

*This article was written by Thariq Shihipar, member of technical staff, Anthropic.*

## 溯源

- 核心主张：模型变强以后，上下文要做减法：少写硬规则、少给例子、不把所有东西一次塞进去，改为让模型自己判断、把工具和参数设计得一看就会用、需要时再加载细节；Claude Code 因此删掉了八成系统提示，编程评测没有下降。
- 源知识：
  - [AI 智能体的上下文工程](../roots/anthropic-2025-effective-context-engineering.md) · 关系：直接源自 · 强弱：强。作者在文中直接链接这篇，把它当作“上下文工程”的定义；本文是它在 Claude 5 代模型上的更新版
  - [渐进式披露](../roots/progressive-disclosure.md) · 关系：直接源自 · 强弱：强。作者明说用渐进式披露：审代码、验证拆成技能，工具延迟加载，CLAUDE.md 只留入口
  - [规则与标准：经济分析](../roots/kaplow-1992-rules-versus-standards.md) · 关系：相近 · 强弱：弱（模型复核通过）。从“给规则”换成“给判断”，就是法经济学里规则和标准的取舍：执行方判断能力变强、情况变多时，标准比事先写死的规则更划算（模型推断，待 Luke 确认）
  - [可供性（示能）](../roots/affordance.md) · 关系：相近 · 强弱：弱（模型复核通过）。“与其给例子，不如设计界面”：状态枚举本身就提示了工具该怎么用，正是让对象自己显示用法的可供性思路（模型推断，待 Luke 确认）
  - [语言模型是少样本学习者（GPT-3 论文）](../roots/brown-2020-few-shot-learners.md) · 关系：挑战 · 强弱：弱（模型复核通过）。少样本示例曾是提示的头号做法；作者发现对新模型给例子反而把它限制在例子圈出的范围里（模型推断，待 Luke 确认）
- 本质：这条新知识本质上是“规则与标准之争”和渐进式披露在大模型上下文设计里的应用：执行者（模型）判断力变强后，用少量目标加好用的界面、按需加载，替代事先写死的规则和例子。
- 整理于：2026-10-21（第 5 轮）
