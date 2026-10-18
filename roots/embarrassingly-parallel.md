---
name_zh: "易并行（尴尬并行）"
name_en: "Embarrassingly parallel"
proposer: "Cleve Moler（自称想出这个词）"
year: "1986"
type: 理论
verified: true
---

# 易并行（尴尬并行）（Embarrassingly parallel）

## 一句话

能几乎不费力地拆成很多互不依赖、不用互相通信的子任务的问题，比如逐帧渲染、蒙特卡洛模拟；这类任务最适合分散到大量机器上同时算。

## 原始出处

- Embarrassingly parallel, Wikipedia（含词源与“适合 BOINC 等志愿计算平台”的说明），https://en.wikipedia.org/wiki/Embarrassingly_parallel
- 争议：这个词最早见于 1986 年一本讲多处理器的书，Cleve Moler 自称是他想出来的。

## 更底层的源头

- [阿姆达尔定律](amdahls-law.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [买两台 DGX 出租视频算力的生意](../clips/2026-10-18-boxmrchen-dgx-video-compute-rental.md) | 换了说法 | 强 |
