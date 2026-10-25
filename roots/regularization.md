---
name_zh: "正则化（防过拟合的约束与惩罚）"
name_en: "Regularization (mathematics)"
proposer: "Andrey Tikhonov（反问题，1943、1963）、David L. Phillips（1962）；统计学里 Arthur Hoerl 与 Robert Kennard（岭回归，1970）、Robert Tibshirani（Lasso，1996）"
year: "1963"
type: 方法论
verified: true
---

# 正则化（防过拟合的约束与惩罚）（Regularization (mathematics)）

## 一句话

只看训练数据会把细节甚至噪声也“背”下来；给模型加约束或惩罚（限制参数的大小或个数、提前停止、丢弃等），用一点偏差换更小的方差，让它在没见过的数据上也表现好。

## 原始出处

- Solution of incorrectly formulated problems and the regularization method, A. N. Tikhonov, Doklady Akademii Nauk SSSR 151: 501–504, 1963（英译 Soviet Mathematics 4: 1035–1038）；1943 年的《论反问题的稳定性》更早（据维基百科 Ridge regression 条目），https://en.wikipedia.org/wiki/Ridge_regression
- A Technique for the Numerical Solution of Certain Integral Equations of the First Kind, D. L. Phillips, Journal of the ACM 9: 84–97, 1962，https://doi.org/10.1145/321105.321114
- Ridge Regression: Biased Estimation for Nonorthogonal Problems, Arthur E. Hoerl & Robert W. Kennard, Technometrics 12(1): 55–67, 1970，https://doi.org/10.1080/00401706.1970.10488634
- Regression Shrinkage and Selection via the Lasso, Robert Tibshirani, Journal of the Royal Statistical Society Series B 58(1): 267–288, 1996，https://doi.org/10.1111/j.2517-6161.1996.tb02080.x
- Deep Learning 第 7 章 Regularization for Deep Learning, Ian Goodfellow, Yoshua Bengio, Aaron Courville, MIT Press, 2016（RRSI 引的教材），https://www.deeplearningbook.org/contents/regularization.html
- Regularization (mathematics)，英文维基百科（显式正则化与隐式正则化、与过拟合的关系），https://en.wikipedia.org/wiki/Regularization_(mathematics)
- 争议：没有单一的提出者：维基百科说 Tikhonov 正则化“在许多场合被独立发明”，在积分方程上因 Tikhonov（1943、1963）和 Phillips（1962）的工作而知名，也叫 Tikhonov–Phillips 正则化；统计学里叫岭回归，由 Hoerl 与 Kennard 1970 年提出（Hoerl 1962 年已有岭分析），机器学习里叫权重衰减。L1 正则化（Lasso）通常归于 Tibshirani 1996。

## 更底层的源头

- [偏差-方差权衡](bias-variance-tradeoff.md) · 关系：直接源自
- [奥卡姆剃刀](occams-razor.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [RRSI：agent 自己改 harness 会"背题"，Google Cloud AI Research 等把机器学习的正则化搬进来：每轮少改、记住试错、先筛泄题、涨分要超过噪声、多花的 token 要用涨分换、没用的就删；换考卷后也能涨分，比不加正则化的自我改进省约 30% token（比原始 harness 还是更贵）](../clips/2026-10-25-xia-rrsi-regularized-harness-self-improvement.md) | 直接源自 | 强 |
