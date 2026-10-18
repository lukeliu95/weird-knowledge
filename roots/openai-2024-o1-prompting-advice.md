---
name_zh: "OpenAI 推理模型提示建议（提示要简单直接、不必写思维链）"
name_en: "Advice on prompting (OpenAI reasoning models guide, later \"Reasoning best practices\")"
proposer: "OpenAI"
year: "2024"
type: 方法论
verified: true
---

# OpenAI 推理模型提示建议（提示要简单直接、不必写思维链）（Advice on prompting (OpenAI reasoning models guide, later "Reasoning best practices")）

## 一句话

OpenAI 在 2024 年 9 月发布 o1 时建议：推理模型会在内部自己推理，提示要简单直接，不必要求它“一步步思考”或“解释推理过程”，用分隔符区分输入的不同部分，检索来的资料只给最相关的。

## 原始出处

- Reasoning best practices, OpenAI API 文档（现行版本：直截了当的提示效果最好，不必让模型 think step by step），https://developers.openai.com/api/docs/guides/reasoning-best-practices
- How to prompt on OpenAI's o1, VentureBeat, 2024-09-12（报道 o1 发布时官方的四条提示建议），https://venturebeat.com/ai/how-to-prompt-on-openai-o1/
- 争议：2024 年 9 月的原始版本（Reasoning models 指南里的提示建议一节）没能打开存档逐字核对，内容依据 VentureBeat 同期报道和 OpenAI 现行文档；现行文档改名为 Reasoning best practices，内容有扩充。

## 更底层的源头

- [思维链提示](wei-2022-chain-of-thought-prompting.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [提示词精髓：有什么、做什么、怎么做](../clips/2026-10-18-dotey-prompt-context-task-how.md) | 相近 | 强 |
