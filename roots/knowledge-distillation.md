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
| [MiMo-V2.6 的强化学习之路](../clips/2026-10-18-luofuli-mimo-v2-6-scaling-rl.md) | 直接源自 | 强 |
| [论文从闭源模型里偷出隐藏思维链](../clips/2026-10-18-maxforai-stealing-hidden-chain-of-thought.md) | 直接源自 | 强 |
| [agent 每步的选择题交给小决策模型（UIUC 等，推文误作普林斯顿和谷歌），模拟网店里 4B 模型完成率 91.5%](../clips/2026-10-20-rohanpaul-ai-agent-decision-model-small-beats-big.md) | 直接源自 | 强 |
| [Personal Agent 像 2012 年的滴滴：是上游模型厂补贴下游的出口，要能自己后训练小模型降本](../clips/2026-10-20-willwangtf-personal-agent-didi-2012.md) | 相近 | 弱（模型复核通过） |
