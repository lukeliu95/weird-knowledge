---
name_zh: "GSM1k：用没公开的新题检验大模型数学成绩是不是背出来的"
name_en: "A Careful Examination of Large Language Model Performance on Grade School Arithmetic"
proposer: "Hugh Zhang、Jeff Da、Summer Yue 等（Scale AI）"
year: "2024"
type: 论文
verified: true
---

# GSM1k：用没公开的新题检验大模型数学成绩是不是背出来的（A Careful Examination of Large Language Model Performance on Grade School Arithmetic）

## 一句话

仿照 GSM8K 的风格和难度请人新写 1205 道小学数学题（GSM1k），保证不在任何训练数据里且暂不公开；部分模型在新题上掉分最多 8%，掉分多少和模型能否复述 GSM8K 原题正相关，说明一些模型背过公开测试集，但前沿模型掉分很小。

## 原始出处

- A Careful Examination of Large Language Model Performance on Grade School Arithmetic，Zhang 等，arXiv:2405.00332（v4，NeurIPS 2024 数据集与基准赛道），2024，https://arxiv.org/abs/2405.00332
- 争议：第一版写的是最多掉 13%，修订后的 v4 改为最多 8%，引用时注明版本。

## 更底层的源头

- [可复用的留出集（自适应数据分析中的泛化与留出集复用）](dwork-2015-reusable-holdout.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [作者称：微调 Qwen 在自家任务上追平前沿模型，靠私有测试集验证（未公开细节）](../clips/2026-11-18-simonhoiberg-private-benchmark-fine-tuned-qwen.md) | 相近 | 弱（模型复核通过） |
