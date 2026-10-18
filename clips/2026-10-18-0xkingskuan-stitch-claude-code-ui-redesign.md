---
title: "用Stitch一小时重做丑UI"
author: "币世王 (@0xKingsKuan)"
url: https://x.com/0xKingsKuan/status/2040357839714275647
source: X
published: 2026-04-04 09:16 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

丑 UI 得救了，看完后沉默了三分钟！

分享 @PrajwalTomar_ 这篇文章，因为它解决了我（和 99% 用 AI 建 App 的独立开发者）最头疼的问题；功能做好了，但 UI 丑得像猪。

作者 Prajwal Tomar 直接甩出一个工作流：Google Stitch 2.0 + Claude Code（MCP 连接），号称能把普通 AI 产品 1 小时重塑成专业级设计。我试了，真的香到离谱。

以前：

•  功能用 AI 几小时就做好了
•  但 UI 千篇一律、字体乱飞、颜色不统一
•  找设计师？$3000 起步 + 等两周
•  自己改？改一个屏幕崩另一个

🟢

现在整个流程被他压缩成这样（超简单 5 步）：

1.  丢截图给 Stitch 2.0
 把你当前 App 的主界面截图扔进去，或者丢 2-3 张 Dribbble/21st.dev 的灵感图。

2.  一句话提示词
 “帮我从新设计成暗黑极简 SaaS 风格，标题用 serif 字体，正文用干净 sans，生成 4 个变体”

3.  Stitch 自动生成完整设计系统 它会自动给你输出：

•  完整的 typography 层级
•  主/辅/三级色系 + 所有深浅值
•  组件规范、间距、阴影、dos & don’ts
 全部打包成一个 design.md 文件

4.  把 design.md 扔进你的项目
 这份 markdown 就是设计圣经，Claude Code 以后每次生成新页面都会死死参考它，彻底杜绝每 prompt 一次风格就飘的灾难。

5.  MCP 连接后让 Claude 直接读真实设计
 通过 Stitch 的 MCP，Claude 不再是靠文字猜设计、而是直接读取 Stitch 画布的真实 HTML/CSS，精准还原 + 自动加 hover、过渡动画等细节。

🟢🟢

作者实测：

以前需要花几千美元 + 几周的 UI 重做，现在一个人下午就能干完。他还诚实写了缺点（字体偶尔要微调、超复杂布局可能有 5% 偏差），但整体体验已经把以前的流程甩出几条街。

2026 年了，功能已经不是护城河，好看才是。

那些还在为 MVP 界面发愁的开发者，真的该醒醒了。这套工作流就是把高端设计这个能力，从大厂设计师手里，抢到了每一个人手里。

## 溯源

