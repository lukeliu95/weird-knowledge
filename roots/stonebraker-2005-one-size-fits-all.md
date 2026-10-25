---
name_zh: "“一种数据库通吃”的时代已经过去"
name_en: "\"One Size Fits All\": An Idea Whose Time Has Come and Gone"
proposer: "Michael Stonebraker、Uğur Çetintemel"
year: "2005"
type: 论文
verified: true
---

# “一种数据库通吃”的时代已经过去（"One Size Fits All": An Idea Whose Time Has Come and Gone）

## 一句话

传统关系数据库想用一套引擎服务所有场景，作者认为这已行不通：流处理、数据仓库等专用引擎会比通用数据库快一个数量级，市场会分裂成多种专用数据库。

## 原始出处

- "One Size Fits All": An Idea Whose Time Has Come and Gone，Michael Stonebraker & Uğur Çetintemel，21st International Conference on Data Engineering（ICDE'05），pp. 2–11，2005，DOI 10.1109/ICDE.2005.1，https://doi.org/10.1109/ICDE.2005.1
- 争议：Stonebraker 本人正是 Postgres 的创造者。之后二十年专用数据库确实大量出现，但近年“Postgres 加插件”又把不少专用场景收了回去，两种走向至今并存。

## 更底层的源头

- [分工](division-of-labour.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Postgres 吞掉各类专用数据库之后，能不能连 Redis 缓存也替掉](../clips/2026-10-25-realchendahuang-can-postgres-replace-redis-cache.md) | 挑战 | 弱（模型复核通过） |
