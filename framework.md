# 我的思考框架

> 最近一次整理：2026-10-18（第 2 轮）· 新知识 1734 条（已溯源 216、待溯源 1、已归档 1517）· 源知识 769 个
> 规则见 [AGENTS.md](AGENTS.md)。标"草稿"的是模型提炼的，Luke 确认后才改成"已确认"。本轮记录：[docs/reviews/2026-10-18-round-2.md](docs/reviews/2026-10-18-round-2.md)

## 一、我的原则

第 1 轮从 65 条里提炼出 7 条。第 2 轮又溯源了 151 条：7 条都补上了新证据，另外新增 4 条（原则 8～11）。2026-10-18 Luke 全部确认，其中原则 2、6、8 按建议改了说法。

### 原则 1：质量靠闭环：回路越短、越能自动判对错，进步越快

- 状态：已确认（2026-10-18）
- 支撑的新知识：[吴恩达讲做产品的三个循环](clips/2026-10-18-andrewyng-andrew-ng-three-product-loops.md)、[AlphaCodium 与流程工程](clips/2026-10-18-dotey-alphacodium-flow-engineering.md)、[外层harness让智能体连跑数小时](clips/2026-10-18-baoweiheihei-harness-unattended-long-running.md)、[Monolith论文：实时推荐致瘾](clips/2026-10-18-interjc-tiktok-monolith-realtime-recsys.md)、[陶哲轩谈 AI 与数学的演讲要点](clips/2026-10-18-dotey-terence-tao-ai-math-talk.md)、[Samuel 的跳棋程序：机器靠自己对弈学习，下得比写它的人还好](clips/2026-10-18-samuel-machine-learning-checkers.md)、[DeepSeek R1 论文解读：自学成才之路](clips/2026-10-18-oran-ge-deepseek-r1-paper-explained.md)、[开源模型自我验证跑赢闭源模型](clips/2026-10-18-jackyk02-self-verification-open-model-beats-closed.md)
- 第 2 轮新增：[Anthropic：让模型验证自己的输出](clips/2026-10-18-0xcodez-anthropic-agent-loop-self-verify.md)、[吴恩达：自我改进循环将取代提示](clips/2026-10-18-0xmovez-andrew-ng-self-improving-loops.md)、[智谱让 GLM-5.3 自己优化推理系统](clips/2026-10-18-dotey-glm-5-3-optimizes-own-inference.md)、[Astra 电脑操作让验收成闭环](clips/2026-10-18-dotey-astra-computer-use-acceptance-loop.md)、[Claude Code之父的三条心得](clips/2026-10-18-ayi-ainotes-boris-cherny-workflow-three-rules.md)、[自然语言 Agent 应像好员工的七点](clips/2026-10-18-remixdesigner-agent-as-good-employee.md)、[Anthropic专家谈提示词工程师](clips/2026-10-18-eze-is-1-anthropic-prompt-engineering-notes.md)、[开 100 家便利店经验写成选址指南](clips/2026-10-18-hitw93-convenience-store-site-selection.md)（共 16 条）
- 对应的源知识：[控制论](roots/cybernetics.md)、[反馈](roots/feedback.md)、[效果律](roots/law-of-effect.md)、[测试驱动开发](roots/test-driven-development.md)；第 2 轮新增 [验收测试](roots/acceptance-testing.md)、[PDCA 循环（计划-执行-检查-处置）](roots/pdca.md)、[复合工程](roots/compounding-engineering.md)、[奖励塑形（势函数塑形下的策略不变性）](roots/ng-1999-reward-shaping.md)
- 和你已有原则的关系：就是你全局规则里的“生成、评估、改进”，这次找到了理论根：控制论里的负反馈。
- 矛盾：只对能自动判对错的任务（代码、数学、推荐点击）最灵；品味、长期战略这类判断，陶哲轩也强调“人得懂行才能把关”。
- 第 2 轮的新线索：智谱那条给了缩短回路的具体办法：结果信号太稀疏（只知道最后成没成）时，把它拆成一层层便宜、能马上验证的过程信号。Boris Cherny 那条补了另一半：每次纠正都写进 CLAUDE.md，回路才会越转越好，而不是每次从头来。
- 没想清楚的问题：获客这种反馈慢、难归因的事怎么缩短回路？按智谱的思路，可以把“签单”拆成“打开、回信、约到会”这几层过程信号分别优化（推断，待 Luke 确认）。复旦那条“看能说明因果的指标，不看虚荣指标”（[复旦分享：脑科学视角拆品牌营销](clips/2026-10-18-yangyi-fudan-brand-marketing-neuroscience.md)）提醒：拆出来的过程信号要真的能预测结果。

### 原则 2：能力还在快速变强时，给目标、工具和边界，不写死步骤；脚手架按需加、定期删；要长期保持一致、出错代价大的部分照样写死

- 状态：已确认（2026-10-18，说法按建议改过）
- 支撑的新知识：[什么才是 AI Native：别写死步骤](clips/2026-10-18-programerjohann-ai-native-agent-four-things.md)、[Claude Code之父：配置越少越好](clips/2026-10-18-xiaohu-claude-code-minimal-claude-md.md)、[Claude Code播客：工具终将消失](clips/2026-10-18-genie0309-claude-code-podcast-tools-disappear.md)、[合成数据与苦涩的教训讨论](clips/2026-10-18-dotey-synthetic-data-bitter-lesson.md)、[Agent 基础设施的一线观察](clips/2026-10-18-dotey-anthropic-agent-infrastructure-talk.md)
- 第 2 轮新增：[谈用 Claude 做智能体：少搭脚手架](clips/2026-10-18-alexalbert-agent-scaffolding-context-talk.md)、[提示词精髓：有什么、做什么、怎么做](clips/2026-10-18-dotey-prompt-context-task-how.md)、[Sora 团队伯克利课堂分享字幕翻译](clips/2026-10-18-dotey-sora-team-berkeley-talk.md)（共 8 条）
- 对应的源知识：[苦涩的教训](roots/bitter-lesson.md)、[摩尔定律](roots/moores-law.md)；第 2 轮新增 [归纳偏置](roots/inductive-bias.md)、[OpenAI 推理模型提示建议（提示要简单直接、不必写思维链）](roots/openai-2024-o1-prompting-advice.md)、[任务式指挥](roots/mission-type-tactics.md)
- 和你已有原则的关系：对应你的“该交给模型的交给模型”，以及“确定的事用确定的代码”；根在 Sutton 的苦涩的教训。第 2 轮找到一个军事上的老版本：任务式指挥（只下达意图和目标，不规定怎么打）。
- 矛盾：
  - “Agent 和工作流的区别”那条提醒：能用确定路径解决的，还是用工作流。两者的分界是“这一步需不需要判断”。第 2 轮的 [给公司业务接入智能体的五点思考](clips/2026-10-18-dotey-enterprise-agent-integration-tips.md) 和 [大白话讲清 Agent、工作流与 ReACT](clips/2026-10-18-yangyi-agent-workflow-react-explained.md) 说法一样：新问题先让模型探索，跑通了再固化成规则。
  - [Tripo Eden：先建地图再渲染](clips/2026-10-18-svpino-tripo-eden-world-model-map.md) 和 Sora 那条正好对着干：Sora 团队押“规模够了，物体不消失这种能力自己会冒出来”，Tripo 押“要长期一致的东西，必须显式存一份状态”。
