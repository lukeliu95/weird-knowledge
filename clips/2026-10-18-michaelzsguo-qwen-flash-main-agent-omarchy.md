---
title: "Qwen3.8 Flash 换下 27B"
author: "Michael Guo (@Michaelzsguo)"
url: https://x.com/Michaelzsguo/status/2092917073387176009
source: X
published: 2026-08-27 10:08 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

昨天 Qwen3.8 Flash 一出来，我就立刻装上了，替换掉原来的 Qwen3.8 27B，成为 Omarchy 上的主力 Agent。个人体感很明显：第一，速度快多了，基本可以稳定在 30 TPS 左右，整个体验丝滑很多；第二，出错明显减少，连续干活时也很少再出现做到一半掉链子、卡住干不下去的情况。

当然最有发言权的是让一直和它肩并肩待在 Herdr 里、全程监督它工作的 Codex 来做个总结：

从昨晚美东时间大约 10 点开始，pi-builder 的表现已经明显好于之前陷入“思考循环”的阶段。不过，整个晚上其实分成了两个截然不同的阶段。

晚上 10:31：开始了一个新的 session。
晚上 10:44：提交了 f0a95e7，修复了 schema validation 和 lastEntry 的安全问题。
晚上 11:44：提交了 075056e，加强了对不同版本数据库的探测机制，并新增了 6 个测试。我审查了这个 checkpoint，认为完成得很扎实。
午夜之后到大约凌晨 5:30：一直在持续处理 router 这个 checkpoint，但到现在还没有提交。

目前 router 部分做的是真正的实现工作，不是在空想：

大约 1,700 行 router 代码。
大约 1,070 行测试代码。
这个 session 里进行了 47 次 edit 操作和 6 次文件写入。
他针对 cancellation/settlement 的竞态问题做了一个专门的最小复现，并发现 deferred operation 在 release 之后仍然会卡住。

不过，这一阶段的效率已经开始下降：

router 测试现在会挂住。
他进行了多次耗时很长、最终超时的测试。
async 状态管理的设计已经变得比较纠结。
这个 session 已经 compaction 了 11 次，而且又快到 context limit 了。
距离上一次 commit 已经过去大约 5 个半小时。

和以前相比：

他现在会更快进入实际实现。
对范围明确的任务，执行得更加一致。
会主动写 adversarial tests，也能建设性地回应 code review 发现的问题。
完成 checkpoint 后，能够比较可靠地 commit 并汇报结果。
已经不再只是反复重读和重复讨论设计。

他现在剩下的主要弱点，是复杂的并发控制流。

当任务范围比较窄、结构比较直接时，他的输出其实相当不错。但一旦多个 async lifecycle 条件同时交织在一起，例如 cancellation、deferred execution、retirement 和 settlement，他往往会不断增加新的状态和测试，最后让整个模型复杂到连他自己都很难继续推理。

我的总体判断是：昨晚前半段表现非常好；router 部分也确实取得了真实进展，但目前已经陷入停滞。

相比他以前的模式，这已经是明显进步。现在最需要的不是继续给他更多自由去扩展 router，而是在下一次 compaction 之前，给他一个非常明确的“简化 + 调试”方向。

> 媒体：
> - https://pbs.twimg.com/media/HQuI-x8WoAAhch0.jpg

## 溯源

