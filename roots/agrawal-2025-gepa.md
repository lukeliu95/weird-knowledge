---
name_zh: "GEPA：反思式提示词进化（遗传 + 帕累托）"
name_en: "GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning"
proposer: "Lakshya A Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems 等 17 人（含 Christopher Potts、Ion Stoica、Dan Klein、Matei Zaharia、Omar Khattab）"
year: "2025"
type: 论文
verified: true
---

# GEPA：反思式提示词进化（遗传 + 帕累托）（GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning）

## 一句话

让大模型读系统的执行轨迹（推理、工具调用和返回），用自然语言诊断问题、改写提示词并试跑，在自己历次尝试的帕累托前沿上挑候选、合并互补的经验；作者报告在 6 个任务上平均比 GRPO 强化学习高 6%，试跑次数最多少 35 倍。

## 原始出处

- GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning, Agrawal 等, arXiv:2507.19457, 2025，https://arxiv.org/abs/2507.19457
- 代码 gepa-ai/gepa，https://github.com/gepa-ai/gepa

## 更底层的源头

- [演化算法](evolutionary-algorithm.md) · 关系：直接源自
- [帕累托效率（帕累托改进）](pareto-efficiency.md) · 关系：直接源自
- [Reflexion：用语言反思做强化（不改模型权重）](shinn-2023-reflexion.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [把 skill 当参数来训：别的模型读执行记录提改法，每步只许改几处，留出集上变好才收下；6 个测试集、7 个模型、3 种运行环境里 52 格全部第一或并列第一](../clips/2026-10-25-yang-skillopt-self-evolving-agent-skills.md) | 相近 | 强 |
