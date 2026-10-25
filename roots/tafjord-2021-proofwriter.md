---
name_zh: "ProofWriter：在自然语言规则上推理并写出证明"
name_en: "ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language"
proposer: "Oyvind Tafjord, Bhavana Dalvi Mishra, Peter Clark（艾伦人工智能研究所）"
year: "2021"
type: 论文
verified: true
---

# ProofWriter：在自然语言规则上推理并写出证明（ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language）

## 一句话

用模板生成的英文小题（一组事实加“如果……就……”规则），让模型判断一句话是真、假还是无法确定，并写出证明；每题标了要连推几步（证明深度），难度可以按步数量化；数据有“证不出就算假”的封闭世界和可以答“不知道”的开放世界两种设定。

## 原始出处

- ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language, Tafjord, Dalvi, Clark, Findings of ACL-IJCNLP 2021, pp. 3621–3634，https://doi.org/10.18653/v1/2021.findings-acl.317
- 前作 RuleTaker：Transformers as Soft Reasoners over Language, Clark, Tafjord, Richardson, IJCAI 2020, pp. 3882–3890，https://doi.org/10.24963/ijcai.2020/537
- 争议：按证明深度出规则推理题的做法始于 2020 年的 RuleTaker（Clark 等，封闭世界）；ProofWriter 在此基础上加了开放世界版本和证明生成。“开放世界版本由 ProofWriter 新加”这一点是模型按记忆写的，没逐字核对原文。

## 更底层的源头

- [一阶逻辑（谓词逻辑）](first-order-logic.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Anthus 实测 GPT-6 Luna（通用版，不是 OpenAI Decisions API 本身）：说 99% 确定时只对 68%，推理到第五步接近瞎猜；决策模型要紧的是置信度可信（厂商测评：Anthus 卖决策模型的校准服务）](../clips/2026-10-25-porter-decisions-api-luna-calibration.md) | 直接源自 | 强 |
