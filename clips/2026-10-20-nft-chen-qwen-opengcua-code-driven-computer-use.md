---
title: "阿里开源 OpenGCUA：让模型写代码来操作电脑"
author: "SuSu_酥酥👅 (@NFT_Chen)"
url: https://x.com/NFT_Chen/status/2112201212644954125
source: X
published: 2026-10-19 15:16 UTC
saved: 2026-10-20
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: Agent 与 Skill
roots: []
---

## 原文

💥牛逼！阿里Qwen团队偷偷放了个“能自己写代码操作电脑”的神器，并且把它开源了！

以前的AI操作电脑，大多是看一眼截图、点一下、再看一眼，一步一步来，又慢又费token。

现在Qwen MAI开源的OpenGCUA不一样：它让模型自己决定“要不要看屏幕、怎么动手、怎么安排任务”，还能直接写一段带循环和判断的代码，把点鼠标、敲命令、调接口混在一起干。中间结果出来就能接着干，不用每次都问模型。

实测效果很猛： 🔹在OSWorld-v2上，包括GPT-6 Astra、Claude Opus 5在内的8个大模型，平均分数直接涨了19.6分，步骤少了53%。

🔹还开放了跨设备SDK（电脑、手机、浏览器都能统一控制）、macOS真机运行框架，以及这8个模型的完整操作轨迹，方便大家复现和二次开发。

想自己跑起来，几步就行（macOS）：
1️⃣克隆仓库：git clone https://t.co/6LhK3RHtAg

2️⃣用uv建环境并安装依赖（推荐Python 3.12）

3️⃣运行mu setup macos和浏览器设置

4️⃣复制配置文件，填上你的API Key和模型名（支持Qwen）

5️⃣系统里给权限后直接跑agent

👉 项目地址：https://t.co/6LhK3RHtAg 论文：https://t.co/jipNpIyDbh

#OpenGCUA #Qwen #阿里开源 #AI操作电脑 #ComputerUse #开源项目 #通义千问 #Alibaba

> 媒体：
> - https://pbs.twimg.com/media/HVALynsa8AAlC6s.jpg
> - https://pbs.twimg.com/media/HVALyn0aMAEYhSh.jpg
> - https://pbs.twimg.com/media/HVALynwbsAAT_cw.jpg

## 溯源

