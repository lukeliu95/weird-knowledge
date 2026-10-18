---
title: "claude-api 优化 skill"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/2095329314778607932
source: X
published: 2026-09-03 01:53 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 编程智能体
roots: []
---

## 原文

Anthropic 刚开源了一个 /claude-api 的 skill，内置到了 Claude Code。

这个 Skill 的使用场景是帮你优化 Claude API 调用的，针对 Agent 开发或者基于 Claude API 开发，如果你只是 Claude Code 用户，那么不需要管，或者你不是用的 Claude 模型，那效果估计要差一点，但也会有效果。

使用方法很简单，在 Claude Code 里输入 /claude-api 加子命令，就能触发对应的诊断或迁移流程。

它的代码在 GitHub 上公开：https://t.co/C8BfqwkWrA

这个 skill 本身不是一个独立工具，而是一组结构化的参考文档和工作流指令。当 Claude Code 检测到你的项目里 import 了 Anthropic SDK，或者你主动输入 /claude-api，它就会把对应语言（Python、TypeScript、Java、Go、Ruby、C#、PHP 或 cURL）的 API 文档加载到上下文里，让 Claude 在帮你写代码时有准确的 API 知识可用。

支持 8 种语言，覆盖两个开发面：Messages API（常规的请求、流式输出、工具调用、批量处理、提示词缓存等）和 Managed Agents（Anthropic 托管的有状态 Agent，带沙箱环境）。

三个主要的子命令

/claude-api cost-optimize

分析你项目的实际 API 使用情况，按优先级排列省钱建议。它不是给你一份通用清单，而是看你具体的用量模式，逐项提出修改方案，你可以逐条批准或跳过。检查的项目包括缓存配置、Token 冗余、批量处理机会、effort 级别和模型选择。

/claude-api prompt-audit

扫描项目里的提示词和 skill 文件，找出针对当前模型来说已经过时或有问题的写法。比如过度验证（让模型反复确认自己的输出）、多余的强调语句、过时的 few-shot 示例、自相矛盾的规则。产出两样东西：一份审计报告（标出具体文件、行号和问题模式），以及一个修改建议的 diff。

/claude-api migrate

帮你把现有的 Claude API 代码迁移到更新的模型。它会先确认范围（哪些文件需要改），再逐个文件分类，然后按目标模型的 breaking changes 列表逐项处理。比如从 Fable 5 迁移到 Fable 5.1，或从 Opus 4.6 升级到 4.8，涉及的参数变化、废弃字段、新的默认行为，都会在这个流程里覆盖到。

这些命令在 Fable 5.1 发布的背景下尤其有用。Fable 5.1 的提示词缓存价格降了 75%，但你得先确认自己的缓存配置没有问题才能真正省到钱。cost-optimize 就是干这个的。同样，Fable 5.1 在低 effort 下就能达到上一代高 effort 的水平，但如果你的提示词里还塞着大量为旧模型写的验证指令和脚手架，实际效果就打折扣。prompt-audit 帮你清理这些。

除了这三个，还有一个 /claude-api managed-agents-onboard，用于从零搭建一个 Managed Agent，走一个交互式的引导流程。

如果你需要做 Claude 模型 API 的优化，值得试试。

---

附加（翻译自原推）：常见提示词“反模式” (anti-patterns)：

1. 流于形式的“验证仪式” (Verification rituals)。 

诸如“仔细检查你的工作”或“在回答前核对两次”这类指令，往往会被前沿模型从字面上死板理解。这不仅没必要，还会白白浪费你的 tokens。

2. 用力过猛的强调与“详尽感” (Thoroughness and emphasis boosters)。 

“尽可能详尽”、“关键注意：你必须永远……”这类强调语，在指导前沿模型时，反而会导致模型变得异常啰嗦，甚至去执行大量不必要的工具调用。

3. 强制性的流程与“草稿本”脚手架 (Mandatory procedures and scratchpad scaffolds)。 

强制性的固定步骤（比如“在草稿本 (scratchpad) 中一步步思考”）或者思维模板，对于前沿模型来说完全是多此一举。这些人为强加的“脚手架”会与模型原生的推理能力重叠，从而白白消耗掉不必要的词元。

4. 过时的示例 (Stale examples)。 

有些少样本示例 (few-shot examples)（注释：在提示词中提供少量示范例子，以便让模型模仿学习的一种常见技巧） 往往是针对老一代模型常犯的错误来设计的。如果拿这些去教前沿模型，反而会让它在原本很简单、根本不需要复杂思考的任务上，刻意模仿出冗长的推理链条。

5. 自相矛盾的规则 (Contradictory rules)。 

前沿模型在遵循指令方面非常听话。如果你给出的指令本身存在矛盾（例如同时规定“始终在政策范围内退款”和“未经上报绝不退款”），模型会非常实在地去执行这些冲突的规则，最终导致整体表现大打折扣。

6. 过时的配置 (Dated configuration)。 为老一代 Claude 编写的设置（例如手动设置思考预算 (thinking budgets)），在配合新一代模型使用时，可能会直接被 Claude 平台拒绝访问。

随着时间的推移，这些反模式会在你的提示词中不断累积。当你将大语言模型升级到最新版本时，它们就会在暗中悄悄拖累整体性能。这背后的一个常见原因是：前沿模型太擅长遵循指令了，以至于这些糟糕的规则反而会误导它们，让它们把精力花在毫无意义的地方，花费不必要的 Token。

举个真实案例：在一个内部的客户服务基准测试 (benchmark) 中，测试了从 Opus 4.8 升级到 Opus 5 的情况。结果发现，在使用 Opus 5（以及像 Fable 5.1 这样的其他前沿模型）时，那些所谓的“验证仪式”（比如“核对两次”）会让模型重复劳动，浪费大量的 Token。而那些“强调增强语”（比如“尽可能详尽”）则会触发几十次完全没必要的系统搜索。

执行提示词审计 (prompt audits) 可以显著提升大语言模型的性能并降低成本。

## 溯源

