---
title: "Harness²：agent 不改模型，靠对照试验改自己的运行框架，还学会怎么改得更好"
author: "Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu, Bhavana Dalvi Mishra, Yifei Ming, Han Yu, Rujun Han, Chen-Yu Lee, Tomas Pfister（Google Cloud AI Research、Northwestern University）"
url: https://arxiv.org/abs/2610.14224
source: 论文
published: "2026-10（arXiv 预印本 2610.14224v1，2026-10-09 提交，未经同行评审）"
saved: 2026-10-19
why: 未说明
related_principles: [原则 1, 原则 11]
status: 未整理
kind: 观点
topic: Agent 与 Skill
roots: []
---

## 原文

全文含附录，许可是 CC BY 4.0。按规则论文只存出处和要点，原文看上面的链接。

- 标题：Harness²: Recursive Agent Harnessing for an Open World
- 发表：arXiv 预印本，2026-10-09 提交 v1，还没有标出期刊或会议
- DOI：[10.48550/arXiv.2610.14224](https://doi.org/10.48550/arXiv.2610.14224)
- 全文网页版：[arxiv.org/html/2610.14224v1](https://arxiv.org/html/2610.14224v1)
- 代码：[github.com/google-research/harness2](https://github.com/google-research/harness2)
- 被引：刚发布十天，暂无

### 内容要点（模型概括，不是原文）

读了正文和附录 B、E、F、G，附录 H 的提示词原文没有细读。

**要解决的问题**

agent 的本事不只看模型，也看"运行框架"（harness）：提示词、记忆、skill、工具说明、脚本、子 agent 这些包在模型外面的东西。让 agent 自己改进运行框架（递归自我改进，RSI），在开放世界里有两个难点（第 1 节）：

| 难点 | 大白话 |
|---|---|
| 没有标准答案 | 新任务来了，没有现成的检查来判断改动对不对 |
| 改进不能迁移 | 为一个任务改好的框架，换个任务往往不管用；直接继承还会越改越乱 |

作者的核心问题："递归自我改进能不能既改进当前的框架，也改进以后改框架的方法？"（第 1 节）

**核心想法：两层递归**

| 层 | 做什么 |
|---|---|
| 任务层 | 给当前任务改运行框架，用"提议、试跑、合成"三步，不需要标准答案 |
| 改进方法层 | 每个任务做完后，把"哪种改动在什么情况下有用、证据是什么"记进一个库（每条带一个 EXPERIENCE.md），下一个任务改框架时参考它。下一个任务不直接继承上一个的框架，而是从同一个起点出发，只借经验 |

**主要方法**（第 2 节）

- 运行框架拆成 8 个文件：系统提示词、护栏、记忆、skill、工具说明、脚本、子 agent、中间件插件（第 2.1 节）
- **提议**：先照原样跑一遍做参照，再提两个候选改动：一个针对通用的毛病（规划、工具使用、上下文管理、分派），一个针对这个领域的知识和流程（第 2.2.1 节）
- **试跑**：两个候选在同样条件下各跑一遍，和参照对比行为。作者明说这只是"行为对照"，不是验证答案对不对（第 2.2.1 节）
- **合成**：读参照、两个候选和它们的差异，挑有证据支持的改动合在一起，也可以一个都不要。每个决定都要对应一处具体观察（第 2.2.1 节）
- 预算 k 可以加大：并行（同时试多个候选再合成）或串行（一轮接一轮改）（第 2.2.2 节）
- 改框架的"编辑者"默认是 Claude Opus 4.8；执行任务的模型是 Gemini 3.5 Flash 和 GLM-5，模型权重全程不变（第 3.1 节）

**主要结果**

| 结果 | 数字 | 出处 |
|---|---|---|
| 改一步（k=1）的最大提升 | WorkBuddy-Bench +11.5 分，JobBench +4.5 分，Harvey 法律基准 LAB 部分通过率 +11.8 个百分点 | 第 1 节、第 3.2 节 |
| GLM-5 在 WorkBuddy-Bench（OpenCode） | 64.2 → 75.7，超过了没改框架的 Gemini 3.5 Flash（72.4） | 表 1 |
| 并行递归 k=5 再加 | WorkBuddy-Bench +2.9～3.9，JobBench +3.0～4.2，LAB +2.6～6.7 个百分点 | 第 3.2 节 |
| 消融：去掉经验库 / 去掉两类候选的分工 / 去掉合成 | WorkBuddy-Bench 分别 −3.1 / −2.9 / −1.6；JobBench −1.8 / −3.7 / −1.9 | 表 3 |
| 没有参照和对照、直接让模型改框架 | Code 73.4 → 63.2，Web 69.9 → 65.0，反而变差 | 第 4 节、图 7 |
| 经验库跨基准迁移（JobBench 的库用到 WorkBuddy-Bench） | +0.6、+0.5、+2.9 | 第 4 节、图 7 |
| 执行者和编辑者用同一个模型 | 5 个模型都在 3 个基准上提升；GLM-5 在 LAB +13.7 | 第 4 节、图 8 |
| 为 Gemini 改好的框架直接给别的模型用 | GLM-5 在 Code 上 58.5 → 75.8；Opus 4.8 只 +2.6、+1.1 | 附录 E.3 |
| 工具调用出错率（Gemini、k=1） | JobBench 14.4% → 9.1% | 附录 E.4，表 7 |
| 对照组：把过去的经验总结检索回提示词（ReasoningBank） | 在编程任务上最多比原框架低 6.6 分 | 第 3.2 节 |

**需要说清楚的边界**

- 没有标准答案时，改动靠"行为对照加模型判断"，这些信号受运行随机性和模型共同偏见影响，不保证对，也不保证能迁移到别的任务（附录 F）
- 多跑多试要额外花算力；作者只在有限预算范围内测了这个取舍（附录 F）
- 失败案例：最后挑选时选了更差的候选（一个 55 分的结果被选中，放弃了 95 分的）；一个错误前提会传给所有候选（附录 E.6）
- 测试集不大：WorkBuddy-Bench 三个领域的测试半边分别是 40、35、25 个任务，JobBench 34 个（附录 B）；主表是 3 次运行的平均
- 评分里有大模型当裁判的部分（Gemini 3.5 Flash、Claude Opus 4.8）（附录 B）
- 预印本，还没经过同行评审

**作者明说引用的前人工作**（供整理时溯源参考）

递归自我改进：Self-Rewarding LM（Yuan 等，2024）、STOP（Zelikman 等，2024）、达尔文哥德尔机（Zhang 等，2026）。自我反馈：Self-Refine（Madaan 等，2023）、Reflexion（Shinn 等，2023）。并行聚合：RSA（Venkatraman 等，2025）。运行框架优化：Meta-Harness（Lee 等，2026）、AHE（Lin 等，2026）的 8 文件拆分、Harness Scaling（Wang 等，2026）、ReasoningBank（Ouyang 等，2026）。提示词和流程优化：DSPy（Khattab 等，2024）、GEPA（Agrawal 等，2026）。

## 溯源

（整理时填写，存的时候留空）
