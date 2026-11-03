---
title: "craft-anything：Rust 写的逆向复刻工具"
author: "明子206 (@mingzi206)"
url: https://x.com/mingzi206/status/2117093182441972165
source: X
published: 2026-11-02 03:15 UTC
saved: 2026-11-03
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

逆向工程界这两天杀出一个核弹级 Rust 新项目：craft-anything。

它的定位极其暴力：
不只是看懂封闭软件的代码，而是彻底观测它的底层工作原理，并在理解的基础上，直接帮你克隆重构出一套属于自己的原生软件！

传统 IDA Pro 或 Ghidra 只是把汇编翻译成死板的伪代码，而 craft-anything 走的是系统级全景观测：

· 沙箱内自动抓包与 Hook：丢进一个未知的应用或前端包，它自动记录所有系统调用、内存状态机迁移与网络私有协议
· 拓扑重构架构图：内置符号执行引擎，把乱成一团的 API 请求和事件流，自动还原成清晰的业务架构交互图
· 直接生成骨架代码：结合 Coding Agent，直接输出结构清晰的模块化规范与原生复刻代码

不管是想扒大厂闭源软件的底层私有协议，还是想搞 Clean-Room 净室逆向手搓原生替代品，原本需要几天的人工逆向分析，现在几分钟内搞定。

纯 Rust 打造，内存占用极低。搞安全、逆向和底层架构的兄弟建议直接马住！
👉 开源地址：https://t.co/MZtonZu5Mn #Rust #AI #开源

## 溯源

