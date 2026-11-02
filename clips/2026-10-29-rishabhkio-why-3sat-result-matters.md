---
title: "通俗解释 OpenAI 的 ETH 反驳声称：次指数不等于实用可解，外部核验仍在进行"
author: "Rishabh Karnawat (@rishabhkio)"
url: https://x.com/rishabhkio/status/2114892366586823133
source: X
published: 2026-10-27 01:30 UTC
saved: 2026-10-29
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 学习与研究
roots: [openai-2026-eth-is-false, exponential-time-hypothesis, lean-proof-assistant]
---

## 原文

Many of you don't understand how serious this is, so let me break it down. 

In computer science there is a famous kind of puzzle called 3-SAT. You are given a long list of yes-or-no switches and a set of rules about how they must be arranged, and you have to find a combination that satisfies every rule. The obvious way to solve it is to try every combination, but each new switch doubles the number of possibilities, so a puzzle with a few hundred switches would take longer than the age of the universe to brute force. 

For decades, the smartest people in the field found clever tricks that made this a little faster, but every trick still hit the same wall: the time required kept exploding as the puzzle grew.
About 25 years ago, two computer scientists, Russell Impagliazzo and Ramamohan Paturi, working with Francis Zane, turned that wall into a formal idea. 

They proposed the Exponential Time Hypothesis, which says this explosion is not a failure of human cleverness but a law of nature. No algorithm, however brilliant, will ever solve 3-SAT without the time blowing up exponentially. Nobody could prove it, but almost everyone believed it, and it became one of the foundations of modern computer science. 

Researchers used it as a measuring stick. If you could show that solving some other problem quickly would also crack 3-SAT quickly, you had shown that problem was hopelessly hard too. Hundreds of papers, across scheduling, graphs, logic and much more, rest on this one assumption.

Now an internal AI model at OpenAI claims to have broken it. It says it found an algorithm that solves these puzzles meaningfully faster than the hypothesis allows, and it has checked the proof in a computer verification system called Lean. 

And here is the remarkable part: the very people who proposed the hypothesis, Impagliazzo and Paturi, along with MIT's Ryan Williams, are now leading the public review of whether a machine has disproved their own idea.
So what happens next? If the disproof holds, a large part of theoretical computer science has to be revisited. 

Every result that said "this problem cannot be solved faster, assuming ETH" loses its foundation, and researchers will have to work out which of those walls were real and which were simply where we stopped looking. It does not mean everything becomes easy. The new algorithm is still slow in absolute terms and this is not the famous P versus NP problem being solved. 

But it means our map of what is possible was wrong in a place we were very confident about, and it was an AI that redrew it. If the disproof fails, the hypothesis survives and the field breathes out, but we will still have watched an AI produce serious, checkable work on one of the deepest questions in the discipline, closely enough that the founders of the idea had to take it seriously. Either way, something has shifted.

## 溯源

- 核心主张：若公开稿声称的固定k-SAT次指数算法经独立核验成立，ETH将被反驳，相关条件困难性解释需重估；这不等于P与NP解决或所有问题实用可解。
- 源知识：
  - [《指数时间假说是假的》公开稿及 Lean 范围说明](../roots/openai-2026-eth-is-false.md) · 关系：直接源自 · 强弱：强。解释对象与公开稿及Lean范围说明一致；需分清厂商宣布与外部核验，本库只核对出处，未独立证明。
  - [指数时间假说（ETH）](../roots/exponential-time-hypothesis.md) · 关系：挑战 · 强弱：强。固定k的次指数SAT算法若确认，直接与ETH冲突。已有条件定理的逻辑形式仍成立，失去的是把假设当真时的困难性依据。
  - [Lean 证明助手](../roots/lean-proof-assistant.md) · 关系：直接源自 · 强弱：强。公开材料明确列出Lean范围。自然语言稿更尖锐的时间界，与范围说明中形式化的时间界不同。
- 本质：这条内容本质上是对计算复杂性中条件假设进行公开可检查的反证尝试；次指数、形式化与实用可解不能混为一谈。
- 整理于：2026-11-03（第 9 轮）