- 没想清楚的问题：底层能力什么时候算“不再快速变强”？那时该反过来多写结构。Tripo 那条给了一个判断口：需要长期保持一致、出错代价大的部分，先写死。

### 原则 3：一种能力变得人人可得，价值就转到和它互补、仍然稀缺的东西上

- 状态：已确认（2026-10-18）
- 已加进全局规则：2026-10-18，`~/.claude/CLAUDE.md` 第 5 节「先问什么变便宜了」
- 支撑的新知识：[智力平权之后，行动力成最大差异](clips/2026-10-18-oran-ge-agency-after-intelligence-equality.md)、[DeepResearch小众话题更有价值](clips/2026-10-18-dotey-deep-research-knowledge-value.md)、[大模型是冰箱，赚钱的是卖冷饮的人](clips/2026-10-18-mubeitech-llm-fridge-coca-cola-analogy.md)、[AI 是独立产品还是平台功能](clips/2026-10-18-dotey-ai-product-or-feature.md)、[Thiel一小时讲透从零做垄断的底层逻辑](clips/2026-10-18-kkawsb-peter-thiel-monopoly-lecture.md)
- 第 2 轮新增：[AI 时代最值钱的是懂 AI 的产品经理](clips/2026-10-18-dotey-ai-product-manager-skills.md)、[稀缺从怎么做转向做什么](clips/2026-10-18-lijigang-scarcity-how-to-what.md)、[品味可以被模仿，决策才不可替代](clips/2026-10-18-mengkepm-taste-copyable-decision-irreplaceable.md)、[AIGC 作品的关键是加上人味](clips/2026-10-18-jesselaunz-aigc-add-human-touch.md)、[NVIDIA DGX Spark 从买机器到变现指南](clips/2026-10-18-ai-goge-dgx-spark-monetization-guide.md)、[Gumloop四人团队冲击十亿公司](clips/2026-10-18-wanghao8080-gumloop-small-team-unicorn.md)、[对接 SD 做细分领域插画生成器](clips/2026-10-18-yangyi-niche-illustration-generator.md)、[写好Spec后让Agent整周自动开发](clips/2026-10-18-timyangnet-spec-driven-agent-development.md)、[吴恩达的智能体编程时代软件工程能力图](clips/2026-10-18-andrewyng-andrew-ng-ai-engineering-skills-map.md)、[技术领导者要知道的生成式 AI 五个真相](clips/2026-10-18-dotey-five-hard-truths-genai.md)（共 15 条，是支撑最多的一条）
- 对应的源知识：[互补品](roots/complementary-good.md)、[商品化（同质化）](roots/commoditization.md)、[诱人利润守恒定律](roots/law-of-conservation-of-attractive-profits.md)、[完全竞争](roots/perfect-competition.md)；第 2 轮新增 [《预测机器：人工智能的简单经济学》](roots/agrawal-2018-prediction-machines.md)、[杰文斯悖论](roots/jevons-paradox.md)、[没有银弹（本质复杂度与偶然复杂度）](roots/no-silver-bullet.md)、[资源基础观](roots/resource-based-view.md)
- 矛盾：“冰箱和可口可乐”这个比喻本身没找到原始出处（待确认）；诱人利润守恒定律的 HBR 原文也没找到。
- 第 2 轮的新线索：这一轮的 10 条对“什么还稀缺”说法很一致：决定做什么（规格、取舍、判断）、分发、独有而干净的数据、离客户问题最近的那一层。布鲁克斯 1986 年《没有银弹》早就说过：最难的是精确决定要造什么。
- 没想清楚的问题：AI 让什么变便宜了，对 GBase 的客户来说，现在稀缺的是什么？

### 原则 4：说不清的知识只能去现场取，取回来要沉淀成可复用的东西

- 状态：已确认（2026-10-18）
- 已加进全局规则：2026-10-18，`~/.claude/CLAUDE.md` 第 5 节「需求去现场取」
- 支撑的新知识：[Anthropic 讲前线部署工程师](clips/2026-10-18-dotey-fde-101-forward-deployed-engineer.md)、[前线部署工程师为何是 AI 落地时代的关键职业](clips/2026-10-18-indigox-forward-deployed-engineer-ai-era.md)、[AIDE：让用户给样本打"相关/不相关"，用主动学习猜出他真正想查的数据](clips/2026-10-18-dimitriadou-aide-active-learning-data-exploration.md)、[帮家具厂建 AI 产品库月入一万八](clips/2026-10-18-miles-mazy-furniture-factory-ai-product-library.md)、[OpenAI 报告：用户最常用的是懒脑力活](clips/2026-10-18-frxiaobei-chatgpt-usage-lazy-moments.md)
- 第 2 轮新增：[范冰免费开源新书《前置部署工程师》](clips/2026-10-18-iluciddreaming-fde-book-free-open-source.md)、[国内 ToB 智能体至少还要一年](clips/2026-10-18-frxiaobei-tob-agent-one-year-away.md)、[同城 IP 团队的真实 Agent 需求](clips/2026-10-18-wanghao8080-local-ip-agent-need.md)、[Anthropic：用技能代替独立智能体](clips/2026-10-18-hongming731-anthropic-agent-skills-talk.md)、[征求产品意见别只问程序员群体](clips/2026-10-18-gorden-sun-dont-ask-programmers-product-feedback.md)、[做到千万美元ARR的B2B代理路径](clips/2026-10-18-financeyf5-b2b-ai-agent-10m-arr.md)、[Clay：给 ToB 销售补全客户数据](clips/2026-10-18-wanghao8080-clay-sales-data-enrichment.md)（共 12 条）
- 对应的源知识：[默会知识（隐性知识）](roots/tacit-knowledge.md)、[粘滞信息](roots/sticky-information.md)、[《知识在社会中的运用》](roots/the-use-of-knowledge-in-society.md)、[SECI 知识转化模型](roots/seci-model-of-knowledge-dimensions.md)、[待完成的任务](roots/jobs-to-be-done.md)；第 2 轮新增 [知识获取瓶颈](roots/knowledge-acquisition-bottleneck.md)、[知识原则：智能体的本事主要来自专门知识](roots/feigenbaum-1977-knowledge-engineering.md)、[过程性知识（知道怎么做）](roots/procedural-knowledge.md)、[苦差事盲区](roots/graham-2012-schlep-blindness.md)
- 和你已有原则的关系：和你做 GTM 的主线最近：客户的真实需求在现场，不在问卷里。第 2 轮补上了“沉淀”那一半：Anthropic 说“别造新 agent，造 skill”，skill 就是把现场取回的做事经验写成文件；这和 1977 年专家系统时代的“知识工程”是同一件事，当年卡在“知识获取瓶颈”，现在 ToB agent 卡的还是它。
- 矛盾：前线部署很贵，规模化时会撞上利润率；两条 FDE 都没给出“什么时候该收手”的标准。
- 没想清楚的问题：客户画像也是说不清的知识。能不能像 AIDE 那样，拿一批具体公司让客户判“是 / 不是”，反推出画像？“征求意见别只问程序员”那条提醒：判“是 / 不是”的人必须是真正的目标客户。

