---
title: "RAG 准确率从 45% 提到 98%"
author: "Y11 (@seclink)"
url: https://x.com/seclink/status/1796502273197314545
source: X
published: 2024-05-31 11:21 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

OpenAI分享他们在RAG技术的最佳实践：

客户需求：他们有大量文档（比如10万份），希望模型只基于这些文档进行知识检索。

解决方案：
1.  直接将PDF和docx文件嵌入，准确率是45%。

2. 经过20次调优迭代，解决细节小Bug - 准确率到65%

3. 基于规则进行优化，譬如先判断问题属于什么领域（退一步思考），然后再回答，效果提升到85%

4. 发现数据里有一些是结构化数据（如表格），为此定制提取解决，准确率提升到98%。

视频地址：https://t.co/3w1NMti0M5

> 媒体：
> - https://pbs.twimg.com/media/GO50fqdbEAACXo3.jpg

## 溯源

