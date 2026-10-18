# 我的思考框架

> 最近一次整理：2026-10-18（第 1 轮）· 新知识 1733 条（已溯源 65、待溯源 354、已归档 1314）· 源知识 380 个
> 规则见 [AGENTS.md](AGENTS.md)。标"草稿"的是模型提炼的，Luke 确认后才改成"已确认"。本轮记录：[docs/reviews/2026-10-18-round-1.md](docs/reviews/2026-10-18-round-1.md)

## 一、我的原则

第 1 轮从 65 条溯源过的新知识里提炼出 7 条，全部是草稿，等 Luke 确认。

### 原则 1：质量靠闭环：回路越短、越能自动判对错，进步越快

- 状态：草稿
- 支撑的新知识：[吴恩达讲做产品的三个循环](clips/2026-10-18-andrewyng-andrew-ng-three-product-loops.md)、[AlphaCodium 与流程工程](clips/2026-10-18-dotey-alphacodium-flow-engineering.md)、[外层harness让智能体连跑数小时](clips/2026-10-18-baoweiheihei-harness-unattended-long-running.md)、[Monolith论文：实时推荐致瘾](clips/2026-10-18-interjc-tiktok-monolith-realtime-recsys.md)、[陶哲轩谈 AI 与数学的演讲要点](clips/2026-10-18-dotey-terence-tao-ai-math-talk.md)、[Samuel 的跳棋程序：机器靠自己对弈学习，下得比写它的人还好](clips/2026-10-18-samuel-machine-learning-checkers.md)、[DeepSeek R1 论文解读：自学成才之路](clips/2026-10-18-oran-ge-deepseek-r1-paper-explained.md)、[开源模型自我验证跑赢闭源模型](clips/2026-10-18-jackyk02-self-verification-open-model-beats-closed.md)（共 8 条）
- 对应的源知识：[控制论](roots/cybernetics.md)、[反馈](roots/feedback.md)、[效果律](roots/law-of-effect.md)、[测试驱动开发](roots/test-driven-development.md)
- 和你已有原则的关系：就是你全局规则里的“生成、评估、改进”，这次找到了理论根：控制论里的负反馈。
- 矛盾：只对能自动判对错的任务（代码、数学、推荐点击）最灵；品味、长期战略这类判断，陶哲轩也强调“人得懂行才能把关”。
- 没想清楚的问题：获客这种反馈慢、难归因的事怎么缩短回路？Reddit 那条“管住投入型指标”是一条线索，还要更多证据。

### 原则 2：能力还在快速变强时，给目标、工具和边界，不写死步骤；脚手架按需加、定期删

- 状态：草稿
- 支撑的新知识：[什么才是 AI Native：别写死步骤](clips/2026-10-18-programerjohann-ai-native-agent-four-things.md)、[Claude Code之父：配置越少越好](clips/2026-10-18-xiaohu-claude-code-minimal-claude-md.md)、[Claude Code播客：工具终将消失](clips/2026-10-18-genie0309-claude-code-podcast-tools-disappear.md)、[合成数据与苦涩的教训讨论](clips/2026-10-18-dotey-synthetic-data-bitter-lesson.md)、[Agent 基础设施的一线观察](clips/2026-10-18-dotey-anthropic-agent-infrastructure-talk.md)（共 5 条）
- 对应的源知识：[苦涩的教训](roots/bitter-lesson.md)、[摩尔定律](roots/moores-law.md)
- 和你已有原则的关系：对应你的“该交给模型的交给模型”，以及“确定的事用确定的代码”；根在 Sutton 的苦涩的教训。
- 矛盾：“Agent 和工作流的区别”那条提醒：能用确定路径解决的，还是用工作流。两者的分界是“这一步需不需要判断”。
- 没想清楚的问题：底层能力什么时候算“不再快速变强”？那时该反过来多写结构。

### 原则 3：一种能力变得人人可得，价值就转到和它互补、仍然稀缺的东西上

