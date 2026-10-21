---
title: "Claude Code 的 Task 工具原理"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/1935794151293083803
source: X
published: 2025-06-19 20:17 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 编程智能体
roots: [divide-and-conquer-algorithm, anthropic-2025-multi-agent-research-system, martin-2025-context-engineering-agents, yao-2022-react, yan-2025-dont-build-multi-agents]
---

## 原文

我看到有人在让“Claude Code”自己开新进程 `claude -p `实现多任务，其实没必要，有更简单的办法。这个简单办法就是让它自己开子 Agent。Claude Code 现在有 18 个工具，最特殊的一个工具叫 Task，它本质就是一个 Claude Code 的克隆工具，只不过是作为 Claude Code 的一个工具。

如果你懂递归的话就很好理解。如果你不懂递归，可以这么理解：Claude Code 是个 AI 程序员，它可以用一堆工具，其中最神奇的一个工具叫 Task，就是克隆一个自己的分身去干活！

这样做有什么好处呢？就是可以并行多任务，还可以控制上下文，让子任务更专注。

举例来说，你粘贴一段错误代码让 Claude Code 去 Debug，并且还让它写测试代码覆盖这个错误。Claude Code 会先调用 TodoWrite 这个工具写一个 TODO List。把任务分成 3 步：

- [ ] 根据错误信息收集相关代码
- [ ] 根据错误信息和相关代码解决 Bug
- [ ] 写新的测试覆盖

这一步完了后它会起一个 Task，这个 Task 就是专门根据错误信息去找到相关代码的位置，那么这个子任务只需要接受错误信息找上下文，它不管怎么解决 Bug，也不管怎么写测试覆盖。

主任务就会等这个子任务完成，子任务完成后，主任务就调用 TODO Write 更新 TODO List。

- [x] 根据错误信息收集相关代码
- [ ] 根据错误信息和相关代码解决 Bug
- [ ] 写新的测试覆盖

然后调用 TodoRead 工具看下一步要干嘛，现在有充足上下文了，它可以再起一个子任务去根据错误信息和代码修复 Bug，等修复 Bug 的子任务完成了，再回到主任务，继续更新 TODO List，继续读取下一个 Item

最后再启动一个子任务去写测试，测试子任务也完成了，返回结果到主任务，这时候调用 TodoRead 一看任务都处理完了，最后根据前面的任务情况给你一个总结摘要，表示任务都完成了。

Claude Code 真的没有做什么工程上的优化，什么上下文压缩、临时存储，都没有的！就是简单粗暴：
1. 把用户问题、系统提示词、能用到的工具一股脑发给 Claude，问下一步该干嘛
2. Claude 就返回说现在你要到 TodoWriter 工具
3. Claude Code 就去调用 TodoWriter 工具，本质上也是一个 AI 请求，最后返回生成的 Todo List
4. 然后 Claude Code 把工具返回结果和前面的所有消息继续发给 Claude，Claude 返回说你现在要去起一个新的 Task 去收集代码了
5. 然后 Claude Code 就起一个新的 Task，把错误信息和要求收集相关代码的任务说明、系统提示词、环境说明、能用到的工具一股脑发给 Claude，问下一步该干嘛
  - 在新的 Task 里面，就是不停的问 Claude 该用啥工具，然后发送工具结果和前面所有历史消息
  - 任务完成后，返回任务结果
6. 然后 Claude Code 把子 Task 的结果和前面历史信息一起发给 Claude 问下一步干嘛
7. 就这样循环直到 Claude 认为任务完成了

所以你经常看到 Claude Code 在那几十分钟上下文也没爆掉，因为它会启动子任务，这样上下文就分摊到子任务中了，主任务中只是保留子任务完成后的内容。

> 媒体：
> - https://pbs.twimg.com/media/Gt1LrTkWkAAINrA.jpg
> - https://pbs.twimg.com/media/Gt1OLcTXEAIP9Cp.jpg
> - https://pbs.twimg.com/media/Gt1O7j0WIAAf2kW.jpg
> - https://video.twimg.com/amplify_video/1935790834911215616/vid/avc1/360x270/35X65ZrlyeL3PBfW.mp4?tag=21

## 溯源

- 核心主张：Claude Code 的 Task 工具是把自己克隆成一个工具（递归）：主 agent 按待办清单把每一步交给只带必要上下文的子 agent，主线只保留子任务的结果，所以长时间运行上下文也不爆；整个系统就是“把历史和工具发给模型、执行它选的工具、把结果追加回去”的循环。
- 源知识：
  - [分治法](../roots/divide-and-conquer-algorithm.md) · 关系：相近 · 强弱：强。作者明说“懂递归就很好理解”：大任务拆成同类子任务交给自己的分身去做，结果再汇总回主任务。
  - [Anthropic 多智能体研究系统](../roots/anthropic-2025-multi-agent-research-system.md) · 关系：相近 · 强弱：弱（模型复核通过）。Anthropic 一周前（2025-06-13）发布的编排-工人架构：主 agent 规划，子 agent 各带独立上下文干活，与本条描述的主任务/子任务结构一致。
  - [智能体的上下文工程（写入、选取、压缩、隔离）](../roots/martin-2025-context-engineering-agents.md) · 关系：相近 · 强弱：弱（模型复核通过）。上下文管理四类做法里的“隔离”：把上下文拆给子 agent，主线只接收结果，就是本条说的“上下文分摊到子任务”。
  - [ReAct：推理与行动协同](../roots/yao-2022-react.md) · 关系：相近 · 强弱：弱（模型复核通过）。第 1～7 步“问模型下一步用什么工具、执行、把结果连同历史再发回去”就是 ReAct 式的推理-行动循环。
  - [别做多智能体](../roots/yan-2025-dont-build-multi-agents.md) · 关系：挑战 · 强弱：弱（模型复核通过）。Cognition 同期文章说 Claude Code 的子 agent 从不和主 agent 并行干活、通常只回答问题不写代码，和本条“子任务修 bug、写测试、可以并行多任务”的说法相反。另外本条说 Claude Code“没有上下文压缩”，但官方更新记录在研究预览期的 0.2.47 版就列有“自动压缩对话”，这一句与事实不符。
- 本质：这条新知识本质上是分治（递归拆成同类子问题）加上下文隔离在编码 agent 场景下的应用：子 agent 就是 agent 对自己的递归调用，用来分摊上下文。
- 整理于：2026-10-18（第 2 轮）
