# 第 12 轮整理 · 证据记录

> 2026-11-23。六组 subagent 各自交回的核查记录原样合并：每条读了哪些一手资料、读到哪一节、核对了哪些数字、哪些没能核实。主会话合并时改动过的地方见[本轮记录](2026-11-23-round-12.md)。

## A 组：agent 方法


2026-11-23。所有外部请求只用通用 User-Agent `weird-knowledge-research-bot`，没有带任何个人信息。

### 1. clips/2026-11-18-dotey-always-on-agent-five-parts.md

- 读了：Anthropic《Building always-on agents》全文，https://claude.com/blog/building-always-on-agents （William Hu，2026-11-13，Best practices 类，14 分钟）。还提取了正文里的链接：core loop 链到 anthropic.com/research/building-effective-agents，dreaming 链到 anthropic.com/research/components-of-agent-memory，凭据代理链到 Agent SDK 的 secure-deployment 文档
- 核对：日期、作者对。五样东西对。“一件事进收件箱才醒”“定时器让它主动”“记忆是一个文件夹”“两件事同时来”（一个收件箱只有一个 worker）“要紧的事等你拍板”（延迟工具调用）“一开始安静一点”（start quiet and earn attention）都在原文里
- 加了原文没有的：“不调用模型，也不花钱”里的“不花钱”。原文只说大部分时间在睡，没谈费用；收件箱、轮询器这些基础设施照样在跑
- 没读到：帖子附的两段视频没看

### 2. clips/2026-11-18-tekonburns-anthropic-always-on-agents-guide.md

- 读了：同一篇原文全文；企业集成模式官网的 Idempotent Receiver、Guaranteed Delivery、Polling Consumer、Competing Consumers 四页；actor 模型的英文维基
- 核对（帖子对的）：一张数据库表挡在 webhook 前面、快速确认、一个收件箱一个 worker（原文另外建议先一个用户一个收件箱，所以“每个用户一个 worker”是两句合起来的说法，没问题）、批量合并；定时器单独存表、分成一次性跟进和周期任务、轮询器投进收件箱；记忆只存查不回来的四类；密钥由外部代理注入；延迟工具调用不卡 worker
- 说重了或加了的：
  - “凌晨 3 点刷屏”是帖子自己加的，原文没提时间
  - 原文说多数 agent 有个 send 工具就够，正式发件箱只在要控制节奏或要能从错误恢复时才需要；帖子写得像必需品
  - “定期做梦”：原文是可选的（can also add）
  - “醒来只读小索引、不读每个文件”：只适用于用户笔记和任务进度，用户指令每次都全量加载
  - “Never put raw API keys”比原文的“推荐做法”（recommended pattern）语气更重
  - 漏了：auto mode（分类器审查高风险动作）、用 eval 调发消息的量
- 标题不用改

### 3. clips/2026-11-19-akshay-pachaar-google-rsi-harness-model-transfer.md

- 读了：arXiv 2611.18856 v1 的 PDF，https://arxiv.org/abs/2611.18856 ，读了摘要、第 1～5 节、Limitations、Ethics，附录 F.3–F.6，表 1–3，图 1、3、4、11。作者单位：Google Cloud AI、Google DeepMind、Google Cloud AI Research、宾夕法尼亚州立大学
- 数字核对：
  - 搬到 Gemini 后 4 个领域起点都低于 Gemini 原始 harness：对，差 0.60～5.48 分（§4.3.1）
  - 工作空间任务“约 3 倍”：起点 68.41，有 SIM 到 84.75（+16.34），没有到 73.42（+5.01），约 3.3 倍，对（图 1b、§4.3.1）
  - 10 次独立编程运行赢 9 次：对，平均多 2.36 分，95% 置信区间 [1.05, 3.68]，p=0.003（表 3、§4.4）。**但这是换题库的实验（TB2.1→TB4，模型一直是 Gemini 3.8 Flash），不是换模型**，帖子接在跨模型那句后面，容易读错
  - “同一个检查改了 4 次，两次修自己造成的死锁”：附录 F.3 原话是“edits the same gate four times, twice to repair completion deadlocks”，还把继承来的检查记成自己第一轮加的。“自己造成的”是帖子的推断，和图 11b 的改动顺序（第 5 轮加锁存，第 7 轮修锁存死锁）对得上，论文没有明说。这个案例同样是换题库的实验
  - SIM 每条记录的 4 项：对（§3.2 式 2：改动和理由、预测和实际结果、出处，即领域、题库、模型、轮次）。“测试前写下预测”：对
  - “整本账每轮都进优化器的提示词”：对（§3.2：提议者在系统提示里拿到完整 SIM，不检索也不截断；挑选者也读）
- 局限（论文自己写的）：独立重复只做了编程；其余领域每个条件跑一次；工作空间由 Gemini 3.8 Flash 当评委，可能有偏差；跨模型只有 Opus 5.5→Gemini 3.8 Flash 一对
- 帖子后半段推广 Comet Opik 的文章，和论文无关，没溯源
- 机制判断：切斯特顿的篱笆（维基原文段落，出自 1929 年《The Thing》）、架构决策记录（Nygard 2011 博文全文，原话：没有理由的人只能“blindly accept”或“blindly change”）都和“没有 SIM 时乱改看不懂的检查”是同一机制，连了，都是相近、弱。组织记忆（Walsh & Ungson 1991）这个更大的类别，没核实到它专门谈“为什么会丢”，没新建，用库里已有的“组织学习”挂在 SIM 和 ADR 下面当更底层的源头。另外 SIM 的“先写预测、再记结果”和行动后复盘（AAR）的“预期对实际”同构，连了
- 标题订正：见 out-agent.json 的 corrections

### 4. clips/2026-11-23-aiguide-notion-playbook-teams-with-ai.md

- 找到原文：Notion《A New Shape for Work》v1.0，https://www.notion.com/a-new-shape-for-work ，读了全文（目录 1.1～6.1）。页面没写日期，也没署个人作者（落款 Notion Labs, Inc.）。用 `opencli twitter search` 查到 X 上最早的讨论在 2026-11-21 00:25 UTC，所以大约是 11-20（美国时间）发布的
- 核对“一万字”：结论原话“You've just read some ten thousand words”，对
- 6 条逐条核对：
  1. 别一次性聊天，给 agent 一个共享的地方：§2.2、§2.5、§3.1，对
  2. 租模型、握上下文：§2.7 原句“Rent the intelligence. Own the context.”，对。这句口号 2026-05-17 已经是 X 上一篇同名长文的标题（按推文编号推算的日期，来自搜索结果），不是 Notion 首创
  3. skill 好，工厂更好；少数人维护、大家共用：§4.1、§4.3，对。原文说工厂可以是“一个 agent 或一组 agent”，帖子写成“一个共享 agent”，稍简化
  4. 重复、好检查、错了代价小：§5.1 列了 7 个特征（重复、可验证、流程稳定、要的是平均质量、纯数字工作、信息范围已知、错了代价不大或容易发现），原文说“至少有其中一些”，帖子只挑了 3 个。例子（客服邮件、周报、销售跟进、发票）都在原文清单里
  5. 影子运行、只起草不发送：§5.3，对
  6. 保持简单、看它坏、只修坏的：§5.2，对
  - 最简工厂：§4.6，对（原文是“five minutes or less”）
- 原手册明说点名 Adam Smith 的“专业分工和交易收益”（§1.1、§4.1、§4.2），还有单独一节讲规模经济（§4.5，固定成本、学习曲线），这几条挂成 Notion 源知识的更底层源头
- 考虑过没连的：单一事实来源。原文强调的是记忆能累积、能复利，不是“不重复存副本”，机制不完全一样，所以没连
- 标题不用改

### 5. clips/2026-11-18-theturingpost-steve-yegge-agent-software-factory.md

- 不是访谈或播客：用 `opencli twitter thread` 看了回复，这是 Turing Post 对 Yegge 在 AI Engineer 活动上演讲（2026-11-11 美国时间）的现场推文摘要。Yegge 本人 11-12 05:44 UTC 转发时说“a pretty solid summary of the key points from my talk today”
- 读了 Yegge 本人的一手资料：
  - 2026-11-14 长帖 https://x.com/Steve_Yegge/status/2121671447810888185 ：“把 AI 产出的节奏放慢到人的速度”；agent 让玩家应接不暇、让会计收到太多邮件；前五个工厂都烧掉重写了；工厂会变得非常贴合自己的业务；明年人人有 chief-of-staff agent 和一群 agent 随从（entourage）；明年几乎所有人都要和 AI 员工共事
  - 2026-11-12 回复 https://x.com/Steve_Yegge/status/2120888723009393141 ：22 个订阅约 5 千美元，再加云和 GitHub 等 5～7 千美元
  - 2026-11-11 帖子提到上一周在纽约的另一场演讲，YouTube 标题“Steve Yegge: The Future of AI-Powered Factories | Gas Town”（AI Native Dev 频道，oEmbed 核对过标题）。那是另一场演讲，视频没看
