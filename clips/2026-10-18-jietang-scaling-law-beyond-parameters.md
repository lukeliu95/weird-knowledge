---
title: "唐杰谈缩放定律：不只是堆参数"
author: "jietang (@jietang)"
url: https://x.com/jietang/status/2089941544581403107
source: X
published: 2026-08-19 05:04 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 模型与本地部署
roots: [kaplan-2020-scaling-laws, hoffmann-2022-compute-optimal, sardana-2023-beyond-chinchilla, roberts-2025-compute-optimal-skills, mixture-of-experts, nakamura-2025-moe-sparsity-reasoning, guo-2025-deepseek-r1, liebigs-law-of-the-minimum]
---

## 原文

Thoughts About Scaling Law

Scaling, but not only of parameters. Every model release now ends with the same question: how many parameters? It isn't a question that can be answered on its own. Parameter count is only meaningful alongside three others — how much data you have, where you intend to spend your compute, and who will run the model, under what conditions.

The field learned this the hard way. Kaplan et al. (2020) fit an exponent that told everyone to grow parameters faster than data — roughly 2.7:1 — and the industry complied: GPT-3, Gopher, MT-NLG. Hoffmann et al. (2022) redid the experiment across four hundred models and found the compute-optimal split is closer to 20 tokens per parameter, and that with sufficient compute the two should grow at the same rate rather than drifting apart. The error in the earlier fit compounded with every order of magnitude of compute, which is why the largest models of that generation were the most misallocated. The trillion-parameter round was, in retrospect, a detour the whole field took together and then reversed.

Chinchilla wasn't the end either. It optimized training compute for models that would be trained once and evaluated. Today a model is called billions of times a day and inference dominates lifetime cost. Put inference into the objective and the optimum moves toward smaller models trained far longer — deliberate over-training, which is what Llama-2-7B and Gemma-2-9B were doing at roughly 290 and 889 tokens per parameter.

Sparsity moved the target again. In a MoE model two quantities have to be kept apart: total parameters govern roughly how much the model can hold — knowledge, facts, the long tail — while activated parameters and effective depth govern roughly how far it can think, how many steps of a causal chain it can carry before it comes apart. A dense 20:1 ratio does not transfer. And the ratio isn't a single number at all: Roberts et al. (2025) find the optimal tokens-per-parameter is task-dependent, with memorization favoring more parameters and reasoning favoring more data. Follow-up work on MoE observes that at fixed TPP, pushing total parameters higher actually degrades reasoning, while activating more experts reliably helps it.

This matters for what we are building toward. Finding a vulnerability is not a retrieval problem. It doesn't come from having memorized more CVEs; it comes from carrying a twenty-step chain of inference to the end without losing the thread. That capability does not live in total parameter count.

Which brings us to this release. Total parameters appear to matter up to a threshold — enough to hold the world — after which additional capability comes from scaling elsewhere: effective depth per forward pass, and above all post-training. GLM-5.3 is our controlled experiment on that claim. Same base, same architecture, same total and activated parameters as GLM-5.2. One month of scaling long-horizon environments and RL. The gains are not marginal. Well, scaling has more than one dial. We turned the post-training one this time because it had the most slack left in it — not because the others are finished. Base model size, pretraining data, compute spent per forward pass: all of them are still on the table, and we will come back to each. What this experiment taught us is that the dials do not have to be turned together, and that the one worth turning next is rarely the one that was worth turning last. We are not done scaling. Next time, maybe mid-training, pre-training, and even more.

## 溯源

- 核心主张：参数量单独看没有意义，要和数据量、算力花在哪、谁在什么条件下运行模型一起看。缩放有好几个旋钮（参数、数据、推理成本、稀疏度、有效深度、后训练），最优配比随目标而变。总参数过了“装得下世界”的门槛后，新的能力来自余量最大的那个旋钮，这次是后训练：GLM-5.3 和上一版用同一个底座，只多做了一个月长程环境和强化学习。
- 源知识：
  - [神经语言模型的缩放定律](../roots/kaplan-2020-scaling-laws.md) · 关系：挑战 · 强弱：强。作者点名 Kaplan 等 2020，并明确说它“参数要比数据长得快”的拟合把整个行业带上了弯路
  - [训练算力最优的大语言模型（Chinchilla）](../roots/hoffmann-2022-compute-optimal.md) · 关系：直接源自 · 强弱：强。作者点名 Hoffmann 等 2022（Chinchilla），以它的“参数和数据同比例增长”为出发点，再指出它没把推理成本算进去
  - [超越 Chinchilla 最优：把推理成本算进缩放定律](../roots/sardana-2023-beyond-chinchilla.md) · 关系：直接源自 · 强弱：强。“把推理成本算进目标后，最优点移向更小、训练更久的模型”，与这篇论文的结论几乎一字不差，只是作者没点名
  - [技能的算力最优缩放：知识与推理](../roots/roberts-2025-compute-optimal-skills.md) · 关系：直接源自 · 强弱：强。作者点名 Roberts 等 2025：每个参数该配多少 token 随任务而变，记忆类更吃参数，推理类更吃数据
  - [混合专家](../roots/mixture-of-experts.md) · 关系：直接源自 · 强弱：强。原文专门讨论 MoE 里总参数和激活参数要分开看
  - [推理任务下 MoE 的最优稀疏度](../roots/nakamura-2025-moe-sparsity-reasoning.md) · 关系：直接源自 · 强弱：弱（模型复核通过）。原文说“MoE 的后续研究”发现：每参数 token 数固定时，加大总参数反而伤推理，多激活专家则有帮助。这和这篇论文的摘要高度吻合，但作者没点名
  - [DeepSeek-R1：用强化学习激发推理能力](../roots/guo-2025-deepseek-r1.md) · 关系：相近 · 强弱：弱（模型复核通过）。把后训练（长程环境加强化学习）当作可以单独加码的旋钮，和 DeepSeek-R1 用大规模强化学习激发推理能力的思路相近；原文没提
  - [最小因子定律（短板定律）](../roots/liebigs-law-of-the-minimum.md) · 关系：相近 · 强弱：弱（模型复核通过）。“总参数过了门槛就不再是瓶颈，能力要从别处来；下一个该拧的旋钮很少是上一个”，就是“短板决定增长”的思路，属推断
- 本质：这条新知识本质上是三条经济学老道理在“大模型算力该投向哪个缩放旋钮”上的应用：边际收益递减、按边际收益分配资源（等边际原则）、短板定律。
- 整理于：2026-10-18（第 1 轮）
