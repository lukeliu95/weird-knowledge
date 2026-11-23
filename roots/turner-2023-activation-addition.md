---
name_zh: "激活工程：用激活加法引导语言模型（ActAdd）"
name_en: "Steering Language Models With Activation Engineering"
proposer: "Alexander Matt Turner、Lisa Thiergart、Gavin Leech、David Udell、Juan J. Vazquez、Ulisse Mini、Monte MacDiarmid"
year: "2023"
type: 论文
verified: true
---

# 激活工程：用激活加法引导语言模型（ActAdd）（Steering Language Models With Activation Engineering）

## 一句话

推理时往模型中间层的激活上加一个“引导向量”（比如“爱”和“恨”两段提示的激活之差），不训练就能把输出的情绪、话题往指定方向推，其他任务基本不受影响。

## 原始出处

- Steering Language Models With Activation Engineering，Turner 等，arXiv:2308.10248，2023，https://arxiv.org/abs/2308.10248
- 争议：摘要注明“引导向量”的说法借自 Subramani 等 2022；ActAdd 的贡献是用一对提示的激活差来算引导向量、不用优化。

## 更底层的源头

- 已追到基础层，或暂未找到更底层的源头

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [agent 找出 Qwen3-TTS 里 417 个神经元，放大后会笑、耳语、插话（作者自测）](../clips/2026-11-18-tensorslay-qwen-tts-dormant-neurons.md) | 相近 | 弱（模型复核通过） |
