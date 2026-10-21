---
title: "Agent Skills设计哲学与迭代"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/2036114136245969025
source: X
published: 2026-03-23 16:13 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [anthropic-2025-agent-skills, unix-philosophy, anthropic-2024-building-effective-agents, anthropic-2025-effective-context-engineering, zechner-2025-dont-need-mcp, eating-your-own-dog-food]
---

## 原文

Agent Skills 设计哲学和实战进化

前半段是真实场景演示，看我日常怎么用 Agent + Skills 完成实际工作；后半段是设计哲学和迭代方法论，把踩过的坑和悟出来的经验都讲透。

四个核心观点：

1）从提示词到 Skills：起步没有门槛。把你已有的好用提示词、好的实践、甚至模糊的想法，直接用 /skill-creator 变成 Skill。关键是动手。

2）别做万能 Skill：Skill 要原子化，每个只做一件事。然后用 Skill 或者 AGENTS.md 编排成工作流，让 Agent 灵活执行。我的素材收集和写作流程就是这么串起来的。

3）Skills 像随身小刀，越用越顺手：自己常用、遇到问题当场改、给 Agent 高质量对比样例让它自己优化、用 git 做版本管理留后悔药。

4）站在 Agent 角度设计：多存中间文件、先分析再执行、写清验证标准、用子 Agent 并行、脚本优先于 MCP。这些小细节决定 Skill 能不能真正跑通。

baoyu-skills 已全部开源：https://t.co/pRDqxdiSrH

> 媒体：
> - https://video.twimg.com/amplify_video/2036110650577928192/vid/avc1/480x270/DG7cjHiKYrNLcOB2.mp4?tag=21

## 溯源

- 核心主张：做 Skill 没有门槛，可以直接从现成的好提示开始；每个 Skill 只做一件事，再编排成工作流；在日常使用中当场修改、给对比样例让 agent 自己优化、用 git 留版本；设计时站在 agent 的角度：多存中间文件、先分析后执行、写清验证标准、用子 agent 并行、优先用脚本而不是 MCP。
- 源知识：
  - [用 Agent Skills 让智能体胜任真实工作](../roots/anthropic-2025-agent-skills.md) · 关系：直接源自 · 强弱：强。Agent Skills 是 Anthropic 2025 年提出的格式，文中用的 /skill-creator 出自 Anthropic 官方 skills 仓库；该文建议“让 Claude 把成功做法和常见错误沉淀进 Skill”，对应“给 Agent 高质量对比样例让它自己优化”。
  - [Unix 哲学](../roots/unix-philosophy.md) · 关系：换了说法 · 强弱：强。“Skill 要原子化，每个只做一件事，然后编排成工作流”，几乎就是 Unix 哲学“每个程序只做好一件事、再把它们组合起来”的原话。
  - [构建高效的智能体](../roots/anthropic-2024-building-effective-agents.md) · 关系：相近 · 强弱：强。“站在 Agent 角度设计”和该文附录里的“Put yourself in the model's shoes”（站在模型的位置想）几乎一字不差，都是在讲为 agent 设计好用的接口（ACI）。
  - [AI 智能体的上下文工程](../roots/anthropic-2025-effective-context-engineering.md) · 关系：相近 · 强弱：弱（模型复核通过）。“多存中间文件”“用子 Agent 并行”，对应上下文工程里的结构化笔记和子 agent 架构，目的都是让主上下文保持干净。
  - [Mario Zechner：也许你根本不需要 MCP](../roots/zechner-2025-dont-need-mcp.md) · 关系：相近 · 强弱：弱（模型复核通过）。“脚本优先于 MCP”和 Zechner 说“多数场景让 agent 直接调命令行和脚本就够，MCP 既占上下文又不好组合”是同一个判断；作者没有引用。
  - [吃自己的狗粮（自用产品）](../roots/eating-your-own-dog-food.md) · 关系：相近 · 强弱：弱（模型复核通过）。“自己常用、遇到问题当场改”，靠自己天天用来发现问题、持续改进，是自用产品（吃自己的狗粮）的做法。
- 本质：这条新知识本质上是 Unix 哲学（小而专、可组合）和“站在使用者角度设计接口”在 agent 技能包上的应用。
- 整理于：2026-10-18（第 2 轮）
