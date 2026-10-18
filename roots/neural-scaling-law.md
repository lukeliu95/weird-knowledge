---
name_zh: "神经网络规模定律"
name_en: "Neural scaling law"
proposer: "Hestness 等（2017）；Jared Kaplan 等（2020）"
year: "2017 / 2020"
type: 定律
verified: true
---

# 神经网络规模定律（Neural scaling law）

## 一句话

模型参数、训练数据、算力按比例加大时，模型的损失会按可预测的幂律稳定下降，所以「做大就会变好」。

## 原始出处

- Scaling Laws for Neural Language Models, Jared Kaplan et al., 2020，https://arxiv.org/abs/2001.08361
- Neural scaling law（维基百科），https://en.wikipedia.org/wiki/Neural_scaling_law
- Deep Learning Scaling is Predictable, Empirically, Joel Hestness et al., 2017，https://arxiv.org/abs/1712.00409
- 争议：Hestness 等 2017 年更早做了系统的实证拟合，Kaplan 等 2020 年让它在大语言模型圈广为人知；2022 年 Hoffmann 等（Chinchilla）修正了参数和数据的最优配比。；维基把 Hestness 等 2017 年的论文当作常见参照点，并说更早的工作要么是纯理论、要么规模小得多；Kaplan 2020 和 Chinchilla（Hoffmann 2022）在参数与数据的最优配比上结论不同。；更早已有理论推导或小规模研究；基于大规模实验拟合的经验定律，常以 Hestness 等 2017 为参照，Kaplan 等 2020 让它出名

## 更底层的源头

- [苦涩的教训](bitter-lesson.md) · 关系：相近
- [边际收益递减](diminishing-returns.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [LeCun：下个万亿AI公司不靠LLM](../clips/2026-10-18-phosphenq-lecun-lecture-beyond-llms.md) | 挑战 | 强 |
| [Kimi 创始人谈 AGI 需要新组织](../clips/2026-10-18-vartekxx-kimi-founder-agi-organization.md) | 相近 | 弱（待 Luke 确认） |
| [Anthropic 多智能体研究系统详解](../clips/2026-10-18-oran-ge-anthropic-multi-agent-research.md) | 相近 | 弱（待 Luke 确认） |
| [AI 应用及格线与文艺行业首当其冲](../clips/2026-10-18-dotey-ai-passing-line-creative-industry.md) | 直接源自 | 强 |
