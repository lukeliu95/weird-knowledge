---
title: "Magpie 的全自动开发流：三个 /loop 把用户反馈变成发版"
author: "Kxians (@xulijian1994)"
url: https://x.com/xulijian1994/status/2119956996279669088
source: X
published: 2026-11-10 00:55 UTC
saved: 2026-11-10
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

Magpie 这个开源项目，最让我震惊的不是产品本身，而是 yetone 搞出来的全自动开发工作流。

他用 Claude Code + Opus 5.5，同时运行三个 /loop：

1. 监控 GitHub Issue、PR 和 Discord，自动处理需求、修复 Bug、审查代码、合并 PR、发布版本。

2. 监控 X 上的产品反馈，先用便宜的模型过滤，再交给 Opus 5.5 处理，有价值的反馈直接进入开发流程。

3. 定期清理代码、检查安全问题、复盘错误，把经验写进 LESSONS.md，避免重复踩坑。

甚至准备了 macOS、Windows、Linux 三套真实测试环境，让 Agent 自己复现和验证 Bug。

这就出现了一种非常离谱的软件开发交互体验。

你现在甚至可以直接在 X 上给 @magpie_router 留言，反馈 Bug 或者提出新需求。

你的反馈可能就这样被自动收集，交给模型分析、修改代码、测试、发版。等新版本发布，更新软件就能用上了。

但我觉得这套工作流真正厉害的地方，是它把软件开发变成了一种用户共创。

光靠 yetone 一个人，不可能照顾到那么多不同 Agent、模型和使用场景。

他只需要把基础架构和自动开发流程搭好，剩下的需求和问题由用户不断提供，Agent 再负责实现和修复。

用户一方面是软件的使用者，另一方面又成了软件的共同创造者。

这和 Deepseek Harness 的插件生态有点像，但我觉得 Magpie 这套模式在产品稳定性上甚至可能更有优势。

Deepseek Harness 是让开发者各自开发插件，而 Magpie 的实际开发仍然集中在 yetone 搭建的统一工程体系里。

用户不需要自己写代码，人人都可以当产品经理。

既能让用户一起推动产品进化，又能让代码规范、架构和质量控制保持统一。

https://t.co/SgZJC5kf9a

## 溯源

