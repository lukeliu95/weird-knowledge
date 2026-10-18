---
title: "Griffin 全双工视频模型解读"
author: "Max For AI (@MaxForAI)"
url: https://x.com/MaxForAI/status/2105877225237352691
source: X
published: 2026-10-02 04:27 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已归档
kind: 工具
topic: 语音与数字人
roots: []
---

## 原文

卧槽。。。有点吓人，第一个通过图灵测试的视频模型出现了。。。

刚刚 @tavus  发布了一个叫 Griffin 的新模型，他们直接给它定义了一个新类别：Human Interaction Model，HIM，人类交互模型。

Tavus 找了 54 个美国和欧洲的参与者，让他们和 Griffin 进行 1 分钟视频通话，事先不告诉对面是 AI。

聊完之后，有 26 个人（48%）认为自己刚才是在和真人视频。

而 Tavus 上一代系统 Phoenix-4.5，用同样的方法测试，41 个人里只有 1 个被骗过去，通过率只有 2.4%。

Tavus 因此把 Griffin 称作第一个通过实时视频图灵测试的模型。

我还去看了下它的技术路线，Griffin 不再是以前那种 ASR → LLM → TTS → 数字人，一段一段串起来的 Pipeline。

它做的是一个 full-duplex 的 video-to-video 系统。

你说话的时候，它还在持续看你、听你、理解你的表情和动作；它自己说话的时候，也没有停止感知。

每隔不到一秒，它都在重新判断现在该继续说、停下来、插一句，还是等你说完。

所以你可以打断它，它会停；你不说话，它能判断这是在思考还是话讲完了。

你拿个东西到摄像头前，它一边跟你说话，一边还能看你手上到底在干什么。

这个区别其实很大。

过去的实时语音模型解决的是“怎么让 AI 和人自然地说话”。

Griffin想做的是怎么让 AI 像人一样参与一场面对面的互动。

这让我想到了著名AI圣经电影《Her》。

最后需要提一下的是在 NVIDIA 的 VideoFDB 全双工音视频 Benchmark 里，Griffin-Lite 目前 generation 和 perception 两项都是第一。

生成侧 3.83 分，人类参考是 3.92；感知侧 3.73，人类是 4.20。Ta

所以我感觉，下一代 AI Agent 的 UI 可能真的会发生一次变化。

不是你打开一个 Chatbot，对着输入框想 Prompt。

而是它就在摄像头另一边。

你看着它，它也看着你。

而且这次，已经有接近一半的人没认出来了。

## 溯源

