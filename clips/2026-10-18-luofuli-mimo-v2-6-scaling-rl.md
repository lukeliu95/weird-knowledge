---
title: "MiMo-V2.6 的强化学习之路"
author: "Fuli Luo (@_LuoFuli)"
url: https://x.com/_LuoFuli/status/2102162926802968749
source: X
published: 2026-09-21 22:27 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 模型与本地部署
roots: [xiaomi-2026-mimo-v2-6-scaling-rl, ma-2026-mopd, multi-task-learning, espeholt-2018-impala, wei-2025-verifiers-law, wang-2025-octothinker-mid-training, conways-law, knowledge-distillation]
---

## 原文

MiMo-V2.6: The Hard Road to Scaling Up RL

MiMo-V2.6 is very likely one of the largest single RL runs, by compute, that any open-source model team has undertaken to date. In an era when compute is brutally scarce, we still chose to dedicate a team of several dozen people to one goal over an extended period: scaling up RL. That takes more than research conviction. It takes a vision for AGI, respect for the unknown, and the nerve to walk straight into the hardest problems.

The result is a model whose potential was built through mid-training and unlocked through heavy RL. Today, it is the number one open-source model. I strongly recommend reading the technical report. I believe it will become one of those papers that Agent RL practitioners keep reopening and discovering something new in each time. In my view, the research innovations and engineering challenges behind it surpass those of DeepSeek R1, which I was partly involved in.

Some will ask: why MixRL instead of MOPD? First, they are not competing choices. We ran MixRL on verifiable tasks of moderate difficulty, including code and related agentic tasks, and found that the resulting models generalize remarkably well. Second, tasks that are difficult to verify, extremely long-horizon, or simply too challenging to include in a joint RL run are trained separately. Including them would substantially reduce rollout efficiency or introduce significant rollout staleness. We then merge the resulting capabilities through MOPD. Games, 3D tasks, and tasks with subjective evaluation signals all fall into this category.

There is also a third, slightly cheeky answer. Our team is flat enough and free enough of organizational silos that MixRL simply is not difficult for us. More importantly, everyone enjoys working this way. People from different domains come together every day, driven by the pursuit of AGI and intelligence that can continuously improve itself, to confront and resolve the RL bottlenecks in each field. I will always remember the RL daily update meetings from this period. They were intense and dense, with intelligence emerging in real time.

To help the open-source community focus on solving real Agentic RL problems, we have released a Qwen model distilled from MiMo RL trajectories as a stronger starting point for RL, along with 7K diverse environments and a complete RL training framework. We hope these resources will help move Agentic RL research forward.

MiMo-V2.6 is only the beginning. In an era when intelligence is easy to replicate, we still choose the hard road toward self-improvement and AGI. Much of what lies ahead remains unknown. But we are willing to keep investing the time, compute, and passion required to take on one hard problem after another and work each of them all the way through, until intelligence crosses into a new regime.

> 媒体：
> - https://pbs.twimg.com/media/HSxiBKkWQAA1LpY.jpg

## 溯源

- 核心主张：模型潜力靠中期训练打底、靠大规模强化学习释放；中等难度、可验证的任务放进同一次混合强化学习，泛化很好；难验证、超长程或太难的任务单独训练，再用多教师在线策略蒸馏（MOPD）合并，免得拖慢采样或让采样数据落后于最新模型；团队扁平、没有部门墙，混合训练才做得起来。
- 源知识：
  - [MiMo-V2.6：扩展强化学习走向自我改进](../roots/xiaomi-2026-mimo-v2-6-scaling-rl.md) · 关系：直接源自 · 强弱：强。推文就是在介绍这份技术报告；报告摘要写明先做中期训练扩大探索空间、再扩展强化学习算力，正文写明用 GRPO 和异步部分采样（滞后度 4）
  - [MOPD：多教师在线策略蒸馏](../roots/ma-2026-mopd.md) · 关系：直接源自 · 强弱：强。推文明说单独训练的能力用 MOPD 合并；MOPD 由同一个小米 MiMo 团队提出
  - [多任务学习](../roots/multi-task-learning.md) · 关系：相近 · 强弱：弱（模型复核通过）。相关任务一起训练能互相当归纳偏置、提升泛化，冲突的任务会互相拖累（负迁移），正对应“能一起练的混练、练不到一起的分开”；属推断
  - [IMPALA：可扩展的分布式深度强化学习](../roots/espeholt-2018-impala.md) · 关系：相近 · 强弱：弱（模型复核通过）。推文说的 rollout staleness，就是采样用的策略落后于正在更新的策略；IMPALA 是处理这个问题的经典异步架构；属推断
  - [验证的不对称与验证者法则](../roots/wei-2025-verifiers-law.md) · 关系：相近 · 强弱：弱（模型复核通过）。可验证任务直接上强化学习、难验证任务另想办法，符合“越好验证越容易被强化学习训好”；属推断
  - [OctoThinker：中期训练让强化学习更能扩展](../roots/wang-2025-octothinker-mid-training.md) · 关系：相近 · 强弱：弱（模型复核通过）。“潜力靠中期训练打底、靠强化学习释放”与 OctoThinker 的“中期训练让强化学习更能扩展”几乎是同一个主张；推文没有引用
  - [康威定律](../roots/conways-law.md) · 关系：相近 · 强弱：弱（模型复核通过）。作者说团队扁平、没有部门墙，所以混合强化学习不难：训练方式（联合训练还是各领域分开再合并）跟着组织的沟通结构走；MOPD 专文也说它让各领域老师能独立并行开发
  - [知识蒸馏](../roots/knowledge-distillation.md) · 关系：直接源自 · 强弱：强。推文明说开源了用 MiMo 强化学习轨迹蒸馏出的 Qwen 模型
- 本质：这条新知识本质上是“多任务联合训练加知识蒸馏”在大模型强化学习后训练上的组合应用，而选联合训练还是分开再合并，又受团队组织结构（康威定律）影响。
- 整理于：2026-10-18（第 2 轮）
