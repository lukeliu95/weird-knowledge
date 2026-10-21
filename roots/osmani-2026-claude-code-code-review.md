---
name_zh: "Claude Code 团队怎么审代码（七层检查、少量人工）"
name_en: "How the Claude Code team does code review"
proposer: "Addy Osmani、Morgan Westlee Lunt、Qing Wang（Anthropic）"
year: "2026"
type: 研究报告
verified: true
---

# Claude Code 团队怎么审代码（七层检查、少量人工）（How the Claude Code team does code review）

## 一句话

Claude 写约九成代码后，团队把审查改成七层：Claude 自验并由新上下文子 agent 复审、每个 PR 的 AI 审查（发现再由别的 agent 核实）、能卡住合并的安全审查、必过的自动检查、按风险分级的人工批准（改动定级，不看作者）、合并队列加开关和逐步发布、快速发现和回滚；六到九月合并量翻倍多，撤回比例降四成多，每个上线改动都有一个人负责。

## 原始出处

- How the Claude Code team does code review, Addy Osmani, Morgan Westlee Lunt, Qing Wang, claude.dev 博客, 2026-10-15，https://claude.dev/blog/solving-code-review-at-anthropic/
- 争议：撤回比例下降四成多是团队自报的内部数字，没有外部独立核实；原文没有用“瑞士奶酪”一词，只写了“每层会漏一些，很少能穿过所有层，剩下的靠回滚”。

## 更底层的源头

- [瑞士奶酪模型](swiss-cheese-model.md) · 关系：相近
- [持续交付](continuous-delivery.md) · 关系：相近
- [人在环中](human-in-the-loop.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Claude Code 团队审代码的做法：九成代码由 AI 写，多道检查像叠起来的瑞士奶酪片，人只做机器做不好的判断](../clips/2026-10-21-dotey-claude-code-review-swiss-cheese.md) | 直接源自 | 强 |
