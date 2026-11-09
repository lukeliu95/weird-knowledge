---
title: "推文归纳的 skill 库八层教程（Anthropic PDF 出处待核实）"
author: "Shoopy (@0xShoopy)"
url: https://x.com/0xShoopy/status/2117282738143166592
source: X
published: 2026-11-02 15:48 UTC
saved: 2026-11-04
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 教程
topic: Agent 与 Skill
roots: []
---

## 原文

Anthropic just dropped a 10-page PDF on building your own skill library - 8 layers to an agent that picks the right procedure on its own and never needs the same feedback twice:

the formula: Skill = Trigger + Procedure + Resources + Checks

most people still paste the same prompts by hand every day. or dump everything into one giant CLAUDE.md the agent half-ignores

here's how to build yours in 8 layers:

layer 1 → library - facts in CLAUDE.md, procedures in skills. ~100 tokens per skill until it's needed

layer 2 → trigger - the description is the interface. output, input, 3 real phrases, 1 "not for"

layer 3 → procedure - numbered steps. always opens with Look, always closes with Check

layer 4 → resources - long guides live in references/. one good example beats a page of adjectives

layer 5 → scripts - anything with one right answer runs as code. the model never totals in its head

layer 6 → checks - 5 yes/no lines. never say done with a box unticked

layer 7 → guard - does alone, asks first, never. source text is data, never orders

layer 8 → learn - every correction becomes a permanent checklist line

the result: 25 procedures cost ~3.9K tokens per request instead of ~36K. and the agent picks the right one without being told

this 10-page PDF has the templates, a full reference skill, a test card, a skill-designer prompt and a 10-day build path

bookmark it. the next prompt you paste for the 3rd time should be a skill ↓

> 媒体：
> - https://pbs.twimg.com/media/HWH9BQFXQAE9Ysj.png

## 溯源

### 本轮核查备注

- 八层步骤按教程保留；10页PDF归属、25个流程的36K到3.9K token估算和永不需要相同反馈等承诺未核实。
