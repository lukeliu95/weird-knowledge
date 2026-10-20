---
title: "普林斯顿和谷歌：agent 每步选择交给小决策模型，4B 模型完成率 91.5%"
author: "Rohan Paul (@rohanpaul_ai)"
url: https://x.com/rohanpaul_ai/status/2112107486098473471
source: X
published: 2026-10-19 09:04 UTC
saved: 2026-10-20
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind: 观点
topic: Agent 与 Skill
roots: []
---

## 原文

New Princeton Univ +  Google paper finds that the decision model most accurate on isolated questions solved only 69.5% of agent tasks, while a 4B model trained on agent states solved 91.5%.

Agent harnesses call a big LLM at every step, which makes long tasks slow and costly. Yet most of those calls just pick from a list, like which tool to use next.

Their harness asks a fast decision model each multiple-choice question and uses its answer only above a confidence threshold fitted on the agent's own runs. They also trained AgentDecision-4B on states the agent actually reaches, including after its own mistakes.

On tasks like their training data, 4B models trained this way made agents 81.1% to 89.0% cheaper and up to 2.5x faster. Success stayed within 3 points, while handing over every tool choice with no threshold lowered success by 19.0 points.

To hand routine agent choices to a small model, train it and set its confidence threshold on your agent's own runs.

– arxiv. org/abs/2610.21412

Title: "JevAgentHarness: Benchmarking, Deploying and Training Decision Models That Share Control with LLMs"

> 媒体：
> - https://pbs.twimg.com/media/HU-owJPbsAA_oce.jpg

## 溯源

