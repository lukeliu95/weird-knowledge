# 第11轮整理：出处与证据边界

2026-11-14。模型概括，不等于实验复现、数学审稿或法院认定。只读部分或摘要的材料逐项说明。

## 第11轮新闻与制作案例核查

2026-11-14。以下均为模型概括，保留诉讼指控、官方声明和机制推断的区别。

### 校园 Gemini 诉讼及默认权限

- 原报道[IT之家](https://www.ithome.com/1/023/765.htm)正文已读。没有重发未成年人的对话、身份或伤害方法。
- 找到[原告代理机构案件页](https://edtech.law/cases/emma-v-google/)和它公布的[起诉书原件](https://edtech.law/wp-content/uploads/2026/11/2026.11.04-Dkt-001-1-Emma-v-Google-Complaint_2.pdf)。这是原告一方材料，不是法院认定。起诉书共108个PDF页，本轮只核对封面、目录及引言开头，没有读完全文，不概括其全部证据。
- 封面（PDF第2页）州法院收件章为2026-11-02，州案号26CV507724；联邦文书页眉为5:26-cv-13205，文书1-1于11-04入档。案件页标11-04，两个日期不应混为同一程序日期。本轮不推断最终审判结果。
- [Google 11月3日官方公告](https://blog.google/products-and-platforms/products/education/ai-learning-era-updates-2026/)的“Enhancing school controls”说：Gemini、Gemini Notebook、Gemini in Classroom与Search将默认关闭，待管理员明确开通；并说之后数月再给实施细节。因此只能说宣布调整，不写成当日已全面生效。
- 同一官方页面说明Search内的Guided Learning会先在部分美国学校试点。“关闭独立Gemini”与“关闭搜索里的全部AI”不是同一设置；没有从该页获得已实施的全部管理员开关说明，不把捆绑关系写成法律结论。
- [Saltzer与Schroeder 1975原论文](https://www.cs.virginia.edu/~evans/cs551/saltzer/)第I.A.3(b)定义fail-safe defaults为默认无访问、按明确许可放行。只用于权限模式的弱类比，不声称Google引用过该论文，或新策略已经证明能避免危害。
- 原保存要点中的“未读起诉书”和本轮补读发生时间不同，原文区照留，本轮说明另写。58%市场份额及完整监控链路未独立核对。

### 董事会调查报道

- The Verge原页面本轮仍无法访问，不补写作者身份或其完整原文。
- 已读[英伟达董事会2026-11-08原始声明](https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors)：启动调查，由独立董事委员会监督、独立外部律师协助；当时没有理由认为国家安全或公司机密受损。声明证明公司启动程序，不证明新闻指控成立。
- 已核对[美国众议院原始函件](https://foreignaffairs.house.gov/sites/evo-subsites/republicans-foreignaffairs.house.gov/files/evo-media-document/11.4.26nvidialetter.pdf)，1页，落款11-04，要求11-18进行闭门说明。原保存要点转述成“11-05要求”，本轮另注日期，不改旧文。函件中的指控仍是公开报道背景，不是裁决。
- [OECD 2023第V章](https://www.oecd.org/en/publications/2023/09/g20-oecd-principles-of-corporate-governance-2023_60836fcb/full-report/component-8.html)章首、V.A、V.E和V.F要求监督管理层、独立判断、获取准确信息。由此作机制比较，不倒写成公司明引的来源。报告为规范性指引，未阅读全文其他章节。
- 不扩充私人关系、匿名指控或新闻后续。整理目标是核实原条目中的治理程序及证据层级。

### 歌剧制作工具体系

- 已读保存的作者全文；没有观看完整成片或取得内部工具代码，效率收益没有独立测量。
- 原文明确是“Yuri的首部AI歌剧”，不是世界首部，标题据此订正。
- [GNU Bash手册3.2.3 Pipelines](https://www.gnu.org/s/bash/manual/html_node/Pipelines.html)原文摘录定义将一条命令的输出接到下一条输入。本轮直连GNU页面超时，从该官方页面的索引摘录核对定义；POSIX页面403，未声称读到。Unix历史原件入口本轮也未成功，不补写历史新结论。
- 独立复核认为原文没有明确的输出到输入串接证据，主会话采纳：不挂管道理论，保留为已核查但源头待查的观点；不补造实现细节。

## 第11轮工程观点核查

2026-11-14。只核查公开原文和公开一手资料；不改 clips、roots 和框架。本组2条溯源、1条低价值归档，复用已有源知识。

### Magpie 三循环

- 原条：`clips/2026-11-10-xulijian1994-magpie-three-loops-auto-dev-workflow.md`，已读完整原文。
- 找到库内旧材料 `clips/2026-10-18-yetone-claude-code-three-parallel-loops.md`（作者本人短帖）及宝玉的完整转述。作者原推为 [2026-10-13 的公开说明](https://x.com/yetone/status/2109855710444237018)，本轮网页工具读X返回403；不能声称重新取得原帖或三张截图。新条是已有案例的再讲述。
- [Magpie 当前 AGENTS.md](https://github.com/yetone/magpie/blob/main/AGENTS.md)：已读相关规则，修改前读设计文档、代码标准、贡献者规则和 LESSONS.md；这是当前版本的要求，不是重建发帖时历史状态。
- [Magpie 当前 LESSONS.md](https://github.com/yetone/magpie/blob/main/LESSONS.md)：核对开头说明、若干真实验证和跨平台条目及“Red tests and releases”。明确自述由agent写代码、审查、合并和发布，每晚复盘；同时记录Windows测试漏跑及带失败结果发布的教训。这支持存在该工程流程，不能证明无人介入、所有变更均合格，或比别的生态稳定。本轮没有独立运行Magpie测试或审计全仓库。
- [Kieran Klaassen 原文](https://every.to/source-code/my-ai-had-already-fixed-the-code-before-i-saw-it)：读到标题、日期和开篇定义、案例。发表2025-08-18，页面标2026-10-02更新；把修复、评审经验写成以后默认做法，是本条“复合工程”相近关系的依据。不是说 yetone 直接引用了它。
- [Claude Code 当前最佳实践](https://code.claude.com/docs/en/best-practices)：读“Give Claude a check to run”及其验收方式；支持给agent可运行检查的机制比较。没有把当前不断更新的写法归为2025年旧文原话。
- 还查了 [von Hippel 1986原论文作者版](https://web.mit.edu/people/evhippel/papers/Lead%20Users%20Paper%20-1986.pdf) 的摘要、引言与第3节定义。领先用户既要处在需求前沿，也要有较高解决收益。新条只说普通用户提供反馈，未说明符合这两点，也未证明用户自己创新，故**不追加用户创新或领先用户关系**。
- 本条无可核对性能增益数字；“稳定性更有优势”是转述者判断。

### 本地 Qwen + 教师案例 + LoRA

- 原条：`clips/2026-11-11-simonhoiberg-qwen-lora-distill-support-cases-local.md`，已读完整原文；原文含数千案例、自定筛选标准、小LoRA、本地运行的自述。
- [作者X原帖](https://x.com/SimonHoiberg/status/2120132843669979347) 本轮网页工具403，未读附带20秒视频。搜索找到作者LinkedIn公开个人页同文帖，但不据搜索重述补充新的实验细节；不把聚合站或二手转述当验证。
- [LoRA论文摘要页](https://arxiv.org/abs/2106.09685)及[正文第4.1节](https://arxiv.org/html/2106.09685v2)：已核对作者、2021年初版、冻结原权重并学习低秩更新的定义。原文明说LoRA，因此直接源自、强。未重算论文结果，也不把早年GPT系列实验数字外推成Qwen客服成绩。
- [Hinton等2015论文摘要页](https://arxiv.org/abs/1503.02531)及[正文引言、第2节](https://arxiv.org/html/1503.02531v1)：核对教师向较小学生迁移能力、温度软目标的具体方法。本条描述生成后筛选的文本案例，未给logits、温度、损失；只提出知识蒸馏“相近、弱”候选，不声称直接复现2015算法。
- 未找到本帖可核对的客服留出集规模、评判人/评判模型、通过率、训练与推理配置或与Opus对照。数千案例是作者声称；“达到Opus质量”不能作为实测结果。“无API账单”限本地推理调用形态，不等于训练、硬件、电力或运维免费。
- 建议标题写明“作者称”“未给对照评测”。

### 神鱼认知纲要

- 原条：`clips/2026-11-11-something-labs-bitfish-compute-era-cognition.md`，已读完整原文。
- 原文只有标题式概括，并重复“向内觉察”一项；没有展开“两个核心旋钮”“双轨阅读”的定义。
- 搜索原短语只得到相同发布者镜像和延伸感想，没有取得原视频逐字稿；未听/看完整视频。
- 建议观点、思维与成长、溯源价值1归档。保留内容及媒体链接，明确“未核视频”；不凭隐喻强连控制论、认知科学或时间物理理论。

## 第11轮科学与预测条目：出处核对

核查日期：2026-11-14。只处理本轮两条公开帖子；未修改公开知识文件。下列概括均为模型分析，不是作者原文。

### 1. Claude两项理论物理结果

条目：`clips/2026-11-11-bettercallmedhi-claude-theoretical-physics-black-holes-bootstrap.md`。

#### 直接证据

- 已完整阅读条目法语正文；下载并逐张查看其四张公开配图（本机 `science-media/HWu7I0*.jpg`）。第二、第四图为两篇预印本的摘要截图，第一、第三图为标明理论条件的结果示意图。因此这里不是凭关键词相似猜论文。
- [Anthropic 2026-11-09发布页](https://www.anthropic.com/claude-fable-and-mythos-5-2)的“Theoretical physics”部分直接链接下面两篇稿件。本轮仅核对相关段落，没有以整页其他模型成绩作为物理结果的额外证明。
- [The Hawking-Page transition at weak coupling](https://hexagonmath.org/2611.00175v1)，2026-11-07 v1，42页。已读网页摘要、Provenance statement、参考文献入口，以及[PDF](https://hexagonmath.org/pdf/2611.00175v1)第1节结果/检查和第1.7节限制（PDF第7至8页相关内容）。没有通读或复算全文。结果限定于大N及弱耦合，原稿明确不证明相变线从弱耦合一直连续接到强耦合。
- [The spinless modular bootstrap at large central charge](https://hexagonmath.org/2611.00174v1)，2026-11-07 v1，131页。已读网页摘要、Provenance statement、参考文献入口，以及[PDF](https://hexagonmath.org/pdf/2611.00174v1)第1.3节结果和“does and does not say”（PDF第4至6页）。没有通读131页或复算证明。斜率约9.1266是限定泛函类、大中心荷极限下的结果；不是声称所有有限中心荷理论的最强界均被取代，更不是排除一切量子引力候选。

#### 人与模型各做了什么

- 第一篇来源声明：内部Claude研究模型在物理学家提示后取得结果；物理学家核对已知特例；另一个Claude计算用不同方法得到同样结果。未署该物理学家的个人姓名。
- 第二篇来源声明：内部研究模型先取得主要结果，公开Opus 5.5之后独立取得同一结果；Claude在物理学家简短指导下写稿，物理学家检查主要结果。
- 发布页将两项工作归于Fable 5.2；预印本声明的模型名称更笼统。这两个来源口径分别保留。
- 仅核对公开稿，不宣称自己已验证数学正确性、复现代码或确认正式同行评审状态。不是现实宇宙黑洞形成的实验发现。

#### 往下追的原始工作

- [Maldacena，1997年AdS/CFT论文](https://arxiv.org/abs/hep-th/9711200)：只读摘要及书目信息；此文被第一篇新预印本明确引用。记录1997初稿、1998期刊发表的区别。它提出特定理论的引力/场论对偶，不能泛化为现实宇宙已经被统一解释。
- [Hellerman，2009年二维CFT上界](https://arxiv.org/abs/0902.2790)：初查只读摘要及书目信息，独立复核后补读第4.1节及文献28；此文列在第二篇新预印本参考文献第一项。记录2009初稿、2011期刊发表的区别。
- 两个底层工作初查只读摘要；Hellerman在独立复核时补读第4.1节及引用，见后文。阅读范围逐项写明；不作为已阅读全文的补课材料新增clip。

### 2. “若轨迹持续，2027年智能爆炸”

条目：`clips/2026-11-11-dr-singularity-intelligence-explosion-2027-trajectory.md`。

#### 配图与话语来源

- 已完整读条目正文，并查看公开原图 `science-media/HWu87HIWkAAhMYx.jpg`。图署名`graph: @kbeguir`，纵轴明确是 **80% coding time horizon**。图例分别标出AI2027情景、METR实测、ECI估算、Models 3/4、预测门槛与外推曲线。图中还画出Kokotajlo与Lifland两条不同的中位数轨迹。因此原图本身并不是一组纯实测数据。
- 找到[Karim Beguir 2026-11-08原帖链接](https://x.com/kbeguir/status/2119510769259720963)。X直接访问403；用[公开镜像](https://xitter.cf/kbeguir/status/2119510769259720963)核对作者、日期和完全一致的引句。镜像只用于定位话语，不作为内部模型能力或2027结局的独立证据。
- 原帖作者说曾修正AI2027作者指出的绘图bug；本轮没有取得修正前图和完整绘图代码，不能复核每个点的换算。

#### 一手预测文件

- [AI 2027原站](https://ai-2027.com/)：读开头的方法、2025-11-22补充说明、研发加速定义，没有通读全部分支。作者明确不知道AGI确切年份；2027是发布时众数，作者中位数更晚；情景不等于预测已兑现。
- [Timelines Forecast](https://ai-2027.com/research/timelines-forecast)：读摘要、方法、区间、条件及新版模型指针。预测依赖灾害、供应链、暂停等假设，不是仅把一条拟合曲线无限延伸即可。
- [Takeoff Forecast](https://ai-2027.com/research/takeoff-forecast)：读概要、主要里程碑定义、方法和不确定性声明；其时间表先条件于达到超人编码能力。原文明确大量依赖直觉判断、证据不足以确定外推。
- 新版[AI Futures Model](https://www.aifuturesmodel.com/)为动态页面，本轮未能读到完整内容。因此不拿2025年模型中的数字冒充2026年最新版。

#### 判断与处理建议

配图足够定位AI2027，建议保留为价值2的观点并溯源；标题补回“若轨迹持续”和“可能”。两篇物理预印本各形成具体源知识，基础追到已有/新建的理论原作。2027条目链接AI2027情景源知识，关系表示其话语出处，不表示认可年份会成为现实。最终4个新root及复用的AI2027均核实了原始出版入口，`verified: true`仅代表出处已核实。

#### 合并前独立复核补正

- AI2027已有 `kokotajlo-2025-ai-2027`，最终复用，未重复新建；本组实际新建4个源知识。
- 独立复核读到[Hellerman v2第4.1节及文献28](https://arxiv.org/html/0902.2790v2)，该引力解释明确引用Maldacena原文。只把这部分解释追到AdS/CFT，CFT上界本身不依赖bulk引力推导。

## 归档内容的边界

12条归档由5条工具、4条教程和3条低溯源价值观点组成。归档不代表推荐、许可证、模型质量、平台上限或作品首创经过验证。具体未验证内容已写入各条目“第11轮核查边界”。

## 独立核查与弱关系复核

- 合并前删除歌剧到管道的候选：仅有多个制作环节，不足以确认输出输入串接。该观点保留待查。
- 复用已有AI2027，避免为同一报告建立重复源知识。
- 第二模型复核5处弱关系，全部保留；知识蒸馏由相近改为直接源自（弱），表示广义教师输出训练的使用，不表示复现2015年温度软目标算法。
- 13条已确认原则原话与状态保留；本轮未出现需要推翻原则的可靠新证据。
