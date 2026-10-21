---
title: "必要时才澄清：有一个能猜到的主流意思就直接做，“模型说自己不确定”不是可靠的提问信号"
author: "Michael J.Q. Zhang, Eunsol Choi"
url: https://aclanthology.org/2025.findings-naacl.306/
source: 论文
published: "2025-04（Findings of NAACL 2025: 5541–5558, DOI 10.18653/v1/2025.findings-naacl.306；arXiv 2311.09469）"
saved: 2026-10-19
why: "补课：第 4 题 问题协商"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [der-kiureghian-2009-aleatory-epistemic, howard-1966-information-value-theory, horvitz-1999-mixed-initiative-user-interfaces]
adopted: false
---

## 原文

全文 18 页，ACL Anthology 有免费版（[PDF](https://aclanthology.org/2025.findings-naacl.306.pdf)）。按规则只存要点。

- 标题：Clarify When Necessary: Resolving Ambiguity Through Interaction with LMs
- 被引：18 次（OpenAlex，2026-10-19 查）
- 读了多少：发表版正文全文，附录没读；arXiv 初版也读了用来对比

### 内容要点（模型概括，不是原文）

- 把澄清拆成三步：该不该问 → 问什么 → 拿到回答后怎么答。本文只研究第一步（§1、§2.2）
- 一句话有歧义，不等于就该问。很多歧义有一个能猜到的主流意思，这时直接答更好；"该不该问"要估计"问了之后效果能提高多少"（§2.1）
- 要分清两种不确定：需求本身有多种可能（问用户能解决），和模型自己不懂（问用户也没用）。只有前一种值得问（§2.1）
- 给了澄清，效果大多变好（比如 GPT-3 问答 51.8 → 61.8），但也有变差的（LLaMA-2 翻译）（表 2）
- 只允许对 10% 的输入提问时，最好的方法拿到"全部都问"所获提升的 11%～24%，随机挑只有 10%；"看模型多不自信"和"问模型要不要追问"有时比随机还差（§5.3，表 4）。他们的方法是模拟多个用户的回答、看回答有多分散

**需要说清楚的边界**

- 初版和发表版说法不同：arXiv 初版说"只问 10% 时提升是随机的两倍"，发表版删了；按表 4 实际是 1.1～2.4 倍
- 区分能力不强：各方法 AUROC 大多在 0.5～0.63（0.5 等于随机）（表 4）
- 用的是 GPT-3、LLaMA-2 这类老模型，澄清问答是理想化生成的，只做单轮（§8）

## 溯源

- 核心主张：有歧义不等于该问：有一个能猜到的主流意思就直接做，只有需求真的分散时才问；而且模型说自己“不确定”不是可靠的提问信号，看可能的回答有多分散更准。
- 源知识：
  - [偶然不确定性与认知不确定性](../roots/der-kiureghian-2009-aleatory-epistemic.md) · 关系：直接源自 · 强弱：弱（模型复核通过）。本文直接用了这对概念，但引的是 Cole 等 2023，是推断。
  - [信息价值理论](../roots/howard-1966-information-value-theory.md) · 关系：相近 · 强弱：弱（模型复核通过）。“问不问，看问了之后期望效果能提高多少”，是推断。
  - [混合主导用户界面的原则](../roots/horvitz-1999-mixed-initiative-user-interfaces.md) · 关系：相近 · 强弱：弱（模型复核通过）。不确定时再开口、权衡打扰成本，本文没引 Horvitz，是推断。
- 本质：这条新知识本质上是信息价值理论在“大模型该不该反问用户”上的应用。
- 整理于：2026-10-19（补课第 4 题）
