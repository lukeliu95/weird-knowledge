---
name_zh: "达尔文哥德尔机：自我改进 agent 的开放式演化"
name_en: "Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents"
proposer: "Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, Jeff Clune"
year: "2025"
type: 论文
verified: true
---

# 达尔文哥德尔机：自我改进 agent 的开放式演化（Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents）

## 一句话

放弃哥德尔机“先证明改动有益再改”的要求，改成让编程 agent 改自己的代码、用编程基准实测每次改动，并保留一个不断长大的 agent 档案库、从中抽样继续改（开放式探索）；SWE-bench 从 20.0% 升到 50.0%，Polyglot 从 14.2% 升到 30.7%。

## 原始出处

- Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents, Jenny Zhang 等, 2025, arXiv:2505.22954，https://arxiv.org/abs/2505.22954
- Sakana AI 博客：The Darwin Gödel Machine（Imbue 原文引用的链接），https://sakana.ai/dgm/
- 代码仓库 jennyzzt/dgm（arXiv 备注给出），https://github.com/jennyzzt/dgm
- 争议：arXiv 预印本 2025-05；Evo² 和 HarnessPro 的参考文献都把它记为 ICLR 2026 论文，没有直接核对会议页面。

## 更底层的源头

- [哥德尔机：只做可证明有益的自我改写的通用求解器](schmidhuber-2003-godel-machine.md) · 关系：直接源自
- [演化算法](evolutionary-algorithm.md) · 关系：直接源自
- [新颖性搜索（放弃目标，只追求新）](lehman-2011-novelty-search.md) · 关系：相近
- [递归自我改进](recursive-self-improvement.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [让大模型当"变异器"做进化：一套几乎通吃的代码和提示词优化办法，开源 Darwinian Evolver](../clips/2026-10-22-imbue-llm-evolution-universal-optimizer.md) | 直接源自 | 强 |
| [Evo² 解读：把改权重和改 harness 两条自进化路线接起来，让“改进者”本身也被训练](../clips/2026-10-22-xudong-evo2-weight-harness-co-evolution.md) | 相近 | 强 |
| [agent 的外壳代码按"类继承"分家：按任务的共同毛病长出一族专用外壳，先跑一遍通用版看出毛病再挑；比只练一个全局外壳分数高、搜索快](../clips/2026-10-25-li-object-oriented-harness.md) | 直接源自 | 弱（模型复核通过） |
