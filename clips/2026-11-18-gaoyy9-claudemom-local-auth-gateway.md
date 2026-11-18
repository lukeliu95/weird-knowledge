---
title: "ClaudeMom：拦截官方客户端鉴权的本地网关项目"
author: "加西 (@gaoyy9)"
url: https://x.com/gaoyy9/status/2121854835297567171
source: X
published: 2026-11-15 06:36 UTC
saved: 2026-11-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

卧槽！
刚在 GitHub 刷到个极度狂野的项目 ClaudeMom，我一开始以为这哥们是自己手搓了个高仿 Claude 客户端，仔细一看源码发现格局小了——人家不是做李鬼替李逵，而是直接把真李逵给“催眠”了😂

这哥们的解法堪称“夺舍”： 他用 Tauri 写了个本地伪装网关，直接拦截官方原版客户端的鉴权请求。当官方客户端联网查岗时，本地直接假传圣旨：“已登录！满血权限全开！” 
https://t.co/N2PiVHLDEv

## 溯源

