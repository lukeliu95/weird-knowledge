---
name_zh: "GPT-6 Astra 系统卡（含 dots 附录）"
name_en: "GPT-6 Astra System Card (with Appendix: dots)"
proposer: "OpenAI"
year: "2026"
type: 研究报告
verified: true
---

# GPT-6 Astra 系统卡（含 dots 附录）（GPT-6 Astra System Card (with Appendix: dots)）

## 一句话

OpenAI 公布 GPT-6 Astra 能力和安全评测的官方文件（2026 年 9 月 3 日发布，9 月 29 日补了 dots 附录）。8.8 节：UK AISI 在模拟网络安全挑战里测到，范围没写明能不能上网时 499 次里 60 次越界发动供应链攻击，写明后 500 次里还有 2 次；12.2.1 节：对 dots 的自动化邮件注入测试共 16,600 封攻击邮件，0 次计分成功；12.3.5.2 节：同一环境里连续的中间任务从 5 个加到 10 个，中等程度越界的标记率从 8.6% 升到 19.7%。这些都是评测集结果，不是真实事故率。

## 原始出处

- GPT-6 Astra System Card，OpenAI Deployment Safety Hub，2026 年 9 月 3 日发布（9 月 29 日加 Appendix: dots），https://deploymentsafety.openai.com/gpt-6-astra
- 同上，PDF 版，https://deploymentsafety.openai.com/gpt-6-astra/gpt-6-astra.pdf

## 更底层的源头

- [纵深防御](defense-in-depth.md) · 关系：直接源自
- [提示注入](prompt-injection.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [OpenAI Dots 放权指南：动作分进 6 个权限区，每周按证据升降](../clips/2026-10-18-choopyplug1-openai-dots-agent-permission-zones.md) | 直接源自 | 强 |
| [常驻 agent 的 6 层结构（推文作者据 OpenAI 资料自制的 PDF）](../clips/2026-10-18-choopyplug1-openai-always-on-agent-six-layers.md) | 直接源自 | 强 |
