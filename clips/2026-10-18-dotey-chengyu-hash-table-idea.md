---
title: "成语是哈希表而不是压缩"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/1811276890788753899
source: X
published: 2024-07-11 05:50 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 思维与成长
roots: [hash-table, commercial-code-communications, dictionary-coder, high-context-and-low-context-cultures]
---

## 原文

中文成语之类不算是压缩，而是一种哈希表，让你记住键值对，然后只保留键。也可以说是中文密码本，成语就是密码，成语故事就是密码对应的内容，我们从小就要背密码本所以一看密码就知道对应的内容 https://t.co/LYNngAH3pe

> 媒体：
> - https://pbs.twimg.com/media/GSLyTldWYAA--kL.png
> - https://pbs.twimg.com/media/GSLyYbLW4AAm8N0.png
> - https://pbs.twimg.com/media/GSLyacSW0AA7H-V.png
> - https://pbs.twimg.com/media/GSLye3sXIAAFHog.png

## 溯源

- 核心主张：成语能用四个字表达一大段意思，不是把内容塞进了这四个字，而是大家从小背熟了“成语→故事”的对照表，四个字只是查表用的键。
- 源知识：
  - [哈希表（散列表）](../roots/hash-table.md) · 关系：直接源自 · 强弱：强。作者明说成语是“一种哈希表”：记住键值对，只保留键，用键去取值
  - [电报商用密码本](../roots/commercial-code-communications.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。作者说的“中文密码本”和 19 世纪的电报商用密码本几乎是同一个机制：公开出版的码本把一整句话对应成一个词，收发双方都有这本书就能还原
  - [字典编码（替换编码）](../roots/dictionary-coder.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。信息论里，收发双方事先共享一本字典、只传条目编号，本身就算无损压缩（静态字典编码），维基也把电报密码本称为一种数据压缩；所以“哈希表”和“压缩”并不矛盾，区别只在字典是事先背好的
  - [高语境文化与低语境文化](../roots/high-context-and-low-context-cultures.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。成语的意思不在字面上，而在双方共有的文化背景里，这正是霍尔说的高语境沟通：大量信息放在语境里，不明说
- 本质：这条新知识本质上是“共享密码本、只传索引”（字典编码）在汉语成语场景下的应用：省下的长度全靠双方事先背好的那本字典，没有字典，四个字什么也传不过去。
- 整理于：2026-10-18（第 2 轮）
