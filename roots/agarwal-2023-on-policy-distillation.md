---
name_zh: "在线策略蒸馏（GKD：从自己犯的错里学）"
name_en: "On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes"
proposer: "Rishabh Agarwal 等（Google DeepMind）"
year: "2023"
type: 论文
verified: true
---

# 在线策略蒸馏（GKD：从自己犯的错里学）（On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes）

## 一句话

让学生模型在自己生成的输出上接受老师模型的反馈来学，解决“训练时看老师的答案、推理时却要接着自己的输出往下写”的分布不一致问题。

## 原始出处

- On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes, Rishabh Agarwal et al., 2023 (arXiv 2306.13649, ICLR 2024)，https://arxiv.org/abs/2306.13649
- On-Policy Distillation, Kevin Lu / Thinking Machines Lab, 2025-10-27，https://thinkingmachines.ai/blog/on-policy-distillation/
- 争议：同期 Gu 等的 MiniLLM 也做学生自采样的蒸馏；MiMo-V2-Flash 报告把 MiniLLM、这篇和 Thinking Machines 的博文一起列为在线策略蒸馏的来源。

## 更底层的源头

- [知识蒸馏](knowledge-distillation.md) · 关系：直接源自
- [模仿学习（行为克隆）](imitation-learning.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Meta 的 MIMESIS：用真人行为训练的用户模拟器，比让助手模型扮用户更好练 agent](../clips/2026-10-20-dair-ai-mimesis-user-simulator.md) | 相近 | 弱（模型复核通过） |