- 数字核对：每月约 1 万美元：按本人说法是 1.0～1.2 万，对得上。约 50 个 agent、每天 50～100 个功能、12～18 个月、两层分化：出自 Turing Post 的摘要，Yegge 认可了摘要，但在本人的长帖里没找到逐字的数字。每两个月烧一次工厂：本人说的是“前五个工厂都烧掉了”，频率没核实
- 杰文斯悖论：判断**不是同一机制**，没连。杰文斯说的是变省的资源自身总用量上升；Yegge 说的是 agent 变便宜后，搭配它的人（审核、消化变化）成了瓶颈、需求上升，属于互补品和约束理论。库里的 jevons-paradox 没挂这条
- 标题不用改（“50 个 agent”是摘要里的说法，本人认可了摘要）

### 6. clips/2026-11-23-john-ssuh-agent-platform-2027-endgame.md

- 读了：帖子正文和 4 张配图（作者长文的截图，下载下来看的）。配图分节：Agents as actors、Environments and computers、RBAC-ed filesystem、Separation of session and conversation、Inbox、Listeners/monitors、Workflows、Apps，以及“操作系统里的操作系统”、垂直 SaaS 论点
- **注意**：库里的原文只有正文和媒体链接。actor 模型、创新者的窘境这两条“直接源自”的依据都在配图里，正文没有，复核时要看图
- Nadella 2024：BG2 播客视频（YouTube oEmbed 核对了标题“Satya Nadella | BG2 w/ Bill Gurley & Brad Gerstner”）。原话据 CX Today 2024-12-23 的报道核对，视频没看。“SaaS 是带业务逻辑的 CRUD 数据库”在报道里是记者的转述
- 考虑过没连的：聚合理论。它靠的是分发成本归零、聚合者握住用户需求、把供给方商品化；作者的论证是“agent 能按需改应用，所以通用平台胜过垂直 SaaS”，只是结论长得像，机制不同，按“不硬连”没连
- 整条是愿景和预测，没有数据，标题不用改

### 新建的源知识（9 个）

hu-2026-building-always-on-agents、actor-model、hohpe-2003-enterprise-integration-patterns、yu-2026-self-improvement-memory、chestertons-fence、nygard-2011-architecture-decision-records、notion-2026-new-shape-for-work、pine-1998-experience-economy、nadella-2024-saas-collapse-agent-tier。都写了查过的出处链接，verified 都是 true。没通读全文的（actor 1973 年论文、EIP 全书、HBR 全文、Chesterton 扫描本、Nadella 视频）都在 dispute 里写明了。

## B 组：AI 产业与模型


查询日期：2026-11-23。所有外部请求只用通用 User-Agent `weird-knowledge-research-bot`，没带任何个人信息。

### 1. clips/2026-11-18-hilbertspaess-anthropic-roadshow-compute-efficiency.md

