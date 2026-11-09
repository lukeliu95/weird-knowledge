# 第 10 轮整理：出处核查与边界

2026-11-09。以下是分组形成的核查摘要，正式结果已统一合并；模型概括不等于独立复现实验或医学审稿。

## 归档条目的补充核查

2026-11-09。工具与教程归档表示保留供查找，不表示性能及宣传承诺都已独立验证。

### ScientistTwo

已打开[项目作者页面](https://scientist-two.github.io/)，核对页面列出的作者、Google Cloud AI Research 署名、方法和表格，未独立重跑代码或逐篇评审。

- 作者报告在 107 个研究问题中有 86 个优于所选人类基线，平均相对增益 25.2%。不能把 86 写成全部测试问题，也不能把相对指标增益说成所有科研工作的统一提升。
- 审稿分数和接受率来自 ScholarPeer、Stanford Agentic Reviewer 两个自动评审器，不是正式顶会接受结果，更不是博士学位授予结果。
- 完整系统的完整性审计对应 49 篇的分数与代码检查、1814 个引用的存在性核验；零虚构引用不表示所有内容、推理和结论零幻觉，也不是全体科研框架的永久保证。
- 归档题名改为“ScientistTwo 自动科研框架：项目自报在 86/107 个研究问题上改进基线”；原阿拉伯语正文不改。

### 其他归档边界

- Hassabis 视频帖只给转述者的宣传和发展阶梯，没有核实具体演讲和时间。“一人胜过整个初创团队”不作为 Hassabis 已验证的原话或结果。
- “鼠标集群”、agent 强但令人沮丧、《代码的未来》奇书都是缺少可追论证的感想或推荐，未从视频或书名反推理论。
- Cat Wu 的消息按作者人事自述归档，不由这一条推导行业或产品能力结论。
- Skill 库八层步骤按教程归档；“Anthropic 10 页 PDF”归属及 25 个流程的 token 估计未核实为官方评测，原文数字不当性能承诺。

其余工具保持为入口资源，本轮不安装、运行、部署或替用户调用这些项目。

## 第 10 轮 · 模型组出处核查

日期：2026-11-09。范围：4 条公开内容。以下保留原始查证内容；最终关系按本轮统一复核结果写入。

### 1. 权重空间编程

条目：clips/2026-11-03-rikiyatakehi-weight-space-programming.md

已读原推全文，并阅读[作者研究博客](https://rikiyat.github.io/blog/weight-space-programming/)的导言、相关工作、实验 7、8 和限制。作者署名为 Rikiya Takehi、Jayden Teoh、Alex Zhang、Omar Khattab，日期 2026-11-02。附有[公开日志](https://github.com/RikiyaT/lm_understand-logs)，本轮未复算。

最需要保留的条件：

- 数学实验的目标模型是 Qwen3.5-0.8B，使用练习题、Python、最多 50 次目标模型前向反馈。不用梯度下降，不等于不用数据和计算。
- MATH-500 从 7.9% 到 48.1% 是作者报告的特定设置；约 6 倍是正确率之比。
- 作者把主要机制解释为移除导致长推理循环的方向。对原本少循环的 Gemma 3 270M，没有建立同样收益；不能说模型凭空获得缺失的数学能力。
- 读权重判断行为也出现失败案例，不能外推成所有内部性质都可直接读出。
- 原候选曾把实验反馈关联到通用反馈理论，第二模型认为只是背景沾边，已删除直接关系及同义的更底层链接；没有因此改动研究实验本身。

建议标题只收窄模型概括，原文不动。

### 2. 对比语言模型 CLM

条目：clips/2026-11-06-dailydoseofds-contrastive-language-model-decision-as-retrieval.md

已读原推全文，并核对当前[官方仓库 README](https://github.com/Contrastive-LM/CLM)与[官方模型卡](https://huggingface.co/Contrastive-LM/CLM-v0.1-8B/blob/main/README.md)。官方研究博客入口本轮无法访问，不声称读到。作者信息取自仓库引用，未拿二手推文替代论文署名。

方法证据：冻结 Qwen3-8B 编码器，训练状态和动作两个投影头，以双向 InfoNCE 区分匹配与不匹配，再评分给定候选。该方法本身不生成候选之外的新动作。

最需要保留的条件：

- 官方的最高 9 倍延迟改善与候选规模、可缓存性和具体任务有关，不是所有推理统一快 9 倍。
- 模型卡另给约 1000 个缓存候选的 13 倍说明，是另一个条件，不能串成同一测试。
- 零样本动作选择与任务微调后的代码验证是不同实验；后者不是通用零样本成绩。
- 候选概率是相对于给定集合的分布，不能直接当作真实世界的绝对置信度。
- 本轮核对当前材料，没有重建原推发布时仓库，也没有独立测延迟。

基础来源：Aaron van den Oord、Yazhe Li、Oriol Vinyals，[Representation Learning with Contrastive Predictive Coding](https://arxiv.org/abs/1807.03748)，初版 2018-07-10。核对[正文 v2](https://arxiv.org/html/1807.03748v2)第 2.1—2.4 节，特别是 InfoNCE、正负采样和互信息下界；未逐项复算实验或声称读完附录。它不是全部对比学习的起点。CLM 明确使用 InfoNCE，故这条是直接源自、强；InfoNCE 的互信息论证再接已有信息论。

### 3. 模型判断与代码决定

条目：clips/2026-11-07-allietheicon-dont-call-jev-a-decision-model.md

已读原推全文及 Allie Laabs 的[TypeSafe 原文](https://typesafe.ai/blog/dont-call-it-a-decision-model)。原文日期 2026-11-03，不拿转发日期当首次发表日期。作者来自销售相关模型的厂商，属于工程建议。

原文的退款例子区分语义问题与已知规则：用户是否想退款，需要模型理解；是否满足金额等明确条件，可由代码计算。多个判断由代码组合，比把全部流程塞进一个模型选择题更便于查错。这里没有证明“所有决定都能硬编码”，也没有受控实验保证任意场景都更准。

另核对 Dijkstra 1974 年[On the role of scientific thought](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD447.html)关于关注点分离的原意。TypeSafe 没有明确引用它；只写相近、弱，禁止写直接继承。没有把 System 1 的修辞继续硬接成心理学因果证据。

### 4. Anthropic 智能体记忆与离线整理

条目：clips/2026-11-08-dotey-anthropic-agent-memory-dreaming.md

已读宝玉原文全文，以及 Lance Martin 于 2026-11-06 发布的[Anthropic 原文](https://www.anthropic.com/research/components-of-agent-memory)全部正文。四层记忆是经历记录、笔记、组织表示、注入上下文；后台整理可修正笔记、合并经验，也可能引入错误。

关键修正和边界：

- 原文合并资料测试的 87% 对 73% 指需要多文档信息的题目子集，不能写成整组 24 题的总体成绩。将说明写进溯源，保留宝玉原文。
- 宝可梦每个模型只运行一次，不能从这项展示得到稳定统计优势。
- 内部文档和其他测评都是厂商自报，没有本轮独立验证；单文档任务未显示同样的维基收益。
- 共享记忆实验同时改变组织方式、写入责任和提示要求，不能把所有收益归因于一个并发变量。
- 不好的记忆可以传播错误；后台整理消耗计算，也有更新延迟。文章讨论方法，不据此承诺某项产品今天的可用范围。
- “做梦”是比喻，不能把生物睡眠与软件整理写成已证实的同一机制。

原文明确引用 Lin 等 2025 年[Sleep-time Compute: Beyond Inference Scaling at Test-time](https://arxiv.org/abs/2504.13171)，故相关关系为直接源自、强。核对[论文正文 v1](https://arxiv.org/html/2504.13171v1)的摘要、引言、方法与第 7 节讨论，未声称读完整本附录或复现实验。其核心是对共享背景先算，给未来多个查询复用；收益依赖未来问题的可预测性与复用次数。SWE-Features 的文件预测匹配不能冒充端到端代码正确率。未硬接生物睡眠研究作为软件收益的证明。

## 第 10 轮科学组：原始出处与证据边界

核查日：2026-11-09。范围为本组4条保存原文；以下为查证结果，未独立复现实验或校准原帖视频。

### 四条结论

| 条目 | 读到的一手材料 | 核查结果和边界 |
|---|---|---|
| 地球从不回到同一点 | [NASA 太阳事实页](https://science.nasa.gov/sun/facts/)、[Chandra 的太阳系问答](https://chandra.cfa.harvard.edu/resources/faq/sources/solsys/solsys-6.html)、[爱因斯坦原著第 II—III 章](https://www.gutenberg.org/files/5001/5001-h/5001-h.htm) | 太阳系绕银河中心运动与行星绕日公转可以同时成立；轨迹先指定参考系。不能把银河视角说成唯一绝对轨迹，也不能据一幅动画证明 45 亿年绝不重访某位置。230 km/s × 80 s = 18400 km，原帖“超过 18000”没有算错。 |
| 太阳系螺旋前进 | 同上；[NASA 托管 NIAC Phase I 报告](https://www.nasa.gov/wp-content/uploads/2017/07/niac_2012_phasei_nosanov_ssears_tagged.pdf)支持太阳系平面与银河面约 60° | 原帖“朝 Sagittarius A* 冲去”把绕银河中心运动写成了朝中心直冲。NASA 太阳页约 720000 km/h，原帖 828000 km/h 是不同近似口径，不能把机构科普数字当精密速度裁决。没有取得原动画的数据、尺度或坐标定义，不认证“真实 165 年轨迹”。 |
| 衰老和癌症是同一种病 | [Meta-hallmarks 原论文摘要](https://www.sciencedirect.com/science/article/pii/S1550413122004922)、[Sinclair 团队细胞与小鼠原研究](https://pmc.ncbi.nlm.nih.gov/articles/PMC10166133/)、[KAIST 作者实验室原论文](https://sbie.kaist.ac.kr/wp-content/uploads/2025/01/Advanced-Science-2024-Gong_official_publication.pdf) | 共享机制不等于同一种病。综述明确有共同、拮抗和情境依赖作用。Sinclair 工作为细胞和 ICE 小鼠模型，KAIST 工作主要为三种细胞系和裸鼠移植模型；不支持人体长期维持 25—35 岁或一并治愈所有癌症的结论。 |
| SenoMune-0257 首例给药 | [Immorta Bio 2026-11-02 原公告](https://www.prnewswire.com/news-releases/first-human-administration-of-senolytic-immunotherapy-to-fight-cellular-aging-announced-by-immorta-bio-302926449.html)，已读正文 | 开发商报告 10 月 29 日在墨西哥给首位晚期癌症患者使用九氨基酸多肽。公司明确人体安全有效性尚未建立；公告未给本次人体结果和完整样本量。“首位给药”不等于整项研究 n=1，也不等于任何衰老细胞靶向疗法的全球首次人体研究。 |

### 天文出处与推理范围

- 爱因斯坦公版原著第 III 章用车上和路边观察同一落石得到直线、抛物线的例子说明：轨迹相对参考体定义。本条只使用这个基础概念，没有声称太阳系或银河参考系全程均为惯性系。
- NASA 的太阳事实页及 Chandra 问答均说明绕银河中心公转，约 2.3 亿年一周。Chandra 还说明相对银河面的运动；原帖的精确 60.2°、3000 万年振荡周期和完整历史轨迹未由本轮材料全部核定。
- 两条推文的“我们被教错了”“唯一真实轨迹”属于包装。切换参考系不会推翻日心公转。原视频未逐帧观看或重建，不根据它编造精确轨道参数。

### 医学出处与读到的范围

#### 衰老与癌症

1. Carlos López-Otín、Federico Pietrocola、David Roiz-Valle、Lorenzo Galluzzi、Guido Kroemer，**Meta-hallmarks of aging and cancer**，Cell Metabolism 35(1):12–35，2023-01-03，DOI [10.1016/j.cmet.2022.11.001](https://doi.org/10.1016/j.cmet.2022.11.001)。本轮取得摘要和公开摘要节选，期刊全文访问受限。摘要已明确区分共同和拮抗特征，细胞衰老可依情境抑癌或促癌，不能只据“都和年龄相关”判作同病。
2. Yang 等，**Loss of epigenetic information as a cause of mammalian aging**，Cell 186(2):305–326.e27，2023-01-19，DOI [10.1016/j.cell.2022.12.027](https://doi.org/10.1016/j.cell.2022.12.027)，[PMC 原文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10166133/)。读到摘要、ICE 与 OSK 结果和讨论，未逐项复算全部实验。它支持特定模型中的机制解释，没有报告普通人长期保持 25—35 岁生物年龄。
3. Gong 等，**Control of Cellular Differentiation Trajectories for Cancer Reversion**，2024-12-11 在线，Advanced Science 2025, 12(3), 2402132，DOI [10.1002/advs.202402132](https://doi.org/10.1002/advs.202402132)。作者实验室 17 页原件的结果 2.8—2.9 和讨论显示：MYB、HDAC2、FOXA2 的联合抑制使 HT-29、HCT-116、CACO-2 三种癌细胞系趋向正常样分化，并在裸鼠移植模型中抑制肿瘤。normal-like 不是完整正常，也不是人体临床治愈。
4. 同一 KAIST 团队还有另一篇 [2025 年 REVERT 研究](https://pure.kaist.ac.kr/en/publications/attractor-landscape-analysis-reveals-a-reversion-switch-in-the-tr/)，DOI [10.1002/advs.202412503](https://doi.org/10.1002/advs.202412503)，基于匹配的患者来源类器官。原推只说团队，未给题名，故不确定唯一指哪篇；两篇的名称、DOI、模型不可混写。

原帖末尾推广作者自己的长寿书籍，这不是试验结果。其“癌细胞是最极端老细胞”“解决衰老就能治癌”“今天可维持人体 25—35 岁”等主张，本轮未核实到支持这些整体结论的原始数据。关系中的“挑战”只标出原帖与机制综述说法冲突，不代表原帖完成了科学反驳。

#### 首次给药

- 公司是药物开发者和供应者，具有直接商业利益。按公告，独立研究者在 ICCA 进行研究；本轮没有核实独立临床记录、完整方案、伦理审查或注册号，不能由“公告未列出”反推“肯定没有”。
- 公司“据其所知首次”的对象是专门清除衰老细胞的免疫疗法。此前已有 [Justice 等 2019 年 D+Q 的 14 人 IPF 先导研究](https://pmc.ncbi.nlm.nih.gov/articles/PMC6412088/)，DOI [10.1016/j.ebiom.2018.12.052](https://doi.org/10.1016/j.ebiom.2018.12.052)。那是小分子组合、开放标签可行性研究，不能作为 SenoMune 肽的人体疗效或安全数据。
- 公告引用 [Ichim 等 2025 年 SenoVax 动物研究](https://pmc.ncbi.nlm.nih.gov/articles/PMC12661736/)。SenoVax 是树突细胞免疫疗法，不能把它的小鼠结果直接改名为 SenoMune-0257 多肽的人体结果。
- “免疫系统识别衰老细胞”是设计目标，首次注射没有证明人体中已清除细胞、改善癌症或延寿。没有把多个疾病的潜在应用当成既定适应证。

## 第10轮：参与权、技术回顾与奇点预测的核查

日期：2026-11-09。范围为本轮基线中的3条观点。已读保存原文；以下为核查记录，最终关系已由主会话合并。

本组核查覆盖3条；最终关系采用情况见[本轮整理记录](2026-11-09-round-10.md)。Ilya与自我决定论的候选联系未通过复核，已删除；Miles与METR保留为弱关系。

### 1. Ilya：完全代办与人的参与

对应：`clips/2026-11-06-bottegamd-sutskever-humans-no-longer-participants.md`。

- 一手出处是 [Dwarkesh Patel的访谈逐字稿](https://www.dwarkesh.com/p/ilya-sutskever-2)，发布于2025-11-25。核对段落为01:07:58至01:10:47，不能把2026年的转述当成新访谈。
- 原话确实讨论一种长期设想：AI替人挣钱、表达政治诉求，再给人报告；人只说继续做，可能不再实际参与。Ilya也提到Neuralink++，并明确表示不喜欢这个方案。这是未来社会判断，没有证明脑机融合可行或此结局必然发生。
- 帖子末尾“学会自己运行agent就能继续参与”的建议，不能归给该段访谈中的Ilya。它是转述者加上的操作建议。
- 新源知识以原访谈作为直接来源；与自我决定论的候选联系没有通过第二模型复核，直接关系和对应的更底层链接均已删除。
- 自我决定论的 [Ryan与Deci 2000年原论文](https://www.selfdeterminationtheory.org/SDT/documents/2000_RyanDeci_SDT.pdf) 支持自主、胜任与联结三种基本需要；原文第74页还强调，自主意愿不等于独立做事。因而不能用它证明“委托越多，人的自主必然越少”。本轮核对了三需要定义及这一区分。

建议标题：转述Ilya 2025年访谈：AI完全代办后，人可能失去实际参与。

### 2. Karpathy：从1970年代回看AI需要几次推断

对应：`clips/2026-11-06-karpathy-predicting-ai-from-1970s-six-leaps.md`。

保存原文是一条回顾性的技术解释链，不是作者在1970年代已经作出并接受检验的预测，也没有证明这几个环节必然导向今天的大模型。只选3个原文明确提及且库中已有的源知识，不为每个历史人名各建一根。

| 复用源知识 | 核对的一手材料 | 成立的关系与边界 |
|---|---|---|
| `information-theory` | [Shannon 1948，A Mathematical Theory of Communication](https://www.cs.yale.edu/homes/yry/readings/general/shannon1948.pdf)，第一部分第3节，重印PDF第6—7页 | 原帖点名Shannon的英语n-gram近似；原著确实展示字符与词的统计近似。直接源自／强。不能改写成Shannon预测了现代大模型。 |
| `moores-law` | [Moore 1965，Cramming More Components onto Integrated Circuits](https://www.cs.cmu.edu/~18742/papers/Moore1965.pdf)，1998年IEEE重印，4页 | 原帖点名Moore 1965，直接源自／强。1965年的原口径约为每年倍增，不能把后来的两年口径倒写回去。 |
| `neural-scaling-law` | [Kaplan等2020，Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361)，本轮核对摘要 | 原帖直接列出Scaling laws，直接源自／强。Kaplan是核对该概念的代表研究，不表示帖子明确引用了这一篇；损失函数的经验规律不等于通用智能必然出现。 |

原文还提到Licklider、Rosenblatt和ELIZA。本轮没有为这些节点另建根，也没有把其所有历史细节作为新增核实结论。Shannon只读相关章节，Kaplan只核对摘要，没有声称读完这两篇全文。

### 3. Miles：奇点判断与未来五年预测

对应：`clips/2026-11-07-milesdeutscher-singularity-five-year-forecast.md`。

文章的主要概念是已有 `recursive-self-improvement`。它引用的 [Anthropic Institute：When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement) 可单独作为厂商一手报告建根 `anthropic-2026-when-ai-builds-itself`。作者为Marina Favaro、Jack Clark；本轮核对完整公开正文、脚注及2026-09-18更新。Anthropic销售模型和智能体服务，报告中的自测不能当成独立验证。

| 文章中的说法或依据 | 一手材料实际支持什么 | 整理时的写法 |
|---|---|---|
| 研究判断从51%提高到64% | Anthropic从2026年1—3月的真实研发会话中，刻意选择129个人类走弯路的节点，让模型看此前上下文提出下一步，再由另一个Claude参照后续结果裁判。51%对应Opus 4.5，64%对应Mythos Preview。 | 这是特选样本上的模型裁判结果，不能写成AI在所有研究决策上已胜过人类。 |
| 对照样本的限制 | 报告脚注8补充：另选127个人类原本走得较好的节点，模型被判更好的比例仅约20%。 | 必须与129节点结果一起保留。这是本条最关键的样本选择边界。不能从51%与64%外推2028年已拥有顶尖研究判断。 |
| 超过80%的代码由Claude写 | 报告称截至2026年5月，合入Anthropic生产代码库的代码中，超过80%可归因于Claude；这是公司自己的归因口径。 | 是代码行数占比，不能解释为AI独立选择研究目标、设计和训练后继模型的比例。代码量增长也不等于同倍生产率增长。 |
| 递归自改进已经开始 | 报告开头明确说，完整自主设计和开发后继模型尚未实现，也不必然发生；执行给定实验与选出值得做的研究仍有距离。 | “奇点已开始”保留为Miles的判断；不能安在Anthropic报告头上当成既成事实。 |
| AI能处理的任务从6.5小时到16小时以上 | [METR官方方法页](https://metr.org/time-horizons/) 将时间门槛定义为人类专家完成任务所需时间，常用50%成功率，也可看80%口径；样本以软件、机器学习和网络安全任务为主。官网提示当前题库对16小时以上的估计不可靠。 | 不是agent实际连续工作16小时，也不是整个职业的交付可靠性。保存原文未明确点名METR，本轮也没有把6.5→16+逐项对上，所以只建“相近／弱”关系，不能声称已找到直接引用链。 |

METR新根为 `metr-2025-long-task-time-horizons`。另核对了 [Measuring AI Ability to Complete Long Software Tasks论文摘要](https://arxiv.org/abs/2503.14499)：2025-03-18首发，2026-07-10更新至v4。官方方法页最后更新2026-09-08，并提示不再积极更新。本轮读摘要和方法页，没有重跑测试，也没有把它当成2026年11月所有模型的完整排名。可在更底层以“相近”连到已有 `scientific-method`，说明把笼统能力变成可测任务与成功概率的思路。

以下内容本轮留作待查，不进入源知识的一般事实：

- 2027—2031逐年预测及后面的8个判断：属于作者汇总或自己的情景预测，不是已观察事实或专家共识。
- 初级专业岗位下降29%、青年大学毕业生失业率5.3%、AI技能工资溢价62%、当月16家提供商20个模型及多位CEO引语：未逐项匹配原始统计或完整发言，不能当作已核实数据。
- 30美元到0.10美元的算术降幅约99.67%；模型质量、服务条件和时间是否可比没有核实，不能据此推出智能将永久免费。
- 6.5小时与16小时以上的具体模型、版本、成功率和测试集：未逐项匹配；METR只能帮助澄清相近指标的定义。

建议标题：作者判断奇点已开始：研发证据、反方理由与2027—2031年预测。

### 统一关系复核结果

第二模型复核12处弱关系，保留9处、删除3处，其中3处保留关系改了类型。删除的是权重空间实验与通用反馈、首例给药与机制综述、Ilya参与权与自我决定论的泛化联系；对应3条新源知识的同义向下链接也已清理。核实原始材料与建立理论关系是两步，拒绝关联不表示删除原始事实或改变阅读结论。
