---
name_zh: "CPU-ARC：把推理过程缓存成可在 CPU 上复用的代码"
name_en: "CPU-ARC: Agentic Reasoning Caching for on-CPU Reasoning Reuse"
proposer: "Peter Belcak、Greg Heinrich、Saurav Muralidharan、Shizhe Diao、Pavlo Molchanov（NVIDIA）"
year: "2026"
type: 论文
verified: true
---

# CPU-ARC：把推理过程缓存成可在 CPU 上复用的代码（CPU-ARC: Agentic Reasoning Caching for on-CPU Reasoning Reuse）

## 一句话

让 Claude Opus 4.5 把一次解题的推理记录改写成带参数的小 Python 函数，遇到换说法、换数字的同类题先在 CPU 上跑这些函数（只在抽取数值等小事上调用微调过的 Llama 3.2 1B），没命中再交回大模型；8 个数学和科学测试里 7 个准确率不低于原模型，每次调用便宜 16～291 倍，但构建一次要花原模型 12～84 倍。

## 原始出处

- CPU-ARC: Agentic Reasoning Caching for on-CPU Reasoning Reuse，Belcak 等，arXiv:2611.09891，2026-11-06（表 2、第 3.4–3.6 节），https://arxiv.org/abs/2611.09891
- 争议：准确率是在建缓存用的同一道题上算的，构建时根函数要对照原始推理和金标答案检查（第 2.2.1 节），所以「缓存比原模型准」部分来自构建时用了金标；改写题的标准答案由 Opus 4.5 生成、2 个 Opus 评委一致通过，不是人工核对；扰动测试只在缓存已答对的题上做。AIME 的 93.3% 对 83.3% 按百分比推算约是 30 题里差 3 题（推算，论文没写题数）。

## 更底层的源头

- [记忆化（备忘函数）](memoization.md) · 关系：相近
- [基于解释的学习（解释泛化）](explanation-based-learning.md) · 关系：相近
- [案例推理（基于案例的推理）](case-based-reasoning.md) · 关系：相近
- [FrugalGPT：用级联大模型省钱又提效](chen-2023-frugalgpt.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [NVIDIA 论文：推理一次转成 CPU 代码，同类题每次调用便宜 16～291 倍（构建要花 12～84 倍）](../clips/2026-11-23-rohanpaul-ai-nvidia-reasoning-to-cpu-code.md) | 直接源自 | 强 |
