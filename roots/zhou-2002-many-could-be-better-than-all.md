---
name_zh: "选择性集成：挑一部分可能比全用更好"
name_en: "Ensembling neural networks: Many could be better than all"
proposer: "Zhi-Hua Zhou（周志华）, Jianxin Wu, Wei Tang"
year: "2002"
type: 论文
verified: true
---

# 选择性集成：挑一部分可能比全用更好（Ensembling neural networks: Many could be better than all）

## 一句话

训练出一批神经网络后，用遗传算法给每个网络在集成里的贡献打权重，只留下权重高的组成集成（GASEN）；在回归和分类上都比把全部网络合起来更准、规模更小，作者也从理论上说明“挑一部分可能比全用好”。

## 原始出处

- Ensembling neural networks: Many could be better than all, Zhou, Wu & Tang, Artificial Intelligence 137(1–2): 239–263, 2002，https://doi.org/10.1016/S0004-3702(02)00190-X
- 早期版本：Genetic Algorithm Based Selective Neural Network Ensemble, Zhou, Wu, Jiang & Chen, IJCAI 2001，https://mlanthology.org/ijcai/2001/zhou2001ijcai-genetic
- 争议：作者 2010 年在同一期刊发过勘误（Corrigendum, DOI 10.1016/j.artint.2010.10.001）。

## 更底层的源头

- [集成学习](ensemble-learning.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [用多个大模型"群体投票"预测未来时，按推理方式聚类、每类只挑 1 个代表，3 个模型就比 25 个全投票略准，调用少 88%、花费约省 80%；故意挑最不一样的反而更差](../clips/2026-10-25-chetlapalli-diverse-by-reasoning-llm-crowds.md) | 相近 | 弱（模型复核通过） |
