---
name_zh: "用更好的图片描述改进图像生成（DALL·E 3 论文）"
name_en: "Improving Image Generation with Better Captions"
proposer: "James Betker, Gabriel Goh, Li Jing, Tim Brooks 等（OpenAI）"
year: "2023"
type: 论文
verified: true
---

# 用更好的图片描述改进图像生成（DALL·E 3 论文）（Improving Image Generation with Better Captions）

## 一句话

训练一个专门的描述模型，把训练集图片重新标注成高度详细的描述，生成模型就更听提示；因为模型适应了长描述，推理时要用大模型把用户的短提示“扩写”成同样详细的描述，避免在训练分布之外采样。

## 原始出处

- Improving Image Generation with Better Captions, Betker et al., OpenAI, 2023（第 3.5 节讲提示扩写），https://cdn.openai.com/papers/dall-e-3.pdf

## 更底层的源头

- [数据集偏移](dataset-shift.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Sora 团队伯克利课堂分享字幕翻译](../clips/2026-10-18-dotey-sora-team-berkeley-talk.md) | 直接源自 | 强 |
