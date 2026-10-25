---
name_zh: "深度神经网络的选择性分类（带拒答选项）"
name_en: "Selective Classification for Deep Neural Networks"
proposer: "Yonatan Geifman, Ran El-Yaniv"
year: "2017"
type: 论文
verified: true
---

# 深度神经网络的选择性分类（带拒答选项）（Selective Classification for Deep Neural Networks）

## 一句话

让分类器在没把握时拒绝回答：给训练好的网络配一个按置信度设的门槛，用户先定可接受的错误率，测试时低于门槛的样本一律拒答，用少答一部分换取答出来的更准，并给出高概率的风险保证。

## 原始出处

- Selective Classification for Deep Neural Networks, Yonatan Geifman & Ran El-Yaniv, NeurIPS 2017 (Advances in Neural Information Processing Systems 30)，https://papers.nips.cc/paper/7073-selective-classification-for-deep-neural-networks
- 同上，arXiv:1705.08500，https://arxiv.org/abs/1705.08500
- JevAgentHarness 并引的“学会交回给专家”：Consistent Estimators for Learning to Defer to an Expert, Hussein Mozannar & David Sontag, ICML 2020, arXiv:2006.01862，https://arxiv.org/abs/2006.01862
- 争议：拒答选项本身是 Chow 在 1957、1970 年提出的老思想（见更底层源头）；这篇是把它用到深度网络上。“该不该交回、交回给谁”另一支是 Mozannar 与 Sontag 2020 的“学会交回”，JevAgentHarness 两篇并引。

## 更底层的源头

- [Chow 拒识规则：识别错误率与拒识率的最优权衡](chow-1970-reject-option.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [agent 每步的选择题交给小决策模型（UIUC 等，推文误作普林斯顿和谷歌），模拟网店里 4B 模型完成率 91.5%](../clips/2026-10-20-rohanpaul-ai-agent-decision-model-small-beats-big.md) | 直接源自 | 强 |
| [agent 每一步的选择题交给小决策模型：按 agent 自己的运行记录给每类选择拟合把握门槛，够把握才交出去，否则还是大模型定；不设门槛成功率掉 19 个点，设了门槛再用 agent 自己走到的状态训一个 4B 模型，便宜 81%～89%、成功率掉不到 3 个点](../clips/2026-10-25-zhu-jevagentharness-decision-models-share-control.md) | 直接源自 | 强 |
| [Anthus 实测 GPT-6 Luna（通用版，不是 OpenAI Decisions API 本身）：说 99% 确定时只对 68%，推理到第五步接近瞎猜；决策模型要紧的是置信度可信（厂商测评：Anthus 卖决策模型的校准服务）](../clips/2026-10-25-porter-decisions-api-luna-calibration.md) | 相近 | 弱（模型复核通过） |
