---
title: "Exa 2.0：为 AI 智能体重做的搜索引擎"
author: "Will Bryk (@WilliamBryk)"
url: https://x.com/WilliamBryk/status/1976733013171224599
source: X
published: 2025-10-10 19:34 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

For those unaware, search is undergoing a renaissance. AI triggered of course.

AI completely reorients both what search the world needs and what search algorithms are possible. This Exa 2.0 release is part of that story, and it's a sign of where search is going.

Search got big in the late 90s with the rise of the internet and Google, but by the 2010s and early 2020s it was hitting diminishing returns. How much better can you get at "costco near me" queries?

But now Agentic LLMs are making an increasing share of searches. They'll soon search the web faaaar more than humans. And the entire search stack needs to be revamped accordingly.

If you're a human, you lazily type a few keywords, click on a couple links, and generally prefer nice looking sites that other humans click on. Google was built for you.

If you're an AI, you can instantly output a complex query, maybe several in a row, can process tens or hundreds of results, and prefer pure knowledge over clickbait.

It would be shocking if the optimal search engine built for the latter creature was the same as the former one.

At Exa, we've been building a search engine from scratch for years for this agentic world. That world has arrived.

With this 2.0 release we get closer to the perfect search engine for agents we've been envisioning. Super low latency, super optimized for quality knowledge, can handle complex queries, and exposes  lots of controls to customize the search. Luckily it's also the kind of search engine I personally would prefer :)

We now offer the fastest search API in the world, "Exa Fast". It's <350ms P50 end-to-end from us-west-2. Around 300ms not including network.

That's technically lower than the blink of an eye (for slow blinkers). One day it'll be much faster than the blink of anyone's eye.

We also now offer one the slowest search APIs, "Exa Deep", at 3500ms P50. This is for AI products that want the highest quality search. Quality and latency are always a tradeoff, and we want to offer developers a knowledge API across this latency spectrum.

Building an extremely optimized search engine from scratch is no easy feat. It took a heroic effort from our eng and research teams for many months.

A sampling of things we shipped to get here:
- overhauled our crawling infra to waterfall different types of crawlers + parsers with LLM grading
- did a couple month training run (with many hiccups)
- invented a new technique for training embedding models
- somehow optimized our already hyperoptimized VectorDB by another 50%
- removed milliseconds from every part of the stack, from inference optimization to internode communication to nginx shenanigans

Our research exploration keeps revealing new unexplored avenues in this agentic world. I've never been more excited about where our search can go.

AI enables all sorts of new training and realtime techniques. What might've taken Google a thousand people to build a reranker can now be done with an LLM call. That means building Google-level search is no longer the bar... what if search was perfect?

Work on Exa 3.0 begins today. The search renaissance has just begun.

## 溯源