### 原则 5：先在最小单位验证见效，再逐层放大；需求不清时，先做一个准备扔掉的原型

- 状态：已确认（2026-10-18）
- 支撑的新知识：[Agent 基础设施的一线观察](clips/2026-10-18-dotey-anthropic-agent-infrastructure-talk.md)、[Thiel一小时讲透从零做垄断的底层逻辑](clips/2026-10-18-kkawsb-peter-thiel-monopoly-lecture.md)、[Vibe Coding：原型加重设计两步法](clips/2026-10-18-dotey-vibe-coding-prototype-method.md)、[多数 Agent 其实只是工作流](clips/2026-10-18-eze-is-1-agent-vs-workflow-definition.md)
- 第 2 轮新增：[工具站出海月入 3000 刀的一年踩坑记](clips/2026-10-18-gefei55-tool-site-overseas-lessons.md)、[Marc Lou 六月赚 8.3 万美元](clips/2026-10-18-marclou-marclou-june-2026-revenue.md)、[宝玉写提示词的原则：做成可玩的模板](clips/2026-10-18-dotey-dotey-prompt-writing-principles.md)、[OpenAI 企业用 AI 的七条经验](clips/2026-10-18-shao-meng-openai-enterprise-ai-lessons.md)（共 8 条）
- 对应的源知识：[加尔定律](roots/galls-law.md)、[《人月神话》（准备扔掉一个）](roots/the-mythical-man-month.md)、[从 0 到 1](roots/zero-to-one.md)；第 2 轮新增 [精益创业](roots/lean-startup.md)、[小赌注组合](roots/portfolio-of-small-bets.md)、[过早优化是万恶之源（Knuth《带 goto 语句的结构化编程》）](roots/knuth-1974-structured-programming-go-to.md)
- 和你已有原则的关系：对应你的“先骨架后填充”，根在加尔定律。宝玉写提示词那条是同一个顺序：先让一个具体例子跑通，再抽象成模板，优化放最后（Knuth：过早优化是万恶之源）。
- 矛盾：暂时没看到反例。
- 没想清楚的问题：“最小单位”在 GTM 里是什么：一个客户、一个行业，还是一封邮件？B2B 代理那条给了一个答案：一个行业里一条还靠人和表格硬撑的苦活流程，做透了再复制到相邻行业（推断，待 Luke 确认）。

### 原则 6：执行者越多，协调和验收越贵；整体速度由最慢的环节决定。执行一变快，瓶颈就移到定义需求、验收和获客上

- 状态：已确认（2026-10-18，说法按建议改过）
- 已加进全局规则：2026-10-18，`~/.claude/CLAUDE.md` 第 5 节「找新瓶颈」
- 支撑的新知识：[Anthropic 多智能体研究系统详解](clips/2026-10-18-oran-ge-anthropic-multi-agent-research.md)、[Codex 28天做出Sora安卓版](clips/2026-10-18-dotey-codex-sora-android-28-days.md)、[玉伯谈 AI 时代小团队生产力的真相](clips/2026-10-18-saitowu-small-team-productivity-ai-era.md)、[前Meta工程师的AI优先团队落地报告](clips/2026-10-18-ayi-ainotes-peter-pang-ai-first-report.md)、[唐杰谈缩放定律：不只是堆参数](clips/2026-10-18-jietang-scaling-law-beyond-parameters.md)
- 第 2 轮新增：[两天用完 AI 额度，四天做营销的周节奏](clips/2026-10-18-yihui-indie-ai-two-day-dev-week-rhythm.md)、[Anthropic 设计负责人谈 AI 时代设计流程](clips/2026-10-18-dotey-anthropic-design-process-ai-era.md)、[Claude Code 的 Task 工具原理](clips/2026-10-18-dotey-claude-code-task-subagent.md)、[用个人AI编排者带动一支永不睡觉的开发队](clips/2026-10-18-ayi-ainotes-personal-ai-orchestrator-openclaw.md)、[备忘录加 worktree 就够了](clips/2026-10-18-hilng77042-opc-agents-notes-worktrees.md)、[Kimi-code重构一个月的架构复盘](clips/2026-10-18-real-kai42-kimi-code-rewrite-retrospective.md)（共 11 条）
- 对应的源知识：[布鲁克斯定律](roots/brookss-law.md)、[管理幅度](roots/span-of-control.md)、[约束理论](roots/theory-of-constraints.md)、[阿姆达尔定律](roots/amdahls-law.md)；第 2 轮新增 [分治法](roots/divide-and-conquer-algorithm.md)、[别做多智能体](roots/yan-2025-dont-build-multi-agents.md)
- 矛盾：Anthropic 的多智能体研究显示，价值高、能并行的任务拆开反而更好；所以不是“越少越好”，而是“拆之前先算协调成本”。Cognition《别做多智能体》站在另一边：拆开会丢上下文、各自做出互相冲突的决定。
- 第 2 轮的新线索：约束理论现在被直接指向 7 次，并列第 3，其中 5 条是第 2 轮的。几条说的是同一件事：写代码一被 AI 加速，瓶颈就移到没被加速的环节：定义需求、验收、获客。独立开发者那条干脆把一周拆成“两天开发、四天做营销”。
- 没想清楚的问题：你同时开多个会话、多个 worktree，瓶颈是不是已经从“写”变成了“你的审查”？kimi-code 那条的结论是：质量最终取决于人投入了多少注意力。

### 原则 7：先保证不出局：不拿输不起的去换用不上的，把关键依赖分散开

