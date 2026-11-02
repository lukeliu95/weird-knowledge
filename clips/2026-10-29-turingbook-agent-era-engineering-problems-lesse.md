---
title: "Anthropic 平台负责人谈智能体时代工程师还要解决的问题"
author: "刘江/LIU Jiang (@turingbook)"
url: https://x.com/turingbook/status/2114724007639392330
source: X
published: 2026-10-26 14:21 UTC
saved: 2026-10-29
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [lesse-2026-new-problems-for-engineers, principle-of-least-privilege]
---

## 原文

Anthropic平台研发负责人Katelyn Lesse的文章，谈智能体时代，工程师不要觉得没事儿可做了，还有很多需要解决的问题：
-智能体基础设施，类似传统软件中k8s，包括新的文件系统、沙箱服务、Agent Substrate这样的运行时。
-智能体的身份验证与授权。问题可能很复杂：什么时候是智能体自己，什么时候它在代表人类？
-安全与隔离。漏洞的发现比修补速度快，智能体本身也存在安全问题，在多智能体环境中更为严峻。
-监控与停机。确保智能体在干好事儿，如果不及时发现并停止。

## 溯源

- 核心主张：Lesse 认为长期多 agent 系统把工程挑战转向有状态运行基建、身份和授权、安全隔离、跨 agent 监控和全局停止。这是问题清单与研究方向，不是已解决问题的产品能力表或数千 agent 已普遍落地的统计。
- 源知识：
  - [Lesse：多 agent 系统给工程师的新问题](../roots/lesse-2026-new-problems-for-engineers.md) · 关系：直接源自 · 强弱：强。已读 Lesse 本人网站全文，四类问题与存档转述吻合；作者站日期为 2026-10-25，转述推文发于 10-26。
  - [最小权限原则](../roots/principle-of-least-privilege.md) · 关系：相近 · 强弱：弱（模型复核通过）。身份授权、沙箱及限制失陷范围，与只给必要权限的原则相近；不表示最小权限可以解决全部 agent 安全问题。
- 本质：这条新知识本质上是经典身份、权限与隔离工程在长期多 agent 系统里的重新设计。
- 整理于：2026-11-03（第 9 轮）