- 状态：草稿
- 支撑的新知识：[智力平权之后，行动力成最大差异](clips/2026-10-18-oran-ge-agency-after-intelligence-equality.md)、[DeepResearch小众话题更有价值](clips/2026-10-18-dotey-deep-research-knowledge-value.md)、[大模型是冰箱，赚钱的是卖冷饮的人](clips/2026-10-18-mubeitech-llm-fridge-coca-cola-analogy.md)、[AI 是独立产品还是平台功能](clips/2026-10-18-dotey-ai-product-or-feature.md)、[Thiel一小时讲透从零做垄断的底层逻辑](clips/2026-10-18-kkawsb-peter-thiel-monopoly-lecture.md)（共 5 条）
- 对应的源知识：[互补品](roots/complementary-good.md)、[商品化（同质化）](roots/commoditization.md)、[诱人利润守恒定律](roots/law-of-conservation-of-attractive-profits.md)、[完全竞争](roots/perfect-competition.md)
- 矛盾：“冰箱和可口可乐”这个比喻本身没找到原始出处（待确认）；诱人利润守恒定律的 HBR 原文也没找到。
- 没想清楚的问题：AI 让什么变便宜了，对 GBase 的客户来说，现在稀缺的是什么？

### 原则 4：说不清的知识只能去现场取，取回来要沉淀成可复用的东西

- 状态：草稿
- 支撑的新知识：[Anthropic 讲前线部署工程师](clips/2026-10-18-dotey-fde-101-forward-deployed-engineer.md)、[前线部署工程师为何是 AI 落地时代的关键职业](clips/2026-10-18-indigox-forward-deployed-engineer-ai-era.md)、[AIDE：让用户给样本打"相关/不相关"，用主动学习猜出他真正想查的数据](clips/2026-10-18-dimitriadou-aide-active-learning-data-exploration.md)、[帮家具厂建 AI 产品库月入一万八](clips/2026-10-18-miles-mazy-furniture-factory-ai-product-library.md)、[OpenAI 报告：用户最常用的是懒脑力活](clips/2026-10-18-frxiaobei-chatgpt-usage-lazy-moments.md)（共 5 条）
- 对应的源知识：[默会知识（隐性知识）](roots/tacit-knowledge.md)、[粘滞信息](roots/sticky-information.md)、[《知识在社会中的运用》](roots/the-use-of-knowledge-in-society.md)、[SECI 知识转化模型](roots/seci-model-of-knowledge-dimensions.md)、[待完成的任务](roots/jobs-to-be-done.md)
- 和你已有原则的关系：和你做 GTM 的主线最近：客户的真实需求在现场，不在问卷里。
- 矛盾：前线部署很贵，规模化时会撞上利润率；两条 FDE 都没给出“什么时候该收手”的标准。
- 没想清楚的问题：客户画像也是说不清的知识。能不能像 AIDE 那样，拿一批具体公司让客户判“是 / 不是”，反推出画像？

### 原则 5：先在最小单位验证见效，再逐层放大；需求不清时，先做一个准备扔掉的原型

- 状态：草稿
- 支撑的新知识：[Agent 基础设施的一线观察](clips/2026-10-18-dotey-anthropic-agent-infrastructure-talk.md)、[Thiel一小时讲透从零做垄断的底层逻辑](clips/2026-10-18-kkawsb-peter-thiel-monopoly-lecture.md)、[Vibe Coding：原型加重设计两步法](clips/2026-10-18-dotey-vibe-coding-prototype-method.md)、[多数 Agent 其实只是工作流](clips/2026-10-18-eze-is-1-agent-vs-workflow-definition.md)（共 4 条）
- 对应的源知识：[加尔定律](roots/galls-law.md)、[《人月神话》（准备扔掉一个）](roots/the-mythical-man-month.md)、[从 0 到 1](roots/zero-to-one.md)
- 和你已有原则的关系：对应你的“先骨架后填充”，根在加尔定律。
- 矛盾：暂时没看到反例。
- 没想清楚的问题：“最小单位”在 GTM 里是什么：一个客户、一个行业，还是一封邮件？

### 原则 6：执行者越多，协调和验收越贵；整体速度由最慢的环节决定

