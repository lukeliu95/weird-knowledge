---
name_zh: "以亚线性显存训练深度网络（梯度检查点）"
name_en: "Training Deep Nets with Sublinear Memory Cost"
proposer: "Tianqi Chen、Bing Xu、Chiyuan Zhang、Carlos Guestrin"
year: "2016"
type: 论文
verified: true
---

# 以亚线性显存训练深度网络（梯度检查点）（Training Deep Nets with Sublinear Memory Cost）

## 一句话

训练时不保存所有中间结果，只留少数“检查点”，反向传播需要时再重新算一遍，用多做一次前向计算的代价，把 n 层网络的显存从 O(n) 降到 O(√n)。

## 原始出处

- Training Deep Nets with Sublinear Memory Cost, Chen, Xu, Zhang, Guestrin, arXiv 1604.06174, 2016，https://arxiv.org/abs/1604.06174
- 争议：论文自己说，丢掉中间结果再重算的思路在自动微分领域早就叫“检查点”（引 Griewank 与 Walther 的 Revolve 算法，2000），这篇的贡献是把它系统地用到通用深度网络训练上。

## 更底层的源头

- [时空权衡（以时间换空间）](space-time-tradeoff.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [开源工具让普通人也能微调 27B 模型](../clips/2026-10-18-minlibuilds-open-source-27b-finetune-unsloth.md) | 直接源自 | 强 |
