---
title: "Playwright MCP 入门例子"
author: "Jason Zhou (@jasonzhouu)"
url: https://x.com/jasonzhouu/status/1900220497247543737
source: X
published: 2025-03-13 16:20 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

mcp-playwright

这个比较简单，很适合入门了解MCP server的构建，创建的server提供了这么几种情况：
- list resource
- read resource
- list tools
- call tool

resource用于提供资源，比如截图、浏览器控制台的日志；
tools提供各种功能，比如导航、点击、填写表单之类的；

MCP server需要给LLM提供它的功能的列表，类似于API文档，对每一个功能和参数都需要做文字介绍；
以及通过调用外部资源去实现这些功能，这里就是调用playwright进行一些浏览器操作。

## 溯源