- 状态：草稿
- 支撑的新知识：[Anthropic 多智能体研究系统详解](clips/2026-10-18-oran-ge-anthropic-multi-agent-research.md)、[Codex 28天做出Sora安卓版](clips/2026-10-18-dotey-codex-sora-android-28-days.md)、[玉伯谈 AI 时代小团队生产力的真相](clips/2026-10-18-saitowu-small-team-productivity-ai-era.md)、[前Meta工程师的AI优先团队落地报告](clips/2026-10-18-ayi-ainotes-peter-pang-ai-first-report.md)、[唐杰谈缩放定律：不只是堆参数](clips/2026-10-18-jietang-scaling-law-beyond-parameters.md)（共 5 条）
- 对应的源知识：[布鲁克斯定律](roots/brookss-law.md)、[管理幅度](roots/span-of-control.md)、[约束理论](roots/theory-of-constraints.md)、[阿姆达尔定律](roots/amdahls-law.md)
- 矛盾：Anthropic 的多智能体研究显示，价值高、能并行的任务拆开反而更好；所以不是“越少越好”，而是“拆之前先算协调成本”。
- 没想清楚的问题：你同时开多个会话、多个 worktree，瓶颈是不是已经从“写”变成了“你的审查”？

### 原则 7：先保证不出局：不拿输不起的去换用不上的，把关键依赖分散开

- 状态：草稿
- 支撑的新知识：[巴菲特经典演讲：先保证不穷回去](clips/2026-10-18-nextbullready-buffett-classic-speech.md)、[三旗理论：合法减税、保护资产、自由生活](clips/2026-10-18-eric-make-money-three-flags-theory.md)、[张一鸣 66 条成长心得与延迟满足](clips/2026-10-18-sea-bitcoin-zhang-yiming-66-growth-tips.md)（共 3 条）
- 对应的源知识：[破产风险](roots/risk-of-ruin.md)、[赌徒破产问题](roots/gamblers-ruin.md)、[凯利公式](roots/kelly-criterion.md)、[分散投资](roots/diversification-finance.md)
- 矛盾：张一鸣那条转述者认为“落袋为安也是选项”，和棉花糖实验对着干；后来的复现研究（Watts 2018）支持他：延迟满足划不划算，要看未来回报是否可靠。
- 没想清楚的问题：三旗理论的具体做法在配图里，没核对到。

## 二、知识底座

被新知识指向得最多的源理论。“直接”是新知识直接指向它；“连同间接”还算上了通过更上层源知识追到它的。排在最前面的，就是最近看到的这些新东西共同的根。

| 排名 | 源知识 | 被几条新知识指向（直接 / 连同间接） | 更底层的源头 |
|---|---|---|---|
| 1 | [控制论](roots/cybernetics.md) | 4 / 17 | 已到基础层 |
| 2 | [反馈](roots/feedback.md) | 0 / 15 | 已到基础层 |
| 3 | [自然选择](roots/natural-selection.md) | 0 / 15 | 已到基础层 |
| 4 | [经验曲线效应](roots/experience-curve-effect.md) | 1 / 11 | [学习曲线](roots/learning-curve.md) |
| 5 | [学习曲线](roots/learning-curve.md) | 0 / 11 | 已到基础层 |
| 6 | [苦涩的教训](roots/bitter-lesson.md) | 6 / 10 | [摩尔定律](roots/moores-law.md) |
| 7 | [摩尔定律](roots/moores-law.md) | 0 / 10 | [经验曲线效应](roots/experience-curve-effect.md) |
| 8 | [控制理论](roots/control-theory.md) | 0 / 9 | [反馈](roots/feedback.md) |
| 9 | [信息论](roots/information-theory.md) | 0 / 9 | 已到基础层 |
| 10 | [分工](roots/division-of-labour.md) | 3 / 8 | [比较优势](roots/comparative-advantage.md) |
| 11 | [比较优势](roots/comparative-advantage.md) | 0 / 8 | 已到基础层 |
| 12 | [效果律](roots/law-of-effect.md) | 0 / 7 | [自然选择](roots/natural-selection.md) |
| 13 | [孔多塞陪审团定理](roots/condorcets-jury-theorem.md) | 0 / 6 | 已到基础层 |
| 14 | [正反馈](roots/positive-feedback.md) | 0 / 6 | [控制论](roots/cybernetics.md) |
| 15 | [构建高效的智能体](roots/anthropic-2024-building-effective-agents.md) | 4 / 5 | [智能体](roots/intelligent-agent.md)、[分工](roots/division-of-labour.md) |

