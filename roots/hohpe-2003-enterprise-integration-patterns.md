---
name_zh: "企业集成模式（持久消息通道、可靠投递、幂等接收者、轮询消费者等）"
name_en: "Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions"
proposer: "Gregor Hohpe、Bobby Woolf"
year: "2003"
type: 方法论
verified: true
---

# 企业集成模式（持久消息通道、可靠投递、幂等接收者、轮询消费者等）（Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions）

## 一句话

65 个用消息把系统松耦合地连起来的模式，例如：消息先存下来再投递，系统崩了也不丢（可靠投递）；接收方收到重复消息也不出错（幂等接收者）；消费方准备好了再去取（轮询消费者）。

## 原始出处

- Enterprise Integration Patterns，Gregor Hohpe & Bobby Woolf，Addison-Wesley，2003（英文维基：65 个企业应用集成和面向消息中间件的模式，以模式语言的形式写成），https://en.wikipedia.org/wiki/Enterprise_Integration_Patterns
- 作者官网的模式页：Idempotent Receiver（另读了 Guaranteed Delivery、Polling Consumer、Competing Consumers 三页），https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html
- 争议：这些做法是业界几十年积累下来的消息队列惯例，书做的是系统整理和命名，不是首创。本轮读了官网相关模式页，没读全书。

## 更底层的源头

- 已追到基础层，或暂未找到更底层的源头

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Anthropic 常驻 agent 指南的五个要点](../clips/2026-11-18-tekonburns-anthropic-always-on-agents-guide.md) | 相近 | 弱（模型复核通过） |
