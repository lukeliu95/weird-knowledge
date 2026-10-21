---
name_zh: "逐步验证（过程监督优于结果监督）"
name_en: "Let's Verify Step by Step"
proposer: "Hunter Lightman、Vineet Kosaraju、Karl Cobbe 等（OpenAI）"
year: "2023"
type: 论文
verified: true
---

# 逐步验证（过程监督优于结果监督）（Let's Verify Step by Step）

## 一句话

比较只看最终答案的结果监督和给每一步推理打分的过程监督，发现在 MATH 难题上过程监督训练出的奖励模型明显更好（解出代表性子集 78% 的题），并公开了 80 万条步骤级人工标注 PRM800K。

## 原始出处

- Let's Verify Step by Step, Hunter Lightman et al., 2023, arXiv:2305.20050，https://arxiv.org/abs/2305.20050
- Solving math word problems with process- and outcome-based feedback, Jonathan Uesato et al.（DeepMind）, 2022, arXiv:2211.14275，https://arxiv.org/abs/2211.14275
- 争议：过程监督和结果监督的对比更早见于 DeepMind 的 Uesato 等 2022 年论文：它发现两者最终答案错误率相近，但要让推理步骤也正确，需要过程监督或模仿过程反馈的奖励模型；“过程奖励”谁最先提出说法不一。

## 更底层的源头

- [训练验证器来解数学应用题](cobbe-2021-training-verifiers.md) · 关系：直接源自
- [迈向人工智能的步骤（提出信用分配问题）](minsky-1961-steps-toward-ai.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [智谱让 GLM-5.3 自己优化推理系统](../clips/2026-10-18-dotey-glm-5-3-optimizes-own-inference.md) | 直接源自 | 弱（模型复核通过） |
