---
title: "TuriX-CUA：能操作桌面的智能体"
author: "sitin (@sitinme)"
url: https://x.com/sitinme/status/2030507553172451567
source: X
published: 2026-03-08 04:55 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

最近逛 GitHub，又挖到一个挺有意思的项目，叫 TuriX-CUA。这东西很适合拿来给 OpenClaw 这种 Agent 当“手”和“眼睛”。

它本质上不是那种只能在网页里点点 DOM 的自动化工具，也不是传统那种死板的 RPA。

更像一个真正的 Computer Use Agent：能看屏幕、理解桌面环境、自己决定下一步点哪里、输什么、切哪个应用。

也就是说，只要是人能在电脑上完成的操作路径，理论上它就有机会复现，不一定非要对方开放 API。

现实世界里，很多软件压根没有 API，或者 API 很残、很封闭。你想让 Agent 真正帮你干活，最后一定会遇到“系统不开放”的墙。

到了这一步，能不能直接像人一样操作电脑，基本就决定了 Agent 到底只是个聊天机器人，还是一个真的能交付结果的数字员工。TuriX 这类框架，本质上就是在补这一块。

它会把职责拆成了 brain、planner、actor、memory 这几个角色。

未来真正好用的 Agent，大概率都不会是“一个模型包打天下”，而是不同模块各司其职：大模型负责判断和决策，小模型负责执行、记忆、压成本。这样不仅更灵活，也更接近一个可长期维护的 Agent 系统，而不是一次性的 demo。

对玩 OpenClaw、Claude Code 这类工具的人来说，这种项目尤其值得关注。

Agent 真正的天花板，很多时候不是“它会不会想”，而是“它能不能动手”。代码会写、规划会做、文档会总结，这些大家已经很熟了。

接下来真正拉开差距的，是谁能把 Agent 从命令行、浏览器，进一步扩展到整个桌面环境。谁先把这层打通，谁的自动化能力就会直接上一个台阶。

> 媒体：
> - https://pbs.twimg.com/media/HCshMzRbcAA1b3o.jpg
> - https://pbs.twimg.com/media/HCshTwDaIAAG2l5.jpg

## 溯源

