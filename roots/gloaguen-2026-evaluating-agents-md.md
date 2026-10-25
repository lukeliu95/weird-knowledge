---
name_zh: "评测 AGENTS.md：仓库级上下文文件对编程 agent 有没有用"
name_en: "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"
proposer: "Thibaud Gloaguen、Niels Mündler-Sasahara、Mark Niklas Müller、Veselin Raychev、Martin Vechev"
year: "2026"
type: 论文
verified: true
---

# 评测 AGENTS.md：仓库级上下文文件对编程 agent 有没有用（Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?）

## 一句话

在 SWE-bench 任务（配模型生成的上下文文件）和一批自带开发者所写上下文文件的真实仓库 issue 上测试编程 agent，发现给 AGENTS.md 这类文件总体不提高任务成功率，推理成本平均增加 20% 以上；文件里的指令会被遵守，但仓库概览没有帮助，这类文件适合写非标准的约定。

## 原始出处

- Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?，Gloaguen 等，arXiv 预印本 2602.11988，2026-02-12（DOI 10.48550/arXiv.2602.11988，DataCite 注册），https://arxiv.org/abs/2602.11988

## 更底层的源头

- [大模型很容易被无关上下文带偏](shi-2023-irrelevant-context-distraction.md) · 关系：相近
- [上下文工程](context-engineering.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [为什么 harness 加太多 AI 会迷路：删的是指示，强制机制要留](../clips/2026-10-25-hirakaw-trim-instructions-keep-enforcement.md) | 直接源自 | 强 |
