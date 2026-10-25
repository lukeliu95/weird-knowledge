---
name_zh: "Vercel：我们删掉了 agent 八成的工具"
name_en: "We removed 80% of our agent's tools"
proposer: "Andrew Qu（Vercel）"
year: "2025"
type: 研究报告
verified: true
---

# Vercel：我们删掉了 agent 八成的工具（We removed 80% of our agent's tools）

## 一句话

Vercel 内部的文本转 SQL agent d0 原有 17 个专用工具和大量提示工程，改成主要让模型用 bash 直接读语义层文件后，在 5 个代表性问题上成功从 4/5 升到 5/5，平均耗时从 274.8 秒降到 77.4 秒，token 少约 37%；作者的结论是“我们在给本来就读得懂的东西写摘要工具”，前提是底层文档本身写得清楚。

## 原始出处

- We removed 80% of our agent's tools，Andrew Qu，Vercel 博客，2025-12-22，https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools
- 争议：厂商博客，只测了 5 题。正文说剥到只剩“执行 bash”一个工具，示例代码里却有执行命令和执行 SQL 两个工具；引用者（如 y-hirakaw）说的“17 个减到 2 个”取的是代码里的数。

## 更底层的源头

- [苦涩的教训](bitter-lesson.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [为什么 harness 加太多 AI 会迷路：删的是指示，强制机制要留](../clips/2026-10-25-hirakaw-trim-instructions-keep-enforcement.md) | 直接源自 | 强 |
