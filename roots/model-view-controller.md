---
name_zh: "模型-视图-控制器（MVC）"
name_en: "Model–view–controller"
proposer: "Trygve Reenskaug（施乐帕洛阿尔托研究中心，Smalltalk-79）"
year: "1979"
type: 方法论
verified: true
---

# 模型-视图-控制器（MVC）（Model–view–controller）

## 一句话

把程序分成三块：模型保存数据和规则，视图只负责把模型呈现出来，控制器接收用户输入去改模型；同一个模型可以同时有多个视图。

## 原始出处

- Model–view–controller，英文维基百科，https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller
- 争议：维基百科只写 1970 年代末；Reenskaug 最初的设计有模型、视图、物件、编辑器四部分，和 Smalltalk 团队讨论后才定为三部分，后来各框架对“视图”“控制器”的定义并不一致。

## 更底层的源头

- [关注点分离](separation-of-concerns.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Tripo Eden：先建地图再渲染](../clips/2026-10-18-svpino-tripo-eden-world-model-map.md) | 相近 | 弱（模型复核通过） |
