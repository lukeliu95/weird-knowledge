---
title: "有道开源实时听写和实时翻译模型"
author: "实践哥 Li (@MinLiBuilds)"
url: https://x.com/MinLiBuilds/status/2102634531782308170
source: X
published: 2026-09-23 05:41 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 语音与数字人
roots: []
---

## 原文

卧槽，国产开源这次真把实时同传做出来了。😲
看了雨哥这条，我深度评测了网易有道的这两个模型。R2T2实时听写模型，T3PO 实时翻译。

🎉牛逼的是，两个模型一上来就把 Hugging Face 各自的 Trending 分区第一拿了：
R2T2：ASR #1 
T3PO：Translation #1

🔥更骚的是，这两个都能 Streaming，而且还能直接串起来。
怎么记住这两个模型，一个是R开头，Realtime，一个是T开头，Translation。后面阅读就会顺一些。

对面的话还没说完，中文字幕已经出来了。所以我直接搞了个很抽象的 Demo：

😍如果邻居娶一个乌克兰老婆，用英语连续跟他吵 30 秒。
中间老公回嘴、老婆切俄语、再切乌克兰语，我作为隔壁老王插话。
乌克兰语，它是没训练过的，我来盘盘它 😂

ASR+Translation, 除了视频字幕，以后直接挂在电脑上，挂录音豆里，挂手机上，挂AI眼镜上：
看剧、Zoom、Meet、Teams、Discord、跨国电话……
对面老外说话，你屏幕下面直接出中文。
出国泡吧搭讪也更方便。
下面视频就是完整实测。

R2T2｜实时 ASR https://t.co/OU833Calzj
T3PO｜实时翻译 https://t.co/W8VQX711nx

> 媒体：
> - https://video.twimg.com/amplify_video/2102633182051155968/vid/avc1/480x270/8nOSa9LbDGOAyURG.mp4?tag=29

## 溯源

