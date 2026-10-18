---
title: "Claude 3 Opus 整理访谈字幕"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/1769913488485253246
source: X
published: 2024-03-19 02:27 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: 提示词与写作
roots: []
---

## 原文

分享一点利用 Claude 3 Opus 整理字幕文稿的经验，它可以非常好的将文稿整理成对话形式，并且还可以按照话题分成章节！几个要点：
1. 说明对话的人物（基本上Claude能自动分辨出哪些话是谁说的，很准）
2. 要求根据话题分成章节（这个对于阅读、总结都很重要）
3. 要求不要遗漏内容（不说明可能就给你总结了）

参考 Prompt：
“以下是我整理的 XXX 对 YYY 的采访文稿，请整理成更适合阅读的对话形式，根据话题形成章节，包含人名，尊照原意的情况下适当润色，从头开始，不要遗漏任何内容！”

如果没有输出完整需要不停的输入 continue 直到结束。

如果要总结，最好等到完整文稿输出完成，然后让它基于章节来总结，这样总结出来效果最好，不容易遗漏要点。

参考 Prompt：
“请按照上面的章节总结上面的文稿，需要详尽不要遗漏重点！”

> 媒体：
> - https://pbs.twimg.com/media/GI_9ropXIAAhgve.jpg
> - https://pbs.twimg.com/media/GI_-PvOWUAErnPl.jpg
> - https://pbs.twimg.com/media/GI_-1JuWUAAa1SD.jpg

## 溯源

