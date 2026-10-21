---
name_zh: "Claude Code 最佳实践（给 Claude 一个验证自己工作的办法）"
name_en: "Claude Code: Best practices for agentic coding"
proposer: "Boris Cherny（Anthropic）"
year: "2025"
type: 方法论
verified: true
---

# Claude Code 最佳实践（给 Claude 一个验证自己工作的办法）（Claude Code: Best practices for agentic coding）

## 一句话

用 Claude Code 做事，最关键的是给它一个能自己运行的检查（测试、构建、截图对比），让它做完、跑检查、看结果、再改，直到通过；配合“先探索、再规划、后写代码”（计划模式）和多个 Claude 互相审查。

## 原始出处

- Claude Code: Best practices for agentic coding, Boris Cherny, Anthropic Engineering, 2025-04-18（互联网档案馆存档），http://web.archive.org/web/20250502205533/https://www.anthropic.com/engineering/claude-code-best-practices
- Best practices for Claude Code, Claude Code 官方文档（原文章网址现在跳转到这里，持续更新），https://code.claude.com/docs/en/best-practices
- 争议：2025 年原文的说法是“Claude 有明确的迭代目标（视觉稿、测试用例）时表现最好”，并推荐测试驱动开发；“Give Claude a way to verify its work”“the loop closes on its own”这些原话出自后来更新、不再署名的官方文档。

## 更底层的源头

- [测试驱动开发](test-driven-development.md) · 关系：直接源自
- [反馈](feedback.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Anthropic：让模型验证自己的输出](../clips/2026-10-18-0xcodez-anthropic-agent-loop-self-verify.md) | 直接源自 | 强 |
| [Claude Code之父的三条心得](../clips/2026-10-18-ayi-ainotes-boris-cherny-workflow-three-rules.md) | 直接源自 | 强 |
| [Astra 电脑操作让验收成闭环](../clips/2026-10-18-dotey-astra-computer-use-acceptance-loop.md) | 相近 | 弱（模型复核通过） |
| [yetone 用 3 个 /loop 循环让 Claude Code 自己维护 Magpie](../clips/2026-10-18-dotey-yetone-magpie-three-loops-workflow.md) | 相近 | 弱（模型复核通过） |