## 三、待查

真正的新东西最可能藏在这里。

### 和经典理论对着干的

| 新知识 | 对着干的经典 | 强弱 |
|---|---|---|
| [杨立昆谈智能不等于控制欲](clips/2026-10-18-dotey-lecun-intelligence-not-domination.md) | [工具性趋同](roots/instrumental-convergence.md) | 强 |
| [LeCun：下个万亿AI公司不靠LLM](clips/2026-10-18-phosphenq-lecun-lecture-beyond-llms.md) | [神经网络规模定律](roots/neural-scaling-law.md) | 强 |
| [唐杰谈缩放定律：不只是堆参数](clips/2026-10-18-jietang-scaling-law-beyond-parameters.md) | Kaplan 等 2020《神经语言模型的缩放定律》 | 强 |
| [陶哲轩谈 AI 与数学的演讲要点](clips/2026-10-18-dotey-terence-tao-ai-math-talk.md) | 微软《通用人工智能的火花》（GPT-4 早期实验） | 强 |
| [Pi 作者：代码即真相，Bash 够用](clips/2026-10-18-dotey-pi-authors-code-bash-insights.md) | 检索增强生成（RAG） | 强 |
| [Karpathy 的 YC 演讲：软件 3.0](clips/2026-10-18-op7418-karpathy-software-3-talk.md) | Dijkstra《论“自然语言编程”之愚蠢》 | 弱（待 Luke 确认） |
| [Samuel 的跳棋程序：机器靠自己对弈学习，下得比写它的人还好](clips/2026-10-18-samuel-machine-learning-checkers.md) | 洛夫莱斯夫人的异议（机器不能原创） | 弱（待 Luke 确认） |
| [张一鸣 66 条成长心得与延迟满足](clips/2026-10-18-sea-bitcoin-zhang-yiming-66-growth-tips.md) | 斯坦福棉花糖实验 | 弱（待 Luke 确认） |
| [Karpathy：让AI模拟专家来答](clips/2026-10-18-dotey-karpathy-simulator-not-entity.md) | “让 AI 扮演专家效果更好” | 弱（待 Luke 确认） |

两条杨立昆和唐杰、杨植麟的新知识正好对着干：一边说规模扩展到头了，一边在押规模定律继续成立。

### 没找到源头的

第 1 轮 65 条都找到了源头。

### 出处还没核实的

- [“大模型是冰箱，可口可乐还没出现”比喻](roots/palihapitiya-refrigeration-coca-cola-analogy.md)：只找到二手转述，两篇转述给的时间对不上
- [为 AGI 而压缩](roots/rae-2023-compression-for-agi.md)：讲座原视频没找到，只有二手整理

### 顺手查出来的误传

- Samuel 的跳棋程序“超越了写它的人”，是 Wiener 1960 年的解读；Samuel 本人同年撰文不同意（见 [Samuel 的跳棋程序：机器靠自己对弈学习，下得比写它的人还好](clips/2026-10-18-samuel-machine-learning-checkers.md)）
- “ikigai 四圈图”不是日本原创，是 Marc Winn 2014 年改自西班牙人 Zuzunaga 的图；日本原本的生き甲斐不要求能赚钱（见 [世界需要、擅长、热爱、能谋生的交集](clips/2026-10-18-zutaomin-ikigai-meaning-of-life.md)）
- 情境领导里的 S1～S4 是领导风格，员工的成熟度是 R1～R4 / D1～D4，宝玉那条把两者混了（见 [情境领导模型 S1 到 S4 会动态变化](clips/2026-10-18-dotey-situational-leadership-model.md)）
- “枢密院高级国务大臣”不是明朝官名，徐光启实际是礼部尚书、文渊阁大学士（见 [南明皇室受洗的冷知识：借调侃“历史老师去美国”说出来](clips/2026-10-18-tombkeeper-southern-ming-baptism.md)）
- 奥卡姆剃刀那句名言不见于奥卡姆本人的著作

## 四、主题地图

全部新知识按主题和发布年份分布，看关注点这几年怎么变。由 `tools/topic_map.py` 生成。

