---
name_zh: "职责分离（四眼原则、制单与复核分开）"
name_en: "Separation of duties (segregation of duties; maker-checker; four-eyes principle)"
proposer: "没有单一提出者：会计内部控制沿用已久；计算机安全里 Saltzer 与 Schroeder（1975，“特权分离”）、Clark 与 Wilson（1987，“职责分离”）把它写成成文原则"
year: "1975 / 1987（计算机安全里的成文表述）"
type: 方法论
verified: true
---

# 职责分离（四眼原则、制单与复核分开）（Separation of duties (segregation of duties; maker-checker; four-eyes principle)）

## 一句话

关键的事不能由一个人从头做到尾：执行的人和核对、批准的人必须分开（Clark–Wilson 模型要求交易的认证者和执行者不是同一方），这样单个人的差错或舞弊没法自己掩盖。

## 原始出处

- A Comparison of Commercial and Military Computer Security Policies，David D. Clark、David R. Wilson，1987 IEEE Symposium on Security and Privacy（提出以“良构事务”和“职责分离”保证商业数据完整性），https://doi.org/10.1109/SP.1987.10001
- The Protection of Information in Computer Systems，Jerome H. Saltzer、Michael D. Schroeder，Proceedings of the IEEE 63(9)，1975（设计原则“特权分离”：要两把钥匙才能打开的保护机制比一把更稳），https://doi.org/10.1109/PROC.1975.9939
- 同上论文的作者网页版（Basic Principles 一节），https://web.mit.edu/Saltzer/www/publications/protection/Basic.html
- Separation of duties，维基百科（会计行业几百年来靠分职防舞弊；也叫四眼原则），https://en.wikipedia.org/wiki/Separation_of_duties
- 争议：没有公认的首创者。维基百科说会计行业几百年来就用分职牵制防差错和舞弊；银行业叫 maker-checker，也叫四眼原则；计算机安全里常引 Saltzer 与 Schroeder 1975 的“特权分离”和 Clark 与 Wilson 1987 的“职责分离”。

## 更底层的源头

- [最小权限原则](principle-of-least-privilege.md) · 关系：相近
- [委托-代理问题](principal-agent-problem.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [把 Claude Code 分成"司令官"和"部下"自主跑开发：主会话 Opus 只管计划、分工、验证、记录，实现、审查、调研交给 Sonnet / Haiku 的 subagent，用定义文件的工具栏和模型栏硬性限权](../clips/2026-10-25-xin-tech-commander-subordinate-agent-roles.md) | 换了说法 | 强 |
| [编排 Claude Code 的"幕僚长"模式：一个会话只协调和验收、别的会话干活，状态放外部看板，每份汇报当证据重跑再信](../clips/2026-10-25-jalangan-chief-of-staff-agent-orchestration.md) | 直接源自 | 强 |
