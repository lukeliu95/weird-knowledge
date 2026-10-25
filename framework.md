# 我的思考框架

> 最近一次整理：2026-10-24（第 6 轮）· 新知识 1873 条（已溯源 302、待溯源 0、已归档 1571），另有补课找来、还没认可的 36 条 · 源知识 947 个
> 规则见 [AGENTS.md](AGENTS.md)。标"草稿"的是模型提炼的，Luke 确认后才改成"已确认"。本轮记录：[docs/reviews/2026-10-24-round-6.md](docs/reviews/2026-10-24-round-6.md)

## 一、我的原则

第 1 轮从 65 条里提炼出 7 条。第 2 轮又溯源了 151 条：7 条都补上了新证据，另外新增 4 条（原则 8～11）。2026-10-18 Luke 全部确认，其中原则 2、6、8 按建议改了说法。第 3 轮溯源了 7 条：原则 1、2、5、7、8、10、11 补了新证据，另外新增 1 条（原则 12），Luke 当天确认。第 4 轮溯源了 25 条：原则 1、2、3、4、6、7、8、10、11、12 补了新证据，另外新增 1 条（原则 13），Luke 当天确认。第 6 轮溯源了 21 条：原则 1、2、4、6、10、11、12、13 补了新证据，没有新增原则。第 7 轮溯源了 1 条：原则 7、10 补了新证据。

### 原则 1：质量靠闭环：回路越短、越能自动判对错，进步越快

- 状态：已确认（2026-10-18）
- 支撑的新知识：[吴恩达讲做产品的三个循环](clips/2026-10-18-andrewyng-andrew-ng-three-product-loops.md)、[AlphaCodium 与流程工程](clips/2026-10-18-dotey-alphacodium-flow-engineering.md)、[外层harness让智能体连跑数小时](clips/2026-10-18-baoweiheihei-harness-unattended-long-running.md)、[Monolith论文：实时推荐致瘾](clips/2026-10-18-interjc-tiktok-monolith-realtime-recsys.md)、[陶哲轩谈 AI 与数学的演讲要点](clips/2026-10-18-dotey-terence-tao-ai-math-talk.md)、[Samuel 的跳棋程序：机器靠自己对弈学习，下得比写它的人还好](clips/2026-10-18-samuel-machine-learning-checkers.md)、[DeepSeek R1 论文解读：自学成才之路](clips/2026-10-18-oran-ge-deepseek-r1-paper-explained.md)、[开源模型自我验证跑赢闭源模型](clips/2026-10-18-jackyk02-self-verification-open-model-beats-closed.md)
- 第 2 轮新增：[Anthropic：让模型验证自己的输出](clips/2026-10-18-0xcodez-anthropic-agent-loop-self-verify.md)、[吴恩达：自我改进循环将取代提示](clips/2026-10-18-0xmovez-andrew-ng-self-improving-loops.md)、[智谱让 GLM-5.3 自己优化推理系统](clips/2026-10-18-dotey-glm-5-3-optimizes-own-inference.md)、[Astra 电脑操作让验收成闭环](clips/2026-10-18-dotey-astra-computer-use-acceptance-loop.md)、[Claude Code之父的三条心得](clips/2026-10-18-ayi-ainotes-boris-cherny-workflow-three-rules.md)、[自然语言 Agent 应像好员工的七点](clips/2026-10-18-remixdesigner-agent-as-good-employee.md)、[Anthropic专家谈提示词工程师](clips/2026-10-18-eze-is-1-anthropic-prompt-engineering-notes.md)、[开 100 家便利店经验写成选址指南](clips/2026-10-18-hitw93-convenience-store-site-selection.md)（共 16 条）
- 第 5 轮新增：[模拟客户从不走开](clips/2026-10-21-chen-simulated-customers-never-walk-away.md)：只有拿真实结果（付款）对照，才看得出模拟客户在"不会买的人"那里系统性地偏；回路要闭在真实结果上，闭在模拟器上会越练越偏
- 对应的源知识：[控制论](roots/cybernetics.md)、[反馈](roots/feedback.md)、[效果律](roots/law-of-effect.md)、[测试驱动开发](roots/test-driven-development.md)；第 2 轮新增 [验收测试](roots/acceptance-testing.md)、[PDCA 循环（计划-执行-检查-处置）](roots/pdca.md)、[复合工程](roots/compounding-engineering.md)、[奖励塑形（势函数塑形下的策略不变性）](roots/ng-1999-reward-shaping.md)
- 第 3 轮新增：[Terminal-RSI：命令行 agent 拿自己验证过的成功经验反复训练自己，一轮比一轮强](clips/2026-10-18-yang-terminal-rsi-recursive-self-improving-agents.md)、[yetone 用 3 个 /loop 循环让 Claude Code 自己维护 Magpie](clips/2026-10-18-dotey-yetone-magpie-three-loops-workflow.md)（共 18 条）；新源知识 [ReST：强化自训练](roots/gulcehre-2023-rest.md)、[ReST-EM](roots/singh-2023-rest-em.md)、[行动后复盘](roots/after-action-review.md)
- 第 3 轮的新线索：Terminal-RSI 说明“自己练自己”能跑起来，前提是每一轮都有外部的自动检查把关，只留验证通过的记录；没有这一层，就会滑向模型崩溃。yetone 那条是同一件事的工程版：先搭好三端真实复现环境，“修好了”要靠实际跑一遍来判，教训写下来留给下一轮。
- 和你已有原则的关系：就是你全局规则里的“生成、评估、改进”，这次找到了理论根：控制论里的负反馈。
- 矛盾：只对能自动判对错的任务（代码、数学、推荐点击）最灵；品味、长期战略这类判断，陶哲轩也强调“人得懂行才能把关”。
- 第 2 轮的新线索：智谱那条给了缩短回路的具体办法：结果信号太稀疏（只知道最后成没成）时，把它拆成一层层便宜、能马上验证的过程信号。Boris Cherny 那条补了另一半：每次纠正都写进 CLAUDE.md，回路才会越转越好，而不是每次从头来。
- 第 4 轮新增：[Harness²：agent 不改模型，靠对照试验改自己的运行框架，还学会怎么改得更好](clips/2026-10-19-xu-harness2-recursive-agent-harnessing.md)、[模型不动，只让技能库从用户请求里长：设计 agent 的技能从 76 个长到 139 个](clips/2026-10-20-du-designer-rsi-procedural-memory.md)、[Meta 的 MIMESIS：用真人行为训练的用户模拟器，比让助手模型扮用户更好练 agent](clips/2026-10-20-dair-ai-mimesis-user-simulator.md)、[用户模拟器会是 agent 强化学习里被低估的一环：真考法是预测一个人的留出选择](clips/2026-10-20-genai-is-real-user-simulation-agentic-rl.md)（共 22 条）；新源知识 [Meta-Harness：端到端优化模型的运行框架](roots/lee-2026-meta-harness.md)、[带基线自举的安全策略改进（SPIBB）](roots/laroche-2019-spibb.md)、[τ-bench：工具、agent、用户三方交互的基准](roots/yao-2024-tau-bench.md)、[翻转对话：训练和评测用户语言模型](roots/naous-2025-user-language-models.md)
- 第 4 轮的新线索：两点。一是检查这一步要保守：Harness² 只合入在同样条件下试跑赢了的改动，Designer-RSI 要求“一个用例不输、至少赢一个”才留下，本项目流程五“比冠军好的概率到 80% 才采用”是同一类门。二是检查器本身会骗人：MIMESIS 实测，同一个 agent 对真人成功率 63.6%，换成大模型扮用户就升到 82%～84%；拿太配合的模拟用户练，闭环转得越快越走偏。检验“像不像某个人”，要看能不能预测他没答过的选择，并知道自己证据够不够（Park 2024，也是本项目 80% 门槛的出处）。
- 第 6 轮新增：[HarnessPro](clips/2026-10-24-qbitai-harnesspro-pareto-rsi.md)：没有标准答案时，大模型当裁判只抓到 41.7% 的失败案例，换成按任务写的可执行测试升到 83.3%，再按分数和成本两个目标留候选；[Harness² 解读](clips/2026-10-22-xudong-harness-squared-self-evolution.md)、[Evo² 解读](clips/2026-10-22-xudong-evo2-weight-harness-co-evolution.md)、[Imbue 的 Darwinian Evolver](clips/2026-10-22-imbue-llm-evolution-universal-optimizer.md)都是“改一点、同条件对照、赢了才留”。新线索：把关的检查最好是能执行的测试，不是另一个模型的印象
- 没想清楚的问题：获客这种反馈慢、难归因的事怎么缩短回路？按智谱的思路，可以把“签单”拆成“打开、回信、约到会”这几层过程信号分别优化（推断，待 Luke 确认）。复旦那条“看能说明因果的指标，不看虚荣指标”（[复旦分享：脑科学视角拆品牌营销](clips/2026-10-18-yangyi-fudan-brand-marketing-neuroscience.md)）提醒：拆出来的过程信号要真的能预测结果。

### 原则 2：能力还在快速变强时，给目标、工具和边界，不写死步骤；脚手架按需加、定期删；要长期保持一致、出错代价大的部分照样写死

- 状态：已确认（2026-10-18，说法按建议改过）
- 支撑的新知识：[什么才是 AI Native：别写死步骤](clips/2026-10-18-programerjohann-ai-native-agent-four-things.md)、[Claude Code之父：配置越少越好](clips/2026-10-18-xiaohu-claude-code-minimal-claude-md.md)、[Claude Code播客：工具终将消失](clips/2026-10-18-genie0309-claude-code-podcast-tools-disappear.md)、[合成数据与苦涩的教训讨论](clips/2026-10-18-dotey-synthetic-data-bitter-lesson.md)、[Agent 基础设施的一线观察](clips/2026-10-18-dotey-anthropic-agent-infrastructure-talk.md)
- 第 2 轮新增：[谈用 Claude 做智能体：少搭脚手架](clips/2026-10-18-alexalbert-agent-scaffolding-context-talk.md)、[提示词精髓：有什么、做什么、怎么做](clips/2026-10-18-dotey-prompt-context-task-how.md)、[Sora 团队伯克利课堂分享字幕翻译](clips/2026-10-18-dotey-sora-team-berkeley-talk.md)（共 8 条）
- 对应的源知识：[苦涩的教训](roots/bitter-lesson.md)、[摩尔定律](roots/moores-law.md)；第 2 轮新增 [归纳偏置](roots/inductive-bias.md)、[OpenAI 推理模型提示建议（提示要简单直接、不必写思维链）](roots/openai-2024-o1-prompting-advice.md)、[任务式指挥](roots/mission-type-tactics.md)
- 第 3 轮新增：[OpenAI Dots 放权指南：动作分进 6 个权限区，每周按证据升降](clips/2026-10-18-choopyplug1-openai-dots-agent-permission-zones.md)（共 9 条）；新源知识 [失效安全默认（默认拒绝）](roots/fail-safe-defaults.md)
- 第 3 轮的新线索：Dots 那条给“出错代价大的部分照样写死”补了做法：碰钱、凭证、永久删除的动作一律交回人；规则要“像律师一样写”，写清对谁、做什么、到哪天为止；没写到的一律退回“先问”。
- 和你已有原则的关系：对应你的“该交给模型的交给模型”，以及“确定的事用确定的代码”；根在 Sutton 的苦涩的教训。第 2 轮找到一个军事上的老版本：任务式指挥（只下达意图和目标，不规定怎么打）。
- 矛盾：
  - “Agent 和工作流的区别”那条提醒：能用确定路径解决的，还是用工作流。两者的分界是“这一步需不需要判断”。第 2 轮的 [给公司业务接入智能体的五点思考](clips/2026-10-18-dotey-enterprise-agent-integration-tips.md) 和 [大白话讲清 Agent、工作流与 ReACT](clips/2026-10-18-yangyi-agent-workflow-react-explained.md) 说法一样：新问题先让模型探索，跑通了再固化成规则。
  - [Tripo Eden：先建地图再渲染](clips/2026-10-18-svpino-tripo-eden-world-model-map.md) 和 Sora 那条正好对着干：Sora 团队押“规模够了，物体不消失这种能力自己会冒出来”，Tripo 押“要长期一致的东西，必须显式存一份状态”。
