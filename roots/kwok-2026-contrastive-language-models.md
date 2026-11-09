---
name_zh: "对比语言模型（候选动作检索）"
name_en: "Contrastive Language Models"
proposer: "Jacky Kwok、Hangoo Kang、Tarun Suresh、Jon Saad-Falcon、Marco Pavone、Christopher Ré、Azalia Mirhoseini"
year: "2026"
type: 方法论
verified: true
---

# 对比语言模型（候选动作检索）（Contrastive Language Models）

## 一句话

冻结语言模型编码器，用双向 InfoNCE 训练状态与动作的投影头，把给定候选动作的选择化为向量评分与检索，适合能够枚举并复用候选的场景。

## 原始出处

- CLM 官方仓库 README：方法、训练目标、缓存、动作选择和代码验证评测；本轮核对当前版本，非重建原推发布时版本。，https://github.com/Contrastive-LM/CLM
- CLM-v0.1-8B 官方模型卡：冻结 Qwen3-8B 编码器与两个投影头的模型结构，以及候选评分的适用方式。，https://huggingface.co/Contrastive-LM/CLM-v0.1-8B/blob/main/README.md
- 争议：“最高 9 倍”是官方特定比较的延迟改善，不是统一加速系数；大候选集合与可缓存动作时收益更大。另有约 1000 个缓存候选的 13 倍说明，不能混为同一设置。代码验证结果另用任务微调，不能当作通用零样本成绩；候选集概率不是自动校准的绝对置信度。官方研究博客入口本轮无法访问，未声称读到。

## 更底层的源头

- [对比预测编码与 InfoNCE](oord-2018-contrastive-predictive-coding.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [CLM 把候选动作选择做成检索，作者报告特定测试最高快 9 倍](../clips/2026-11-06-dailydoseofds-contrastive-language-model-decision-as-retrieval.md) | 直接源自 | 强 |
