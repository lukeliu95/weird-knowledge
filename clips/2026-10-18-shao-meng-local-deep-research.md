---
title: "本地可跑的深度研究助手项目"
author: "meng shao (@shao__meng)"
url: https://x.com/shao__meng/status/1901422074394247220
source: X
published: 2025-03-16 23:55 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 模型与本地部署
roots: []
---

## 原文

Local Deep Research - AI 驱动研究助手项目，能够使用多个 LLMs 和网络搜索执行深度、迭代式分析,可以在本地运行以保护隐私，或者配置为使用云端 LLMs 以增强功能。

核心功能
1. 高级研究能力
- 自动深度研究并生成智能跟进问题
- 追踪引用并验证信息源
- 多轮迭代分析以实现全面覆盖
- 分析完整网页内容(不仅仅是片段)

2. 灵活的 LLM 支持
- 使用 @ollama 模型进行本地 AI 处理
- 支持云端 LLM(如 Claude, GPT)
- 兼容所有 Langchain 模型
- 可根据需求配置模型选择

3. 丰富的输出选项
- 带引用的详细研究发现
- 全面的研究报告
- 快速摘要以获取快速洞见
- 来源追踪和验证

4. 注重隐私
- 使用本地模型时完全在机器上运行
- 可配置搜索设置
- 透明的数据处理

5. 增强的搜索集成
- 自动选择搜索源:"auto"搜索引擎智能分析查询并选择最合适的搜索引擎
- 集成多种知识源:
  - Wikipedia(一般知识)
  - arXiv(科学论文)
  - PubMed(生物医学文献)
  - DuckDuckGo(网络搜索)
  - SerpAPI(Google搜索结果，需API密钥)
  - Google 可编程搜索引擎(需API密钥)
  - The Guardian(新闻文章，需API密钥)
- 本地 RAG 搜索私人文档

6. 本地文档搜索(RAG)
- 基于向量嵌入搜索本地文档
- 为不同主题创建自定义文档集合
- 保护隐私 - 文档留在本地
- 智能分块和检索
- 兼容多种文档格式(PDF、文本、markdown等)

Web 界面功能
- 仪表板:直观界面启动和管理研究查询
- 实时更新:通过实时更新跟踪研究进度
- 研究历史:访问和管理过去的研究查询
- PDF 导出:下载完成的研究报告为PDF文档
- 研究管理:终止正在进行的研究过程或删除过去的记录

> 媒体：
> - https://pbs.twimg.com/media/GmM1RTxawAAAuy5.jpg

## 溯源

