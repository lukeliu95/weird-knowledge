---
title: "CLM 把候选动作选择做成检索，作者报告特定测试最高快 9 倍"
author: "Daily Dose of Data Science (@DailyDoseOfDS_)"
url: https://x.com/DailyDoseOfDS_/status/2118010458653573179
source: X
published: 2026-11-04 16:00 UTC
saved: 2026-11-06
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 模型与本地部署
roots: [kwok-2026-contrastive-language-models, oord-2018-contrastive-predictive-coding]
---

## 原文

NVIDIA and Stanford challenged Jev.

(their new System 1 architecture runs up to 9x faster.)

It is called a Contrastive Language Model, or CLM.

Like Jev, CLM is not designed to generate text. It handles the small, repeated decisions inside AI systems, such as choosing a tool, ranking a patch, routing a request, or selecting the next action.

But CLM reaches those decisions differently.

Instead of generating an answer token by token, it treats decision-making as a retrieval problem.

Here is how it works.

1) Encode the state

CLM takes the current situation, such as an agent’s context or the state of a game, and converts it into a vector.

It uses a frozen Qwen3-8B model with a small trainable state projection head.

2) Encode every possible action

A separate action head converts each candidate into the same vector space.

In the Mario example, the candidates are left, jump, and right run. CLM does not invent a fourth option. It only evaluates the actions supplied by the application.

3) Learn which states and actions belong together

During training, the correct state-action pair is pulled closer while incorrect pairs are pushed apart.

A batch of B examples produces a B × B similarity matrix. The matching pairs sit on the diagonal. Every other pairing becomes a negative example.

This contrastive training uses InfoNCE, the same general mechanism behind systems such as CLIP and dense retrieval.

4) Turn similarity into a decision

At inference, CLM measures the cosine similarity between the state and every candidate action.

A softmax converts those scores into a probability distribution. The application can choose the winner, apply a confidence threshold, or escalate an uncertain result.

The real speed advantage comes from separating states and actions.

Actions can be embedded once and cached. If an agent repeatedly chooses between the same tools, CLM only needs to encode the changing state and compare it with stored action vectors.

That replaces repeated generation with one embedding pass and a set of cheap dot products.

The researchers report that CLM-8B matches Jev across computer-use, gaming, and tool-calling evaluations while reaching up to 9x lower latency. The improvement is largest when actions repeat or the candidate set grows.

CLM still has limits. It cannot generate new actions, its probabilities are relative to the supplied candidates, and its strongest verifier results require task-specific fine-tuning.

But its central idea is powerful.

The entire research is open-source, including the code.

Read more here: https://t.co/QgtOOttgaj

When software already knows the possible answers, an AI model should score them instead of generating more words.

We also wrote a full breakdown on how system one models like Jev work.

The article is quoted below.

> 媒体：
> - https://video.twimg.com/amplify_video/2118010425497554944/vid/avc1/1892x1080/37nYFeIh810KP8-I.mp4?tag=16

## 溯源

- 核心主张：CLM 把当前状态和给定候选动作编码到同一空间，用对比学习训练评分头，再检索最合适的动作；官方所报最高 9 倍延迟改善依赖测试任务、候选数量及缓存条件，不能理解成任意任务都快 9 倍。
- 源知识：
  - [对比语言模型（候选动作检索）](../roots/kwok-2026-contrastive-language-models.md) · 关系：直接源自 · 强弱：强。官方仓库和模型卡明确说明冻结 Qwen3-8B 编码器、训练两个投影头并给候选动作评分。零样本动作选择与另行微调的代码验证结果是不同设置，不能合并解读。候选概率也不等于对真实世界的绝对置信度。
  - [对比预测编码与 InfoNCE](../roots/oord-2018-contrastive-predictive-coding.md) · 关系：直接源自 · 强弱：强。原帖和官方实现明确使用双向 InfoNCE：匹配状态与正确动作，并与批内错误配对区分；InfoNCE 的原始定义见对比预测编码论文第 2.3 节。
- 本质：这条新知识本质上是把对比学习与检索用于有限候选动作的选择，以预先训练、缓存和向量评分换取较低的在线计算；它本身不生成未给定的新动作。
- 整理于：2026-11-09（第 10 轮）
