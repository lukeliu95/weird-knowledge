---
title: "阿里 AgentScope 1.0 智能体框架"
author: "AIGCLINK (@aigclink)"
url: https://x.com/aigclink/status/1963005626910752976
source: X
published: 2025-09-02 22:26 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

阿里放出了全新智能体开发框架：AgentScope 1.0，核心是深度融合了实时介入控制、智能上下文管理、高效工具调用能力

把智能体开发、部署、监控打包成了一条生产线

1、基于异步架构，原生支持实时中断和自定义中断处理
可以安全中断，支持状态持续，任务流无缝续接
可以实时打断，支持实时干预
通过中断处理机制，可以自定义智能体的中断响应逻辑

2、AgentScope通过短期记忆与跨会话长期记忆协同，重构了上下文管理

通过“动态压缩”和“混合压缩”技术，在对话内部实时提炼语义主干，保留关键信息

可配置原文与摘要的比例，在有限的上下文窗口中最大化信息密度，减缓“失忆”与“记忆混乱”

支持“动态”、“静态”、和“混合”三种长期记忆管理模式

3、AgentScope用“注册、管理、执行”三个步骤，构建了一套高效可靠的工具管理体系

提供标准化的注册接口，支持自动提取工具的JSON Schema，提供参数预设和工具函数后处理接口

支持工具的结构化组织与动态控制

采用统一接口处理所有工具调用，无论同步、异步或流式输出，在 AgentScope 中将被统一为异步流式返回，降低工具函数返回的处理代价

AgentScope由三层技术架构组成：
AgentScope：核心框架，负责智能体的构建与应用编排
AgentScope Runtime： 提供智能体运行和部署环境
AgentScope Studio： 提供可视化开发与监控工具

这三层架构也是三个独立的项目，可以单独使用，AgentScope Runtime、AgentScope Studio也可以兼容像LangGraph、AutoGen等其他框架

AgentScope同时还给出了一些开箱即用的示例，示例可以根据自己的需求进行定制

#AIagent #智能体构建 #AgentScope

> 媒体：
> - https://pbs.twimg.com/media/Gz37wBDbAAcnWCh.jpg

## 溯源

