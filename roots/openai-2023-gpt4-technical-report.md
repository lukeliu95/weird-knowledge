---
name_zh: "GPT-4 技术报告"
name_en: "GPT-4 Technical Report"
proposer: "OpenAI"
year: "2023"
type: 研究报告
verified: true
---

# GPT-4 技术报告（GPT-4 Technical Report）

## 一句话

OpenAI 介绍 GPT-4 的能力、可预测的扩展、局限和安全措施；其中一张图显示，只做过预训练的模型在 MMLU 上给的概率和实际答对率很贴近（校准好），经过后训练后校准明显变差。

## 原始出处

- GPT-4 Technical Report, OpenAI, arXiv:2303.08774, 2023（DOI 10.48550/arXiv.2303.08774），https://arxiv.org/abs/2303.08774
- “预训练校准好、后训练变差”在图 8，依据 Porter 文和 Kalai 等 2025《Why Language Models Hallucinate》的引用；本次没能直接读出原图说明，https://arxiv.org/abs/2509.04664

## 更底层的源头

- [基于人类反馈的强化学习（RLHF）](reinforcement-learning-from-human-feedback.md) · 关系：相近
- [现代神经网络的校准（温度缩放）](guo-2017-calibration.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Anthus 实测 GPT-6 Luna（通用版，不是 OpenAI Decisions API 本身）：说 99% 确定时只对 68%，推理到第五步接近瞎猜；决策模型要紧的是置信度可信（厂商测评：Anthus 卖决策模型的校准服务）](../clips/2026-10-25-porter-decisions-api-luna-calibration.md) | 直接源自 | 强 |
