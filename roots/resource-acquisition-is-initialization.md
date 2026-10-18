---
name_zh: "资源获取即初始化（RAII）"
name_en: "Resource acquisition is initialization (RAII)"
proposer: "Bjarne Stroustrup、Andrew Koenig"
year: "1984–1989"
type: 方法论
verified: true
---

# 资源获取即初始化（RAII）（Resource acquisition is initialization (RAII)）

## 一句话

把资源的占用绑定到对象的生命周期上：对象创建时获取，离开作用域时自动按顺序释放，保证不泄漏。

## 原始出处

- The Design and Evolution of C++，Bjarne Stroustrup，1994，https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization

## 更底层的源头

- 已追到基础层，或暂未找到更底层的源头

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [DeepSeek Harness 论文](../clips/2026-10-18-michaelzsguo-deepseek-harness-cordis-paper.md) | 相近 | 强 |
