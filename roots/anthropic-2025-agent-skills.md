---
name_zh: "用 Agent Skills 让智能体胜任真实工作"
name_en: "Equipping agents for the real world with Agent Skills"
proposer: "Barry Zhang、Keith Lazuka、Mahesh Murag（Anthropic）"
year: "2025"
type: 方法论
verified: true
---

# 用 Agent Skills 让智能体胜任真实工作（Equipping agents for the real world with Agent Skills）

## 一句话

把指令、脚本和资源打包成一个个带 SKILL.md 的文件夹（Skill）；智能体平时只看名字和描述，用到时才加载正文和附带文件（渐进式披露），Skill 里的脚本可以直接执行而不必读进上下文；建议先在代表性任务上找能力缺口，再让 Claude 把成功做法和常见错误沉淀进 Skill 里迭代。

## 原始出处

- Equipping agents for the real world with Agent Skills, Barry Zhang, Keith Lazuka, Mahesh Murag, Anthropic Engineering, 2025-10-16，https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- anthropics/skills（Anthropic 官方 Agent Skills 仓库，含 skill-creator）, GitHub，https://github.com/anthropics/skills
- 同文 Claude 官方博客版，https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills

## 更底层的源头

- [渐进式披露](progressive-disclosure.md) · 关系：直接源自
- [AI 智能体的上下文工程](anthropic-2025-effective-context-engineering.md) · 关系：相近
- [模块化编程](modular-programming.md) · 关系：相近
- [过程性知识（知道怎么做）](procedural-knowledge.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Agent Skills设计哲学与迭代](../clips/2026-10-18-dotey-agent-skills-design-philosophy.md) | 直接源自 | 强 |
| [ADK 开发者该懂的五种 Agent Skill 设计模式](../clips/2026-10-18-googlecloudtech-adk-agent-skill-design-patterns.md) | 直接源自 | 强 |
| [Agent Skills 是上下文卸载](../clips/2026-10-18-yonah-x-skills-context-offloading.md) | 直接源自 | 强 |
| [模型不动，只让技能库从用户请求里长：设计 agent 的技能从 76 个长到 139 个](../clips/2026-10-20-du-designer-rsi-procedural-memory.md) | 直接源自 | 弱（模型复核通过） |
