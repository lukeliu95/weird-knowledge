---
title: "Anthropic 六种工作流与智能体"
author: "一泽Eze (@eze_is_1)"
url: https://x.com/eze_is_1/status/1982741162311270514
source: X
published: 2025-10-27 09:28 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [anthropic-2024-building-effective-agents, pipeline-software, mixture-of-experts, ensemble-learning, divide-and-conquer-algorithm, madaan-2023-self-refine, yao-2022-react]
---

## 原文

除此之外， Anthropic 还总结了一些 workflow 与 Agents 类型，可能为你带来一些参考启发：

Workflow：
1）增强型 LLM（the augmented LLM）
给 LLM 配上检索、工具、记忆等增强功能，LLM 可以主动使用，生成自己的搜索查询、选择合适的工具。
和 Agent 的区别是，增强型 LLM 不会规划任务流程，也无法自行决定下一步做什么，不能自主进行多轮交互。

2）提示链工作流（Workflow： Prompt Chaining） 
通过将任务分解为多个子环节，由多个 LLM 分别处理前一个环节的输出，就像 coze、dify 一样。
示例应用：营销文案生成 → 翻译为其他语言；文章大纲生成 → 检查 → 分段完成正文编写

3）路由式工作流（Workflow：Routing） 
允许 LLM 分类 input，并在更合适的子任务中解决。可以对不同类型的任务进行分别的提示优化，不会干扰其他任务的表现
比如：AI  客服、Chatbot 自主切换回答模型（简单问题就切换到小模型，类似 ChatGPT 5 网页服务，优化成本和响应速度）

4）并行式工作流（Workflow：Parallelization） 
允许 LLMs 同时处理一个任务，并程序性地聚合它们的输出。分两种应用角度：
一是将任务分解为并行运行的独立子任务
二是多次运行同一任务获取多样化结果 or 进行投票
并行式工作流更适合在提升任务执行性能 或者 LLM 拆解处理单因素任务优于同时处理多因素任务时使用，比如： 
 - Sectioning：在与用户对话时，一个模型负责处理用户意图，一个模型筛查问答中不适当、不合规的内容。
 - Voting：代码 or 内容审计，通过不同模型/不同提示，从不同方面对内容进行评估，甚至通过投票阈值来过滤假阳性。

5）协调-执行式工作流（Workflow：Orchestrator-Workers） 
中央 LLM 分解任务（相较并行式更灵活，子任务不是预先定义的），工作者 LLM 分别执行，返回结果，综合输出。
示例应用：需要对多个文件进行复杂更改的 coding 产品，需要分解从多个来源收集信息的 search 任务等。

6）评估-优化式工作流（Workflow：Evaluator-Optimizer） 
一个 LLM 调用生成响应，而另一个提供评估和反馈，形成循环。其有效程度可以这样衡量：当人类清晰地表达其反馈时，首先，LLM 的响应可以明显改进；其次，LLM 能够提供这种反馈。
比如：Search 场景、多轮文学创作与编辑（Evaluator 对多轮生成内容，进行综合反馈与建议）。

Agent：
通常指自主智能体，不断基于环境反馈的循环使用工具。能够理解复杂输入，推理与规划，以及从错误中恢复。（通常会包含最大迭代次数，控制 Agent 行动何时终止）
常见的 Computer Use、Coding Agent 均在此列。
随着底层模型能力的提升，Agent 独立解决复杂问题、处理错误反馈的能力也会随之提升。

> 媒体：
> - https://pbs.twimg.com/media/G4QcjXJXYAAjZV2.jpg
> - https://pbs.twimg.com/media/G4QcjXMXEAAzElH.jpg

## 溯源

- 核心主张：大模型系统可以归纳成几种可组合的基本模式：增强型 LLM、提示链、路由、并行、协调-执行、评估-优化，以及基于环境反馈循环调用工具的自主 Agent。
- 源知识：
  - [构建高效的智能体](../roots/anthropic-2024-building-effective-agents.md) · 关系：直接源自 · 强弱：强。作者明说是 Anthropic 总结的类型，列表与原文逐条对应。
  - [管道（软件）](../roots/pipeline-software.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。提示链「前一环节的输出交给下一个 LLM 处理」就是软件管道「前一个单元的输出是后一个的输入」。
  - [混合专家](../roots/mixture-of-experts.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。路由「先给输入分类，再交给更合适的子任务」与混合专家用门控把输入分给擅长的专家是同一结构。
  - [集成学习](../roots/ensemble-learning.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。并行里的投票（多个模型或提示分别评估，再按投票阈值过滤）就是集成学习的多数投票。
  - [分治法](../roots/divide-and-conquer-algorithm.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。协调-执行「中央拆任务、工人分别做、再综合」是分治的思路，只是子任务由模型动态决定。
  - [自我改进：用自我反馈迭代改写](../roots/madaan-2023-self-refine.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。评估-优化「一个生成、一个给反馈、循环改进」与 Self-Refine 的生成-反馈-改写循环一致；Anthropic 原文没有引用。
  - [ReAct：推理与行动协同](../roots/yao-2022-react.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。Agent「基于环境反馈循环使用工具、能从错误中恢复」就是 ReAct 的推理-行动-观察循环；Anthropic 原文没有引用。
- 本质：这条新知识本质上是管道、分治、集成投票、反馈循环这些经典计算与控制思想在大模型编排上的重新组合。
- 整理于：2026-10-18（第 1 轮）
