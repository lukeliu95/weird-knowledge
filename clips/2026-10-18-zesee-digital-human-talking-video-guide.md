---
title: "数字人口播实战攻略"
author: "Rachel🥥 (@Zesee)"
url: https://x.com/Zesee/status/2077723280534851786
source: X Article
published: 2026-07-16 11:53 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 未整理
roots: []
---

## 原文

# 99% 的人没看出来的数字人口播实战攻略

昨天发了一条数字人讲 FDE 的口播视频，很多人的第一反应不是问我用了哪个工具，不相信这真的是数字人。我把整条数字人口播流程做成了一个可以复用的 Codex Skill。

GitHub 仓库：https://github.com/Jingyi-Wu-Richael/rachel-digital-human-production

我的最终工作流是：

素材检查 → MiniMax 生成配音 → HeyGen 15 秒样片 → 人工确认 → HeyGen 完整版 → 下载验片 → 状态归档

这套方案适合知识口播、短视频批量生产、课程讲解、产品介绍、多语言内容和固定 IP 数字人账号。

![Image](https://pbs.twimg.com/media/HNWLRYhWoAABTgS.jpg)

## 一、整条链路怎么分工

这套方案的核心，是把声音和画面拆开。

- MiniMax：负责声音克隆和 TTS。

- HeyGen：负责人像驱动、口型、表情和动作。

- Codex：负责检查素材、调用流程、记录状态、控制风险。

完整链路是：

1. 准备真人录音，用 MiniMax 海外版克隆声音。

2. 把文案交给 MiniMax TTS，生成克隆音色的 MP3。

3. 准备一张清晰正面人像。

4. 把人像和 MiniMax 生成的 MP3 上传到 HeyGen。

5. 先生成 15 秒样片，确认后再生成完整视频。

这里最容易犯的错是：声音已经由 MiniMax 克隆完成，却又让 HeyGen 重新配音。

如果目标是保留 MiniMax 的克隆音色，就应该把 MiniMax 生成的音频上传到 HeyGen，用这个音频驱动画面。不要切回 HeyGen 的 `script + voice_id` 方案，否则声音相似度会被覆盖。

## 二、HeyGen和 Minimax 模式怎么选

第一次操作，建议直接用 `Image-to-Video`，调用api key即可，一次2min的视频大约消耗2刀。

它比较轻：不用一开始就训练 Avatar，只要上传一张人像和一段音频，就能快速看到口型、表情、脸部稳定性和构图是否可用。

我的建议：

- 单条测试：先用 Image-to-Video。

- 固定账号长期生产：再做 Photo Avatar。

- 没验证前不要急着训练 Avatar，测试阶段越轻越好。

再说 MiniMax，我的建议：

- 第一次测试：用海外版 Voice Clone 克隆声音，再用 TTS 生成 MP3。

- 追求质量：优先选 `speech-2.8-hd`。

- 追求速度和批量预览：可以用 `speech-2.8-turbo` 先跑测试。

![Image](https://pbs.twimg.com/media/HNWLh8PXkAAXR9u.jpg)

![Image](https://pbs.twimg.com/media/HNWOFu1XAAA_tKR.jpg)

## 三、素材准备：不用复杂，但必须干净

声音克隆效果不好，很多时候不是模型不行，而是样本不干净。

MiniMax 当前官方要求里，声音样本需要满足：

- 格式：MP3、M4A 或 WAV。

- 时长：至少 10 秒，最多 5 分钟。

- 文件大小：不超过 20 MB。

- 可选提示音频：少于 8 秒，并且要提供与音频完全对应的文字。

实操里我更建议录 30 到 90 秒：单人、无背景音乐、无明显混响和电流声，音量稳定，语速接近日常口播，不要用过度降噪、变速或压缩严重的二手音频。

![Image](https://pbs.twimg.com/media/HNWNKgfXUAAiMth.jpg)

人像也一样，要干净：

- 正脸看镜头，五官无遮挡。

- 露出头、肩和上半身，人物占画面约 50% 到 70%。

- 嘴部清晰，不要被头发、手、滤镜遮挡。

- 竖屏短视频优先用 9:16 或接近 9:16 的图片。

- HeyGen Assets API 支持 PNG、JPEG 图片；普通素材上传单文件上限为 32 MB。

嘴部越清晰，口型越稳定；声音越干净，克隆越像本人。

![Image](https://pbs.twimg.com/media/HNWNWrfXwAAyrJX.jpg)

## 四、怎么放进 Codex 执行

我会把每个数字人项目都按同一个目录结构放：

然后对 Codex 说：

```text

请用 MiniMax 海外版声音克隆和 HeyGen API 制作数字人口播。

输入：

- 文案：inputs/script.md

- 人像：inputs/portrait.jpg

- 声音样本：inputs/voice-source.mp3

- MiniMax 密钥来自环境变量 MINIMAX_API_KEY

- HeyGen 密钥来自环境变量 HEYGEN_API_KEY

流程：

1. 先检查素材。

2. 先生成 15 秒样片。

3. 样片确认后再生成完整版。

4. 所有任务 ID 写入 work/job-state.json。

5. 不要在日志、脚本或文档中显示完整密钥。

```

这一步的重点是标准化。

你不需要相信自己每次都记得所有细节。你只需要把正确流程写进 Skill，让 Codex 每次按流程执行。

## 五. 这个 Skill 固定了什么

仓库地址：

https://github.com/Jingyi-Wu-Richael/rachel-digital-human-production

调用方式：

```text

用 $rachel-digital-human-production 做这条视频，先只做 15 秒样片。

```

它固定了：

- 固定目录结构。

- 先检查文案、人像和声音样本。

- MiniMax 负责声音，HeyGen 负责画面。

- 永远先生成 15 秒样片。

- 样片没有明确确认，不生成完整版。

- 每一步记录 `voice_id`、`asset_id`、`video_id` 和状态。

- 失败不盲目重试，避免重复扣费。

- 最终 MP4 必须完整检查。

- 不把 API Key、授权 header、临时下载链接写进日志或状态文件。

## 六、小tips

数字人视频最容易踩坑的地方，是成片不自然。

常见问题包括：声音不像本人、中文口型跟不上、脸部轻微变形、嘴角和下巴运动奇怪、眨眼和肩部动作不自然、构图不适合短视频平台。

所以我把“15 秒样片”写成强制步骤。先用 15 秒确认声音、口型、画面和构图。确认没问题，再跑完整视频。

相关链接：

- GitHub 仓库：https://github.com/Jingyi-Wu-Richael/rachel-digital-human-production

- MiniMax Voice Clone 官方文档：https://platform.minimax.io/docs/guides/speech-voice-clone

- HeyGen Image to Video 官方文档：https://developers.heygen.com/image-to-video

- HeyGen Assets 官方文档：https://developers.heygen.com/assets

## 溯源

