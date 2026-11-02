---
title: "Moli：Rust 写的不渲染浏览器，专给 Agent 用"
author: "Gk (@0xGky)"
url: https://x.com/0xGky/status/2117082265641779707
source: X
published: 2026-11-02 02:32 UTC
saved: 2026-11-02
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: Agent 与 Skill
roots: []
---

## 原文

有人用 Rust 从头造了个浏览器，专供 AI Agent 干活使！

一个开源项目：Moli。

以往让 Claude Code、Codex 去操作网页，动不动就得拉起 Chrome，内存吃得厉害，速度又慢。

Moli 这思路够狠：网页不用看，那就干脆不渲染！

网页抓取、JavaScript 执行、自动化操作全都支持，Playwright、CDP、WebDriver 也兼容。

项目测试里，Moli 的内存占用明显比 Chrome 低，AI 爬虫、Agent 自动化、批量网页处理用它特别合适。

往后给 AI 配浏览器，未必非得绑在 Chrome 上了。

GitHub： ⁠https://t.co/bMBjK7lrxE

> 媒体：
> - https://pbs.twimg.com/media/HWEekvWaIAA0Hja.jpg

## 溯源

