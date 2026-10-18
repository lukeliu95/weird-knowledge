---
name_zh: "QLoRA：在量化后的大模型上高效微调"
name_en: "QLoRA: Efficient Finetuning of Quantized LLMs"
proposer: "Tim Dettmers、Artidoro Pagnoni、Ari Holtzman、Luke Zettlemoyer"
year: "2023"
type: 论文
verified: true
---

# QLoRA：在量化后的大模型上高效微调（QLoRA: Efficient Finetuning of Quantized LLMs）

## 一句话

先把冻住的底模压成 4-bit（NF4 数据类型、双重量化），再在上面训练 LoRA，并用分页优化器扛住显存峰值，让 65B 模型能在一张 48GB 显卡上微调，效果接近 16-bit 全量微调。

## 原始出处

- QLoRA: Efficient Finetuning of Quantized LLMs, Dettmers et al., arXiv 2305.14314, 2023，https://arxiv.org/abs/2305.14314

## 更底层的源头

- [LoRA：大语言模型的低秩适配](hu-2021-lora.md) · 关系：直接源自
- [量化（信号处理）](quantization-signal-processing.md) · 关系：直接源自
- [虚拟内存](virtual-memory.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [开源工具让普通人也能微调 27B 模型](../clips/2026-10-18-minlibuilds-open-source-27b-finetune-unsloth.md) | 直接源自 | 强 |
