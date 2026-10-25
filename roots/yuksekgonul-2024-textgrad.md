---
name_zh: "TextGrad：用文字反馈做“自动求导”"
name_en: "TextGrad: Automatic \"Differentiation\" via Text"
proposer: "Mert Yuksekgonul, Federico Bianchi, Joseph Boen, Sheng Liu, Zhi Huang, Carlos Guestrin, James Zou"
year: "2024"
type: 论文
verified: true
---

# TextGrad：用文字反馈做“自动求导”（TextGrad: Automatic "Differentiation" via Text）

## 一句话

把由多次大模型调用和工具组成的系统看成一张计算图，让大模型对输出写出文字批评（“文字梯度”），再沿计算图把批评反向传给各处的提示词、代码或答案去修改，像反向传播那样优化文字变量。

## 原始出处

- TextGrad: Automatic "Differentiation" via Text, Yuksekgonul 等, arXiv:2406.07496, 2024，https://arxiv.org/abs/2406.07496
- Optimizing generative AI by backpropagating language model feedback, Yuksekgonul 等, Nature 639: 609–616, 2025（期刊版），https://doi.org/10.1038/s41586-025-08661-4

## 更底层的源头

- [反向传播（用误差反传学习表示）](rumelhart-1986-backpropagation.md) · 关系：直接源自
- [梯度下降](gradient-descent.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [把 skill 当参数来训：别的模型读执行记录提改法，每步只许改几处，留出集上变好才收下；6 个测试集、7 个模型、3 种运行环境里 52 格全部第一或并列第一](../clips/2026-10-25-yang-skillopt-self-evolving-agent-skills.md) | 直接源自 | 强 |
