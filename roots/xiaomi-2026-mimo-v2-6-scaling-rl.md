---
name_zh: "MiMo-V2.6：扩展强化学习走向自我改进"
name_en: "MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement"
proposer: "小米 LLM-Core 团队"
year: "2026"
type: 论文
verified: true
---

# MiMo-V2.6：扩展强化学习走向自我改进（MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement）

## 一句话

小米的技术报告：先在多模态语料上做中期训练扩大探索空间，再从批量吞吐、环境多样性、评分算力三个方向扩展强化学习算力；多类任务在一次异步运行里混合训练，难验证的任务另训老师再用 MOPD 合并，并开源任务环境、强化学习框架和蒸馏出的 Qwen 9B 小模型。

## 原始出处

- MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement, Xiaomi LLM-Core Team, 2026 (arXiv 2610.11959)，https://arxiv.org/abs/2610.11959
- 争议：推文说的“MixRL”在报告里叫混合任务强化学习（mixed-task RL），没出现 MixRL 这个词；推文说 7K 个环境，报告表 5 写的是约 7 千个任务（代码 3k、网安 1k、通用 1k、视觉 2k）。报告里的数字是团队自报。

## 更底层的源头

- [DeepSeekMath 论文（提出 GRPO 算法）](shao-2024-deepseekmath-grpo.md) · 关系：直接源自
- [MOPD：多教师在线策略蒸馏](ma-2026-mopd.md) · 关系：直接源自
- [知识蒸馏](knowledge-distillation.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [MiMo-V2.6 的强化学习之路](../clips/2026-10-18-luofuli-mimo-v2-6-scaling-rl.md) | 直接源自 | 强 |
