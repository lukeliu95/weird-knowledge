---
name_zh: "预写日志"
name_en: "Write-ahead logging"
proposer: "Jim Gray（IBM Research）"
year: "1978"
type: 方法论
verified: true
---

# 预写日志（Write-ahead logging）

## 一句话

改动数据之前，先把改动写进放在稳定存储上的追加式日志；崩溃后对照日志决定撤销、补完或保留每个操作，从而保证原子性和持久性。

## 原始出处

- Wikipedia: Write-ahead logging（ARIES 是 WAL 家族的代表算法），https://en.wikipedia.org/wiki/Write-ahead_logging
- Bruce Lindsay 回忆 Jim Gray 的文章, SIGMOD Record, 2008（称 Gray 在 IBM Research 定义了 WAL 协议，引 Gray 1978 Notes on Data Base Operating Systems 与 Gray 1981），https://sigmodrecord.org/publications/sigmodRecord/0806/p38.lindsay.pdf
- 争议：维基百科没写发明者；SIGMOD Record 文章归功于 Gray，但 IBM IMS 也有类似的「write ahead data set」日志机制，两者不宜混为一谈。

## 更底层的源头

- [数据库事务](database-transaction.md) · 关系：直接源自

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Pi 开发笔记：长时间运行智能体的难题](../clips/2026-10-18-maxforai-pi-notes-agent-harness-critique.md) | 换了说法 | 强 |
