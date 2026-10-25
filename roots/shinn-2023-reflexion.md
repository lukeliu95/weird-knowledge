---
name_zh: "Reflexion：用语言反思做强化（不改模型权重）"
name_en: "Reflexion: Language Agents with Verbal Reinforcement Learning"
proposer: "Noah Shinn、Federico Cassano、Edward Berman、Ashwin Gopinath、Karthik Narasimhan、Shunyu Yao"
year: "2023"
type: 论文
verified: true
---

# Reflexion：用语言反思做强化（不改模型权重）（Reflexion: Language Agents with Verbal Reinforcement Learning）

## 一句话

不更新模型权重，而是让 agent 每次尝试后用文字反思任务反馈，把反思存进记忆，下次照着改；用“语言反馈”代替传统强化学习里的数值奖励和参数更新。

## 原始出处

- Reflexion: Language Agents with Verbal Reinforcement Learning, Noah Shinn 等, 2023, arXiv:2303.11366，https://arxiv.org/abs/2303.11366

## 更底层的源头

- [强化学习](reinforcement-learning.md) · 关系：相近
- [自我改进：用自我反馈迭代改写](madaan-2023-self-refine.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Terminal-RSI：命令行 agent 拿自己验证过的成功经验反复训练自己，一轮比一轮强](../clips/2026-10-18-yang-terminal-rsi-recursive-self-improving-agents.md) | 相近 | 强 |
| [模型不动，只让技能库从用户请求里长：设计 agent 的技能从 76 个长到 139 个](../clips/2026-10-20-du-designer-rsi-procedural-memory.md) | 直接源自 | 强 |
| [把 skill 当参数来训：别的模型读执行记录提改法，每步只许改几处，留出集上变好才收下；6 个测试集、7 个模型、3 种运行环境里 52 格全部第一或并列第一](../clips/2026-10-25-yang-skillopt-self-evolving-agent-skills.md) | 直接源自 | 强 |
