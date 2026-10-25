---
name_zh: "变异测试（检验测试本身能不能抓到错）"
name_en: "Mutation testing"
proposer: "Richard Lipton（1971 年学生论文中提出）；Richard A. DeMillo、Richard J. Lipton、Frederick G. Sayward（1978 年首次系统发表）"
year: "1971 / 1978"
type: 方法论
verified: true
---

# 变异测试（检验测试本身能不能抓到错）（Mutation testing）

## 一句话

故意在程序里植入小错（变异体），看现有测试会不会失败、把它“杀死”；杀不死说明测试本身不够格，被杀死的变异体占比就是测试质量的分数。

## 原始出处

- Hints on Test Data Selection: Help for the Practicing Programmer，R. A. DeMillo、R. J. Lipton、F. G. Sayward，IEEE Computer 11(4)，1978，https://doi.org/10.1109/C-M.1978.218136
- An Analysis and Survey of the Development of Mutation Testing，Yue Jia、Mark Harman，IEEE Transactions on Software Engineering 37(5)，2011（综述），https://doi.org/10.1109/TSE.2010.62
- Mutation testing，维基百科（Lipton 1971 年作为学生提出，DeMillo、Lipton、Sayward 1978 年首先发表），https://en.wikipedia.org/wiki/Mutation_testing
- 争议：维基百科说最早由 Lipton 1971 年在学生论文里提出，1978 年由 DeMillo、Lipton、Sayward 首先发表；1971 年那篇学生论文本身没有查到可公开访问的版本。

## 更底层的源头

- [科学方法](scientific-method.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [编排 Claude Code 的"幕僚长"模式：一个会话只协调和验收、别的会话干活，状态放外部看板，每份汇报当证据重跑再信](../clips/2026-10-25-jalangan-chief-of-staff-agent-orchestration.md) | 相近 | 弱（模型复核通过） |
