---
title: "Claude Code生成咨询级幻灯片"
author: "Juntaro (@xjuntaro)"
url: https://x.com/xjuntaro/status/2001249186914992139
source: X
published: 2025-12-17 11:12 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: 设计与前端
roots: []
---

## 原文

Claude Code × Nanobanana Skillsでスライド生成したら、クォリティが一発でほぼ完成版のコンサルレベルだったのでやり方を解説。↓　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　

引用ポストが公表だったので、コーディング以外のClaude Codeの使い方を詳しく解説してみます。
まずは「Claude Code × Nanobanana Skillsでスライド生成」。
実験してみた結果、MCPよりSkillsが安定した。

✅️やり方
１）Cursorで適当なフォルダを開く
２）summary .mdみたいなマークダウンファイルで、スライド化したい内容をCursorと相談しながら書く
３）.claude/skillsフォルダに、gemini_image .pyのような、NanobananaのAPIを叩くPythonファイルでClaude CodeのSkillsファイルを作成
４）以下に記載のプロンプトでClaude Codeを実行

基本的にはNotebookLMを使うのが良いと思いますが、自分でもっとプロンプトをコントロールしたい方、NotebookLMに課金したくない方向け。

✅️プロンプト
```
summary .md を読んだ上で、Nanobanana Proの画像生成skillsを並列で実行して、以下の通りスタートアップピッチ資料を作成して。

１）直列：スタートアップピッチ資料の構成を考える。出力は、それぞれのスライドの中身。
２）直列：ピッチ資料のデザインの雰囲気を統一するため、それぞれのスライドに記載するデザインの統一プロンプト（詳細に5行くらい）を作成
３）並列：それぞれのスライドについて、画像生成プロンプトを作成
４）並列：それぞれのスライドについて、画像生成のskillsを実行（出力：./{今日の日付}-pitch-deck-slide-{# number} .png）

スライドは16:9のワイドaspect ratioで。スライドはすべてモダンなシリコンバレースタイルで投資したくなるプロフェッショナルな資料。
デザインの統一プロンプトを作成する時はexample .comにアクセスしてテーマカラーなどを確定する。全てのスライドは日本語で記載することを明示して。

ロゴ： logo .png
アイコン： icon .png
```

> 媒体：
> - https://video.twimg.com/amplify_video/2000954244120432640/vid/avc1/480x270/E9dnFjNzwfyEKpfm.mp4?tag=21

## 溯源

