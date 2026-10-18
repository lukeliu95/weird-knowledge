---
title: "Hypit：给编程智能体用的开源视频语言"
author: "余温 (@gkxspace)"
url: https://x.com/gkxspace/status/2099808769043841452
source: X
published: 2026-09-15 10:33 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

爽了，AI 做视频终于迎来了自己的 Harness 时代，彻底告别手搓剪映和抽卡黑盒！！！

刚挖到一个极其硬核的开源项目：Hypit

它是专门给 Claude Code、Codex 这类 Coding Agent 打造的开源视频语言与编译系统，简单说就是视频领域的开源 Harness。

为什么这玩意儿这么香？我来给大家详细讲一讲：
以前大家做 AI 视频最头疼的两件事：
1、视频模型是个抽卡黑盒，只给一段写死的 MP4，改一个字就得整条视频重抽，费钱、费时间。
2、传统剪辑软件是给人手拖时间线设计的，让 Agent 去对时间码和图层，根本没法自动化。

Hypit 直接把时间线干掉了，用代码来写视频：
1、把特效锚定在词上：它独创的 Hook 机制，把特效、B-roll、字幕直接挂在台词的词上，而不是卡在第几秒。你改一句话，后面的字幕、画面和音效自动重新对齐！

2、爆款视频直接 Clone：看到一条 viral 视频，直接对 Agent 敲 /hypit clone this video，它拆脚本、把整套镜头、B-roll、字幕和特效反向工程成一份可编辑代码。换人、换产品、换语言，一条命令批量跑出 100 个变体！

3、花钱前所有付费素材先占位预览，满意再调 API，修改时旧素材 100% 复用，省钱省到极致。

以前很多此类收费产品，效果还很辣鸡，@hypitai 彻底开源免费，纯代码渲染只要 $0，自带 API Key 跑一条完整视频也就 1 刀左右，很逆天。

强烈建议大家先把仓库收藏星标一下，后面批量做矩阵或者搞出海营销绝对用得上：

🔗：https://t.co/vAzIUHbcdU

> 媒体：
> - https://video.twimg.com/amplify_video/2099731237539823616/vid/avc1/500x270/YCftwYWnpGnzpibq.mp4?tag=29

## 溯源

