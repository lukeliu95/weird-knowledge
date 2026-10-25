---
title: 用多个大模型"群体投票"预测未来时，按推理方式聚类、每类只挑 1 个代表，3 个模型就比 25 个全投票略准，调用少 88%、花费约省 80%；故意挑最不一样的反而更差
author: Nirupam Chetlapalli、Yiming Liao、Min-Chun Chen、Keke Chen（马里兰大学巴尔的摩县分校 UMBC）
url: https://arxiv.org/abs/2608.24001
source: 论文
published: 2026-08（arXiv 预印本 2608.24001 [cs.AI]，v1 2026-08-25，v2 2026-08-26；作者注明已投 IEEE BigData 2026；DOI 10.48550/arXiv.2608.24001）
saved: 2026-10-25
why: 探索日报：Luke 想看
related_principles: []
status: 未整理
kind: 观点
topic: 学习与研究
roots: []
---

## 原文

全文 14 页（正文约 9 页，参考文献 1 页，附录 A、B 约 3 页），版权归作者（arXiv 页面是 arXiv 默认的非独占分发许可）。这个仓库是公开的，按「有版权的长文」只存要点，原文看上面的链接。下面读的是 v2。

- 标题：Diverse by Reasoning: Harnessing the Wisdom of LLM Crowds for Future Prediction
- 出处：arXiv 预印本 2608.24001（人工智能 cs.AI），v2 2026-08-26；作者注明"Submitted to IEEE BigData 2026"，尚未见录用信息
- 作者：Nirupam Chetlapalli、Yiming Liao、Min-Chun Chen（前三位贡献相同）、Keke Chen；University of Maryland, Baltimore County
- DOI：[10.48550/arXiv.2608.24001](https://doi.org/10.48550/arXiv.2608.24001)
- 免费全文：[arXiv PDF](https://arxiv.org/pdf/2608.24001)
- 代码和数据：作者说"会发布"，论文里还没给地址
- 被引：0 次（OpenAlex，2026-10-25 查）；Semantic Scholar 当天限流，未查到

### 内容要点（模型概括，不是原文）

**要解决的问题**

越来越多人用大模型预测未来事件，自然会想到把多个模型凑成"群体"投票（群体智慧）。但群体智慧的经典研究强调，群体好不好看的是成员是否多样、是否独立，不是人数；很多模型行为相近，普通多数投票却给每个模型一票，相似的模型会重复发言、白花钱。所以问题是：**一开始该挑哪些模型进群体？**（第 I、II 节）

**核心想法**

1. 不按厂商、模型家族、参数量判断"多样"，而是看模型实际怎么推理：让所有模型做同一批和预测无关的练习题，把它们的推理过程转成向量，取平均得到每个模型的"行为签名"（第 III-A 节）
2. 按行为签名把模型聚成几类，每类只派一个最有代表性的模型（离同类其他成员平均距离最近的那个，叫 medoid）去投票。这样一类相似的模型不管有多少个，只占一票（第 III-B、III-C 节）
3. 拿另外两种做法当对照，检验"到底哪种多样有用"：每类挑几个彼此差别最大的（追求最大差异）；全部模型都投，但先类内投票、再各类一票（只平衡票权，不省调用）（第 III-C 节）
4. 用来分类的练习题和用来考预测的题完全分开，分类时不看任何预测题的答案（第 III、IV 节）

**主要方法**

- 25 个模型：17 个开放权重（Gemma、Llama、Qwen、DeepSeek、Kimi、GLM、MiniMax、Mistral、Nemotron 等）、8 个闭源（GPT-5.4 和 mini、Claude Haiku 4.5 和 Sonnet 4.6、Gemini 3.1 Flash-Lite 和 Pro、Grok-4.3、Mistral Medium 3.1），全部经 OpenRouter 调用（第 IV-A 节，表 I）
- 练习题：7 个通用基准（LiveBench 的推理、数学、指令遵循、数据分析，GPQA Diamond，Natural Plan，LiveCodeBench 执行）各抽 50 题，共 350 题；推理过程用 BAAI/bge-m3 转成向量（第 IV-A 节）
- 预测题：FutureX-Past 和 Bench to the Future v3 各抽 100 题，只用在 25 个模型最晚训练截止日（2026-02-16）之后才揭晓的题，揭晓时间分别是 2026-03-07～07-28 和 2026-05-05～07-01，保证模型不可能背过答案（第 IV-A3 节）
- 聚类用 K-means++ 和层次聚类两种；对照组有 25 个全投票、凭成绩挑出的单个"专家"模型（五折交叉验证选）、同样大小的随机组合（抽 1000 次）（第 IV-A 节）
- 花费按服务商实际扣的钱算，不是按标价估（第 IV-D 节）

**主要结果**

| 项 | 数字 | 出处 |
|---|---|---|
| 3 个代表投票（K-means++，K=3） | FutureX-Past 0.302，BTF-v3 0.810，两项综合排第 1 | 第 IV-C 节，表 III |
| 25 个模型全投票 | 0.296，0.800 | 表 III |
| 凭成绩挑的单个专家模型 | 0.265，0.790 | 表 III |
| 同样 3 个模型随机挑 | 0.274（K-means++ 分组）/ 0.285（层次分组），0.771 / 0.798 | 表 III |
| 每类挑 4 个最不一样的（共 12 个） | 0.272，0.780，比同样大小的随机组合还差（FutureX-Past 上只比 5% 的随机组合好） | 表 III、第 IV-C 节 |
| 先类内再类间投票（25 个全用） | 0.284，0.790，不如直接全投票 | 表 III |
| 被选中的 3 个代表 | qwen-2.5-72b-instruct（12 个模型的类）、kimi-k2.6（8 个的类）、gpt-5.4（5 个的类） | 第 IV-C 节 |
| 和同样大小随机组合比 | BTF-v3 上排第 88 百分位，FutureX-Past 第 83 百分位；随机抽，大约每 8 次就有 1 次能追平 | 第 IV-C 节 |
| 调用次数 | 300 次对 2500 次，少 88% | 表 IV |
| 花费（每 100 题） | FutureX-Past 2.10 美元对 10.96（0.19 倍）；BTF-v3 4.51 对 21.26（0.21 倍） | 表 IV |
| 花费主要看选了哪个模型 | 不同模型单次价格差约两个数量级；最贵的一个模型自己就比 3 个代表合起来还贵（BTF-v3 每 100 题 6.46 美元） | 第 IV-D 节 |
| 只用 17 个开放权重模型投票 | 9.66 美元、0.790，便宜了但更不准，开不开源不能当省钱的替代指标 | 第 IV-D 节 |
| 群体内部推理越不一样、成绩越好吗 | 498 个候选组合、固定人数后，FutureX-Past 上相关 +0.211，七个人数档都是正的；BTF-v3 上没有（约 0） | 附录 A |

作者的结论：群体怎么组成可能比人数多少更重要；有用的是"有代表性地覆盖不同推理方式"，不是"越不一样越好"（第 V 节）。

**需要说清楚的边界**

- 领先幅度很小：3 个代表比 25 个全投票只高 0.006（FutureX-Past）和 0.010（BTF-v3），每个基准只有 100 题（表 III、第 V 节）
- 效果只在 K-means++ 分组下成立。换成层次聚类，同样的做法在 BTF-v3 上拿到全表最高 0.830，但在 FutureX-Past 上掉到第 8（0.270）（第 IV-C 节）
- FutureX-Past 上平票很多：K=3 时 100 题里有 28～32 题靠平票规则决定；层级越难平票越多（第 1 级 22.3%，第 4 级 80.6%）。不同平票规则带来的分数差，和各方法之间的差距差不多大。作者说论文用的按字母排序规则恰好偏不利，结果"如果有偏，也是对自己不利"；BTF-v3 用中位数，不存在平票（第 IV-B 节、附录 B）
- 聚类指标最好的不一定最好用：轮廓系数最推荐 K=2，但 K=2 时 72 题靠平票决定，成绩在所有设置里最差。作者以平票太多为由改选 K=3，并拿下游成绩佐证（第 IV-B 节）
- 和"事先知道哪个模型最好"比：如果能提前选中最好的单个模型，BTF-v3 上 0.820、只花 0.35 美元，比 3 个代表更准、便宜约 13 倍；但不看答案选不出来。能实际做到的"专家"做法是 0.790、1.31 美元（第 IV-D 节）
- 附录 A 只证明"多样和好成绩相伴"，不是挑组合的规则：固定人数后按差异大小挑，并不能稳定赢随机组合（附录 A-D）
- 作者自己承认的局限：行为签名是把推理过程向量取平均，可能抹掉随任务变化的差异；只构造一个固定群体，没有按题目动态挑；只测了 25 个模型、两个预测基准各 100 题（第 V 节）
- 签名只代表"看得到的推理文字"，作者明说不代表模型内部真实的推理过程（第 III-A 节）

**作者明说引用的前人工作**（供整理时溯源参考）

- 群体智慧：Surowiecki, The Wisdom of Crowds, 2004
- 小而精的群体：Goldstein、McAfee、Suri, The Wisdom of Smaller, Smarter Crowds, 2014；Davis-Stober 等, The Composition of Optimally Wise Crowds, 2015；Galesic 等, Smaller Crowds Outperform Larger Crowds and Individuals in Realistic Task Conditions, 2018
- 从可观察行为推断人群多样性、聚类后选代表：Bhatt 等, 2019（预测英超梦幻足球队长，ICWSM；作者名单里有 K. Chen）
- 大模型群体预测可比人类群体：Schoenegger 等, Wisdom of the Silicon Crowd, Science Advances, 2024（含 Tetlock）
- 自洽性（同一模型多条推理取多数）：Wang 等, 2023；多 agent 辩论：Du 等, 2024；Mixture-of-Agents：Wang 等, 2025
- 换投票规则：Zhao 等, 选举方法分散多 agent 决策, 2024；Ai 等, Beyond Majority Voting, 2025
- 预测基准：Autocast（Zou 等, 2022）、Halawi 等接近人类水平的预测（2024）、ForecastBench（Karger 等, 含 Tetlock, 2025）、Bench to the Future（2025）、FutureX（2026）
- 轮廓系数：Rousseeuw, 1987；聚类稳定性：Hennig, 2007

## 溯源

（整理时填写，存的时候留空）
