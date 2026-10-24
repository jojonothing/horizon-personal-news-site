---
layout: default
title: "Horizon Summary: 2026-10-24 (ZH)"
date: 2026-10-24
lang: zh
---

> 从 16 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [博客声称攻破 iPhone，社区追问 Lockdown Mode 效果](#item-tech-news-1) ⭐️ 8.0/10
2. [Kimi K3.1 Pro 登陆 API：Highspeed 提速 2–3 倍、价格翻倍](#item-tech-news-2) ⭐️ 7.0/10
3. [Block 展示 Dessa：可在本地运行的全双工语音模型](#item-tech-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [博客声称攻破 iPhone，社区追问 Lockdown Mode 效果](https://blog.calif.io/p/iphone) ⭐️ 8.0/10

博客文章《Today, we hacked what we&\#x27;d set out to hack: the iPhone》声称团队已按计划攻破 iPhone，并给出漏洞利用演示；这是单方面、带宣传色彩的声明，尚无独立验证或厂商确认。评论围绕演示本身、前沿实验室对红队模型的访问限制以及 Lockdown Mode 能否挡住这类攻击展开，而不是已确认的攻击链细节。由于没有源正文，受影响 iOS 版本、漏洞编号、利用条件和披露时间均无法核实。

hackernews · pavel\_lishin · 10月23日 16:21 · [社区讨论](https://news.ycombinator.com/item?id=50211474)

**「背景」** 这篇博客对应的是作者在巴黎 Hexacon 安全会议上现场展示的一系列攻击演示；博文只给出演示线索（例如“Signal 1-click”），并称完整内容“会在适当时候发布”，因此目前公开的只是演示层面的说法，尚无漏洞细节或可复现的攻击链。评论中提到的锁定模式（Lockdown Mode）是苹果面向高风险用户提供的可选加固开关，讨论的焦点正是它能否实际削弱此类攻击。

**「影响」** 在缺少受影响版本、利用条件和 Lockdown Mode 测试结果的情况下，iPhone 用户和安全团队目前无法判断实际暴露面，也无法据此决定是否调整锁定模式或更新策略；该演示应被视为待复现的研究主张，而非已确认的在野攻击。

**「社区讨论」** 评论者称演示“非常酷”，但直接追问 Lockdown Mode 在真实攻击面前是否有效；有评论者还抱怨前沿实验室只向“圈内”成员或公司开放红队模型，认为“可信网络访问”计划更像竞争壁垒而非安全保障。另有评论者感叹 iOS 生态锁定和越狱检测会让设备失去 iCloud、iMessage 等功能，并怀念早期可 root 的设备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.calif.io/p/iphone">Today , we hacked what we &#x27; d set out to hack : the iPhone .</a></li>

</ul>
</details>

**标签**: `#iPhone security`, `#vulnerability research`, `#AI red teaming`, `#mobile exploitation`, `#Lockdown Mode`

---

<a id="item-tech-news-2"></a>
### [Kimi K3.1 Pro 登陆 API：Highspeed 提速 2–3 倍、价格翻倍](https://www.kimi.ai/blog/kimi-k3-1-pro) ⭐️ 7.0/10

Moonshot AI 于 10 月 23 日通过 Kimi API 发布 Kimi K3.1 Pro，并同时提供速度提升 2–3 倍的 Highspeed 版本；Highspeed 的价格翻倍，但输入 token 缓存命中的价格保持不变。API 定价为每百万 token 输入 2 美元、输出 10 美元，与 GPT-6.1 Sol 相同，是 Claude Opus 5.5 的一半。模型暂未开放权重，Moonshot 承诺在 2026 年 11 月 4 日前发布完整权重；Moonshot 的自测显示，其性能大致与 Opus 5.5 和 GPT-6 Astra 持平；Artificial Analysis 给它的评分为 55 分，低于 Opus 5.5 的 58 分，高于 Claude Fable 5.1、GPT-6 Astra 和 Gemini 4 Argon 的 53 分。

hackernews · Jowsey · 10月23日 16:59 · [社区讨论](https://news.ycombinator.com/item?id=50212065)

**「背景」** Kimi K3.1 Pro 是 Moonshot Kimi 系列的点版本更新，此前已有 K3 作为上一代模型，并被评论者和第三方测试用作对照基线。此次新版先通过 Kimi API 提供，尚未开放权重；Moonshot 表示完整模型权重将在 2026 年 11 月 4 日前发布。

**「影响」** 需要更快响应的 API 用户可选用 Highspeed 版本，但其单价翻倍；需要自托管部署的团队则要等到 Moonshot 承诺的 2026 年 11 月 4 日权重发布之后。

**「社区讨论」** HN 评论中，有开发者报告，Kimi K3.1 Pro 在其数据分析基准上的得分从 7 月 Kimi K3 的 81% 升至 98%，但运行速度偏慢，且工具调用频繁；例如，有一道题发出了 73 次查询，而 GPT-6.1 Sol 为 18 次。另有人称，其 99 美元/月订阅在单个会话进行到 47 分钟时，触发了 5 小时配额限制；还有用户觉得它的回答比美国模型更直白、更好辩，并注意到它在推理内容中自称 Kimi，偶尔误认自己是 ChatGPT。

**标签**: `#LLM release`, `#Kimi K3.1 Pro`, `#AI benchmarks`, `#Moonshot AI`, `#model evaluation`

---

<a id="item-tech-news-3"></a>
### [Block 展示 Dessa：可在本地运行的全双工语音模型](https://block.xyz/dessa) ⭐️ 7.0/10

Block 展示了 Dessa，一款据称支持全双工对话的语音模型：人与模型可以同时说话，而不是严格轮流；页面称它能在 MacBook Pro M4 Max 或更高配置上本地推理，并且只靠一套 NVIDIA GB200 NVL72 完成训练。这些均为项目方的说法，提供的材料没有给出独立基准、模型许可或正式可用时间，标题中的“最真实”属于宣传性描述。

hackernews · dsr12 · 10月23日 19:09 · [社区讨论](https://news.ycombinator.com/item?id=50213925)

**「背景：什么是全双工语音模型」** 常见的语音对话系统把语音识别、语言模型和语音合成串成流水线，并按“你说完我再说”的轮次工作，因此难以处理插话、附和、笑声这类同时发生的交互。全双工（full-duplex）模型的目标是边听边说：在同一时刻既能接收输入又能生成语音，从而让回应延迟更低、互动更接近真人对话，但也更容易显得刻意或过度打断。Block 对 Dessa 的介绍正是放在这一方向上，并同时强调本地推理与训练效率。

**「影响」** 如果本地推理和低延迟能按页面所述复现，语音应用开发者可把连续对话放在端侧处理，减少云端往返；但在获得模型、许可信息和实测延迟前，不应据此安排部署。

**「社区讨论」** 部分评论者对“MacBook Pro M4 Max 本地运行、单套 GB200 NVL72 训练”表示印象深刻，认为若低延迟和表现力属实，这是独立 AI 的重要成果。另一些评论者则认为演示对话刻意、像“AI 女友”，并质疑模型被训练成频繁打断用户，以及“最真实”只是营销措辞。

**标签**: `#full-duplex speech`, `#speech AI`, `#local inference`, `#training efficiency`, `#Hacker News`

---