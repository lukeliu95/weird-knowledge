---
title: "PostgreSQL 加插件替代常用外挂产品清单"
author: "陈大黄 (@realchendahuang)"
url: https://x.com/realchendahuang/status/2114145162406535218
source: X
published: 2026-10-25 00:01 UTC
saved: 2026-10-25
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

PostgreSQL 本身已经很牛逼了，再加上插件会更牛逼。

常用的那些外挂商业产品，靠 PG 加插件基本全能干掉，这里给大家汇总一下：

RabbitMQ 任务队列：pgmq插件。
在表里做排队、延时和死信重试。最爽的是发任务和写业务数据在同一个数据库事务里，同生共死，根本不会发生数据写完了消息却丢了的鬼故事。

Elasticsearch 全文搜索：ParadeDB（pg_search）插件。
底层直接封装了 Rust 的 Tantivy 引擎，在 SQL 里就能跑正经的 BM25 相关性检索。常规搜关键词连这都不用，自带的 tsvector 就够用，省掉搭 Logstash 双写管道。

MongoDB 文档库：直接用原生的 jsonb。
二进制紧凑存储带 GIN 索引，支持深层字段检索和原地修改。既有文档数据库随心所欲改 Schema 的自由，又能随时跟旁边的关系表 JOIN，谁还乐意单独跑个 Mongo。

Redis 轻量缓存：直接建 UNLOGGED 表。
跳过 WAL 日志落盘换极致读写，配个触发器自动清理过期行。丢了也不心疼的会话和临时指标，完全没必要专门供一个 Redis 实例。

Pinecone 专用向量库：pgvector插件。
高维向量直接作为表里的一列，加个 HNSW 索引，余弦相似度和业务字段条件直接在一条 SQL 里过滤，省得在两个系统之间倒腾一堆 ID 映射。

ClickHouse  时序打点：TimescaleDB插件。
把大表自动按时间切块做 hypertable，后台冷数据直接无损压掉 90% 体积，监控和高频打点依然老老实实用标准 SQL 查。

Neo4j  图数据库：Apache AGE插件。
原生支持 openCypher 查询语言，直接用 MATCH 语句在关系表里查多度好友和层级路径，复杂网络关系不用再跨库跳。

Celery  定时调度：pg_cron插件。
用标准的 cron 表达式直接在数据库内部跑定时 SQL，定时算报表、刷物化视图或清理过期数据，随数据库备份走，宿主机干干净净。

通用 CRUD 微服务： PostgREST插件。
读你的表结构和权限策略，自动暴露开箱即用的 REST API，省掉写大把重复 controller 和 service 的体力活。

GIS 专业地理引擎：PostGIS插件
算经纬度、画电子围栏、几何拓扑计算全包揽，整个行业的事实标准，专用地理软件基本没它能打。

这套东西配齐，大多数中早期系统基本不用再看分布式全家桶的脸色。数据全在单库里，事务有兜底，备份拿 pg_dump 一锅端，排查问题再也不用去五个控制台翻日志。

爽的一批。

## 溯源

