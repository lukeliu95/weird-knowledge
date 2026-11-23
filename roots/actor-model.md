---
name_zh: "actor 模型"
name_en: "Actor model"
proposer: "Carl Hewitt、Peter Bishop、Richard Steiger"
year: "1973"
type: 理论
verified: true
---

# actor 模型（Actor model）

## 一句话

把并发系统看成一群各管各的 actor（参与者）：每个 actor 只改自己的私有状态，彼此只靠发消息往来，不共享内存，所以不用加锁，也不会互相覆盖。

## 原始出处

- A Universal Modular ACTOR Formalism for Artificial Intelligence，Carl Hewitt、Peter Bishop、Richard Steiger，IJCAI 1973，pp. 235–245，https://www.ijcai.org/Proceedings/73/Papers/027B.pdf
- Actor model，英文维基百科（起源于 1973 年；actor 只能改自己的私有状态，彼此只能通过消息间接影响，因此不需要基于锁的同步），https://en.wikipedia.org/wiki/Actor_model
- 争议：Hewitt 1973 年的形式化本身并没规定“一个 actor 一次只处理一条消息”；“每个 actor 一个邮箱、按顺序逐条处理”是 Erlang、Akka 等实现里的通行做法。本轮只核对了论文 PDF 链接能打开和维基条目，没有通读 1973 年论文。

## 更底层的源头

- 已追到基础层，或暂未找到更底层的源头

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [24 小时在线的 agent 助理靠五样东西](../clips/2026-11-18-dotey-always-on-agent-five-parts.md) | 相近 | 弱（模型复核通过） |
| [Anthropic 常驻 agent 指南的五个要点](../clips/2026-11-18-tekonburns-anthropic-always-on-agents-guide.md) | 相近 | 弱（模型复核通过） |
| [2027 年的 agent 平台：应用层的终局](../clips/2026-11-23-john-ssuh-agent-platform-2027-endgame.md) | 直接源自 | 强 |
