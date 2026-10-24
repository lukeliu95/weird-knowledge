---
title: "OpenAI FDE 实战：Codex 变强后删掉九成定制代码"
author: "Xudong Han (@Xudong07452910)"
url: https://x.com/Xudong07452910/status/2113415101877559707
source: X
published: 2026-10-22 23:40 UTC
saved: 2026-10-24
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: AI 产品与创业
roots: [forward-deployed-engineer, bitter-lesson, modularity-theory, anthropic-2025-agent-skills, openai-2025-ai-in-the-enterprise]
---

## 原文

非常推荐读一下 OpenAI FDE 负责人 Colin Jarvis 今天发的这篇工程博客！

他们的 FDE 团队花了几个月给客户做 AI 系统，结果 Codex 变强后，直接删掉了约 90% 的定制代码。

文章用一个半导体客户的真实项目，讲清楚了 FDE 到底在做什么。

工程师直接深入客户团队，跟芯片专家一起设计 Eval、搭建 Harness，把 AI 真正用到芯片验证和调试流程里。

在这个行业，验证约占项目工作量的 70%。前 3–6 个月，几个场景都上了生产：定向测试生成节省约 48% 的时间，几周的调试被压缩到几小时。

但项目上线只是第一步。

随着 Codex 能力提升，团队把原来的定制应用逐步改造成通用 Harness 上的 Skills 和插件。Codex 本身成了交互界面，原来各场景单独写的终端界面和命令行工具全部退役。

扩展到新团队时，基本只需要换上新的连接器和 MCP，再用一个 Skill 生成新的 Eval。第一次部署花了两个月，复制到第二个团队只用了一天。

而当模型能力不够时，FDE 还要把真实业务中的失败案例和能力缺口反馈给 Research。一家电信客户做语音客服，模型一开始在关键 Eval 上只有约 60%，六个月里随着新模型迭代涨到 90% 以上，才达到上线标准。

我很喜欢作者提到的一个目标：让 FDE 不断减少别人对自己的依赖。

我觉得企业 Agent 项目里真正留得下来的，是 Eval、失败案例和沉淀成 Skill 的业务知识；为了补模型短板写的胶水代码，每次模型升级都该重新审一遍，随时准备删。

做企业 AI 落地的建议先收藏。如果你每接一个新客户都还在从头写一套，说明东西还停在定制应用这一层，没沉淀下来。

原文：https://t.co/IQt7Ssve87

## 溯源

- 核心主张：基础模型变强后，为补模型短板写的定制代码和界面大多可以删掉；企业 AI 项目里真正留得下来的是评测集、真实失败案例和沉淀成 skill 的业务知识，FDE 把它们装进通用 harness，复制到新团队就从两个月缩到一天，模型不够时再把失败反馈给研究团队。
- 源知识：
  - [前线部署工程师](../roots/forward-deployed-engineer.md) · 关系：直接源自 · 强弱：强。讲的就是 OpenAI 前线部署工程师团队怎么驻进客户团队、和芯片专家一起设计 eval、搭 harness。原文（openai.com/index/forward-deployed-engineering-means）2026-10-24 对抓取返回 403，没读到原文，只依据推文转述。
  - [苦涩的教训](../roots/bitter-lesson.md) · 关系：相近 · 强弱：弱（模型复核通过）。模型一升级、手写的胶水代码就该删，和“苦涩的教训”一致：长期看随算力变强的通用方法胜过把人的领域技巧写死进系统。推文没引它。
  - [相互依赖与模块化理论](../roots/modularity-theory.md) · 关系：相近 · 强弱：弱（模型复核通过）。模型“不够好”时只能一个场景一个场景写一体化定制应用；够用以后，换连接器、MCP、skill 这种标准接口的模块化做法胜出，复制成本骤降（两个月到一天）。
  - [用 Agent Skills 让智能体胜任真实工作](../roots/anthropic-2025-agent-skills.md) · 关系：直接源自 · 强弱：弱（模型复核通过）。把业务知识和做法打包成 skill 挂在通用 agent 上、用代表性任务找能力缺口再补进 skill，就是 Agent Skills 的思路；推文说的是 Codex 上的 Skills 和插件。
  - [OpenAI《企业中的 AI：七家前沿公司的经验》](../roots/openai-2025-ai-in-the-enterprise.md) · 关系：相近 · 强弱：弱（模型复核通过）。同一家公司 2025 年企业落地指南的第一条经验就是“先做评估”；这里把 eval 和失败案例当成最值钱、最留得住的资产，是同一主张的实战版。
- 本质：这条新知识本质上是“苦涩的教训”和“模块化理论”在企业 AI 落地上的应用：模型够强以后，定制胶水代码贬值，评测、失败案例和沉淀成 skill 的业务知识才是留得住的资产。
- 整理于：2026-10-24（第 6 轮）
