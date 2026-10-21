---
title: "开源工具让普通人也能微调 27B 模型"
author: "实践哥 Li (@MinLiBuilds)"
url: https://x.com/MinLiBuilds/status/2092484626384380017
source: X
published: 2026-08-26 05:29 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: 模型与本地部署
roots: [hu-2021-lora, dettmers-2023-qlora, chen-2016-sublinear-memory-cost, transfer-learning, whole-product, commons-based-peer-production]
---

## 原文

真得感谢 Unsloth、SGLang 这种开源佬。

模型厂把权重放出来，只是第一步。

后面这帮人孜孜不倦地做适配、写 Kernel、降显存、提速度、补工具、写教程，甚至连免费算力入口都给你铺好。

没有这些人，很多所谓“开源模型”，其实就只是 Hugging Face 上的一堆权重。

现在已经夸张到什么程度？

Qwen3.8-27B 这种 27B Dense，普通人都能自己微调了。

甚至显卡都不用买。

Unsloth 把 Notebook、教程、训练流程都做好，直接用 Kaggle 免费 GPU 就能开炼。

🔥很多人可能会问：

27B Dense 不是很吃显存吗？为什么 24GB 都能训？

因为这里不是 Full Fine-Tuning。

真把 27B 参数全部训练一遍，光 BF16 权重就 50GB+，再算 Gradient、Optimizer、Activation，几百 GB 显存很正常。

现在主要玩的是 LoRA / QLoRA。

LoRA：27B 底模冻住，只训练旁边一小部分低秩参数。

QLoRA：更狠，底模先压成 4-bit，再训练 LoRA。

🔥再加上 Unsloth 继续狠狠干 Attention、Activation、Gradient Checkpointing 这些训练显存，最后把 27B 微调门槛狠狠干到一张消费卡，甚至免费云 GPU。

🔥以前普通人玩开源：

下载权重 → 跑起来 → 聊两句。

现在已经可以：

做数据 → 微调 → Eval → 部署 → 做一个真正属于自己的模型。

未来每个企业都会有自己的模型。

当然不是每家公司都从头预训练一个 GPT。

而是拿 Qwen 这种强开源底模，把自己的 数据、Know-how、业务规则、工作流 炼进去。

基础模型已经会中文、数学、代码了。

🔥关注我们公司这件事，到底应该怎么干。

大厂负责造模型。

开源社区负责把模型真正送到每个人手里。

现在连 GPU 都没有的人，都可以开始炼一个 27B 模型。

这才是开源真正牛逼的地方。

然后再看看这篇文章，讲的是开源 Agent 所需要的 OpenContext，卷不了大模型，我们就卷微调，卷 Agent。感谢这批开源佬。

> 媒体：
> - https://pbs.twimg.com/media/HQn_oR0aIAAISyi.jpg

## 溯源

- 核心主张：开源权重只是第一步，社区做的适配、内核、省显存（LoRA、QLoRA、梯度检查点）、教程和免费算力，才让普通人用一张消费卡甚至免费 GPU 就能微调 27B 模型；企业以后不必从头预训练，而是在开源底模上微调出自己的模型。
- 源知识：
  - [LoRA：大语言模型的低秩适配](../roots/hu-2021-lora.md) · 关系：直接源自 · 强弱：强。推文点名 LoRA：冻住底模，只训练旁边一小部分低秩参数，和 Hu 等 2021 的做法一字不差。
  - [QLoRA：在量化后的大模型上高效微调](../roots/dettmers-2023-qlora.md) · 关系：直接源自 · 强弱：强。推文点名 QLoRA：底模先压成 4-bit 再训练 LoRA；原论文就是靠这个让 65B 模型在一张 48GB 显卡上微调。
  - [以亚线性显存训练深度网络（梯度检查点）](../roots/chen-2016-sublinear-memory-cost.md) · 关系：直接源自 · 强弱：强。推文点名梯度检查点（Gradient Checkpointing）这个省显存手段，把它系统地用到深度网络训练上的是 Chen 等 2016。
  - [迁移学习（机器学习）](../roots/transfer-learning.md) · 关系：换了说法 · 强弱：强。“拿强开源底模，把自己的数据、Know-how 炼进去，而不是从头预训练”，就是“预训练加微调”的迁移学习，LoRA 论文开头就把这个范式写明了。
  - [整体产品](../roots/whole-product.md) · 关系：相近 · 强弱：弱（模型复核通过）。“没有这些人，开源模型就只是一堆权重”：核心产品（权重）要加上让人真正用起来的配套（内核、教程、算力）才算完整，和整体产品的说法很像；作者没提这个理论，是推断。
  - [基于共享资源的同侪生产](../roots/commons-based-peer-production.md) · 关系：相近 · 强弱：弱（模型复核通过）。推文感谢的 Unsloth、SGLang 等是社区自愿协作做出的开放成果，属于同侪生产；是推断。
- 本质：这条新知识本质上是“预训练加微调”的迁移学习，借低秩适配、量化、梯度检查点这些省显存技术，从大厂下沉到个人的应用；而“开源模型要靠社区补齐配套才真正可用”，是整体产品理论在开源模型生态里的应用。
- 整理于：2026-10-18（第 2 轮）
