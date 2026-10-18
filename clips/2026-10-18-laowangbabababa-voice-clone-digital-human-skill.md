---
title: "语音克隆加数字人出镜 Skill"
author: "产品经理老王霸 (@laowangbabababa)"
url: https://x.com/laowangbabababa/status/2085711630516584755
source: X
published: 2026-08-07 12:56 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

有人把 MiniMax 语音克隆和 HeyGen 数字人出镜，写成了一个 Agent Skill。

用法不复杂。

给它一张正面肖像，一段声音样本，一份脚本。Agent 拿到先不干活，先看声音格式对不对，文件大小超不超，肖像够不够清晰。

有一项没过就会停下，不会让你付了 API 调用的钱才发现素材有问题。

校验过了才进正式流程。MiniMax 做语音克隆生成旁白，HeyGen 拿图片驱动视频。

你可以先出一版 15 秒 720p 预览视频，仔细看口型、面部变形、眨眼幅度。确认没问题，再生成 1080p 成片。

出错后的恢复策略也做得特别好。API 超时不直接判失败，下载失败只重试下载不重开任务，签名链接过期不另起新请求。每次出问题优先用已有结果恢复，而不是再来一遍付费调用。

把校验、重试、状态追踪这套产线逻辑，写成 Agent 能执行的指令。

下面是作者的视频，很哇塞 @Zesee

> 媒体：
> - https://video.twimg.com/amplify_video/2085711357257863168/vid/avc1/478x270/C9LoYih8vYQOtBrJ.mp4?tag=29

## 溯源

