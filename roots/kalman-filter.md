---
name_zh: "卡尔曼滤波"
name_en: "Kalman filter"
proposer: "Rudolf E. Kálmán"
year: "1960"
type: 方法论
verified: true
---

# 卡尔曼滤波（Kalman filter）

## 一句话

用“预测、观测、修正”的递推，把带噪声的测量和系统模型合起来，逐步估计一个看不见的状态；是导航、机器人定位和早期 SLAM（扩展卡尔曼滤波 SLAM）的基础工具。

## 原始出处

- A New Approach to Linear Filtering and Prediction Problems, R. E. Kalman, Journal of Basic Engineering 82(1): 35–45, 1960，https://doi.org/10.1115/1.3662552
- Kalman filter，英文维基百科，https://en.wikipedia.org/wiki/Kalman_filter
- 争议：维基百科写明 Thorvald Nicolai Thiele 和 Peter Swerling 更早做过类似的算法，Ruslan Stratonovich 提出过更一般的非线性滤波、卡尔曼滤波是其特例；通常以 Kalman 1960 为出处。

## 更底层的源头

- [控制理论](control-theory.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
