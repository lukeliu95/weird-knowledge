---
name_zh: "训练验证器来解数学应用题"
name_en: "Training Verifiers to Solve Math Word Problems"
proposer: "Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian 等（OpenAI）"
year: "2021"
type: 论文
verified: true
---

# 训练验证器来解数学应用题（Training Verifiers to Solve Math Word Problems）

## 一句话

测试时让模型生成很多候选解，再用单独训练的验证器打分、选排名最高的那个；验证明显提升了成绩，而且比单纯微调更能随数据扩展。

## 原始出处

- Training Verifiers to Solve Math Word Problems, Cobbe et al., 2021，https://arxiv.org/abs/2110.14168

## 更底层的源头

- [P 与 NP 问题](p-versus-np-problem.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [开源模型自我验证跑赢闭源模型](../clips/2026-10-18-jackyk02-self-verification-open-model-beats-closed.md) | 直接源自 | 强 |
