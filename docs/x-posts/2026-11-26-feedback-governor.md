# X 帖子：反馈回路，从蒸汽机到 Claude Code

- 写于 2026-11-26，Luke 自己发
- 引子：[Claude Code之父的三条心得](../../clips/2026-10-18-ayi-ainotes-boris-cherny-workflow-three-rules.md)
- 理论：[反馈](../../roots/feedback.md)、[控制论](../../roots/cybernetics.md)
- 配图：`2026-11-26-feedback-governor.png`（Codex 生成）

## 正文

Claude Code 的作者 Boris Cherny 说，用它最重要的一条：
给 Claude 一个验证自己工作的办法。有了这个反馈回路，质量能提高 2 到 3 倍。

这不是新发明。

1788 年，瓦特给蒸汽机装了一个离心调速器：转太快，两个铁球甩开，自动关小气门；转慢了，再开大。机器自己看结果、自己纠正。

1868 年，麦克斯韦写了《论调速器》，成了反馈控制理论的经典。

1948 年，维纳把这门学问叫作"控制论"（Cybernetics），词根是希腊语的"舵手"。英文里的 governor，调速器，也是"统治者"，来自同一个词。

AI 写代码最新的心得，和蒸汽机是同一个道理：
不让 agent 看结果，就像让舵手蒙着眼睛掌舵。

## 出处核对

| 说法 | 出处 |
|---|---|
| Boris：最重要的是给 Claude 验证自己工作的办法，反馈回路让质量提高 2～3 倍 | Boris Cherny 2026-01-02 串推（`roots/cherny-2026-claude-code-setup-thread.md`） |
| 1788 年瓦特把离心调速器用到蒸汽机上 | Wikipedia: Centrifugal governor |
| 1868 年麦克斯韦《On Governors》，反馈控制理论的经典 | 同上 |
| 维纳 1948 年取名 Cybernetics，来自希腊语"舵手"；governor 经拉丁语 gubernator 也来自这个词 | Wikipedia: Cybernetics（引维纳原书） |

注意：网上流传的"让画家蒙着眼睛画画"比喻，不是 Boris 原话，是转述者加的，正文里没用。
