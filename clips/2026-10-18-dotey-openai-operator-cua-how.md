---
title: "Operator靠CUA操作屏幕的原理"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/1883005723493199999
source: X
published: 2025-01-25 04:15 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [openai-2025-computer-using-agent, intelligent-agent, wei-2022-chain-of-thought-prompting, yao-2022-react, robotic-process-automation, human-in-the-loop]
---

## 原文

OpenAI Operator 的工作原理

为 Operator 提供支持的是 Computer-Using Agent (CUA)，它结合了 GPT-4o 的视觉能力与通过强化学习获得的高级推理能力。

当用户向 Operator 网页发送请求的时候，Operator 会启动一个用户专属的虚拟主机（这也可能是为什么现在只能面向 pro 用户的原因之一），这个虚拟机上装了一个 Chrome 浏览器，并且 Session、Cookie 会一直给你保留。

虚机的截图会同步到 Operator 网页，所以网页上可以实时看到网页操作的情况。CUA 根据系统提示词+用户输入的任务+当前任务状态+截图会借助 CoT 思考生成可以执行的 Actions，由于系统提示词包含了一系列品目操作的指令，比如鼠标移动、点击、拖动等等，最终这些 Action 会编程屏幕操作的指令，这样 CUA 就可以操作屏幕了。

只是我没搞明白的是，多模态是怎么精准获取坐标位置的？

CUA 通过处理原始像素数据来理解屏幕上发生的内容，并通过虚拟的鼠标和键盘来执行操作。它能够进行多步骤的任务导航、处理错误并适应意外变化。这让 CUA 能够在各种数字环境中行动，例如填写表单、浏览网站，而无需使用专门的 API。

在接收到用户指令后，CUA 通过一个融合感知、推理和动作的迭代循环来执行操作：

- 感知（Perception）：从计算机截取的屏幕截图会加入到模型的上下文中，为模型提供当下计算机状态的视觉快照。
- 推理（Reasoning）：CUA 使用链式思考（chain-of-thought）来推断下一步的行动，同时考虑当前和过去的屏幕截图及操作。这种“内在独白”有助于模型评估观察结果、跟踪中间步骤并进行动态调整，从而提升任务完成度。
- 动作（Action）：模型执行点击、滚动或键入等操作，直到它判断任务已完成或需要用户进一步输入。虽然大多数步骤能自动完成，但在遇到敏感操作（例如输入登录信息或回答 CAPTCHA 等）时，CUA 会请求用户进行确认。

> 媒体：
> - https://pbs.twimg.com/media/GiHGLBEXQAAALEX.jpg

## 溯源

- 核心主张：OpenAI 的 Operator 靠 CUA 模型工作：在每个用户专属的虚拟机浏览器里，循环执行“截屏感知、用思维链推理下一步、用虚拟鼠标键盘执行”，不需要专门的 API 就能操作各种界面，直到判断任务完成；遇到登录、验证码等敏感操作交给用户确认。
- 源知识：
  - [OpenAI 计算机使用智能体（CUA）](../roots/openai-2025-computer-using-agent.md) · 关系：直接源自 · 强弱：强。原文大段是在转述 OpenAI 2025 年 1 月发布的 CUA 介绍：GPT-4o 视觉加强化学习、处理原始像素、虚拟鼠标键盘、感知—推理—动作三步、敏感操作请用户确认，几乎逐句对应。
  - [智能体](../roots/intelligent-agent.md) · 关系：换了说法 · 强弱：弱（待 Luke 确认）。“感知—推理—动作”的迭代循环就是教科书里智能体“感知环境、采取行动实现目标”的定义，只是把环境换成了电脑屏幕。
  - [思维链提示](../roots/wei-2022-chain-of-thought-prompting.md) · 关系：直接源自 · 强弱：强。原文明说 CUA“使用链式思考（chain-of-thought）来推断下一步的行动”，把思维链当成“内在独白”。
  - [ReAct：推理与行动协同](../roots/yao-2022-react.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。先推理下一步、执行动作、再看新截图继续推理，是 ReAct 把推理和行动交替进行、读环境反馈再调整的模式；原文没有引用 ReAct。
  - [机器人流程自动化（RPA）](../roots/robotic-process-automation.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“通过虚拟的鼠标和键盘来执行操作……而无需使用专门的 API”，和 RPA 模仿人在界面上点击输入、绕开 API 的做法一样；区别是 RPA 照着录好的脚本走，CUA 每一步看屏幕自己判断。
  - [人在环中](../roots/human-in-the-loop.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。大多数步骤自动完成，但输入登录信息、回答验证码等敏感操作要请用户确认，是在关键节点保留人的介入。
- 本质：这条新知识本质上是“感知—推理—行动”的智能体反馈循环，在只靠屏幕像素和鼠标键盘去操作通用电脑界面的场景下的应用。
- 整理于：2026-10-18（第 2 轮）
