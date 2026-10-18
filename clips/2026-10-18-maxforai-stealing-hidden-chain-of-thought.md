---
title: "论文从闭源模型里偷出隐藏思维链"
author: "Max For AI (@MaxForAI)"
url: https://x.com/MaxForAI/status/2087184155461452192
source: X
published: 2026-08-11 14:27 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

刚刚，一篇可能会引起大模型圈地震的论文发表了！

研究人员第一次系统性地从 OpenAI、Anthropic、Google 的闭源模型里，大规模“偷”出了真正的隐藏思维链。

然后，他们顺手拿这些思维链去研究了 Kimi K3、GLM-5.2、DeepSeek 等一批开源模型。

结果非常有意思。

01｜原来闭源模型的 CoT，真的可以被“偷”出来

现在 OpenAI、Anthropic、Google 都越来越不愿意把完整思维链交给用户。

原因也很好理解：最终答案可以抄，真正值钱的是模型“怎么想”。

一旦完整 CoT 被批量拿走，就可以直接拿去做蒸馏，训练自己的模型。

所以现在很多 API 的做法，是把模型的 reasoning 加密以后返回给客户端。你看不到内容，但下一轮请求可以把这坨加密数据再交回模型，让它继续思考。

结果研究者发现了一个很离谱的漏洞：

这些加密思维链，在同一家厂商的不同用户、Session，甚至不同模型之间，居然可以互相兼容。

于是攻击方法简单得有点荒谬：

让最强模型思考 → 拿到加密 CoT → 扔给同厂更弱、更容易越狱的模型 → 让小模型把它解出来。

比如 Claude Opus 4.8 的隐藏思维链，可以交给 Haiku 去“念”出来。

你甚至不需要攻破 Opus，找它的小弟Haiku就行。

论文最终在 Claude、GPT、Gemini 三套 API 上都实现了隐藏 reasoning 的提取，等于直接绕过了厂商原本用来防止 CoT 蒸馏的那层保护。

> 媒体：
> - https://pbs.twimg.com/media/HPcq649aQAAXbKf.jpg

## 溯源

