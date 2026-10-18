---
name_zh: "MOPD：多教师在线策略蒸馏"
name_en: "MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training"
proposer: "小米 MiMo 团队（专文第一作者 Wenhan Ma，作者含 Fuli Luo）"
year: "2026"
type: 论文
verified: true
---

# MOPD：多教师在线策略蒸馏（MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training）

## 一句话

先给每个领域单独用强化学习训一个老师模型，再让学生模型用自己的采样、由各领域老师逐词打分来蒸馏，把多种能力合进一个模型，几乎不丢老师的水平。

## 原始出处

- MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training, Wenhan Ma et al., 2026 (arXiv 2606.30406)，https://arxiv.org/abs/2606.30406
- MiMo-V2-Flash Technical Report, Xiaomi LLM-Core Team, 2026 (arXiv 2601.02780)，https://arxiv.org/abs/2601.02780
- 争议：MOPD 最早在 2026 年 1 月的 MiMo-V2-Flash 技术报告里提出，2026 年 6 月才有专文；专文把混合强化学习（Mix-RL）当对比基线并报告 MOPD 更好，而这条推文说两者不冲突、各管一类任务。

## 更底层的源头

- [在线策略蒸馏（GKD：从自己犯的错里学）](agarwal-2023-on-policy-distillation.md) · 关系：直接源自
- [知识蒸馏](knowledge-distillation.md) · 关系：直接源自
- [强化学习](reinforcement-learning.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [MiMo-V2.6 的强化学习之路](../clips/2026-10-18-luofuli-mimo-v2-6-scaling-rl.md) | 直接源自 | 强 |
