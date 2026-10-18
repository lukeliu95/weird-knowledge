---
name_zh: "Twitter 推荐算法开源（Heavy Ranker 互动权重表）"
name_en: "Twitter's Recommendation Algorithm (twitter/the-algorithm, twitter/the-algorithm-ml)"
proposer: "Twitter 工程团队"
year: "2023"
type: 研究报告
verified: true
---

# Twitter 推荐算法开源（Heavy Ranker 互动权重表）（Twitter's Recommendation Algorithm (twitter/the-algorithm, twitter/the-algorithm-ml)）

## 一句话

Twitter 2023 年公开“为你推荐”信息流的代码：先召回候选帖子，再由约 4800 万参数的神经网络 Heavy Ranker 预测用户点赞、转发、回复、作者回复、点进停留、负反馈、举报等各种行为的概率，按配置好的权重加权求和得出排序分（README 标明这是 2023-04-05 的权重，随时可能调整）。

## 原始出处

- twitter/the-algorithm-ml，projects/home/recap/README.md（Heavy Ranker 权重表，2023-04-05），https://github.com/twitter/the-algorithm-ml/blob/main/projects/home/recap/README.md
- twitter/the-algorithm，GitHub 仓库 README，https://github.com/twitter/the-algorithm
- Twitter's Recommendation Algorithm，Twitter Engineering Blog，2023（仓库 README 链接的官方博客），https://blog.x.com/engineering/en_us/topics/open-source/2023/twitter-recommendation-algorithm

## 更底层的源头

- [排序学习（重排）](learning-to-rank.md) · 关系：直接源自
- [注意力经济](attention-economy.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [X推荐算法权重表：回复比点赞值钱](../clips/2026-10-18-ityouknows-x-algorithm-weights-reply-vs-like.md) | 直接源自 | 强 |
