# 20个真实事件：查知识库后，判断有没有更准

> 2026-11-24，日本时间。结论：**有小幅改善迹象，还不能确认稳定提升。** 直接判断两遍是19/20、20/20，查库两遍是20/20、20/20；差别仅来自一个事件的一次判断；解释辅助评分两组打平。

## 这次能说明什么

用同一模型、同一事实卡对比“直接判断”和“额外看已有基础知识”。查库组平均100%，直接组97.5%，高2.5个百分点。按20个事件配对统计，90%区间为0～7.5个百分点，包含没有改善；20个事件中1个偏向查库、19个持平，双侧符号检验p=1。样本少、基线接近满分，不能把这点差距说成能力已经提升。

这里的“直接判断”是同一个模型不看本库，并非早期版本lukeeMind；这轮也没测未来预测、自己找事实或真实业务决策。没有改生产入口、模型默认或已确认原则。

## 主结果

两组都用当前决定判断模型Opus 5.5，推理强度相同。共20个真实事件，每组独立做两遍，80份判断全部有效。正确性是与提前冻结的S/C/U标签一致；不是人类主观觉得说得好。

| 组别 | 次数 | 正确数 | 正确率 | 概率误差Brier，越低越好 | 有效回答 |
|---|---|---|---|---|---|
| 直接判断 | 第1遍 | 19/20 | 95% | 0.07891 | 20/20 |
| 直接判断 | 第2遍 | 20/20 | 100% | 0.04439 | 20/20 |
| 查知识库 | 第1遍 | 20/20 | 100% | 0.03896 | 20/20 |
| 查知识库 | 第2遍 | 20/20 | 100% | 0.05079 | 20/20 |

先把同一事件的两遍取平均，再对20事件配对，重复运行不当成40个独立事件：

| 指标 | 直接判断 | 查知识库 | 差异及不确定性 |
|---|---|---|---|
| 平均正确率 | 97.5% | 100% | 查库+2.5个百分点；90%配对区间0～7.5个百分点 |
| 平均Brier | 0.061650 | 0.044875 | 查库误差低0.016775；90%区间−0.010155～0.061315，仍包含无改善 |
| 事件胜／负／平 | — | 1／0／19 | 差别集中在一道题，不能当成广泛提升 |

Brier比较三类概率与实际标签的距离，0最好、2最差。第一遍查库更好，第二遍直接判断的Brier反而更低，因此概率优势也没有稳定复现。重采样中准确率差为正的比例64.17%、为零35.83%；这只是本题集的重采样结果，不是“知识库更有用的真实概率”。

## 唯一改变结论的案例：日本微软四天工作周

待判断：“用电减少23.1%，全部是每周少工作一天造成的。”材料还列了会议规则、Teams等同时变化，用电比较年份也不同，缺少能拆分单项影响的对照。因此提前定的答案是**材料不足U**：不能确定全是它造成，也没有证据证明它绝对不是。

- 直接判断第一遍判C，写“全部归因与材料直接矛盾”；但边界又承认“只是无法支持全部归因”。第二遍自己改为U。
- 查库两遍都判U，都自报用了A/B测试知识。它指出没有只改变工作天数的对照，也没有相反的分解结果。

