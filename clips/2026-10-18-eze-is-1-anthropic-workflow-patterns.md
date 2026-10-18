---
title: "Anthropic 六种工作流与智能体"
author: "一泽Eze (@eze_is_1)"
url: https://x.com/eze_is_1/status/1982741162311270514
source: X
published: 2025-10-27 09:28 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind: 观点
topic: Agent 与 Skill
roots: []
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

