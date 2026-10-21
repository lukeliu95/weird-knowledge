---
title: "GLM 5.3 只靠后训练大涨，被 SemiAnalysis 嘉宾称为警钟"
author: "SuSu_酥酥👅 (@NFT_Chen)"
url: https://x.com/NFT_Chen/status/2111712278827643204
source: X
published: 2026-10-18 06:53 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 模型与本地部署
roots: [zai-2026-glm-5-3-post-training, davidson-2023-ai-capabilities-without-retraining, zhou-2023-lima, guo-2025-deepseek-r1]
---

## 原文

SemiAnalysis 嘉宾直言智谱GLM5.3给他敲响了警钟！

“GLM 5.3 完全是靠后训练前代模型做出来的，对我来说是个警钟。”

同一基座，不换架构、不加参数，Terminal-Bench 从 4.6 干到 28.3，Cyber 能力直接 night and day。

后训练比从头预训练省 GPU 太多了。有私有数据的公司，完全可以在开源底座上 post-train，直接打过部分闭源模型。

基座潜力远未触顶。后训练才是下半场真正的战场。

#智谱 #GLM53 #后训练 #AI #开源模型 #PostTraining #唐杰 #Zai

https://t.co/4qzDrCmjxb https://t.co/ULmPTsXAv9

> 媒体：
> - https://video.twimg.com/ext_tw_video/2111596378220535809/pu/vid/avc1/1280x720/lhWYOycg3zJyp9hg.mp4?tag=12

## 溯源

- 核心主张：GLM-5.3 不换底座、不改架构、不加参数，只靠后训练就把 Terminal-Bench（3.0）从 4.6 提到 28.3、网安能力大涨；后训练比从头预训练省得多算力，所以有私有数据的公司可以在开源底座上后训练、追上部分闭源模型，后训练是接下来的主战场。
- 源知识：
  - [GLM-5.3：同一底座只靠扩展后训练](../roots/zai-2026-glm-5-3-post-training.md) · 关系：直接源自 · 强弱：强。“同一基座”和“Terminal-Bench 4.6→28.3”都能在智谱官方模型卡和开发文档里找到原句（基准是 Terminal-Bench 3.0），唐杰本人在 X 长文里也说过同底座、同参数、只多做后训练。
  - [不重新训练也能大幅提升 AI 能力（训练后增强）](../roots/davidson-2023-ai-capabilities-without-retraining.md) · 关系：相近 · 强弱：弱（模型复核通过）。“后训练比从头预训练省 GPU 太多”，和这篇“训练后增强用不到 1% 的成本换来相当于多倍训练算力的提升”是同一笔账；推文没引用，属推断。
  - [LIMA：对齐少即是多（表层对齐假说）](../roots/zhou-2023-lima.md) · 关系：相近 · 强弱：弱（模型复核通过）。“基座潜力远未触顶”和 LIMA“能力基本在预训练时学到，后训练负责引出来”相近；但 LIMA 认为少量数据就够，GLM-5.3 是靠大规模强化学习换来能力跳涨，两者对后训练分量的判断不同（推断）。
  - [DeepSeek-R1：用强化学习激发推理能力](../roots/guo-2025-deepseek-r1.md) · 关系：相近 · 强弱：弱（模型复核通过）。DeepSeek-R1 也是在已有底座（V3）上靠大规模强化学习把能力拉上去，是“只靠后训练大涨”的前例；推文没提，属推断。
- 本质：这条新知识本质上是“先预训练、再微调”（迁移学习）在大模型时代的放大版：底座里的能力远没用完，用强化学习和更像真实工作的训练环境把它激发出来，花的算力比重新预训练少得多。
- 整理于：2026-10-18（第 3 轮）
