---
name_zh: "临床规模负载下，编排式多 agent 比单 agent 更能保住准确率"
name_en: "Orchestrated multi agents sustain accuracy under clinical-scale workloads compared to a single agent"
proposer: "Eyal Klang, Mahmud Omar, Ganesh Raut 等，通讯作者 Girish N. Nadkarni（西奈山伊坎医学院 Windreich 人工智能与人类健康系）"
year: "2025（medRxiv 预印本）/ 2026（npj Health Systems 正式发表）"
type: 论文
verified: true
---

# 临床规模负载下，编排式多 agent 比单 agent 更能保住准确率（Orchestrated multi agents sustain accuracy under clinical-scale workloads compared to a single agent）

## 一句话

把检索、抽取、剂量计算三类临床任务按 5 到 80 个一批交给模型：一个 agent 包办全部时，准确率从 73.1% 跌到 16.6%；由编排器把每个任务派给专门的工人 agent 时，准确率从 90.6% 只降到 65.3%，token 最多少用 65 倍；作者归因于任务隔离避免了上下文互相干扰。

## 原始出处

- Orchestrated multi agents sustain accuracy under clinical-scale workloads compared to a single agent, Eyal Klang 等, medRxiv 预印本, 2025-08-24，https://doi.org/10.1101/2025.08.22.25334049
- 同上，npj Health Systems 3(1): 23, 2026-03-09，https://doi.org/10.1038/s44401-026-00077-0
- 西奈山医院新闻稿，2026-03-10，https://www.mountsinai.org/about/newsroom/2026/orchestrated-multi-agent-ai-systems-outperforms-single-agents-in-health-care

## 更底层的源头

- [大模型很容易被无关上下文带偏](shi-2023-irrelevant-context-distraction.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Meta 的瘦编排器模式：编排器只管路由和检查，不做领域推理，14 个专项子 agent 各管一块](../clips/2026-10-20-meta-thin-orchestrator-agent-architecture.md) | 直接源自 | 强 |
