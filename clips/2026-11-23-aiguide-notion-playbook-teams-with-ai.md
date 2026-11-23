---
title: "Notion 万字手册：团队怎么和 AI 一起工作"
author: "Grant Miller (@AIGuide_)"
url: https://x.com/AIGuide_/status/2124241227927388263
source: X
published: 2026-11-21 20:39 UTC
saved: 2026-11-23
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: Agent 与 Skill
roots: [notion-2026-new-shape-for-work, division-of-labour, vendor-lock-in, parasuraman-2000-levels-of-automation, galls-law, you-arent-gonna-need-it]
---

## 原文

Notion just dropped a 10,000-word playbook on how teams should work with AI...

the biggest lessons:

1. stop using AI as a one-off chat. give every agent one shared place for your company's info so it never starts from zero
2. rent the intelligence, own the context. don't lock your team into one model provider
3. skills are good, "factories" are better. a factory is one shared agent for a specific job that a few people maintain and everyone uses
4. the best factory jobs repeat often, are easy to check and are cheap to get wrong, like support emails, weekly updates, sales follow-ups and invoices
5. start with a shadow run. let it draft instead of send until you trust it
6. keep it simple, watch it fail, then fix only what breaks

the simplest factory takes 5 minutes:
> make a "Slide Decks" database with to-do, doing and done
> trigger an agent whenever a new to-do is added
> it moves the card to doing, builds the deck, links it and moves it to done
> share it with your team and update the prompt every time it makes a mistake

> 媒体：
> - https://pbs.twimg.com/media/HXrSIjoXoAAUrqe.jpg

## 溯源

- 核心主张：团队用 AI 要从一次性聊天转向共享系统：给所有 agent 一个共用的公司信息库；模型租来用，上下文自己握着；建由少数人维护、大家共用、专做一类事的“工厂”。工厂挑重复、好检查、错了代价小的活，先影子运行只起草不发送，从简单开始，坏了再修。
- 源知识：
  - [Notion《A New Shape for Work》：上下文系统与 AI 工厂](../roots/notion-2026-new-shape-for-work.md) · 关系：直接源自 · 强弱：强。帖子转述的就是 Notion 的《A New Shape for Work》，原文结尾自称约一万字。6 条都能在原文找到：共享上下文系统（§2.2、§3.1），租模型、握上下文（§2.7），工厂胜过 skill（§4.1、§4.3），挑重复、可检查、错了代价小的活（§5.1 列了 7 个特征，帖子挑了 3 个，例子也对得上），影子运行（§5.3），从简单开始、看它坏了再修（§5.2），5 分钟的最简工厂（§4.6）。
  - [分工](../roots/division-of-labour.md) · 关系：直接源自 · 强弱：强。原手册 §1.1、§4.1、§4.2 明说工厂的价值是“专业分工和交易收益”（specialization and gains from trade），还点了 Adam Smith 的名。帖子第 3 条“少数人维护、大家共用”说的就是这个。
  - [供应商锁定](../roots/vendor-lock-in.md) · 关系：相近 · 强弱：弱（模型复核通过）。“别把团队绑在一家模型厂商上”（§2.7）就是在避免供应商锁定：哪家模型最好和哪个工作区最好是两个问题，没必要捆在一起赌。
  - [自动化的类型与等级模型](../roots/parasuraman-2000-levels-of-automation.md) · 关系：相近 · 强弱：弱（模型复核通过）。“先影子运行，只起草不发送，信任了再放开”（§5.3），就是先把自动化停在“给建议”这一级，可靠了、量也放上去了再升到“自动执行”，而且看出错的代价来定级别。
  - [加尔定律](../roots/galls-law.md) · 关系：相近 · 强弱：弱（模型复核通过）。原文说，与其一开始就做复杂的工厂，不如从简单的工厂开始，跑起来看它坏，只修真实出现的失败（§5.2）。这和“能运转的复杂系统都是从能运转的简单系统演化来的”是同一机制。原文没提 Gall。
  - [YAGNI（你不会需要它）](../roots/you-arent-gonna-need-it.md) · 关系：相近 · 强弱：弱（模型复核通过）。原文反对一开始就加一堆修补去防想象中的失败，理由是“我们都不擅长预测工厂会怎么坏，何必猜”（§5.2）。这就是 YAGNI 说的“真正需要时再做”。
- 本质：这条新知识本质上是分工和规模经济用在团队怎么落地 AI 上：少数人建好共享的工厂，大家共用。上线方法用的是加尔定律和自动化分级：从简单开始、先只给建议。
- 整理于：2026-11-23（第 12 轮）
