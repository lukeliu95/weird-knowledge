---
name_zh: "Anthropic 多智能体研究系统"
name_en: "How we built our multi-agent research system"
proposer: "Jeremy Hadfield、Barry Zhang、Kenneth Lien、Florian Scholz、Jeremy Fox、Daniel Ford（Anthropic）"
year: "2025"
type: 研究报告
verified: true
---

# Anthropic 多智能体研究系统（How we built our multi-agent research system）

## 一句话

Anthropic 用“一个主 Agent 规划、多个子 Agent 各带独立上下文并行搜索”的编排-工人架构做研究，内部评测比单 Agent 高 90.2%，但 token 消耗约为聊天的 15 倍，只适合高价值、可并行的任务。

## 原始出处

- How we built our multi-agent research system, Jeremy Hadfield et al., Anthropic Engineering, 2025-06-13，https://www.anthropic.com/engineering/multi-agent-research-system

## 更底层的源头

- [构建高效的智能体](anthropic-2024-building-effective-agents.md) · 关系：相近
- [集体智能](collective-intelligence.md) · 关系：直接源自
- [神经网络规模定律](neural-scaling-law.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Anthropic 多智能体研究系统详解](../clips/2026-10-18-oran-ge-anthropic-multi-agent-research.md) | 直接源自 | 强 |
| [用个人AI编排者带动一支永不睡觉的开发队](../clips/2026-10-18-ayi-ainotes-personal-ai-orchestrator-openclaw.md) | 相近 | 弱（模型复核通过） |
| [Matrix：Agent 公司架构](../clips/2026-10-18-bruceguai-matrix-agent-company-architecture.md) | 相近 | 弱（模型复核通过） |
| [Claude Code 的 Task 工具原理](../clips/2026-10-18-dotey-claude-code-task-subagent.md) | 相近 | 弱（模型复核通过） |
| [微软 Agensh：不设管家，最多 1024 个 agent 靠共享工作区和团队 Wiki 自协作，规模变大后自发长出评审和整合者](../clips/2026-10-22-aigclink-agensh-decentralized-1024-agents.md) | 挑战 | 强 |
| [把 Claude Code 分成"司令官"和"部下"自主跑开发：主会话 Opus 只管计划、分工、验证、记录，实现、审查、调研交给 Sonnet / Haiku 的 subagent，用定义文件的工具栏和模型栏硬性限权](../clips/2026-10-25-xin-tech-commander-subordinate-agent-roles.md) | 直接源自 | 强 |
