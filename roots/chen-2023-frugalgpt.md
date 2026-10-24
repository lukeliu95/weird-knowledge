---
name_zh: "FrugalGPT：用级联大模型省钱又提效"
name_en: "FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance"
proposer: "Lingjiao Chen、Matei Zaharia、James Zou"
year: "2023"
type: 论文
verified: true
---

# FrugalGPT：用级联大模型省钱又提效（FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance）

## 一句话

各家大模型接口价格能差两个数量级。把一个问题依次交给一串模型，前面的答案经打分判断可靠就直接用，不可靠才交给后面更贵的模型；作者称这样能在追平最强单个模型效果的同时最多省 98% 成本。

## 原始出处

- FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance，Lingjiao Chen、Matei Zaharia、James Zou，arXiv:2305.05176，2023（第 3 节 LLM cascade），https://arxiv.org/abs/2305.05176

## 更底层的源头

- [级联分类器（Viola–Jones 快速目标检测）](viola-2001-boosted-cascade.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [yetone 用 3 个 /loop 循环让 Claude Code 自己维护 Magpie](../clips/2026-10-18-dotey-yetone-magpie-three-loops-workflow.md) | 相近 | 弱（模型复核通过） |
| [agent 每步的选择题交给小决策模型（UIUC 等，推文误作普林斯顿和谷歌），模拟网店里 4B 模型完成率 91.5%](../clips/2026-10-20-rohanpaul-ai-agent-decision-model-small-beats-big.md) | 直接源自 | 强 |
| [智谱唐杰团队开源 HarnessPro：agent 无标签自己改 harness，按"省钱、均衡、性能"三档进化，成本最多降 53%](../clips/2026-10-24-qbitai-harnesspro-pareto-rsi.md) | 相近 | 弱（模型复核通过） |
| [Harrison Chase：agent 里很多步骤是是非题不是生成，交给决策模型给带校准的概率，大模型只做难的](../clips/2026-10-22-hwchase17-yes-no-calls-jev.md) | 相近 | 弱（模型复核通过） |
