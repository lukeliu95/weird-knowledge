---
title: "Browserbase给智能体装黑匣子"
author: "AYi (@AYi_AInotes)"
url: https://x.com/AYi_AInotes/status/2049484868636025286
source: X
published: 2026-04-29 13:44 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

今天看到一个东西，我觉得是2026年Agent工程化到目前为止最重要的进展之一！

说实话，我之前对各种Agent浏览器工具已经有点审美疲劳了。

无非就是能点按钮、能填表单，一到复杂页面就乱点，一出问题就抓瞎。

但Browserbase刚出的这个/browser-trace不一样。

他们做了个演示：让Claude在TikTok上自动刷视频，50秒内刷了几十条，全程后台悄无声息地记录了一切：
2077个CDP事件，
43张DOM和截图快照，
320多个网络请求，包括失败的、中断的、媒体预加载的，
所有console日志、JS异常、页面生命周期。

最后自动生成了一份带仪表盘的HTML报告，点任何一个事件都能跳转到对应的截图和DOM。

卧槽这个就太屌了，
以前Agent在网页上乱点卡住，
兄弟们知道最痛苦的是什么吗？
我想了很久，答案就是：你根本不知道它为什么卡住🤣🤣🤣

它看到了什么？它点击了哪里？网络请求返回了什么？有没有JS报错？
传统的Playwright调试已经够痛苦了，Agent更惨，

它自己决策、自己执行、自己出问题，你连复现都做不到。

所以有时候你会发现，我们之前一直在给Agent造手和眼睛，但从来没人给它造黑匣子。

我觉得这才是/browser-trace真正的意义。
它不是一个更好的调试器，
更像一个浏览器Agent的OpenTelemetry。
把浏览器从Agent的黑箱执行器，变成了一个完全透明、可查询、可复现的系统。
而正是有了这种真正的可观测性，才构成了Agent可靠性的起点。

> 媒体：
> - https://video.twimg.com/amplify_video/2049484745223114752/vid/avc1/434x270/XsAGGZZXWjw9XAEF.mp4?tag=21

## 溯源

