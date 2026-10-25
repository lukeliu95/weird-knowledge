---
name_zh: "存储层次（缓存）"
name_en: "Memory hierarchy"
proposer: "Arthur W. Burks、Herman H. Goldstine、John von Neumann（概念）；Maurice Wilkes（缓存，“从属存储器”）"
year: "1946"
type: 理论
verified: true
---

# 存储层次（缓存）（Memory hierarchy）

## 一句话

存储器越快就越小、越贵，越大就越慢，所以计算机把存储分成一层层，把常用数据放在更快的上层（缓存），用局部性让整体又快又便宜。

## 原始出处

- Preliminary Discussion of the Logical Design of an Electronic Computing Instrument，Burks、Goldstine、von Neumann，1946（重印于 The Origins of Digital Computers，1982，pp. 399–413，DOI 10.1007/978-3-642-61812-3_32），https://doi.org/10.1007/978-3-642-61812-3_32
- Slave Memories and Dynamic Storage Allocation，Maurice V. Wilkes，IEEE Transactions on Electronic Computers EC-14: 270–271，1965，DOI 10.1109/PGEC.1965.264263，https://doi.org/10.1109/PGEC.1965.264263
- Memory hierarchy，英文维基百科，https://en.wikipedia.org/wiki/Memory_hierarchy
- 争议：1946 年报告里“不得不考虑构建一个存储器的层次，每一层容量比上一层大、但访问更慢”的原话，是通过教材（如 Hennessy & Patterson《计算机体系结构》存储层次一章）的转引核对的，报告原件本次没有打开。

## 更底层的源头

- 已追到基础层，或暂未找到更底层的源头

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Postgres 吞掉各类专用数据库之后，能不能连 Redis 缓存也替掉](../clips/2026-10-25-realchendahuang-can-postgres-replace-redis-cache.md) | 直接源自 | 强 |
