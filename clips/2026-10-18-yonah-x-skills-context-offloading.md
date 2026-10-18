---
title: "Agent Skills 是上下文卸载"
author: "汉松 (@Yonah_x)"
url: https://x.com/Yonah_x/status/1979030811656573183
source: X
published: 2025-10-17 03:44 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

Claude 的 Agent Skills 本质上是一种“上下文卸载”，把冗长的技能信息移出上下文，按需加载。巧的是最近 Manus 的 Peak 也分享一些“上下文卸载”的技巧。Manus 有很多工具，但是并不会把这些工具的完整定义告诉模型。那它怎么知道有哪些工具，又怎么调用它们呢？想象一下，给你一台新电脑，你怎么知道有哪些工具能用？普通用户会打开应用程序的列表，程序员会 `ls /usr/bin` 看一下有哪些命令可以用。

同样的，Manus 的解法是在系统提示词中，告诉模型在某个特定文件夹里，有许多预装的命令行实用工具。那些最常用的工具（ls、grep、cat、less、more等），就默认内置在系统提示里面的。不需要告诉模型如何使用这些工具，只需要列出工具名，然后告诉它可以使用 --help 参数来了解如何使用工具。最妙的是这些 shell 操作模型都是学过的，所以它的泛化能力很强，要加新的工具只需要往文件夹里面放一个命令就行。

我发现 Manus 真的是把 Unix 哲学贯彻到底了：KISS（Keep It Simple, Stupid）。

> 媒体：
> - https://pbs.twimg.com/media/G3bqREpWkAAE-Qx.png

## 溯源

