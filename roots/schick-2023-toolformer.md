---
name_zh: "Toolformer：语言模型自学使用工具"
name_en: "Toolformer: Language Models Can Teach Themselves to Use Tools"
proposer: "Timo Schick、Jane Dwivedi-Yu、Roberto Dessì 等（Meta AI）"
year: "2023"
type: 论文
verified: true
---

# Toolformer：语言模型自学使用工具（Toolformer: Language Models Can Teach Themselves to Use Tools）

## 一句话

让语言模型在生成的文本里插入形如 [Calculator(400 / 1400) → 0.29] 的 API 调用标记，由外部程序执行后把结果接回文本；模型用自监督的方式学会何时调用、调用哪个、传什么参数。

## 原始出处

- Toolformer: Language Models Can Teach Themselves to Use Tools, Timo Schick et al., 2023, arXiv:2302.04761，https://arxiv.org/abs/2302.04761

## 更底层的源头

- [自监督学习](self-supervised-learning.md) · 关系：直接源自
- [ReAct：推理与行动协同](yao-2022-react.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [ChatGPTMac版提示词触发共享屏幕](../clips/2026-10-18-dotey-chatgpt-mac-screen-share-prompt.md) | 相近 | 弱（模型复核通过） |
