---
title: "Dokobot让智能体读登录后网页"
author: "ZEN (@supezen)"
url: https://x.com/supezen/status/2032824859227771011
source: X
published: 2026-03-14 14:23 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

大家好，我的新产品 @dokobot 正式上线 🚀

AI agent 读网页这个难题，现有方案各有各的缺陷：
- Jina Reader / Firecrawl：转 Markdown 不错，但过不了 Cloudflare 反爬，登录页也读不了
- Browserbase / Steel 这类云浏览器：能渲染 JS，但读不了你登录过的 Gmail 和 Notion，输出还是原始 HTML
- Agent-browser / Chrome CDP 方案：权限太大，能注入脚本、读 cookie、操控 DOM，安全隐患多

Dokobot 在 Chrome CDP 基础上增加一层，让 Agent 可以高效且安全的通过你的浏览器来读网页，试图彻底解决这个难题。

Dokobot 利用 CDP 和 Treewalker 技术预处理好页面内容，提供一条安全的通道供 agent 随时查询，避免 agent 直接操作 CDP 注入动态脚本带来安全隐患。

总之你登录了什么它就能读什么，反爬天然免疫，被网站屏蔽的风险也最低，同时输出 AI 可直接消费的 Markdown，最多可节省 99% token。

经过几周的内测后，产品已经基本稳定，现在开放注册，有免费套餐和人类使用彩蛋，欢迎大家体验！期待听到大家的反馈！😊

> 媒体：
> - https://pbs.twimg.com/media/HDYKPhQagAAR3Zs.jpg

## 溯源