<!-- topic-map:begin -->
共 1733 条新知识（含已归档）。数字是每年存下的条数；按发布年份算，不是保存日期。

| 主题 | 更早 | 2023 | 2024 | 2025 | 2026 | 未知 | 合计 | 观点 / 工具 / 教程 |
|---|---|---|---|---|---|---|---|---|
| Agent 与 Skill |  | 8 | 38 | 115 | 97 |  | 258 | 38 / 169 / 51 |
| 其他 |  | 25 | 32 | 47 | 92 |  | 196 | 71 / 110 / 15 |
| AI 产品与创业 |  | 18 | 32 | 43 | 83 |  | 176 | 125 / 41 / 10 |
| 视频生成 |  | 2 | 10 | 18 | 138 |  | 168 | 13 / 65 / 90 |
| 编程智能体 |  | 4 | 21 | 38 | 77 |  | 140 | 27 / 52 / 61 |
| 模型与本地部署 |  | 9 | 14 | 27 | 88 |  | 138 | 16 / 95 / 27 |
| 设计与前端 |  | 8 | 17 | 39 | 57 |  | 121 | 8 / 77 / 36 |
| 图像生成 |  | 11 | 29 | 45 | 21 |  | 106 | 1 / 62 / 43 |
| 提示词与写作 |  | 5 | 17 | 61 | 12 |  | 95 | 7 / 15 / 73 |
| 语音与数字人 |  | 9 | 41 | 19 | 24 |  | 93 | 0 / 82 / 11 |
| 学习与研究 | 2 | 11 | 31 | 16 | 21 |  | 81 | 16 / 32 / 33 |
| 增长与获客 |  | 1 | 15 | 16 | 41 |  | 73 | 24 / 22 / 27 |
| 思维与成长 |  | 6 | 12 | 8 | 24 | 1 | 51 | 50 / 1 / 0 |
| 日本 |  | 5 | 4 | 6 | 9 |  | 24 | 12 / 11 / 1 |
| 历史与冷知识 |  | 3 | 1 | 3 | 6 |  | 13 | 11 / 1 / 1 |

**每个主题的代表**（先选已溯源的，再选观点类，最后按发布时间取最新）

