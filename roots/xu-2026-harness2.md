---
name_zh: "Harness²：面向开放世界的递归 agent 运行框架改进"
name_en: "Harness^2: Recursive Agent Harnessing for an Open World"
proposer: "Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu, Bhavana Dalvi Mishra, Yifei Ming, Han Yu, Rujun Han, Chen-Yu Lee, Tomas Pfister（Google Cloud AI Research、Northwestern University）"
year: "2026"
type: 论文
verified: true
---

# Harness²：面向开放世界的递归 agent 运行框架改进（Harness^2: Recursive Agent Harnessing for an Open World）

## 一句话

两层递归改进 agent 的运行框架：任务层用“提议—试跑对照—合成”在没有标准答案时改当前任务的框架；框架层从这些改动里抽经验，更新一个持续改进用的框架，让以后的新任务改得更好；单步就让 GLM-5 和 Gemini 3.5 Flash 在 WorkBuddy-Bench、JobBench、LAB 上最多提升 11.5、4.5、11.8 个点，加大任务层递归预算还能再涨。

## 原始出处

- Harness^2: Recursive Agent Harnessing for an Open World, Ruiyao Xu 等, 2026, arXiv:2610.14224，https://arxiv.org/abs/2610.14224
- 争议：arXiv 预印本（2026-10-09 提交），未经同行评审。库里已有这篇论文本身的新知识（clips/2026-10-19-xu-harness2-recursive-agent-harnessing.md）。

## 更底层的源头

- [递归自我改进](recursive-self-improvement.md) · 关系：直接源自
- [Meta-Harness：端到端优化模型的运行框架](lee-2026-meta-harness.md) · 关系：直接源自
- [自学优化器（STOP）：递归自我改进的代码生成](zelikman-2023-self-taught-optimizer.md) · 关系：直接源自
- [自我改进：用自我反馈迭代改写](madaan-2023-self-refine.md) · 关系：直接源自
- [递归自聚合（RSA）：让大模型深度思考](venkatraman-2025-rsa.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Harness² 解读：没有标准答案时让新旧 harness 同条件对跑定去留，并把\"怎么改好自己\"沉淀成经验](../clips/2026-10-22-xudong-harness-squared-self-evolution.md) | 直接源自 | 强 |
