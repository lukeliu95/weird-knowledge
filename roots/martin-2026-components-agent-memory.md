---
name_zh: "智能体记忆的四个组成部分与离线整理"
name_en: "The components of agent memory"
proposer: "Lance Martin（Anthropic）"
year: "2026"
type: 研究报告
verified: true
---

# 智能体记忆的四个组成部分与离线整理（The components of agent memory）

## 一句话

把跨会话经验分成经历记录、记忆笔记、组织表示与注入上下文，并通过后台整理修正和合并；效果取决于材料、任务和整理质量，记错和覆盖也会伤害后续表现。

## 原始出处

- Lance Martin，The components of agent memory，Anthropic，2026-11-06；已读正文，包括 CL-Bench、宝可梦、内部文档、合并资料与共享记忆写入案例。，https://www.anthropic.com/research/components-of-agent-memory
- 争议：所有成绩均是作者或厂商自报，本轮未独立复现。宝可梦每个模型仅一次运行；合并资料的 87% 对 73% 是多文档题子集，不是整组 24 题总分；共享写入实验同时改变组织方式与提示要求，不能把收益全部归因于单一写入策略。原文在部分单文档任务中未见维基收益；“做梦”不证明软件复制了生物睡眠机制。

## 更底层的源头

- [睡眠时间计算（面向未来查询的离线预计算）](lin-2025-sleep-time-compute.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Anthropic 拆解智能体记忆：边干边记，再靠“做梦”回头纠错整理](../clips/2026-11-08-dotey-anthropic-agent-memory-dreaming.md) | 直接源自 | 强 |
