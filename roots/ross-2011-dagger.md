---
name_zh: "DAgger：把模仿学习化为无悔在线学习（在自己会走到的状态上学）"
name_en: "A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning"
proposer: "Stéphane Ross, Geoffrey J. Gordon, J. Andrew Bagnell"
year: "2011"
type: 论文
verified: true
---

# DAgger：把模仿学习化为无悔在线学习（在自己会走到的状态上学）（A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning）

## 一句话

模仿学习只学专家走过的状态，一上手犯错就进入没见过的状态、错误越滚越大；DAgger 让学生自己去跑，把它实际走到的状态交给专家标注，再合进数据重训，反复几轮，使训练分布贴近部署时真实会遇到的分布。

## 原始出处

- A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning, Stéphane Ross, Geoffrey J. Gordon, J. Andrew Bagnell, AISTATS 2011, PMLR 15: 627–635，https://proceedings.mlr.press/v15/ross11a.html
- 同上，arXiv:1011.0686，https://arxiv.org/abs/1011.0686

## 更底层的源头

- [模仿学习（行为克隆）](imitation-learning.md) · 关系：直接源自
- [数据集偏移](dataset-shift.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [agent 每步的选择题交给小决策模型（UIUC 等，推文误作普林斯顿和谷歌），模拟网店里 4B 模型完成率 91.5%](../clips/2026-10-20-rohanpaul-ai-agent-decision-model-small-beats-big.md) | 直接源自 | 强 |
| [agent 每一步的选择题交给小决策模型：按 agent 自己的运行记录给每类选择拟合把握门槛，够把握才交出去，否则还是大模型定；不设门槛成功率掉 19 个点，设了门槛再用 agent 自己走到的状态训一个 4B 模型，便宜 81%～89%、成功率掉不到 3 个点](../clips/2026-10-25-zhu-jevagentharness-decision-models-share-control.md) | 直接源自 | 强 |
| [视频世界模型的长期记忆改用"平面块"来存：一个场景约 10 万块、约 5MB，比逐像素点云小三个数量级，生成几百帧后画面和几何仍连贯](../clips/2026-10-25-he-ppmem-persistent-planar-memory-video-world-models.md) | 相近 | 弱（模型复核通过） |
