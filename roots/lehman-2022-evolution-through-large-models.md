---
name_zh: "借大模型演化（ELM）：用代码大模型当遗传编程的变异算子"
name_en: "Evolution through Large Models"
proposer: "Joel Lehman, Jonathan Gordon, Shawn Jain, Kamal Ndousse, Cathy Yeh, Kenneth O. Stanley"
year: "2022"
type: 论文
verified: true
---

# 借大模型演化（ELM）：用代码大模型当遗传编程的变异算子（Evolution through Large Models）

## 一句话

用训练过代码的大模型代替遗传编程里的随机变异：它见过大量人写的代码修改，能提出“像人会做的改动”；配合 MAP-Elites 生成了几十万个能让 Sodarace 机器人走起来的程序，再用这些数据训练新模型。

## 原始出处

- Evolution through Large Models, Joel Lehman 等, 2022, arXiv:2206.08896，https://arxiv.org/abs/2206.08896
- 同名书章, Springer《Genetic and Evolutionary Computation》系列, 2023, pp. 331–366，https://doi.org/10.1007/978-981-99-3814-8_11

## 更底层的源头

- [演化算法](evolutionary-algorithm.md) · 关系：直接源自
- [MAP-Elites：按特征格子保留精英来照亮搜索空间](mouret-2015-map-elites.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [让大模型当"变异器"做进化：一套几乎通吃的代码和提示词优化办法，开源 Darwinian Evolver](../clips/2026-10-22-imbue-llm-evolution-universal-optimizer.md) | 相近 | 弱（模型复核通过） |
