---
title: "纯代码在 Three.js 生成丛林小径"
author: "Geek (@geekbb)"
url: https://x.com/geekbb/status/2085565091035087192
source: X
published: 2026-08-07 03:14 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 设计与前端
roots: []
---

## 原文

好玩，不用任何外部美术资源，仅靠代码在 Three.js 里程序化生成一条完整的丛林小径场景。

12000 行手写 JavaScript 搭出一条穿越石质废墟和瀑布的丛林小径，场景里没有一张贴图文件、一个模型或一段录音。树叶、树皮、石头、角色皮肤和全部 60 段音频都在加载时由代码算出来。

规模上有 423.8 米长的小径、16 个物种共 100799 株植物、536 块逐块侵蚀的石块，还有 22 根骨骼的程序化角色和 15 次 GPU 烘焙产生的 29 张贴图。

https://t.co/RL4aek2lha

> 媒体：
> - https://video.twimg.com/amplify_video/2085549453621264384/vid/avc1/334x270/bJ2uoR4ndwY1HtDV.mp4?tag=29

## 溯源

