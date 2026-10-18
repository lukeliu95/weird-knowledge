---
name_zh: "提示注入"
name_en: "Prompt injection"
proposer: "Jonathan Cefalu（Preamble，最早发现）；Simon Willison（推广命名）；Kai Greshake 等（间接提示注入）"
year: "2022"
type: 方法论
verified: true
---

# 提示注入（Prompt injection）

## 一句话

大模型分不清开发者给的指令和外部输入的数据，攻击者把指令藏进模型会读到的内容（网页、邮件、文档）里，就能让模型做出预期之外的事；藏在外部数据里的叫间接提示注入。

## 原始出处

- Prompt injection，英文维基百科，https://en.wikipedia.org/wiki/Prompt_injection
- Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection, Kai Greshake et al., 2023, arXiv:2302.12173，https://arxiv.org/abs/2302.12173
- 争议：维基百科：Preamble 的 Jonathan Cefalu 2022 年 5 月发现并称之为“命令注入”；“prompt injection”一词最早由推特用户 @himbodhisattva 在 2022 年 5 月使用，Simon Willison 2022 年 9 月独立提出并推广；间接提示注入由 Greshake 等 2023 年描述。

## 更底层的源头

- [代码注入](code-injection.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [腾讯 Agent 反复爬高德被抓](../clips/2026-10-18-sleepy0x13-tencent-agents-amap-scraping.md) | 直接源自 | 强 |
| [OpenAI Dots 放权指南：动作分进 6 个权限区，每周按证据升降](../clips/2026-10-18-choopyplug1-openai-dots-agent-permission-zones.md) | 直接源自 | 强 |
