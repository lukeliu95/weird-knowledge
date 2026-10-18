---
title: "OpenAI 企业用 AI 的七条经验"
author: "meng shao (@shao__meng)"
url: https://x.com/shao__meng/status/1919285184102277546
source: X
published: 2025-05-05 06:57 UTC
saved: 2026-10-18
why: "X 点赞（批量导入）"
related_principles: []
status: 已整理
kind: 观点
topic: AI 产品与创业
roots: [openai-2025-ai-in-the-enterprise, test-driven-development, lean-startup, user-innovation, absorptive-capacity, autor-2003-skill-content-technological-change]
---

## 原文

OpenAI 最新发布 AI in the Enterprise 报告，为企业采用AI提供指导，总结了七个关键经验教训，并通过案例展示了AI在企业中的应用

核心内容
强调 AI 在企业中的三大价值：
1. 提升员工绩效：帮助员工更快地产出高质量成果
2. 自动化常规操作：解放重复性任务，让员工专注高价值工作
3. 增强产品功能：通过更个性化的客户体验提升产品竞争力
OpenAI 倡导以实验性、迭代的方式部署 AI，通过持续反馈和改进实现价值最大化。

七个经验教训
1. 从评估开始 
• 通过系统性评估（evals）测试AI模型在特定用例中的表现，确保质量与安全性。  
• 案例：摩根斯坦利通过评估优化金融顾问效率，98%的顾问每天使用 AI，文档访问率从20%提升至80%。

2. 将 AI 嵌入产品
• 用 AI 提升客户体验，增加交互的个性化与相关性。  
• 案例：Indeed 利用 GPT-40 mini 优化职位匹配，职位申请量增加20%，招聘成功率提升13%。

3. 尽早开始并持续投资
• 早期采用 AI 可通过迭代实现价值  compounding。  
• 案例：Klarna 的 AI 客服助理处理2/3的客户咨询，节省了数百万美元，同时90%的员工日常使用 AI。

4. 定制与微调模型
• 针对企业特定需求微调模型，提升准确性与效率。  
• 案例：Lowe’s 微调 AI 模型优化电商搜索，产品标签准确率提升20%，错误检测率提升60%。

5. 让专家使用 AI
• 将 AI 交给最了解业务流程的员工，激发创新解决方案
• 案例：BBVA 员工创建了2900多个定制 GPT，显著缩短项目周期，覆盖信贷、法律、客服等多个领域。

6. 解放开发者  
• 通过 AI 平台加速开发，减少瓶颈。  
• 案例：Mercado Libre 的 Verdi 平台帮助17000名开发者快速构建 AI 应用，提升库存管理、欺诈检测等效率。

7. 设定大胆的自动化目标  
• 利用 AI 自动化繁琐工作，释放员工潜能。  
• 案例：OpenAI 内部自动化平台处理数十万任务，提升客服效率并扩展至其他部门。

其他要点
• 安全与隐私：OpenAI 承诺企业数据不用于模型训练，提供加密、合规性认证和灵活的访问控制。
• 产品亮点：
  ▪︎Operator：一种代理工具，可自动化复杂工作流程，如软件测试和系统更新。
  ▪︎ChatGPT Enterprise 和 API 平台支持企业定制化 AI 解决方案。
• 结论：企业应以开放、实验的心态部署 AI，聚焦高回报、低投入的用例，通过迭代学习扩展应用。

> 媒体：
> - https://pbs.twimg.com/media/GqKrsG3aEAExM0O.jpg

## 溯源

- 核心主张：企业用 AI 要靠实验和迭代：先定评估，再嵌进产品，尽早投入让收益复利，按需微调，把工具交给最懂业务的员工，给开发者铺平台，定大胆的自动化目标。
- 源知识：
  - [OpenAI《企业中的 AI：七家前沿公司的经验》](../roots/openai-2025-ai-in-the-enterprise.md) · 关系：直接源自 · 强弱：强。推文就是 OpenAI 报告《AI in the Enterprise: Lessons from seven frontier companies》的摘要，三类价值和七条经验与原报告目录一致。
  - [测试驱动开发](../roots/test-driven-development.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“从评估开始”：先定好怎么衡量好坏再上线，和测试驱动开发“先写测试再写代码”同一个思路；报告没提 TDD。
  - [精益创业](../roots/lean-startup.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。报告说要用“实验心态、迭代部署、持续反馈”，和精益创业的“构建—衡量—学习”循环同一个思路；报告没提精益创业。
  - [用户创新](../roots/user-innovation.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。报告原话是员工最贴近流程和问题，往往最适合找到 AI 解法；BBVA 员工 5 个月自建 2900 多个 GPT，就是冯·希佩尔说的“用户自己创新”。
  - [吸收能力](../roots/absorptive-capacity.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。报告说越早开始、收益越会复利，Klarna 九成员工日常用 AI 后推进更快，和“组织已有的相关知识决定它能吸收多少新技术”的吸收能力理论很像。
  - [近期技术变革的技能内涵（例行任务替代假说）](../roots/autor-2003-skill-content-technological-change.md) · 关系：相近 · 强弱：弱（待 Luke 确认）。“自动化例行操作，让人去做更有价值的事”，就是 Autor 等人说的“计算机替代例行任务、补充非例行任务”。
- 本质：这条新知识本质上是精益迭代（构建—衡量—学习）和用户创新在企业导入 AI 场景下的应用。
- 整理于：2026-10-18（第 2 轮）