- 第 4 轮新增：[Meta 的瘦编排器模式：编排器只管路由和检查，不做领域推理，14 个专项子 agent 各管一块](clips/2026-10-20-meta-thin-orchestrator-agent-architecture.md)、[agent 每步的选择题交给小决策模型（UIUC 等，推文误作普林斯顿和谷歌），模拟网店里 4B 模型完成率 91.5%](clips/2026-10-20-rohanpaul-ai-agent-decision-model-small-beats-big.md)（共 11 条）
- 第 4 轮的新线索：两条都把“写死”和“交给模型”的分界画清楚了。Meta 的编排器只做确定性的路由、收集字段和检查，不做任何领域推理，领域判断交给各管一块的子 agent。小决策模型那篇是另一种切法：每一步的选择题先交给小模型，拿不准（低于在自己运行记录上拟合的门槛）再交给大模型。
- 第 6 轮新增：[OpenAI FDE 实战](clips/2026-10-24-xudong07452910-xudong-openai-fde-codex-deleted-custom-code.md)：Codex 变强后，前线部署团队删掉了九成给客户写的定制代码，留下来的是评测、失败案例和写成 skill 的业务知识。这是“脚手架定期删”在企业落地上的例子
- 没想清楚的问题：底层能力什么时候算“不再快速变强”？那时该反过来多写结构。Tripo 那条给了一个判断口：需要长期保持一致、出错代价大的部分，先写死。

### 原则 3：一种能力变得人人可得，价值就转到和它互补、仍然稀缺的东西上

- 状态：已确认（2026-10-18）
- 已加进全局规则：2026-10-18，`~/.claude/CLAUDE.md` 第 5 节「先问什么变便宜了」
- 支撑的新知识：[智力平权之后，行动力成最大差异](clips/2026-10-18-oran-ge-agency-after-intelligence-equality.md)、[DeepResearch小众话题更有价值](clips/2026-10-18-dotey-deep-research-knowledge-value.md)、[大模型是冰箱，赚钱的是卖冷饮的人](clips/2026-10-18-mubeitech-llm-fridge-coca-cola-analogy.md)、[AI 是独立产品还是平台功能](clips/2026-10-18-dotey-ai-product-or-feature.md)、[Thiel一小时讲透从零做垄断的底层逻辑](clips/2026-10-18-kkawsb-peter-thiel-monopoly-lecture.md)
- 第 2 轮新增：[AI 时代最值钱的是懂 AI 的产品经理](clips/2026-10-18-dotey-ai-product-manager-skills.md)、[稀缺从怎么做转向做什么](clips/2026-10-18-lijigang-scarcity-how-to-what.md)、[品味可以被模仿，决策才不可替代](clips/2026-10-18-mengkepm-taste-copyable-decision-irreplaceable.md)、[AIGC 作品的关键是加上人味](clips/2026-10-18-jesselaunz-aigc-add-human-touch.md)、[NVIDIA DGX Spark 从买机器到变现指南](clips/2026-10-18-ai-goge-dgx-spark-monetization-guide.md)、[Gumloop四人团队冲击十亿公司](clips/2026-10-18-wanghao8080-gumloop-small-team-unicorn.md)、[对接 SD 做细分领域插画生成器](clips/2026-10-18-yangyi-niche-illustration-generator.md)、[写好Spec后让Agent整周自动开发](clips/2026-10-18-timyangnet-spec-driven-agent-development.md)、[吴恩达的智能体编程时代软件工程能力图](clips/2026-10-18-andrewyng-andrew-ng-ai-engineering-skills-map.md)、[技术领导者要知道的生成式 AI 五个真相](clips/2026-10-18-dotey-five-hard-truths-genai.md)（共 15 条）
- 对应的源知识：[互补品](roots/complementary-good.md)、[商品化（同质化）](roots/commoditization.md)、[诱人利润守恒定律](roots/law-of-conservation-of-attractive-profits.md)、[完全竞争](roots/perfect-competition.md)；第 2 轮新增 [《预测机器：人工智能的简单经济学》](roots/agrawal-2018-prediction-machines.md)、[杰文斯悖论](roots/jevons-paradox.md)、[没有银弹（本质复杂度与偶然复杂度）](roots/no-silver-bullet.md)、[资源基础观](roots/resource-based-view.md)
- 矛盾：“冰箱和可口可乐”这个比喻本身没找到原始出处（待确认）；诱人利润守恒定律的 HBR 原文也没找到。
- 第 2 轮的新线索：这一轮的 10 条对“什么还稀缺”说法很一致：决定做什么（规格、取舍、判断）、分发、独有而干净的数据、离客户问题最近的那一层。布鲁克斯 1986 年《没有银弹》早就说过：最难的是精确决定要造什么。
- 第 4 轮新增：[日本 B2B 采购者：八成嫌官网都是一般论，57.1% 按“诚实”决定找谁询问](clips/2026-10-20-ideatech-btob-buyer-information-contact-survey.md)、[模型每周都在换：别把自己的上下文锁在一家产品里](clips/2026-10-20-brian-lovin-portable-context-switching.md)、[Personal Agent 像 2012 年的滴滴：是上游模型厂补贴下游的出口，要能自己后训练小模型降本](clips/2026-10-20-willwangtf-personal-agent-didi-2012.md)（共 18 条）；新源知识 [双面说服（正反两面信息）](roots/two-sided-persuasion.md)、[自愿披露与“沉默即坏消息”（信息解开）](roots/voluntary-disclosure-unraveling.md)、[滴滴与快的打车补贴大战](roots/didi-kuaidi-subsidy-war-2014.md)
- 第 4 轮的新线索：IDEATECH 的 105 人调查说，买方把一般信息交给生成式 AI，让他们决定找谁询问的，是肯公开缺点、风险、真实价格的诚实（厂商调查，卖的正是调查型内容营销）。这一块单独写成了原则 13。Brian Lovin 和 willwangtf 是同一件事的两面：模型被做成大路货（上游补贴 token 抢用户，像 2014 年腾讯、阿里补贴打车），握在自己手里的个人上下文、自己训的小模型才是资产。
- 没想清楚的问题：AI 让什么变便宜了，对 GBase 的客户来说，现在稀缺的是什么？

### 原则 4：说不清的知识只能去现场取，取回来要沉淀成可复用的东西

- 状态：已确认（2026-10-18）
- 已加进全局规则：2026-10-18，`~/.claude/CLAUDE.md` 第 5 节「需求去现场取」
- 支撑的新知识：[Anthropic 讲前线部署工程师](clips/2026-10-18-dotey-fde-101-forward-deployed-engineer.md)、[前线部署工程师为何是 AI 落地时代的关键职业](clips/2026-10-18-indigox-forward-deployed-engineer-ai-era.md)、[AIDE：让用户给样本打"相关/不相关"，用主动学习猜出他真正想查的数据](clips/2026-10-18-dimitriadou-aide-active-learning-data-exploration.md)、[帮家具厂建 AI 产品库月入一万八](clips/2026-10-18-miles-mazy-furniture-factory-ai-product-library.md)、[OpenAI 报告：用户最常用的是懒脑力活](clips/2026-10-18-frxiaobei-chatgpt-usage-lazy-moments.md)
- 第 2 轮新增：[范冰免费开源新书《前置部署工程师》](clips/2026-10-18-iluciddreaming-fde-book-free-open-source.md)、[国内 ToB 智能体至少还要一年](clips/2026-10-18-frxiaobei-tob-agent-one-year-away.md)、[同城 IP 团队的真实 Agent 需求](clips/2026-10-18-wanghao8080-local-ip-agent-need.md)、[Anthropic：用技能代替独立智能体](clips/2026-10-18-hongming731-anthropic-agent-skills-talk.md)、[征求产品意见别只问程序员群体](clips/2026-10-18-gorden-sun-dont-ask-programmers-product-feedback.md)、[做到千万美元ARR的B2B代理路径](clips/2026-10-18-financeyf5-b2b-ai-agent-10m-arr.md)、[Clay：给 ToB 销售补全客户数据](clips/2026-10-18-wanghao8080-clay-sales-data-enrichment.md)（共 12 条）
- 第 5 轮新增：[范冰《前线部署工程师》](clips/2026-10-21-fanbing-fde-guidance-book.md)：整本书讲"把工程师驻到客户现场"，影子工作法直接引用人类学参与式观察和丰田现地现物；第 7 章"砾石路与高速公路"正是"取回来要沉淀成可复用的东西"那一半。Luke 存它的原因是想借鉴在日本落地
- 对应的源知识：[默会知识（隐性知识）](roots/tacit-knowledge.md)、[粘滞信息](roots/sticky-information.md)、[《知识在社会中的运用》](roots/the-use-of-knowledge-in-society.md)、[SECI 知识转化模型](roots/seci-model-of-knowledge-dimensions.md)、[待完成的任务](roots/jobs-to-be-done.md)；第 2 轮新增 [知识获取瓶颈](roots/knowledge-acquisition-bottleneck.md)、[知识原则：智能体的本事主要来自专门知识](roots/feigenbaum-1977-knowledge-engineering.md)、[过程性知识（知道怎么做）](roots/procedural-knowledge.md)、[苦差事盲区](roots/graham-2012-schlep-blindness.md)
- 和你已有原则的关系：和你做 GTM 的主线最近：客户的真实需求在现场，不在问卷里。第 2 轮补上了“沉淀”那一半：Anthropic 说“别造新 agent，造 skill”，skill 就是把现场取回的做事经验写成文件；这和 1977 年专家系统时代的“知识工程”是同一件事，当年卡在“知识获取瓶颈”，现在 ToB agent 卡的还是它。
- 矛盾：前线部署很贵，规模化时会撞上利润率；两条 FDE 都没给出“什么时候该收手”的标准。
- 第 4 轮新增：[问题协商：用户说不清想找哪类企业时，先给样本，再陪他把问题说清](clips/2026-10-19-luke-question-negotiation-icp-search.md)、[Taylor 1968：提问协商——四层需求（Q1～Q4）和馆员问清需求的五个过滤器](clips/2026-10-19-taylor-question-negotiation-information-seeking.md)（共 14 条）；新源知识 [AIDE：按例探索的交互式数据探索](roots/dimitriadou-2014-aide-explore-by-example.md)、[提问与命令的信息分析](roots/mackay-1961-questions-and-commands.md)
- 第 4 轮的新线索：上面“没想清楚的问题”有了你自己的答案：用户说不清想找哪类企业时，先搜一小批具体企业给他看，再围绕样本协商“到底在问什么”，“未知”和“不符合”分开记。溯源时查出两处要你判断：方案说“照 AIDE 挑最像的样本”，AIDE 第一步其实是到没探索过的地方分散取样，不挑最像的（见误传）；方案规定“协商只在看到样本之后”，比 Taylor 更严，Taylor 的馆员是先问主题、动机、背景。
- 第 6 轮新增：[RealUserSim](clips/2026-10-22-zhu-realusersim-grounded-user-simulation.md)：用真实用户的原话约束模拟用户，像不像真人从 24% 升到 45%；人写的“你很生气”这类指令会被模型过度演绎。[Sim2Real 差距](clips/2026-10-22-zhou-sim2real-gap-user-simulation.md)：451 名真人对照 31 个模拟器，模拟用户太配合、打分太宽。现场取回来的样本，比坐在办公室里写的人设准
- 没想清楚的问题：客户画像也是说不清的知识。能不能像 AIDE 那样，拿一批具体公司让客户判“是 / 不是”，反推出画像？“征求意见别只问程序员”那条提醒：判“是 / 不是”的人必须是真正的目标客户。

### 原则 5：先在最小单位验证见效，再逐层放大；需求不清时，先做一个准备扔掉的原型

