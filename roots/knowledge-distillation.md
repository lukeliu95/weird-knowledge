---
name_zh: "知识蒸馏"
name_en: "Knowledge distillation"
proposer: "Geoffrey Hinton、Oriol Vinyals、Jeff Dean（命名并系统化）"
year: "2015"
type: 方法论
verified: true
---

# 知识蒸馏（Knowledge distillation）

## 一句话

用大模型（老师）的输出去训练小模型（学生），把大模型的能力压缩到小模型里，换来更低的运行成本。

## 原始出处

- Distilling the Knowledge in a Neural Network, Geoffrey Hinton, Oriol Vinyals, Jeff Dean, 2015 (arXiv 1503.02531)，https://arxiv.org/abs/1503.02531
- Wikipedia: Knowledge distillation，https://en.wikipedia.org/wiki/Knowledge_distillation
- 争议：思路更早就有：Schmidhuber 1991 年在循环网络里做过类似压缩，2006 年有人提出 model compression（用大模型标注的数据训练小模型）；「蒸馏」这个名字和通行做法来自 Hinton 等 2015。

## 更底层的源头

- 已追到基础层，或暂未找到更底层的源头

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [DeepSeek R1 论文解读：自学成才之路](../clips/2026-10-18-oran-ge-deepseek-r1-paper-explained.md) | 直接源自 | 强 |
