---
title: "Claude Code 配置 GLM 4.6"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/1980384391785263607
source: X
published: 2025-10-20 21:23 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: 编程智能体
roots: []
---

## 原文

正确在 Claude Code 中配置 GLM 4.6 的方法

{
    "env": {
        "ANTHROPIC_AUTH_TOKEN": "your_zai_api_key",
        "ANTHROPIC_BASE_URL": "https://t.co/UjDHScg5y8",
        "API_TIMEOUT_MS": "3000000",
        "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-4.5-air",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-4.6",
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-4.6"
    }
}

## 溯源