- 状态：已确认（2026-10-18）
- 支撑的新知识：[Agent 基础设施的一线观察](clips/2026-10-18-dotey-anthropic-agent-infrastructure-talk.md)、[Thiel一小时讲透从零做垄断的底层逻辑](clips/2026-10-18-kkawsb-peter-thiel-monopoly-lecture.md)、[Vibe Coding：原型加重设计两步法](clips/2026-10-18-dotey-vibe-coding-prototype-method.md)、[多数 Agent 其实只是工作流](clips/2026-10-18-eze-is-1-agent-vs-workflow-definition.md)
- 第 2 轮新增：[工具站出海月入 3000 刀的一年踩坑记](clips/2026-10-18-gefei55-tool-site-overseas-lessons.md)、[Marc Lou 六月赚 8.3 万美元](clips/2026-10-18-marclou-marclou-june-2026-revenue.md)、[宝玉写提示词的原则：做成可玩的模板](clips/2026-10-18-dotey-dotey-prompt-writing-principles.md)、[OpenAI 企业用 AI 的七条经验](clips/2026-10-18-shao-meng-openai-enterprise-ai-lessons.md)（共 8 条）
- 对应的源知识：[加尔定律](roots/galls-law.md)、[《人月神话》（准备扔掉一个）](roots/the-mythical-man-month.md)、[从 0 到 1](roots/zero-to-one.md)；第 2 轮新增 [精益创业](roots/lean-startup.md)、[小赌注组合](roots/portfolio-of-small-bets.md)、[过早优化是万恶之源（Knuth《带 goto 语句的结构化编程》）](roots/knuth-1974-structured-programming-go-to.md)
- 第 3 轮新增：[OpenAI Dots 放权指南：动作分进 6 个权限区，每周按证据升降](clips/2026-10-18-choopyplug1-openai-dots-agent-permission-zones.md)（共 9 条）
- 第 3 轮的新线索：给 agent 放权也是这个顺序：先挑一件出了错也扛得住的事，第一周全部只起草，之后每周只改一处。一次改三处，就不知道是哪一处出的问题。
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
- 第 4 轮新增：[拿 240 个真实外包项目考 AI agent：最好的也只做成 2.5%](clips/2026-10-20-mazeika-remote-labor-index.md)、[马斯克：未来的发现全是工程（“最稀缺的是验证”是转述者加的）](clips/2026-10-20-financeyf5-musk-future-discovery-is-engineering.md)（共 13 条）；新源知识 [GDPval：在真实的经济价值任务上评测 AI](roots/patwardhan-2025-gdpval.md)、[O 形环理论](roots/kremer-1993-o-ring-theory.md)
- 第 4 轮的新线索：RLI 拿 240 个真实外包项目考 agent，最好的也只做成 2.5%；GDPval 里单项任务已接近专家，换成要客户收下的整单就掉下来。整体速度由最慢的环节决定，整单成败由最弱的环节决定（O 形环，推断）。马斯克那条的“接下来最稀缺的是验证”是转述者加的，马斯克原推只说“未来的发现全是工程”。
- 第 6 轮新增（可能的反例）：[微软 Agensh](clips/2026-10-22-aigclink-agensh-decentralized-1024-agents.md)不设管家，最多 1024 个 agent 靠共享工作区和团队 Wiki 协作，规模变大后自己长出评审和整合者；[RLCR](clips/2026-10-24-genreasoning-genreasoning-rlcr-collective-rewards-agent-orgs.md)只奖励整体时，多个 agent 也自发长出分工和层级。协调成本没有消失，是被自己长出来的组织结构吸收了（推断）
- 没想清楚的问题：你同时开多个会话、多个 worktree，瓶颈是不是已经从“写”变成了“你的审查”？kimi-code 那条的结论是：质量最终取决于人投入了多少注意力。

### 原则 7：先保证不出局：不拿输不起的去换用不上的，把关键依赖分散开

- 状态：已确认（2026-10-18）
- 支撑的新知识：[巴菲特经典演讲：先保证不穷回去](clips/2026-10-18-nextbullready-buffett-classic-speech.md)、[三旗理论：合法减税、保护资产、自由生活](clips/2026-10-18-eric-make-money-three-flags-theory.md)、[张一鸣 66 条成长心得与延迟满足](clips/2026-10-18-sea-bitcoin-zhang-yiming-66-growth-tips.md)
- 第 2 轮新增：[Marc Lou 六月赚 8.3 万美元](clips/2026-10-18-marclou-marclou-june-2026-revenue.md)、[离职大厂做 OPC 第一年收入报告](clips/2026-10-18-weiyipei-opc-first-year-income-report.md)（共 5 条）
- 对应的源知识：[破产风险](roots/risk-of-ruin.md)、[赌徒破产问题](roots/gamblers-ruin.md)、[凯利公式](roots/kelly-criterion.md)、[分散投资](roots/diversification-finance.md)；第 2 轮新增 [小赌注组合](roots/portfolio-of-small-bets.md)、[机会成本](roots/opportunity-cost.md)
- 第 3 轮新增：[保险建议：孩子重疾险在香港买，成人买医疗险不买重疾](clips/2026-10-18-captainlufei999-insurance-advice-hk-critical-illness.md)、[OpenAI Dots 放权指南：动作分进 6 个权限区，每周按证据升降](clips/2026-10-18-choopyplug1-openai-dots-agent-permission-zones.md)（共 7 条）；新源知识 [道德风险](roots/moral-hazard.md)、[逆向选择](roots/adverse-selection.md)、[理性购买保险](roots/mossin-1968-rational-insurance-purchasing.md)
- 第 3 轮的新线索：Mossin 1968 年的结论：保费里的附加费用越高，越该少买保险、自己扛小损失，只把扛不住的大损失交出去。这就是“不拿输不起的去换用不上的”在保险上的算法。保险那条推文有几处事实说过头了，见「三、待查 · 顺手查出来的误传」。
- 矛盾：张一鸣那条转述者认为“落袋为安也是选项”，和棉花糖实验对着干；后来的复现研究（Watts 2018）支持他：延迟满足划不划算，要看未来回报是否可靠。
- 第 2 轮的新线索：Marc Lou 和 OPC 两条是个人版本：AI 把每次尝试的成本压低后，同时押很多小赌注、靠多条收入线兜底，比押一个大项目更不容易出局。
- 第 4 轮新增：[Sohl-Dickstein 在斯坦福：稳妥的路已经不稳妥](clips/2026-10-20-financeyf5-sohl-dickstein-safe-path-not-safe.md)（共 8 条）；新源知识 [现代投资组合理论（均值-方差分析）](roots/modern-portfolio-theory.md)
- 第 4 轮的新线索：Sohl-Dickstein 给这条加了边界：躲不开的共同风险很高时（他说的是 AI 带来的全局冲击），“稳妥”的选项不再降低风险，只是放弃了上限。所以“不出局”要看自己扛不扛得住，不看选项表面上稳不稳。
- 第 7 轮新增：[天涯大佬：2027 年以后要活成的样子](clips/2026-10-24-caomei-nz-tianya-how-to-live-after-2027.md)：第四、六条说轻资产、无负债、多国签证、美元现金，“不要把所有鸡蛋放在一个篮子里”，随时能换个地方重新开始。是这条原则落到个人生活规划上的样子（Luke 点赞的帖子，不是研究）
- 没想清楚的问题：三旗理论的具体做法在配图里，没核对到。

### 原则 8：AI 在它擅长的事上拉平差距，在它不擅长、要判断好坏的地方，放大会判断的人

- 状态：已确认（2026-10-18，第 2 轮新增，说法按建议改过）
- 已加进全局规则：2026-10-18，`~/.claude/CLAUDE.md` 第 5 节「标出要人判断的地方」
- 支撑的新知识：[会写代码才玩得好 vibe coding](clips/2026-10-18-aryanlabde-vibe-coding-needs-coding-skill.md)、[Agent 智能体是模型能力的放大器](clips/2026-10-18-waytoagi-agent-model-capability-amplifier.md)、[Kimi-code重构一个月的架构复盘](clips/2026-10-18-real-kai42-kimi-code-rewrite-retrospective.md)、[吴恩达的智能体编程时代软件工程能力图](clips/2026-10-18-andrewyng-andrew-ng-ai-engineering-skills-map.md)、[Agent 循环工程晚宴讨论要点](clips/2026-10-18-jerryjliu0-agent-loop-engineering-dinner.md)、[哈萨比斯：懂 AI 的一个人胜过团队](clips/2026-10-18-anatolikopadze-hassabis-ai-person-outperforms-team.md)（共 6 条）
- 对应的源知识：[技术放大定律](roots/law-of-amplification.md)、[智力放大](roots/intelligence-amplification.md)、[吸收能力](roots/absorptive-capacity.md)、[自动化的反讽](roots/ironies-of-automation.md)、[人类监督控制](roots/sheridan-1992-human-supervisory-control.md)
- 第 3 轮新增：[yetone 用 3 个 /loop 循环让 Claude Code 自己维护 Magpie](clips/2026-10-18-dotey-yetone-magpie-three-loops-workflow.md)（共 7 条）
- 第 3 轮的新线索：yetone 把修 bug、发版、回复用户都交给循环，自己只留 AI 做不好的 UI/UX 审美判断，是这条原则落到分工上的样子。
- 和你已有原则的关系：对应你的“模型出草稿，人来定稿”：定稿的人得自己看得出好坏。
- 矛盾：这是这一轮最大的一处冲突。实验数据站在另一边：BCG 顾问实验（[在参差不齐的技术边界上航行（BCG 顾问实验）](roots/dellacqua-2023-jagged-technological-frontier.md)）和 GitHub Copilot 对照实验（[AI 对开发者生产率的影响：GitHub Copilot 对照实验](roots/peng-2023-copilot-developer-productivity.md)）都发现，原本水平低的人提升最多；[世界分成会用与不会用 ChatGPT](clips/2026-10-18-dotey-chatgpt-two-kinds-of-people.md) 也说 AI 先缩小新手和高手的差距。所以草稿原来的说法“工具放大的是判断力，自己判断不了好坏的产出用得越多越危险”只对了一半，确认时改成了现在这样：两边都对，只是适用的任务不同。BCG 实验里，超出 AI 能力边界的任务，用 AI 的人反而做得更差。
- 第 4 轮新增：[人和 AI 比设计游戏：AI 自己设计的卖得更贵，标明"人做的"也不加价](clips/2026-10-20-conlon-human-ai-competition-experiment.md)、[AI 个性化的大规模随机实验：人和 AI 的人格搭配会影响广告质量和点击率（PNAS）](clips/2026-10-20-sinan-aral-ai-personalization-pnas.md)、[拿 240 个真实外包项目考 AI agent：最好的也只做成 2.5%](clips/2026-10-20-mazeika-remote-labor-index.md)（共 10 条）；新源知识 [手工效应](roots/fuchs-2015-handmade-effect.md)、[人格搭配改善人机协作（PNAS 广告实验）](roots/ju-2026-personality-pairing.md)
- 第 4 轮的新矛盾：Conlon 的实验（真钱激励）里，AI 自己设计的小游戏比专业人士指挥 AI 做的卖得更贵，人事先以为自己会赢，标明“人做的”也不加价。“人保留品味和判断”在这个实验里没得到支持（和《预测机器》、手工效应对着干，强）。不过实验是几分钟、几十美分的小产品。RLI 站在另一边：整单交付 AI 只做成 2.5%。可能的分界（推断）：小而完整、马上能被市场打分的东西，AI 已经不输人；链条长、要客户验收的整单，还离不开会判断的人。
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
- 第 3 轮新增：这一轮 7 条里有 4 条的转述和原文对不上：[Terminal-RSI：两轮自重写加强化学习，27B 终端 agent 从 51.7% 涨到 86.5%](clips/2026-10-18-nft-chen-terminal-rsi-recursive-self-improvement.md)、[GLM 5.3 只靠后训练大涨，被 SemiAnalysis 嘉宾称为警钟](clips/2026-10-18-nft-chen-glm-5-3-post-training-wake-up-call.md)、[常驻 agent 的 6 层结构（推文作者据 OpenAI 资料自制的 PDF）](clips/2026-10-18-choopyplug1-openai-always-on-agent-six-layers.md)、[保险建议：孩子重疾险在香港买，成人买医疗险不买重疾](clips/2026-10-18-captainlufei999-insurance-advice-hk-critical-illness.md)（共 11 条）
- 第 3 轮的新线索：最典型的是“OpenAI 刚发了一份 10 页 PDF”：那份 PDF 其实是推文作者自己整理的，6 层的名字也是他起的，转一手就成了“官方文件”。同一个作者的长文里写明了哪些是官方、哪些是自创，推文却没写。
- 和你已有原则的关系：就是你全局规则里的“不编造：每个数字要能指回出处”，也是这个仓库本身的做法。这一轮核对一手材料时，151 条里查出十几处转述和原文对不上（见「三、待查 · 顺手查出来的误传」）。
- 矛盾：一手材料不自动更可信，当事人讲自己的东西也有立场。黄仁勋那条（[黄仁勋首发：开放模型为何重要](clips/2026-10-18-jensenhuang-jensen-open-models-letter.md)）就是例子：要同时看论证和说话人的利益。
- 第 4 轮新增：[PwC 调查（在用或打算用生成式 AI 的大企业部长级 487 人）：已导入者里只有 29% 说对收入有贡献，多数只感到生产率提升](clips/2026-10-20-pwc-japan-b2b-sales-genai-survey-2025.md)、[日本大额 B2B 采购：九成选型用生成式 AI，84.7% 至少对一家候选厂商没填表就做了调查](clips/2026-10-20-ideatech-btob-buyer-genai-purchasing-survey.md)、[日本 B2B 的 AI 搜索对策：77% 觉得丢了商机，一半多还没动手，卡在不会做和算不清回报](clips/2026-10-20-probel-btob-ai-search-llmo-survey.md)、[AI 个性化的大规模随机实验：人和 AI 的人格搭配会影响广告质量和点击率（PNAS）](clips/2026-10-20-sinan-aral-ai-personalization-pnas.md)、[agent 每步的选择题交给小决策模型（UIUC 等，推文误作普林斯顿和谷歌），模拟网店里 4B 模型完成率 91.5%](clips/2026-10-20-rohanpaul-ai-agent-decision-model-small-beats-big.md)、[马斯克：未来的发现全是工程（“最稀缺的是验证”是转述者加的）](clips/2026-10-20-financeyf5-musk-future-discovery-is-engineering.md)、[智谱论文曝光内部统一多模态模型 GLM-Omni](clips/2026-10-20-nft-chen-zhipu-glm-omni-unified-multimodal-paper.md)、[麦肯锡报告《优秀 CEO 的行为习惯》](clips/2026-10-20-jujulife7-mckinsey-ceo-habits-report.md)、[网易 LobsterAI《中国办公 Agent 用户行为报告》的反直觉结论](clips/2026-10-20-vista8-lobsterai-china-office-agent-user-report.md)（共 20 条）
- 第 4 轮的新线索：这一轮 25 条里查出 22 处转述和原件对不上，4 个存档标题当场改了。最多的是厂商调查：PwC 的“68% 已用 AI”其实是样本只收“在用或打算用”的人；IDEATECH 只报了“不信任”的 48.5%，没报同样多的“信任”；PROBEL 的 80.6% 和自己的图表算不上。这些厂商的结论又都和它卖的东西一致。引用厂商数字时，要同时写清样本是谁、有多大、这家厂商卖什么。
- 第 6 轮新增：[HarnessPro 的报道](clips/2026-10-24-qbitai-harnesspro-pareto-rsi.md)：量子位标题写“成本降 53%”，查论文，这是均衡档在一个基准上对比 RHO 的单项数字；摘要里的平均数是高性能档降 26.1%。转述挑了最好看的那个数
- 第 7 轮新增：[天涯大佬：2027 年以后要活成的样子](clips/2026-10-24-caomei-nz-tianya-how-to-live-after-2027.md)：第一、五条说只看中文互联网和算法推荐，看到的都是“别人筛选过、翻译过、加工过”的二手信息，会被困在信息茧房里，所以要能直接读英文的一手材料
- 没想清楚的问题：给客户的提案和邮件里引用的数字（比如“一小时内联系线索，谈上决策人的可能性高 7 倍”），有多少是二手转述？这一轮查到这组数字就常被混着引用（见误传）。

