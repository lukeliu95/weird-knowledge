---
name_zh: "自我改进记忆（SIM）：换模型、换题库后接着做 harness 递归自我改进"
name_en: "Self-Improvement Memory Enables Continual Recursive Self-Improvement"
proposer: "Xin Yu、Fei Xia、Jiaqi Pan 等（Google Cloud AI、Google DeepMind、宾夕法尼亚州立大学）"
year: "2026"
type: 论文
verified: true
---

# 自我改进记忆（SIM）：换模型、换题库后接着做 harness 递归自我改进（Self-Improvement Memory Enables Continual Recursive Self-Improvement）

## 一句话

harness 的自我优化换了模型或题库后，只带走改好的代码不够。要把每处改动记成一本账交给优化器：针对什么问题、理由是什么、事先预测能修好哪些题、实际修好了哪些、在哪个模型和题库上测的。这样继续优化的效果更好。

## 原始出处

- Self-Improvement Memory Enables Continual Recursive Self-Improvement，Xin Yu 等，arXiv:2611.18856，2026-11-13；读了摘要、第 1～5 节、局限和附录 F.3–F.6，https://arxiv.org/abs/2611.18856
- 争议：全部是作者自报的成绩，没见到独立复现。独立重复实验只在编程一个领域做了（10 对，SIM 赢 9 对，平均多 2.36 分，p=0.003），其余领域每个条件只跑了一次。工作空间任务的 68.41→84.75 对 68.41→73.42 是单次运行，而且是 Gemini 3.8 Flash 当评委打分，可能有评委偏差。跨模型只测了 Claude Opus 5.5→Gemini 3.8 Flash 这一对。

## 更底层的源头

- [Meta-Harness：端到端优化模型的运行框架](lee-2026-meta-harness.md) · 关系：直接源自
- [递归自我改进](recursive-self-improvement.md) · 关系：直接源自
- [组织学习](organizational-learning.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Google 论文：harness 换模型时带上改动记录，接着优化更有效](../clips/2026-11-19-akshay-pachaar-google-rsi-harness-model-transfer.md) | 直接源自 | 强 |
