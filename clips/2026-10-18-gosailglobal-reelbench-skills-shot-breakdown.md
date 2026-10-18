---
title: "reelbench-skills 拆分镜"
author: "Jason Zhu (@GoSailGlobal)"
url: https://x.com/GoSailGlobal/status/2098939757346918526
source: X
published: 2026-09-13 01:00 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 视频生成
roots: []
---

## 原文

做 AI 视频最容易忽略的一步，其实是先学会拆别人的片

reelbench-skills，上线两天 196 star，Apache 2.0

两个 skill 干两件事

video-shots 拉片：一条成片拆成逐镜头分析表，时长、景别、运镜、画面描述全在一张表里。切点和时长由 ffmpeg 量出来，模型只判断该它判断的四件事，14 道质量门逐条对账

video-sync 合成：画面一边，分镜信息一边，镜头一切信息跟着切，横版竖版各一套布局

最妙的是拉片报告是单文件交互页，内嵌播放器，播放时同步高亮镜头，点镜头就跳，离线双击能开

零 npm 依赖，零 API key，只要 node 和 ffmpeg

Claude Code、Codex 一个脚本软链装好：
git clone 仓库后运行 ./scripts/install.sh

> 媒体：
> - https://video.twimg.com/amplify_video/2098939728657883136/vid/avc1/320x324/zLfp7NzMUtmHJG1d.mp4?tag=16

## 溯源