### 原则 11：上下文是稀缺资源：常驻只放索引，细节按需加载，子任务各带干净的上下文

- 状态：已确认（2026-10-18，第 2 轮新增）
- 支撑的新知识：[上下文工程：智能体的核心实践指南](clips/2026-10-18-shao-meng-context-engineering-guide.md)、[Agent Skills 是上下文卸载](clips/2026-10-18-yonah-x-skills-context-offloading.md)、[Manus 把工具分成三层的设计](clips/2026-10-18-dotey-manus-three-layer-tools.md)、[ADK 开发者该懂的五种 Agent Skill 设计模式](clips/2026-10-18-googlecloudtech-adk-agent-skill-design-patterns.md)、[Agent Skills设计哲学与迭代](clips/2026-10-18-dotey-agent-skills-design-philosophy.md)、[Claude Code 的 Task 工具原理](clips/2026-10-18-dotey-claude-code-task-subagent.md)、[用个人AI编排者带动一支永不睡觉的开发队](clips/2026-10-18-ayi-ainotes-personal-ai-orchestrator-openclaw.md)（共 7 条）
- 第 5 轮新增：[Claude 5 代模型的上下文工程新规矩](clips/2026-10-21-shihipar-context-engineering-claude-5.md)：系统提示删掉八成，少写规则和例子，按需加载
- 对应的源知识：[AI 智能体的上下文工程](roots/anthropic-2025-effective-context-engineering.md)、[上下文工程](roots/context-engineering.md)、[用 Agent Skills 让智能体胜任真实工作](roots/anthropic-2025-agent-skills.md)、[渐进式披露](roots/progressive-disclosure.md)、[Unix 哲学](roots/unix-philosophy.md)、[虚拟内存](roots/virtual-memory.md)
- 第 3 轮新增：[常驻 agent 的 6 层结构（推文作者据 OpenAI 资料自制的 PDF）](clips/2026-10-18-choopyplug1-openai-always-on-agent-six-layers.md)（共 8 条）；新源知识 [纵深防御](roots/defense-in-depth.md)
- 第 3 轮的新线索：OpenAI 系统卡实测，同一个环境里连着做的中间任务从 5 个加到 10 个，越界比例从 8.6% 升到 19.7%，多是把信息带进了不相关的任务。给“子任务各带干净的上下文”添了一条实测证据。
- 和你已有原则的关系：你做 skill 的规矩“主文件要小，细节拆出去按需加载”就是这一条。根是 1985 年苹果界面设计里的渐进式披露，和操作系统的虚拟内存（常用的放内存，其余放磁盘，用到再调）。
- 矛盾：Cognition《别做多智能体》认为拆成子任务会丢上下文；所以只拆“只读、只交回结果”的子任务，要做决定的留在主线。
- 第 4 轮新增：[Meta 的瘦编排器模式：编排器只管路由和检查，不做领域推理，14 个专项子 agent 各管一块](clips/2026-10-20-meta-thin-orchestrator-agent-architecture.md)、[agent 的记忆先存原始轨迹，等新任务来了再现场整理，比事先提炼成反思或 skill 更好用](clips/2026-10-20-zhou-just-in-time-memory.md)、[模型每周都在换：别把自己的上下文锁在一家产品里](clips/2026-10-20-brian-lovin-portable-context-switching.md)（共 11 条）；新源知识 [临床规模负载下，编排式多 agent 比单 agent 更能保住准确率](roots/klang-2025-orchestrated-multi-agents.md)、[建构性记忆的认知神经科学：回忆过去与想象未来](roots/schacter-2007-constructive-memory.md)、[惰性学习（对照：积极学习）](roots/lazy-learning.md)
- 第 4 轮的新线索：Meta 引的西奈山研究给“子任务各带干净的上下文”添了实测：80 个任务一起塞给一个 agent，准确率 16.6%；分给编排式多 agent，65.3%。JitMem 又往前推了一步，连整理也按需做：先存原始记录，等知道要解决什么再现场整理。这和本项目经验库“做完就提炼”的做法相反，见「三、待查」的对照。
- 第 6 轮新增：[REM：编程 agent 的经验记忆](clips/2026-10-22-chen-rem-experience-memory-coding-agents.md)：难点不在找得准，而在存成什么样、什么时候给、给完就撤；无关的经验放进上下文会拖累表现，对最强的模型甚至有害
- 没想清楚的问题：这一条和原则 4 的“沉淀”是一回事吗？skill 既是给 agent 省上下文的办法，也是把现场经验存下来的办法。

### 原则 12：放权按后果分级、靠证据升级：碰钱、对外、删除、难撤销的留给人；其余先只起草，记录好了再一级级放宽，一次意外就收回

- 状态：已确认（2026-10-18，第 3 轮新增）
- 已加进全局规则：2026-10-18，`~/.claude/CLAUDE.md` 第 5 节「放权靠证据升级」
- 支撑的新知识：[OpenAI Dots 放权指南：动作分进 6 个权限区，每周按证据升降](clips/2026-10-18-choopyplug1-openai-dots-agent-permission-zones.md)、[常驻 agent 的 6 层结构（推文作者据 OpenAI 资料自制的 PDF）](clips/2026-10-18-choopyplug1-openai-always-on-agent-six-layers.md)、[yetone 用 3 个 /loop 循环让 Claude Code 自己维护 Magpie](clips/2026-10-18-dotey-yetone-magpie-three-loops-workflow.md)（共 3 条）
- 第 5 轮新增：[Claude Code 团队审代码的做法](clips/2026-10-21-dotey-claude-code-review-swiss-cheese.md)：九成代码由 AI 写，多道机器检查像叠起来的瑞士奶酪片，人只做机器做不好的判断，剩下的靠快速回滚兜底
- 对应的源知识：[最小权限原则](roots/principle-of-least-privilege.md)、[失效安全默认（默认拒绝）](roots/fail-safe-defaults.md)、[自动化的类型与等级模型](roots/parasuraman-2000-levels-of-automation.md)、[对自动化的信任：为恰当依赖而设计](roots/lee-2004-trust-in-automation.md)、[纵深防御](roots/defense-in-depth.md)、[瑞士奶酪模型](roots/swiss-cheese-model.md)、[例外管理（例外原则）](roots/management-by-exception.md)
- 和你已有原则的关系：你全局规则第 3 节写的“只有这几类事才停下来问他：要花钱、要对外发送、要删除东西、要合并或上线……”，就是 Dots 那条说的“必须交回人”那一区。这一条补的是另一半：其余的事不是一次放开，而是按记录一级级放宽，出一次意外就退一级。
- 矛盾：支撑只有 3 条，都是这两天的常驻 agent 话题，还要更多证据。另外，什么都要批准会让人开始闭着眼点同意（Dots 那条自己也提到），分级太细反而失效。
- 第 4 轮新增：[agent 每步的选择题交给小决策模型（UIUC 等，推文误作普林斯顿和谷歌），模拟网店里 4B 模型完成率 91.5%](clips/2026-10-20-rohanpaul-ai-agent-decision-model-small-beats-big.md)、[Anthropic 经济指数「节奏」：用法跟着作息走，越值钱的活越费算力，越放手交给 AI 的人越乐观](clips/2026-10-20-anthropic-economic-index-cadences.md)、[模型不动，只让技能库从用户请求里长：设计 agent 的技能从 76 个长到 139 个](clips/2026-10-20-du-designer-rsi-procedural-memory.md)（共 6 条）；新源知识 [深度神经网络的选择性分类（带拒答选项）](roots/geifman-2017-selective-classification.md)、[Chow 拒识规则：识别错误率与拒识率的最优权衡](roots/chow-1970-reject-option.md)、[哪些经济任务在用 AI 做（Anthropic 经济指数第一篇）](roots/handa-2025-anthropic-economic-index.md)
- 第 4 轮的新线索：三条都在讲按证据一点点放手。小决策模型那篇：门槛在 agent 自己的运行记录上拟合，有把握才交给小模型；不设门槛、全部放手，成功率掉 19 个百分点。那篇里当老师的就是本项目分类用的 Jev，和第零步“置信度 0.9 以上才直接采用”是同一个做法。Designer-RSI 借的安全策略改进（SPIBB）：证据不够的地方沿用旧做法。Anthropic 经济指数：Claude Code 里人更放手，越放手的人越乐观（只是相关，可能是选择效应）。
- 第 6 轮新增：[人在回路里只是摆设](clips/2026-10-22-mitchell-agents-push-humans-out-of-loop.md)：agent 用得越久，人越没本事审它（挑战“人在环中”，强）；[长任务 agent 的证据式监督](clips/2026-10-22-sun-evidence-grounded-agent-oversight.md)：用程序把 agent 自作主张的关键决定连同证据摆给人看，只把有后果的交给人；[Harrison Chase：是非题交给决策模型](clips/2026-10-22-hwchase17-yes-no-calls-jev.md)：拿得准的便宜模型先判，拿不准的再往上交。新线索：放权靠证据升级的前提，是人还看得懂证据
- 没想清楚的问题：你同时开多个会话、用 /loop 跑任务，现在哪些动作已经可以从“先问”升到“自己做”？可以拿你最近一周批准过、而且一字没改的动作当证据（推断，待 Luke 确认）。

### 原则 13：买方先自己查、后找销售。一般信息被 AI 做便宜后，能让买方开口的是 AI 给不了的一手信息（缺点、风险、真实价格、不适合谁）。联系要踩在买方要买的时间点上，次数要少，走对方愿意的渠道；买方要的硬信息（服务保证、安全、解约条件、真实价格、实绩）先公开出来

