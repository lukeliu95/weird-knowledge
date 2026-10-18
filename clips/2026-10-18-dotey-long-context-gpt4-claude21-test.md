---
title: "GPT-4 与 Claude 长文遗忘"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/1727454708627808261
source: X
published: 2023-11-22 22:31 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

将Greg Kamradt的两次实验：
- GPT-4-128K https://t.co/e4hBVBj7TF
- Claude 2.1 200K：https://t.co/KzG3bIWZNJ 

两次结果放一起对比，可以看到：

GPT-4-128K
1. 在上下文长度小于 73K Tokens时，不会有信息遗忘
2. 在上下文长度超出 73K 后，位于中间7%-50% 区间的信息可能会被遗忘

Claude-2.1-200K
1. 上下文长度小于24K时效果最好，几乎不会有信息遗忘
2. 上下文长度超过24K就开始变差，90K后，效果很差，一大半信息会遗忘
3. 最头部和最顶部的1%效果最好，不会被遗忘

我的总结
1. GPT-4还是最强的
2. 尽量少一些上下文，长文还是需要手动或者自动分割，GPT-4 的话，不要超过73K（输入输出加一起）
3. System Prompt 放在最前或者最后都可以，放在后面更好
4. 如果System Prompt 放在前面，对于GPT-4来说，不要超过5%，对于Claude来说不要超过1%
4. GPTs的Prompt只能放在最前面，所以不要超过不要超过5%也就是128*0.05 = 6.4 K Tokens比较好

> 媒体：
> - https://pbs.twimg.com/media/F_kl-_GXkAAKzcf.jpg
> - https://pbs.twimg.com/media/F_kmA7SXIAAjIF9.jpg

## 溯源

