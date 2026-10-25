---
title: 拆 11 个编程 agent 的源码看外壳怎么搭：7 个子系统、29 种常见设计；没有一家用通用 agent 框架、没有一家用向量检索读代码，skill 的普及已略超 MCP（9/11 对 8/11），外壳正从工具变成平台
author: Paul Barbaste 等 4 人（Wavestone AI Lab、Inclusive Brains）
url: https://arxiv.org/abs/2609.00006
source: 论文
published: 2026-07（arXiv 预印本 2609.00006 [cs.SE]，v1 2026-07-15；DOI 10.48550/arXiv.2609.00006）
saved: 2026-10-25
why: 探索日报：Luke 想看
related_principles: [原则 2, 原则 11, 原则 3]
status: 已整理
kind: 观点
topic: 编程智能体
roots: [harness-engineering, anthropic-2024-building-effective-agents, yao-2022-react, dominant-design, galls-law]
---

## 原文

全文 83 页（正文第 1～74 页，附录和参考文献第 75～83 页，7 张图、18 张表），版权归作者（arXiv 页面标的是 CC BY 4.0 许可）。这个仓库是公开的，按「有版权的长文」只存要点，原文看上面的链接。读的是 v1（2026-07-15）：第 1～6 节、第 12.5 节、第 13～17 节和 13 条观察结论都读了；第 7～12 节逐系统的细节（提示词、工具、记忆、安全、多 agent）只读了每节的结论段和表格，附录 A 的大表和参考文献只扫过。