- 状态：已确认（2026-10-18）
- 支撑的新知识：[巴菲特经典演讲：先保证不穷回去](clips/2026-10-18-nextbullready-buffett-classic-speech.md)、[三旗理论：合法减税、保护资产、自由生活](clips/2026-10-18-eric-make-money-three-flags-theory.md)、[张一鸣 66 条成长心得与延迟满足](clips/2026-10-18-sea-bitcoin-zhang-yiming-66-growth-tips.md)
- 第 2 轮新增：[Marc Lou 六月赚 8.3 万美元](clips/2026-10-18-marclou-marclou-june-2026-revenue.md)、[离职大厂做 OPC 第一年收入报告](clips/2026-10-18-weiyipei-opc-first-year-income-report.md)（共 5 条）
- 对应的源知识：[破产风险](roots/risk-of-ruin.md)、[赌徒破产问题](roots/gamblers-ruin.md)、[凯利公式](roots/kelly-criterion.md)、[分散投资](roots/diversification-finance.md)；第 2 轮新增 [小赌注组合](roots/portfolio-of-small-bets.md)、[机会成本](roots/opportunity-cost.md)
- 矛盾：张一鸣那条转述者认为“落袋为安也是选项”，和棉花糖实验对着干；后来的复现研究（Watts 2018）支持他：延迟满足划不划算，要看未来回报是否可靠。
- 第 2 轮的新线索：Marc Lou 和 OPC 两条是个人版本：AI 把每次尝试的成本压低后，同时押很多小赌注、靠多条收入线兜底，比押一个大项目更不容易出局。
- 没想清楚的问题：三旗理论的具体做法在配图里，没核对到。

### 原则 8：AI 在它擅长的事上拉平差距，在它不擅长、要判断好坏的地方，放大会判断的人

- 状态：已确认（2026-10-18，第 2 轮新增，说法按建议改过）
- 已加进全局规则：2026-10-18，`~/.claude/CLAUDE.md` 第 5 节「标出要人判断的地方」
- 支撑的新知识：[会写代码才玩得好 vibe coding](clips/2026-10-18-aryanlabde-vibe-coding-needs-coding-skill.md)、[Agent 智能体是模型能力的放大器](clips/2026-10-18-waytoagi-agent-model-capability-amplifier.md)、[Kimi-code重构一个月的架构复盘](clips/2026-10-18-real-kai42-kimi-code-rewrite-retrospective.md)、[吴恩达的智能体编程时代软件工程能力图](clips/2026-10-18-andrewyng-andrew-ng-ai-engineering-skills-map.md)、[Agent 循环工程晚宴讨论要点](clips/2026-10-18-jerryjliu0-agent-loop-engineering-dinner.md)、[哈萨比斯：懂 AI 的一个人胜过团队](clips/2026-10-18-anatolikopadze-hassabis-ai-person-outperforms-team.md)（共 6 条）
- 对应的源知识：[技术放大定律](roots/law-of-amplification.md)、[智力放大](roots/intelligence-amplification.md)、[吸收能力](roots/absorptive-capacity.md)、[自动化的反讽](roots/ironies-of-automation.md)、[人类监督控制](roots/sheridan-1992-human-supervisory-control.md)
- 和你已有原则的关系：对应你的“模型出草稿，人来定稿”：定稿的人得自己看得出好坏。
- 矛盾：这是这一轮最大的一处冲突。实验数据站在另一边：BCG 顾问实验（[在参差不齐的技术边界上航行（BCG 顾问实验）](roots/dellacqua-2023-jagged-technological-frontier.md)）和 GitHub Copilot 对照实验（[AI 对开发者生产率的影响：GitHub Copilot 对照实验](roots/peng-2023-copilot-developer-productivity.md)）都发现，原本水平低的人提升最多；[世界分成会用与不会用 ChatGPT](clips/2026-10-18-dotey-chatgpt-two-kinds-of-people.md) 也说 AI 先缩小新手和高手的差距。所以草稿原来的说法“工具放大的是判断力，自己判断不了好坏的产出用得越多越危险”只对了一半，确认时改成了现在这样：两边都对，只是适用的任务不同。BCG 实验里，超出 AI 能力边界的任务，用 AI 的人反而做得更差。
- 没想清楚的问题：哈萨比斯那句“懂 AI 的一个人胜过团队”查不到出处，最接近的证据只是“一个人用 AI 追平两人团队”。说法比证据强得多。

### 原则 9：红利和信息差都会被挤平：越早进越便宜，要按时间点重估

- 状态：已确认（2026-10-18，第 2 轮新增）
- 已加进全局规则：2026-10-18，`~/.claude/CLAUDE.md` 第 5 节「渠道打法看时间」
- 支撑的新知识：[TikTok头部机构创始人讲跨境价差生意](clips/2026-10-18-vincent-ainotes-tiktok-mcn-arbitrage-talk.md)、[出租屋卖亚马逊爆款配件月销二十万](clips/2026-10-18-vincent-ainotes-amazon-accessories-side-hustle.md)、[Reddit 是被低估的软件出海分发渠道](clips/2026-10-18-wanghao8080-reddit-distribution-channel.md)、[北美增长负责人谈各平台获客要点](clips/2026-10-18-oran-ge-na-growth-channel-notes.md)、[阿里国际站用590万AI页面冲SEO](clips/2026-10-18-willlhhh-alibaba-5-9m-ai-pages-seo.md)、[巴西青年靠 AI 工地女孩赚订阅费](clips/2026-10-18-bober-smart-ai-construction-girl-subscription.md)（共 6 条）
- 对应的源知识：[套利](roots/arbitrage.md)、[完全竞争](roots/perfect-competition.md)、[信息经济学（搜寻成本与价格离散）](roots/stigler-1961-economics-of-information.md)、[烂点击率定律（营销渠道衰减）](roots/law-of-shitty-clickthroughs.md)、[牛眼框架（《Traction》19 种获客渠道）](roots/bullseye-framework.md)、[古德哈特定律](roots/goodharts-law.md)、[蓝海战略](roots/blue-ocean-strategy.md)
- 和你已有原则的关系：和你的 GTM 主线直接相关。“烂点击率定律”说的是：任何获客渠道，用的人一多，点击率和回信率都会往下掉。冷邮件、表单营销应该也逃不掉（推断）。
- 矛盾：阿里那条显示，挤平不是对所有人同时发生：平台信号能被低成本批量制造时，优势越大的玩家在规则边缘停得越久（马太效应）。
- 没想清楚的问题：日本市场的获客渠道（展会、冷邮件、表单营销、合作伙伴）现在哪个还在红利期？要用你自己的回信数据按季度看，而不是照搬别人前几年的打法。

### 原则 10：转述每多一层就多走样一层：下结论前回到一手材料

