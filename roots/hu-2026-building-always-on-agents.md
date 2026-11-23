---
name_zh: "构建常驻智能体（事件收件箱、定时器、记忆、权限、发件箱）"
name_en: "Building always-on agents"
proposer: "William Hu（Anthropic）"
year: "2026"
type: 方法论
verified: true
---

# 构建常驻智能体（事件收件箱、定时器、记忆、权限、发件箱）（Building always-on agents）

## 一句话

常驻 agent 并不是一直在跑：它大部分时间在睡，事件进了收件箱或定时器到点才醒来跑一次。事件收件箱、定时器、记忆、权限、发件箱五个部件，把一次次短跑连成一个看起来一直在线的循环。

## 原始出处

- Building always-on agents，William Hu，Anthropic（claude.com 资源文章，Best practices 类），2026-11-13；已读全文，https://claude.com/blog/building-always-on-agents
- 争议：这是 Anthropic 的工程建议，不是实验研究，文中没有对照数据。文中唯一的数字（Opus 5.5 在一个长任务编程基准上每解一题比 Opus 5 便宜 78%，常规负载便宜 40%）引自它自己的模型文档。正式发件箱是可选的：文中说多数常驻 agent 有一个直接发送的工具就够，要控制发送节奏或要能从错误中恢复时才需要发件箱。“做梦”（回看旧会话整理记忆）也是可选项。

## 更底层的源头

- [构建高效的智能体](anthropic-2024-building-effective-agents.md) · 关系：直接源自
- [智能体记忆的四个组成部分与离线整理](martin-2026-components-agent-memory.md) · 关系：直接源自
- [AI 智能体的上下文工程](anthropic-2025-effective-context-engineering.md) · 关系：相近
- [actor 模型](actor-model.md) · 关系：相近
- [企业集成模式（持久消息通道、可靠投递、幂等接收者、轮询消费者等）](hohpe-2003-enterprise-integration-patterns.md) · 关系：相近
- [最小权限原则](principle-of-least-privilege.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [24 小时在线的 agent 助理靠五样东西](../clips/2026-11-18-dotey-always-on-agent-five-parts.md) | 直接源自 | 强 |
| [Anthropic 常驻 agent 指南的五个要点](../clips/2026-11-18-tekonburns-anthropic-always-on-agents-guide.md) | 直接源自 | 强 |
| [2027 年的 agent 平台：应用层的终局](../clips/2026-11-23-john-ssuh-agent-platform-2027-endgame.md) | 相近 | 弱（模型复核通过） |
