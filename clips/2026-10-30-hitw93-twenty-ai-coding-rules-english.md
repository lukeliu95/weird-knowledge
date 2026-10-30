---
title: "Tw93 把 AI 编程习惯写成 20 条规则（英文版）"
author: "Tw93 (@HiTw93)"
url: https://x.com/HiTw93/status/2115805352520282623
source: X
published: 2026-10-29 13:58 UTC
saved: 2026-10-30
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

I spent an afternoon turning my AI coding habits into 20 rules that you and your agent can learn from together.

Briefing
1. Stop dictating the implementation. Describe the outcome you want. Models are good enough now, so aim high and don't worry that it can't be done.
2. Give your agent the background and the goal: why it matters, who it's for, what great looks like. Then let go of the technical details.
3. Use the best model available. A weaker one just means more back-and-forth, wasted time and frustration.
4. Before adding a feature, setting or toggle, have the agent check with you first. Don't let it add features, toggles or copy nobody will use, and have it write your product rules down as it goes.
5. Think big, but have it build in the smallest usable steps and commll back anytime.

Rules
6. Teach it how you talk: "look at" or "analyze" means read and report, "fix" or "change" means edit. Commits, releases and deletions always need your OK.
7. In AGENTS.md or CLAUDE.md, write only what it can't learn from the've already ruled out. Never paste keys or tokens into the chat. If you do, treat them as leaked and rotate them.
8. Prompts alone won't hold hard rules. Enforce them with scripts, anthe checks actually pass.

Coding
9. Before writing code, have it explain what it will change and what that will affect, so you have the context to make the call.
10. Have it build a verification script for the project, run it at ch results. Over time, that becomes your agent's test suite.
11. Parallel agents each get their own worktree and commit only their own changes. Once everything is merged, run the full test suite.

Debugging
12. Find the cause before fixing. If two fixes fail, add logs and looguessing.
13. If three fail, clear the context and start fresh with the problem, the goal and what you've already tried.

Review
14. Keep the agent that writes separate from the agent that reviews, her.
15. Cap reviews at 3 rounds. From round two on, only review what's new.
16. The riskier the change, the deeper the check. Deletions, paymentsdoors, so check them yourself and click through the real result.

Shipping
17. Every commit says what changed, how it was verified and how to roll it back. Your git history becomes great context for the next agent.
18. Use it yourself or give it to early testers first. Add a beta updse doesn't hit everyone.

Retro
19. Every production bug and user report gets a test case that runs before each release. Rerun them whenever you switch models to see if the new one holds up.
20. When fixing one thing, have it find and fix the same problem everures and visual polish.

## 溯源