- 状态：已确认（2026-10-18，第 2 轮新增）
- 支撑的新知识：[Jeff Dean 一小时讲 AI 系统](clips/2026-10-18-huxlab-jeff-dean-ai-course-hour.md)、[X推荐算法权重表：回复比点赞值钱](clips/2026-10-18-ityouknows-x-algorithm-weights-reply-vs-like.md)、[传闻：头部实验室已实现自我改进](clips/2026-10-18-maxforai-frontier-labs-rsi-claim.md)、[亿万富翁 42 分钟讲清全球经济运转](clips/2026-10-18-engmoelgaraihy-billionaire-global-economy-video.md)，以及这一轮核对时抓到走样的 [黄亚生预测中国模式走到尽头](clips/2026-10-18-bingliu34173809-huang-yasheng-china-model.md)、[Claude Code之父的三条心得](clips/2026-10-18-ayi-ainotes-boris-cherny-workflow-three-rules.md)、[哈萨比斯：懂 AI 的一个人胜过团队](clips/2026-10-18-anatolikopadze-hassabis-ai-person-outperforms-team.md)（共 7 条）
- 对应的源知识：[一手史料（原始资料）](roots/primary-source.md)、[传递链方法（传话实验）](roots/transmission-chain-method.md)、[信息处理不等式](roots/data-processing-inequality.md)
- 和你已有原则的关系：就是你全局规则里的“不编造：每个数字要能指回出处”，也是这个仓库本身的做法。这一轮核对一手材料时，151 条里查出十几处转述和原文对不上（见「三、待查 · 顺手查出来的误传」）。
- 矛盾：一手材料不自动更可信，当事人讲自己的东西也有立场。黄仁勋那条（[黄仁勋首发：开放模型为何重要](clips/2026-10-18-jensenhuang-jensen-open-models-letter.md)）就是例子：要同时看论证和说话人的利益。
- 没想清楚的问题：给客户的提案和邮件里引用的数字（比如“一小时内联系线索，谈上决策人的可能性高 7 倍”），有多少是二手转述？这一轮查到这组数字就常被混着引用（见误传）。

### 原则 11：上下文是稀缺资源：常驻只放索引，细节按需加载，子任务各带干净的上下文

- 状态：已确认（2026-10-18，第 2 轮新增）
- 支撑的新知识：[上下文工程：智能体的核心实践指南](clips/2026-10-18-shao-meng-context-engineering-guide.md)、[Agent Skills 是上下文卸载](clips/2026-10-18-yonah-x-skills-context-offloading.md)、[Manus 把工具分成三层的设计](clips/2026-10-18-dotey-manus-three-layer-tools.md)、[ADK 开发者该懂的五种 Agent Skill 设计模式](clips/2026-10-18-googlecloudtech-adk-agent-skill-design-patterns.md)、[Agent Skills设计哲学与迭代](clips/2026-10-18-dotey-agent-skills-design-philosophy.md)、[Claude Code 的 Task 工具原理](clips/2026-10-18-dotey-claude-code-task-subagent.md)、[用个人AI编排者带动一支永不睡觉的开发队](clips/2026-10-18-ayi-ainotes-personal-ai-orchestrator-openclaw.md)（共 7 条）
- 对应的源知识：[AI 智能体的上下文工程](roots/anthropic-2025-effective-context-engineering.md)、[上下文工程](roots/context-engineering.md)、[用 Agent Skills 让智能体胜任真实工作](roots/anthropic-2025-agent-skills.md)、[渐进式披露](roots/progressive-disclosure.md)、[Unix 哲学](roots/unix-philosophy.md)、[虚拟内存](roots/virtual-memory.md)
- 和你已有原则的关系：你做 skill 的规矩“主文件要小，细节拆出去按需加载”就是这一条。根是 1985 年苹果界面设计里的渐进式披露，和操作系统的虚拟内存（常用的放内存，其余放磁盘，用到再调）。
- 矛盾：Cognition《别做多智能体》认为拆成子任务会丢上下文；所以只拆“只读、只交回结果”的子任务，要做决定的留在主线。
- 没想清楚的问题：这一条和原则 4 的“沉淀”是一回事吗？skill 既是给 agent 省上下文的办法，也是把现场经验存下来的办法。

## 二、知识底座

被新知识指向得最多的源理论。“直接”是新知识直接指向它；“连同间接”还算上了通过更上层源知识追到它的。排在最前面的，就是最近看到的这些新东西共同的根。由 `tools/rank_roots.py` 算出。

| 排名 | 源知识 | 被几条新知识指向（直接 / 连同间接） | 更底层的源头 |
|---|---|---|---|
| 1 | [反馈](roots/feedback.md) | 3 / 62 | 已到基础层 |
| 2 | [控制论](roots/cybernetics.md) | 4 / 59 | 已到基础层 |
| 3 | [自然选择](roots/natural-selection.md) | 0 / 42 | 已到基础层 |
| 4 | [比较优势](roots/comparative-advantage.md) | 0 / 35 | 已到基础层 |
| 5 | [有限理性](roots/bounded-rationality.md) | 0 / 34 | 已到基础层 |
| 6 | [经验曲线效应](roots/experience-curve-effect.md) | 2 / 31 | [学习曲线](roots/learning-curve.md) |
| 7 | [学习曲线](roots/learning-curve.md) | 0 / 31 | 已到基础层 |
| 8 | [分工](roots/division-of-labour.md) | 5 / 30 | [比较优势](roots/comparative-advantage.md) |
| 9 | [智能体](roots/intelligent-agent.md) | 4 / 28 | [反馈](roots/feedback.md) |
| 10 | [摩尔定律](roots/moores-law.md) | 1 / 28 | [经验曲线效应](roots/experience-curve-effect.md) |
| 11 | [苦涩的教训](roots/bitter-lesson.md) | 11 / 27 | [摩尔定律](roots/moores-law.md) |
| 12 | [构建高效的智能体](roots/anthropic-2024-building-effective-agents.md) | 14 / 23 | [智能体](roots/intelligent-agent.md)、[分工](roots/division-of-labour.md) |
| 13 | [完全竞争](roots/perfect-competition.md) | 3 / 23 | 已到基础层 |
| 14 | [控制理论](roots/control-theory.md) | 0 / 23 | [反馈](roots/feedback.md) |
| 15 | [正反馈](roots/positive-feedback.md) | 0 / 21 | [控制论](roots/cybernetics.md) |

和第 1 轮比：前 3 名还是反馈、控制论、自然选择这三个，反馈从 15 条涨到 62 条，升到第 1。新进前 15 的是有限理性、智能体、完全竞争；信息论、效果律、孔多塞陪审团定理掉出去了。

直接被指向最多的：构建高效的智能体（14）、苦涩的教训（11）、AI 智能体的上下文工程（7）、约束理论（7）、颠覆式创新（6）、待完成的任务（6）、精益创业（6）、SECI 知识转化模型（6）。苦涩的教训从 6 条涨到 11 条；约束理论从 2 条涨到 7 条。

## 三、待查

真正的新东西最可能藏在这里。

### 和经典理论对着干的

第 1 轮 9 处，第 2 轮新增 21 处，共 30 处。强的 8 处排在前面。

