---
name_zh: "时空可组合性编程范式（Cordis 论文）"
name_en: "A Programming Paradigm for Spatiotemporal Composability"
proposer: "Yifan Shi、Wei Zhang、Tianyi Cui（北京大学、DeepSeek-AI）"
year: "2026"
type: 论文
verified: true
---

# 时空可组合性编程范式（Cordis 论文）（A Programming Paradigm for Spatiotemporal Composability）

## 一句话

把动态组合拆成两个维度：时间可组合（组件移除时副作用能完整撤销）和空间可组合（组件声明依赖、运行时响应式管理），用可撤销效应和响应式余效应形式化，并实现为 Cordis 框架。

## 原始出处

- A Programming Paradigm for Spatiotemporal Composability，Yifan Shi, Wei Zhang, Tianyi Cui，arXiv:2608.25512，2026-08-26，https://arxiv.org/abs/2608.25512
- Cordis 代码仓库，https://github.com/cordiverse/cordis
- 争议：预印本，仍在修订，未经同行评审。推文称这套架构由 Shigma（孤梦星影）带来，论文第一作者是否就是他本人，待确认。

## 更底层的源头

- [效应系统](effect-system.md) · 关系：直接源自
- [余效应：依赖上下文的计算演算](petricek-2014-coeffects-context-dependent.md) · 关系：直接源自
- [依赖注入](dependency-injection.md) · 关系：相近
- [资源获取即初始化（RAII）](resource-acquisition-is-initialization.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [DeepSeek Harness 论文](../clips/2026-10-18-michaelzsguo-deepseek-harness-cordis-paper.md) | 直接源自 | 强 |
