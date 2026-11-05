---
title: "英伟达和斯坦福的对比式语言模型 CLM：把决策当检索，比 Jev 快 9 倍"
author: "Daily Dose of Data Science (@DailyDoseOfDS_)"
url: https://x.com/DailyDoseOfDS_/status/2118010458653573179
source: X
published: 2026-11-04 16:00 UTC
saved: 2026-11-06
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
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

