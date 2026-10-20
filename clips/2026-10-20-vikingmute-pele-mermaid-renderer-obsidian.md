---
title: "Obsidian CEO 写的 Mermaid 渲染库 Pele，小 6 倍快 500 倍"
author: "Viking (@vikingmute)"
url: https://x.com/vikingmute/status/2111794162702114894
source: X
published: 2026-10-18 12:18 UTC
saved: 2026-10-20
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

Obsidian 的 CEO kepano 写了一个 Mermaid 渲染库 Pele，同样的 Mermaid 语法 输出变成可换主题的 SVG ，但是性能和大小都有绝对优势：
https://t.co/ms1qKlu3d7
gzip 后 230 kB vs Mermaid.js 的 1.6 MB 大约小 6 倍
渲染官方说最多快 500 倍
换肤是改 CSS 变量，不用重新渲染
浏览器和 node 都能跑

之后Obsidian 会用它默认渲染图，还在用 Mermaid.js 可以去试试看

> 媒体：
> - https://pbs.twimg.com/media/HU6Zl9Ga8AA_x6L.jpg

## 溯源

