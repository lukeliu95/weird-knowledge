---
name_zh: "失效安全默认（默认拒绝）"
name_en: "Fail-safe defaults"
proposer: "Jerome H. Saltzer、Michael D. Schroeder（成文）；据他们的论文，E. Glaser 1965 年最早提出"
year: "1975（据论文，1965 年已有人提出）"
type: 理论
verified: true
---

# 失效安全默认（默认拒绝）（Fail-safe defaults）

## 一句话

能不能做，要按"明确允许"来决定，而不是按"明确禁止"：默认什么都不能做，只有写明的条件下才放行。这样设计时漏想了某种情况，结果是拒绝而不是放行，错误也更容易被发现。

## 原始出处

- The Protection of Information in Computer Systems，Jerome H. Saltzer、Michael D. Schroeder，Proceedings of the IEEE 63(9):1278-1308，1975（设计原则第 2 条 Fail-safe defaults），https://doi.org/10.1109/PROC.1975.9939
- 同上，网页全文，https://www.cs.virginia.edu/~evans/cs551/saltzer/
- 争议：常引的成文出处是 Saltzer 与 Schroeder 1975 年的论文，但论文自己说这条原则是 E. Glaser 在 1965 年提出的。

## 更底层的源头

- [最小权限原则](principle-of-least-privilege.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [OpenAI Dots 放权指南：动作分进 6 个权限区，每周按证据升降](../clips/2026-10-18-choopyplug1-openai-dots-agent-permission-zones.md) | 换了说法 | 强 |
