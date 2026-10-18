---
name_zh: "大模型当验证器"
name_en: "LLM-as-a-Verifier: A General-Purpose Verification Framework"
proposer: "Jacky Kwok, Shulu Li, Pranav Atreya, Yuejiang Liu, Yixing Jiang, Chelsea Finn, Marco Pavone, Ion Stoica, Azalia Mirhoseini"
year: "2026"
type: 论文
verified: true
---

# 大模型当验证器（LLM-as-a-Verifier: A General-Purpose Verification Framework）

## 一句话

把“验证”当成新的扩展维度：对模型输出的打分 token 按概率求期望，得到连续分数，再按分数从多个候选里挑最优；作者报告在 Terminal-Bench V2 等榜单上拿到最好成绩。

## 原始出处

- LLM-as-a-Verifier: A General-Purpose Verification Framework, Kwok et al., 2026，https://arxiv.org/abs/2607.05391
- Stanford Scaling Intelligence Lab 项目页，https://scalingintelligence.stanford.edu/pubs/llm_as_a_verifier/

## 更底层的源头

- [训练验证器来解数学应用题](cobbe-2021-training-verifiers.md) · 关系：直接源自
- [用大模型当裁判](zheng-2023-llm-as-a-judge.md) · 关系：直接源自
- [大语言猴子：靠重复抽样扩展推理算力](brown-2024-large-language-monkeys.md) · 关系：直接源自
- [测试时算力的最优扩展](snell-2024-test-time-compute.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [开源模型自我验证跑赢闭源模型](../clips/2026-10-18-jackyk02-self-verification-open-model-beats-closed.md) | 直接源自 | 强 |
