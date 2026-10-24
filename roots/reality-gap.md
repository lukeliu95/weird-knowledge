---
name_zh: "现实鸿沟（仿真到现实差距）"
name_en: "Reality gap (sim-to-real gap)"
proposer: "Nick Jakobi、Phil Husbands、Inman Harvey（“reality gap”一说）；深度学习时代由 Tobin 等推广"
year: "1995"
type: 理论
verified: true
---

# 现实鸿沟（仿真到现实差距）（Reality gap (sim-to-real gap)）

## 一句话

在仿真里训练或演化出来的机器人控制器搬到真实硬件上常常失灵，这道落差叫现实鸿沟；Jakobi 等发现在仿真里加接近真实的噪声能让表现对得上，Tobin 等用“域随机化”把仿真参数打乱，让真实世界在模型眼里只是又一种变化。

## 原始出处

- Noise and the reality gap: The use of simulation in evolutionary robotics，Jakobi, Husbands & Harvey，ECAL 1995（LNCS 929），pp. 704–720，DOI 10.1007/3-540-59496-5_337，https://doi.org/10.1007/3-540-59496-5_337
- Domain randomization for transferring deep neural networks from simulation to the real world，Tobin, Fong, Ray, Schneider, Zaremba & Abbeel，IROS 2017，pp. 23–30，DOI 10.1109/IROS.2017.8202133，https://doi.org/10.1109/IROS.2017.8202133
- Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey，Zhao, Peña Queralta & Westerlund，IEEE SSCI 2020，pp. 737–744，DOI 10.1109/SSCI47803.2020.9308468，https://doi.org/10.1109/SSCI47803.2020.9308468
- 争议：仿真不可靠的问题在进化机器人领域更早就有人指出（Jakobi 等 1995 的摘要自己说“已被认识到”），“reality gap”这个说法因这篇的标题流行，最早是谁说的没有逐一核实；“sim-to-real”的叫法在深度强化学习兴起后（Tobin 等 2017、Zhao 等 2020）才普及。

## 更底层的源头

- [数据集偏移](dataset-shift.md) · 关系：相近
- [迁移学习（机器学习）](transfer-learning.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [模拟用户给 agent 开了"简单模式"：451 名真人跑完整 τ-bench，对照 31 个大模型模拟器，模拟用户太配合、打分太宽，最好的也只有 76 分（真人 93 分）](../clips/2026-10-22-zhou-sim2real-gap-user-simulation.md) | 直接源自 | 强 |
