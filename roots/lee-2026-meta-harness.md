---
name_zh: "Meta-Harness：端到端优化模型的运行框架"
name_en: "Meta-Harness: End-to-End Optimization of Model Harnesses"
proposer: "Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, Chelsea Finn"
year: "2026"
type: 论文
verified: true
---

# Meta-Harness：端到端优化模型的运行框架（Meta-Harness: End-to-End Optimization of Model Harnesses）

## 一句话

大模型系统的表现不只看权重，也看运行框架（决定存什么、取什么、给模型看什么的代码）；用一个外层循环让 agent 当提议者，通过文件系统读以往所有候选框架的源码、分数和执行记录，去搜索更好的框架代码，在文本分类、检索增强数学题和 TerminalBench-2 上超过人工设计的框架。

## 原始出处

- Meta-Harness: End-to-End Optimization of Model Harnesses, Yoonho Lee 等, arXiv:2603.28052, 2026-03-30，https://arxiv.org/abs/2603.28052
- Harness² 参考文献把它记为发表于 Third Conference on Language Modeling（COLM 2026），https://arxiv.org/html/2610.14224v1

## 更底层的源头

- [自学优化器（STOP）：递归自我改进的代码生成](zelikman-2023-self-taught-optimizer.md) · 关系：相近
- [上下文工程](context-engineering.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Harness²：agent 不改模型，靠对照试验改自己的运行框架，还学会怎么改得更好](../clips/2026-10-19-xu-harness2-recursive-agent-harnessing.md) | 直接源自 | 强 |
