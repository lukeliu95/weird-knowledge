---
title: "Qwen 模型解码最快的上下文长度"
author: "Andy Stewart (@manateelazycat)"
url: https://x.com/manateelazycat/status/2099831903985803305
source: X
published: 2026-09-15 12:05 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: 模型与本地部署
roots: []
---

## 原文

这几天在做精细化的 AI 模型移植，发现一个特别有趣的现象

Qwen 3.8 Flash Next 的甜品区是 265K 的上下文，它的解码速度最快

Qwen 3.8 27B 的甜品区，不是 265K，也不是 900K，反而是 512K 的时候，它的解码速度最快

这个测试结果是非常有意思的，分享给大家，赶快去把你的上下文调到最优的值吧😎 https://t.co/EGTMUpOE4R

> 媒体：
> - https://pbs.twimg.com/media/HSQZ-2gaoAAF1eK.jpg

## 溯源