| 新知识 | 对着干的经典 | 强弱 |
|---|---|---|
| [陶哲轩谈 AI 与数学的演讲要点](clips/2026-10-18-dotey-terence-tao-ai-math-talk.md) | [通用人工智能的火花：GPT-4 早期实验](roots/bubeck-2023-sparks-agi.md) | 强 |
| [黄亚生预测中国模式走到尽头](clips/2026-10-18-bingliu34173809-huang-yasheng-china-model.md) | [中国模式（北京共识）](roots/china-model.md) | 强 |
| [Anthropic 设计负责人谈 AI 时代设计流程](clips/2026-10-18-dotey-anthropic-design-process-ai-era.md) | [双钻石设计流程](roots/double-diamond-design-process-model.md) | 强 |
| [杨立昆谈智能不等于控制欲](clips/2026-10-18-dotey-lecun-intelligence-not-domination.md) | [工具性趋同](roots/instrumental-convergence.md) | 强 |
| [唐杰谈缩放定律：不只是堆参数](clips/2026-10-18-jietang-scaling-law-beyond-parameters.md) | [神经语言模型的缩放定律](roots/kaplan-2020-scaling-laws.md) | 强 |
| [LeCun：下个万亿AI公司不靠LLM](clips/2026-10-18-phosphenq-lecun-lecture-beyond-llms.md) | [神经网络规模定律](roots/neural-scaling-law.md) | 强 |
| [Pi 作者：代码即真相，Bash 够用](clips/2026-10-18-dotey-pi-authors-code-bash-insights.md) | [检索增强生成（RAG）](roots/retrieval-augmented-generation.md) | 强 |
| [与Claude Code讨论艺术与约束](clips/2026-10-18-turingou-constraint-in-live-music-product.md) | [Cloudflare Code Mode：让模型写代码放进沙箱执行](roots/varda-2025-code-mode.md) | 强 |
| [Tripo Eden：先建地图再渲染](clips/2026-10-18-svpino-tripo-eden-world-model-map.md) | [苦涩的教训](roots/bitter-lesson.md) | 弱（待 Luke 确认） |
| [Tripo Eden：先建地图再渲染](clips/2026-10-18-svpino-tripo-eden-world-model-map.md) | [视频生成模型是世界模拟器（Sora 技术报告）](roots/brooks-2024-video-world-simulators.md) | 弱（待 Luke 确认） |
| [Kimi-code重构一个月的架构复盘](clips/2026-10-18-real-kai42-kimi-code-rewrite-retrospective.md) | [在参差不齐的技术边界上航行（BCG 顾问实验）](roots/dellacqua-2023-jagged-technological-frontier.md) | 弱（待 Luke 确认） |
| [Karpathy 的 YC 演讲：软件 3.0](clips/2026-10-18-op7418-karpathy-software-3-talk.md) | [论“自然语言编程”之愚蠢](roots/dijkstra-1979-natural-language-programming.md) | 弱（待 Luke 确认） |
| [用自然语言让 LLM 承担业务数据存储](clips/2026-10-18-jefferytatsuya-llm-natural-language-data-store.md) | [论“自然语言编程”之愚蠢](roots/dijkstra-1979-natural-language-programming.md) | 弱（待 Luke 确认） |
| [缠论简纲思维导图](clips/2026-10-18-dtdt666-chanlun-mind-map.md) | [有效市场假说](roots/efficient-market-hypothesis.md) | 弱（待 Luke 确认） |
| [Sora 加 Vision Pro 展望](clips/2026-10-18-indigox-sora-vision-pro-immersive.md) | [体验机](roots/experience-machine.md) | 弱（待 Luke 确认） |
| [工具站出海月入 3000 刀的一年踩坑记](clips/2026-10-18-gefei55-tool-site-overseas-lessons.md) | [免费增值](roots/freemium.md) | 弱（待 Luke 确认） |
| [Sam 谈我们创造的是工具还是生物](clips/2026-10-18-dotey-altman-tool-or-creature.md) | [工具性趋同](roots/instrumental-convergence.md) | 弱（待 Luke 确认） |
| [Agent 循环工程晚宴讨论要点](clips/2026-10-18-jerryjliu0-agent-loop-engineering-dinner.md) | [自动化的反讽](roots/ironies-of-automation.md) | 弱（待 Luke 确认） |
| [备忘录加 worktree 就够了](clips/2026-10-18-hilng77042-opc-agents-notes-worktrees.md) | [看板方法（软件开发）](roots/kanban-development.md) | 弱（待 Luke 确认） |
| [Samuel 的跳棋程序：机器靠自己对弈学习，下得比写它的人还好](clips/2026-10-18-samuel-machine-learning-checkers.md) | [洛夫莱斯夫人的异议（机器不能原创）](roots/lady-lovelaces-objection.md) | 弱（待 Luke 确认） |
| [日语学习的素读法与家庭使用整理](clips/2026-10-18-interjc-sodoku-japanese-learning.md) | [产出效应（出声读出来的词记得更牢）](roots/macleod-2010-production-effect.md) | 弱（待 Luke 确认） |
| [ChatGPTMac版提示词触发共享屏幕](clips/2026-10-18-dotey-chatgpt-mac-screen-share-prompt.md) | [提示科学报告 3：威胁或给小费对大模型有没有用](roots/meincke-2025-threaten-or-tip.md) | 弱（待 Luke 确认） |
| [买两台 DGX 出租视频算力的生意](clips/2026-10-18-boxmrchen-dgx-video-compute-rental.md) | [摩尔定律](roots/moores-law.md) | 弱（待 Luke 确认） |
| [会写代码才玩得好 vibe coding](clips/2026-10-18-aryanlabde-vibe-coding-needs-coding-skill.md) | [AI 对开发者生产率的影响：GitHub Copilot 对照实验](roots/peng-2023-copilot-developer-productivity.md) | 弱（待 Luke 确认） |
| [买两台 DGX 出租视频算力的生意](clips/2026-10-18-boxmrchen-dgx-video-compute-rental.md) | [完全竞争](roots/perfect-competition.md) | 弱（待 Luke 确认） |
| [WorkBuddy 播客：编程不再稀缺](clips/2026-10-18-ayi-ainotes-workbuddy-podcast-ai-era-skills.md) | [理解语言模型的谄媚（迎合用户）](roots/sharma-2023-sycophancy-language-models.md) | 弱（待 Luke 确认） |
| [世界分成会用与不会用 ChatGPT](clips/2026-10-18-dotey-chatgpt-two-kinds-of-people.md) | [技能偏向型技术变革](roots/skill-biased-technological-change.md) | 弱（待 Luke 确认） |
| [张一鸣 66 条成长心得与延迟满足](clips/2026-10-18-sea-bitcoin-zhang-yiming-66-growth-tips.md) | [斯坦福棉花糖实验](roots/stanford-marshmallow-experiment.md) | 弱（待 Luke 确认） |
| [Claude Code 的 Task 工具原理](clips/2026-10-18-dotey-claude-code-task-subagent.md) | [别做多智能体](roots/yan-2025-dont-build-multi-agents.md) | 弱（待 Luke 确认） |
| [Karpathy：让AI模拟专家来答](clips/2026-10-18-dotey-karpathy-simulator-not-entity.md) | [系统提示里的角色不能提升表现](roots/zheng-2023-personas-system-prompts.md) | 弱（待 Luke 确认） |

