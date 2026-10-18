---
title: "Dream-RSI：回放里做梦改策略"
author: "Max For AI (@MaxForAI)"
url: https://x.com/MaxForAI/status/2100111071726174279
source: X
published: 2026-09-16 06:34 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [zheng-2026-dream-rsi-replay, sutton-1990-dyna, ha-2018-world-models, recursive-self-improvement, zelikman-2023-self-taught-optimizer, exploration-exploitation-dilemma]
---

## 原文

卧槽，Google 和 Google DeepMind 最新放出了一篇很有意思的论文：Dream-RSI。

全称就是 Recursive Self-Improvement through Evolving Worlds，讲的是RSI（递归自我改进）。

但它做 RSI 的方式，和我们过去想象的不太一样。模型没有自己训练模型，也没有修改自己的权重，而是开始修改自己的「探索策略」。

简单来说，Agent 每次执行任务，都会留下完整的探索历史：试过哪些方案、哪些失败了、哪个分支效果最好、花了多少计算。

Dream-RSI 会把这些历史直接做成一个 Replay Simulator，然后让 Agent 在里面不断「做梦」：如果当时先走另一个分支呢？如果多开几个并行任务呢？如果这个方向早点停掉呢？

关键是，历史里的结果都已经算过了，所以这些实验根本不用重新调用 Coding Agent 和 Evaluator。

一次昂贵的真实探索，可以拿来做成千上万次几乎零执行成本的策略实验。

找到更好的策略之后，再把它部署回真实世界，于是就形成了一个完整循环：

探索 → 积累历史 → 做梦 → 改进 Policy → 再探索 → 再做梦。

一个 RSI Loop 就这么闭上了。

效果也很好啊，在 GPU Kernel 任务里，VGG16 和 LayerNorm 达到类似性能，分别少用了 2.43× 和 1.79× generations；
ConvDiv 和 ConvMax 在相近预算下，性能分别提高了 2.09× 和 1.44×。

还有一个实验我觉得特别有意思。

他们也试过更传统的办法：把过去探索得到的经验总结出来，直接塞回 Prompt 里指导下一轮，结果反而更差。

因为这些总结出来的「经验」很容易变成偏见，让 Agent 过早集中在某几个看起来正确的方向上，反而损失了探索的多样性。

所以这篇论文真正值得关注的地方，是它展示了另一条 RSI 路线：

模型不一定要先学会修改自己的权重，Agent 可以先学会修改自己的 Harness。

怎么搜索、开多少分支、什么时候继续、什么时候放弃、计算资源怎么分配，这些过去由人类工程师设计的东西，现在也开始进入 Agent 自己的优化循环。

底层还是同一个模型，但它开始自己研究：到底怎么用自己，才能变得更强。

> 媒体：
> - https://pbs.twimg.com/media/HSUWf6DaMAEPDKn.jpg

## 溯源

- 核心主张：把 Agent 过去的探索历史做成回放模拟器，在里面低成本反复试验新的探索策略再部署回真实任务，就能在不改模型权重的前提下递归改进 Agent 的外层编排；而把经验总结塞回提示词，反而会因偏见损失探索多样性。
- 源知识：
  - [Dream-RSI：在演化的世界里递归自我改进](../roots/zheng-2026-dream-rsi-replay.md) · 关系：直接源自 · 强弱：强。作者明说在介绍这篇论文；回放模拟器、做梦、把经验当提示反而更差，都与论文一致。
  - [Dyna：学习、规划与反应的一体化架构](../roots/sutton-1990-dyna.md) · 关系：直接源自 · 强弱：强。论文引用 Sutton 1990，并以「学一个环境模型、用想象的轨迹改进策略」作为核心类比，这正是 Dyna 的思路。
  - [世界模型](../roots/ha-2018-world-models.md) · 关系：直接源自 · 强弱：强。论文引用 World Models；「在自己的梦里训练策略、再搬回真实环境」是 World Models 摘要里的原话思路。
  - [递归自我改进](../roots/recursive-self-improvement.md) · 关系：直接源自 · 强弱：强。论文标题就是 Recursive Self-Improvement。
  - [自学优化器（STOP）：递归自我改进的代码生成](../roots/zelikman-2023-self-taught-optimizer.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。「模型不变，改进的是外层脚手架」与 STOP 的做法相同；抓取到的论文引用列表里没看到 STOP。
  - [探索与利用困境](../roots/exploration-exploitation-dilemma.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。「总结出的经验变成偏见，让 Agent 过早集中在少数方向」是过度利用、探索不足的典型表现；论文只泛泛说会限制探索。
- 本质：这条新知识本质上是基于模型的强化学习（Dyna 和世界模型里的「做梦」）在 Agent 外层编排自我改进上的应用。
- 整理于：2026-10-18（第 1 轮）
