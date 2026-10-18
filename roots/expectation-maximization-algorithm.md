---
name_zh: "期望最大化算法（EM 算法）"
name_en: "Expectation–maximization algorithm"
proposer: "Arthur Dempster、Nan Laird、Donald Rubin（1977 年命名并系统阐述）"
year: "1977"
type: 方法论
verified: true
---

# 期望最大化算法（EM 算法）（Expectation–maximization algorithm）

## 一句话

模型里有看不到的隐藏部分时，交替做两步来找最可能的参数：先按当前参数推测隐藏部分（E 步），再把推测当真去更新参数（M 步），反复迭代直到稳定。

## 原始出处

- Maximum Likelihood from Incomplete Data via the EM Algorithm, A. P. Dempster、N. M. Laird、D. B. Rubin, 1977, Journal of the Royal Statistical Society Series B 39(1)，https://doi.org/10.1111/j.2517-6161.1977.tb01600.x
- Expectation–maximization algorithm, Wikipedia（History 一节），https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm
- 争议：Dempster 等人自己说这个方法之前已在特殊场合被多次提出（维基百科列出 Cedric Smith 的基因计数法、Hartley 1958 年等）；1977 年论文的收敛性证明有误，Wu 1983 年给出了正确证明。

## 更底层的源头

- [最大似然估计](maximum-likelihood-estimation.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