- 标题：Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents -- A Source-Code Study of Eleven Systems
- 出处：arXiv 预印本 2609.00006（软件工程 cs.SE；多智能体系统 cs.MA），2026-07-15。作者说明这是 2026 年 4 月版研究的第二版、大幅扩充：系统从 8 个增到 11 个，另加一个"元外壳"作对照
- 作者：Paul Barbaste（一作、通讯作者；Inclusive Brains、Wavestone AI Lab）、Tristan Darrigol、Germain Vu、Tom Wiltberger（Wavestone AI Lab）
- DOI：[10.48550/arXiv.2609.00006](https://doi.org/10.48550/arXiv.2609.00006)
- 免费全文：[arXiv PDF](https://arxiv.org/pdf/2609.00006)
- 被引：0 次（OpenAlex，2026-10-25 查）

### 内容要点（模型概括，不是原文）

**要解决的问题**

"agent = 模型 + 外壳"，外壳（harness）是模型以外的一切：循环、工具、上下文管理、安全控制、多 agent 调度、扩展接口。"外壳工程"这个词 2026 年 2 月才流行起来（作者记为 Mitchell Hashimoto 先随口用、LangChain 的 Trivedy 下定义），但还没有一份基于真实源码的参考：外壳到底由什么组成、几家主流实现差在哪（第 1、2.1 节）。已有的综述要么只报跑分不碰架构，要么只讲概念没有实现；最接近的 Rombaut 源码分类只看开源系统，没包含 Claude Code（第 1、3.3 节）。本文不跑分、不排名，只描述和比较这些系统是怎么搭的（摘要）。

**研究对象和方法**（第 4 节，表 3）

- 11 个系统，版本都固定在 2026 年 7 月：四家模型厂商的旗舰（Claude Code、Codex CLI、Gemini CLI、Mistral Vibe），七个开源（OpenHands、Aider、Mini-SWE-Agent、Hermes、Pi、OpenCode、OpenClaw）；另把 Databricks 的 Omnigent（统一调度多家外壳的"元外壳"）当对照
- Claude Code 用的是 2026 年 3 月流出的源码快照，不是官方发布的源码（第 1 节、第 15.6 节）
- 4 月版里的 8 个系统保留了旧快照，和 7 月版逐行比较，等于一份"同一批系统隔 90 天"的纵向样本（第 14.5 节）
- 按 7 个维度读源码：循环、模型接入、工具、记忆和上下文、安全和权限、多 agent、扩展（第 4.2 节）

**核心框架：外壳的 7 个子系统**（第 2.3 节，表 1）

| 子系统 | 管什么 | 最简的样子 | 最复杂的样子 |
|---|---|---|---|
| agent 循环 | 推理和执行交替，决定何时停 | Mini-SWE-Agent：一个 while 循环加一个 bash 工具 | OpenHands：事件溯源的对话树，并行执行一批动作 |
| 模型接入 | 讲各家协议、拼提示词、缓存、思考、路由 | 一次 LiteLLM 调用加一个模板 | Hermes 自己写 5 种传输、29 个厂商配置；Codex 由服务端下发模型目录 |
| 工具 | 定义并执行 agent 能做的事，首先是改文件 | 只有 bash | Claude Code 43 个带类型的工具、按需加载；Codex 把工具调用当成 V8 执行的代码 |
| 记忆和上下文 | 分配上下文窗口，跨轮、跨会话记东西 | 历史无限往后堆 | Codex 由 agent 自己维护跨会话记忆；Gemini CLI 按图结构提炼上下文 |
| 安全和权限 | 决定什么能跑、什么要问、什么禁止，隔离执行 | 只限花费和步数 | Codex：策略规则 + 模型审批 + 三种操作系统的沙箱 |
| 多 agent 调度 | 派生、协调子 agent，连接别的 agent | Aider：没有（故意单 agent） | Claude Code 递归派生；Omnigent 跨厂商协调 |
| 扩展 | 配置、钩子、skill、插件、MCP | Python 接口约定 | Pi"一切都是扩展"；Codex 插件市场 |

**13 条观察结论里最重要的几条**

| 结论 | 内容 | 出处 |
|---|---|---|
| 循环复杂不等于跑分高 | 代码量差三个数量级，干的是同类任务；Mini-SWE-Agent 约 100 行的循环，自报 SWE-bench Verified 74% 以上，和大系统在同一档。大系统多出来的代码花在安全、体验、扩展、客户端上，OpenCode 约五分之三的非测试代码是各种客户端 | 观察 1，第 2.4 节 |
| 两个"都没有" | 约 400 万行 Python、TypeScript、Rust 里，没有一个 agent 运行时导入 LangChain、LangGraph、AutoGen、CrewAI 等通用 agent 框架（Gemini CLI 连 Google 自家的 Genkit、ADK 都不用）；没有一个用向量检索读代码，都靠 ripgrep、tree-sitter、glob 和自动发现的 Markdown 上下文文件。向量只出现在聊天记忆里（OpenClaw 默认开），Hermes 的历史搜索用 SQLite 全文检索 | 观察 9，第 13.2 节，表 13 |
| skill 略超 MCP | 11 个里 9 个支持 SKILL.md 形式的 skill，8 个支持 MCP；4 月时打平，是 Pi"要 skill、不要 MCP"打破了平局。9 个里 8 个只先加载 skill 的名字和简介、用到再读正文；4 个系统有 skill 仓库，出现了信任分级、隔离、来源校验，还有 agent 自己写的 skill（Hermes 做完任务后自动建、改 skill） | 观察 8，第 12.5 节，表 10 |
| 持久记忆成了新前沿 | 压缩上下文的做法已趋同（11 个里 7 个到阈值就让模型总结）；拉开差距的是"记忆怎么写进去"：agent 自己维护、人审后写入、模型直接写但限字数、每次回复前先让子 agent 回忆 | 观察 5 |
| 主从分工各自长出来 | 四家厂商旗舰和多数开源系统都独立长出"主 agent 派子 agent"的结构；但多用于并行查资料，不是并行写代码，和 Anthropic"编程任务能并行的部分比研究少"的提醒一致；Pi 故意只做单 agent | 观察 7，第 15.1 节 |
| 和厂商绑定，绑的是更新回路 | 多家开源系统证明，缓存、思考档位、按模型定制提示词这些优化，不绑定某家模型也做得到，代价是自己维护每家的适配；只有厂商能在新模型发布当天从服务端重调外壳行为（Codex 的模型目录） | 观察 2，第 15.4 节 |
| 沙箱是选择，不是规模的结果 | 4 月版以为越大的系统越会做操作系统级沙箱，7 月版被推翻：Hermes、OpenCode 都很大，却没有系统级隔离，把安全预算花在防提示注入和细粒度命令权限上；Pi 明说半吊子沙箱"容易被误当成安全边界" | 观察 6，第 15.3 节 |
| 提示词里的规矩在变少 | 不要画蛇添足、不要自己提交代码这类规矩，4 月时几乎各家都有；到 7 月，Codex 新一代模型的提示词删掉了这两条，Mistral Vibe 反过来要求提交；规矩从提示词（模型读）搬到配置（平台强制） | 观察 3，第 14.5 节 |
| 外壳变成了平台 | 外壳变成可导入的 SDK（Claude Agent SDK、openai-codex 等），框架厂商反过来做外壳（LangChain 的 Deep Agents）；出现插件市场、互相导入对方会话记录的工具（Codex 能导入 Claude Code 的会话和设置）、企业设备管理级的管控；agent 本身能当成一个兼容 OpenAI 接口的"模型"被调用；Omnigent 在上面统一调度 23 种外壳 | 观察 12，第 14 节 |

**90 天里变了什么**（第 14.5 节）

- 趋同变成照抄：Codex 原样采用 Claude Code 的钩子事件名，OpenHands 读 Claude Code 的插件格式，OpenCode 读 Claude Code 的 skill 目录，Hermes 的代码注释写明借鉴了谁
- 好做法往下扩散：按需加载工具从 1 家到 3 家，只读的计划模式扩到四家厂商旗舰。作者说一个独家功能的"半衰期"现在以周计
- 代码量暴涨：Codex 一个季度从约 62 万行到约 112 万行 Rust
- 4 月版的 3 条结论被改写；作者的方法教训是：清单类说法（工具数、版本、功能格）几周就过时，结构类说法（子系统划分、两个"都没有"）到目前还站得住

**给做外壳的人的 18 条建议**（第 16 节，挑要紧的）

| 编号 | 建议 |
|---|---|
| 1 | 先用一个线性 while 循环；出现 3 个以上互不相干的回合级规则（回合上限、花费上限、自动压缩等）再改成中间件管道 |
| 3 | 先只给一个 bash 工具，看到具体失败再加工具 |
| 4 | 工具超过约 15 个再做按需加载 |
| 5 | 改文件：前沿模型用"精确匹配唯一片段再替换"，较弱模型用模糊匹配；都不要按行号改 |
| 6 | 按目录层级自动读 Markdown 上下文文件，也读别家的文件名（AGENTS.md、CLAUDE.md 等） |
| 8、16 | 不要给代码做向量检索；真觉得需要，先在留出的任务集上证明它比 ripgrep 加 tree-sitter 好 |
| 11 | 安全规则写成数据或策略文件，不写死在代码里；有"全放行"模式也要留一条底线 |
| 12 | 在说得出一个明确的、并行查找确实更好的环节之前，保持单 agent |
| 14 | 做事的方法和领域知识用 skill，接外部系统用 MCP，优先 skill |
| 15 | 不要用通用 agent 框架搭运行时；要现成底座就用各家的外壳 SDK |

最后给了一个约 90 行的 Python 最小外壳，实现了其中 10 条（第 16.10 节）。

**需要说清楚的边界**

- 全文只读源码，不跑程序、不测速度、不做对照实验；文中的跑分都是各系统自己报的，模型、时间、配置都不同，作者明说不能拿来比高低（第 15.6 节，表 4 脚注）
- Claude Code 的分析基于 2026 年 3 月流出的源码快照，作者承认这是可复现性最弱的一环，7 月的正式版可能已经不同（第 15.6 节）
- "没人用框架"只查了依赖清单和代码里的导入语句，没追动态加载、内部分支、编译后的发布包（第 15.6 节）
- skill 超过 MCP 只差 1 个系统（9 对 8），而且正是作者说的 Pi 一家打破平局；如果把不是编程 agent 的 OpenClaw 去掉，作者建议用 10 个系统的口径（第 4.1 节，观察 8）
- "没人用向量检索"只针对读代码；聊天记忆里有用的（OpenClaw 默认开）
- 和 Anthropic 那 4 篇工程文章高度吻合，作者说这不能证明是受了文章影响，要去访谈各家工程师才能分清（观察 10，第 15.6 节）
- "外壳复杂度和成功率是一条先陡后平的曲线"只是作者的直觉，明说没有测（第 15.5 节）
- 论文本身大量借助 Claude Code 做源码分析和起草，作者说结论都对过源码（致谢一节）
- 第 3.7 节的行业事件（收购、改名、停服等）来自厂商公告和仓库信息，作者注明这些没有核对源码

**作者明说引用的前人工作**（供整理时溯源参考）

- Anthropic 工程文章 4 篇：Building Effective Agents（Schluntz & Zhang 2024，主张少用框架、先用原始 SDK）、Effective Context Engineering for AI Agents（Rajasekaran 等 2025，主张即用即取的检索）、Writing Effective Tools for AI Agents（2025，工具少而精）、How We Built Our Multi-Agent Research System（Hadfield 等 2025，多 agent 约多花 15 倍 token）（第 3.6、15.1 节）
- ReAct（Yao 等 2023）：几乎所有循环的底子（第 6.1 节）
- SWE-bench、SWE-agent 的"agent 与计算机的接口"（ACI）、CodeAct（第 3.1 节）
- 自我修正一脉：Reflexion、Self-Refine、CRITIC、Self-Debug（第 6.3 节）
- Agentic Harness Engineering（Lin 等 2026）：自动进化外壳，从只有 bash 起步到 SWE-bench Verified 71.9%，拆解发现工具、中间件、长期记忆贡献提升，只改系统提示词反而变差（第 3.1、15.5 节）
- 路由和级联：FrugalGPT、RouteLLM、Hybrid LLM（第 15.4 节）
- 代码检索研究：RepoCoder、RepoBench、CodeRAG-Bench（检索对代码生成的帮助因任务差别很大）（第 13.2 节）
- Rombaut《Inside the Scaffold》：13 个开源脚手架的源码分类（第 3.3 节）
- Macedo：外壳的第一个操作性定义（第 2.1 节）
- "循环工程"：Steinberger、Osmani 2026 年 6 月的说法，"设计会给 agent 出提示的循环"（第 6.1 节）

## 溯源

- 核心主张：拆 11 个编程 agent 的源码发现：外壳都由同样 7 个子系统构成，循环复杂度不决定跑分，没有一家用通用 agent 框架或向量检索读代码，各家做法在 90 天里从趋同走到互相照抄，外壳正从工具变成平台。
- 源知识：
  - [外壳工程（agent = 模型 + 外壳）](../roots/harness-engineering.md) · 关系：直接源自 · 强弱：强。论文标题和第 2.1 节直接沿用“外壳工程”这一说法和“agent = 模型 + 外壳”的定义（Hashimoto 先用、Trivedy 下定义）。
  - [构建高效的智能体](../roots/anthropic-2024-building-effective-agents.md) · 关系：直接源自 · 强弱：强。论文引用它（文献 [16]），“不用通用框架”“从简单起步”两条结论与建议 1、15 和观察 13 都明说对上这篇的主张。
  - [ReAct：推理与行动协同](../roots/yao-2022-react.md) · 关系：直接源自 · 强弱：强。第 6.1 节明说 11 个系统的循环全是 ReAct 的变体，只是复杂度、并发和状态管理不同。
  - [主导设计](../roots/dominant-design.md) · 关系：相近 · 强弱：弱（模型复核通过）。7 个子系统成为“标准解剖”、钩子事件名和 skill 目录被互相照抄、独家功能半衰期以周计，是新品类收敛到主导设计的过程；论文没有用这个理论。
  - [加尔定律](../roots/galls-law.md) · 关系：相近 · 强弱：弱（模型复核通过）。约 100 行的 Mini-SWE-Agent 跑分和大系统同档，建议 1、3 让人先用一个 while 循环、一个 bash 工具，看到具体失败再加，就是复杂系统要从能用的简单系统长出来。
- 本质：这条新知识本质上是外壳工程在编程 agent 上的源码实证：各家独立演化出同一套结构（趋同到主导设计），复杂度并不换来跑分，所以应从简单起步、按观察到的失败加功能。
- 整理于：2026-10-25（第 8 轮）
