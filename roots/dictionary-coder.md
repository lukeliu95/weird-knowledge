---
name_zh: "字典编码（替换编码）"
name_en: "Dictionary coder"
proposer: "无单一提出者；自适应字典编码以 Jacob Ziv 与 Abraham Lempel 的 LZ77、LZ78 为代表"
year: "1977"
type: 方法论
verified: true
---

# 字典编码（替换编码）（Dictionary coder）

## 一句话

一类无损压缩方法：在文本里找出和“字典”里相同的字符串，换成它在字典里的编号；字典可以事先定好（静态字典），也可以边压缩边建。

## 原始出处

- Dictionary coder，英文维基百科，https://en.wikipedia.org/wiki/Dictionary_coder
- A universal algorithm for sequential data compression，Jacob Ziv & Abraham Lempel，IEEE Transactions on Information Theory，1977，https://doi.org/10.1109/tit.1977.1055714
- 争议：维基没写静态字典编码的最早提出者；1977 年是 LZ77 发表的年份，并非字典编码思想本身的起点。

## 更底层的源头

- [信息论](information-theory.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [成语是哈希表而不是压缩](../clips/2026-10-18-dotey-chengyu-hash-table-idea.md) | 挑战 | 弱（模型复核通过） |
