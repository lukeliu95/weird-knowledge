---
name_zh: "现代神经网络的校准（温度缩放）"
name_en: "On Calibration of Modern Neural Networks"
proposer: "Chuan Guo、Geoff Pleiss、Yu Sun、Kilian Q. Weinberger"
year: "2017"
type: 论文
verified: true
---

# 现代神经网络的校准（温度缩放）（On Calibration of Modern Neural Networks）

## 一句话

模型给出的置信度应当和它真实答对的概率一致，这叫校准；作者发现现代深度网络比十年前的网络更不校准，和网络深度、宽度、权重衰减、批归一化有关，用只有一个参数的温度缩放（Platt 缩放的变体）就能在多数数据集上修正。

## 原始出处

- On Calibration of Modern Neural Networks, Chuan Guo, Geoff Pleiss, Yu Sun, Kilian Q. Weinberger, ICML 2017, PMLR 70: 1321–1330，https://proceedings.mlr.press/v70/guo17a.html
- arXiv:1706.04599（DOI 10.48550/arXiv.1706.04599），https://arxiv.org/abs/1706.04599
- 争议：“校准”这个概念远早于本文，来自天气预报的概率预报检验（如 Brier 1950，Monthly Weather Review 78: 1–3，https://doi.org/10.1175/1520-0493(1950)078<0001:VOFEIT>2.0.CO;2）；本文的贡献是指出现代深度网络失准并给出温度缩放。

## 更底层的源头

- 已追到基础层，或暂未找到更底层的源头

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Harrison Chase：agent 里很多步骤是是非题不是生成，交给决策模型给带校准的概率，大模型只做难的](../clips/2026-10-22-hwchase17-yes-no-calls-jev.md) | 相近 | 弱（模型复核通过） |