几组值得对照着看：
- **规模还是结构**：杨立昆、Tripo Eden 认为光靠规模不够，要有新的结构或显式保存的状态；唐杰、Sora 团队押规模继续有效，能力会自己冒出来。
- **AI 放大高手还是拉平差距**：kimi-code、vibe coding 两条说只放大高手，BCG 和 Copilot 的实验说新手受益最多。已写成原则 8（已确认）。
- **流程还要不要**：Anthropic 设计负责人说双钻石流程“基本已死”，worktree 那条说连看板都不需要了。两条都是执行变快之后，围绕新瓶颈重组流程。

### 没找到源头的

- [李自然讲独立开发出海营销增长方法](clips/2026-10-18-yihui-indie-indie-marketing-growth-talk.md)：原文只推荐了一期播客，没写方法本身。要 Luke 贴内容
- [人大附中讲座：培养怎样的孩子](clips/2026-10-18-lubtc888-ai-era-raising-children-lecture.md)：原文只有一句提问加一个视频链接，讲座文字材料搜不到。要 Luke 贴内容

### 出处还没核实的

- [“大模型是冰箱，可口可乐还没出现”比喻](roots/palihapitiya-refrigeration-coca-cola-analogy.md)：只找到二手转述，两篇转述给的时间对不上
- [为 AGI 而压缩](roots/rae-2023-compression-for-agi.md)：讲座原视频没找到，只有二手整理
- [“计算机不能被问责，所以不能做管理决策”（IBM 1979 培训资料）](roots/ibm-1979-computer-accountable.md)：原件据说毁于水灾，IBM 档案馆也没找到

### 顺手查出来的误传

第 1 轮：
- Samuel 的跳棋程序“超越了写它的人”，是 Wiener 1960 年的解读；Samuel 本人同年撰文不同意（见 [Samuel 的跳棋程序：机器靠自己对弈学习，下得比写它的人还好](clips/2026-10-18-samuel-machine-learning-checkers.md)）
- “ikigai 四圈图”不是日本原创，是 Marc Winn 2014 年改自西班牙人 Zuzunaga 的图；日本原本的生き甲斐不要求能赚钱（见 [世界需要、擅长、热爱、能谋生的交集](clips/2026-10-18-zutaomin-ikigai-meaning-of-life.md)）
- 情境领导里的 S1～S4 是领导风格，员工的成熟度是 R1～R4 / D1～D4，宝玉那条把两者混了（见 [情境领导模型 S1 到 S4 会动态变化](clips/2026-10-18-dotey-situational-leadership-model.md)）
- “枢密院高级国务大臣”不是明朝官名，徐光启实际是礼部尚书、文渊阁大学士（见 [南明皇室受洗的冷知识：借调侃“历史老师去美国”说出来](clips/2026-10-18-tombkeeper-southern-ming-baptism.md)）
- 奥卡姆剃刀那句名言不见于奥卡姆本人的著作

第 2 轮：
- 黄亚生那篇文章 2012 年就发表了，推文写的 2016 年是转载时间；推文里卢比、土地私有那几段原文里没有，是转述者加的（见 [黄亚生预测中国模式走到尽头](clips/2026-10-18-bingliu34173809-huang-yasheng-china-model.md)）
- Boris Cherny 三条心得的转述有四处和原串推对不上：原文是 Opus 4.5 不是 4.6；理由是“要纠偏的少，总体更快”，不是“省 token”；文件是放进 git 的 CLAUDE.md，不是 txt；“画家蒙眼作画”的比喻原串推里没有（见 [Claude Code之父的三条心得](clips/2026-10-18-ayi-ainotes-boris-cherny-workflow-three-rules.md)）
- 宝玉那条说 Claude Code“没有上下文压缩”，但官方更新记录在研究预览期的 0.2.47 版就有“自动压缩对话”（见 [Claude Code 的 Task 工具原理](clips/2026-10-18-dotey-claude-code-task-subagent.md)）
- “懂 AI 的一个人胜过团队”查不到哈萨比斯说过；最接近的宝洁实验只是“一个人用 AI 追平两人团队”（见 [哈萨比斯：懂 AI 的一个人胜过团队](clips/2026-10-18-anatolikopadze-hassabis-ai-person-outperforms-team.md)）
- 小米 MiMo 那条说的“MixRL”报告里没有这个词，报告叫混合任务强化学习；“7K 个环境”报告里是约 7 千个任务（见 [MiMo-V2.6 的强化学习之路](clips/2026-10-18-luofuli-mimo-v2-6-scaling-rl.md)）
- “日本纬度和东北相似”不准：日本国土中心约北纬 36°，辽宁约北纬 41°；高知平原历史上种过水稻二期作（见 [日本稻田能否收二茬的回复](clips/2026-10-18-wangtianlaw-japan-rice-ratoon-crop.md)）
- “卖铲子比淘金稳”常被说成马克·吐温的话，查无实据，这种归属 1982 年才出现（见 [卖铲子策略（淘金热里卖工具）](roots/picks-and-shovels.md)）
- “交易成本”这个词不是科斯造的，他 1937 年说的是“使用价格机制的成本”（见 [交易成本](roots/transaction-cost.md)）
- “选择太多反而不买”（选择过载）没有想象中普遍：2010 年合并 50 个实验的元分析，平均效应几乎为零（见 [选择过载](roots/overchoice.md)）
- “需求错误晚修贵 100 倍”出处不清，Boehm 本人后来说小型非关键系统更接近 5 倍（见 [《软件工程经济学》（错误越晚修越贵）](roots/boehm-1981-software-engineering-economics.md)）
- “一小时内联系线索，谈上决策人的可能性高 7 倍”和“5 分钟内联系高 21 倍”出自 Oldroyd 的两项不同研究，常被混在一起引用（见 [线上销售线索的短命（线索响应速度研究）](roots/oldroyd-2011-short-life-online-sales-leads.md)）
- 最小因子定律常归给李比希，但 Sprengel 1828 年已提出，李比希是推广者（见 [最小因子定律（短板定律）](roots/liebigs-law-of-the-minimum.md)）
- 蔡格尼克效应（没做完的事记得更牢）复现不稳，2025 年的元分析只支持“想把中断的事做完”的倾向（见 [蔡格尼克效应](roots/zeigarnik-effect.md)）
- 霍尔的“高语境、低语境文化”常被说成出自 1976 年的书，其实 1959 年就有；霍尔本人也说日本文化里两种场合都有（见 [高语境文化与低语境文化](roots/high-context-and-low-context-cultures.md)）

## 四、主题地图

