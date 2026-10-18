---
title: "阿里ViDoRAG：能读图表的RAG"
author: "AIGCLINK (@aigclink)"
url: https://x.com/aigclink/status/1896468397619380512
source: X
published: 2025-03-03 07:51 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

阿里巴巴通义实验室刚刚开源了一个面向视觉文档的RAG系统：ViDoRAG，ViDoRAG在GPT-4o上准确率达到了 79.4%，比传统RAG提高了10%以上

它可以在一堆包含图片文档中找到，比如“这个产品的最高温度是多少？”或者“这篇文章主要讲了什么？”，

ViDoRAG能看文字、看图片、看图表，核心是它基于高斯混合模型的多模态混合检索策略，及多智能体迭代推理机制，来提升模型在视觉丰富文档上的检索和推理能力

多智能体协作：
1、Seeker，负责快速浏览文档，找出可能相关的图片或页面
2、Inspector，仔细检查Seeker找到的内容，判断是否真的有用，提出进一步建议
3、Answer Agent，根据Inspector的结果给出准确的答案

此外还开源了一个专注于大规模数据文档集合下的检索和复杂推理的数据集，ViDoSeek

用来测试ViDoRAG，里面包含文本、图表、表格、布局等各种各样的问题和对应的答案，每个问题都有唯一的答案，并且指明了答案在文档的哪一页

各个模块像检索器、推理代理和生成器都是独立设计的，可以根据需要进行替换或修改

#RAG #图像RAG #视觉文档RAG #ViDoRAG

> 媒体：
> - https://pbs.twimg.com/media/GlGaqXxa0AABjp_.jpg

## 溯源

