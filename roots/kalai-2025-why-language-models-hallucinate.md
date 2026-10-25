---
name_zh: "语言模型为什么会幻觉"
name_en: "Why Language Models Hallucinate"
proposer: "Adam Tauman Kalai, Ofir Nachum, Edwin Zhang（OpenAI）, Santosh S. Vempala（佐治亚理工）"
year: "2025"
type: 论文
verified: true
---

# 语言模型为什么会幻觉（Why Language Models Hallucinate）

## 一句话

幻觉不神秘，本质上是二分类错误：分不清对错的地方，预训练自然会产生看似合理的错话；它一直消不掉，是因为多数评测只算答对率、不扣乱猜的分，模型被训练成“不确定也要猜”的应试者。作者主张改评分规则，在题目里写明置信门槛 t（只在把握超过 t 时作答，答错扣 t/(1−t) 分，答“不知道”得 0 分）。

## 原始出处

- Why Language Models Hallucinate, Kalai, Nachum, Vempala, Zhang, arXiv:2509.04664, 2025（置信门槛见第 4.2 节），https://arxiv.org/abs/2509.04664
- 前作：Calibrated Language Models Must Hallucinate, Kalai & Vempala, STOC 2024, pp. 160–171，https://doi.org/10.1145/3618260.3649777

## 更底层的源头

- [Chow 拒识规则：识别错误率与拒识率的最优权衡](chow-1970-reject-option.md) · 关系：相近
- [现代神经网络的校准（温度缩放）](guo-2017-calibration.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [宝玉的 Jev 科普视频：只做选择题、按把握深浅涂答题卡的模型，为什么快、为什么便宜、"幻觉率为零"怎么来的、会在哪儿涂错](../clips/2026-10-25-dotey-jev-answer-sheet-explainer.md) | 相近 | 弱（模型复核通过） |