- **Agent 与 Skill**：[AlphaCodium 与流程工程](clips/2026-10-18-dotey-alphacodium-flow-engineering.md)、[Anthropic 多智能体研究系统详解](clips/2026-10-18-oran-ge-anthropic-multi-agent-research.md)、[什么才是 AI Native：别写死步骤](clips/2026-10-18-programerjohann-ai-native-agent-four-things.md)
- **其他**：[三旗理论：合法减税、保护资产、自由生活](clips/2026-10-18-eric-make-money-three-flags-theory.md)、[平屋，平屋的配图短帖](clips/2026-10-18-qiancaobuzhiqiu-hiraya-photos-three.md)、[图拉鼎在村里拍结婚照并登记](clips/2026-10-18-tualatrix-tualatrix-wedding-news.md)
- **AI 产品与创业**：[杨立昆谈智能不等于控制欲](clips/2026-10-18-dotey-lecun-intelligence-not-domination.md)、[AI 是独立产品还是平台功能](clips/2026-10-18-dotey-ai-product-or-feature.md)、[为什么大多数公司不该有 AI 战略](clips/2026-10-18-dotey-why-no-ai-strategy.md)
- **视频生成**：[H3 接力生成 110 秒古装短片](clips/2026-10-18-eternityspring-minimax-h3-continuum-short-film.md)、[Fable 5.5 做的人类简史视频](clips/2026-10-18-tz-2022-fable-human-history-video.md)、[Opus 5.5 自己剪出汕头 vlog](clips/2026-10-18-dashiaixz-opus-edits-vlog-itself.md)
- **编程智能体**：[公司推广 AI 编程为何要靠内部](clips/2026-10-18-dotey-promote-ai-coding-in-company.md)、[Vibe Coding：原型加重设计两步法](clips/2026-10-18-dotey-vibe-coding-prototype-method.md)、[Claude Code播客：工具终将消失](clips/2026-10-18-genie0309-claude-code-podcast-tools-disappear.md)
- **模型与本地部署**：[Karpathy 谈 GPT 现状](clips/2026-10-18-dotey-karpathy-state-of-gpt.md)、[合成数据与苦涩的教训讨论](clips/2026-10-18-dotey-synthetic-data-bitter-lesson.md)、[DeepSeek R1 论文解读：自学成才之路](clips/2026-10-18-oran-ge-deepseek-r1-paper-explained.md)
- **设计与前端**：[设计师口袋心理学 53 个知识卡片](clips/2026-10-18-hitw93-designer-pocket-psychology.md)、[学 Vercel 设计系统的逻辑](clips/2026-10-18-mengkepm-vercel-design-system-learn-logic.md)、[Sonnet3.5让前端设计起飞](clips/2026-10-18-arvin17x-v0-sonnet-design-moment.md)
- **图像生成**：[Qwen 生图 Turbo 开放权重](clips/2026-10-18-qwendevs-qwen-image-turbo-open-weights.md)、[Qwen 换脸换头 LoRA 更新](clips/2026-10-18-lonely-mh-qwen-image-face-swap-lora.md)、[Qwen-Image 2.1 即将开源](clips/2026-10-18-qwendevs-qwen-image-2-1-early-access.md)
- **提示词与写作**：[Karpathy：让AI模拟专家来答](clips/2026-10-18-dotey-karpathy-simulator-not-entity.md)、[用航空维修英语规范让 AI 讲清楚话](clips/2026-10-18-hitw93-asd-ste100-clarity-waza.md)、[Anthropic专家谈提示词工程师](clips/2026-10-18-eze-is-1-anthropic-prompt-engineering-notes.md)
- **语音与数字人**：[Fish 开源 Drama3 语音模型](clips/2026-10-18-kay2289123-fish-audio-drama3-open-source.md)、[Griffin 全双工视频模型解读](clips/2026-10-18-maxforai-griffin-full-duplex-video-model.md)、[Griffin 通过视频图灵测试](clips/2026-10-18-tavus-tavus-griffin-video-turing-test.md)
- **学习与研究**：[Samuel 的跳棋程序：机器靠自己对弈学习，下得比写它的人还好](clips/2026-10-18-samuel-machine-learning-checkers.md)、[AIDE：让用户给样本打"相关/不相关"，用主动学习猜出他真正想查的数据](clips/2026-10-18-dimitriadou-aide-active-learning-data-exploration.md)、[陶哲轩谈 AI 与数学的演讲要点](clips/2026-10-18-dotey-terence-tao-ai-math-talk.md)
- **增长与获客**：[Monolith论文：实时推荐致瘾](clips/2026-10-18-interjc-tiktok-monolith-realtime-recsys.md)、[Reddit 营销怎么算投产：看投入型指标](clips/2026-10-18-yangyi-reddit-marketing-input-metrics.md)、[MrBeast的YouTube上瘾蓝图](clips/2026-10-18-0xcheshire-youtube-addiction-blueprint.md)
- **思维与成长**：[张一鸣 66 条成长心得与延迟满足](clips/2026-10-18-sea-bitcoin-zhang-yiming-66-growth-tips.md)、[Paul Graham 谈超线性回报](clips/2026-10-18-dotey-paul-graham-superlinear-returns.md)、[天涯神贴：专注一件事死磕到擅长](clips/2026-10-18-caijingtianxia-focus-one-thing-tianya-post.md)
- **日本**：[日本 Times Car 被盗风险](clips/2026-10-18-interjc-times-car-theft-risk.md)、[日本公司邮件与外资邮件的对比段子](clips/2026-10-18-hikaru-hackjpn-japan-vs-foreign-email-meme.md)、[Kimi 进入日本并送出月度套餐](clips/2026-10-18-kimiai-japan-kimi-japan-launch-giveaway.md)
- **历史与冷知识**：[南明皇室受洗的冷知识：借调侃“历史老师去美国”说出来](clips/2026-10-18-tombkeeper-southern-ming-baptism.md)、[美国人一天生活的数据可视化](clips/2026-10-18-alexxubyte-day-in-life-americans-dataviz.md)、[一百年前世界的上色影像](clips/2026-10-18-historyinmemes-colorized-footage-100-years-ago.md)
<!-- topic-map:end -->
