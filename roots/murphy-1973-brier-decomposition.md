---
name_zh: "Brier 分数的三分解（可靠性、分辨力、不确定性）"
name_en: "A New Vector Partition of the Probability Score"
proposer: "Allan H. Murphy"
year: "1973"
type: 论文
verified: true
---

# Brier 分数的三分解（可靠性、分辨力、不确定性）（A New Vector Partition of the Probability Score）

## 一句话

概率预报的总误差（Brier 分数）可以拆成三块：说的概率和实际发生的频率对不对得上（可靠性，即校准）、能不能把会发生和不会发生的情况分开（分辨力）、事情本身有多难预测（不确定性）；校准好不等于有用，一个永远报历史平均概率的预报可以完全校准，却没有任何分辨力。

## 原始出处

- A New Vector Partition of the Probability Score, Allan H. Murphy, Journal of Applied Meteorology 12: 595–600, 1973，https://doi.org/10.1175/1520-0450(1973)012<0595:ANVPOT>2.0.CO;2
- Brier 分数本身：Verification of Forecasts Expressed in Terms of Probability, Glenn W. Brier, Monthly Weather Review 78: 1–3, 1950，https://doi.org/10.1175/1520-0493(1950)078<0001:VOFEIT>2.0.CO;2
- 争议：“一个永远报历史平均概率的预报完全校准却没有分辨力”是由这个分解直接推出的常见例子，不是原文的话。

## 更底层的源头

- 已追到基础层，或暂未找到更底层的源头

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Anthus 实测 GPT-6 Luna（通用版，不是 OpenAI Decisions API 本身）：说 99% 确定时只对 68%，推理到第五步接近瞎猜；决策模型要紧的是置信度可信（厂商测评：Anthus 卖决策模型的校准服务）](../clips/2026-10-25-porter-decisions-api-luna-calibration.md) | 换了说法 | 弱（模型复核通过） |
