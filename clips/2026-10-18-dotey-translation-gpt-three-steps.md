---
title: "翻译 GPT 改成直译找问题意译三步"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/1737627478007456183
source: X
published: 2023-12-21 00:14 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: 提示词与写作
roots: []
---

## 原文

我最近对我的翻译 GPT https://t.co/WDvGUzZqFS 做了一点优化，将原来的直译->意译两步拆成了三步：
1. 直译
2. 指出直译中的问题，例如：“不符合中文表达习惯”、“语句不通顺”和“晦涩难懂”，并且指出位置或者给出解释
3. 根据直译和问题进行意译

经过我几天的测试下来，效果确实要更好，因为通过指出问题，可以将问题具体化，由于提供了更多上下文，得到了更好的结果。

举一个例子，我翻译的一段英文其中有这样一句话：“I enjoy writing. I do it in a fast way. Why am I even a researcher if I don’t write my own research?”

之前用两步，意译后得到的结果是：“我热爱写作，写得也很迅速。如果我不亲自完成我的研究写作，我还算什么研究员呢？”（参考图二）

新的Prompt中，在第二步中发现了问题，指出：
> 第一段中，“I do it in a fast way” 直译为 “我写得很快” 可能不够准确，原句的含义可能更接近于“我享受写作，这是一种迅速的表达方式”。

最后意译时给出了翻译：
> “我喜欢写作，这是我快速表达思维的方式。如果我连自己的研究都不亲自写，我还算什么研究者？”

可以对比“I do it in a fast way.”部分的翻译结果：
“我热爱写作，写得也很迅速。” 
vs
“我喜欢写作，这是我快速表达思维的方式。”

可以看到翻译质量确实有提升。当然缺点是更费 Token 了一些，往好处想想少了更多人工校对的时间！

更新后Prompt见评论

> 媒体：
> - https://pbs.twimg.com/media/GB1ISBvXkAAoVdp.jpg
> - https://pbs.twimg.com/media/GB1JrhnX0AAH_tV.jpg
> - https://pbs.twimg.com/media/GB1KqENXIAAhePI.jpg

## 溯源

