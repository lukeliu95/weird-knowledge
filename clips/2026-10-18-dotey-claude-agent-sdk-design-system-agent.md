---
title: "用 Agent SDK 做设计系统智能体"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/1973937260220330005
source: X
published: 2025-10-03 02:24 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: Agent 与 Skill
roots: []
---

## 原文

如果你想开发一个 Agent，无论你是打算做 CLI 还是做 Web 还是 Windows，都可以考虑使用 Claude Agent SDK，和 Claude Code 共享的底层代码，Claude Code 就是基于它之上加了个 CLI 的 UI，也就是说你完全可以基于它写一个 Claude Code 出来。

我昨天帮朋友花了几个小时就实现了个简单的 Agent，实现了输入提示词，就可以基于某个没训练的 Design System 写一套 UI 出来。

他写的这个 Agent 原理很简单，就是把这套设计系统的所有 Markdown 文档（几百个）放到一个它可以访问的目录，然后在 Systme Prompt 里面引导它去检索这个文档目录。

当用户输入提示词或者 Screenshot 要做一个 UI，Agent 就根据提示词规划可能要用到的组件，然后用 SDK 自带的 GREP 工具去检索文档库找到这些组件的 API，最后基于收集到的信息用这个 Design System 组件生成页面。

这个 SDK API 很简单，但很强大，你不止是可以用它内置的工具（Task、Grep、WebFetch 等等），你还可以添加自己的工具，还可以用 MCP。并且它可以把整个交互的结果通过 API 让你可以获取到原始的请求和返回消息，这样你可以自己实现一套比 CLI 更好用的交互 UI。

当然这个局限也有：
1. 只能用 Claude 模型兼容的 API，如果你想用 GPT-5 之类模型，估计效果不会太好
2. 只支持 Python 和 TypeScript
3. Tokens 消耗飞快

如果你只是做前期的 POC，强烈建议你试试。

## 溯源

