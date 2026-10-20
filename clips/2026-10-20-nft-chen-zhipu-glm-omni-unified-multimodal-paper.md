---
title: "智谱论文曝光内部统一多模态模型 GLM-Omni"
author: "SuSu_酥酥👅 (@NFT_Chen)"
url: https://x.com/NFT_Chen/status/2112077671836606748
source: X
published: 2026-10-19 07:05 UTC
saved: 2026-10-20
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 模型与本地部署
roots: [aerni-2025-modal-aphasia, allen-zhu-2023-knowledge-storage-extraction, transfer-learning, dual-coding-theory]
---

## 原文

🤯我靠！智谱Zai创始人唐杰署名新论文直接曝光智谱内部统一多模态模型「GLM-Omni」！GLM-5.4/5.5 剑已出鞘！

智谱已在内部训练出能同时理解和生成的统一模型，并拿它做了知识互通实验。

GLM-Omni核心信息：
🔹论文《Can Visual Generation Expand What Unified Multimodal Models Know?》，通讯作者唐杰，三位一作均为智谱实习生。

🔹GLM-Omni基于GLM-4.1V-Thinking预训练基座初始化，采用离散图像tokenizer，是智谱内部的统一多模态模型。

🔹论文中与BAGEL、SenseNova-U1一同被测试，首次对外公开。

关键实验结果：
1️⃣通过图像生成训练，模型能学到只存在于图片中的新知识，但直接迁移到纯文字回答能力有限。

2️⃣采用交错图文对齐后，GLM-Omni平均准确率从12.57%提升到26.86%。

3️⃣消融实验：取消图像部分训练损失后，准确率大幅下降至13.71%，证明视觉生成监督对知识获取至关重要。

4️⃣模型经常能正确生成包含知识的图片，却难以用语言准确表达，视觉与语言知识仍存在明显鸿沟。

这不是普通论文，而是智谱内部统一多模态方向的一次实质推进。

论文链接：https://t.co/YSxlCyRFJt

#智谱 #GLMOmni #唐杰 #统一多模态 #大模型 #AI论文 #内部模型 #Zai #Zcode #GLM45

> 媒体：
> - https://pbs.twimg.com/media/HU-bZ_6awAAGXJX.jpg
> - https://pbs.twimg.com/media/HU-bZ_4aYAAPEm2.jpg
> - https://pbs.twimg.com/media/HU-bZ_4bQAAgWCg.jpg
> - https://pbs.twimg.com/media/HU-bZ_4bMAABuxv.jpg

## 溯源

- 核心主张：统一多模态模型通过学画图，能学到只出现在图片里的新知识，但这些知识直接用纯文字问答取出来的效果有限、因模型和知识类别而异；在一部分实体上加“边画边答”的交错图文对齐训练，能让其他实体的视觉知识更多地用文字答出来，而且起作用的主要是交错数据里图像部分的监督。
- 源知识：
  - [模态失语：统一多模态模型能凭记忆描述图像吗](../roots/aerni-2025-modal-aphasia.md) · 关系：直接源自 · 强弱：强。论文明确以 Aerni 等的“模态失语”为出发点（模型能把学到的东西画对却说不出来），并沿用其“用画图辅助回忆”的方向做视觉思维链实验。
  - [语言模型物理学 3.1：知识的存储与提取](../roots/allen-zhu-2023-knowledge-storage-extraction.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“知识存进去了但用别的方式取不出来；在一部分实体上加问答对齐，能让模型对其余实体也答得出”，和 Allen-Zhu 与 Li 用虚构人物传记做的“存储与提取”实验设计和结论都很像；论文没引用，是推断。
  - [迁移学习（机器学习）](../roots/transfer-learning.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。论文研究的就是“跨模态知识迁移”：从图像生成目标学到的知识能否迁移到文字问答目标上。
  - [双重编码理论](../roots/dual-coding-theory.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。双重编码理论认为语言和意象是两套独立又靠“指称联结”相连的系统；论文发现视觉学到的知识要靠交错对齐把两套表征连起来才更能用语言取出，和它很像；论文没引用，是推断。
- 本质：这条新知识本质上是“跨模态迁移学习”在统一多模态模型上的检验：从画图学到的知识像 Allen-Zhu 说的“存得进、取不出”（即模态失语），要靠交错图文的训练数据把视觉和语言两套表征接起来。
- 整理于：2026-10-21（第 4 轮）
