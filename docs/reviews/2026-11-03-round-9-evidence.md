# 第 9 轮整理：出处核查与边界

2026-11-03。以下为模型核查摘要。核实出处不等于独立复现实验、运行 Lean 或完成临床医学审稿。

## 第 9 轮：语言、记忆和代码审查的溯源核查

2026-11-03。以下是分组阶段的核查结论，现已统一合并。

| 条目 | 核对的一手材料 | 结论和边界 |
|---|---|---|
| Clark 论文、李继刚转述 | [Clark 等 arXiv 正文](https://arxiv.org/html/2610.29162v1)，重点复查第 2—5、7 节及附录 B、C | 长度惩罚实验是小模型概念验证；前沿模型的训练病因仍是推测。没有直接做人的阅读测验，也不能把英语结果直接当中文写作处方。 |
| 同上：均匀信息密度 | [Levy、Jaeger 的会议原件](https://proceedings.neurips.cc/paper/2006/hash/c6a01432c8138d46ba39957a8250e027-Abstract.html)，已打开 8 页 PDF；Jaeger 2010 的 DOI、卷期页码另经 Crossref 核对 | 保留可省略词以分摊理解负担，和缩短依存距离是两个不同概念；会议年 2006 与论文集年 2007 不混写。 |
| 同上：依存距离 | [Futrell 等 PNAS 原件](https://doi.org/10.1073/pnas.1502134112) | 37 种语言整体短于随机排列；作者不声称所有句子都采用全局最短距离，也不声称这是他们首先发明的想法。 |
| 代码审查长文 | [三位作者的官方博客，2026-10-15](https://claude.dev/blog/solving-code-review-at-anthropic/) | 可复用已有 osmani-2026-claude-code-code-review。正文是六层检查加回滚；第七点是兜底。回滚率改善是厂商团队自报；2,500→30,000 是 Anthropic 单体仓库的数据，不能安到独立的 Claude Code 仓库头上。 |
| 代码审查与瑞士奶酪 | [Reason 2000 原文](https://pmc.ncbi.nlm.nih.gov/articles/PMC1117770/) | 多道防线含义相近，但官方长文没有直接引用 Reason，关系标“相近、弱”，交第二模型复核。 |
| Raw-RAG | [Bao 等论文](https://arxiv.org/html/2610.30755v1)，核对正文第 3—6 节及附录 F；[原始 RAG 论文登记页](https://arxiv.org/abs/2005.11401) | 六组领先是相对被比较的记忆系统；四个离线对话基准不代表所有交互记忆任务。证据预算、上下文位置和读者能力影响部分诊断，不能把残差全部叫作“压缩丢信息”。没有逐项复算 62 页论文的所有表格。 |

### 建议订正

1. 李继刚条目的标题缩窄为“论文转述：AI 文字难懂的可能原因，以及四条写作建议”。四条建议来自转述者，尚未经过论文验证。
2. Raw-RAG 标题补上“四个对话记忆基准”的适用范围。
3. Clark 存档概括把 object relative clause 简称为“宾语从句”，容易与附录 C 另一个训练结构 complement clause 混淆。原文不动，在溯源边界里说明“宾语关系从句”。

## 第 9 轮 · 工程组核查记录

> 2026-11-03。以下是分组阶段的核查结论，现已统一合并。8 条溯源，Google 六层另按教程归档；4 个新源知识、8 个已有源知识，11 处弱关系交第二模型复核。

### 一手来源与边界

| 条目 | 核查 | 边界 |
|---|---|---|
| 宝玉转述 Manus | [Tao Zhang 官网长文](https://manus.im/blog/rebuilding-manus-with-manus)，2026-10-30 英文版，已读全文 | 原帖是宝玉提炼；公司原件保留人工合并、发布批准，承认注意力碎片化。中文原版微信链接遇到验证码，英文版不能替中文原版核定全部数值。 |
| Tw93 中英规则 | [作者博客后续版](https://tw93.fun/2026-10-29/practice.html)，2026-10-29；[Claude Code 官方实践](https://code.claude.com/docs/en/best-practices) | 作者博客是 21 条，存档原推是 20 条，不替换。英文存档有 commll、looguessing 等缺字、连写，按原样保留；只分析仍明确的主张。 |
| 客户端选型 | [作者博客](https://tw93.fun/2026-10-22/desktop.html)，已读全文；[Dijkstra 原文 EWD447](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD447.html) | 多端各写原生代码是作者场景选择；效率、性能、体验的“不可能三角”没有形式定理证据，不写成普适定律。价格、证书地域等时效细节未作为本次核心结论。 |
| QingYue 转述 Thorsten Ball | [Ball 原 X Article](https://x.com/thorstenball/status/2114386050638336082)；通过 opencli twitter article 成功取得全文 | 原文有目标优先、自建迭代工具、证据与高风险审查；属于个人经验，不等于可以不设权限或测试边界。全文备份 thorsten-article.json 留在本机。 |
| Ronny 逐瓶颈改工具链 | 原推已保存全文；[TOC Institute 五聚焦步骤](https://www.tocinstitute.org/five-focusing-steps.html) | 原推没有引用 Goldratt，和约束理论只标相近、弱；链接指向的扩展 X Article 没取得正文，不据它补内容。 |
| Lesse 工程问题 | [本人原文](https://www.katelynlesse.com/blog/new-problems-for-engineers-to-solve)，2026-10-25；[本人安全展开文](https://www.katelynlesse.com/blog/secure-agents-architecture-and-sandboxing)，2026-09-13 | 四类问题是展望，不是已上线能力或部署规模统计。认证和长期授权不是同一问题。 |
| Stripe 接入工厂 | [Stripe 官方原件](https://stripe.dev/blog/stripes-payment-method-factory-orchestrating-agents-for-repeated-custom-integrations)，2026-09-30，已读全文 | 20→4 天是两名工程师做同一前端 API 接入；半年→2–6 周是整体周期。不能混成一组通用倍数，也不是随机试验。知识更新由模型提议，工程师仍判断。 |
| Google 六层（归档） | [Google Codelabs](https://codelabs.developers.google.com/codelabs/long-running-agents/instructions)；[Google 官方源码中的恢复设计](https://github.com/google/adk-python/blob/main/.agents/skills/adk-architecture/references/architecture-workflow-resumability.md) | 已找到对应长程教程，但未找到原推所称 9 页 PDF。恢复有至少一次语义，外部操作要自己幂等；不能把 finished steps never run twice 推广成任何副作用永不重跑。 |

### 复用理论的核实

- 关注点分离：Dijkstra 本人档案 EWD447 明说应逐个方面深入分析，不是忽略其他方面。
- 职责分离与最小权限：[Saltzer 与 Schroeder 作者网页](https://web.mit.edu/Saltzer/www/publications/protection/Basic.html)。将其用于不同模型的编码和复核是类比，不能证明两个模型的错误独立。
- 约束理论：TOC Institute 的五聚焦步骤解释了定位当前限制、先改善限制、限制转移后重新识别。本轮只将 Ronny、Manus、客户端验证与其关联为弱关系。
- Claude Code 官方实践：当前文档区分模型读取的建议和工具强制的规则，并要求可执行检查。此文网址从 2025 文章重定向而来，不把持续更新正文的所有措辞都归给 Boris Cherny 2025 原文。
- 构建高效的智能体：Stripe 的代码编排与现有源知识所述“代码预设工作流、模型决定开放步骤”相近；无证据表明 Stripe 引用过该文，标弱。

### 修改建议

1. Manus 标题加“宝玉转述”，避免把提炼当原作者一手稿。
2. Google 标题降为“推文归纳”，9 页 PDF 归属待核实。
3. Tw93 英文不修补原文，不静默换成博客后续版；在溯源说明文本缺损。


### Manus 时间关系补核

原推发表于 10-27、保存于 10-29，所引短链重定向到微信中文原作。微信正文仍遇验证码，首发日未核实，不能仅凭转载报道确定为 10-26。10-30 官网英文版是后来读取的校对材料，故该关系降为“相近、弱”，不再标“直接源自、强”。源知识保留已核实的英文发布日期，并列明未读中文原作链接及边界。

## 主会话核查：内存与赫拉利

核查日：2026-11-03。未改原文。

- [Marshall 公版原著第五篇第五章](https://www.econlib.org/library/Marshall/marP.html?chapter_num=33)，§§5–8 解释短长期设备调整差别；[第六章](https://www.econlib.org/library/Marshall/marP.html?chapter_num=34)核对派生需求。只据此说明机制，不替具体内存预测背书。
- [SK 海力士 2026-08-07 扩产公告](https://news.skhynix.com/en/fab-facility-investment-2026/)，Y2 计划 2027-07 开工、2029-06 首间洁净室开放。这是厂商计划，不等于满产日期，不能当整个行业的统一周期，也不能证明全行业售罄至 2029。
- [Harari 署名原文](https://www.ynetnews.com/article/bkszgnrvn)，已读公开正文，核对语言、法律、货币、AI 叙事和影响关系。只用模型概括，不转载全文。
- [Harari 官方视频](https://www.youtube.com/watch?v=LWiM-LuRe6w)仅核对说明：2023-04-29 演讲、2023-05-14 发布；未声称观看或取得完整字幕。
- [Searle 出版社 2010 章摘要](https://academic.oup.com/book/5336/chapter-abstract/148101790)、[2011 作者公开节选](https://academic.oup.com/analysis/article-abstract/71/4/733/159943)核实语言、制度事实、共同承认关系；全文未取得。与 Harari 只标相近，不写直接继承。
- RAM 帖的 1%、机器人将消费大部分内存、全行业 2029 售罄及 iPhone 涨价未核实；赫拉利转述里的“A 社实验”不明确，未擅指某篇论文。

## 第 9 轮：科学发现与风险材料核查

> 核查日期：2026-11-03。范围为本组 4 条公开内容。分组阶段只交查证结果，现已由主会话合并；原文保留。核查到一手出处不等于独立复现研究、检查 Lean 或完成医学全文审稿。

### 一、三项科学公告与 ETH 解读

对应条目：

- clips/2026-10-29-gdb-openai-three-scientific-discoveries.md
- clips/2026-10-29-rishabhkio-why-3sat-result-matters.md

[OpenAI 2026-10-26 官方公告](https://openai.com/index/building-scientific-understanding-with-academic-communities/)确实公布数学、计算机和物理三类材料，但发布策略不同：

| 项目 | 原件明确说的 | 本轮结论 |
|---|---|---|
| 调和分析 | 公布自然语言材料及 Lean 证明材料，让学者自行组织理解 | 是公开研究材料，不能把公布当共同体已完成评审 |
| ETH | 公开自然语言稿与 Lean 材料，Impagliazzo、Paturi、Williams 组织外部工作组，邀请社区检查 | OpenAI 声称反驳 ETH；本轮未独立证明，也未运行 Lean |
| 量子场论 | 外部工作组先组织理解，暂缓公开模型原始产物 | 不能说三项都已同等完整公开并独立验证 |

原始理论已经查到提出者自己的论文：

- [Impagliazzo 与 Paturi，On the Complexity of k-SAT，2001，9 页](https://cseweb.ucsd.edu/~paturi/myPapers/pubs/ImpagliazzoPaturi_2001_jcss.pdf)，DOI 10.1006/jcss.2000.1727；第 1—2 页定义 ETH 为固定 k≥3 的 k-SAT 没有次指数算法，期刊前有 1999 会议版。
- [Impagliazzo、Paturi 与 Zane，Which Problems Have Strongly Exponential Complexity?，2001，19 页](https://cseweb.ucsd.edu/~paturi/myPapers/pubs/ImpagliazzoPaturiZane_2001_jcss.pdf)，DOI 10.1006/jcss.2001.1774；初版 FOCS 1998。
- [Paturi 的论文目录](https://cseweb.ucsd.edu/~paturi/myPapers/index.html)同时列了会议与期刊年份。因此不能笼统说恰好 25 年前某一篇论文首次提出全部概念。

[2026-10-25 公开稿](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf)与[Lean 范围说明](https://raw.githubusercontent.com/openai/math/main/lean/docs/378.md)应分别引用。已读的范围说明给出：固定 k、规范编码 k-CNF、编码长度 L、变量数 n，确定性精确计数时间为 (L+1) 的多项式乘以 2 的 O_k(n(loglog n)^2/sqrt(log n)) 次方，空间为 (L+1) 的多项式。范围说明另列稿件中更尖锐的时间界。

需要保留三个边界：

1. 次指数不是多项式；不等于 P 与 NP 问题已解决，也不直接保证日常规模可用。
2. 原有“如果 ETH 成立，那么某问题很难”的条件定理不会因此变成逻辑错误；被改变的是把前提当真时的解释和推论用途。
3. “存在原始出处”与“学界已完成独立核验”不同。本轮前者已核对，后者未获证据，不写已最终确认。

### 二、生医清单：十项逐项对照

对应条目：clips/2026-10-29-m-goes-distance-biotech-breakthroughs-last-six-months.md。

下面是中文核查摘要，不是原文。该帖不附各项原始出处，匹配是本轮根据数字和描述查得；不能因此声称作者本人读过这些论文。

| 原帖声称 | 对应原始材料及核查结果 | 必须写清的边界 |
|---|---|---|
| 每日口服药使转移性胰腺癌中位生存 13.2 对 6.6 个月 | [RASolute 302 原论文摘要](https://pubmed.ncbi.nlm.nih.gov/42223072/)，DOI 10.1056/NEJMoa2605555。随机 500 人，数字对应 RAS G12 亚组；全体为 13.2 对 6.7 个月 | 人群为既往治疗后的转移性胰腺导管腺癌；中位改善不是治愈，也不是所有胰腺癌人群的效果。期刊正文403，本轮只读摘要 |
| 一次基因编辑让 HAE 发作减少 87%，62% 半年无发作且停预防药 | [Intellia 2026-06-13 原始数据发布](https://ir.intelliatx.com/news-releases/news-release-details/intellia-therapeutics-reports-additional-positive-phase-3)，对应 [NEJM HAELO 论文](https://doi.org/10.1056/NEJMoa2600931)。52 对 28 人，观察第5—28周 | 厂商一手发布，商业利益为基因编辑治疗；87%是对安慰剂的发作率相对减少，62%是该观察期比例，不是永久治愈。未读付费全文 |
| 一次胆固醇基因编辑降 LDL 最多 62%，持续超一年 | [Lilly 2026-05-25 VERVE-102 Heart-2 发布](https://investor.lilly.com/news-releases/news-release-details/single-dose-lillys-pcsk9-base-editor-verve-102-reduced-pcsk9-88)。开放标签1b期35人，62%来自最高剂量组；部分人随访最多18个月 | 厂商一手声明；不是所有35人都最高剂量、都满18个月。替代终点 LDL 改善不等于已证明减少心梗或终身安全 |
| 个体化 mRNA 疫苗在1137人黑色素瘤3期胜过Keytruda单用 | [Merck 与 Moderna 2026-08-19 INTerpath-001 发布](https://www.merck.com/news/merck-and-moderna-announce-phase-3-interpath-001-trial-of-intismeran-autogene-plus-keytruda-met-endpoints-of-recurrence-free-survival-rfs-and-distant-metastasis-free-survival-dmfs-in-patient/)。1137人，2:1随机，intismeran加pembrolizumab，RFS和DMFS达标 | 厂商一手声明；术后完全切除IIB—IV期患者的辅助治疗，不能写成疫苗单药治疗所有癌症；总生存还要继续观察 |
| retatrutide 3期减重约28% | [Lilly 2026-05-21 TRIUMPH-1 发布](https://investor.lilly.com/news-releases/news-release-details/lillys-triple-agonist-retatrutide-delivered-powerful-weight-loss)。12mg/80周疗效估计为28.3%；同页治疗策略估计为25.0% | 厂商数据；剂量、时间和统计口径不能省。治疗策略口径包含停药等；不是所有人都减28%。这是试验结果，不自动等于已获上市批准 |
| AI设计药已进3期 | [Insilico 2026-07-07 原始公告](https://insilico.com/news/xmjsn4l091-insilico-initiates-phase-iii-clinical-tr)对应 rentosertib/ISM001-055/INS018_055，TNIK抑制剂，GENESIS-IPF-3，NCT07687459、CTR20262475 | 厂商一手声明；进入3期不是通过3期，不代表药已有效获批。适应证为特发性肺纤维化 |
| 生发口服药通过第二个3期 | [Veradermics 2026-10-19 SEC披露](https://www.sec.gov/Archives/edgar/data/1827635/000182763526000036/exhibit991datarelease101926.htm)对应缓释口服米诺地尔VDPHL01，304研究536人、6个月安慰剂对照结果阳性 | 精确说法是Phase2/3的302研究和Phase3的304研究，两项注册研究，不是两个纯Phase3；试验阳性不是FDA已经批准 |
| 可让部分直肠癌患者免去手术、放化疗的免疫药已获批 | [FDA 2026-10-19 直接批准通知](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-grants-accelerated-approval-dostarlimab-locally-advanced-rectal-cancer)对应dostarlimab/Jemperli | 是加速批准，限定FDA认可检测确认MSI-H/dMMR、II/III期局晚直肠癌；需密切监测，并非每位患者均免后续治疗 |
| 猪肾让一人271天不用透析 | [Mass General Brigham研究团队原始说明](https://news.massgeneralbrigham.org/en/pig-kidney-xenotransplant-bridge-to-human-transplant)，对应 [Lancet病例](https://doi.org/10.1016/S0140-6736(26)01295-X) | 事件发生于2025年1月移植后的271天，2026年1月已换成人肾；2026是病例报告。不能写十项全是近半年发生，更不能说猪肾已是永久替代方案 |
| 人类细胞能把染色体大小DNA传给邻居并改变行为 | [作者机构原论文摘要](https://utsouthwestern.elsevierpure.com/en/publications/genome-instability-triggers-intercellular-dna-transfer-between-hu/)，[团队2026-05-19说明](https://www.utsouthwestern.edu/newsroom/articles/year-2026/may-cri-human-cells-dna.html)，DOI 10.1016/j.cell.2026.04.041 | 原件支持培养细胞间大片段DNA转移、稳定遗传和性状变化；“染色体片段”不等于完整染色体，体内普遍性和疾病意义仍待研究，不是已有人体升级技术 |

综合判断：十项大多能找到对应进展，但它们横跨细胞实验、早期人体试验、三期结果和监管批准，不能混作“全部成熟”。“人体是软件问题”是作者的类比与预测，十项材料不能共同证明这一命题。本组正式源知识只选三项最具体的研究（Daraxonrasib、HAELO、DNA转移），不为十个新闻各造一个理论。

上述边界已并入本轮公开记录，正式条目也附有入口。

### 三、匿名黑帽邀约与模型微调风险

对应条目：clips/2026-11-01-jun-song-black-hat-offer-post-train-open-models-exploit-data.md。

- 邀约、报酬、数据规模以及作者自述GLM-5.3项目表现，只有原帖陈述，没有可独立核验的任务、数据、指标或客户身份。本轮不把它们升格为事实。
- [Qi等，2023原论文](https://arxiv.org/abs/2310.03693)及[ICLR 2024正式版](https://proceedings.iclr.cc/paper_files/paper/2024/file/83b7da3ed13f06c13ce82235c8eedf35-Paper-Conference.pdf)确实研究了定制微调导致安全行为退化。已读[HTML正文](https://arxiv.org/html/2310.03693v1)中概念与实证说明。
- 研究对象和任务不同；有害内容服从、安全对齐退化，不等于现实网络攻击成功率。本条只能标“相近·弱”，交第二模型复核。
- 论文支持机制风险，不能证实匿名故事，更不能由此推出后训练数据越多实际攻击越强的普遍规律。
