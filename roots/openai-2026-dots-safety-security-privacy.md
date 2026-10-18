---
name_zh: "OpenAI dots 的安全设计（《我们如何将安全性、信息安全和隐私保护融入 dots》及帮助中心）"
name_en: "How we build safety, security, and privacy into dots"
proposer: "OpenAI"
year: "2026"
type: 研究报告
verified: true
---

# OpenAI dots 的安全设计（《我们如何将安全性、信息安全和隐私保护融入 dots》及帮助中心）（How we build safety, security, and privacy into dots）

## 一句话

OpenAI 对常驻 agent dots 的官方安全设计：模型训练守规矩；每个 dot 一台隔离的云电脑；安全登录不让密码进模型；空闲时的主动研究只给只读工具（用代码强制）；动作规则分直接做、每次确认、交回给你（改密码、转账必须交回）；自定义规则只能在内置保护之内调整；执行前由独立的自动审核检查；工作中读到的外部内容不授予权限；官方承认 dot 仍会出错，重要的事要人审。

## 原始出处

- How we build safety, security, and privacy into dots，OpenAI，2026-09-29，https://openai.com/index/how-we-build-safety-security-and-privacy-into-dots/
- Introducing dots（dots 发布文），OpenAI，2026-09-29，https://openai.com/index/introducing-dots/
- Dots privacy, security, and safety FAQs，OpenAI 帮助中心，2026，https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs
- Getting started with your dot，OpenAI 帮助中心，2026，https://help.openai.com/en/articles/20001530-getting-started-with-your-dot

## 更底层的源头

- [纵深防御](defense-in-depth.md) · 关系：直接源自
- [最小权限原则](principle-of-least-privilege.md) · 关系：相近
- [人在环中](human-in-the-loop.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [OpenAI Dots 放权指南：动作分进 6 个权限区，每周按证据升降](../clips/2026-10-18-choopyplug1-openai-dots-agent-permission-zones.md) | 直接源自 | 强 |
| [常驻 agent 的 6 层结构（推文作者据 OpenAI 资料自制的 PDF）](../clips/2026-10-18-choopyplug1-openai-always-on-agent-six-layers.md) | 直接源自 | 强 |
