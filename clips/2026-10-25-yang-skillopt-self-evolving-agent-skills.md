---
title: 把 skill 当参数来训：别的模型读执行记录提改法，每步只许改几处，留出集上变好才收下；6 个测试集、7 个模型、3 种运行环境里 52 格全部第一或并列第一
author: Yifan Yang 等 15 人（微软、上海交通大学、同济大学、复旦大学）
url: https://arxiv.org/abs/2605.23904
source: 论文
published: 2026-05（arXiv 预印本 2605.23904 [cs.AI]，v1 2026-05-22，v2 2026-05-25；DOI 10.48550/arXiv.2605.23904）
saved: 2026-10-25
why: 探索日报：Luke 想看
related_principles: [原则 1, 原则 2]
status: 未整理
kind: 观点
topic: Agent 与 Skill
roots: []
---

## 原文

全文 27 页（正文第 1～17 页，参考文献第 17～20 页，附录第 20～27 页），版权归作者（arXiv 页面标的是 arXiv 非独占发布许可，不是开放许可）。这个仓库是公开的，按「有版权的长文」只存要点，原文看上面的链接。读的是 v2（2026-05-25）。

- 标题：SkillOpt: Executive Strategy for Self-Evolving Agent Skills
- 出处：arXiv 预印本 2605.23904（人工智能 cs.AI），v1 2026-05-22，v2 2026-05-25
- 作者：Yifan Yang、Ziyang Gong、Weiquan Huang、Qihao Yang、Ziwei Zhou、Zisu Huang（前六人并列一作）、Yan Li、Xuemei Gao、Qi Dai、Bei Liu、Kai Qiu、Yuqing Yang、Dongdong Chen、Xue Yang、Chong Luo；通讯作者 Yifan Yang、Xue Yang；微软、上海交通大学、同济大学、复旦大学
- DOI：[10.48550/arXiv.2605.23904](https://doi.org/10.48550/arXiv.2605.23904)
- 免费全文：[arXiv PDF](https://arxiv.org/pdf/2605.23904)
- 代码：[项目页](https://microsoft.github.io/SkillOpt/)（论文写的短链 aka.ms/SkillOpt 跳到这里）、[GitHub microsoft/SkillOpt](https://github.com/microsoft/SkillOpt)
- 被引：2 次（OpenAlex，2026-10-25 查）；Semantic Scholar 当天限流，未查到

### 内容要点（模型概括，不是原文）

**要解决的问题**

现在 agent 的 skill（一份写着做事步骤、领域经验、工具用法、输出要求的文字文件）要么人手写，要么让模型一次生成，要么让 agent 自己随手改。作者认为这几种都不像正经的"训练"：改得没有约束，也不能保证越改越好。闭源大模型改不了权重，开源模型改权重又贵，所以作者主张把 skill 文件当成一个冻结 agent 的"外部参数"，用深度学习训练那套纪律来训它（摘要，第 1 节）。

**核心想法**

把训练神经网络的几样东西一一搬到文字上（第 1 节图 1，第 3 节）：

| 训练神经网络 | SkillOpt 里对应的东西 |
|---|---|
| 参数 | skill 文件 |
| 梯度方向 | 从执行记录里总结出的修改方向 |
| 学习率 | 每一步最多改几处（编辑预算） |
| 验证集 | 留出的选择集，变好了才收下修改 |
| 批量、小批量、学习率衰减 | 每次跑多少题、几条记录一起反思、预算逐步变小 |
| 动量 | 每轮结束后的"慢更新"，把跨轮次稳定的经验写进一块受保护的区域 |

执行任务的模型（被适配的模型）不动；另用一个更强的"优化器模型"读执行记录、提修改。最后交付的只是一个 300～2,000 个 token 的 `best_skill.md`，部署时不多调用任何模型（第 1 节，第 3.7 节）。

**主要方法**（第 3 节，附录 C）

| 步骤 | 做什么 |
|---|---|
| 跑一批 | 用当前 skill 在训练集上跑一批题（默认 40 题），记下消息、工具调用、输出、评分（第 3.2 节） |
| 分组反思 | 失败的和成功的分开，每 8 条一组交给优化器模型：失败组提"缺什么规则、哪条要改"，成功组提"哪些做法值得保留"。单条记录容易得出个案式的修法，一组一起看才看得出反复出现的毛病（第 3.3 节） |
| 合并 | 先各自合并失败组和成功组的修改，再合并，冲突时失败组优先；去掉重复、矛盾、只针对个例的修改（第 3.3 节，附录 C.2.3～C.2.5） |
| 限量修改 | 把修改按预期作用排序，只取前 L 条（默认 4 条，余弦衰减到最少 2 条）。修改只有四种：追加、插在某处后面、替换、删除（第 3.4 节，附录 C.3） |
| 验证门槛 | 改出来的新 skill 在选择集上的分数必须严格高于当前分数才收下，持平也拒（第 3.5 节，第 4 节默认设置） |
| 记下失败的修改 | 被拒的修改连同它让分数掉了多少，存进本轮的"失败修改记录"，之后的反思能看到，避免重复犯错（第 3.5 节） |
| 每轮慢更新 | 每轮结束时，同 20 道训练题分别用上轮和本轮的 skill 跑一遍，分成"变好、变差、一直失败、一直成功"四类，由优化器写一段长期指导放进受保护区域（步骤级修改不能碰这块），这一步同样要过验证门槛（第 3.6 节） |
| 优化器自己的经验 | 另写一份"优化器经验"：哪类修改管用、哪类被拒。只给优化器看，不随 skill 交付（第 3.6 节） |
| 换运行环境 | 用一个轻量适配层，同一套流程可在直接对话、Codex、Claude Code 三种环境里跑；Codex 和 Claude Code 里 skill 放成每题一份 SKILL.md，并把执行过程摘要交给优化器看（第 3.7 节，第 4 节"Harnesses"） |

**主要结果**

| 结果 | 数字 | 出处 |
|---|---|---|
| 全面领先 | 7 个模型 × 6 个测试集（直接对话）加 GPT-5.5 在 Codex 和 Claude Code 各 5 个测试集，共 52 格，全部第一或并列第一（并列的一格：GPT-5.4-mini 在 LiveMath 上和 Trace2Skill 同为 32.8） | 第 4.1 节，表 1 |
| 对比的方法 | 不用 skill、人写 skill、模型一次生成的 skill、Trace2Skill、TextGrad、GEPA（只在直接对话比）、EvoSkill（只在 Codex 和 Claude Code 比） | 第 4 节"Baselines"，表 1 |
| GPT-5.5 直接对话 | 6 个测试集平均从 58.8 升到 82.3（+23.5）；比"每格取最好的对手"拼出来的平均 76.9 还高 5.4。表格题 SpreadsheetBench 41.8→80.7，文档问答 OfficeQA 33.1→72.1，数学 LiveMath 37.6→66.9 | 第 4.1 节，表 1 |
| 在 agent 环境里 | GPT-5.5 在 Codex 里平均 +24.8，比 EvoSkill 多 14.0；在 Claude Code 里平均 +19.1，比 EvoSkill 多 3.2 | 第 4.1 节，表 1 |
| 小模型受益更多 | 7 个模型平均每个提升约 17.6 分；GPT-5.4-nano 平均 +26.7，在 ALFWorld 从 34.3 到 69.4；Qwen3.5-4B 平均 +19.2 | 第 4.1 节 |
| 迁移到别的模型 | 在 GPT-5.4 上训出的表格 skill 给 GPT-5.4-mini 用 +9.4、给 nano 用 +3.0；数学 skill 给 mini +4.5、给 nano +5.6 | 第 4.3 节，表 4(a) |
| 迁移到别的运行环境 | 在 Codex 里训的表格 skill 拿到 Claude Code 用，从 22.1 到 81.8（+59.7），比在 Claude Code 里直接训的 80.4 还高；反方向 27.5→71.1。数学 skill 的迁移小得多：Codex→Claude Code 只 +1.6 | 第 4.3 节，表 4(b) |
| 迁移到相近测试集 | 在 OlympiadBench 训的 skill 用到 Omni-MATH，三个模型分别 +3.7、+1.8、+1.3 | 第 4.3 节，表 4(c) |
| 优化器强弱 | 用和执行模型同一个模型当优化器，也能拿到用 GPT-5.5 当优化器时 56%～74% 的提升 | 第 4.3 节，表 5 |
| 部件拆掉会怎样 | 不限修改数量时是 84.6/75.7/57.3，低于默认的 87.1/77.5/61.3；去掉失败修改记录，三个测试集各降 1.6、4.6、2.4；慢更新和优化器经验都去掉，SpreadsheetBench 从 77.5 跌到 55.0 | 第 4.2 节，表 3 |
| 批量大小不敏感 | 反思组大小 1～32、每次跑的题数 8～整轮，SearchQA 和 SpreadsheetBench 都只在 2～3 分范围内波动 | 第 4.2 节，表 2(b)(c) |
| 最后的 skill 很短、只改了几处 | 最终 379～1,995 个 token；真正被收下的修改只有 1～4 处，OfficeQA 的 +39.0 来自 1 处修改 | 第 4.4 节，表 6 |
| 训练成本 | 每个测试集训练用 20.8M～213.8M token；每提升 1 分要 0.6M（表格）到 46.4M（DocVQA）token，只在训练时花 | 第 4.4 节，表 6 |
| 学到的是做法不是答案 | 每个测试集各举一条学到的规则，都是通用做法，例如表格题"先看表结构和公式，把算好的值直接写进整个目标区域，不靠 Excel 重算"、找东西任务"记下去过哪些地方，同类失败几次就换方向" | 第 4.4 节图 4，第 4.5 节 |

**需要说清楚的边界**

- 要有能自动打分的题：作者自己说，只在有自动判分、精确匹配或可执行检查的任务上最适用；主观、多维、判一次很贵的任务，验证门槛要靠更强的人工或模型评估（附录 B）
- 一份 skill 只管一个领域，不做 skill 库；差异很大的领域可能一份不够（附录 B）
- 每格只报一次结果，没有误差范围或多次重复；收不收修改只看"严格高于"，没有做显著性检验。选择集小的时候，可能把运气当成进步（这一条是模型的判断，论文没讨论）
- 消融实验只用 GPT-5.5、只在 3 个测试集上做（第 4.2 节）
- 几处数字对不上（模型核对发现，论文没解释，待确认）：
  - 表 1 里 GPT-5.5 直接对话的 SearchQA 87.3、SpreadsheetBench 80.7、LiveMath 66.9，和默认设置（学习率 4、余弦衰减）在表 3 的 87.1/77.5/61.3 不同，却分别等于表 2 里"固定学习率"那一行（87.3/80.7）和"学习率 8"那一格（66.9）。主表像是取了不同超参数里最好的一次，论文没说主表的超参数怎么选
  - 同样是"学习率 4"，表 2(d) 是 86.5/78.2/56.5，表 3 是 87.1/77.5/61.3
  - 训练/选择/测试的切分比例，表 2 说明写 4:1:5，附录 C 写 2:1:7
  - 附录 C 提到 SealQA，正文实验里没有
- 有的对手只在部分环境里比：TextGrad、GEPA 只比了直接对话，EvoSkill 只比了 Codex 和 Claude Code；ALFWorld 没在两种 agent 环境里跑（第 4.1 节）
- EvoSkill 在 Codex 的 SearchQA 上比不用 skill 还低 20.4 分，论文没解释原因（表 1）
- 迁移结果不均：表格 skill 跨环境迁移很强，数学 skill 只 +1.6；跨测试集迁移只有 1～4 分（表 4）
- 训练要额外跑大量题、调用优化器，一次性任务不划算（附录 B，表 6）
- 预印本，尚未同行评审；文中模型名（GPT-5.5、GPT-5.4-nano、Qwen3.6-35B-A3B 等）照论文写

**作者明说引用的前人工作**（供整理时溯源参考）

- 提示词和 agent 配置的自动优化：GEPA（Agrawal 等 2025，反思式提示词进化）；TextGrad（Yuksekgonul 等 2024，用文字"求导"）；把大模型当优化器（Yang 等 2023，OPRO）；DSPy（Khattab 等 2023）；ABSTRAL、EvoTest
- 从执行记录里反思改进：Reflexion（Shinn 等 2023）；Self-Refine（Madaan 等 2023）
- skill 的定义与评测：SkillsBench（Li 等 2026）；SoK: Agentic Skills（Jiang 等 2026）
- skill 的构建与进化：Trace2Skill、EvoSkill、SkillForge、SkillFoundry、AutoSkill、SkillX、Memp（程序性记忆）、EvoSkills、SkillClaw、SkillRL、AutoRefine、ProcMem、EvolveR
- agent 基础：ReAct、Toolformer、Voyager、SWE-agent；运行环境 Codex（OpenAI 2025）、Claude Code（Anthropic 2025）
- 测试集：SearchQA、SpreadsheetBench、OfficeQA、DocVQA、LiveMathematicianBench、ALFWorld、OlympiadBench、Omni-MATH

## 溯源

（整理时填写，存的时候留空）
