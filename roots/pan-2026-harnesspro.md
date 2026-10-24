---
name_zh: "HarnessPro：带帕累托优化的运行框架递归自我改进（性能与成本权衡）"
name_en: "HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs"
proposer: "Zhuoshi Pan, ZhiYuan Feng, Yukuo Cen, Honglin Lin, Junru Lu, Zhongxia Chen, Shuo Yang, H. Vicky Zhao, Jie Tang"
year: "2026"
type: 论文
verified: true
---

# HarnessPro：带帕累托优化的运行框架递归自我改进（性能与成本权衡）（HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs）

## 一句话

无标签地进化 agent 运行框架，同时提高通过率、压低执行成本：用大模型生成的测试代替官方测试和标准答案，专门的 agent 诊断轨迹、按不同性能—成本取向规划改动并实现，再用归一化加权平方距离选出省钱、均衡、高性能三档进入下一轮；GPT-5.5 + Codex 下，高性能档相对 RHO 平均通过率高 2.0 个点、单任务成本降 26.1%。

## 原始出处

- HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs, Zhuoshi Pan 等, 2026, arXiv:2610.26770，https://arxiv.org/abs/2610.26770
- 代码仓库 pzs19/HarnessPro，https://github.com/pzs19/HarnessPro
- 争议：arXiv 预印本（v2，备注 under review），未经同行评审。量子位报道的“成本降 53%”是均衡档在 SWE-Bench Pro 上对 RHO 的单项数字；摘要里的平均数是高性能档成本降 26.1%。

## 更底层的源头

- [递归自我改进](recursive-self-improvement.md) · 关系：直接源自
- [帕累托效率（帕累托改进）](pareto-efficiency.md) · 关系：直接源自
- [达尔文哥德尔机：自我改进 agent 的开放式演化](zhang-2025-darwin-godel-machine.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [智谱唐杰团队开源 HarnessPro：agent 无标签自己改 harness，按"省钱、均衡、性能"三档进化，成本最多降 53%](../clips/2026-10-24-qbitai-harnesspro-pareto-rsi.md) | 直接源自 | 强 |
