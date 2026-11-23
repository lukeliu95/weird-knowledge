---
name_zh: "Lean 与 Mathlib 社区关于黎曼猜想 Lean 证明的联合声明"
name_en: "Lean verification of the Riemann Hypothesis (joint statement)"
proposer: "Lean 与 Mathlib 社区（Lean FRO、Mathlib Initiative 背书）"
year: "2026"
type: 研究报告
verified: true
---

# Lean 与 Mathlib 社区关于黎曼猜想 Lean 证明的联合声明（Lean verification of the Riemann Hypothesis (joint statement)）

## 一句话

2026-11-21 声明：按 Buzzard 的四条标准，确认 Mathlib 里的黎曼猜想陈述正确、Alpöge 的库能零错误编译（几十人复现）、两个独立工具确认证明的正是这条陈述、导出的证明被 Lean 官方内核和多个独立检查器接受；“完全有信心”证明正确，并期待数学界解释其中的新思路。

## 原始出处

- Lean verification of the Riemann Hypothesis，Lean and Mathlib communities，Lean community blog，2026-11-21，https://leanprover-community.github.io/blog/posts/riemann-hypothesis/
- Lean FRO 在 X 上的发布推文，2026-11-21，https://x.com/leanprover/status/2124159121645801562
- 争议：这是社区背书声明，不是期刊同行评审；它认证的是“Mathlib 定义下的形式陈述可由三条标准公理推出”，依赖 Mathlib 的定义和各检查器本身可靠，不代表数学思路已被人读懂（维基百科记 Radziwiłł、Granville 等的保留意见）。

## 更底层的源头

- [判断“已在 Lean 里检查过”可不可信的四个问题](buzzard-2026-checked-in-lean.md) · 关系：直接源自
- [Sutherland（MIT）整理的黎曼猜想 Lean 证明核验文件页](sutherland-2026-rh-lean-verification-files.md) · 关系：直接源自
- [Lean 证明助手](lean-proof-assistant.md) · 关系：直接源自
- [德布鲁因准则（证明要能被小而独立的程序复查）](de-bruijn-criterion.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Lean FRO 和 Mathlib 发声明：验证了黎曼猜想的 Lean 证明](../clips/2026-11-23-leanprover-lean-mathlib-statement-riemann-proof.md) | 直接源自 | 强 |
| [5 分钟讲清 Claude 参与证明黎曼猜想这件事](../clips/2026-11-23-dotey-riemann-hypothesis-claude-explainer.md) | 直接源自 | 弱（模型复核通过） |
| [帖子称黎曼猜想 Lean 证明“零报错、没人看得懂”（夸大：是社区背书，人还没完全读懂）](../clips/2026-11-23-rachelrifx-riemann-proof-verified-nobody-understands.md) | 直接源自 | 强 |
