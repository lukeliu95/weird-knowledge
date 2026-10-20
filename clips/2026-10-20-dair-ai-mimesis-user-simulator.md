---
title: Meta 的 MIMESIS：用真人行为训练的用户模拟器，比让助手模型扮用户更好练 agent
author: DAIR.AI (@dair_ai)
url: https://x.com/dair_ai/status/2108588052914598084
source: X
published: 2026-10-09
saved: 2026-10-20
why: 探索日报：Luke 想看
related_principles: ["原则 1：质量靠闭环"]
status: 未整理
kind: 观点
topic: Agent 与 Skill
roots: []
---

## 原文

Banger paper from Meta Superintelligence Labs on user simulators for agent training.

Agent RL setups usually let an assistant LLM play the user, so the simulated user is too cooperative and too explicit.

A fixed GPT-5.5 agent finds tau-bench tasks easier with these users than with real people.

This work trains MIMESIS, a 9B user simulator, on human conversations and 13 behavior patterns observed in real users. It beats Claude Opus 5 on behavioral fidelity by 13.4 points.

Agents trained against it outperform agents trained against GPT-5.5 under all nine user simulators they never saw.

They find that adding a coaching step that turns the simulator's private reasoning into feedback adds further gains.

Paper: https://t.co/mFhOJwKPLW


论文链接（t.co 展开后）：https://academy.dair.ai/papers/mimesis-learning-user-simulators-as-training-environments-for-interactive-agents-2610.09484 （arXiv 2610.09484）

媒体：
- https://pbs.twimg.com/media/HUM1qKBbsAAG7TM.jpg

## 溯源

