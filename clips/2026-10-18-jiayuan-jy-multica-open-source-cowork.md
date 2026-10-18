---
title: "Multica：开源本地版Cowork"
author: "Jiayuan (JY) Zhang (@jiayuan_jy)"
url: https://x.com/jiayuan_jy/status/2012040329407713404
source: X
published: 2026-01-16 05:52 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 编程智能体
roots: []
---

## 原文

分享我们最近实现的一个开源版本 Claude Cowork

Multica 👇
https://t.co/NzqZmZd3ao

完全本地化、同时支持 Claude Code、Codex 以及开源的 @opencode 。

Multica 的目标是成为 coding agent 和终端用户的中间层，有点类似 Obsidian 的模式，每个人都可以根据自己的工作流使用插件的方式来定制化。

Multica + 开发相关插件 -> Cursor/Lovable/Conductor
Multica + 设计相关插件 -> Lovart
Multica + Research 相关插件 -> NotebookLM

Multica 会完成中间层：
- UIUX 交互
- VM & Sandbox
- 多 agent & llm 编排调度
- 插件商店

这个名字的灵感来自于 Multics（Multiplexed Information and Computing Service，多路复用信息与计算服务），这是一个创建于 1964 年的开创性操作系统。

尽管 Multics 最终没有广泛普及，但它奠定了现代操作系统的基础，包括层级文件系统等概念。Unix 本身就是从 Multics 衍生而来的（Uniplexed Information and Computing Service -> Unics -> Unix）。

现在还是一个非常早期的预览版本，欢迎大家参与来一起构建。

视频中的例子是我让 Multica 下载 Ilya Sutskever 推荐的论文，并创建一个网页 & 综述，整体运行时间大概在 20min。

> 媒体：
> - https://video.twimg.com/amplify_video/2012037177610231808/vid/avc1/378x270/pyOaNuqpXtGTtC9S.mp4?tag=21

## 溯源

