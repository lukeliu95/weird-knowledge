---
name_zh: "权重空间编程（小模型权重读写实验）"
name_en: "Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights"
proposer: "Rikiya Takehi、Jayden Teoh、Alex Zhang、Omar Khattab"
year: "2026"
type: 研究报告
verified: true
---

# 权重空间编程（小模型权重读写实验）（Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights）

## 一句话

让前沿模型分析并直接编辑其他网络的权重，研究其能否识别或修正行为；作者的数学提升主要来自解除一个小模型的推理循环，尚不能外推成普遍新增能力。

## 原始出处

- Takehi 等，Sparks of Weight-Space Programming，作者研究博客，2026-11-02；核对实验 7、8 与相关工作。目标数学实验不用梯度训练，但有练习题、Python 分析和最多 50 次前向反馈。，https://rikiyat.github.io/blog/weight-space-programming/
- 作者公开的实验日志仓库，提供记录供进一步复查；本轮未逐条复算日志或复现实验。，https://github.com/RikiyaT/lm_understand-logs
- 争议：“约 6 倍”是特定 Qwen3.5-0.8B 实验在 MATH-500 上的正确率之比；对少循环的 Gemma 3 270M，作者未建立同样提升。读权重推断行为也有失败案例。本文是作者实验报告，未独立复现。

## 更底层的源头

- 已追到基础层，或暂未找到更底层的源头

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [权重空间编程：直接改权重，修复小模型推理循环（作者实验）](../clips/2026-11-03-rikiyatakehi-weight-space-programming.md) | 直接源自 | 强 |
