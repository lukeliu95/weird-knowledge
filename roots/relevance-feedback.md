---
name_zh: "相关性反馈"
name_en: "Relevance feedback"
proposer: "J. J. Rocchio（Salton 的 SMART 检索系统）"
year: "1965（技术报告）/1971（正式出版）"
type: 方法论
verified: true
---

# 相关性反馈（Relevance feedback）

## 一句话

检索系统先给出一批结果，让用户标出哪些相关、哪些不相关，再用这些标记修正查询，一轮轮逼近用户真正要找的东西。

## 原始出处

- Relevance feedback in information retrieval, J. J. Rocchio, 1971, in The SMART Retrieval System（Stanford IR 教材对 Rocchio 1971 算法的说明），https://nlp.stanford.edu/IR-book/html/htmledition/the-rocchio71-algorithm-1.html
- Relevance feedback in image retrieval: A comprehensive review, Xiang Sean Zhou & Thomas S. Huang, 2003，https://doi.org/10.1007/s00530-002-0070-3
- Relevance feedback, Wikipedia，https://en.wikipedia.org/wiki/Relevance_feedback
- 争议：Rocchio 的算法最早是 1965 年哈佛计算实验室的技术报告，1971 年收入 Salton 主编的 SMART 文集；维基百科没有写明谁最先提出相关性反馈这个思路。

## 更底层的源头

- [控制论](cybernetics.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [AIDE：让用户给样本打"相关/不相关"，用主动学习猜出他真正想查的数据](../clips/2026-10-18-dimitriadou-aide-active-learning-data-exploration.md) | 直接源自 | 强 |
| [ASK：信息需求本来就说不准，系统应先给结果并解释为什么选它，再问用户反馈](../clips/2026-10-19-belkin-ask-information-retrieval.md) | 相近 | 强 |
| [对话式搜索的理论框架：帮用户说出需要、给有边界的选项、记住他否掉的条件](../clips/2026-10-19-radlinski-conversational-search-framework.md) | 直接源自 | 强 |
| [问一个好的澄清问题效果能翻倍，但那是理想上限，真实模型只提高三四成，问错还会变差](../clips/2026-10-19-aliannejadi-asking-clarifying-questions-qulac.md) | 相近 | 弱（待 Luke 确认） |
