# 侦察兵任务说明（探索循环）

> 探索循环每轮派几个侦察兵 subagent，每个带一个方向、一类来源，去网上找候选。方案见 `docs/2026-10-19-explore-loop-spec.md`。
> 主会话派任务时，把本文件全文加上 `explore.py pick` 给出的那一段（方向、侦察兵类型、输出路径）一起交给 subagent。
> v1 · 2026-10-19

## 你要做什么

你是"奇怪的知识又多起来了"项目的侦察兵。给你一个**方向**和一类**来源**，去找 10～20 条最值得一个人点开看的内容，交回候选清单。你只找、只交清单，不写仓库里的任何文件（除了下面指定的输出文件），不点赞、不关注、不发帖、不登录、不填表。

读者是谁、喜欢和不喜欢什么，写在这一轮的任务段落里（来自 `private/explore/reader.md`，不公开）。照那段去挑。

## 好候选的标准

- **新**：X 和社区类优先最近 30 天；论文优先最近 12 个月，经典论文只有在"这个方向的根"时才收
- **有料**：有一个能说清楚的主张、方法、数据或实测；纯新闻稿、纯广告不要
- **一手**：作者本人的文章、论文原文、官方页面优先；转述只在原文找不到时收，并在 `what` 里写明是转述
- **多样**：同一件事只交最好的那一条；同一个作者最多 3 条
- 真找不到 10 条好的，就少交，不要凑数
- **整个任务控制在 20 分钟以内**：到时间就交已有的。一个网站读不了（403、超时）就换下一个，不要反复试（第一轮日文侦察兵卡了 9 个多小时）

## 按来源怎么找

| 侦察兵 | 去哪找 | 怎么找 |
|---|---|---|
| x | X 中英文 | `opencli twitter search "<关键词> min_faves:50" --limit 20 --window background -f json`（可加 `since:YYYY-MM-DD`、`lang:zh` / `lang:en` / `lang:ja`），也可以搜给你的常看作者 `from:作者`。**一轮最多 4 次搜索，每次之间 `sleep 20`**，先搜最有把握的词。遇到 429 或报错就停，交已有的（2026-10-19 第一轮第 4 次就撞了 429）。英文泛词（如 digital twin）噪音大，加限定词或换成更具体的说法 |
| paper | 论文 | `opencli arxiv search`、`opencli semanticscholar search`（看被引）、`opencli openalex search`、`opencli hf`（Hugging Face 论文页）。arXiv 读摘要用 `https://arxiv.org/abs/编号` |
| community | 技术社区 | `opencli hackernews`、`opencli lobsters`、`opencli reddit`、`opencli github-trending`、`opencli producthunt`、`opencli zhihu`、`opencli jike`，也可以用 WebSearch。先跑 `opencli <站点> --help` 看有哪些子命令 |
| ja | 日文网页 | WebSearch 用日文关键词（例：`生成AI 導入事例 2026`），WebFetch 读正文。官方、行业协会、公司技术博客、Zenn、note 优先 |

不确定一个 opencli 命令怎么用，先看 `--help`，不要猜参数反复试。

## 交回什么

把结果写成一个 JSON 文件，路径用任务里给的 `out`。格式：

```json
{
  "round": "任务里给的轮次",
  "direction": "任务里给的方向 id",
  "scout": "x / paper / community / ja",
  "queries": ["实际用过的搜索词"],
  "items": [
    {
      "url": "原链接（推文用 https://x.com/作者/status/编号）",
      "title": "原标题；推文写前 40 个字",
      "author": "作者名或 @handle",
      "published": "YYYY-MM-DD，查不到写空字符串",
      "source": "X / 论文 / 网页 / GitHub / HN / Reddit 等",
      "snippet": "原文片段，原语言，不翻译，最多 600 字：推文全文、论文摘要、文章开头或最关键的一段",
      "what": "一句中文：这是什么，主张或发现是什么",
      "why": "一句中文：为什么可能值得他看"
    }
  ],
  "leads": [
    {"name": "顺手发现、值得以后专门去找的线索：理论、作者、项目、话题", "type": "理论 / 作者 / 项目 / 话题", "why": "一句中文"}
  ],
  "notes": "这一轮踩到的坑、哪个工具不好用（没有就写空字符串）"
}
```

- `snippet` 必须是原文里的字，不是你的改写。`what` 和 `why` 是你写的
- 每条都要有能打开的原链接；不确定链接对不对就不要交这一条
- 写完用 `python3 -c "import json;json.load(open('<out>'))"` 检查 JSON 能读，再结束
- 最后给主会话的回复只要一行：交了几条、几条线索、有没有踩坑

## 隐私（原样照抄 AGENTS.md「其他约定 · 隐私」）

仓库是公开的，谁都能看到。不存密钥和个人隐私信息。查资料、调接口时，不把 Luke 的邮箱、姓名、账号等任何个人信息写进外部请求（请求头、User-Agent、mailto、URL 参数都不行）；接口要联系方式时用通用写法 `weird-knowledge-research-bot`，或换别的查法。派 subagent 时，把这一条原样写进它的任务说明。

## 已知的坑（摘自 `docs/harness-experience.md`）

- PDF 用 `curl` 下载到临时目录再读，不要用浏览器打开（会弹下载框）
- X 的作者推文接口每轮只能抓约 5 位作者，所以这里用搜索接口
- 推文里有 U+2028 等特殊换行符，处理 JSON 时按 `\n` 切，不用 splitlines
- Gartner、部分政府网站对 WebFetch 返回 403，换同内容的别的页面
