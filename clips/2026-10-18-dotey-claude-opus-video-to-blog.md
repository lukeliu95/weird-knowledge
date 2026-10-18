---
title: "Claude 把两小时视频写成博客"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/1764741444974051703
source: X
published: 2024-03-04 19:55 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: 提示词与写作
roots: []
---

## 原文

这个Claude 3 Opus的测试案例让人印象深刻，作者将2小时的视频文稿和一些关键帧的截图一起扔给API，最终生成了一篇不错的HTML格式的图片并茂的博文。

项目地址：https://t.co/Fa0VWC7Mum

Prompt：
用户:这里有一段视频的文字记录,包括不同时间戳的屏幕截图。
该文字记录是由AI语音识别工具生成的,可能包含一些错误/不当之处。
你的任务是将文字记录转换为一个html博客。
博客的写作风格,包括文字和代码之间的期望平衡,在<desired_writing_style>的屏幕截图中有所说明。 
博客的视觉风格,包括页面布局、字体、标题和图像样式,在<desired_visual_style>中有所描述。

{transcript_with_name}  
<desired_writing_style>
{desired_writing_style}
</desired_writing_style>
<desired_visual_style> 
{desired_visual_style}
</desired_visual_style>

这份文字记录有一些噪音。请按照以下指南将其重写为一个html格式的博客:
- 输出有效的html
- 在适当的地方插入章节标题和其他格式
- 使用样式使图像、文本、代码、标注和页面布局、边距看起来像<desired_visual_style>中的示例
- 删除任何口头禅
- 如果有重复的信息,只呈现一次 
- 用<desired_writing_style>中显示的风格改写对话内容,包括标题,使叙述结构更容易理解
- 每个文字记录包含太多图像,所以你的输出应该只包括最重要的1-2张图像
- 选择能提供与文字记录相关的插图的图像
- 优先包含显示完整代码的图像,而不是部分代码
- 在相关时转录重要的代码片段和其他有价值的文本
- 如果某个图像有助于说明文字记录的某个部分,请包含它
- 要包含图像,请插入一个带有src="frames/hh_mm_ss.jpg"的标签(例如"frames/00_12_35.jpg"),准确复制文字记录中图像上方插入的时间戳 
- 为图像添加标题
- 不要添加任何无关信息:只包括在文字记录或图像中提到的内容

你的最终输出应该适合收录到教科书中。

助手:<!DOCTYPE html>

## 溯源

