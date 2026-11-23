---
layout: default
title: "Horizon Summary: 2026-11-23 (ZH)"
date: 2026-11-23
lang: zh
---

> 从 11 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [OpenAI 文章讨论困惑度与模型智能](#item-tech-news-1) ⭐️ 7.0/10

**科技博客**
1. [不确定时，不妨乱撞一通](#item-tech-blog-1) ⭐️ 6.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenAI 文章讨论困惑度与模型智能](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 7.0/10

OpenAI 发布文章，讨论把困惑度（perplexity）作为语言模型智能的衡量指标，并在 Hacker News 上引发围绕交叉熵损失、评测基准简洁性和模型进展的技术讨论。由于原文正文未提供，文章中的具体图表、评测设置和结论无法核实；评论者 hazrmard 还指出原文没有定义困惑度，并补充其最坏情况等于词表大小、最好情况为 1。

hackernews · acossta · 11月22日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=50601525)

**「背景」** 困惑度通常被理解为模型预测下一 token 时的“意外程度”：每一步都完全命中时值为 1，接近随机猜测时则接近词表大小。OpenAI 首席科学家 Jakub Pachocki 的文章以此为线索讨论模型智能，并把 2026 年 OpenAI 模型损失曲线出现的陡峭加速作为观察起点。OpenAI 一名员工在 Hacker News 讨论中补充，困惑度与模型质量的相关性“不是 1，但也不是 0”。

**「社区讨论」** 评论者 jrflo 称交叉熵损失与模型能力之间的趋势清晰得令人意外，并认为一个简单基准比日益复杂的评测更有价值；d\_burfoot 则把预测/压缩率与智能提取世界模型的能力联系起来。另有评论称微软 MAI 模型被加入同一图表并给出对数困惑度数值，但这只是评论者引述的说法，未在原始材料中核实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/perplexity-and-intelligence/">Perplexity and Intelligence | OpenAI</a></li>
<li><a href="https://news.ycombinator.com/item?id=50601525">Perplexity and Intelligence | Hacker News</a></li>

</ul>
</details>

**标签**: `#perplexity`, `#LLM evaluation`, `#cross-entropy`, `#AI scaling`, `#OpenAI`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [不确定时，不妨乱撞一通](https://seangoedecke.com/when-in-doubt-flail-about/) ⭐️ 6.0/10

rss · Sean Goedecke · 11月23日 00:00

**「背景」** 在缺乏明确指引、不知什么真正有用的模糊情境中，作者主张与其谨慎等待理解，不如“乱撞”（flail about）：快速尝试多种行动并紧贴反馈——尽管不得法的乱撞会严重损害你在科技公司的声誉。

**「方案」** 作者提出三条准则：大量尝试、密切关注反馈、无情砍掉没有正反馈的方案。多试既是为了直接接触现实，也因为多数想法本就糟糕——试十个才可能有一个可行，且手上方案多就不会过度投入、能果断放手。他把乱撞分为三类：产品上，在尚未找到产品市场契合的功能边缘试错，他在 GitHub Models（现已退役）上的许多集成都没成，只有“用 GitHub Actions token 运行 AI 推理”意外留存并成为 Continuous AI 的种子；工程上，面对过于庞大、纠缠或已高度优化而不知从何下手的系统，与其通读全局，不如做一批试探性改动，无改善就立即放弃，有改善再深挖原因；组织上，对团队互不沟通、某团队不满而总监也说不清缘由这类非技术问题，可以自动化手工工作、主动接手任务、提出长期方案，多数不会有用，但至少显示你在努力。他特别提醒组织场景最需敏感于反馈：及时放弃失败方案能积累信任，无视反馈硬推则会把愤怒引向自己。作者也说，叫“乱撞”是因为内心感受像反复失败出丑，但这种不适是需要跨过的心理障碍，而非危险信号。

**「启示」** 作者的结论是：只要紧盯反馈并愿意立刻放弃无效方案，乱撞式快速实验就是处理棘手工程与组织问题的高效路径；那种像在瞎撞的难受感，本身不该成为停手的理由。

**标签**: `#software engineering`, `#uncertainty`, `#experimentation`, `#feedback loops`, `#organizational dynamics`

---