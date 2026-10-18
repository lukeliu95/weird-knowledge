---
title: "提取图片视觉风格输出JSON的提示词"
author: "123olp (@123olp)"
url: https://x.com/123olp/status/1996910851568075199
source: X
published: 2025-12-05 11:53 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: 图像生成
roots: []
---

## 原文

请从输入图像中智能、全面地提取视觉风格信息，并将结果以**严格有效的 JSON** 格式输出。  
字段数量不做限制，可根据图像特征灵活增减，但需保持结构清晰、语义明确、分类合理。  
以下为建议的通用结构，请在此基础上根据实际情况动态调整、增删字段：

{
  "colors": {
    "palette": [],                 // 色板（HEX/RGB）
    "dominant_colors": [],         // 主色
    "accents": [],                 // 点缀色
    "tone_contrast": ""            // 明度/色温/对比特征
  },
  "typography": {
    "fonts": [],                   // 字体名称或风格
    "style_features": [],          // 字重/字宽/字型特征
    "hierarchy": ""                // 排版层级
  },
  "composition": {
    "layout": "",                  // 布局方式
    "balance": "",                 // 对称、非对称、中心构图等
    "focal_points": [],            // 视觉焦点
    "spacing_and_rhythm": ""       // 留白、节奏、密度
  },
  "visual_effects": {
    "textures": [],                // 纹理
    "lighting": "",                // 光影表现
    "shadows": "",                 // 阴影类型
    "filters": [],                 // 滤镜或后期效果
    "other_effects": []            // 其他识别到的风格特征
  },
  "overall_style": {
    "design_language": "",         // 如极简/复古/赛博等
    "emotional_tone": "",          // 感性气质，如温暖/冷峻/活泼
    "reference_genres": []         // 类似的风格类型或艺术流派
  }
}

要求：
- 输出必须是**纯 JSON**，不包含任何额外说明文字。  
- 可根据图像内容自由扩展或删减字段，但需保持命名专业、语义明确。  
- 无法判断的字段请使用空字符串、空数组或省略。

## 溯源

