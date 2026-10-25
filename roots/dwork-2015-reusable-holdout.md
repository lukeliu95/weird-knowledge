---
name_zh: "可复用的留出集（自适应数据分析中的泛化与留出集复用）"
name_en: "Generalization in Adaptive Data Analysis and Holdout Reuse (The reusable holdout)"
proposer: "Cynthia Dwork, Vitaly Feldman, Moritz Hardt, Toniann Pitassi, Omer Reingold, Aaron Roth"
year: "2015"
type: 论文
verified: true
---

# 可复用的留出集（自适应数据分析中的泛化与留出集复用）（Generalization in Adaptive Data Analysis and Holdout Reuse (The reusable holdout)）

## 一句话

看了留出集的结果再决定下一步怎么改（自适应地用），留出集本身也会被过拟合；作者用差分隐私的办法证明，只要对留出集的回答加噪声、并且只在训练结果和留出结果差得超过一个门槛时才报留出集的值（Thresholdout），同一份留出集就能被安全地反复使用很多次。

## 原始出处

- Generalization in Adaptive Data Analysis and Holdout Reuse, Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, NeurIPS 2015（Advances in Neural Information Processing Systems 28；RRSI 引的就是这一版），https://papers.nips.cc/paper_files/paper/2015/hash/bad5f33780c42f2588878a9d07405083-Abstract.html
- 同上，arXiv:1506.02629，https://arxiv.org/abs/1506.02629
- The reusable holdout: Preserving validity in adaptive data analysis, 同一组作者, Science 349: 636–638, 2015，https://doi.org/10.1126/science.aaa9375
- Preserving Statistical Validity in Adaptive Data Analysis, 同一组作者, STOC 2015, pp. 117–126（理论版），https://doi.org/10.1145/2746539.2746580
- 争议：同一组作者 2015 年发了三篇（STOC 理论版、NeurIPS 版、Science 版），各家引用时常只写“Dwork 等 2015”，要看具体指哪一篇；RRSI 引的是 NeurIPS 版。

## 更底层的源头

- [差分隐私](differential-privacy.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [RRSI：agent 自己改 harness 会"背题"，Google Cloud AI Research 等把机器学习的正则化搬进来：每轮少改、记住试错、先筛泄题、涨分要超过噪声、多花的 token 要用涨分换、没用的就删；换考卷后也能涨分，比不加正则化的自我改进省约 30% token（比原始 harness 还是更贵）](../clips/2026-10-25-xia-rrsi-regularized-harness-self-improvement.md) | 直接源自 | 强 |
| [把 skill 当参数来训：别的模型读执行记录提改法，每步只许改几处，留出集上变好才收下；6 个测试集、7 个模型、3 种运行环境里 52 格全部第一或并列第一](../clips/2026-10-25-yang-skillopt-self-evolving-agent-skills.md) | 挑战 | 弱（模型复核通过） |