- 状态：已确认（2026-10-21，第 4 轮新增）；2026-10-24 按补课第 10 题改了后半句，原来是“联系的时机交给买方”，Luke 选了 A
- 已加进全局规则：2026-10-21，`~/.claude/CLAUDE.md` 第 5 节「买方先自己查」（2026-10-25 已同步成新说法，Luke 选了 A）
- 补课第 10 题（2026-10-24，[简报](docs/study/2026-10-24-topic-10-buyer-self-research.md)；材料还没认可，不计入排名）：前半句大体站得住，但“先用 AI 查”在日本要打折，[総務省 2026 白书](clips/2026-10-24-soumu-2026-procurement-genai-use.md)里日本企业采购业务用生成式 AI 的只有 38.0%（美国 80.9%）。后半句改写的依据：[联系太多会把客户推走](clips/2026-10-24-godfrey-enough-is-enough-multichannel-contact.md)、[在客户要买的时候上门](clips/2026-10-24-kumar-customer-focused-sales-campaign-timing.md)、[展会见过再跟进](clips/2026-10-24-smith-trade-show-follow-up-personal-selling.md)、[买方决定什么时候找销售](clips/2026-10-24-kalwey-holistic-selling-buyer-led-journey.md)；“硬信息先公开”的依据：[IPA 云服务安全利用指引](clips/2026-10-24-ipa-sme-cloud-service-checklist.md)
- 支撑的新知识：[日本 B2B 采购者：八成嫌官网都是一般论，57.1% 按“诚实”决定找谁询问](clips/2026-10-20-ideatech-btob-buyer-information-contact-survey.md)、[日本大额 B2B 采购：九成选型用生成式 AI，84.7% 至少对一家候选厂商没填表就做了调查](clips/2026-10-20-ideatech-btob-buyer-genai-purchasing-survey.md)、[日本 B2B 的 AI 搜索对策：77% 觉得丢了商机，一半多还没动手，卡在不会做和算不清回报](clips/2026-10-20-probel-btob-ai-search-llmo-survey.md)、[Gartner 新 B2B 购买旅程：买方只花 17% 的时间见供应商](clips/2026-10-18-gartner-new-b2b-buying-journey.md)（共 4 条）
- 第 5 轮新增：[生成 AI 时代的 BtoB 买方旅程图](clips/2026-10-21-kitagawa-genai-btob-buyer-journey-map.md)、[HubSpot Japan《日本 BtoB 购买意识与实态调查》](clips/2026-10-21-hubspot-japan-state-of-buyer-2026.md)：日本买方见销售之前先自己用 AI 查，和这条的前半句一致
- 对应的源知识：[CEB：B2B 营销的数字化演变（57% 研究）](roots/ceb-2012-digital-evolution-b2b-marketing.md)、[6sense 2024 B2B 买方体验报告](roots/6sense-2024-b2b-buyer-experience.md)、[Gartner 新 B2B 购买旅程（购买任务与买方赋能）](roots/gartner-2019-b2b-buying-journey.md)、[双面说服（正反两面信息）](roots/two-sided-persuasion.md)、[自愿披露与“沉默即坏消息”（信息解开）](roots/voluntary-disclosure-unraveling.md)、[信息经济学（搜寻成本与价格离散）](roots/stigler-1961-economics-of-information.md)、[生成式引擎优化（GEO）](roots/aggarwal-2024-geo.md)
- 和你已有原则的关系：是原则 3 落到获客上的样子：AI 把一般信息做便宜了，稀缺的是只有卖方自己知道、又肯说出来的那部分。也碰到原则 9：AI 搜索（GEO）是新渠道，PROBEL 说一半多的企业还没动手。
- 矛盾：4 条证据都是厂商调查，结论都和各自卖的东西一致。IDEATECH 自己的数据也显示，66.5% 的买方在方案探索阶段为止就向最终厂商报了名，比“走完 57%（CEB）、69%（6sense）才接触”早；Oldroyd 的线索研究主张一小时内跟进，和“联系时机交给买方”对着干（弱）。2026-10-24 改写后的说法把两边接上了：要联系，但要踩在买方发出信号或要买的时候。另外按 Allen 1991 的元分析，只讲缺点、不回应，可能适得其反。
- 第 6 轮新增：[厂商调查：B2B 采购者用生成式 AI 选供应商](clips/2026-10-22-probel-btob-buyers-ai-vendor-selection-survey.md)：66.4% 用生成式 AI 选供应商。厂商调查（这家卖“让 AI 推荐你”的服务，149 人网络调查），“98% 会考虑不知名公司”来自带条件的问法，要打折看
- 没想清楚的问题：你的冷邮件和表单营销里，主动写出“不适合谁”“真实价格”，回信率会不会变？可以拿一封邮件做两版对照（推断，待验证）。

## 二、知识底座

被新知识指向得最多的源理论。“直接”是新知识直接指向它；“连同间接”还算上了通过更上层源知识追到它的。排在最前面的，就是最近看到的这些新东西共同的根。由 `tools/rank_roots.py` 算出。

| 排名 | 源知识 | 被几条新知识指向（直接 / 连同间接） | 更底层的源头 |
|---|---|---|---|
| 1 | [反馈](roots/feedback.md) | 4 / 97 | 已到基础层 |
| 2 | [控制论](roots/cybernetics.md) | 4 / 75 | 已到基础层 |
| 3 | [自然选择](roots/natural-selection.md) | 0 / 65 | 已到基础层 |
| 4 | [有限理性](roots/bounded-rationality.md) | 0 / 59 | 已到基础层 |
| 5 | [比较优势](roots/comparative-advantage.md) | 2 / 50 | 已到基础层 |
| 6 | [控制理论](roots/control-theory.md) | 0 / 45 | [反馈](roots/feedback.md) |
| 7 | [分工](roots/division-of-labour.md) | 6 / 42 | [比较优势](roots/comparative-advantage.md) |
| 8 | [经验曲线效应](roots/experience-curve-effect.md) | 2 / 37 | [学习曲线](roots/learning-curve.md) |
| 9 | [学习曲线](roots/learning-curve.md) | 0 / 37 | 已到基础层 |
| 10 | [智能体](roots/intelligent-agent.md) | 4 / 36 | [反馈](roots/feedback.md) |
| 11 | [摩尔定律](roots/moores-law.md) | 1 / 34 | [经验曲线效应](roots/experience-curve-effect.md) |
| 12 | [效果律](roots/law-of-effect.md) | 0 / 34 | [自然选择](roots/natural-selection.md) |
| 13 | [苦涩的教训](roots/bitter-lesson.md) | 12 / 33 | [摩尔定律](roots/moores-law.md) |
| 14 | [构建高效的智能体](roots/anthropic-2024-building-effective-agents.md) | 17 / 31 | [智能体](roots/intelligent-agent.md)、[分工](roots/division-of-labour.md) |
| 15 | [强化学习](roots/reinforcement-learning.md) | 2 / 28 | [效果律](roots/law-of-effect.md)、[控制理论](roots/control-theory.md) |

和第 5 轮比：反馈从 84 条涨到 97 条，控制论 70→75，自然选择 56→64，有限理性 52→59，比较优势 43→50，分工 36→42。强化学习新进前 15，默会知识掉了出去。第 6 轮 22 条新知识里，追到这几个基础源头的主要是三组：agent 自己改自己的运行框架（HarnessPro、Harness² 解读、Evo² 解读、Imbue），用户模拟（Sim2Real 差距、RealUserSim、披露闸门、KnowSim），人怎么监督 agent（Mitchell、证据式监督）。

和第 4 轮比：反馈从 80 条涨到 84 条，自然选择 54→56，有限理性 51→52，控制论 70→70（2026-10-21 弱关系复核删掉了 92 处牵强的关系，所以涨得比第 5 轮刚合并时少）。控制理论从第 7 名升到第 6 名。第 5 轮 8 条新知识里，追到这几个基础源头的主要是用户模拟（模拟客户从不走开、Sim2Real 差距）、开放式搜索（质量多样性、新颖性搜索）和企业 AI 落地（前线部署工程师、现地现物）这几条。

和第 3 轮比（含 2026-10-19 认可补课第 1 题后的重排）：反馈从 68 条涨到 80 条，自然选择从 45 条涨到 54 条、升到第 3。涨的全来自这一轮：25 条里有 12 条顺着更底层的源头追到反馈，9 条追到自然选择，主要是 agent 自我改进（Harness²、Designer-RSI、JitMem）、用户模拟（MIMESIS 等）和算法合谋这几条。控制理论从第 12 名升到第 7 名；效果律回到前 15，完全竞争掉了出去。

直接被指向最多的：构建高效的智能体（17）、苦涩的教训（12）、AI 智能体的上下文工程（9）、递归自我改进（8）、约束理论（8）、待完成的任务（7）、人类监督控制（7）、Unix 哲学（7）。递归自我改进从第 5 轮的 5 条涨到 8 条，人类监督控制是这一轮新挤进来的。

## 三、待查

真正的新东西最可能藏在这里。

### 和经典理论对着干的

第 1 轮 9 处，第 2 轮新增 21 处，第 3 轮新增 3 处，2026-10-19 认可补课第 1 题后计入 2 处，第 4 轮新增 6 处，第 5 轮新增 2 处；2026-10-21 弱关系复核删掉 5 处牵强的；第 6 轮新增 10 处，现在共 51 处。强的 18 处排在前面。

