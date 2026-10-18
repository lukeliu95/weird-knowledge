---
title: "OpenClaw的底层引擎Pi是什么"
author: "苏打白.Dev (@sodawhite_dev)"
url: https://x.com/sodawhite_dev/status/2019932622298775834
source: X
published: 2026-02-07 00:34 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

OpenClaw的底层是Pi

Pi是什么？

Pi 是 OpenClaw 的核心底层引擎（Agent Engine），提供以下基础能力：
模型抽象 - 统一接口调用不同大模型（Claude、GPT、Gemini 等）
流式推理 - 实时响应的推理机制
Agent Loop - 思考-行动-观察的循环架构
工具执行 - Read/Write/Edit/Bash 等基础工具的原语支持

关系类比
Pi = 汽车的引擎（让它能跑起来）
OpenClaw = 车身+交通规则（会话管理、IM 集成、工具链、沙箱等）
Pi 的设计哲学是"核心极小，但能长出来"——底层能力收敛到最少的原语，但可通过插件和工具链无限扩展。

> 媒体：
> - https://video.twimg.com/amplify_video/2019812123745161216/vid/avc1/480x270/2Hy_SqSMg3zG5glU.mp4?tag=21

## 溯源

