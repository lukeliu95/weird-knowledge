---
title: "大白话讲清 Agent、工作流与 ReACT"
author: "Yangyi (@yangyi)"
url: https://x.com/yangyi/status/1926647632950104095
source: X
published: 2025-05-25 14:32 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
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