全部新知识按主题和发布年份分布，看关注点这几年怎么变。由 `tools/topic_map.py` 生成。

<!-- topic-map:begin -->
共 1734 条新知识（含已归档）。数字是每年存下的条数；按发布年份算，不是保存日期。

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
| 未分类 |  |  |  |  | 1 |  | 1 | 0 / 0 / 0 |

**每个主题的代表**（先选已溯源的，再选观点类，最后按发布时间取最新）

- **Agent 与 Skill**：[AlphaCodium 与流程工程](clips/2026-10-18-dotey-alphacodium-flow-engineering.md)、[Agent 智能体是模型能力的放大器](clips/2026-10-18-waytoagi-agent-model-capability-amplifier.md)、[ChatGPTMac版提示词触发共享屏幕](clips/2026-10-18-dotey-chatgpt-mac-screen-share-prompt.md)
- **其他**：[黄亚生预测中国模式走到尽头](clips/2026-10-18-bingliu34173809-huang-yasheng-china-model.md)、[缠论简纲思维导图](clips/2026-10-18-dtdt666-chanlun-mind-map.md)、[三旗理论：合法减税、保护资产、自由生活](clips/2026-10-18-eric-make-money-three-flags-theory.md)
- **AI 产品与创业**：[学超级个体 Jack Butcher](clips/2026-10-18-starzq-jack-butcher-solo-brand.md)、[用 PHP 套现 5400 万美元](clips/2026-10-18-imwsl90-php-jquery-54m-dollars.md)、[开 100 家便利店经验写成选址指南](clips/2026-10-18-hitw93-convenience-store-site-selection.md)
- **视频生成**：[Sora 团队伯克利课堂分享字幕翻译](clips/2026-10-18-dotey-sora-team-berkeley-talk.md)、[Tripo Eden：先建地图再渲染](clips/2026-10-18-svpino-tripo-eden-world-model-map.md)、[别再说 AI 电影，这就是电影](clips/2026-10-18-ehuanglu-ai-film-is-just-film.md)
- **编程智能体**：[AI 辅助编程带来的需求开发范式变化](clips/2026-10-18-dotey-ai-coding-requirements-shift.md)、[公司推广 AI 编程为何要靠内部](clips/2026-10-18-dotey-promote-ai-coding-in-company.md)、[AI 编程像人一样拆解任务的神仙项目](clips/2026-10-18-yangyi-task-breakdown-agent-project.md)
- **模型与本地部署**：[Karpathy 谈 GPT 现状](clips/2026-10-18-dotey-karpathy-state-of-gpt.md)、[合成数据与苦涩的教训讨论](clips/2026-10-18-dotey-synthetic-data-bitter-lesson.md)、[DeepSeek R1 论文解读：自学成才之路](clips/2026-10-18-oran-ge-deepseek-r1-paper-explained.md)
- **设计与前端**：[设计师口袋心理学 53 个知识卡片](clips/2026-10-18-hitw93-designer-pocket-psychology.md)、[Anthropic 设计负责人谈 AI 时代设计流程](clips/2026-10-18-dotey-anthropic-design-process-ai-era.md)、[学 Vercel 设计系统的逻辑](clips/2026-10-18-mengkepm-vercel-design-system-learn-logic.md)
- **图像生成**：[Qwen 生图 Turbo 开放权重](clips/2026-10-18-qwendevs-qwen-image-turbo-open-weights.md)、[Qwen 换脸换头 LoRA 更新](clips/2026-10-18-lonely-mh-qwen-image-face-swap-lora.md)、[Qwen-Image 2.1 即将开源](clips/2026-10-18-qwendevs-qwen-image-2-1-early-access.md)
- **提示词与写作**：[Anthropic专家谈提示词工程师](clips/2026-10-18-eze-is-1-anthropic-prompt-engineering-notes.md)、[提示词精髓：有什么、做什么、怎么做](clips/2026-10-18-dotey-prompt-context-task-how.md)、[写提示词的三条路与第四条路：故事](clips/2026-10-18-lijigang-prompt-writing-fourth-path-story.md)
- **语音与数字人**：[Fish 开源 Drama3 语音模型](clips/2026-10-18-kay2289123-fish-audio-drama3-open-source.md)、[Griffin 全双工视频模型解读](clips/2026-10-18-maxforai-griffin-full-duplex-video-model.md)、[Griffin 通过视频图灵测试](clips/2026-10-18-tavus-tavus-griffin-video-turing-test.md)
- **学习与研究**：[Samuel 的跳棋程序：机器靠自己对弈学习，下得比写它的人还好](clips/2026-10-18-samuel-machine-learning-checkers.md)、[AIDE：让用户给样本打"相关/不相关"，用主动学习猜出他真正想查的数据](clips/2026-10-18-dimitriadou-aide-active-learning-data-exploration.md)、[吴恩达对话李飞飞谈以人为本的 AI](clips/2026-10-18-dotey-andrew-ng-fei-fei-li-interview.md)
- **增长与获客**：[MrBeast的YouTube上瘾蓝图](clips/2026-10-18-0xcheshire-youtube-addiction-blueprint.md)、[Reddit 是被低估的软件出海分发渠道](clips/2026-10-18-wanghao8080-reddit-distribution-channel.md)、[北美增长负责人谈各平台获客要点](clips/2026-10-18-oran-ge-na-growth-channel-notes.md)
- **思维与成长**：[张一鸣 66 条成长心得与延迟满足](clips/2026-10-18-sea-bitcoin-zhang-yiming-66-growth-tips.md)、[Paul Graham 谈超线性回报](clips/2026-10-18-dotey-paul-graham-superlinear-returns.md)、[一句话总结 AI 算法的含义](clips/2026-10-18-dotey-ai-algorithm-one-liner.md)
- **日本**：[大阪府各区划与公立小学教育概况](clips/2026-10-18-qiancaobuzhiqiu-osaka-areas-public-schools.md)、[日语学习的素读法与家庭使用整理](clips/2026-10-18-interjc-sodoku-japanese-learning.md)、[GA决算说明资料的结构化设计](clips/2026-10-18-powerpoint-jp-ga-technologies-earnings-deck-design.md)
- **历史与冷知识**：[日本稻田能否收二茬的回复](clips/2026-10-18-wangtianlaw-japan-rice-ratoon-crop.md)、[南明皇室受洗的冷知识：借调侃“历史老师去美国”说出来](clips/2026-10-18-tombkeeper-southern-ming-baptism.md)、[美国人一天生活的数据可视化](clips/2026-10-18-alexxubyte-day-in-life-americans-dataviz.md)
- **未分类**：[Terminal-RSI：命令行 agent 拿自己验证过的成功经验反复训练自己，一轮比一轮强](clips/2026-10-18-yang-terminal-rsi-recursive-self-improving-agents.md)
<!-- topic-map:end -->
