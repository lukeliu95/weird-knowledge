---
name_zh: "智能体的上下文工程（写入、选取、压缩、隔离）"
name_en: "Context Engineering for Agents"
proposer: "Lance Martin（LangChain）"
year: "2025"
type: 方法论
verified: true
---

# 智能体的上下文工程（写入、选取、压缩、隔离）（Context Engineering for Agents）

## 一句话

把 agent 管理上下文的常见做法归成四类：写入（把信息存到上下文窗口之外，如草稿本、长期记忆）、选取（需要时再拉回窗口）、压缩（只保留完成任务所需的 token）、隔离（把上下文拆给子 agent、沙箱或不同的状态字段）。

## 原始出处

- Context Engineering for Agents, Lance Martin, 2025-06-23（作者博客），https://rlancemartin.github.io/2025/06/23/context_engineering/
- Context Engineering for Agents, LangChain Blog, 2025-07-02，https://www.langchain.com/blog/context-engineering-for-agents
- 争议：LangChain 官网版本署名为“LangChain 团队”，发布于 2025-07-02；作者个人博客署名 Lance Martin，发布于 2025-06-23。

## 更底层的源头

- [上下文工程](context-engineering.md) · 关系：直接源自
- [MemGPT：让大模型像操作系统一样管理内存](packer-2023-memgpt-llm-os.md) · 关系：相近
- [关注点分离](separation-of-concerns.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [上下文工程：智能体的核心实践指南](../clips/2026-10-18-shao-meng-context-engineering-guide.md) | 直接源自 | 强 |
| [Claude Code 的 Task 工具原理](../clips/2026-10-18-dotey-claude-code-task-subagent.md) | 相近 | 弱（模型复核通过） |
| [Meta 的瘦编排器模式：编排器只管路由和检查，不做领域推理，14 个专项子 agent 各管一块](../clips/2026-10-20-meta-thin-orchestrator-agent-architecture.md) | 相近 | 弱（模型复核通过） |
| [KV cache 的暴政：今天的 agent 只能"只追加对话"，由此带来路由失效、工具挤占上下文、压缩丢信息、子 agent 少等六个毛病（《Jev 工程学：为 coding agent 而作》中译介绍）](../clips/2026-10-25-yibie-jev-engineering-kv-cache-tyranny.md) | 相近 | 弱（模型复核通过） |
