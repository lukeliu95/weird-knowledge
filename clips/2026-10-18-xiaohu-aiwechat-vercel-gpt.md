---
title: "Vercel 免服务器接入公众号"
author: "小互 (@xiaohu)"
url: https://x.com/xiaohu/status/1767033651123171689
source: X
published: 2024-03-11 03:43 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: Agent 与 Skill
roots: []
---

## 原文

AIwechat-Vercel：无需服务器 无需备案 将GPT接入微信公众号

AIwechat-Vercel利用 Vercel 的 Serverless Functions 提供后端服务，无需自己管理服务器、只需一个可以绑定到 Vercel 的域名（无需备案）

实现将 AI 功能集成到微信公众号中，支持GPT、星火、通义千问、Gemini等

主要功能：

1、AI对话能力：集成多种AI服务（如GPT、星火、通义千问、Gemini等），允许微信公众号通过文本消息与用户进行智能对话。

2、超时回复与连续问答：通过使用 Vercel 创建的 Redis 实例，实现了超时回复和记忆对话内容（最长30分钟），从而支持连续问答的功能。

3、图床功能：用户发送图片到微信公众号后，可自动返回图片的URL，方便用户分享和存储图片。

4、被关注时自定义回复：为新关注的用户提供自定义的欢迎消息或其他回复，增强用户体验。

GitHub：https://t.co/85ZyGXMFt7

视频教程：https://t.co/2MmZwh85do

> 媒体：
> - https://pbs.twimg.com/media/GIXDTjNasAASTkY.jpg

## 溯源