这一次查库组避免了“没证实”与“已证伪”的混淆，直接组的解释也已抓到主要限制。差别主要是证据等级标签，不能解释成已证明真实业务决策更好，更不能排除一次重跑波动。[原始公告](https://news.microsoft.com/ja-jp/2019/10/31/191031-published-the-results-of-measuring-the-effectiveness-of-our-work-life-choice-challenge-summer-2019/)和四份完整回答可在题集及运行记录中回查。

## 20个事件逐题结果

S=材料支持，C=材料反驳，U=材料不足；每格依次为第一遍／第二遍。主张是测试编写者提出的推论，不是原作者引语。完整事实、主张和阅读范围见[cases.json](cases.json)，标准答案见[gold.json](gold.json)。

| 题号 | 一手事件来源 | 事件/论文日期 | 标准答案 | 直接判断 | 查库判断 | 提供片段数 |
|---|---|---|---|---|---|---|
| E01 | [GitLab生产数据库误删](https://about.gitlab.com/blog/postmortem-of-database-outage-of-january-31/) | 2017-01-31 | C | C / C | C / C | 1 |
| E02 | [Fastly合法配置触发全球故障](https://www.fastly.com/blog/summary-of-june-8-outage) | 2021-06-08 | S | S / S | S / S | 4 |
| E03 | [AWS内部网络重试拥塞](https://aws.amazon.com/message/12721/) | 2021-12-07 | S | S / S | S / S | 2 |
| E04 | [Atlassian备份恢复耗时](https://www.atlassian.com/blog/how-we-build/post-incident-review-april-2022-outage) | 2022-04-05 | C | C / C | C / C | 2 |
| E05 | [Discord消息库迁移](https://discord.com/blog/how-discord-stores-trillions-of-messages) | 2023-03-06 | U | U / U | U / U | 1 |
| E06 | [GitHub跨中心切换故障](https://github.blog/news-insights/company-news/oct21-post-incident-analysis/) | 2018-10-21 | S | S / S | S / S | 2 |
| E07 | [eBay付费搜索现场实验](https://www.nber.org/papers/w20171) | 2014-05 | C | C / C | C / C | 1 |
| E08 | [Facebook广告因果估计对照](https://www.kellogg.northwestern.edu/faculty/gordon_b/files/fb_comparison.pdf) | 2018-04 | C | C / C | C / C | 2 |
| E09 | [DoorDash区域时间切换实验](https://careersatdoordash.com/blog/switchback-tests-and-randomized-experimentation-under-network-effects-at-doordash/) | 2018-02-13 | S | S / S | S / S | 2 |
| E10 | [Uber消费者剩余估计](https://www.nber.org/papers/w22627) | 2016-09 | U | U / U | U / U | 1 |
| E11 | [日本微软四天工作周试行](https://news.microsoft.com/ja-jp/2019/10/31/191031-published-the-results-of-measuring-the-effectiveness-of-our-work-life-choice-challenge-summer-2019/) | 2019-10-31 | U | C / U | U / U | 1 |
| E12 | [Trip.com混合办公随机实验](https://www.nature.com/articles/s41586-024-07500-2) | 2024-06-12 | S | S / S | S / S | 2 |
| E13 | [三家企业AI编程随机试验](https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/) | 2025-06 | C | C / C | C / C | 2 |
| E14 | [METR资深开源开发者试验](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) | 2025-07-10 | C | C / C | C / C | 3 |
| E15 | [Google Willow纠错结果](https://research.google/blog/making-quantum-error-correction-work/) | 2024-12-09 | S | S / S | S / S | 1 |
| E16 | [氮掺杂镥氢化物论文撤稿](https://www.nature.com/articles/s41586-023-06774-2) | 2023-11-07 | U | U / U | U / U | 1 |
| E17 | [RECOVERY地塞米松分组结果](https://www.recoverytrial.net/news/low-cost-dexamethasone-reduces-death-by-up-to-one-third-in-hospitalised-patients-with-severe-respiratory-complications-of-covid-19/) | 2020-06-16 | C | C / C | C / C | 2 |
| E18 | [NIF首次点火能量口径](https://lmf.llnl.gov/news/iaea-webinar-explores-nifs-ignition-energy-gain-breakthroughs) | 2022-12-05 | C | C / C | C / C | 1 |
| E19 | [NASA DART改变双小行星轨道](https://www.nasa.gov/news-release/nasa-confirms-dart-mission-impact-changed-asteroids-motion-in-space/) | 2022-10-11 | S | S / S | S / S | 1 |
| E20 | [英国四天工作周试点](https://www.cam.ac.uk/stories/fourdayweek) | 2023-02-21 | S | S / S | S / S | 0 |

## 检索实际做到哪一步

冻结1098条源知识，其中1093条出处标记可用。按题目与事实先从定义索引取40个候选，再选0～4段；不拿标准答案做查询。19题最终得到32段材料，涉及26条不同知识；E20没有有效片段，仍计入全部结果。查库40份回答中23份自报使用了材料，这不等于已经客观证明每段影响了推理。

选材有明显问题：4批各试两次，8次都出现至少一个跨题或越界编号，按提前写定的规则剔除后才生成材料；最终一次输出合计剔除13个编号。没有按答案手工补材。部分材料关系偏间接，例如量子纠错题检索到的是科学核验流程。因此这轮比较的是**这一套实际检索方式的效果**，不能称为完整知识库的最佳效果，也不能把未测出稳定提升全归因于知识没价值。[固定材料](knowledge-packets.json)、[正式前检查](preflight-review.md)。

## 解释的独立评分

80份解释先打乱顺序、隐藏组别、概率和知识编号，由未编写答题脚本的独立agent评分。每项0/1，下一步不要求照抄gold示例。理论用词可能暴露组别，因此属于不完全盲审、模型辅助评分。

| 组别 | 抓对关键事实 | 保留主要边界 | 可验证下一步 | 总分 |
|---|---|---|---|---|
| 直接判断 | 39/40 | 40/40 | 40/40 | 119/120 |
| 查知识库 | 39/40 | 40/40 | 40/40 | 119/120 |

两组都是119/120，没有测出解释质量增益。各有一次事实项扣分：直接组是上述E11；查库组是E05，把“多项变化同时发生、尚未拆分贡献”写成“改善并非单靠换库”。后者虽然U标签正确，理由仍把未知的因果份额说满，说明查库也可能出现解释越界。

解释得分只作为辅助，不能凭它宣布客观正确率或通用判断能力提升。评分逐份理由和揭盲映射都保留在[explanation-scores.json](explanation-scores.json)。

## 调用和成本

| 阶段 | 订阅模型调用 | 输入token，含创建/读取缓存 | 输出token | CLI按API价折算 |
|---|---|---|---|---|
| 准备选材 | 8 | 268,448 | 2,797 | $1.1566 |
| 正式答题 | 16 | 60,758 | 18,786 | $0.8617 |

共24次订阅调用，输入329,206 token、输出21,583 token，API折算合计$2.0182；使用现有Claude Code订阅，没有新增收费接口，折算价不是新增账单。正式16批零失败、零重试；8次选材错误都保留并计入用量。未知用量调用为0。直接组答题输入19,050 token，查库组41,708 token，约2.19倍；正式答题两组共122秒墙钟时间，另有选材与核查时间。

独立审查与解释评分由Codex协作agent完成，未另开外部付费评分接口；当前工具不提供这部分完整token账单，不编总费用。精确调用元数据见[scores.json](scores.json)。

## 这轮的边界与后续判断

1. 这20题定向选择，工程、商业和科研都有，但不是现实事件的随机样本。很多答案直接写在事实卡里，措辞也可能提示标签，题目对强模型偏容易。
2. 查了本库未直接存过同事件，不能排除模型预训练已知道；同模型两组能控制部分影响，无法证明首次见到事件。
3. 没有等长度无关材料组，不能拆开“基础知识帮助”和“额外上下文影响”；每批5题也可能相互影响。
4. 20事件中的一题差异无法建立通用判断能力、未来预测或业务收益的结论。解释评分只是辅助，不用它替代准确率。
5. 本轮无论结果好坏都保留两遍和全部失败，正式答题前锁定输入；没有看到成绩后换题、改提示或挑最好的一遍。

**当前可下的判断：lukeeMind在这些给定事实的判断题上表现稳，查库出现一个避免分类错误的例子，但“知识积累已经让判断更准”还没有足够证据。** 更有区分度的下一轮应在开跑前另定：证据冲突、条件缺失、容易套错原则的事件，并先改好跨题选材问题；不因为这次的小幅差距就改默认行为。

## 可回查文件

- [冻结协议](protocol.md)、[冻结哈希](frozen.json)、[知识快照清单](corpus-manifest.json)、[同源排除检查](novelty-audit.json)。
- [全部主评分与逐事件概率误差](scores.json)、[80份隐藏组别解释](judgments-blind.json)、[辅助解释评分](explanation-scores.json)、[运行原始记录目录](runs/)。
- 评测入口：`python3 -X utf8 tools/evolve/event_eval.py self-test`、`run`、`score`。已完成运行再次执行会读取匹配记录，不重新调用模型；只有输入/冻结哈希一致才接受。
