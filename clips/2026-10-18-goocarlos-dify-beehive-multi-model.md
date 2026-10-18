---
title: "Dify 蜂巢架构支持多模型多模态"
author: "Luyu Zhang (@goocarlos)"
url: https://x.com/goocarlos/status/1749841768731038078
source: X
published: 2024-01-23 17:09 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: Agent 与 Skill
roots: []
---

## 原文

过去两周，Dify 支持了一系列新模型，包括 Gemini、GLM 4 以及 Ollama、AWS Bedrock 等托管平台。我其实已经数不清了。

得益于 0.4.X 版本中引入的“Beehive”架构，我们在多模型、多模态上的可插拔行达到了业界最佳水平：
- 多模态原生
- 通过 YAML 文件即可在两个小时内接入新模型
- LLM、TTS、ASR、Embedding、ReRank 多种模型的支持
- 商业 或 通过MaaS 托管/自部署方式的开源模型

这些对于企业级用户都尤为重要。但更重要的是，2024 年会是多模型、多模态繁荣的一年，我们在工程上做好了准备。

> 媒体：
> - https://pbs.twimg.com/media/GEio8Gva0AA24P6.jpg

## 溯源

