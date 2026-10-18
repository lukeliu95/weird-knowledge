---
title: "Manus 把工具分成三层的设计"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/1979041449892004117
source: X
published: 2025-10-17 04:27 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [ji-2025-manus-layered-action-space, unix-philosophy, wang-2024-executable-code-actions, progressive-disclosure, anthropic-2025-effective-context-engineering]
---

## 原文

确实，Manus 很聪明，他们把工具分成了 3 层：

第 1 层：函数调用 (Function Calling)

这是最基础的一层，只保留一小组固定的、原子化的函数，比如：读写文件、执行 Shell 命令、搜索文件等。在 LLM 的系统提示词中就只有这一层的工具定义，相对比较少，15 个以内，输入格式和输出格式都很清晰，不容易出错，但这里面有两个工具很特殊，一个是 Shell， 一个是 File。

第 2 层：沙箱工具 (Sandbox Utilities)

每个 Manus 会话都运行在一个完整的虚拟机沙箱里。就是原推文提到的，虚机预装了很多命令行工具，比如格式转换器、语音识别工具，甚至一个 mcp 命令行客户端。

然后这些工具都通过第 1 层中定义的 Shell 来调用，就是命令行工具，命令行调用。

但是这么多工具模型怎么知道呢？

Manus 在系统提示词里会直接告诉 LLM，在一个特定的文件夹里有很多预装的命令行工具。对于最常用的工具，直接列出它们的名字。不常用的，LLM 可以直接通过原推提到的命令列出所有命令行工具，通过 --help 参数来查看任何一个工具的用法，因为所有这些工具都是他们自己开发的，格式统一。

第 3 层：代码包与 API (Packages and APIs)

这一层其实就是 LLM 实时编写 Python 代码，通过代码实现更复杂的功能。比如用户想查询某个 API 的数据，可以直接用 Python 写一个函数，fetch API 的数据，并解析成需要的格式。

其实在 Codex 中，用 Python 代码当工具已经用的很多了。

由于复杂的运算都是代码完成的，返回给 主 Agent 的知识计算后的结果，所以并不会占用主 Agent 的上下文。

这样 3 层设计的好处是，从模型的角度看，它需要调用的工具就固定是第 1 层的十几个，而借助命令行和代码，它又可以衍生出无数的工具组合。

还有一点就是我在之前推文提到的子智能体，Manus 也是大量采用“智能体即工具 (agent as tool)”的模式。把子智能体当工具用，比如负责检索是一个子智能体，但是这个子智能体在主 Agent 看来就是一个工具。同时也可以很好的起到减少上下文的效果。

> 媒体：
> - https://pbs.twimg.com/media/G3b0_NUWcAAl8y9.jpg

## 溯源

- 核心主张：给智能体的工具接口只保留十几个固定的原子函数（其中 Shell 和文件最关键），更多能力放到沙箱里的命令行工具（不常用的用 --help 按需查）和模型现写的代码里，子智能体也当成工具；这样模型面对的工具集小而稳定，却能组合出无数能力，还不占主智能体的上下文。
- 源知识：
  - [Manus 的分层动作空间（上下文工程分享）](../roots/ji-2025-manus-layered-action-space.md) · 关系：直接源自 · 强弱：强。宝玉转述的正是 Manus 自己公开的设计：Lance Martin 整理的研讨会内容写明 Manus 用“分层动作空间”，函数调用层少于 20 个原子函数，大部分动作下放到沙箱用 Bash 执行，MCP 工具也包成命令行，子智能体用来隔离上下文。
  - [Unix 哲学](../roots/unix-philosophy.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。一个 Shell 加一批格式统一、带 --help 的小命令行工具，靠组合衍生出无数能力，正是 Unix 用管道组合小工具的思路；作者没有提 Unix。
  - [CodeAct：用可执行代码当智能体的动作](../roots/wang-2024-executable-code-actions.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。第 3 层“LLM 实时编写 Python 代码，通过代码实现更复杂的功能”，就是 CodeAct 论文主张的用可执行代码当动作；作者只说 Codex 里用得多，没有引用论文。
  - [渐进式披露](../roots/progressive-disclosure.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。系统提示里只列最常用工具的名字，不常用的让模型自己列出来、用 --help 再看用法，是先给少量、需要时再展开的渐进式披露。
  - [AI 智能体的上下文工程](../roots/anthropic-2025-effective-context-engineering.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“把子智能体当工具用……减少上下文”、复杂运算交给代码只回传结果，和 Anthropic 上下文工程里“工具要精简、用子智能体保持上下文干净”的建议一致；作者没有引用。
- 本质：这条新知识本质上是 Unix“少量通用原语加可组合的小工具”的思路，再加上用代码当动作和渐进式披露，在大模型智能体工具设计场景下的应用。
- 整理于：2026-10-18（第 2 轮）
