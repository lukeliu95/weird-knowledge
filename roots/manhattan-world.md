---
name_zh: "曼哈顿世界假设"
name_en: "Manhattan World assumption"
proposer: "James M. Coughlan, Alan L. Yuille"
year: "1999"
type: 理论
verified: true
---

# 曼哈顿世界假设（Manhattan World assumption）

## 一句话

室内和城市场景大多建在一个三维直角网格上（墙、地、楼面沿三个互相垂直的方向），这个约束强到只凭一张图就能用贝叶斯推断估出观察者的朝向；后来常被放宽成“分段平面”等更一般的场景先验。

## 原始出处

- Manhattan World: Compass Direction from a Single Image by Bayesian Inference, James M. Coughlan & Alan L. Yuille, ICCV 1999（Proceedings of the Seventh IEEE International Conference on Computer Vision），https://doi.org/10.1109/ICCV.1999.790349
- Manhattan World: Orientation and Outlier Detection by Bayesian Inference, Coughlan & Yuille, Neural Computation 15(5), 2003，https://doi.org/10.1162/089976603765202668
- 争议：“曼哈顿世界”这个名字和用贝叶斯推断利用它的做法出自 Coughlan & Yuille 1999；“人造场景由平面和直角构成”的想法更早就被建筑建模等工作使用（例如 Debevec 等 1996 年的 Façade），不是这篇首创。

## 更底层的源头

- [归纳偏置](inductive-bias.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [视频世界模型的长期记忆改用"平面块"来存：一个场景约 10 万块、约 5MB，比逐像素点云小三个数量级，生成几百帧后画面和几何仍连贯](../clips/2026-10-25-he-ppmem-persistent-planar-memory-video-world-models.md) | 直接源自 | 强 |
