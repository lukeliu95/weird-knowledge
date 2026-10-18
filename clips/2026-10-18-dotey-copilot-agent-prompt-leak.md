---
title: "Copilot Agent模式提示词泄漏"
author: "宝玉 (@dotey)"
url: https://x.com/dotey/status/1888050437644865668
source: X
published: 2025-02-08 02:21 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: 编程智能体
roots: []
---

## 原文

GitHub Copilot Agent 模式的系统提示词泄漏

今天破解了一下 GitHub Copilot Agent 模式下的系统提示词，可以看出来，它内置了一系列工具：

• search_codebase：进行自然语言搜索，用于在用户当前工作区中查找与其问题相关的代码或文档注释。
• run_in_terminal： 在终端中运行一个 shell 命令。
• edit_file：修改文件
• file_search：按照 glob 模式在工作区中搜索文件。只返回匹配的文件路径，最多 20 个结果。
• read_file：读取文件的内容。
• list_dir：列出目录内容。
• get_terminal_output：获取先前由 run_in_terminal 启动的终端命令的输出。
• get_errors：获取文件的编译或 lint 错误。
• get_changed_files：获取工作区内文件变更的 Git diff 列表。

所以每次用户操作，大语言模型就会看是否有必要调用这些工具，直到完成任务为止！

> 媒体：
> - https://pbs.twimg.com/media/GjOzuVlXgAAiM-2.jpg

## 溯源

