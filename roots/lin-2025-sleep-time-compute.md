---
name_zh: "睡眠时间计算（面向未来查询的离线预计算）"
name_en: "Sleep-time Compute: Beyond Inference Scaling at Test-time"
proposer: "Kevin Lin、Charlie Snell、Yu Wang、Charles Packer、Sarah Wooders、Ion Stoica、Joseph E. Gonzalez"
year: "2025"
type: 论文
verified: true
---

# 睡眠时间计算（面向未来查询的离线预计算）（Sleep-time Compute: Beyond Inference Scaling at Test-time）

## 一句话

在具体问题到来前，先对共享背景材料作有用推断并保存，供后续多个问题复用，把部分在线推理成本转移到离线阶段。

## 原始出处

- Lin 等，Sleep-time Compute: Beyond Inference Scaling at Test-time，arXiv:2504.13171，2025-04-17；核对摘要、引言、方法和第 7 节讨论，未声称复算实验或读完所有附录。，https://arxiv.org/abs/2504.13171
- 论文 v1 正文，说明背景预处理、多查询复用及对未来问题可预测性的依赖。，https://arxiv.org/html/2504.13171v1
- 争议：离线计算有成本，收益依赖未来问题与已有背景相关、且能够多次复用。文中 SWE-Features 衡量预测应修改文件与实际文件的匹配，不等于证明端到端编码正确；高在线预算下传统测试时计算仍可能更好。“睡眠”是计算时段的类比。

## 更底层的源头

- 已追到基础层，或暂未找到更底层的源头

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Anthropic 拆解智能体记忆：边干边记，再靠“做梦”回头纠错整理](../clips/2026-11-08-dotey-anthropic-agent-memory-dreaming.md) | 直接源自 | 强 |
