---
name_zh: "Manus 的上下文工程（季逸超的博文与研讨会）"
name_en: "Context Engineering for AI Agents: Lessons from Building Manus"
proposer: "季逸超（Yichao “Peak” Ji，Manus 联合创始人、首席科学家）"
year: "2025"
type: 方法论
verified: true
---

# Manus 的上下文工程（季逸超的博文与研讨会）（Context Engineering for AI Agents: Lessons from Building Manus）

## 一句话

Manus 管理上下文的经验：围绕 KV 缓存设计、工具用遮蔽而不是增删、把文件系统当成可无限扩展的外部记忆来卸载上下文；2025 年 10 月与 LangChain 的研讨会又讲了分层动作空间：只给模型少量函数调用，大部分动作卸载到沙箱里的预装工具和标准 shell 命令上。

## 原始出处

- Context Engineering for AI Agents: Lessons from Building Manus, Yichao “Peak” Ji, Manus 博客, 2025-07-18，https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
- Context Engineering in Manus, Lance Martin（LangChain 与 Manus 研讨会的文字总结）, 2025-10-15，https://rlancemartin.github.io/2025/10/15/manus/
- Context Engineering Webinar: Manus + LangChain（活动页面），https://luma.com/819i5ime
- 争议：推文里「只列工具名、让模型用 --help 自己了解用法」这一细节应出自 10 月研讨会；Lance Martin 的文字总结只写到沙箱里有预装工具和标准 shell 命令，没有写 --help，这一细节待对照录像确认。

## 更底层的源头

- [Unix 哲学](unix-philosophy.md) · 关系：相近
- [MemGPT：让大模型像操作系统一样管理内存](packer-2023-memgpt-llm-os.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Agent Skills 是上下文卸载](../clips/2026-10-18-yonah-x-skills-context-offloading.md) | 直接源自 | 强 |
