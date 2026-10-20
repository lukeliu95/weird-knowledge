---
name_zh: "AIDE：按例探索的交互式数据探索"
name_en: "Explore-by-Example: An Automatic Query Steering Framework for Interactive Data Exploration (AIDE)"
proposer: "Kyriaki Dimitriadou、Olga Papaemmanouil、Yanlei Diao"
year: "2014（期刊扩展版 2016）"
type: 论文
verified: true
---

# AIDE：按例探索的交互式数据探索（Explore-by-Example: An Automatic Query Steering Framework for Interactive Data Exploration (AIDE)）

## 一句话

用户写不出查询时，系统挑样本请他标“相关/不相关”，用分类器学出他要的数据区域再翻译成查询；挑样本分三步：去没探索过的区域广撒样本找新的相关对象、在被误判的样本附近补采、在已发现区域的边界附近细化。

## 原始出处

- Explore-by-Example: An Automatic Query Steering Framework for Interactive Data Exploration，Dimitriadou, Papaemmanouil & Diao，SIGMOD 2014: 517–528，https://doi.org/10.1145/2588555.2610523
- AIDE: An Active Learning-Based Approach for Interactive Data Exploration，同三位作者，IEEE TKDE 28(11): 2842–2856，2016（读了第 3 节三个探索阶段），https://doi.org/10.1109/TKDE.2016.2599168
- TKDE 2016 作者主页免费全文，https://people.cs.umass.edu/~yanlei/publications/tkde2016-aide.pdf

## 更底层的源头

- [主动学习](active-learning-machine-learning.md) · 关系：直接源自
- [相关性反馈](relevance-feedback.md) · 关系：直接源自
- [按例查询](query-by-example.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [问题协商：用户说不清想找哪类企业时，先给样本，再陪他把问题说清](../clips/2026-10-19-luke-question-negotiation-icp-search.md) | 直接源自 | 强 |
