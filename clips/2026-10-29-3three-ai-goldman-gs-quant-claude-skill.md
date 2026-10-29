---
title: "高盛量化工具包 gs-quant 自带教 Claude 用的技能"
author: "三个三 (@3three_AI)"
url: https://x.com/3three_AI/status/2114257401809707058
source: X
published: 2026-10-25 07:27 UTC
saved: 2026-10-29
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

高盛给每个量化研究员开约 70 万美元年薪，靠的就是这个仓库！

它叫 gs-quant，由高盛自己的量化团队开发和维护，已经 12.9k 星。

先搞懂它是怎么运作的：

1. 高盛的量化研究员自己写了这套技能：8 个文件、1847 行，教 Claude 用他们的工具包：定价、风险、投资组合、行情数据、回测、互换、互换期权、外汇期权、Delta 对冲、交易成本，全在里面。
它甚至列出了你会遇到的报错，以及怎么修。

2. Claude 每次写 gs-quant 代码都会自动调用它，风险数学直接在你笔记本上跑：波动率、回撤、z 分数、beta、RSI。

下面是你自己免费跑起来的步骤：

1. 打开 Claude Code，装高盛的库：pip install gs-quant，或者直接拉这个仓库——https://t.co/VLvsHaJcXc

2. 添加技能：python -m gs_quant.skills install --global

3. 让 Claude 用 finance 拉任意股票和 SPY 的 5 年日线价格

4. 在上面跑高盛的风险数学：波动率、最大回撤、z 分数、布林带、RSI

5. 看 60 天 beta 和相对 SPY 的相关性。到底是这只股票在动，还是整个市场在动？

6. 标出 z 分数跌破 -2 的每一天。那意味着价格比正常水平低了 2 个标准差

7. 回测一条规则：-2 以下买入，回到 0 卖出，算上手续费。Claude 写代码，在你笔记本上跑

8. 拿它跟一直持有对比。如果扣掉手续费还跑不赢买入持有，那就不是优势

> 媒体：
> - https://video.twimg.com/amplify_video/2114230394430349312/vid/avc1/1080x1456/v8_WmZ-QGxNnlauB.mp4?tag=29

## 溯源

