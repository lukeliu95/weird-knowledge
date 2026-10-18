---
title: "Matrix：Agent 公司架构"
author: "Bruce Guai (@BruceGuai)"
url: https://x.com/BruceGuai/status/2070130243059495142
source: X
published: 2026-06-25 13:01 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
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

