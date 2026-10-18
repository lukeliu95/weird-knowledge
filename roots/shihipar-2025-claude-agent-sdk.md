---
name_zh: "用 Claude Agent SDK 构建智能体（收集上下文→行动→验证→重复）"
name_en: "Building agents with the Claude Agent SDK"
proposer: "Thariq Shihipar（Anthropic）"
year: "2025"
type: 方法论
verified: true
---

# 用 Claude Agent SDK 构建智能体（收集上下文→行动→验证→重复）（Building agents with the Claude Agent SDK）

## 一句话

Claude Code SDK 改名为 Claude Agent SDK，核心思路是给 agent 一台电脑，让它像人一样工作；agent 按“收集上下文→采取行动→验证工作→重复”的循环运转，验证可以靠规则检查、视觉反馈或另一个模型当裁判，上下文靠文件系统检索、子 agent 和自动压缩来管理。

## 原始出处

- Building agents with the Claude Agent SDK, Thariq Shihipar, Anthropic, 2025-09-29（原 anthropic.com/engineering 网址跳转到这里），https://claude.com/blog/building-agents-with-the-claude-agent-sdk

## 更底层的源头

- [构建高效的智能体](anthropic-2024-building-effective-agents.md) · 关系：相近
- [反馈](feedback.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Anthropic：让模型验证自己的输出](../clips/2026-10-18-0xcodez-anthropic-agent-loop-self-verify.md) | 相近 | 弱（待 Luke 确认） |
| [谈用 Claude 做智能体：少搭脚手架](../clips/2026-10-18-alexalbert-agent-scaffolding-context-talk.md) | 直接源自 | 强 |
