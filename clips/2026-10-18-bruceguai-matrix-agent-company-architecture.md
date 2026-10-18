---
title: "Matrix：Agent 公司架构"
author: "Bruce Guai (@BruceGuai)"
url: https://x.com/BruceGuai/status/2070130243059495142
source: X
published: 2026-06-25 13:01 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [blackboard-system, society-of-mind, anthropic-2025-multi-agent-research-system, division-of-labour, organizational-learning, compounding-engineering]
---

## 原文

我们是如何构建当下领先的 Agent 产品架构的？

Matrix 不是一个 Agent，而是一套能长期运行的 Agent 公司架构。

这张图就是 我们最领先的 Agent harness 的底层架构。

Matrix 不是把所有文件、工具、权限都塞给一个巨大的 Agent，然后祈祷它别跑偏。

它是一套 Agent 公司 OS。
一个工作区，先变成公司的大脑：
代码、文档、文件、目标、规则、审批、历史任务、优秀样例、品味，都会进入同一个组织上下文。

在大脑之上，是 Matrix 的运行指挥层：
唤醒、定时任务、部门消息、OKR 状态、权限、模型路由、证据账本、记忆更新，都由它调度。

再往下，工作不再是一个聊天窗口里的随机对话，而是被拆成长期运行的部门：
创始人战略、产品工程、增长市场、运营支持、研究实验台。

每个部门都有自己的身份、记忆、技能、任务历史和独立上下文。
部门主导 Agent 负责读目标、分派任务、选择最合适的执行席位。
有些任务适合 Codex。
有些适合 Claude Code。
有些适合 Matrix 原生 worker。
有些必须交给浏览器和电脑自动化。
重点不是“一个模型做所有事”。

重点是：
正确的 Agent，拿到正确的上下文，待在正确的边界里，用正确的工具，最后用证据证明它真的完成了。

这也是为什么 Matrix 里最重要的不是聊天，而是闭环：
工作区大脑 → 部门主导 Agent → 执行 Agent → 产物 → 证据 → check-in → 记忆更新。

每跑完一轮，公司都会多一点记忆、多一点经验、多一点可复用的工作方法。

这才是我们理解的自进化 Agent。不是一个 Agent 只在虚空里改自己的 prompt，而是一个组织通过真实产物和证据不断复利。Matrix 要做的不是“更聪明的聊天机器人”。而是让每个人都能拥有自己的第一家 Agent 公司。

dm or 评论再给大家送一些测试额度，数量有限

> 媒体：
> - https://pbs.twimg.com/media/HLqTqX2aAAEDzOG.jpg

## 溯源

- 核心主张：与其把所有文件、工具、权限塞给一个大 agent，不如把 agent 系统组织成一家公司：共享的组织上下文当“大脑”，调度层负责唤醒、权限和模型路由，长期运行的“部门”各有身份、记忆和技能，主导 agent 把任务派给最合适的执行者，再用“产物→证据→记忆更新”的闭环让组织越跑越有经验。
- 源知识：
  - [黑板系统](../roots/blackboard-system.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“工作区大脑”是所有部门共用的上下文，多个专门 agent 围绕它读写，上面再有一层调度决定谁何时行动，和黑板系统“公共黑板 + 专门知识模块 + 控制器”的结构几乎一样；作者没有提到。
  - [心智社会](../roots/society-of-mind.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“Matrix 不是一个 Agent”，能力来自许多各司其职的 agent 组织在一起，和 Minsky 说智能来自许多简单 agent 组成的“社会”是同一个思路。
  - [Anthropic 多智能体研究系统](../roots/anthropic-2025-multi-agent-research-system.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。部门主导 agent“读目标、分派任务、选择最合适的执行席位”，就是主 agent 规划、子 agent 执行的编排-工人架构。
  - [分工](../roots/division-of-labour.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。把工作拆给战略、产品工程、增长、运营、研究等长期部门，并按任务挑 Codex、Claude Code 或浏览器自动化，是按专长分工。
  - [组织学习](../roots/organizational-learning.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“每跑完一轮，公司都会多一点记忆、多一点经验、多一点可复用的工作方法”“组织通过真实产物和证据不断复利”，就是组织把经验沉淀为组织记忆的组织学习。
  - [复合工程](../roots/compounding-engineering.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。把每轮的结果和经验写回记忆和工作方法，让下一轮更容易，和复合工程“每次工作的教训写回系统”一致。
- 本质：这条新知识本质上是黑板架构和组织学习在多 agent 系统上的应用：用公司式的分工、共享上下文和闭环复盘，让 agent 组织持续积累经验。
- 整理于：2026-10-18（第 2 轮）
