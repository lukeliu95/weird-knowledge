---
title: "逆向 Wispr Flow，微调 1.7B 小模型做本地语音输入 phonon"
author: "Elliot Arledge (@elliotarledge)"
url: https://x.com/elliotarledge/status/2118386115170496855
source: X
published: 2026-11-05 16:53 UTC
saved: 2026-11-06
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 语音与数字人
roots: []
---

## 原文

i reverse engineered wispr flow, then used deepseek to fine-tune LFM3-1.7B. the result is on par with the wispr flow models you pay for, and it's free, open source and runs entirely on your mac.

key-up latency is 65 ms on my m4 max vs ~520 ms for wispr flow on the same clips. a 6 minute yap session pacing around my office still lands in about a quarter second.

> rust backend with a native metal engine: each decode step runs as one fused megakernel
> a dflash2 speculative drafter is built into the engine, trained on my local 4 x rtx pro 6000 server
> parakeet transcribes, LFM3-1.7B refines. both stream while you talk, so key-up only waits on the last chunk
> never leaves your macbook, so slow internet or bad ping is no longer an issue
> import your own dictionary of terms for your workflow
> i picked every default myself. it feels amazing out of the box
> adapts to the app you're in: discord is lowercase casual, slack and email are formal, claude code gets clear prompts
> training data: 77k transcripts of public audio and synthetic dictations, each rewritten by deepseek v4.1 flash 1017 following a written spec of what "what you meant" means, in 4 writing modes. none of my own dictations went into it
> blind judge (claude opus) on an hour of lectures: phonon's text preferred 90 times, wispr's 23
> built with claude opus 5.5 [xhigh]

brew install --cask infatoshi/tap/phonon

> 媒体：
> - https://video.twimg.com/amplify_video/2118379378275135488/vid/avc1/1920x1080/PlmLHoZYPFNvNZZq.mp4?tag=29

## 溯源

