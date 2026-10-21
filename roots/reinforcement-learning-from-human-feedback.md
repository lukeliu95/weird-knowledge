---
name_zh: "基于人类反馈的强化学习（RLHF）"
name_en: "Reinforcement learning from human feedback"
proposer: "深度强化学习版本以 Paul Christiano 等（2017）为起点；用于语言模型的代表是 Ziegler 等（2019）和 Ouyang 等（InstructGPT，2022）"
year: "2017"
type: 方法论
verified: true
---

# 基于人类反馈的强化学习（RLHF）（Reinforcement learning from human feedback）

## 一句话

先让人给模型的多个输出排出好坏，用这些排序训练一个奖励模型来代表人的偏好，再用强化学习让模型朝奖励高的方向优化。

## 原始出处

- Reinforcement learning from human feedback, Wikipedia，https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback
- Fine-Tuning Language Models from Human Preferences, Ziegler et al., 2019，https://arxiv.org/abs/1909.08593
- Training language models to follow instructions with human feedback, Ouyang et al., 2022，https://arxiv.org/abs/2203.02155
- 争议：不是一个人一篇论文提出的：深度强化学习的做法通常以 Christiano 等 2017 为起点；把它用到大语言模型、形成“预训练、监督微调、奖励模型、强化学习”四步流程的，以 InstructGPT（2022）为代表

## 更底层的源头

- [从人类偏好中做深度强化学习](christiano-2017-human-preferences.md) · 关系：直接源自
- [强化学习](reinforcement-learning.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Karpathy 谈 GPT 现状](../clips/2026-10-18-dotey-karpathy-state-of-gpt.md) | 直接源自 | 强 |
| [Agent 智能体是模型能力的放大器](../clips/2026-10-18-waytoagi-agent-model-capability-amplifier.md) | 相近 | 弱（模型复核通过） |
| [DeepSeek-R1训练流程图解](../clips/2026-10-18-bookwormengr-deepseek-r1-training-flow.md) | 直接源自 | 强 |
