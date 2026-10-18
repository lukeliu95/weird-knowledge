---
name_zh: "长时间运行 agent 的有效 harness"
name_en: "Effective harnesses for long-running agents"
proposer: "Justin Young（Anthropic）"
year: "2025"
type: 方法论
verified: true
---

# 长时间运行 agent 的有效 harness（Effective harnesses for long-running agents）

## 一句话

先用初始化 agent 搭好功能清单、启动脚本、进度日志和第一个 git 提交；之后每个会话只做一个功能，留下干净代码和进度记录交给下一个会话，用浏览器端到端测试通过才标记完成。

## 原始出处

- Effective harnesses for long-running agents, Justin Young, Anthropic Engineering, 2025-11-26，https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents

## 更底层的源头

- 已追到基础层，或暂未找到更底层的源头

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [外层harness让智能体连跑数小时](../clips/2026-10-18-baoweiheihei-harness-unattended-long-running.md) | 直接源自 | 强 |
