---
name_zh: "Manus 的分层动作空间（上下文工程分享）"
name_en: "Context Engineering in Manus (layered action space)"
proposer: "季逸超（Yichao \"Peak\" Ji，Manus 联合创始人）；Lance Martin（LangChain）整理"
year: "2025"
type: 方法论
verified: true
---

# Manus 的分层动作空间（上下文工程分享）（Context Engineering in Manus (layered action space)）

## 一句话

函数调用层只留不到 20 个原子函数（Bash、文件系统、代码执行等），其余大部分动作下放到虚拟机沙箱里用 Bash 调命令行工具（MCP 工具也包成命令行）；子智能体主要用来隔离上下文，而不是按角色分工；文件系统被当作最终的外部记忆。

## 原始出处

- Context Engineering in Manus, Lance Martin, 2025-10-15（与季逸超的上下文工程网络研讨会整理），https://rlancemartin.github.io/2025/10/15/manus/
- Context Engineering for AI Agents: Lessons from Building Manus, Yichao 'Peak' Ji, Manus 博客, 2025-07-18，https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
- Context Engineering Webinar: Manus + LangChain（活动页），https://luma.com/819i5ime
- 争议：宝玉写的三层（函数调用 / 沙箱工具 / 代码包与 API）中，Lance Martin 的文字整理只明确写了「函数调用」和「虚拟机沙箱」两层和不到 20 个原子函数；第三层「代码包与 API」的命名应出自研讨会幻灯片，这次没有找到原件核对（待确认）。

## 更底层的源头

- [AI 智能体的上下文工程](anthropic-2025-effective-context-engineering.md) · 关系：相近
- [Unix 哲学](unix-philosophy.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Manus 把工具分成三层的设计](../clips/2026-10-18-dotey-manus-three-layer-tools.md) | 直接源自 | 强 |
