---
name_zh: "多样性预测定理（集成的分歧分解）"
name_en: "Diversity prediction theorem (ambiguity decomposition)"
proposer: "Scott E. Page（命名，用于人群）；Anders Krogh、Jesper Vedelsby（在神经网络集成里给出同一恒等式）"
year: "2007"
type: 定律
verified: true
---

# 多样性预测定理（集成的分歧分解）（Diversity prediction theorem (ambiguity decomposition)）

## 一句话

对数值估计取平均时，群体的平方误差 = 成员的平均平方误差 − 成员预测之间的离散程度（多样性）；所以群体一定不比成员平均差，但要群体更准，得在不抬高个人误差的前提下增加多样性。

## 原始出处

- The Difference: How the Power of Diversity Creates Better Groups, Firms, Schools, and Societies, Scott E. Page, Princeton University Press, 2007（De Gruyter 电子版 DOI 记为 2008），https://doi.org/10.1515/9781400830282
- Neural Network Ensembles, Cross Validation, and Active Learning, Anders Krogh & Jesper Vedelsby, Advances in Neural Information Processing Systems 7 (NIPS 1994，1995 年出版), pp. 231–238，https://proceedings.neurips.cc/paper/1994/hash/b8c37e33defde51cf91e1e03e51657da-Abstract.html
- Wisdom of the crowd，英文维基百科（引 Page：集体预测的平方误差等于平均平方误差减去预测多样性），https://en.wikipedia.org/wiki/Wisdom_of_the_crowd
- 争议：同一个数学恒等式 Krogh & Vedelsby 早在 NIPS 7（会议 1994 年、出版 1995 年）就作为集成的“分歧分解”发表；Page 2007 年把它命名为多样性预测定理并用到人群上。Krogh & Vedelsby 原文 PDF 是扫描版，本次没有逐字核对公式，公式形式依据多份二手资料。只对平方误差严格成立，换成多数投票分类不再是这个等式。

## 更底层的源头

- [偏差-方差权衡](bias-variance-tradeoff.md) · 关系：相近
- [集成学习](ensemble-learning.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [用多个大模型"群体投票"预测未来时，按推理方式聚类、每类只挑 1 个代表，3 个模型就比 25 个全投票略准，调用少 88%、花费约省 80%；故意挑最不一样的反而更差](../clips/2026-10-25-chetlapalli-diverse-by-reasoning-llm-crowds.md) | 相近 | 弱（模型复核通过） |
