---
title: "Astra 电脑操作让验收成闭环"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/2096051842174087386
source: X
published: 2026-09-05 01:44 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 编程智能体
roots: [acceptance-testing, cherny-2025-claude-code-best-practices, openai-2025-computer-using-agent, feedback]
---

## 原文

目前用下来 GPT 6 Astra 最让我惊艳的还是 Computer Use 的能力，它不像之前 GPT 5.6 那样 要稍微等一会才进行各种操作，现在它能很快很精准的帮我测试 App，在旁边看着它点击真的是一种享受 https://t.co/Q5b3YLuLXY 

这其实带来一个最大的提升就是让 Agent 从开发到验收形成了完整的闭环。

想象一下现在我们开发，在开发完成后，还是不免有很多操作需要手动去验证下，包括线上系统的测试，也是更多的依赖于代码操作 PlayWright 这样的端到端测试框架去执行，之前 Computer Use 也不是不能做到，而是相对成本较高、准确率较低、速度也不够快。

但 GPT 6 可能突破了个 Computer Use 的临界点：准确率高速度快，成本方面现在还不算低，但可以遇见未来会进一步下降。

建议你可以试试在给 GPT 6 安排任务的时候，让它自己去用 Computer Use 测试验收一下，可以大幅减少你手动验收的工作。

另外就是以前一些 App 的自动化测试，也可以试试用 GPT-6 去调用 Computer Use 去做，覆盖一些以前端到端测试框架无法覆盖或者成本过高的场景。

> 媒体：
> - https://video.twimg.com/amplify_video/2095972627244253192/vid/avc1/480x270/Tvflr0jjiudAksnB.mp4?tag=29

## 溯源

- 核心主张：电脑操作能力跨过“又准又快”的门槛后，agent 可以自己点界面测试验收，开发到验收形成闭环，既减少人工验收，也能覆盖端到端测试框架做不到或太贵的场景。
- 源知识：
  - [验收测试](../roots/acceptance-testing.md) · 关系：直接源自 · 强弱：强。作者讲的就是验收：开发完后按需求逐项检查，并点名 Playwright 这类端到端测试框架做对比。
  - [Claude Code 最佳实践（给 Claude 一个验证自己工作的办法）](../roots/cherny-2025-claude-code-best-practices.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。Claude Code 最佳实践的核心是给 agent 一个能自己跑的检查（测试、截图对比），做完、检查、再改；本条把这个检查换成了 agent 自己操作电脑验收。
  - [OpenAI 计算机使用智能体（CUA）](../roots/openai-2025-computer-using-agent.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。OpenAI 的 CUA 只看屏幕像素、用虚拟鼠标键盘操作，本条说的电脑操作是同一类能力；GPT 6 Astra 与 CUA 的具体关系未核实。
  - [反馈](../roots/feedback.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“形成完整的闭环”就是反馈回路：让 agent 看到自己产出的实际效果，再据此纠正。
- 本质：这条新知识本质上是反馈闭环（让执行者自己检查结果再修正）在编码 agent 验收环节的应用：电脑操作够准够快之后，验收这一步也能交给 agent。
- 整理于：2026-10-18（第 2 轮）
