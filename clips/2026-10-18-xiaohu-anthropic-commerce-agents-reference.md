---
title: "Anthropic 开源电商智能体"
author: "小互 (@xiaohu)"
url: https://x.com/xiaohu/status/2095443120477647114
source: X
published: 2026-09-03 09:25 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

Anthropic 开源了其一套可运行的 AI 电商 Agents 参考实现

让电商平台、零售商和开发者在几天内快速搭建出真正能卖货、能管店的 AI Agent...

Anthropic 称，使用 Claude 购物 Agent 的零售商，购物车金额最高增加 35%，消费者完成购买的可能性提高 60%。

这套参考实现包含 Shopping Agent、Merchant Agent、十个 Skills、四个行业示例和三种运行方式

并演示了业务工具、呈现组件、记忆、安全审批和评测的实现。

Commerce Agents 仓库 包含以下内容：

两个 Agent：Shopping Agent 与 Merchant Agent

1. 面向消费者的“导购智能体”（Shopping Agent）
这相当于直接嵌在你的网站或 App 里的 24 小时贴身金牌导购

2. 面向运营者的“掌柜智能体”（Merchant Agent）
这个智能体是给商家老板和运营人员用的后台军师

10个 Skills：两类 Agent 各五个，覆盖搜索、购买研究、规划、客服、个性化、经营分析、商品、库存、定价促销和营销活动

四个可运行行业示例：零售、旅行、电信和娱乐票务。每个示例都有消费者前台和商家后台

三种运行方式：Messages API、Claude Agent SDK 和 Claude Managed Agents

七个本地 Python 包、八个 Web 应用、共享后端接口、前端组件、测试和部署脚本

一个 Claude Code 插件，提供搭建 Agent、增加业务流程、编写 Evals 和审查现有 Agent 的命令

> 媒体：
> - https://video.twimg.com/amplify_video/2095442837651501056/vid/avc1/550x270/95-3vvNg-tb-ffJ0.mp4?tag=29

## 溯源

