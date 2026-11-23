---
name_zh: "德布鲁因准则（证明要能被小而独立的程序复查）"
name_en: "de Bruijn criterion"
proposer: "Henk Barendregt 命名（纪念 Nicolaas de Bruijn），成文见 Barendregt 与 Freek Wiedijk"
year: "2005"
type: 方法论
verified: true
---

# 德布鲁因准则（证明要能被小而独立的程序复查）（de Bruijn criterion）

## 一句话

证明助手应能把证明导出成只用少数逻辑规则写成的“证明对象”，别人用自己写的小检查程序就能独立复查；这样不必信任生成证明的那套大系统。Lean 和 Coq 都能做到。

## 原始出处

- The challenge of computer mathematics，Henk Barendregt、Freek Wiedijk，Phil. Trans. R. Soc. A 363: 2351–2375，2005，https://doi.org/10.1098/rsta.2005.1650
- De Bruijn criterion，维基百科，https://en.wikipedia.org/wiki/De_Bruijn_criterion
- The de Bruijn criterion vs the LCF architecture，Lawrence Paulson，2022（引用了 Barendregt 与 Wiedijk 的定义原文），https://lawrencecpaulson.github.io/2022/01/05/LCF.html
- 争议：名字是 Barendregt 起的，不是 de Bruijn 本人提的；据检索摘要 Barendregt 1998 年在 FOM 邮件列表里已用过这个说法，本轮没读原帖。

## 更底层的源头

- [柯里–霍华德对应（证明即程序）](curry-howard-correspondence.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Lean FRO 和 Mathlib 发声明：验证了黎曼猜想的 Lean 证明](../clips/2026-11-23-leanprover-lean-mathlib-statement-riemann-proof.md) | 相近 | 弱（模型复核通过） |
