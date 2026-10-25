---
name_zh: "别做多智能体"
name_en: "Don't Build Multi-Agents"
proposer: "Walden Yan（Cognition）"
year: "2025"
type: 方法论
verified: true
---

# 别做多智能体（Don't Build Multi-Agents）

## 一句话

多个 agent 并行容易出错，两条原则：要共享完整上下文（整段 agent 轨迹，而不只是单条消息）；行动里暗含决策，决策互相冲突就会出坏结果。文中提到 Claude Code 让子 agent 保持简单，正是因为并行的子 agent 可能给出互相冲突的结果。

## 原始出处

- Don't Build Multi-Agents, Walden Yan, Cognition 博客, 2025-06-12，https://cognition.com/blog/dont-build-multi-agents

## 更底层的源头

- [易并行（尴尬并行）](embarrassingly-parallel.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [给公司业务接入智能体的五点思考](../clips/2026-10-18-dotey-enterprise-agent-integration-tips.md) | 相近 | 弱（模型复核通过） |
| [Claude Code 的 Task 工具原理](../clips/2026-10-18-dotey-claude-code-task-subagent.md) | 挑战 | 弱（模型复核通过） |
| [备忘录加 worktree 就够了](../clips/2026-10-18-hilng77042-opc-agents-notes-worktrees.md) | 相近 | 弱（模型复核通过） |
| [Meta 的瘦编排器模式：编排器只管路由和检查，不做领域推理，14 个专项子 agent 各管一块](../clips/2026-10-20-meta-thin-orchestrator-agent-architecture.md) | 挑战 | 弱（模型复核通过） |
| [KV cache 的暴政：今天的 agent 只能"只追加对话"，由此带来路由失效、工具挤占上下文、压缩丢信息、子 agent 少等六个毛病（《Jev 工程学：为 coding agent 而作》中译介绍）](../clips/2026-10-25-yibie-jev-engineering-kv-cache-tyranny.md) | 相近 | 弱（模型复核通过） |
