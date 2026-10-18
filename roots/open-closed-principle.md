---
name_zh: "开闭原则"
name_en: "Open–closed principle"
proposer: "Bertrand Meyer"
year: "1988"
type: 理论
verified: true
---

# 开闭原则（Open–closed principle）

## 一句话

软件实体应当对扩展开放、对修改封闭：要加新行为时，通过扩展（如新的实现、插件）加进来，而不是改已有的源代码。

## 原始出处

- Open–closed principle，英文维基百科（Meyer, Object-Oriented Software Construction, 1988），https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle
- 争议：Meyer 1988 年的原意靠实现继承；1990 年代起（Robert C. Martin 1996 年的文章是代表）改成“稳定的抽象接口 + 可替换的实现”，两种用法目标和做法不同。Larman 2001 年把它和 Parnas 的信息隐藏联系起来。

## 更底层的源头

- [信息隐藏](information-hiding.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [DeepSeek 仓库开发数据拆解](../clips/2026-10-18-crazyaiagent-deepseek-harness-repo-stats.md) | 相近 | 弱（待 Luke 确认） |
