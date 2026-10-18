---
title: "DeepSeek研究员开源科研SKILL"
author: "思维怪怪 (@0xLogicrw)"
url: https://x.com/0xLogicrw/status/2067507088268632186
source: X
published: 2026-06-18 07:17 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: Agent 与 Skill
roots: []
---

## 原文

DeepSeek 资深研究员陈德里开源了个人项目 Deli AutoResearch SKILL，并发布了由智能体完全自主撰写的第四篇综述论文。

项目以单一的 SKILL.md 协议文件形态呈现，本身不含可执行代码。协议通过规约长周期任务中的状态持久化、防死循环（Anti-Loop）与心跳守护进程（Heartbeat Watchdog），指导 AI 智能体调用子智能体（Subagent）与多角色模拟机制，实现科研全流程的全自动协作。

同时发表的自我博弈综述论文展示了智能体在实验阶段的突破：在零人类干预下，智能体首次自主规划了 GPU 实验，并在 285B 参数量的 DeepSeek 模型上运行强化学习（RL）训练任务。通过 GRPO 算法，智能体完成了从实验设计、编写代码，到运行调试和总结结论的完整研究闭环，并在模拟同行评审中跑出了 8.6/10 的高分。

此前，陈德里已利用同样的方法自主产出过三篇学术综述。首篇关于自主科研智能体的论文经历了约 60 轮智能体迭代，总耗时约 10 小时，实现了从 V1 到 V5 的迭代演进。整套工作流不仅降低了长周期研究的人为操作成本，也验证了 AI 原生研究路径的可行性。

## 溯源

