---
name_zh: "预训练 Transformer 里的知识神经元"
name_en: "Knowledge Neurons in Pretrained Transformers"
proposer: "Damai Dai、Li Dong、Yaru Hao、Zhifang Sui、Baobao Chang、Furu Wei"
year: "2022"
type: 论文
verified: true
---

# 预训练 Transformer 里的知识神经元（Knowledge Neurons in Pretrained Transformers）

## 一句话

用归因方法找出“表达某个事实”的少数前馈层神经元，它们越活跃，模型越容易说出这个事实；把激活加倍或清零就能增强或抹掉这个事实，不用微调。

## 原始出处

- Knowledge Neurons in Pretrained Transformers，Dai 等，arXiv:2104.08696（2021），https://arxiv.org/abs/2104.08696
- 同文 ACL 2022 正式版，https://doi.org/10.18653/v1/2022.acl-long.581

## 更底层的源头

- [Transformer 前馈层是键值记忆](geva-2021-ffn-key-value-memories.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [agent 找出 Qwen3-TTS 里 417 个神经元，放大后会笑、耳语、插话（作者自测）](../clips/2026-11-18-tensorslay-qwen-tts-dormant-neurons.md) | 相近 | 弱（模型复核通过） |
