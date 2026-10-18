---
name_zh: "Cloudflare Code Mode：让模型写代码放进沙箱执行"
name_en: "Code Mode: the better way to use MCP"
proposer: "Kenton Varda、Sunil Pai（Cloudflare）"
year: "2025"
type: 方法论
verified: true
---

# Cloudflare Code Mode：让模型写代码放进沙箱执行（Code Mode: the better way to use MCP）

## 一句话

与其让大模型直接做工具调用，不如把工具转成 TypeScript API，让模型写代码去调用，再放进轻量的 V8 隔离沙箱（Dynamic Workers）里执行；理由是模型见过的真实代码远多于工具调用示例。

## 原始出处

- Code Mode: the better way to use MCP, Kenton Varda & Sunil Pai, Cloudflare Blog, 2025-09-26，https://blog.cloudflare.com/code-mode/
- Sandboxing AI agents, 100x faster（Dynamic Workers 公开测试）, Kenton Varda & Sunil Pai, Cloudflare Blog, 2026-03-24，https://blog.cloudflare.com/dynamic-workers/

## 更底层的源头

- 已追到基础层，或暂未找到更底层的源头

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [与Claude Code讨论艺术与约束](../clips/2026-10-18-turingou-constraint-in-live-music-product.md) | 挑战 | 强 |
