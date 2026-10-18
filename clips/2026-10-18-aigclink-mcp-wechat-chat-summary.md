---
title: "MCP微信群聊总结工具chatsum"
author: "AIGCLINK (@aigclink)"
url: https://x.com/aigclink/status/1898284840472264763
source: X
published: 2025-03-08 08:09 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

牛，基于MCP协议实现的微信机器人和消息总结工具：mcp-server-chatsum

解决你微信群消息太多没时间处理的问题
你可以问它，“今天早上大家都在聊啥？”、  “关于MCP最近有哪些讨论？”

方案：
1. 用Wechaty在本地运行微信机器人，实时收集微信消息并存储在本地文件中，解决隐私问题

2. 在本地运行一个mcp-server-chatsum程序，接收查询请求，从本地文件中返回匹配的微信消息（支持按群名、联系人、话题等条件查询）

3. 用Claude桌面版作为交互入口，随时查询和总结微信消息，由Claude桌面版与本地的mcp-server-chatsum进程通信，再由Claude内置的大模型完成总结回复

代码@idoubicc大佬已开源，下条见链接

> 媒体：
> - https://pbs.twimg.com/media/GlgN_YcbQAA8l8S.jpg

## 溯源

