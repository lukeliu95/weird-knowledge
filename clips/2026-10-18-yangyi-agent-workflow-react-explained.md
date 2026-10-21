---
title: "大白话讲清 Agent、工作流与 ReACT"
author: "Yangyi (@yangyi)"
url: https://x.com/yangyi/status/1926647632950104095
source: X
published: 2025-05-25 14:32 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [anthropic-2024-building-effective-agents, yao-2022-react, zhao-2023-expel, retrieval-augmented-generation, intelligent-agent, exploration-exploitation-dilemma, ambidextrous-organization]
---

## 原文

如果你搞不懂什么是Agent / workflow / Agentic / ReACT
那可以看看我的大白话注释：
----------------
Agent ， 广泛意义上讲，是一个智能黑盒，你给一个input，Agent识别意图，按照它自己的设定去给你一个output

这个黑盒里，很可能出现套娃情况，那也就是MultiAgent，但实际上对外是无感知的，大家仍然把它理解成「一个」Agent，但可能他是个Agent Team

狭隘来说，Agent就是一个定义了Prompt，打通了tools与Rag的LLM

至于说workflow，只是一种多Agent作业的形式，管这里面的串联的各类作业流程统称在一起叫Workflow

也就是说：
Agent > 工人，或者施工团队
workflow > 施工流程
------------------
接下来，workflow是一体两面的
既有Agentic的，也有rule-based的

Agentic就是智能化的，让AI自己去识别意图，定位问题，思考并规划解决方案
Rule-based，就是标准的SOP，AI就是按照人既定的路线进行处理

开放性问题，或者没有经验的探索性问题，就需要偏Agentic，交给AI自己来做，因为没有经验，也没有SOP，更多情况下就是试错>获得经验>沉淀有效经验>慢慢形成固定方法，它更适合系统性的解决泛化问题

明确的问题，已经有固定的处理方法了，很清楚人类是如何处理这类问题的，AI直接COPY完事，那就是Rule-based
你只要按照既定的路线写个规则，让AI照着干，就好了

你想想，日常工作中，是不是既需要创新型人才去探索未知，也需要培训苦力螺丝钉按照既定路线执行？

所以Agent也是这样，既需要agentic，也需要rule-based
这便是一体两面钟摆两端

经常性的情况是，MultiAgent中既有负责agentic的，也有负责rule-based的，这就是阴中有阳，阳中有阴
---------------
那什么是ReACT

人要在干中学，Agent也是如此
光有RAG就像百看兵书的赵括，他想成为白起，就需要ReACT

说白了就是实践，与真实世界交互
每次交互，你都会拿回来一次数据，这就是经验
去分析经验，将有效经验沉淀到知识库，进而增强RAG，这个Agent就会变强了一点儿，这就是ReACT
-----------------
说到这里就不难理解

Agentic workflow往往是动态变化的
Rule-based workflow在某段时期内一般是静态的
前者幻觉更多，因为要试错
后者幻觉更少，因为更确定

前者更适合去ReACT
后者更适合去精准提升细分场景成功率

而实际中往往都会混合使用，在一个MultiAgent中，既有Agentic workflow，又同时存在rule-based workflow

比如在规划时，是Agentic的，干具体任务时，分工给的Agent又是rule-based
------------------
因为有这些东西，才会凸显出工程化的意义
否则大家做的套壳，没有任何壁垒
唯一能做的就是等着基础模型变强罢了

## 溯源

- 核心主张：Agent 是带提示词、工具和检索的大模型（内部可能是多个 agent）；工作流有两端：agentic（让模型自己识别、规划、试错）和 rule-based（按人定好的 SOP 执行），开放、没经验的问题用前者，明确、有成熟做法的问题用后者，实际系统里两者混用；agent 要变强，需要在真实交互中积累经验并沉淀进知识库；把这些组合好的工程化能力才是壁垒。
- 源知识：
  - [构建高效的智能体](../roots/anthropic-2024-building-effective-agents.md) · 关系：换了说法 · 强弱：弱（模型复核通过）。「Agentic 让 AI 自己识别意图、规划方案」对「Rule-based 按人既定路线处理」，和 Anthropic 2024 年把系统分成「智能体（模型自己决定流程）」和「工作流（代码预设路径）」几乎是同一个划分，只是作者把两者都叫 workflow；作者没有引用。
  - [ReAct：推理与行动协同](../roots/yao-2022-react.md) · 关系：直接源自 · 强弱：强。作者点名 ReACT 并做解释；但他说的「把每次交互的经验分析后沉淀进知识库、增强 RAG」不在 ReAct 原论文里，原论文讲的是一次任务中推理和行动交替进行、读环境反馈再推理，作者的解释和原意有出入。
  - [ExpeL：大模型智能体是经验学习者](../roots/zhao-2023-expel.md) · 关系：相近 · 强弱：弱（模型复核通过）。作者对 ReACT 的实际描述（与真实世界交互拿回经验，分析后把有效经验存进知识库，下次检索调用，不改模型）和 ExpeL「收集经验、用自然语言提炼心得、推理时调出心得和过往案例」几乎一样；作者没有引用。
  - [检索增强生成（RAG）](../roots/retrieval-augmented-generation.md) · 关系：直接源自 · 强弱：强。作者直接用 RAG 一词，把狭义的 agent 定义为「打通了 tools 与 RAG 的 LLM」，并用「增强 RAG」解释 agent 如何变强。
  - [智能体](../roots/intelligent-agent.md) · 关系：相近 · 强弱：弱（模型复核通过）。「你给一个 input，Agent 识别意图，按照它自己的设定给你一个 output」，是教科书里「感知环境、自主行动去实现目标的实体」的口语版。
  - [探索与利用困境](../roots/exploration-exploitation-dilemma.md) · 关系：相近 · 强弱：弱（模型复核通过）。「没有经验的探索性问题交给 AI 试错」对「已有固定方法的问题照着干」，前者幻觉多但能发现新办法，后者稳定但只能重复，就是探索与利用的取舍。
  - [双元组织（组织双元性）](../roots/ambidextrous-organization.md) · 关系：相近 · 强弱：弱（模型复核通过）。「既需要创新型人才去探索未知，也需要螺丝钉按既定路线执行」「一个 MultiAgent 里既有负责 agentic 的，也有负责 rule-based 的」，和组织双元性「同一组织里探索单元和执行单元分开又整合」一致。
- 本质：这条新知识本质上是「探索与利用」的分工（没经验的问题靠试错探索，成熟问题按 SOP 执行）加上「从经验中学习」（经验沉淀成案例、再检索复用）在大模型 agent 系统设计场景下的应用。
- 整理于：2026-10-18（第 2 轮）
