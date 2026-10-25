---
name_zh: "同时定位与建图（SLAM）"
name_en: "Simultaneous localization and mapping (SLAM)"
proposer: "Randall Smith、Peter Cheeseman 奠定统计基础；Hugh Durrant-Whyte 等发展和推广"
year: "1986"
type: 方法论
verified: true
---

# 同时定位与建图（SLAM）（Simultaneous localization and mapping (SLAM)）

## 一句话

机器人在未知环境里一边移动、一边建地图、一边用这张地图确定自己的位置；核心难题是地图元素怎么表示、新观察对应哪个旧元素（数据关联），以及地图越来越大时的计算量和地图管理。

## 原始出处

- On the Representation and Estimation of Spatial Uncertainty, Randall C. Smith & Peter Cheeseman, The International Journal of Robotics Research 5(4), 1986，https://doi.org/10.1177/027836498600500404
- Simultaneous Localization and Mapping: Part I, Hugh Durrant-Whyte & Tim Bailey, IEEE Robotics & Automation Magazine 13(2), 2006（教程综述），https://doi.org/10.1109/MRA.2006.1638022
- Simultaneous localization and mapping，英文维基百科，https://en.wikipedia.org/wiki/Simultaneous_localization_and_mapping
- 争议：没有单一提出者：统计基础常追到 Smith & Cheeseman 1986；按维基百科，SLAM 这个缩写出自 1995 年 ISR 上的论文 “Localization of Autonomous Guided Vehicles”；Durrant-Whyte 的团队在 1990 年代初做了大量开创性工作。

## 更底层的源头

- [卡尔曼滤波](kalman-filter.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [视频世界模型的长期记忆改用"平面块"来存：一个场景约 10 万块、约 5MB，比逐像素点云小三个数量级，生成几百帧后画面和几何仍连贯](../clips/2026-10-25-he-ppmem-persistent-planar-memory-video-world-models.md) | 相近 | 弱（模型复核通过） |
