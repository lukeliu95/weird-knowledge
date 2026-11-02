---
name_zh: "定制微调可能破坏已经对齐的语言模型的安全行为"
name_en: "Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!"
proposer: "Xiangyu Qi、Yi Zeng、Tinghao Xie、Pin-Yu Chen、Ruoxi Jia、Prateek Mittal、Peter Henderson"
year: "2023（ICLR 2024）"
type: 论文
verified: true
---

# 定制微调可能破坏已经对齐的语言模型的安全行为（Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!）

## 一句话

对已对齐模型做定制微调可能削弱安全行为，恶意和某些普通任务数据都可能造成变化；改训前的安全评估不能保证改训后仍安全。

## 原始出处

- Qi等，arXiv:2310.03693，2023-10-05；已读摘要及HTML中的概念与实证说明。，https://arxiv.org/abs/2310.03693
- ICLR 2024正式论文。，https://proceedings.iclr.cc/paper_files/paper/2024/file/83b7da3ed13f06c13ce82235c8eedf35-Paper-Conference.pdf
- 争议：研究对象与Jun Song自述项目不同。主要衡量有害内容服从和安全退化，不证明匿名团伙存在、拥有海量数据，或特定网络攻击成功率超过前沿模型。

## 更底层的源头

- [AI 对齐](ai-alignment.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [作者自述：拒绝匿名黑帽团伙的模型后训练邀约（未独立核实）](../clips/2026-11-01-jun-song-black-hat-offer-post-train-open-models-exploit-data.md) | 相近 | 弱（模型复核通过） |
