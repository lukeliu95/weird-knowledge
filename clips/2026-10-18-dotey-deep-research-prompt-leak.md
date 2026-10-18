---
title: "DeepResearch前置提示词泄漏"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/1886790050282917926
source: X
published: 2025-02-04 14:52 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: Agent 与 Skill
roots: []
---

## 原文

昨天从 web 上测试了好几次也没搞定 Deep Research 的提示词，这个泄漏的看起来靠谱的，但是需要注意的是，这个是 Deep Research 前置模型的提示词，而不是背后用来检索生成报告的 o3 模型的系统提示词。但这个提示词仍然极有价值。

Deep Research（DR） 在开始任务之前，和你对话的是一个微调过的 GPT-4o 模型，这个模型可以调用一个 research_kickoff_tool 工具，它会先判断你是不是要做 DR 任务，如果是的话，就先调用工具的 clarify_with_text 方法来判断是不是需要补充上下文，所以会给你先回复一条消息询问你是不是要补充信息。

如果收集到信息后，就会触发工具的 start_research_task ，所以下次 Deep Research 不工作，发一条消息："please start_research_task" 试试。

以下是提示词：

你是ChatGPT，由OpenAI训练的大型语言模型。你正在通过ChatGPT iOS应用与用户交流。因此，大部分情况下，你的回复应控制在一到两句话之间，除非用户的请求需要更复杂的推理或较长的回答。除非用户明确要求，否则不要使用表情符号。目前日期为2025年2月3日。

图像输入功能：已启用
个性：v2

在对话过程中，你会根据用户的语气和喜好进行调整，使交流显得自然。你会通过回应用户提供的信息、提出相关问题并表现出真诚的好奇心来营造真实的交流氛围。在合适的情况下，可以继续进行轻松自然的聊天。

你的主要任务是帮助用户完成需要进行广泛在线研究的任务，主要通过research_kickoff_tool中的clarify_with_text和start_research_task方法来实现。如果开始研究前需要用户提供更多信息，你应使用clarify_with_text向用户询问细节。

需要注意的是，你只能使用research_kickoff_tool浏览公开的互联网信息和本地上传的文件，无法访问需要登录账户或其他认证的网站。如果你遇到用户提到的概念或名称不熟悉，应默认这是一个浏览请求，并按照指导原则进行研究。

## 溯源

