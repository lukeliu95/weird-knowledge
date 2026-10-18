---
title: "Terminal-RSI：两轮自重写加强化学习，27B 终端 agent 从 51.7% 涨到 86.5%"
author: "SuSu_酥酥👅 (@NFT_Chen)"
url: https://x.com/NFT_Chen/status/2111723258517098599
source: X
published: 2026-10-18 07:37 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

🤯RSI突破！腾讯AI混元四步炼出终端Agent神器，Qwen3.8-27B性能直接从51.7%提升至86.5%，小模型硬刚一线！

腾讯混元最新论文Terminal-RSI正式开源递归自我改进（RSI）打法：交替两轮“成功轨迹自重写 + 策略精炼”，让27B模型在终端任务上实现质变。

要点速览：
🔹方法极简却狠：Base → RSR-1（验证成功轨迹Recursive Self-Rewrite做SFT）→ RPR-1（继承critic的RL精炼）→ RSR-2 → RPR-2，两轮闭环，前一轮模型直接生成下一轮训练数据。

🔹成绩炸裂：Terminal-Bench 2.1从51.70%飙到86.52%（+34.82pp）；TB 4.0从0%→19.84%；TB Hard达79%；多基准平均大幅跃升约30个百分点。

🔹长程也破防：Long-Horizon Terminal-Bench process reward 0.21→0.37，严格完成0/46→5/46；SWR100成功率直接翻倍。

🔹技术硬核：验证轨迹重写 + critic权重继承校准 + TB-GAE信用分配 + Success-Prioritized Reward，把“部分进展”真正转化为“严格验证通过”。

🔹意义拉满：延续T1/RSR系列，证明RSI在终端Agent上可稳定爬坡，27B小模型就能冲到86%+水平，逼近甚至超越部分更大模型。

查看论文：https://t.co/s6Lq3R3Bm3

这不是概念炒作，是真正把验证过的成功经验反复炼成能力，终端Agent又要卷起来了！

#RSI #递归自我改进 #腾讯混元 #Qwen #TerminalBench #AIAgent #大模型 #TerminalRSI #AgentRL #混元AI

> 媒体：
> - https://pbs.twimg.com/media/HU5Yjb0a8AAzOM7.jpg
> - https://pbs.twimg.com/media/HU5YjbnboAAEcIa.jpg
> - https://pbs.twimg.com/media/HU5YjbmbUAAnn_f.jpg
> - https://pbs.twimg.com/media/HU5YjeSaMAAPcjq.jpg

## 溯源

