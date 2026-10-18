---
title: "阿里PageAgent：让网页听AI指挥"
author: "爱丽丝呀！ (@BTCqzy1)"
url: https://x.com/BTCqzy1/status/2033773816363815019
source: X
published: 2026-03-17 05:13 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: Agent 与 Skill
roots: []
---

## 原文

阿里开源的新项目霸占了 GitHub Trending 榜单：PageAgent。

一行代码，让任意网页秒变 AI Agent 可控工具。开源后迅速爆火，GitHub Star 数飙至 9.6k+，Fork 747 次，热度还在疯狂飙升中！

一句话概括：阿里给你的网站装上了一个真正的“AI 暴力操作员”。

大多数 AI 网页助手还在折腾脆弱的浏览器插件或者笨重的 Python 爬虫，阿里 PageAgent 做了一件极狠的事——彻底抛弃 OCR 和无头浏览器，直接用纯前端 JS 把网站变成 AI Native App。

核心逻辑极其优雅：Text-based DOM 操作，跳过截图，直达底层。

一行脚本集成 → 纯文本 DOM 提取 → 自然语言控制 → 闭环操作验证

与其让 Agent 去对抗像素级的 UI 变化，不如直接把网页变成结构化的文本流。这种“脱水分析”方式，让 AI 能够像读代码一样读懂网页，操作比人类更快、比视觉 Agent 更准、稳如磐石。

核心杀手锏：

1.阿里级极简接入：Demo 版只需一行 <script> 标签就能快速体验（评估使用）；生产环境推荐 NPM 安装 + 接自己的 LLM（支持 OpenAI 兼容、本地模型、Ollama 等），无需 Browser Extension 和 Python。

2.拒绝截图 OCR：不靠截图、不耗多余 Token，直接基于 DOM 树进行逻辑操作。完美适配复杂的 B2B 系统、ERP 和 Admin 后台。

3.闭环执行：以前需要 20 次点击、3 次跳转的繁琐流程，现在用户只需说一句话，PageAgent 在网页内部自动完成所有点击、输入和提交。

已覆盖各种 Web 应用场景，通过高强度测试。Demo 适合快速试用，正式集成后可用于生产级网页增强。今天的网页服务于人类的视觉，明天的网页将是 Agent 的操作场。

#AI编程 #Alibaba #PageAgent #GitHub #Cursor
传送门：https://t.co/U4wcFwOtay

## 溯源

