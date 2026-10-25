---
name_zh: "BALD：按分歧做贝叶斯主动学习"
name_en: "Bayesian Active Learning for Classification and Preference Learning"
proposer: "Neil Houlsby, Ferenc Huszár, Zoubin Ghahramani, Máté Lengyel"
year: "2011"
type: 论文
verified: true
---

# BALD：按分歧做贝叶斯主动学习（Bayesian Active Learning for Classification and Preference Learning）

## 一句话

挑最值得去问的样本时，看“预测结果和模型参数之间的互信息”：总的预测不确定 = 不同参数假设之间的分歧（问了能消掉）+ 每个假设下本来就有的随机（问了也消不掉）；只去问前一种大的地方。

## 原始出处

- Bayesian Active Learning for Classification and Preference Learning, Houlsby, Huszár, Ghahramani, Lengyel, arXiv:1112.5745, 2011，https://arxiv.org/abs/1112.5745
- 争议：用互信息挑样本的思路更早来自贝叶斯实验设计（如 Lindley 1956、MacKay 1992）；BALD 这个名字和“按分歧”的写法出自本文。前半句是模型按记忆写的，没逐一核对。

## 更底层的源头

- [信息论](information-theory.md) · 关系：直接源自
- [主动学习](active-learning-machine-learning.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [agent 拿不准时先分清该问用户还是该自己查：约九成缺的信息系统里就查得到，只有一成要问人；按来源分流后成功率更高、步数更少](../clips/2026-10-25-li-clarify-user-or-verify-world.md) | 直接源自 | 强 |