| 新知识 | 对着干的经典 | 强弱 |
|---|---|---|
| [人和 AI 比设计游戏：AI 自己设计的卖得更贵，标明"人做的"也不加价](clips/2026-10-20-conlon-human-ai-competition-experiment.md) | [《预测机器：人工智能的简单经济学》](roots/agrawal-2018-prediction-machines.md) | 强 |
| [微软 Agensh：不设管家，最多 1024 个 agent 靠共享工作区和团队 Wiki 自协作，规模变大后自发长出评审和整合者](clips/2026-10-22-aigclink-agensh-decentralized-1024-agents.md) | [Anthropic 多智能体研究系统](roots/anthropic-2025-multi-agent-research-system.md) | 强 |
| [陶哲轩谈 AI 与数学的演讲要点](clips/2026-10-18-dotey-terence-tao-ai-math-talk.md) | [通用人工智能的火花：GPT-4 早期实验](roots/bubeck-2023-sparks-agi.md) | 强 |
| [黄亚生预测中国模式走到尽头](clips/2026-10-18-bingliu34173809-huang-yasheng-china-model.md) | [中国模式（北京共识）](roots/china-model.md) | 强 |
| [保险建议：孩子重疾险在香港买，成人买医疗险不买重疾](clips/2026-10-18-captainlufei999-insurance-advice-hk-critical-illness.md) | [保监会未成年人身故保险金限额通知（保监发〔2015〕90号）](roots/circ-2015-minor-death-benefit-cap.md) | 强 |
| [Anthropic 设计负责人谈 AI 时代设计流程](clips/2026-10-18-dotey-anthropic-design-process-ai-era.md) | [双钻石设计流程](roots/double-diamond-design-process-model.md) | 强 |
| [人和 AI 比设计游戏：AI 自己设计的卖得更贵，标明"人做的"也不加价](clips/2026-10-20-conlon-human-ai-competition-experiment.md) | [手工效应](roots/fuchs-2015-handmade-effect.md) | 强 |
| [人在回路里只是摆设：agent 用得越久，人越没本事审它，要在产品和组织两头给人加"认知脚手架](clips/2026-10-22-mitchell-agents-push-humans-out-of-loop.md) | [人在环中](roots/human-in-the-loop.md) | 强 |
| [杨立昆谈智能不等于控制欲](clips/2026-10-18-dotey-lecun-intelligence-not-domination.md) | [工具性趋同](roots/instrumental-convergence.md) | 强 |
| [唐杰谈缩放定律：不只是堆参数](clips/2026-10-18-jietang-scaling-law-beyond-parameters.md) | [神经语言模型的缩放定律](roots/kaplan-2020-scaling-laws.md) | 强 |
| [LeCun：下个万亿AI公司不靠LLM](clips/2026-10-18-phosphenq-lecun-lecture-beyond-llms.md) | [神经网络规模定律](roots/neural-scaling-law.md) | 强 |
| [Pi 作者：代码即真相，Bash 够用](clips/2026-10-18-dotey-pi-authors-code-bash-insights.md) | [检索增强生成（RAG）](roots/retrieval-augmented-generation.md) | 强 |
| [Gartner 新 B2B 购买旅程：买方只花 17% 的时间见供应商](clips/2026-10-18-gartner-new-b2b-buying-journey.md) | [购买类型三分法与 BuyGrid](roots/robinson-1967-industrial-buying-creative-marketing.md) | 强 |
| [不用反向传播预训练 Transformer，验证损失反超 Adam](clips/2026-10-23-spicey-lemonade-pretrain-transformers-without-backprop.md) | [反向传播（用误差反传学习表示）](roots/rumelhart-1986-backpropagation.md) | 强 |
| [与Claude Code讨论艺术与约束](clips/2026-10-18-turingou-constraint-in-live-music-product.md) | [Cloudflare Code Mode：让模型写代码放进沙箱执行](roots/varda-2025-code-mode.md) | 强 |
| [Meta 的 MIMESIS：用真人行为训练的用户模拟器，比让助手模型扮用户更好练 agent](clips/2026-10-20-dair-ai-mimesis-user-simulator.md) | [τ-bench：工具、agent、用户三方交互的基准](roots/yao-2024-tau-bench.md) | 强 |
| [agent 的记忆先存原始轨迹，等新任务来了再现场整理，比事先提炼成反思或 skill 更好用](clips/2026-10-20-zhou-just-in-time-memory.md) | [ExpeL：大模型智能体是经验学习者](roots/zhao-2023-expel.md) | 强 |
| [智谱唐杰团队开源 HarnessPro：agent 无标签自己改 harness，按"省钱、均衡、性能"三档进化，成本最多降 53%](clips/2026-10-24-qbitai-harnesspro-pareto-rsi.md) | [用大模型当裁判](roots/zheng-2023-llm-as-a-judge.md) | 强 |
| [马斯克：AI 之后工作会变成可选的，像自家种菜（后半段推演是转述者加的）](clips/2026-10-24-ayi-ainotes-musk-future-work-becomes-gardening.md) | [自动化与新任务：技术如何替代又重新吸纳劳动力](roots/acemoglu-2019-automation-new-tasks.md) | 弱（模型复核通过） |
| [马斯克：未来的发现全是工程（“最稀缺的是验证”是转述者加的）](clips/2026-10-20-financeyf5-musk-future-discovery-is-engineering.md) | [多者异也（多即不同）](roots/anderson-1972-more-is-different.md) | 弱（模型复核通过） |
| [Tripo Eden：先建地图再渲染](clips/2026-10-18-svpino-tripo-eden-world-model-map.md) | [苦涩的教训](roots/bitter-lesson.md) | 弱（模型复核通过） |
| [Tripo Eden：先建地图再渲染](clips/2026-10-18-svpino-tripo-eden-world-model-map.md) | [视频生成模型是世界模拟器（Sora 技术报告）](roots/brooks-2024-video-world-simulators.md) | 弱（模型复核通过） |
| [微软 Agensh：不设管家，最多 1024 个 agent 靠共享工作区和团队 Wiki 自协作，规模变大后自发长出评审和整合者](clips/2026-10-22-aigclink-agensh-decentralized-1024-agents.md) | [布鲁克斯定律](roots/brookss-law.md) | 弱（模型复核通过） |
| [Claude 5 代模型的上下文工程新规矩：系统提示删掉八成，少写规则和例子，按需加载](clips/2026-10-21-shihipar-context-engineering-claude-5.md) | [语言模型是少样本学习者（GPT-3 论文）](roots/brown-2020-few-shot-learners.md) | 弱（模型复核通过） |
| [大阪府各区划与公立小学教育概况](clips/2026-10-18-qiancaobuzhiqiu-osaka-areas-public-schools.md) | [科尔曼报告（《教育机会均等》）](roots/coleman-report.md) | 弱（模型复核通过） |
| [马斯克：AI 之后工作会变成可选的，像自家种菜（后半段推演是转述者加的）](clips/2026-10-24-ayi-ainotes-musk-future-work-becomes-gardening.md) | [比较优势](roots/comparative-advantage.md) | 弱（模型复核通过） |
| [Kimi-code重构一个月的架构复盘](clips/2026-10-18-real-kai42-kimi-code-rewrite-retrospective.md) | [在参差不齐的技术边界上航行（BCG 顾问实验）](roots/dellacqua-2023-jagged-technological-frontier.md) | 弱（模型复核通过） |
| [成语是哈希表而不是压缩](clips/2026-10-18-dotey-chengyu-hash-table-idea.md) | [字典编码（替换编码）](roots/dictionary-coder.md) | 弱（模型复核通过） |
| [Karpathy 的 YC 演讲：软件 3.0](clips/2026-10-18-op7418-karpathy-software-3-talk.md) | [论“自然语言编程”之愚蠢](roots/dijkstra-1979-natural-language-programming.md) | 弱（模型复核通过） |
| [用自然语言让 LLM 承担业务数据存储](clips/2026-10-18-jefferytatsuya-llm-natural-language-data-store.md) | [论“自然语言编程”之愚蠢](roots/dijkstra-1979-natural-language-programming.md) | 弱（模型复核通过） |
| [Sora 加 Vision Pro 展望](clips/2026-10-18-indigox-sora-vision-pro-immersive.md) | [体验机](roots/experience-machine.md) | 弱（模型复核通过） |
| [Claude Code 团队审代码的做法：九成代码由 AI 写，多道检查像叠起来的瑞士奶酪片，人只做机器做不好的判断](clips/2026-10-21-dotey-claude-code-review-swiss-cheese.md) | [Fagan 审查（正式代码审查）](roots/fagan-inspection.md) | 弱（模型复核通过） |
| [厂商调查：B2B 采购者 66.4% 用生成式 AI 选供应商，98% 说不知名的公司只要 AI 推荐理由扎实也会列入候选](clips/2026-10-22-probel-btob-buyers-ai-vendor-selection-survey.md) | [《品牌如何成长》（心智显著性与持续触达）](roots/how-brands-grow.md) | 弱（模型复核通过） |
| [Sam 谈我们创造的是工具还是生物](clips/2026-10-18-dotey-altman-tool-or-creature.md) | [工具性趋同](roots/instrumental-convergence.md) | 弱（模型复核通过） |
| [Agent 循环工程晚宴讨论要点](clips/2026-10-18-jerryjliu0-agent-loop-engineering-dinner.md) | [自动化的反讽](roots/ironies-of-automation.md) | 弱（模型复核通过） |
| [Samuel 的跳棋程序：机器靠自己对弈学习，下得比写它的人还好](clips/2026-10-18-samuel-machine-learning-checkers.md) | [洛夫莱斯夫人的异议（机器不能原创）](roots/lady-lovelaces-objection.md) | 弱（模型复核通过） |
| [日语学习的素读法与家庭使用整理](clips/2026-10-18-interjc-sodoku-japanese-learning.md) | [产出效应（出声读出来的词记得更牢）](roots/macleod-2010-production-effect.md) | 弱（模型复核通过） |
| [ChatGPTMac版提示词触发共享屏幕](clips/2026-10-18-dotey-chatgpt-mac-screen-share-prompt.md) | [提示科学报告 3：威胁或给小费对大模型有没有用](roots/meincke-2025-threaten-or-tip.md) | 弱（模型复核通过） |
| [Terminal-RSI：命令行 agent 拿自己验证过的成功经验反复训练自己，一轮比一轮强](clips/2026-10-18-yang-terminal-rsi-recursive-self-improving-agents.md) | [模型崩溃](roots/model-collapse.md) | 弱（模型复核通过） |
| [买两台 DGX 出租视频算力的生意](clips/2026-10-18-boxmrchen-dgx-video-compute-rental.md) | [摩尔定律](roots/moores-law.md) | 弱（模型复核通过） |
| [日本大额 B2B 采购：九成选型用生成式 AI，84.7% 至少对一家候选厂商没填表就做了调查](clips/2026-10-20-ideatech-btob-buyer-genai-purchasing-survey.md) | [线上销售线索的短命（线索响应速度研究）](roots/oldroyd-2011-short-life-online-sales-leads.md) | 弱（模型复核通过） |
| [会写代码才玩得好 vibe coding](clips/2026-10-18-aryanlabde-vibe-coding-needs-coding-skill.md) | [AI 对开发者生产率的影响：GitHub Copilot 对照实验](roots/peng-2023-copilot-developer-productivity.md) | 弱（模型复核通过） |
| [买两台 DGX 出租视频算力的生意](clips/2026-10-18-boxmrchen-dgx-video-compute-rental.md) | [完全竞争](roots/perfect-competition.md) | 弱（模型复核通过） |
| [挑战者销售：明星销售靠教给客户他没看到的问题，而不是靠关系](clips/2026-10-18-dixon-adamson-challenger-sale.md) | [SPIN 销售法](roots/rackham-1988-spin-selling.md) | 弱（模型复核通过） |
| [WorkBuddy 播客：编程不再稀缺](clips/2026-10-18-ayi-ainotes-workbuddy-podcast-ai-era-skills.md) | [理解语言模型的谄媚（迎合用户）](roots/sharma-2023-sycophancy-language-models.md) | 弱（模型复核通过） |
| [世界分成会用与不会用 ChatGPT](clips/2026-10-18-dotey-chatgpt-two-kinds-of-people.md) | [技能偏向型技术变革](roots/skill-biased-technological-change.md) | 弱（模型复核通过） |
| [日本失落年代的大赢家规律：通缩、省钱、不良资产、海外](clips/2026-10-24-towi27266777031-towi-japan-lost-decades-winners.md) | [幸存者偏差](roots/survivorship-bias.md) | 弱（模型复核通过） |
| [Claude Code 的 Task 工具原理](clips/2026-10-18-dotey-claude-code-task-subagent.md) | [别做多智能体](roots/yan-2025-dont-build-multi-agents.md) | 弱（模型复核通过） |
| [Meta 的瘦编排器模式：编排器只管路由和检查，不做领域推理，14 个专项子 agent 各管一块](clips/2026-10-20-meta-thin-orchestrator-agent-architecture.md) | [别做多智能体](roots/yan-2025-dont-build-multi-agents.md) | 弱（模型复核通过） |
| [模拟用户给 agent 开了"简单模式"：451 名真人跑完整 τ-bench，对照 31 个大模型模拟器，模拟用户太配合、打分太宽，最好的也只有 76 分（真人 93 分）](clips/2026-10-22-zhou-sim2real-gap-user-simulation.md) | [用大模型当裁判](roots/zheng-2023-llm-as-a-judge.md) | 弱（模型复核通过） |
| [Karpathy：让AI模拟专家来答](clips/2026-10-18-dotey-karpathy-simulator-not-entity.md) | [系统提示里的角色不能提升表现](roots/zheng-2023-personas-system-prompts.md) | 弱（模型复核通过） |

几组值得对照着看：
- **规模还是结构**：杨立昆、Tripo Eden 认为光靠规模不够，要有新的结构或显式保存的状态；唐杰、Sora 团队押规模继续有效，能力会自己冒出来。
- **AI 放大高手还是拉平差距**：kimi-code、vibe coding 两条说只放大高手，BCG 和 Copilot 的实验说新手受益最多。已写成原则 8（已确认）。
- **流程还要不要**：Anthropic 设计负责人说双钻石流程“基本已死”，worktree 那条说连看板都不需要了。两条都是执行变快之后，围绕新瓶颈重组流程。
- **自己练自己会不会越练越差**：模型崩溃说，拿自己生成的数据反复训练会退化；Terminal-RSI 练了两轮反而变强。区别在于每一轮只留通过外部检查的记录。和原则 1 是一回事：有能自动判对错的检查，闭环才转得起来。
- **提示词该不该写满例外**：yetone 的提示词大部分篇幅在写例外怎么处理；Anthropic 的上下文工程文章建议别塞一长串边界情况，改用几个典型例子。可能的分界：对外回复用户这类出错代价大的场合，例外要写死（原则 2）。
- **经验先提炼还是先存原样**（第 4 轮）：Harness² 和 ExpeL 在任务做完时就把经验提炼成心得，本项目的经验库也是这样做的；JitMem 认为这会过早丢掉细节，主张先存原始轨迹，等新任务来了再针对它整理（挑战 ExpeL，强）。要不要同时留一份原始记录，可以用对照试一下。
- **该不该拆成多个 agent**（第 4 轮）：Meta 的瘦编排器把领域判断全交给上下文隔离的子 agent，西奈山的实测也站在这边；Cognition《别做多智能体》说拆开会丢上下文、各自做出冲突的决定。Meta 的做法是编排器只管路由、不做判断，和原则 11 写的“要做决定的留在主线”正好相反。
- **人还有没有品味优势**（第 4 轮）：Conlon 的实验里 AI 自己设计的东西卖得更贵，消费者也不为“人做的”多付钱；《预测机器》和手工效应都预测人会占优。已写进原则 8 的矛盾。
- **模拟出来的用户靠不靠得住**（第 4 轮）：让大模型扮用户，用户太配合，同一个 agent 的成功率从对真人的 63.6% 虚高到 82%～84%（τ-bench 被 MIMESIS 实测挑战）。lukeeMind 自己就是在模拟 Luke，检验标准该是“预测他没答过的选择”，而不是“说话像不像”。
- **线索要不要马上跟进**（第 4 轮）：Oldroyd 的研究说一小时内联系，谈上决策人的可能性高得多；IDEATECH 的大额采购调查说买方希望比较推进后再被联系（弱，厂商调查）。已写进原则 13 的矛盾。
- **大模型当裁判靠不靠得住**（第 6 轮）：HarnessPro 实测大模型裁判只抓到 41.7% 的失败案例，换成可执行测试升到 83.3%（挑战“大模型当裁判”，强）；Sim2Real 论文也发现模拟用户打分一律偏宽。和原则 1 一回事：检查要能自动判对错，另一个模型的印象不算。
- **要不要一个主 agent 派活**（第 6 轮）：微软 Agensh 不设管家，1024 个 agent 靠共享工作区和 Wiki 协作，规模大了自己长出评审和整合者（挑战 Anthropic 的编排者加工人架构，强）；RLCR 只奖励整体，也长出了分工和层级。和上面“该不该拆成多个 agent”那组对照着看。
- **人在回路里还管不管用**（第 6 轮）：Mitchell 认为 agent 用得越久，人越没本事审它，人在回路里会变成摆设（挑战“人在环中”，强）。这是原则 12 的风险：放权靠证据升级，前提是人还看得懂证据。
- **反向传播是不是唯一的路**（第 6 轮）：Q Labs 只靠前向计算预训练 Transformer，小规模上验证损失超过反向传播加 Adam（挑战反向传播，强）；实验只到 2.4 亿参数，作者自己说算力效率还差几个数量级。
- **AI 之后人还有没有工作**（第 6 轮）：马斯克说有用的工作都会消失，人去“做园艺”；比较优势和 Acemoglu 的“自动化创造新任务”都说相反（都是弱，马斯克那条是推测）。

### 没找到源头的

- [李自然讲独立开发出海营销增长方法](clips/2026-10-18-yihui-indie-indie-marketing-growth-talk.md)：原文只推荐了一期播客，没写方法本身。要 Luke 贴内容
- [人大附中讲座：培养怎样的孩子](clips/2026-10-18-lubtc888-ai-era-raising-children-lecture.md)：原文只有一句提问加一个视频链接，讲座文字材料搜不到。要 Luke 贴内容
- [亿万富翁 42 分钟讲清全球经济运转](clips/2026-10-18-engmoelgaraihy-billionaire-global-economy-video.md)：原来挂的弱关系经 2026-10-21 模型复核都不成立，已删掉
- [BtoB 商材购买行为调查 2025：日本买家八成只比较 3 家以内，展会在回升](clips/2026-10-18-itcommunications-btob-buying-behavior-survey-2025.md)：原来挂的弱关系经 2026-10-21 模型复核都不成立，已删掉
- [特電法条文：违规要先被下整改命令，不服从才罚；表单营销没有官方结论](clips/2026-10-18-japan-specified-email-act.md)：原来挂的弱关系经 2026-10-21 模型复核都不成立，已删掉
- [JUAS 企業IT動向調査 2026：大企业自己定需求、外包开发，生成 AI 最怕泄密](clips/2026-10-18-juas-corporate-it-trends-survey-2026.md)：原来挂的弱关系经 2026-10-21 模型复核都不成立，已删掉
- [埃森哲式资料制作思考法总结](clips/2026-10-18-shin-yoshimura0-accenture-style-deck-thinking.md)：原来挂的弱关系经 2026-10-21 模型复核都不成立，已删掉

### 出处还没核实的

- [“大模型是冰箱，可口可乐还没出现”比喻](roots/palihapitiya-refrigeration-coca-cola-analogy.md)：只找到二手转述，两篇转述给的时间对不上
- [为 AGI 而压缩](roots/rae-2023-compression-for-agi.md)：讲座原视频没找到，只有二手整理
- [“计算机不能被问责，所以不能做管理决策”（IBM 1979 培训资料）](roots/ibm-1979-computer-accountable.md)：原件据说毁于水灾，IBM 档案馆也没找到
- [感知风险](roots/perceived-risk.md)、[意义建构方法论](roots/sense-making-methodology.md)：补课时新建，原始出处还没核实到

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

第 3 轮：
- “腾讯混元最新论文”不准：Terminal-RSI 署名是腾讯 HY Frontier 加新加坡国立大学等四所大学，通讯作者署新国立，底座用的是阿里的 Qwen3.8-27B；推文说“正式开源”，截至 2026-10-18 论文给的代码仓库打不开（见 [Terminal-RSI：两轮自重写加强化学习，27B 终端 agent 从 51.7% 涨到 86.5%](clips/2026-10-18-nft-chen-terminal-rsi-recursive-self-improvement.md)）
- 同一条推文说“证明 RSI 可稳定爬坡”：论文第 5 节自己说证明不了普遍单调提升；标题里的“51.7%→86.5%”只是四个基准里涨得最多的一个，最难的 Terminal-Bench 4.0 只到 19.84%
- GLM 5.3 那条把“对我来说是个警钟”放进引号当嘉宾原话，节目转录里说的是“对很多其他公司也是警钟”；“4.6→28.3”是智谱模型卡的自报数字（Terminal-Bench 3.0），没有第三方复现（见 [GLM 5.3 只靠后训练大涨，被 SemiAnalysis 嘉宾称为警钟](clips/2026-10-18-nft-chen-glm-5-3-post-training-wake-up-call.md)）
- “OpenAI 刚发布了一份 10 页 PDF”不对：PDF 是推文作者自己根据 OpenAI 资料整理的，6 层的名字也是他起的（见 [常驻 agent 的 6 层结构（推文作者据 OpenAI 资料自制的 PDF）](clips/2026-10-18-choopyplug1-openai-always-on-agent-six-layers.md)）
- “一个 agent 管 10 件事漂移多 2 倍”是改写：系统卡比的是连续 5 个和 10 个中间任务，越界比例 8.6%→19.7%，约 2 倍；“一个 agent 一件事”是推文作者的建议，不是 OpenAI 的结论。“16,600 次攻击 0 次得手”属实，但只是评测集结果，不是真实使用中的事故率
- Dots 长文里的 6 个权限区、4 个问题和升降阈值是作者自创，不是 OpenAI 规定；文中标为官方的“暂停不会停掉运行中的任务和定时任务”，帮助中心里没找到（见 [OpenAI Dots 放权指南：动作分进 6 个权限区，每周按证据升降](clips/2026-10-18-choopyplug1-openai-dots-agent-permission-zones.md)）
- 内地未成年人身故“不赔、只退保”不对：保监发〔2015〕90 号规定的是有上限（不满 10 岁 20 万元、10 到 17 岁 50 万元），而且只管身故、不管重疾（见 [保险建议：孩子重疾险在香港买，成人买医疗险不买重疾](clips/2026-10-18-captainlufei999-insurance-advice-hk-critical-illness.md)）
- 分红年金“第一年保费全归经纪”说过头：没有官方统计，媒体说法是经纪渠道首年佣金约为首年保费的 65%～90% 多、代理人渠道约 25%～40%；2026 年起香港要求首年最多发总佣金的 70%
- “保险避税避债都是假的”说得太绝对：香港保单要按 CRS 报给税务机关，避税不成立；但内地指定了受益人的身故金不算被保险人遗产，香港为配偶、子女投保的寿险有法定信托保护

第 4 轮（22 处，合并成下面 14 条）：
- “普林斯顿和谷歌的论文”不准：8 位作者里 6 位来自 UIUC，普林斯顿和谷歌各 1 位；“4B 模型完成率 91.5%”是在作者自建的模拟网店里、让小模型包办所有工具选择的成绩，同一批题大模型自己做是 100%（见 [agent 每步的选择题交给小决策模型（UIUC 等，推文误作普林斯顿和谷歌），模拟网店里 4B 模型完成率 91.5%](clips/2026-10-20-rohanpaul-ai-agent-decision-model-small-beats-big.md)，标题已改）
- Meta 把西奈山的研究叫“预印本”，其实 2026-03 已在 npj Health Systems 正式发表；那项研究测的是一次塞给一个 agent 很多个不同任务，和“一个任务塞太多知识”是相近、不是同一个场景（见 [Meta 的瘦编排器模式：编排器只管路由和检查，不做领域推理，14 个专项子 agent 各管一块](clips/2026-10-20-meta-thin-orchestrator-agent-architecture.md)）
- “微信是最大的办公 Agent 入口”说过头：77% 是聊天软件这个渠道里的占比，上一期报告说聊天窗口整体只是第二入口（17.9%），主要入口是桌面客户端；“73.6% 只用一个模型”没能核实，媒体转述是“近七成”（见 [网易 LobsterAI《中国办公 Agent 用户行为报告》的反直觉结论](clips/2026-10-20-vista8-lobsterai-china-office-agent-user-report.md)）
- Kairos 1 说自己是“第一个模拟个人行为的模型”有争议：Park 等 2024 年已经给 1,052 个具体的人各建了一个 agent（见 [生成式 agent 模拟 1,000 个真人](roots/park-2024-generative-agent-simulations.md)）
- 方案里“照 AIDE 挑最像的样本”和原文对不上：AIDE 第一步是到没探索过的区域分散取样，“边界上的”“可能判错的”才对得上（见 [问题协商：用户说不清想找哪类企业时，先给样本，再陪他把问题说清](clips/2026-10-19-luke-question-negotiation-icp-search.md)）
- IDEATECH 发布稿只报了“约半数不信任以优点为主的宣传”，同一题里“信任”的也是 48.5%（见 [日本 B2B 采购者：八成嫌官网都是一般论，57.1% 按“诚实”决定找谁询问](clips/2026-10-20-ideatech-btob-buyer-information-contact-survey.md)）
- IDEATECH 大额采购那份说买方“到最后阶段才报名”，同一调查的 Q5 显示 66.5% 在方案探索阶段为止就向最终厂商报过名；84.7% 是“至少对一家没填表就调查过”，不等于全程匿名（见 [日本大额 B2B 采购：九成选型用生成式 AI，84.7% 至少对一家候选厂商没填表就做了调查](clips/2026-10-20-ideatech-btob-buyer-genai-purchasing-survey.md)，标题已改）
- PROBEL 的“80.6% 有意愿”和自己的图表算不上（73.3% 或 81.4%），有效回答 659 和原始数据“559 回答”对不上；“AI 最重视外链和评价”调查里没测，而第三方评价正是它卖的东西；“坚持半年效果上升”是两组人的对比，有幸存者偏差（见 [日本 B2B 的 AI 搜索对策：77% 觉得丢了商机，一半多还没动手，卡在不会做和算不清回报](clips/2026-10-20-probel-btob-ai-search-llmo-survey.md)）
- PwC 的“日本大企业 68% 已用生成式 AI”不是导入率：样本只收在用或打算用的人，导入和未导入的比例是回收初期定的；29% 是已导入者里选“收入”的比例，不是全体（见 [PwC 调查（在用或打算用生成式 AI 的大企业部长级 487 人）：已导入者里只有 29% 说对收入有贡献，多数只感到生产率提升](clips/2026-10-20-pwc-japan-b2b-sales-genai-survey-2025.md)，标题已改）
- Aral 论文推文说的“最大三个效应”其实都是变差的（β = −0.670）；“点击率提高 2.7%”是两个估计值相乘推出来的，不是直接测的；人机搭配对团队协作感的效应校正后都不显著（见 [AI 个性化的大规模随机实验：人和 AI 的人格搭配会影响广告质量和点击率（PNAS）](clips/2026-10-20-sinan-aral-ai-personalization-pnas.md)）
- “最稀缺的是验证”是转述者加的，马斯克原推没有这句（见 [马斯克：未来的发现全是工程（“最稀缺的是验证”是转述者加的）](clips/2026-10-20-financeyf5-musk-future-discovery-is-engineering.md)，标题已改）
- Sohl-Dickstein 的演讲不在“斯坦福 HAI”，是 2026-06-12 斯坦福的物理与 AI 会议，HAI 只是发视频的频道；核心原话属实（见 [Sohl-Dickstein 在斯坦福：稳妥的路已经不稳妥](clips/2026-10-20-financeyf5-sohl-dickstein-safe-path-not-safe.md)）
- GLM-Omni 那条的“12.57% 提升到 26.86%”：12.57% 是文字对齐的成绩，比只靠画图的 14.57% 还低；“GLM-5.4/5.5 剑已出鞘”论文里没提（见 [智谱论文曝光内部统一多模态模型 GLM-Omni](clips/2026-10-20-nft-chen-zhipu-glm-omni-unified-multimodal-paper.md)）
- 麦肯锡那份不是“基于丰富研究揭示成功 CEO 的做法”，是 100 多位 CEO 自述做法的汇编，没证明这些习惯带来业绩；7,800 位 CEO 的数据属于《CEO Excellence》那本书（见 [麦肯锡报告《优秀 CEO 的行为习惯》](clips/2026-10-20-jujulife7-mckinsey-ceo-habits-report.md)）

第 6 轮：
- 量子位报道 HarnessPro 的“成本降 53%”，是均衡档在 SWE-Bench Pro 一个基准上对比 RHO 的单项数字；论文摘要里的平均数是高性能档降 26.1%（见 [HarnessPro](clips/2026-10-24-qbitai-harnesspro-pareto-rsi.md)）
- 厂商调查里“98% 说不知名公司也会列入候选”，问法带了前提“如果 AI 给的推荐理由扎实”，不等于 98% 的采购者愿意考虑不知名公司（见 [厂商调查：B2B 采购者用生成式 AI 选供应商](clips/2026-10-22-probel-btob-buyers-ai-vendor-selection-survey.md)）

第 6 轮补充核对（2026-10-24）：
- 日本失落年代那条说长银“被美国 Lone Star 等基金买下，改名新生银行”，买家写错了：买长银的是 Ripplewood 牵头的财团，Lone Star 买的是东京相和银行；“优衣库 1998 年抓住抓绒热潮”顺序也反了，热潮是优衣库自己掀起的（见 [日本失落年代的大赢家规律](clips/2026-10-24-towi27266777031-towi-japan-lost-decades-winners.md)）
- 马斯克“工作会变成园艺”那条，马斯克只说过“工作会变成可选的，像自家种菜”；“被迫退休”“劳动的定义被击碎”是转述者的推演（见 [马斯克：AI 之后工作会变成可选的](clips/2026-10-24-ayi-ainotes-musk-future-work-becomes-gardening.md)）
- 超短波那条说“10 分钟就把阿尔茨海默斑块冲刷干净、认知实质性逆转”：10 分钟见效是在健康小鼠上测的，阿尔茨海默模型小鼠要连照 7 天，Aβ 只是降低、记忆只是改善，没有人体数据（见 [超短波照射加快小鼠类淋巴清除](clips/2026-10-24-430yang-ultrashortwave-glymphatic-clearance-mice.md)）
- KnowSim 那条和真人学到的负相关的，是真人给对话打的“整体交互质量”分，不是满意度；新手组单看不显著（见 [给模拟用户装上会变的知识状态](clips/2026-10-22-lee-knowsim-user-simulators-that-learn.md)）
- Jev-Mem 的“建记忆快 6.6 倍”是和最快的对照系统比，“0.93 秒”是检索加回答的总延迟，最强的对照是同一团队去掉 Jev 的旧版（见 [Jev-Mem](clips/2026-10-22-gorden-sun-jev-mem-fast-slow-memory.md)）
- Mitchell 等论文把“系统越能干，人的技能和情境意识退化越多”安在 Bainbridge 1983 头上；原文的结论是“控制系统越先进，人的贡献可能越关键”，全文没有“情境意识”这个词（见 [人在回路里只是摆设](clips/2026-10-22-mitchell-agents-push-humans-out-of-loop.md)）

## 四、主题地图

全部新知识按主题和发布年份分布，看关注点这几年怎么变。由 `tools/topic_map.py` 生成。

<!-- topic-map:begin -->
共 1875 条新知识（含已归档）。补课找来、还没认可的 45 条不计入。数字是每年存下的条数；按发布年份算，不是保存日期。

| 主题 | 更早 | 2023 | 2024 | 2025 | 2026 | 未知 | 合计 | 观点 / 工具 / 教程 |
|---|---|---|---|---|---|---|---|---|
| Agent 与 Skill |  | 8 | 38 | 116 | 131 |  | 293 | 58 / 181 / 54 |
| 其他 |  | 25 | 32 | 47 | 95 |  | 199 | 74 / 110 / 15 |
| AI 产品与创业 |  | 18 | 32 | 43 | 92 |  | 185 | 134 / 41 / 10 |
| 视频生成 |  | 2 | 10 | 18 | 143 |  | 173 | 13 / 69 / 91 |
| 模型与本地部署 |  | 9 | 14 | 27 | 107 |  | 157 | 20 / 107 / 30 |
| 编程智能体 |  | 4 | 21 | 38 | 87 |  | 150 | 32 / 55 / 63 |
| 设计与前端 |  | 8 | 17 | 39 | 58 |  | 122 | 8 / 78 / 36 |
| 图像生成 |  | 11 | 29 | 45 | 21 |  | 106 | 1 / 62 / 43 |
| 提示词与写作 |  | 5 | 17 | 61 | 16 |  | 99 | 7 / 16 / 76 |
| 增长与获客 | 10 | 1 | 15 | 19 | 53 | 1 | 99 | 49 / 22 / 28 |
| 语音与数字人 |  | 9 | 41 | 19 | 25 |  | 94 | 0 / 83 / 11 |
| 学习与研究 | 3 | 11 | 31 | 16 | 32 |  | 93 | 28 / 32 / 33 |
| 思维与成长 |  | 6 | 12 | 8 | 30 | 1 | 57 | 56 / 1 / 0 |
| 日本 | 4 | 6 | 4 | 6 | 14 | 1 | 35 | 23 / 11 / 1 |
| 历史与冷知识 |  | 3 | 1 | 3 | 6 |  | 13 | 11 / 1 / 1 |

**每个主题的代表**（先选已溯源的，再选观点类，最后按发布时间取最新）

- **Agent 与 Skill**：[AlphaCodium 与流程工程](clips/2026-10-18-dotey-alphacodium-flow-engineering.md)、[Agent 智能体是模型能力的放大器](clips/2026-10-18-waytoagi-agent-model-capability-amplifier.md)、[ChatGPTMac版提示词触发共享屏幕](clips/2026-10-18-dotey-chatgpt-mac-screen-share-prompt.md)
- **其他**：[黄亚生预测中国模式走到尽头](clips/2026-10-18-bingliu34173809-huang-yasheng-china-model.md)、[缠论简纲思维导图](clips/2026-10-18-dtdt666-chanlun-mind-map.md)、[三旗理论：合法减税、保护资产、自由生活](clips/2026-10-18-eric-make-money-three-flags-theory.md)
- **AI 产品与创业**：[学超级个体 Jack Butcher](clips/2026-10-18-starzq-jack-butcher-solo-brand.md)、[用 PHP 套现 5400 万美元](clips/2026-10-18-imwsl90-php-jquery-54m-dollars.md)、[开 100 家便利店经验写成选址指南](clips/2026-10-18-hitw93-convenience-store-site-selection.md)
- **视频生成**：[Sora 团队伯克利课堂分享字幕翻译](clips/2026-10-18-dotey-sora-team-berkeley-talk.md)、[Tripo Eden：先建地图再渲染](clips/2026-10-18-svpino-tripo-eden-world-model-map.md)、[别再说 AI 电影，这就是电影](clips/2026-10-18-ehuanglu-ai-film-is-just-film.md)
- **模型与本地部署**：[Karpathy 谈 GPT 现状](clips/2026-10-18-dotey-karpathy-state-of-gpt.md)、[合成数据与苦涩的教训讨论](clips/2026-10-18-dotey-synthetic-data-bitter-lesson.md)、[DeepSeek R1 论文解读：自学成才之路](clips/2026-10-18-oran-ge-deepseek-r1-paper-explained.md)
- **编程智能体**：[AI 辅助编程带来的需求开发范式变化](clips/2026-10-18-dotey-ai-coding-requirements-shift.md)、[公司推广 AI 编程为何要靠内部](clips/2026-10-18-dotey-promote-ai-coding-in-company.md)、[AI 编程像人一样拆解任务的神仙项目](clips/2026-10-18-yangyi-task-breakdown-agent-project.md)
- **设计与前端**：[设计师口袋心理学 53 个知识卡片](clips/2026-10-18-hitw93-designer-pocket-psychology.md)、[Anthropic 设计负责人谈 AI 时代设计流程](clips/2026-10-18-dotey-anthropic-design-process-ai-era.md)、[学 Vercel 设计系统的逻辑](clips/2026-10-18-mengkepm-vercel-design-system-learn-logic.md)
- **图像生成**：[Qwen 生图 Turbo 开放权重](clips/2026-10-18-qwendevs-qwen-image-turbo-open-weights.md)、[Qwen 换脸换头 LoRA 更新](clips/2026-10-18-lonely-mh-qwen-image-face-swap-lora.md)、[Qwen-Image 2.1 即将开源](clips/2026-10-18-qwendevs-qwen-image-2-1-early-access.md)
- **提示词与写作**：[Anthropic专家谈提示词工程师](clips/2026-10-18-eze-is-1-anthropic-prompt-engineering-notes.md)、[提示词精髓：有什么、做什么、怎么做](clips/2026-10-18-dotey-prompt-context-task-how.md)、[写提示词的三条路与第四条路：故事](clips/2026-10-18-lijigang-prompt-writing-fourth-path-story.md)
- **增长与获客**：[采购中心和五种角色：企业买东西是一群人在组织里一起决定](clips/2026-10-18-webster-wind-organizational-buying-behavior.md)、[谢斯工业品购买者模型：几个部门一起买，冲突怎么解决决定了快慢](clips/2026-10-18-sheth-industrial-buyer-behavior.md)、[SPIN 销售法：大单靠按顺序提问让客户自己说出需求](clips/2026-10-18-rackham-spin-selling.md)
- **语音与数字人**：[Jack Dorsey 发布全双工语音模型 Dessa](clips/2026-10-24-jack-dessa-full-duplex-speech-model.md)、[Fish 开源 Drama3 语音模型](clips/2026-10-18-kay2289123-fish-audio-drama3-open-source.md)、[Griffin 全双工视频模型解读](clips/2026-10-18-maxforai-griffin-full-duplex-video-model.md)
- **学习与研究**：[Samuel 的跳棋程序：机器靠自己对弈学习，下得比写它的人还好](clips/2026-10-18-samuel-machine-learning-checkers.md)、[Taylor 1968：提问协商——四层需求（Q1～Q4）和馆员问清需求的五个过滤器](clips/2026-10-19-taylor-question-negotiation-information-seeking.md)、[AIDE：让用户给样本打"相关/不相关"，用主动学习猜出他真正想查的数据](clips/2026-10-18-dimitriadou-aide-active-learning-data-exploration.md)
- **思维与成长**：[张一鸣 66 条成长心得与延迟满足](clips/2026-10-18-sea-bitcoin-zhang-yiming-66-growth-tips.md)、[Paul Graham 谈超线性回报](clips/2026-10-18-dotey-paul-graham-superlinear-returns.md)、[一句话总结 AI 算法的含义](clips/2026-10-18-dotey-ai-algorithm-one-liner.md)
- **日本**：[稟議和根回し：日本大企业里真正拍板的是起案人和事前协商](clips/2026-10-18-vogel-japanese-organization-decision-making.md)、[今天的上市公司还在用稟議管花钱：有预算也要再走一次稟議](clips/2026-10-18-kamiyama-budgeting-and-ringi-system.md)、[经产省 DXレポート：日本 CIO 倾向选大厂、接受老供应商的提案](clips/2026-10-18-meti-dx-report-2025-digital-cliff.md)
- **历史与冷知识**：[日本稻田能否收二茬的回复](clips/2026-10-18-wangtianlaw-japan-rice-ratoon-crop.md)、[南明皇室受洗的冷知识：借调侃“历史老师去美国”说出来](clips/2026-10-18-tombkeeper-southern-ming-baptism.md)、[美国人一天生活的数据可视化](clips/2026-10-18-alexxubyte-day-in-life-americans-dataviz.md)
<!-- topic-map:end -->

## 五、补课

agent 主动去找一手材料，补框架里薄的地方，规则见 [AGENTS.md「流程四」](AGENTS.md)。补课找来的新知识在 Luke 认可之前，不计入上面的知识底座排名和主题地图。

| 题 | 简报 | 材料 | 新增源知识 | 状态 |
|---|---|---|---|---|
| 1 日本企业怎么买 B2B 产品 | [2026-10-18](docs/study/2026-10-18-topic-1-japan-b2b-buying.md) | 25 份 | 14 个，如 [采购中心](roots/buying-center.md)、[稟議制](roots/ringi-system.md)、[根回し](roots/nemawashi.md)、[许可营销](roots/permission-marketing.md) | 等 Luke 回答 |
| 4 问题协商 | [2026-10-19](docs/study/2026-10-19-topic-4-question-negotiation.md) | 21 份 | 18 个，如 [问题协商](roots/question-negotiation.md)、[知识异常状态](roots/anomalous-state-of-knowledge.md)、[偏好建构](roots/constructive-preferences.md)、[封闭世界假设](roots/closed-world-assumption.md) | 等 Luke 回答 |
| 10 日本企业找销售前先自己查什么 | [2026-10-24](docs/study/2026-10-24-topic-10-buyer-self-research.md) | 9 份 | 9 个，如 [心理抗拒理论](roots/brehm-1966-psychological-reactance.md)、[助推与赋能](roots/hertwig-2017-nudging-boosting.md)、[信号理论](roots/spence-1973-job-market-signaling.md)、[面对面接触与城市经济](roots/storper-2004-buzz-face-to-face.md) | 等 Luke 回答 |

第 1 题和已有原则的关系（草稿，待 Luke 确认）：
- 原则 10（回到一手材料）：这一题又查出 10 处误传，包括"57% 的买家联系销售前已经做好决定"和"冷电话成功率 0.3%"
- 原则 4（需求去现场取）：日本企业的采购决定多在根回し里做完，卖方从外面看不到，这正是要去现场才能取回的那类知识
- 原则 9（渠道打法看时间）：表单营销里"平时少收到营业信息的企业反应更好"，是一条弱证据
