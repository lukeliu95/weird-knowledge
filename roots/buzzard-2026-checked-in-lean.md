---
name_zh: "判断“已在 Lean 里检查过”可不可信的四个问题"
name_en: "“…and the proof is checked in Lean”"
proposer: "Kevin Buzzard（Xena 项目博客）"
year: "2026"
type: 方法论
verified: true
---

# 判断“已在 Lean 里检查过”可不可信的四个问题（“…and the proof is checked in Lean”）

## 一句话

说“在 Lean 里查过所以是对的”之前，尤其是 AI 生成的代码，要问四件事：形式化的陈述对不对得上原题；代码能不能编译；证明的是不是那条陈述（没偷换定义、没加公理，用 lake comparator 查）；有没有钻 Lean 内核的漏洞（用多个独立内核查）。都过了，配套的文字稿也不一定对。

## 原始出处

- “…and the proof is checked in Lean”，Xena 博客，2026-11-12，https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/
- Lean 参考手册：Validating proofs（lake comparator），https://lean-lang.org/doc/reference/latest/ValidatingProofs/#validating-comparator
- 争议：博文署名 xenaproject；Xena 是 Kevin Buzzard 的项目博客，文中“Anthropic 请我看他们费马大定理的 1300 万行代码”也指向 Buzzard，作者归属是据此推断。

## 更底层的源头

- [Lean 证明助手](lean-proof-assistant.md) · 关系：直接源自
- [德布鲁因准则（证明要能被小而独立的程序复查）](de-bruijn-criterion.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Lean FRO 和 Mathlib 发声明：验证了黎曼猜想的 Lean 证明](../clips/2026-11-23-leanprover-lean-mathlib-statement-riemann-proof.md) | 直接源自 | 强 |
| [5 分钟讲清 Claude 参与证明黎曼猜想这件事](../clips/2026-11-23-dotey-riemann-hypothesis-claude-explainer.md) | 相近 | 弱（模型复核通过） |
