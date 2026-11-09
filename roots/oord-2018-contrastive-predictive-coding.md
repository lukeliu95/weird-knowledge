---
name_zh: "对比预测编码与 InfoNCE"
name_en: "Representation Learning with Contrastive Predictive Coding / InfoNCE"
proposer: "Aaron van den Oord、Yazhe Li、Oriol Vinyals"
year: "2018"
type: 论文
verified: true
---

# 对比预测编码与 InfoNCE（Representation Learning with Contrastive Predictive Coding / InfoNCE）

## 一句话

用真实匹配样本和负样本的对比分类学习表示；InfoNCE 在论文给定的采样假设下提供互信息下界，而不是无条件测出语义真实性。

## 原始出处

- van den Oord、Li、Vinyals，Representation Learning with Contrastive Predictive Coding，arXiv:1807.03748，初版 2018-07-10；本轮核对摘要及正文第 2.1—2.4 节，尤其第 2.3 节的 InfoNCE 目标与互信息下界。，https://arxiv.org/abs/1807.03748
- 论文正文 v2，2019-01-22 修订；未逐项复算实验或阅读全文附录。，https://arxiv.org/html/1807.03748v2
- 争议：这篇工作提出对比预测编码及命名为 InfoNCE 的目标，不等于首次发明全部对比学习；作者承认更早的对比、三元组和噪声对比估计工作。互信息下界依赖其定义与采样条件，不能据此断言所有对比模型都有校准概率。

## 更底层的源头

- [信息论](information-theory.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [CLM 把候选动作选择做成检索，作者报告特定测试最高快 9 倍](../clips/2026-11-06-dailydoseofds-contrastive-language-model-decision-as-retrieval.md) | 直接源自 | 强 |
