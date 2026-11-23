---
name_zh: "Alpöge 与 Claude 的黎曼猜想 Lean 证明（公告与代码）"
name_en: "Remark (announcement of a Lean proof of the Riemann Hypothesis)"
proposer: "Levent Alpöge（Anthropic）与 Claude"
year: "2026"
type: 论文
verified: true
---

# Alpöge 与 Claude 的黎曼猜想 Lean 证明（公告与代码）（Remark (announcement of a Lean proof of the Riemann Hypothesis)）

## 一句话

2026-11-20 公布：和 Claude 一起找到并形式化了黎曼猜想及狄利克雷 L 函数的广义黎曼猜想的证明，只发 Lean 代码（约 1700 万行，分 14 个压缩包），不发 25 万多页“不可读”的文字稿；作者自己说还没吃透证明周边的大片数学，打算以后写清楚。

## 原始出处

- Remark（4 页公告），Levent Alpöge，2026-11-20，https://alpo.ge/remark.pdf
- Lean 源码压缩包第 1 部分（共 14 部分，part01–part14），https://alpo.ge/lean.tar.gz.part01
- Deicyde/riemann-hypothesis：源码镜像（除新增的 Comparator 文件外与原压缩包逐字节相同），https://github.com/Deicyde/riemann-hypothesis
- TechCrunch：AI claimed a solution to the 167-year-old Riemann hypothesis — and a human did, too，2026-11-20（作者任职 Anthropic），https://techcrunch.com/2026/11/20/ai-claimed-a-solution-to-the-167-year-old-riemann-hypothesis-and-a-human-did-too/
- 争议：remark.pdf 没写行数，“1700 万行”出自 Lean 社区声明和 Baez 等的转述；作者在 Anthropic 工作，发布在 Anthropic 上市次日，Granville 批评过时机和 4 页说明不清楚（据维基百科）；证明的数学思路尚未被人完整读懂。

## 更底层的源头

- [黎曼猜想](riemann-hypothesis.md) · 关系：直接源自
- [斯捷潘诺夫方法（用带重数的辅助构造证明有限域上曲线的黎曼猜想）](stepanov-method.md) · 关系：直接源自
- [Lean 证明助手](lean-proof-assistant.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Lean FRO 和 Mathlib 发声明：验证了黎曼猜想的 Lean 证明](../clips/2026-11-23-leanprover-lean-mathlib-statement-riemann-proof.md) | 直接源自 | 强 |
| [5 分钟讲清 Claude 参与证明黎曼猜想这件事](../clips/2026-11-23-dotey-riemann-hypothesis-claude-explainer.md) | 直接源自 | 强 |
| [帖子称黎曼猜想 Lean 证明“零报错、没人看得懂”（夸大：是社区背书，人还没完全读懂）](../clips/2026-11-23-rachelrifx-riemann-proof-verified-nobody-understands.md) | 直接源自 | 强 |
