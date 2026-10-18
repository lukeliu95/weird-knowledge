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
| [给公司业务接入智能体的五点思考](../clips/2026-10-18-dotey-enterprise-agent-integration-tips.md) | 相近 | 弱（待 Luke 确认） |
| [Claude Code 的 Task 工具原理](../clips/2026-10-18-dotey-claude-code-task-subagent.md) | 挑战 | 弱（待 Luke 确认） |
| [备忘录加 worktree 就够了](../clips/2026-10-18-hilng77042-opc-agents-notes-worktrees.md) | 相近 | 弱（待 Luke 确认） |
