---
name_zh: "GLM-5.3：同一底座只靠扩展后训练"
name_en: "GLM-5.3 (Z.ai model card and developer docs: same base model as GLM-5.2, every gain comes from post-training)"
proposer: "智谱（Z.ai）"
year: "2026"
type: 研究报告
verified: true
---

# GLM-5.3：同一底座只靠扩展后训练（GLM-5.3 (Z.ai model card and developer docs: same base model as GLM-5.2, every gain comes from post-training)）

## 一句话

智谱自报：GLM-5.3 和 GLM-5.2 用同一个底座（架构、总参数、激活参数都不变），所有提升都来自后训练，主要是把训练环境扩展成更像专家真实工作的长链条任务、自动合成环境和不依赖标准答案的验证器、用解题记录找出并堵住奖励漏洞；Terminal-Bench 3.0 从 4.6 升到 28.3，网安漏洞发现和利用能力涨得比预期快；官方承认这套流程仍需要大量人工参与。

## 原始出处

- GLM-5.3 Overview, Z.ai 开发者文档, 2026，https://docs.z.ai/guides/llm/glm-5.3
- zai-org/GLM-5.3 模型卡（README，含基准表和评测设置）, Z.ai, 2026，https://huggingface.co/zai-org/GLM-5.3
- Thoughts About Scaling Law, 唐杰（智谱）本人的 X 长文, 2026-08-19，https://x.com/jietang/status/2089941544581403107
- Z.ai 发布记录（GLM-5.3 条目日期 2026-08-18），https://docs.z.ai/release-notes/new-released
- 争议：数字都是智谱自测（Terminal-Bench 3.0 用 Claude Code 做外壳、3 次平均），截至核对时没找到第三方复现；发布日期 Z.ai 发布记录写 2026-08-18，部分媒体写 8 月 14 日；唐杰说只多做了“一个月”长程环境和强化学习，官方文档没写时长。

## 更底层的源头

- [强化学习](reinforcement-learning.md) · 关系：直接源自
- [DeepSeek-R1：用强化学习激发推理能力](guo-2025-deepseek-r1.md) · 关系：相近
- [验证的不对称与验证者法则](wei-2025-verifiers-law.md) · 关系：相近
- [AI 安全的具体问题](amodei-2016-concrete-problems-ai-safety.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [GLM 5.3 只靠后训练大涨，被 SemiAnalysis 嘉宾称为警钟](../clips/2026-10-18-nft-chen-glm-5-3-post-training-wake-up-call.md) | 直接源自 | 强 |
