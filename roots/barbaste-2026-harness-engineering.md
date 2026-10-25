---
name_zh: "外壳工程：11 个编程 agent 的源码解剖"
name_en: "Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents -- A Source-Code Study of Eleven Systems"
proposer: "Paul Barbaste、Tristan Darrigol、Germain Vu、Tom Wiltberger（Wavestone AI Lab、Inclusive Brains）"
year: "2026"
type: 论文
verified: true
---

# 外壳工程：11 个编程 agent 的源码解剖（Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents -- A Source-Code Study of Eleven Systems）

## 一句话

读 11 个编程 agent（Claude Code、Codex CLI、Gemini CLI 等）的源码，归纳出外壳的 7 个子系统和 29 种常见设计：没有一家用通用 agent 框架、没有一家用向量检索读代码，skill 普及略超 MCP（9/11 对 8/11），各家 90 天里从趋同走到照抄，外壳正从工具变成平台；附 18 条建议和约 90 行的最小外壳。

## 原始出处

- Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents -- A Source-Code Study of Eleven Systems，Barbaste 等，arXiv:2609.00006 [cs.SE]，2026-07-15，DOI 10.48550/arXiv.2609.00006，https://arxiv.org/abs/2609.00006
- 争议：arXiv 预印本，未经同行评审；只读源码不做实验，跑分是各家自报；Claude Code 部分基于 2026 年 3 月流出的源码快照。库里已有这篇论文本身的新知识（clips/2026-10-25-barbaste-harness-engineering-eleven-coding-agents.md）。

## 更底层的源头

- [外壳工程（agent = 模型 + 外壳）](harness-engineering.md) · 关系：直接源自
- [构建高效的智能体](anthropic-2024-building-effective-agents.md) · 关系：直接源自
- [ReAct：推理与行动协同](yao-2022-react.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Wavestone 拆了 11 个编程 agent 的源码：每个都要在同样 7 个子系统上做取舍（推文转述，“90 行外壳覆盖全部 7 个部件”是说错的）](../clips/2026-10-25-arindam-1729-seven-building-blocks-of-coding-agents.md) | 直接源自 | 强 |
