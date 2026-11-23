---
name_zh: "Lazarus：改写沉睡神经元给 AI agent 植入后门"
name_en: "Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents"
proposer: "Yuchen Zeng、Giorgio Severi、Blake Bullwinkel、Eric Horvitz、Dimitris Papailiopoulos（微软研究院、微软 AI 红队）"
year: "2026"
type: 论文
verified: true
---

# Lazarus：改写沉睡神经元给 AI agent 植入后门（Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents）

## 一句话

不训练模型，只改最后一个前馈层里不到十个“沉睡”神经元（关掉它们几乎不影响正常输出），让它们在看到触发词时各推出一个指定 token，拼成一条恶意命令；同样的结构也能被检测出来，所以模型权重要像代码一样审计。

## 原始出处

- Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents，Zeng 等，arXiv:2611.15118，2026-11-11（预印本，50 页），https://arxiv.org/abs/2611.15118
- 论文首页给出的代码仓库，https://github.com/microsoft/lazarus
- 争议：论文自述：“沉睡神经元可以逐个改写、串成多 token 载荷”这个核心想法，是 Claude Code（Opus 4.5）在 2026 年 2 月自主发现的。

## 更底层的源头

- [BadNets：机器学习模型供应链里的后门](gu-2017-badnets.md) · 关系：直接源自
- [预训练 Transformer 里的知识神经元](dai-2022-knowledge-neurons.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [agent 找出 Qwen3-TTS 里 417 个神经元，放大后会笑、耳语、插话（作者自测）](../clips/2026-11-18-tensorslay-qwen-tts-dormant-neurons.md) | 直接源自 | 强 |
