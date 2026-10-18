---
title: "用 REA 拆解 Codex 的评论标记"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/2109417222724600172
source: X
published: 2026-10-11 22:53 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: 编程智能体
roots: []
---

## 原文

再贡献一个 REA 用法，在不需要你去反编译 Codex 代码的情况下搞懂它一些运行逻辑。

这次我是想搞明白 Codex 是怎么在内置浏览器上标记发评论的，如果知道这个，也许我可以在自己网页上往输入框发消息。

我之前已经安装好了 REA，所以我给 Codex 发了一条消息：
> Use REA 帮我分析下， Codex/ChatGPT App 中，浏览器的标记，然后附加标记内容到 composer 是如何实现的？发送的消息是什么？
> 告诉我需要怎么配合

注意我发了一句：“告诉我需要怎么配合”，这样我可以辅助做一些事帮助它分析。

然后它去查看 Electron App 的原始代码，找到了关键链路（虽然我也不知道它怎么找到的），中间我配合发了一次消息。

分析完了我想验证一下，继续让它帮我做一个测试网页，让我可以测试一下是不是可以给 Codex 输入框发送消息，于是 Codex 帮我做了一个网页，没能直接往输入框附加评论，但是可以弹出评论框，可以帮你填充输入内容，原来 OpenAI 本来就提供了 API 只是我一直不知道。

document.oai.annotation.request() https://t.co/W1KCSfc99E 

继续让它分析了 Cursor 和 Claude Code，可惜它们不支持这样的 API。

> 媒体：
> - https://pbs.twimg.com/media/HUYmEKZXIAAcnjW.jpg
> - https://pbs.twimg.com/media/HUYmuEiWwAEbqW0.jpg
> - https://pbs.twimg.com/media/HUYnL7eWwAIwend.jpg
> - https://pbs.twimg.com/media/HUYnpzkXEAAM1yo.jpg

## 溯源

