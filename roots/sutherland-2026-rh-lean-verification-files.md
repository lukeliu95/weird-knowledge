---
name_zh: "Sutherland（MIT）整理的黎曼猜想 Lean 证明核验文件页"
name_en: "RH Lean proof: verification files"
proposer: "Andrew Sutherland（MIT 数学系），检查用 Claude Code 跑"
year: "2026"
type: 研究报告
verified: true
---

# Sutherland（MIT）整理的黎曼猜想 Lean 证明核验文件页（RH Lean proof: verification files）

## 一句话

逐项公开核验结果和可复现脚本：175,187 个模块零错误编译；五个主定理只依赖 propext、Classical.choice、Quot.sound 三条标准公理；两个独立内核 nanoda、con-leche 接受全量导出；沙箱重建的导出文件逐字节一致；范围只到狄利克雷 L 函数的广义黎曼猜想。

## 原始出处

- RH Lean proof: verification files，Andrew Sutherland，math.mit.edu，页面更新于 2026-11-22 16:20 UTC，https://math.mit.edu/~drew/grh/
- 争议：个人核验页，不是 MIT 的机构声明；截至 2026-11-22 16:20 UTC，Lean 官方内核对完整导出文件的复查和 lake comparator 端到端两项仍在运行（各模块已逐个通过 Lean 内核）。

## 更底层的源头

- [Lean 证明助手](lean-proof-assistant.md) · 关系：直接源自
- [判断“已在 Lean 里检查过”可不可信的四个问题](buzzard-2026-checked-in-lean.md) · 关系：相近
- [德布鲁因准则（证明要能被小而独立的程序复查）](de-bruijn-criterion.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [帖子称黎曼猜想 Lean 证明“零报错、没人看得懂”（夸大：是社区背书，人还没完全读懂）](../clips/2026-11-23-rachelrifx-riemann-proof-verified-nobody-understands.md) | 直接源自 | 弱（模型复核通过） |
