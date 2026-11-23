---
title: "知识库20万token以内不用RAG：全文放进提示词加提示词缓存"
author: "nasuuu (@nasuvit_z)"
url: https://x.com/nasuvit_z/status/2124441515196129660
source: X
published: 2026-11-22 09:55 UTC
saved: 2026-11-23
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

Anthropicの公式ブログで、ナレッジベースが20万トークン（約500ページ）以内なら、RAGを構築するのではなく、全文をプロンプトに含めてClaudeに処理させる方法があると紹介されている。
ナレッジベースにあたる部分をプレフィックス化して、Prompt Cachingを組み合わせれば、レイテンシを2倍超改善し、コストを最大90%削減できるとのこと。
長いコンテキストウィンドウを活用できるがゆえの戦略。
https://t.co/ntRTEP9fgG

## 溯源

