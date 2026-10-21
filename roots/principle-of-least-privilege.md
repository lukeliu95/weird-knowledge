---
name_zh: "最小权限原则"
name_en: "Principle of least privilege"
proposer: "Jerome Saltzer（与 Michael Schroeder 合写的 1975 年论文让它广为人知）"
year: "1974 / 1975"
type: 理论
verified: true
---

# 最小权限原则（Principle of least privilege）

## 一句话

每个程序、每个有特权的用户，都只应该拿到完成当前工作所需的最少权限，这样一处出问题时不会殃及全局。

## 原始出处

- Wikipedia: Principle of least privilege（引 Saltzer 的原始表述与 Saltzer & Schroeder, The Protection of Information in Computer Systems, 1975），https://en.wikipedia.org/wiki/Principle_of_least_privilege
- 争议：维基百科说原始表述来自 Saltzer，但 Roger Needham 1972 年已讨论过“动态分配权限”，早期 Unix 的 login.c 用完超级用户权限就立刻放弃，也被认为是更早的实例。

## 更底层的源头

- 已追到基础层，或暂未找到更底层的源头

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [OpenAI Dots 放权指南：动作分进 6 个权限区，每周按证据升降](../clips/2026-10-18-choopyplug1-openai-dots-agent-permission-zones.md) | 换了说法 | 强 |
| [常驻 agent 的 6 层结构（推文作者据 OpenAI 资料自制的 PDF）](../clips/2026-10-18-choopyplug1-openai-always-on-agent-six-layers.md) | 相近 | 弱（模型复核通过） |
