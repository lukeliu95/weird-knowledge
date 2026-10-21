---
name_zh: "模型崩溃"
name_en: "Model collapse"
proposer: "Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson"
year: "2023"
type: 理论
verified: true
---

# 模型崩溃（Model collapse）

## 一句话

模型反复用自己或其他模型生成的数据来训练，会先丢掉分布里少见的尾部，最后退化成单调、失真的输出。

## 原始出处

- Model collapse, Wikipedia，https://en.wikipedia.org/wiki/Model_collapse
- The Curse of Recursion: Training on Generated Data Makes Models Forget, Shumailov et al., 2023，https://arxiv.org/abs/2305.17493
- AI models collapse when trained on recursively generated data, Shumailov et al., Nature, 2024，https://doi.org/10.1038/s41586-024-07566-y

## 更底层的源头

- 已追到基础层，或暂未找到更底层的源头

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [合成数据与苦涩的教训讨论](../clips/2026-10-18-dotey-synthetic-data-bitter-lesson.md) | 相近 | 弱（模型复核通过） |
| [Terminal-RSI：命令行 agent 拿自己验证过的成功经验反复训练自己，一轮比一轮强](../clips/2026-10-18-yang-terminal-rsi-recursive-self-improving-agents.md) | 挑战 | 弱（模型复核通过） |
