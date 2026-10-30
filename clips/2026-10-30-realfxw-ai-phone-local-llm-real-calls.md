---
title: "ai-phone：Mac 本地大模型接管真实电话"
author: "TechVerser (@realfxw)"
url: https://x.com/realfxw/status/2115702863632494664
source: X
published: 2026-10-29 07:10 UTC
saved: 2026-10-30
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
kind:
topic:
roots: []
---

## 原文

终于有人把“本地大模型打真实电话”做出来了，而且完全开源！

以往体验市面上的各类 AI 电话助手，最让人顾虑的就是隐私安全：通话录音、转写文本、沟通对象全都会留在第三方云端。开发者刚刚开源的 ai-phone 则彻底打通了本地闭环——让你的 Mac 直接接管真实电话线路，所有推理均在本地完成，通话数据完全不出机器。

🛠️ 核心技术栈（基于 Apple Silicon & MLX）：

语音识别（STT）： Parakeet TDT 0.6B 本地运行，极速语音转文字

语言模型（LLM）： 默认本地运行 Qwen3.5 4B（32GB 内存支持 9B 4-bit），同时也支持接入自己的 Claude 或 ChatGPT 端点

语音合成（TTS）： Kokoro 82M / Phonon，生成自然流畅的声音

通信接入： 通过 SIP 协议直连 Telnyx 或 Twilio，直接购买或绑定真实电话号码（月租约 1 美元）

✨ 核心亮点：

低延迟与实时打断： 在 Apple Silicon 芯片上实测首字响应延迟约 1~1.5 秒；支持实时插话打断（Interruption），一旦你开口，AI 会立刻停下倾听。

支持外部 Agent 联动： 提供了 call、listen、say、hangup 等标准化 CLI 接口，可以直接让 Claude Code、Codex 等编码智能体通过命令编排通话，自动完成预约餐厅、电话咨询等任务。

本地守护进程： 提供向导式 CLI 配置，一行命令拉起本地守护进程，静默接听来电或随时发起外呼。

⚠️ 当前要求与限制：

仅支持搭载 Apple Silicon 的 macOS 系统

目前为单路通话，优先支持英文环境

项目刚刚上线，对本地 AI 语音助手与 SIP 通信落地感兴趣的朋友值得关注：https://t.co/n2G7fQGsnG

> 媒体：
> - https://pbs.twimg.com/media/HVx6wL_XUAAWCBw.jpg

## 溯源

