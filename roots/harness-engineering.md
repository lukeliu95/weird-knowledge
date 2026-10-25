---
name_zh: "外壳工程（agent = 模型 + 外壳）"
name_en: "Harness engineering (Agent = Model + Harness)"
proposer: "Mitchell Hashimoto 先用这个词；Vivek Trivedy（LangChain）给出“Agent = Model + Harness”的定义；OpenAI 的 Ryan Lopopolo 同期以此为题发文"
year: "2026"
type: 方法论
verified: true
---

# 外壳工程（agent = 模型 + 外壳）（Harness engineering (Agent = Model + Harness)）

## 一句话

agent 等于模型加外壳，外壳是模型以外的一切（循环、工具、上下文、安全、调度、扩展）；外壳工程就是设计和演进这层运行环境，比如 agent 每犯一次错，就在环境里加一道机制让它以后不再犯。

## 原始出处

- My AI Adoption Journey（Step 5: Engineer the Harness），Mitchell Hashimoto，2026-02-05，https://mitchellh.com/writing/my-ai-adoption-journey
- Harness engineering: leveraging Codex in an agent-first world，Ryan Lopopolo，OpenAI，2026-02-11，https://openai.com/index/harness-engineering/
- The anatomy of an agent harness，Vivek Trivedy，LangChain Blog，2026-03-10，https://www.langchain.com/blog/the-anatomy-of-an-agent-harness
- Harness engineering for coding agent users，Birgitta Böckeler，martinfowler.com，2026-04-02，https://martinfowler.com/articles/harness-engineering.html
- 争议：谁最先提出有争议：Hashimoto 2026-02-05 的博文自称“我开始管这叫 harness engineering”，并说不知道有没有公认的词；OpenAI 的 Lopopolo 2026-02-11 以同名发文（openai.com 对本次抓取返回 403，标题和日期据搜索结果和 InfoQ 报道）；Barbaste 等 2026 记为 Hashimoto 先随口用、Trivedy 下定义并普及“Agent = Model + Harness”。“scaffold（脚手架）”是更早的近义词。

## 更底层的源头

- [上下文工程](context-engineering.md) · 关系：直接源自
- [反馈](feedback.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [Wavestone 拆了 11 个编程 agent 的源码：每个都要在同样 7 个子系统上做取舍（推文转述，“90 行外壳覆盖全部 7 个部件”是说错的）](../clips/2026-10-25-arindam-1729-seven-building-blocks-of-coding-agents.md) | 直接源自 | 强 |
| [拆 11 个编程 agent 的源码看外壳怎么搭：7 个子系统、29 种常见设计；没有一家用通用 agent 框架、没有一家用向量检索读代码，skill 的普及已略超 MCP（9/11 对 8/11），外壳正从工具变成平台](../clips/2026-10-25-barbaste-harness-engineering-eleven-coding-agents.md) | 直接源自 | 强 |
| [Opus 4.5 的跃升可能来自 Claude Code 收集的数据；它能压住自身的发散，有合适的 harness 就能自己跑](../clips/2026-10-25-mizchi-opus-45-harness-data.md) | 相近 | 弱（模型复核通过） |
