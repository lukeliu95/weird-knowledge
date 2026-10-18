---
title: "Vercel市场向AI智能体开放"
author: "sitin (@sitinme)"
url: https://x.com/sitinme/status/2028672964951199934
source: X
published: 2026-03-03 03:25 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: Agent 与 Skill
roots: []
---

## 原文

Vercel 把 Marketplace 直接向 AI Agent 开放了。

什么意思？一句话——以后基础设施这块，真的可以全自动了。

以前我们用 Claude Code、Cursor 这些 AI 编程工具，写代码已经很猛了，但真正上线一个项目，最麻烦的从来不是代码本身，而是那一堆“杂事”：
数据库要去注册，Redis 要单独开，认证服务要配，日志监控要接，邮箱服务要申请 API Key……

这些步骤过去基本都得人肉操作。AI 能写业务逻辑，却卡在基础设施这一步。

这次 Vercel 干了一件很关键的事：
不用搞 MCP Server，不用接新协议，直接把自家 CLI 包成一个 AI Skill。

一行命令：
npx skills add vercel/vercel --skill vercel-cli

装完之后，Agent 就可以像人一样“逛 Marketplace”了。

它能做什么？
·自动 discover 有哪些数据库、认证、日志服务
·自动 add 安装 Neon、Upstash 这种服务
·自动注入环境变量
·自动读取接入文档
·自己把集成代码写好

最后部署上线
你只需要说一句：“帮我做个带登录系统的待办 App，部署到 Vercel。”
剩下的流程，理论上 Agent 全跑完。

我觉得这件事的意义，不只是“方便”。也是在说：基础设施正在从“人操作”变成“Agent 可操作”。

以前：API 是给程序用的；文档是给人看的；CLI 是给人敲的

现在必须：返回结构化数据；支持无交互模式；提供机器可读文档；默认假设：调用者可能是 Agent
这其实是 SaaS 形态的一次升级。

未来能不能被 Agent 调用，可能会成为一个产品的生死线。
如果你的服务不能被自动发现、自动安装、自动配置，那在 AI 自动化流程里，它就会被绕开。

目前来说：项目搭建的“时间成本曲线”正在被压平。

过去从 0 到 1 搭一套完整基础设施，可能要 2～3 小时。
未来可能只是一句 prompt。

当部署成本无限接近 0，真正有价值的东西只剩两件：
1.你想解决什么问题
2.你是否有持续迭代能力

代码门槛在下降，基础设施门槛在消失。AI + 可编排基础设施，正在把“做产品”这件事，压缩到极致。

> 媒体：
> - https://video.twimg.com/amplify_video/2028651804830162944/vid/avc1/368x270/AQw0nmm3DzeYvucu.mp4?tag=21

## 溯源

