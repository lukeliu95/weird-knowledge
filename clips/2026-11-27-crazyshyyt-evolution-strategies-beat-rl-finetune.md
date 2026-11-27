---
title: "进化策略不用反向传播微调大模型，在推理题上胜过强化学习"
author: "CrazyShyyt (@CrazyShyyt)"
url: https://x.com/CrazyShyyt/status/2125074496264737147
source: X
published: 2026-11-24 03:50 UTC
saved: 2026-11-27
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

Reinforcement Learning is officially cooked.

Researchers from MIT and Cognizant AI Lab proved you can fine-tune billion-parameter LLMs using pure evolution.

With zero backpropagation.

Instead of using calculus, gradients, or backpropagation to tweak weights, they simply perturbed the model's parameters, tested the outputs, and evolved the best performers.

Evolution strategies were written off years ago. Everyone assumed they couldn't scale past a few million parameters.

And they scaled it to billions.

The method is almost stupidly simple:

• Make 30 copies of the model
• Add tiny random noise to each copy's weights
• Let every copy answer the prompt
• Nudge the original model toward the copies that scored best
• Repeat

No gradients. No backpropagation.

They tested it across 7 Qwen and Llama models (from 0.5B to 8B) on a reasoning benchmark called Countdown.

Evolution didn't just compete with RL. It embarrassed it.

• Average score gain: ES +36.4 points vs. GRPO +21.4 vs. PPO +17.9
• Matched RL's performance using under 20% of the training samples
• 15.5x less variation from run to run

And on the smallest model, the gap gets absurd.

RL took Qwen 0.5B from 0.1% accuracy to 0.5% at best. Evolution took it to 14.4%.

Even worse for RL: it had a massive unfair advantage. The researchers custom-tuned RL's settings for every single model. Evolution used one default setting for everything.

But here is the craziest part of the paper.

They ran a test to train the models to give shorter answers.

Without a heavy penalty holding it back, GRPO immediately started cheating. It spat out strings of nonsense symbols, because gibberish is technically short.

Evolution never cheated. Nobody even told it not to.

Why?

RL rolls the dice on every single token, hundreds of times per answer, and tries to guess which token earned the reward. It optimizes for loopholes.

Evolution rolls the dice once on the weights, and judges the entire answer as a whole.

> 媒体：
> - https://pbs.twimg.com/media/HX3H-bvaUAAHQWs.jpg

## 溯源

