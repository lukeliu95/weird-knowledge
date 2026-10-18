---
title: "MiMo-V2.6 的强化学习之路"
author: "Fuli Luo (@_LuoFuli)"
url: https://x.com/_LuoFuli/status/2102162926802968749
source: X
published: 2026-09-21 22:27 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind: 观点
topic: 模型与本地部署
roots: []
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