读了什么：
- 原推（opencli 抓到全文和 50 条回复，没有作者续推）和配图 `pbs.twimg.com/media/HXB7mp4bQAAKN3a.jpg`（看了图）
- 图上能读到的：题目「Pre-training compute multiplier over time (code)」；纵轴「Compute multiplier (log scale)」，**没有数字**；横轴「Completion month」2024-07 到 2026-10；3 个点（约 2024-07、2025-04、2026-02/03）加一个指向约 2026-09 的箭头；图注「点的位置是内部估算，仅为示意」
- 路演出处：Anthropic 路演页 ipo.anthropic.com 现在跳转到 investor.anthropic.com，页面上已无路演视频，**我没能看到视频原件**。LessWrong 帖 [trying to understand that compute multiplier graph](https://www.lesswrong.com/posts/WKt2mqJrsFuMiszed/trying-to-understand-that-compute-multiplier-graph)（作者 loops，2026-11-15）说「路演视频里有这张图」，并猜 3 个点是 Claude 3.5、Claude 4、Mythos（作者自己的猜测）。所以「图来自路演」有两个独立说法（发帖人、LessWrong），但没有一手核对
- 路演视频文字：Simon Willison [2026-11-11 帖](https://simonwillison.net/2026/Nov/11/anthropic-ipo-roadshow/) 和他用 MacWhisper 转的[文字稿 gist](https://gist.github.com/simonw/9806757fe8acec6221cb0a5cce4d720d)（只含 Tom Brown「算力」一段）：总有效算力＝物理算力 × 发现的算力乘数；4 倍乘数＝25 份算力训出原本要 100 份的模型；乘数「会叠加」；「接近递归自我改进时 Claude 能完全自己发现算力乘数」。文字稿里没有「超指数」的说法
- Epoch：[Ho 等 2024，arXiv:2403.05812](https://arxiv.org/abs/2403.05812) 摘要和第 3.1 节：所需算力约 8 个月减半（95% 区间 5～14 个月）；按 2016–2020 各年切分「没有发现明显加速的强证据」，作者说统计功效不足
- 软件智能爆炸：[Eth & Davidson 2025 PDF](https://forethought.org/research/will-ai-r-and-d-automation-cause-a-software-intelligence-explosion.pdf) 第 1、5–13、22–28 页：SIE 定义、r>1 条件、引用 Epoch 8 个月数字

核对结果：
- 「超指数」是发帖人的读法。3 个点加 1 个外推箭头、没有刻度、图注写明仅示意，撑不起这个结论；图还限定在「代码」上
- 「重训 Mythos 只需原来一小部分算力」：图上读不出具体倍数，属发帖人的推断
- 发帖人身份：二手媒体称其为前 Anthropic 研究员（egamers.io 等），没核实

### 2. clips/2026-11-18-kevinroose-amodei-big-blob-of-compute-excerpt.md

读了什么：
- 原推和回复（opencli）；短链接解析到 [Roose Substack 文章](https://kevinroose.substack.com/p/the-essay-that-started-the-ai-race)（2026-10-06）
- 节选 PDF（10 页，扫描版，转成图片逐页读了第 1–6、8、10 页，第 7、9 页没读）：标题「The Big Blob of Compute Hypothesis」；第 1 节定义；第 2 节 7 个旋钮（算力、参数、经验多少、经验分布、归一化与条件、对称性与形状、训练目标）；第 3 节证据和例子
- [Dwarkesh 播客 2026-02-13](https://www.dwarkesh.com/p/dario-amodei-2)：Amodei 本人说 2017 年写过 BBOC、列了 7 个因素、Sutton 的苦涩的教训「几年后」出来，「基本是同一个假说」（页面只读到前 10 万字，后面没读）
- [Deep Speech 2，arXiv:1512.02595](https://arxiv.org/abs/1512.02595) 摘要

核对结果：
- 确认是 Amodei 在 OpenAI 时的内部文档（Roose 说法 + Amodei 播客自述 + 节选第 1 节提到「OpenAI 安全团队现在在做的事」）
- 只公开了前 10 页（原文 25 页以上），后半关于安全的论证没公开；Roose 没说怎么拿到，Amodei 不予评论
- 写作时间：节选引用了 2017 年的 RLHF 论文；Amodei 回忆「GPT-1 刚出来」，GPT-1 是 2018 年 6 月（维基），和「2017」有出入
- 节选脚注 1 明说 Deep Speech 2 是他在 AI 的第一份工作、培养了 BBOC 直觉 → Deep Speech 2 记为 BBOC 的直接源头
- 时间顺序：BBOC（2017）早于苦涩的教训（2019-03）和 Kaplan 规模定律（2020-01），与 Hestness 等（2017-12）同期，所以三者都只记「相近」
- 「GPT-2 是检验这个假说的实验」「开启了 AI 竞赛」是 Roose 的说法，节选里没有提 GPT-2
- 节选文末 Amodei 明说这不等于「把现有算法放大就能到 AGI」

### 3. clips/2026-11-18-sujinyan6-why-ai-data-business-booms.md

读了什么：
- 库里的全文（X 长文，读完）。没去抓英文 Substack 版
- 作者提到「Mistral Large 4 技术报告写后训练环境、任务、参考答案和 verifier 主要是 agent 自己搭的」：查了 Mistral 的 [Large 4 开源公告](https://mistral.ai/news/mistral-large-4-oss/)，页面没有这句话；技术报告链接在 alphaxiv，**没读到原文，这句未核实**
- 源知识出处：Burt《Structural Holes》（Crossref 查到 Harvard UP 1992，DOI 10.4159/9780674029095，维基摘要）；囚徒困境（[斯坦福哲学百科](https://plato.stanford.edu/entries/prisoner-dilemma/)、维基）

核对结果：
- 文章是作者个人见闻和判断，没有数据。小红书批评帖、深圳活动、创始人偷数据、「模型厂买到自己的数据」都是转述或传闻，没法核实
- 曾考虑「预算拨了就要花完」（Liebman & Mahoney 2017 AER，DOI 10.1257/aer.20131296，期末最后一周采购是平时的 4.9 倍）；但作者没说预算会过期，机制对不上，没连

### 4. clips/2026-11-23-rohanpaul-ai-nvidia-reasoning-to-cpu-code.md

读了什么：
- 原推（opencli）和配图（就是论文首页）
- 论文 [arXiv:2611.09891](https://arxiv.org/abs/2611.09891) PDF 全文 28 页转文字：摘要、第 1 节、第 2.2 节（构建与调用）、第 3.1–3.6 节、表 2、附录 C 表 3–6

数字核对（都对得上）：
| 推文说法 | 原文 | 出处 |
|---|---|---|
| 便宜 16～291 倍 | 16× 到 291×（GSM8K 16.3，AIME ’25 291.1） | 摘要、表 2、第 3.6 节 |
| AIME ’25 93.3% 对 83.3% | CAcc 93.3，SAcc 83.3 | 表 2、第 3.6 节 |
| 8 个里 7 个不低于原模型 | 唯一例外 GSM8K 98.0 对 98.5 | 第 3.6 节 |
| 改写题至少 90% | 最低 90.8%（AIME ’26 组合扰动） | 第 3.6 节 |
| Opus 4.5 改写、1B 模型做小活 | 源模型和构建模型都是 Opus 4.5；目标模型先用 Haiku 4.5，后换微调的 Llama 3.2 1B | 第 3.4 节 |

推文没说的：
- 构建一次要花原模型 12～84 倍；AIME 约 13 次、GSM8K 约 90 次调用才回本（第 3.6 节）
- 构建时根函数要对照原推理和**金标答案**检查（第 2.2.1 节），所以「缓存比原模型准」不全是代码执行更稳的功劳
- 改写题的标准答案由 Opus 4.5 生成、2 个 Opus 评委一致通过（第 3.2、3.4 节），没有人工核对；扰动测试只在缓存已答对的题上做
- 论文没写每个测试用了多少题；AIME 百分比推算是 30 题里差 3 题（推算）
- 记忆化、EBL 的出处查了 Crossref：Michie 1968 Nature 218:19–22（DOI 10.1038/218019a0）；Mitchell 等 1986 Machine Learning 1(1):47–80；DeJong & Mooney 1986 Machine Learning 1(2):145–176。STRIPS 宏操作是 EBL 前身的说法没逐一核实原文

### 5. clips/2026-11-18-simonhoiberg-private-benchmark-fine-tuned-qwen.md

读了什么：
- 原推和作者回复（opencli）。作者回复：「Qwen 3.8 27B（8 bit），在它被训练的特定工作上接近 Opus 5.5，不是通用模型」；「只分享方法，不分享模型」
- 附带视频没看
- 网上搜作者的私有测试集细节：**没找到任何公开的题数、指标、对照**
- 同作者上一条（2026-11-11）的溯源已读：LoRA + 教师生成案例
- [GSM1k，arXiv:2405.00332](https://arxiv.org/abs/2405.00332)：v4 摘要「最多掉 8%」，v1 摘要「最多掉 13%」；正文 1205 题；第 1 节「暂不公开以防污染」

核对结果：
- 「追平 GPT-6 和 Opus 5.5」是作者自述，且他自己限定在训练过的任务上；没有可核对的测试细节

### 6. clips/2026-11-18-tynric-carter-claude-code-system-prompt-leak.md

读了什么：
- 原推（opencli），短链接解析到 [CL4R1T4S/ANTHROPIC/CLAUDE-CODE-FABLE-5.2.txt](https://github.com/elder-plinius/CL4R1T4S/blob/main/ANTHROPIC/CLAUDE-CODE-FABLE-5.2.txt)
- 用 GitHub API 查了仓库和文件提交记录，下载了提交 84cd1bf9 的文件本身，用脚本数行数、字数、工具和技能
- Fable 5.2 发布日期：[9to5Mac 2026-11-09](https://9to5mac.com/2026/11/09/anthropic-upgrades-claude-with-new-fable-5-2-model-details-here/) 等

数字核对：
| 推文说法 | 查到的 | 结论 |
|---|---|---|
| Fable 5.2 11 月 9 号发布 | 多家媒体 2026-11-09 | 对 |
| 11 月 10 号挂上 GitHub | 提交时间 2026-11-09 21:02 UTC（中国、日本时间是 10 号） | 按东亚时间对 |
| 7832 行 | 7832 行 | 对 |
| 95 万字符 | 953,659 字符（957,315 字节） | 对 |
| 128 个工具 | 不重复的工具名 129 个（`<function>` 定义 131 处，其中系统提示部分 68 处，其余在 ToolSearch 等返回里） | 约等于 |
| 44 个技能 | 44 个 `SKILL.md` 文件 | 对 |
| 仓库五万多星、作者 Pliny | 53,753 星，作者 elder-plinius | 对 |
| 「完整系统提示词，一个字没漏」 | 文件是拼起来的：系统提示部分只有约 1161 行（约 33 万字符），其余是示例对话、工具返回、44 个技能文件；还有 `{PROFILE_REDACTED}` 等脱敏占位 | 夸大 |
| 「给它塞了隐藏输入，它能说自己什么都没看见」 | 只找到「不要提到记忆快照送达或变化」「不要说明这一步」「没结果就不提搜过」之类的不叙述指令，没找到被问时否认看见的写法 | 夸大，未找到原样说法 |

没能核实：
- 文件真伪。Anthropic 没有确认；文件看起来是 claude.ai 上跑 Claude Code 外壳的环境（Linux `/home/claude`、claude_ai 和 widgets 工具），不一定等于本地 Claude Code CLI 的提示词

## C 组：产品与增长


2026-11-23。四条都读了库里的全文；X 帖子用 `opencli twitter thread` 重新抓过，看了续推和评论。外部请求里没带任何个人信息。

### 1. clips/2026-11-19-whereisvivien-manus-zhang-tao-pku-ai-product-talk.md

**读了什么**

- 库里的逐字稿全文（1.1～1.11 节，约 1.5 万字），读完
- 季逸超博文 Context Engineering for AI Agents: Lessons from Building Manus（2025-07-18）开头：https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus 。原句是「模型进步是涨潮，Manus 要做船，不做钉在海底的柱子」，讲的是选上下文工程、不自训模型
- Manus 官网 about 页：https://manus.im/about ，标语 "Hands on AI. Less structure, more intelligence."；南华早报 2025-03 的报道标题也用了这句：https://www.scmp.com/tech/tech-trends/article/3301969/ （403，没读到正文，日期按文章编号推断）
- Sutton《The Bitter Lesson》：库里已有 `bitter-lesson`
- Nielsen《The Articulation Barrier》（2023-05-24，2025-04 更新）：https://jakobnielsenphd.substack.com/p/prompt-driven-ai-ux-hurts-usability （通过搜索摘要核对了论点和 20%、10%、一半人这几个他自估的比例）
- Gourville 2006 HBR：https://hbr.org/2006/06/eager-sellers-and-stony-buyers-understanding-the-psychology-of-new-product-adoption （正文付费，只读到开头）；HBR Store 商品页读到了「九比一错配」「用户高估自己已有的东西、高管高估自己的创新」「四象限」
- Buell & Norton 2011 劳动错觉：IDEAS 摘要页 https://ideas.repec.org/a/inm/ormnsc/v57y2011i9p1564-1579.html ，Crossref 确认 DOI 10.1287/mnsc.1110.1376、卷期页码
- Lee & See 2004：库里已有；想核对它设计建议里「展示自动化的过程和中间结果」的原话，PDF 两个来源都下不下来，**原话没核实**，why 里只写了论文公认的「表现、过程、目的」三分法
- 时间核对：Claude 3.7 Sonnet 2025-02-24 发布（Anthropic 公告、TechCrunch），Manus 2025-03-06 发布、靠邀请码（多家媒体报道，合伙人说是服务器容量不够），和逐字稿 1.6、1.9.1 节一致

**核对**

- 逐字稿把 "Less structure, more intelligence" 归给首席科学家（1.6 节），和 Manus 官网标语对得上
- 「产品能随着模型能力上升而水涨船高」（1.6 节）和季逸超博文的涨潮比喻几乎一样，但博文讲的是不训练自己的模型，逐字稿讲的是不写死工作流；why 里写明了
- 1.2 节小标题本身就点了沉没成本

**没能核实（都是张涛自述）**

- 4 月 ARR「超过 4000 万、接近 5000 万」（1.7 节，没写币种）
- Agent 和 Chatbot 单个 DAU 的 token 消耗差 200～1000 倍、上线三天需求约 800M TPM、高峰一天花 50 万美元（1.9.1 节）
- 「Anthropic 不相信只用了他们的模型」「Claude Code 泄露代码里有我们早期架构的影子」（1.5 节）
- 400 多个任务的评测集、核心用户每月花 4000～5000 美元

**没连的**：免费补贴是陷阱（和库里 `freemium` 相关，但不是核心主张）、通用定位占心智（像 Ries 与 Trout 的定位理论，库里没有，没新建）、全球化视野。都不是这篇最核心的主张，没硬连。

### 2. clips/2026-11-19-tonychuhai-manus-quit-ai-browser-less-structure.md

**读了什么**：库里原文；`opencli twitter thread` 抓了原推和评论，原推引用的就是第 1 条的逐字稿 X 长文（whereisvivien/status/2123103532182282353）。

**转述和逐字稿逐句对照**

| 转述 | 逐字稿 | 判断 |
|---|---|---|
| 2024 年 10 月前在做 AI 浏览器，家人朋友问 Safari、Chrome 的功能去哪找，于是停了 | 1.2 节同样内容；另外还有一条原因：怕团队耗掉 3～6 个月 | 对，略了第二条原因 |
| 北京只有五个人的团队 | 1.3 节「北京团队特别小……一共五个人」；当时全公司 30 人（1.2 节） | 对。评论里有人以为 5 个人做浏览器，Tony 回复「是 30 个人，那 5 个人是开始做 Manus」 |
| Claude 3.5 Sonnet 能力不只编程，能长程规划和工具调用 | 1.3 节 | 对 |
| 展示执行过程和会话回放是为了让非技术用户相信 | 1.4 节 | 对 |
| Claude 3.7 发布当晚没改外壳代码、只换模型接口，评测里原本没解决的问题大约 20%～30% 通了 | 1.6 节：「Harness 一行代码都没改，只把模型接口从 3.5 V2 切到 3.7……剩余未解决的问题里，大约有 20% 到 30% 一下就解决了」 | 对，一字不差的意思。注意 20%～30% 是「剩下没解决的那部分」里解决的比例，不是总分涨了 20%～30%，转述没说错 |
| Less structure, more intelligence | 1.6 节，出自首席科学家 | 对 |

**问题在标题**：库里标题「为什么放弃 AI 浏览器：少写死结构、多留给模型」把两件事连成了因果，已在 corrections 里给新标题。

### 3. clips/2026-11-18-coldemailchris-stop-ai-personalized-first-lines.md

**读了什么**

- 原推和评论（`opencli twitter thread`）。作者 Christian 的简介：Pipeline（@Pipeline_tech）创始人兼 CEO，做 B2B 的「AI 原生外呼系统」，另外教 GTM 课程
- 推文说的「article below」：推文引用的是同公司 Jacob Breton 的 X 长文《The Complete Guide To Personalization In Cold Email》（2026-11-16 21:05 UTC，比推文早约两小时），`opencli twitter article` 抓到全文，读完：https://x.com/itsjacobbreton/status/2122435991973532013 。Breton 的简介：Pipeline 的 GTM 运营，「经我搭的系统发出 1700 万封以上冷邮件」
- Sahni、Wheeler、Chintagunta 2018（Marketing Science 37(2)）：IDEAS 摘要页、Crossref、Chicago Booth Review 报道
- Defau & Zauner 2023（Marketing Letters 34(4): 727–733）：IDEAS 摘要页，Crossref 没查（DOI 从 Springer 链接确认）

**这家厂商卖什么**：Pipeline 卖 B2B 冷邮件外包（「替你建一支内部 GTM 团队」，私信 PERSONAL 或约电话）和 GTM 课程。长文自称为 100 多家 B2B 公司带来 3 万多条线索、1 亿美元以上的商机。

**数字核对（长文「What our data says」一节）**

| 说法 | 原文 | 缺什么 |
|---|---|---|
| AI 写的个性化开头回复率 0.27% | 有，原样 | 没给发了多少封、哪个行业、什么时间 |
| 只带名字变量 10%+ | 有，原样 | 同上；没说两组是不是同一份名单、同一个报价。评论区两个人追问「是不是同一份名单」，作者没回 |
| 同一工作区 4,055 份脚本、1,160 个活动里，用了 {PROJECT} 和 {LOCATION} 的那个活动回复率 14.5%，同脚本普通版平均 1%～3% | 有 | 只有 1 个活动 |

**对不上的地方（同一篇长文里）**

- 一边说只带名字的 10%+，一边说同一脚本的普通版平均 1%～3%、「只用 {FIRST_NAME} 几乎没用」
- 长文自己列的常见错误之一是「按回复率而不是按每条线索要联系多少人来评判个性化测试」，但标题数字用的正是回复率
- 推文和长文都没有统计检验。0.27% 和 10% 差了约 37 倍，评论里也有做行为科学的人说「差 50 倍说明那些开头本身出了问题」

**结论**：主张的方向（AI 套话开头没用，相关性靠名单和报价）有独立研究可以对照：Defau & Zauner 2023 发现连「标题写名字」都已经复现不出效果，作者推测是用的人太多、收件人习惯了。但 0.27% 对 10% 这组数只能当厂商自述，不能当实测结论引用。

**没连的**：信号理论（Spence）。AI 让个性化开头变便宜、不再显得用心，机制上说得通，但原文没讲成本，有 Defau 的实证就够了，没硬连。

### 4. clips/2026-11-22-howtoprompt-colgate-llm-synthetic-consumer-ssr.md

**读了什么**

- 论文 arXiv 摘要页 https://arxiv.org/abs/2510.08338 （v1 2025-10-09，v3 2025-10-27）和 HTML 全文 v3 https://arxiv.org/html/2510.08338v3 ：读了第 3.1、3.3、3.4、4.1～4.4、5 节和附录 A.1、A.3、E。PDF 下载了，但本机没有 PDF 转文字工具，改读 HTML
- Argyle 等 2023：arXiv 2209.06899 摘要页；Crossref 确认 Political Analysis 31(3): 337–351，DOI 10.1017/pan.2023.2，被引 815 次（Crossref，2026-11-23）
- Brand、Israeli、Ngwe：MSI 工作论文页（Report 25-136，2025-11-12）读到了结论；HBS 工作论文 23-062 的 PDF 链接来自搜索，没打开；SSRN 页 403
- 帖子的评论区（`opencli twitter thread`）

**数字核对**

| 帖子说 | 论文 | 判断 |
|---|---|---|
| 高露洁发的论文 | 9 位作者，7 位 PyMC Labs，2 位 Colgate-Palmolive；数据「由一家领先的个护公司提供」，没点名（附录 A.1） | 不准，标题已建议改 |
| 57 个真实个护产品调查 | 57 个个护新品概念调查，美国受访者，概念是假想的新品（第 3.1 节、附录 A.1） | 对 |
| 9,300 个真人回答 | 摘要写 9,300 responses，附录 A.1 写 9,300 名不同的受访者，每个调查 150～400 人 | 对 |
| 达到真人重测信度的 90% | 「相关达成率」ρ = 合成和真人平均购买意向的相关 ÷ 真人拆半重测的相关；GPT-4o 配图片 ρ = 90.2%（表 1） | 数对，但它是 57 个概念平均分的排序相关，不是逐人预测（第 3.3 节） |
| 直接打 1～5 分会给中庸的分数 | 直接打分几乎全是 3 分，分布相似度 K 只有 0.26～0.39（第 4.1 节） | 对 |
| 「完美」复现不同年龄、收入人群对价格变化的反应 | 年龄、收入、价格档位复现得「还不错」，Gemini 的年龄曲线就没对上；性别、地区、族裔复现得不好（第 4.3、5 节） | 夸大 |
| 定性反馈比真人更深入、更挑剔 | 文字「信息丰富得多」，合成顾客「很少憋着不批评」（第 4.4 节、附录 E），只举了例子，没有系统编码对比 | 方向有，证据弱 |
| 杀死整个市场调研行业、悄悄的、没人谈论 | 作者在第 5 节说「不是对真人调研的全面替代」，建议先用合成样本筛概念、把真人小组留给最有希望的；论文 2025-10 就发了，评论区也有人说「你晚了一年」 | 夸大 |

**另外看到的**：KS 相似度「>0.85」只对 GPT-4o 成立（0.88），Gemini 2.0 Flash 是 0.80；去掉人口属性后分布更像（K = 0.91），排序相关却从约 92% 掉到约 50%；参考语句是在这 57 个调查上手工调过的，换领域效果未知。致谢里写了用 ChatGPT-5 改写文字。

**没能核实**：帖子配图（pbs.twimg.com 那张）没看；Brand 等工作论文的具体数字（如含氟牙膏的支付意愿）只在搜索摘要里看到，没写进 roots。

## D1 组：黎曼猜想与 GSI


查询日期 2026-11-23。外部请求只用通用 UA `weird-knowledge-research-bot`，没带任何个人信息。

### 1. leanprover：Lean FRO 和 Mathlib 的联合声明

**读了什么**

- 推文全文（opencli 抓到，t.co 展开后指向声明）：https://x.com/leanprover/status/2124159121645801562
- 声明全文：https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ （2026-11-21 13:55，署名“Lean and Mathlib communities”，Lean FRO 和 Mathlib Initiative 背书）
- Alpöge 公告 remark.pdf 全 4 页：https://alpo.ge/remark.pdf
- 声明引用的 Buzzard 博文全文：https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/
- 声明引用的 Sutherland 核验页全文：https://math.mit.edu/~drew/grh/
- Mathlib 的 RiemannHypothesis 定义：https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html#RiemannHypothesis
- 源码镜像：https://github.com/Deicyde/riemann-hypothesis （只确认存在，没读代码）

**声明到底认证了什么**（逐条对照 Buzzard 的四个问题）

| 问题 | 声明怎么回答 |
|---|---|
| 陈述对不对 | 用的是 Mathlib 里已有的 RiemannHypothesis 定义，“由 Lean 和数论专家仔细审过”。定义本身：ζ(s)=0、s 不是 -2(n+1)、s≠1 ⇒ Re s=1/2（s≠1 是因为 Mathlib 在极点处给了约定值） |
| 能不能编译 | 几十人报告编译成功、复现出同一个导出文件，零错误 |
| 证明的是不是这条陈述 | 社区另写了一个只导入 Mathlib 的陈述文件，用 comparator 和 con-leche --compare 两个独立工具比对，确认一致 |
| 内核有没有被钻漏洞 | 导出的证明被 Lean 官方内核、con-leche、con-ron 和几个第三方用不同语言写的检查器接受；con-leche、con-ron 带有“相对集合论不会接受假证明”的形式化证明；检查在“惰性”导出文件上跑，碰不到源码里可能的恶意代码 |

**公理**：Sutherland 页 `#print axioms` 结果，五个主定理只依赖 propext、Classical.choice、Quot.sound 三条标准公理；环境里的 15 条公理全在 Lean 核心 Init 里。

**范围**：Sutherland 页写明“GRH”只指狄利克雷 L 函数（所有模、所有特征），戴德金 ζ、赫克 L 函数等不在检查范围内。

**核对的数字**：1700 万行（声明原文“17 million lines of code”）；11 月 20 日发布（声明、remark.pdf 一致）；Sutherland 页：175,187 个模块、导出文件 61,570,595,788 字节、nanoda 80 线程 27 分 42 秒。

**没核实的**：声明里的 Zulip 讨论串（要登录，没读）；没自己跑任何 Lean 检查；remark.pdf 本身没写行数。

### 2. dotey：5 分钟讲清 Claude 参与证明黎曼猜想

**读了什么**

- 推文文字（库里原文）。视频本身没看，只核对了推文里的说法。t.co 链接展开是视频制作工具仓库 https://github.com/JimLiu/open-artifact ，与事实核对无关
- remark.pdf、Lean 声明（同上）
- Vakil 博文全文：https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/
- Baez 博文：https://johncarlosbaez.wordpress.com/2026/11/22/masullo-on-the-riemann-hypothesis/
- TechCrunch 2026-11-20：https://techcrunch.com/2026/11/20/ai-claimed-a-solution-to-the-167-year-old-riemann-hypothesis-and-a-human-did-too/
- The Decoder：https://the-decoder.com/hours-after-anthropic-claims-a-claude-proof-of-the-riemann-hypothesis-stanford-releases-an-all-human-competing-draft/
- 维基百科 Riemann hypothesis 的 Alpöge 一节：https://en.wikipedia.org/wiki/Riemann_hypothesis

**逐条核对**

| 推文说法 | 结果 | 依据 |
|---|---|---|
| 11 月 20 日 | 对 | remark.pdf、Lean 声明、维基百科 |
| Anthropic 的数学家 | 对 | TechCrunch 写他的雇主是 Anthropic；维基百科同 |
| 1700 万行 Lean 代码 | 对 | Lean 声明；Baez、Rubinstein 讲解稿同 |
| 斯坦福同一天放出纯人工证明草稿 | 对 | Vakil（斯坦福教授、美国数学会主席）11-20 贴出 Masullo 的 GRH 草稿，原话“It is all human, with no AI” |
| 几小时后有人借助 AI 报告了问题 | 对 | Vakil 原帖“About 8 hours later I updated: Several people have contacted me to report problems ... identified with the assistance of different AI models” |
| 人写的正在大改 | 对 | Vakil：草稿“mid-revision”；Baez 转述 Conrad 对《科学美国人》说正在大改，第 13 章还只有占位 |
| 160 多年 | 对 | 1859 年到 2026 年约 167 年 |

**没核实的**：视频里关于“银行加密会不会失效”等讲解内容没看；Masullo 是否“斯坦福博士后”只见 TechCrunch，Vakil 原帖没写。

### 3. RachelRifx：帖子称零报错、无人能懂

**读了什么**：同第 1、2 条，另读了 Rubinstein 主导的讲解稿前 2 页：https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper.pdf （164 页，2026-11-21 工作稿，署名“Claude Fable 5.2、Codex Astra 6.2、Gemini Carbon，应 Michael O. Rubinstein 之请”）

**逐条核对**

| 帖子说法 | 结果 | 依据 |
|---|---|---|
| 麻省理工正式确认 | 不对 | 没找到 MIT 机构声明。对应的是 MIT 数学家 Andrew Sutherland 的个人核验页（检查用 Claude Code 跑），TechCrunch 也只说他确认能编译 |
| Lean 官方正式确认 | 基本对 | 是 Lean 与 Mathlib 社区的联合声明，Lean FRO 和 Mathlib Initiative 背书 |
| 0 报错 | 对 | 声明“compiles without errors or build failures”；Sutherland 页“zero errors” |
| 100% 通过最严苛验证 | 说早了 | 帖子发于 11-22 01:53 UTC；Sutherland 页到 11-22 16:20 UTC 仍有两项在跑（Lean 官方内核复查完整导出、lake comparator 端到端），不过各模块已逐个通过 Lean 内核，其他独立检查器都通过 |
| Claude 写出的 | 不准确 | Alpöge 原话“working with Claude”“Claude and I have also formalized” |
| 困扰人类 160 年 | 对 | 约 167 年 |
| 全地球没有一个人类能看懂 | 夸大，无出处 | Alpöge 自述“还没吃透周边的大片数学”，不发 25 万页“不可读”文字稿；Lean 声明说期待数学界解释新思路；维基百科记为“尚未被数学家完全理解”，Radziwiłł 指出缺少人类理解；但 11-21 已有 Rubinstein 讲解稿把 ζ 函数情形的部分论证写成人类可读（核心不等式 (M) 仍取自 Lean，没写出），陶哲轩做了初步评论（据维基百科，没读原文） |

### 4. gntalktalk：GSI 只做 harness、250 项突破

**读了什么**

- 推文和回复串（opencli）：https://x.com/gntalktalk/status/2124382319113068963 。GSI 联合创始人 Yashraj Shukla 在下面回复：与其说是 harness，不如说是“元求解器平台（Meta-Solver Platform）”；原作者回“谢谢纠正”
- 创始人发布推文：https://x.com/whynesspower/status/2122315968890474517 （2026-11-16，“250+ novel discoveries and breakthroughs across eight domains”）
- GSI 首页、研究页、方法页、愿景页、联系页：https://generalised.si/ 、/research 、/approach 、/vision 、/contact
- GSI 单篇说明：阿达玛矩阵 /research/hadamard-matrices、循环差集 /research/cyclic-difference-set-465、Two-Gross /research/two-gross-circuit-distance、超导上限 /research/superconducting-tc-ceiling
- 独立综述 Egan、Kotsireas、London、Ó Catháin，arXiv:2610.27175 v2（摘要页和 HTML 正文第 4 节相关段落）：https://arxiv.org/abs/2610.27175

**逐条核对**

| 帖子说法 | 结果 | GSI 原文 / 外部依据 |
|---|---|---|
| 核心班底两个人 | 对 | 愿景页“two people”，联系页列两位联合创始人 |
| 成立仅一个月 | 没核实 | 网站没写成立日期；GSI 的阿达玛提交最早在 2026-10-11 |
| 八大领域 250 多项突破 | 自述 | 出自创始人推文；研究页写“All 112 results here”，首页写“六个领域” |
| 只做了个 harness | 被当事人纠正 | 见上，创始人说是元求解器平台 |
| 五六分钟现场编译出专用求解器 | 说过头 | 方法页“五到六分钟做出验证过的求解器”；研究页注明是两道实验室自己选的题、求解器是重写已发表方法（4 分 46 秒、5 分 55 秒），“自动生成求解器尚未证明”，类别识别盲测 8 个对 5 个 |
| 快数百甚至三万倍 | 自测 | 方法页“Williamson 和 Legendre 问题上比 Kissat、CP-SAT 快三万倍以上”；SAT XOR 实例几何平均至少 341.6 倍；都是自己测的 |
| 每一项都附证书 | 不实 | 研究页多处自注“without a certificate”“lower bound is not released”“Method: Not published” |
| 200 多个阿达玛矩阵，最高 2148 阶 | 数量对，“最高”错 | 200 多个含普通、斜、对称三类；未解阶数做到 11804，斜阿达玛到 14384；2148 只是配图那个 |
| 搜索空间 8.3×10^123 的循环差集无解 | 数字对，有保留 | C(465,145)≈8.32×10^123（自己算过）；GSI 写“据我们所知首个完整证明”，但依赖未重证的已发表结果，“实验室外无人审过” |
| 补全半个世纪的数学证明，0.1827 | 数字对，优先权错 | C∞≈0.182726…；上限 Allen 与 Dynes 1975 年就提出，Kondratev 2026-09-19 先发完整证明，GSI 做的是推广；是线性化 Eliashberg 理论在 μ*=0 下的严格上限，不是“经验公式常数” |
| 审计出约 12.5% 非物理数据 | 基本对 | Alexandria 数据库里“选出的谱约 12.5% 有负值瓣（3,409 条）” |
| Two-Gross 抗噪底线 16 个量子比特 | 单位错，优先权错 | 16 是电路距离（最少多少个故障能骗过检测），不是量子比特数；上界 Crocker 10-21 先给，精确值 Cheng、Guo、Pan 11-05 先报；GSI 的下界计算未公开 |
| 芯片布局“最短连线物理极限” | 说过头 | 给的是带证书的线长下界，只到已知最好布局的 0.338～0.604，不是极限 |

**独立验证**：只查到一处。Egan 等综述 v2 写明“we checked each of their matrices by computing HHᵀ exactly”，并点名 Kumar 的 2148、2284、2636、3964 阶。其余结果都是 GSI 自述，多数自注“实验室外无人审过”。

### 新建源知识的出处核查

| slug | 核查到的原始出处 |
|---|---|
| riemann-hypothesis | 黎曼 1859 原文转录（都柏林三一学院）、克雷研究所页、维基百科、Mathlib 定义 |
| alpoge-2026-rh-lean-proof | remark.pdf 全文、alpo.ge 压缩包第 1 部分可访问（HTTP 200）、Deicyde 镜像 |
| lean-mathlib-2026-rh-verification-statement | 声明原页全文 |
| sutherland-2026-rh-lean-verification-files | 核验页原页全文 |
| buzzard-2026-checked-in-lean | 博文原页全文；作者归属按博客和文中自述推断 |
| de-bruijn-criterion | 维基百科；Barendregt 与 Wiedijk 2005 的 DOI（Crossref 确认）；Paulson 博文引用的定义原文。论文全文没读到（出版社 403） |
| stepanov-method | 维基百科 Stepanov 词条；Bombieri 1973 Bourbaki 报告（Crossref 确认 DOI）；Alpöge remark 原话。Stepanov 1969 原文没读 |
| vakil-2026-masullo-grh-announcement | Vakil 原帖全文；Baez 博文 |
| gsi-2026-meta-solver-research-log | GSI 各页原文；创始人推文；Egan 等 arXiv 正文 |
| mcconnell-2011-certifying-algorithms | Crossref 确认 DOI；作者主页预印本第 1 页摘要原文 |
| crawford-1996-symmetry-breaking-predicates | DBLP、OpenAlex 记录（被引 558）、IJCAI 2003 后续论文页。原文全文没读到，内容依据记录和后续文献的描述 |

## D2 组：神经元与推理


整理于 2026-11-23。外部请求只用通用 User-Agent `weird-knowledge-research-bot`，没带任何个人信息。PDF 下到会话临时目录里读，没进仓库。

### 1. clips/2026-11-18-dotey-four-neurons-learn-to-chase-light.md

**读了什么**

- 推文串（`opencli twitter thread`）：宝玉只有这一条，其余 30 条是别人的回复（有一条回复提到 Braitenberg 1984）。视频没看
- 原文 Myriad 第二章《Watch a Brain Learn》，https://aatishb.com/myriad/how-brains-learn/（t.co 短链跳到这里），页面元数据写发布日 2026-11-13。读了全文，包括附录 How the spark moves、How the spark learns
- 原文链出的一手资料，用 Crossref / Europe PMC 核对了题目和摘要：
  - Williams 1992 REINFORCE，Machine Learning 8:229–256，https://doi.org/10.1007/BF00992696
  - Kasdin 等 2025，Nature 641:699–706，https://doi.org/10.1038/s41586-025-08729-1（读了摘要；参考文献里有 Schultz 1997）
  - Böhner 1990，Animal Behaviour 39:369–374（原文“没有老师也能学会”这句的出处）；Ölveczky 等 2005 PLoS Biol（“随机试变奏”这句的出处）
  - 权重扰动：Züge 等 2023，Physical Review X 13:021006
  - 演化策略：OpenAI 2017（库里已有 salimans-2017-evolution-strategies）
- 布赖滕贝格：英文维基百科词条；Stefik 1985 年在 Artificial Intelligence 上的书评（https://doi.org/10.1016/0004-3702(85)90057-8）确认这本书存在。MIT Press 页面拒绝了机器访问，没读到
- Schultz、Dayan、Montague 1997，Science 275:1593（Crossref 加摘要）；Montague、Dayan、Sejnowski 1996（Crossref）用来写争议

**核对的数字**

| 推文说法 | 核对结果 |
|---|---|
| 四个神经元、三个数字 | 对。两只眼、两个鳍；三个数是同侧连接、交叉连接、驱动力 |
| 两千多种接法里不到 2% 是好答案 | **原文正文没有这句话**，正文只说“只有很小一部分”。这个数是宝玉从原文页面的数据里自己算出来的：页面脚本 `LearningFlow` 里有一张 13×13×13＝2197 格的得分表，得分超过原文目标 0.5 的有 28 格，占 1.27%（我下载脚本算过）。说法本身对得上，但“2197 种接法”是作图时的网格，真实参数是连续的 |
| 2,000 | 原文另有“试 2,000 次后成为专家”，和上面的 2197 格是两回事，别混 |
| 换奖励学会逃跑、装死、战斗 | 对。奖励改成“躲开光”学出逃跑或装死；奖励“高速冲向光”学出冲撞（原文叫 FIGHT） |
| 鸣禽 | 对。原文说幼鸟唱得更接近记忆中的成年歌声就有多巴胺，链到 Kasdin 2025 |

**没核实的**：没看宝玉重画的两个视频；人脑“860 亿神经元”是原文的说法，没另查。

### 2. clips/2026-11-18-tensorslay-qwen-tts-dormant-neurons.md

**读了什么**

- 推文串（36 条，含作者 8 条续推和回复）。作者在回复里说：61 个沉睡神经元单独放大“几乎没效果”；先试了 2×、4×、6×、8× 四种混合强度，8× 才开始听得出变化；最先找到的是耳语 / ASMR；有人问是不是“权重空间编程”，他说这是最接近的叫法，但更愿意叫“神经元空间编辑”；用的是 Opus，它自己做了个声谱图工具来“看”输出
- 作者仓库 https://github.com/areu01or00/qwen-tts-neuron-mapping（2026-11-14 建，读了 README、NEURONS.md、neurons.json、reproduce.py）
- 模型配置 Qwen/Qwen3-TTS-12Hz-0.6B-Base 的 config.json（Hugging Face）
- Lazarus 原文 arXiv 2611.15118 全文 PDF（50 页），读了摘要、第 2 节相关工作、4.2 节和附录 B.1 的“沉睡”定义
- 用来连源头的论文：Dai 2022 知识神经元（arXiv 2104.08696，PDF 里确认它建立在 Geva 的键值记忆上，并做了“激活加倍”实验）、Geva 2021（arXiv 2012.14913）、Turner 2023（arXiv 2308.10248）、BadNets（arXiv 1708.06733 和 IEEE Access 2019 版），都用 arXiv 摘要页或 Crossref 核过

**核对的数字**

| 推文说法 | 核对结果 |
|---|---|
| 417 个神经元 | 对。neurons.json 里 417 条：主组 400 个，加笑声 5、插话 5、耳语 4、停顿 3 |
| 约占 talker MLP 神经元的 0.48% | 对。配置写 talker 28 层、每层 3072 个，共 86,016；417 / 86,016 ≈ 0.485% |
| 61 个沉睡 | 对。主组里 55 个，加四个小组里 6 个；其中 24 个算“严格沉睡” |
| 一起放大出现呼吸、ASMR、笑、耳语、第二个人 | **部分对**。仓库表里笑、耳语、停顿、插话来自 400 个放大 8～12 倍（或加小组微调）；“呼吸”用的是另一种改法：在 CustomVoice 版本上把第 20～27 层全部神经元沿一个方向放大 2 倍，不是这 417 个。ASMR 在仓库表里没有单列 |

**要说清的边界**

- “沉睡”的定义两边不一样：作者是“在 1,050 帧普通语音里，进入本层激活前 1% 的比例低于 1%”；Lazarus 是“把它关掉后，正常输入的下一个 token 分布几乎不变（KL 小于阈值）”
- 主组 400 个的改法不是单纯把激活乘倍数，而是把它们写进残差流的那部分、沿每层一个固定方向 d_L 放大 α 倍；d_L 怎么来的，仓库没写
- 放大到 16 倍以上普通语音会变乱码；在内置音色上 400 个 ×10 有 13/36 次停不下来
- 全部是作者自测，听感判断，没有客观评测，也没人独立复现
- Lazarus 的数字（12,000 多个里改 7 个、触发成功率至少 98.8%、检测 91.4% / 误报 9.7%）是作者预印本自报

### 3. clips/2026-11-18-thesupermannx-molecular-structure-of-thought.md

**读了什么**

- 推文只有一条，没有续推（串里只有原推）
- 论文原文 arXiv 2601.06002 全文 PDF（v2），读了摘要、第 1～5 节、第 9 节相关工作、第 10 节结论、Limitations、附录里的标注方法和注意力“能量”定义。v1 是 2026-01-09，v2 是 01-13；作者来自字节跳动 Seed China、哈工大、北大、2077AI、南大、M-A-P、中南大学
- 论文引用的前人工作：思维链 Wei 2022 [1]、自洽 [2]、DeepSeek-R1 [8]、思维树 [20]、GoT [21]、思维图 [23]、Self-Refine [17]、Reflexion [18]。思维树、思维图另读了 arXiv 摘要页；思维树 PDF 里确认它引了 Newell、Shaw、Simon 的通用问题求解程序和“系统一 / 系统二”

**推文和论文对照**

| 推文 | 论文里有没有 |
|---|---|
| 中国发了一篇论文 | 大体对：作者单位都在中国（含字节跳动 Seed China）。但论文 1 月就挂出，推文 11 月才发 |
| 绘出了 AI 推理的真实内部结构，看清黑箱 | 夸大。主要方法是把推理文本切成步骤，用模型自动标成四类行为（人工抽查 200 条，macro-F1 超过 0.85），统计行为之间的转移；另有少量内部分析：交叉编码器稀疏自编码器特征、步骤向量的 t-SNE 图、注意力“能量” |
| 大家一直以为思维链是直线，被证明完全错了 | 夸大。论文只说早期工作把思维链当步骤序列，并承认 2023 年起已有树状、图状推理（第 9 节）；论文用的词是“提出假说”“结果表明”，不是“证明” |
| 看起来、表现起来和化学分子一模一样 | 和论文相反。论文脚注说 C、H、O 原子只是比喻，附录说“能量”只是注意力 logit 换个写法，不代表物理意义 |
| 思路分叉、绕回去自查、剪掉死路另开新路 | 前两点和论文接近：反思步骤有 81.72% 回连到先前的语义簇，探索步骤连接远处的簇。“剪掉死路”论文没有专门讲 |
| 看形状就能在说出口前发现幻觉、安全失败 | 论文里没有。只有一句假说式的话说反思连接“约束漂移和幻觉” |
| 会改变 AI 怎么思考 | 论文实际的用处是：解释为什么模仿人类或弱模型学不会长推理；提出合成数据方法 Mole-Syn，在 6 个基准上接近蒸馏效果、让强化学习更稳；还说总结、压缩推理过程能防止被蒸馏 |

**核对的数字**：不同模型的行为转移图相关系数大于 0.9（样本超过 2,000 时稳定在 0.95 以上，第 4.1 节）；深推理后 72.56% 的步骤留在近距离簇内、反思步骤 81.72% 回连（第 4.3 节）。这些是论文自报，没复现。

**没核实的**：Mole-Syn 的完整对比表（附录 Table 6）只扫了一眼，没逐项核对；论文没有同行评审版本。

## E 组：社会、历史与成长


2026-11-23。四条都用 `opencli twitter thread` 重新抓过原推，正文和库里一致。两条带视频的（达利欧 44 分钟、基恩 2 分钟）没法看视频，只能核对文字和外部原稿。

### 1. clips/2026-11-21-tom-jerry1088-why-asians-love-japan.md

**原推**：抓到全文（1264 字），没有续推和链接，和库里一致。

**读了的资料**

| 资料 | 读到哪里 | 核对了什么 |
|---|---|---|
| コトバンク「和魂洋才」https://kotobank.jp/word/%E5%92%8C%E9%AD%82%E6%B4%8B%E6%89%8D | 大辞泉、日本国語大辞典、四字熟語辞典三条 | 明治时照“和魂汉才”造的词；最早用例是森鸥外《なのりそ》1911。原文没给年份，但把它放在“1868 年明治维新之后”的语境里，词本身晚于维新 |
| コトバンク「和魂漢才」https://kotobank.jp/word/%E5%92%8C%E9%AD%82%E6%BC%A2%E6%89%8D | 三条 | 出自托名菅原道真的《菅家遺誡》，日国推定镰仓末；本义是汉学知识加实际判断力 |
| コトバンク「東洋道徳西洋芸術」https://kotobank.jp/word/%E6%9D%B1%E6%B4%8B%E9%81%93%E5%BE%B3%E8%A5%BF%E6%B4%8B%E8%8A%B8%E8%A1%93 | 世界大百科事典 | 幕末佐久间象山；和中体西用、东道西器同类 |
| コトバンク「町人文化」「浮世絵」「居酒屋」「士農工商」（链接见 out 文件 chonin-culture） | 各条全文 | 浮世绘是町人绘画，词在 1681–84 前后定型 ✓；专营居酒屋江户中期成形，但酒肆可上溯 761 年 △；士农工商：农工商之间实际无上下 △ |
| 英文维基 History of anime https://en.wikipedia.org/wiki/History_of_anime | 摘要 | 最早可考的日本动画 1917 年，“动漫源头在江户”✗ |
| 英文维基 First Opium War / Perry Expedition | 摘要 | 鸦片战争 1839–1842 早于佩里 1853，“日本是全亚洲第一个被迫直面西方冲击的国家”✗ |
| 英文维基 Japanese asset price bubble / Lost Decades | 摘要 | 泡沫 1986–1991，1990 年起破裂 ✓ |
| CiNii https://ci.nii.ac.jp/ncid/BB22478758 ；豆瓣 https://book.douban.com/subject/26889057/ | 书目、内容简介 | 大前研一《低欲望社会》2015 年小学館初版、2016 年新书改订版；内容：不买房车、不婚、利率不到 1% 也不借钱 ✓ |
| Duke UP https://www.dukeupress.edu/recentering-globalization ；OpenAlex 摘要 https://doi.org/10.1215/9780822384083 | 简介和目录 | 岩渕 2002：日本把西方流行文化本地化卖给亚洲，第 4 章讲台湾的“文化接近” |
| JSTOR Daily https://daily.jstor.org/pan-asianism-redux-or-why-we-think-japan-is-special | 全文相关段 | 岩渕批评“混杂主义”把文化混合当日本国民性 |
| Crossref / OpenAlex：Straubhaar 1991 https://doi.org/10.1080/15295039109366779 | 摘要 | 观众主动寻找文化接近的节目 |
| 英文维基 Edward Relph、Sense of place | 相关段 | 《地方与无地方性》1976，Pion；无地方景观和所在地没关系，例子是连锁店 |

**没能核实**：岩渕、雷尔夫、大前三本书都没读到正文，只读了出版方简介、目录、书目和二手转述；“亚洲人迷恋日本是在找丢掉的东西”是作者推断，没查到问卷或调查支持，也没查到反对的数据；洋食（蛋包饭、咖喱）起源年份没查。

### 2. clips/2026-11-19-lesliedqbb-dalio-shen-old-order-diversify.md

**原推**：抓到全文，视频时长 2651 秒（约 44 分钟），没有续推。评论区 @YunTechX 指出“翻出来是 2022 年的旧视频”。

**读了的资料**

| 资料 | 读到哪里 | 核对了什么 |
|---|---|---|
| HSG（红杉中国）文字稿 Neil Shen and Ray Dalio on Principles, Investment Cycles, and Navigating Global Change，2022-06-22 https://www.hsgcap.com/?p=2421 | 全文（约 6000 词，44 分钟视频的篇幅对得上） | 见下表 |
| 中文报道：北京新闻 https://www.bjnews.com.cn/detail/1656045430169444.html 、澎湃 https://www.thepaper.cn/newsDetail_forward_18718841 （搜索摘要） | 摘要 | 2022 年 6 月 23 日晚抖音直播、中信出版邀请，围绕新书 |
| 搜索 2025–2026 年两人有没有新对谈 | 中英文各搜两次 | 没找到；沈南鹏 2025 年在香港金管局峰会主持过别的圆桌，嘉宾没有达利欧 |
| 桥水 The All Weather Story（2012-01）https://www.bridgewater.com/resources/all-weather-story.pdf | 第 1–3 页 | 全天候 1996 年推出，按增长和通胀情景平衡 |

**帖子各点和原稿对照**

| 帖子说 | 原稿里有没有 |
|---|---|
| 旧世界秩序在瓦解 | 有：达利欧讲秩序从一个换到另一个，通常经过战争 |
| 美国债务和利率到了临界点，拿现金购买力被稀释 | 大体有：印钞让货币贬值、通胀和滞胀；“现金、短期长期国债都会是负实际回报”；利率不会升到足以压住通胀 |
| AI 资本泡沫和洗牌风险 | 没有：AI 只出现在“你们用不用 AI 做研究”和“中国的 AI、量子计算发展”两处 |
| 欧洲深陷结构性泥潭 | 没有：欧洲只在“贫富差距欧洲也大”和“产品可以打进欧洲”里提到 |
| 中美博弈、地缘摩擦 | 有：美国秩序和中国等崛起大国的竞争，五类冲突 |
| 普通人唯一能做的是打破单一资产、单一市场依赖 | 前半句是转述者加的；后半句对得上达利欧原话：先别持现金，要分散，全球投资者要跨地区、国家、行业分散 |

**没能核实**：没看视频，不能 100% 确认视频就是这场 2022 年对谈（时长、评论、搜索结果都指向它，没找到别的同名对谈）；“两位管理着千亿美金”没查。只做溯源，没给投资建议。

### 3. clips/2026-11-18-thedankoe-learn-to-learn-write-speak.md

**原推**：抓到全文，和库里一致。它引用了 Hussain Ibarra 的 X 长文 How to become dangerously well-spoken（用 `opencli twitter article` 读了开头：讲怎么把话说好，第一条是“用写作来想清楚”）。

**读了的资料**

| 资料 | 读到哪里 | 核对了什么 |
|---|---|---|
| 英文维基 Transfer of learning https://en.wikipedia.org/wiki/Transfer_of_learning | Formal discipline、近迁移和远迁移两节 | 形式训练说要求学数学、拉丁语练心智官能；1901 年桑代克和伍德沃斯用相同要素说反驳 |
| Teachers College 2003 文章 | 相关段 | 桑代克挑战“学拉丁语练心智肌肉” |
| Crossref：Thorndike 1924 Mental Discipline in High School Studies https://doi.org/10.1037/h0075386 | 只有书目 | 论文存在；具体样本和结果没读到，没写数字 |
| Sala & Gobet 2017 https://doi.org/10.1177/0963721417712760 | 摘要（OpenAlex） | 三项元分析，效果小到中等、和设计质量反相关，“远迁移很少发生” |
| Sala & Gobet 2019 https://doi.org/10.1016/j.tics.2018.10.004 | 摘要（Semantic Scholar） | 对通用认知能力效果极小 |
| Barnett & Ceci 2002 https://doi.org/10.1037/0033-2909.128.4.612 | 摘要 | 某些条件下远迁移证据可观，不能用一个效应量概括（写进 dispute） |
| Hattie, Biggs & Purdie 1996 https://doi.org/10.3102/00346543066002099 | 摘要 | 51 项研究；训练要放在具体学科、同领域任务、配合元认知 |
| Bangert-Drowns 等 2004 https://doi.org/10.3102/00346543074001029 | 摘要 | 48 个项目；写作对学业有小的正面作用；元认知提示、时间长效果更好 |
| MIT 温斯顿《How to Speak》文字稿 https://www.ocw.mit.edu/courses/15-371-innovation-teams-fall-2024/Unzc731iCUY_transcript.pdf | 第 1 页（下载 PDF 转文字） | 原话：成败很大程度取决于说的能力、写的能力和想法质量，按这个顺序 ✓ |

**没能核实**：几篇元分析只读了摘要，具体效应量数字没写；Dignath & Büttner 2008 自我调节学习元分析（https://doi.org/10.1007/s11409-008-9029-x）摘要被出版方隐去，没用。研究整体是：学习策略和写作对学别的东西有小到中等帮助，但“外溢到任何技能”被远迁移研究否定，所以挂了两条“挑战”。

### 4. clips/2026-11-18-marionawfal-china-800kv-grid-cheap-ai-power.md

**原推**：抓到全文，视频 123 秒；它引用了同作者的另一条（基恩说 AI 泡沫最多是 19 世纪铁路狂热的两倍、美国 AI 公司多数会倒）。原始采访出处没找到。

**读了的资料**

| 资料 | 读到哪里 | 核对了什么 |
|---|---|---|
| 英文维基 Ultra-high-voltage electricity transmission in China | 正文和线路表 | 1000 千伏交流 2009-01；±800 千伏直流（云南—广东）2010-06；水电在西、负荷在东南 |
| 英文维基 Yunnan–Guangdong HVDC | 正文和信息框 | 2007 开工，2009-12 单极、2010-06 双极，世界第一条 800 千伏直流 → 到 2026 年约 17 年，“几十年前”✗（夸大） |
| AEP https://www.aep.com/news/stories/view/837 | 相关句 | AEP 自述 1969 年投运第一条 765 千伏线路 → 美国也早有高电压，差别是长距离特高压直流网络 |
| 英文维基 Joule heating | 相关段 | 1840 年焦耳；高压靠降低电流减少损耗 |
| 发改委高技术司 2022-03-21 专访稿 https://www.ndrc.gov.cn/fzggw/jgsj/gjss/sjdt/202203/t20220321_1319862.html | 全文 | 8 个枢纽、10 个集群，东部土地能源紧张、西部可再生能源丰富，“正式全面启动”；文中没讲电价 |
| Carbon Brief 2025-04-16 | 全文 | 西部中心做离线分析和备份；没有电价数字 |
| EIA Electric Power Monthly 表 5.3（2026-10-23 发布）https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_03 | 表格 | 美国工业平均电价 2025 年 8.51 美分/度，2026 年 1–8 月 9.09；商业 13.37、14.04 |
| 财新 2025-05-16 https://www.caixinglobal.com/2025-05-16/in-depth-chinese-tech-giants-struggle-to-power-ai-data-center-boom-102320408.html | 可见部分（付费墙） | 西部和北部部分地区给数据中心的补贴电价约 0.35–0.36 元/度，其他地方 0.6 元以上 |
| Semafor 2025-11-05（转述 FT）https://www.semafor.com/article/11/05/2025/china-slashes-big-data-centers-electric-bills | 全文 | 地方政府补贴部分大型数据中心电费，最多减半，条件是用国产芯片 |
| OilPrice 2026-09-22（Simon Watkins）https://oilprice.com/Energy/Energy-General/Is-Chinas-Secret-Power-Advantage-About-To-Trigger-An-89-Crash-In-US-AI-Stock.amp.html | 全文 | 基恩之前讲过“中国电网由工程师统一设计、损耗更低”；“九成性能、一成成本”在这篇里是 Betamatrix 的 Mehrdad Emadi 说的 |

**“三分之一电价”粗算**（汇率按约 7.2 元兑 1 美元，未查当日汇率）

| 比法 | 结果 |
|---|---|
| 西部补贴价 0.35–0.36 元 ≈ 4.9–5.0 美分，对美国 2025 年工业均价 8.51 | 约 58%，不到三分之一的水平 |
| 再叠加“最多减半”的补贴 ≈ 2.5 美分 | 约 29%，接近三分之一 |
| 西部补贴价对美国商业均价 13.37 | 约 37% |
| 其他地区 0.6 元以上 ≈ 8.3 美分 | 和美国工业均价差不多 |

结论：“中国数据中心电费约为美国三分之一”只在最便宜的补贴情形下接近，没查到一手的全国平均对比。搜索里有“华盛顿邮报算出约 3 美分、约美国三分之一”的二手转述，没找到原文，没采用。

**没能核实**：视频没看，基恩原话（“九成功能、一成成本”、“兰博基尼价”）没法核对；美国数据中心集中在城市附近、中国把电送到偏远数据中心这两个说法没找到一手数据，按东数西算的官方说法，偏远数据中心是“就地用电”，特高压是往东送电，方向和基恩说的不一致。
