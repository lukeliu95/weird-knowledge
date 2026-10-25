---
name_zh: "差分隐私"
name_en: "Differential privacy"
proposer: "Cynthia Dwork, Frank McSherry, Kobbi Nissim, Adam Smith"
year: "2006"
type: 理论
verified: true
---

# 差分隐私（Differential privacy）

## 一句话

在统计结果里加入按“单个人的数据最多能改变结果多少”校准的噪声，让看结果的人分不出某个人的数据在不在里面；后来被用来证明：用加噪的方式回答查询，可以反复问同一份数据而不过拟合。

## 原始出处

- Calibrating Noise to Sensitivity in Private Data Analysis, Dwork, McSherry, Nissim, Smith, Theory of Cryptography Conference (TCC) 2006, Lecture Notes in Computer Science, pp. 265–284，https://doi.org/10.1007/11681878_14
- 同上完整版, Journal of Privacy and Confidentiality 7(3): 17–51, 2017，https://doi.org/10.29012/jpc.v7i3.405
- Differential privacy，英文维基百科，https://en.wikipedia.org/wiki/Differential_privacy
- 争议：ε-差分隐私的定义一般归于 Dwork、McSherry、Nissim、Smith 2006；维基百科提到 Dinur 与 Nissim 2003 年先证明了“随意公开查询结果必然泄露隐私”，是它的铺垫。

## 更底层的源头

- 已追到基础层，或暂未找到更底层的源头

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
