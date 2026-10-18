---
name_zh: "Terminal-RSI：命令行 agent 的递归自我改进（成功记录自我改写 + 继承评分员的策略精炼）"
name_en: "Terminal-RSI: Recursive Self-Improving Terminal Agents via Recursive Self-Rewrite and Policy-Refine"
proposer: "Junyao Yang、Zongxia Li、Yucheng Shi、Zhongzhi Li、Ruhan Wang、Ruiwen Zhou、Haitao Mi、Shuicheng Yan（颜水成，通讯作者）、Leowei Liang（Tencent Hy Frontier、新加坡国立大学、马里兰大学、佐治亚大学、印第安纳大学）"
year: "2026"
type: 论文
verified: true
---

# Terminal-RSI：命令行 agent 的递归自我改进（成功记录自我改写 + 继承评分员的策略精炼）（Terminal-RSI: Recursive Self-Improving Terminal Agents via Recursive Self-Rewrite and Policy-Refine）

## 一句话

把命令行 agent 自己做成功、通过隐藏检查的记录改写成训练数据做监督微调，再用继承上一轮评分员的 PPO 强化学习精炼，交替两轮；配合按交互轮次分配功劳（TB-GAE）和“成功优先”奖励，Qwen3.8-27B 在四个 Terminal-Bench 上的平均成功率从 20.68% 升到 50.58%；作者承认这是人设计的五个阶段，证明不了规模规律，也不保证一直变强。

## 原始出处

- Terminal-RSI: Recursive Self-Improving Terminal Agents via Recursive Self-Rewrite and Policy-Refine, Junyao Yang 等, 2026, arXiv:2610.22192，https://arxiv.org/abs/2610.22192
- 同上，全文网页版（作者单位、第 3.3 节和第 5 节局限），https://arxiv.org/html/2610.22192v1
- 同一团队前作：Scaling Trajectories for Complex Tasks through Recursive Self-Rewrite, Zongxia Li 等, 2026, arXiv:2610.02826，https://arxiv.org/abs/2610.02826
- 同一团队前作：T1: Terminal Agent Reinforcement Learning for Long-Horizon Tasks, Junyao Yang 等, 2026, arXiv:2609.11042，https://arxiv.org/abs/2609.11042
- 争议：arXiv 预印本，未经同行评审。论文给的代码仓库 github.com/jyyang26/Terminal-RSI 截至 2026-10-18 打不开（404），模型页 huggingface.co/Teriminal-RSI（论文原文拼错）只有组织页、0 个公开模型。和其他模型的比较用的是参考分数，作者说还没逐一核对来源和测试条件。

## 更底层的源头

- [STaR：用推理自举推理（自学推理者）](zelikman-2022-star.md) · 关系：直接源自
- [ReST：强化自训练（用自己生成的数据做离线强化学习）](gulcehre-2023-rest.md) · 关系：直接源自
- [ReST-EM：超越人类数据，扩展自我训练来解题](singh-2023-rest-em.md) · 关系：直接源自
- [近端策略优化（PPO）](schulman-2017-ppo.md) · 关系：直接源自
- [广义优势估计（GAE）](schulman-2015-gae.md) · 关系：直接源自
- [奖励塑形（势函数塑形下的策略不变性）](ng-1999-reward-shaping.md) · 关系：直接源自
- [递归自我改进](recursive-self-improvement.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Terminal-RSI：两轮自重写加强化学习，27B 终端 agent 从 51.7% 涨到 86.5%](../clips/2026-10-18-nft-chen-terminal-rsi-recursive-self-improvement.md) | 直接源自 | 强 |
