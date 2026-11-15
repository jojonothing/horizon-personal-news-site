---
layout: default
title: "Horizon Summary: 2026-11-15 (ZH)"
date: 2026-11-15
lang: zh
---

> 从 30 条内容中筛选出 6 条重要资讯。

---

**科技新闻**
1. [Lovable 应用被曝因 RLS 不足泄露护照信息与逾 20 万条私信](#item-tech-news-1) ⭐️ 8.0/10
2. [PyPI 新版项目页上线，强化安全与来源信号](#item-tech-news-2) ⭐️ 7.0/10
3. [纯 JAX 实现 DeepSeek V3 推理，约 200 行代码](#item-tech-news-3) ⭐️ 7.0/10
4. [EFF 批评科技公司再次试图重塑隐私概念](#item-tech-news-4) ⭐️ 7.0/10
5. [Project Zero 公布分阶段漏洞披露政策：90→60→30 天](#item-tech-news-5) ⭐️ 7.0/10
6. [4.5M 参数全开源 TTS「tiny-voca」：CPU 上约 70 倍实时，可在浏览器运行](#item-tech-news-6) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Lovable 应用被曝因 RLS 不足泄露护照信息与逾 20 万条私信](https://www.crissyfield.de/research/lovable-en/) ⭐️ 8.0/10

一篇安全研究披露，部分由 Lovable 生成的应用因 Row-Level Security（RLS，行级安全）配置不足，暴露了护照信息和超过 20 万条私人消息。Lovable 安全负责人回应称，这些应用的根因确实是 RLS 不足，并称平台会在发布前自动扫描每个应用、提供免费的深度 SAST 扫描，以及可由用户触发的“修复”和自动修复功能。现有材料没有给出受影响应用的具体数量或数据是否已被删除，相关暴露范围仍主要来自研究方披露和厂商回应，尚未独立核实。

hackernews · armcat · 11月14日 17:43 · [社区讨论](https://news.ycombinator.com/item?id=50499017)

**「背景：RLS 与 Supabase 的默认变更」** 行级安全（Row-Level Security, RLS）是 PostgreSQL 的访问控制机制，它通过策略决定某个客户端能读写哪些数据行；在 Supabase 中，public schema 里的表会经自动生成的 Data API 暴露，若未启用 RLS，持有匿名密钥的客户端就可能直接读取数据（tool-1-1）。据一篇介绍该变更的文章，Supabase 已于 2026 年 10 月 30 日调整默认行为：现有项目中 public schema 新建的表不再自动暴露给 Data API（tool-1-2）。社区讨论中有评论者称，部分既有项目的旧默认设置可能仍然生效，但这一说法在现有材料中未获证实。

**「影响」** 对使用 Lovable 构建并连接 Supabase 的开发者，直接后果是需要逐表检查 RLS 是否启用、策略是否覆盖匿名和登录角色，而不能把发布前扫描当作历史应用已安全的证明。平台提供的“修复”和自动修复可降低后续风险，但既有项目是否已重新扫描或修复，仍需开发者自行确认。

**「社区讨论」** 评论中的一项争议是责任归属：有评论者认为 Supabase 多年来的宽松默认设置是重要原因，并提到相关默认值虽被称已于 10 月 30 日修复，但既有项目是否仍沿用旧默认值存在不同说法。另一类观点认为，AI 生成应用并未创造全新的数据库安全问题，只是让这类应用数量更多、攻击门槛更低，普通用户也更难判断风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://supabase.com/docs/guides/database/postgres/row-level-security">Row Level Security - Supabase Docs</a></li>
<li><a href="https://dev.to/dave_thomas_18311ddb9c409/supabases-oct-30-change-what-breaks-what-doesnt-and-the-quick-fix-to-avoid-bg4">Supabase&#x27;s Oct 30 change: what breaks, what doesn&#x27;t, and the ...</a></li>

</ul>
</details>

**标签**: `#security`, `#AI app builders`, `#Supabase`, `#row-level security`, `#data exposure`

---

<a id="item-tech-news-2"></a>
### [PyPI 新版项目页上线，强化安全与来源信号](https://blog.pypi.org/posts/2026-11-06-ui-updates-complete/) ⭐️ 7.0/10

PyPI 重新设计的项目页面已经上线，官方表示新页面会更清晰地展示包的安全与来源（provenance）信号，并让可信发布相关信息更容易被看到。此次改动面向浏览 PyPI 项目页的 Python 开发者。现有信息没有说明具体界面元素、覆盖范围或旧版页面何时停用。

hackernews · rbanffy · 11月14日 15:40 · [社区讨论](https://news.ycombinator.com/item?id=50497892)

**「背景：Trusted Publishing 与来源信息」** PyPI 的 Trusted Publishing 允许项目把某个 CI 服务上的特定配置设为受信任的 OIDC 发布者，从而无需手动配置 API token 或用户名密码即可上传软件包。GitHub 的 pypi-publish Action 等工具已支持这一机制。新版项目页所强调的来源（provenance）信号，正是建立在按这种方式发布、因而可被追溯的包之上。

**「影响」** 依赖第三方包的开发者在选包或升级时，可以把项目页上的 provenance 状态纳入来源检查；评论举例称 datasette 显示 provenance，而 dlt 未显示。该信号不能替代恶意包检测，评论者指出它主要暴露的是原本良性、后来被入侵的项目。

**「社区讨论」** 有评论者担心，这套以可信发布和来源验证为中心的信任模型过度依赖大型云服务与 CI 平台，可能造成锁定；另一名评论者则希望可信发布尽快支持可复用工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.pypi.org/trusted-publishers/">Getting Started - PyPI User Documentation</a></li>
<li><a href="https://github.com/marketplace/actions/pypi-publish">pypi - publish · Actions · GitHub Marketplace · GitHub</a></li>

</ul>
</details>

**标签**: `#PyPI`, `#software supply chain security`, `#package provenance`, `#Python packaging`, `#trusted publishing`

---

<a id="item-tech-news-3"></a>
### [纯 JAX 实现 DeepSeek V3 推理，约 200 行代码](https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax) ⭐️ 7.0/10

开发者 VaibhaavTiwari 在 Hacker News 发布了一个用纯 JAX 实现 DeepSeek V3 推理的 Show HN 项目，代码量约 200 行。项目重点是从零复现模型推理流程，面向想理解模型内部实现、并尝试 JAX 技术栈的开发者。当前公开信息仅限于项目页面和社区讨论，尚无独立基准或完整模型运行结果的验证。

hackernews · VaibhaavTiwari · 11月14日 15:04 · [社区讨论](https://news.ycombinator.com/item?id=50497589)

**「背景」** JAX 是面向加速器的数值计算与自动微分库，通常通过 XLA 编译计算图。用约 200 行代码从头实现 DeepSeek V3 的推理，重点在于展示模型前向计算所需的最小结构，属于教学和动手实验性质，并非完整生产推理框架。

**「影响」** 对使用 AMD ROCm 的开发者而言，一位评论者称该项目是其 RX 7600 XT 16GB 显卡上第一个端到端跑通的项目，但需要设置 HSA\_OVERRIDE\_GFX\_VERSION=11.0.0 等环境变量。这属于用户经验，尚不是项目方或独立测试确认的兼容性承诺。

**「社区讨论」** 评论整体肯定从零重建模型的教学价值，有人表示会照着复现；也有初学者询问系统学习推理实现所需的路线图。

**标签**: `#JAX`, `#DeepSeek V3`, `#inference`, `#model implementation`, `#ROCm`

---

<a id="item-tech-news-4"></a>
### [EFF 批评科技公司再次试图重塑隐私概念](https://www.eff.org/deeplinks/2026/11/tech-companies-are-trying-shift-entire-concept-privacy-again) ⭐️ 7.0/10

电子前哨基金会（EFF）于 2026 年 11 月 14 日发表评论文章，主张科技公司正在再次尝试改变“隐私”这一概念本身的含义。该文属于倡导性分析，而非产品发布或技术突破，因此其中不涉及具体版本号、可用性或兼容性信息。本条目的来源未提供文章正文，所以文中点名了哪些公司、提出了哪些具体论点，均无法在此核实。

hackernews · gslin · 11月14日 12:45 · [社区讨论](https://news.ycombinator.com/item?id=50496602)

**「背景」** EFF 的这篇文章把当前争议概括为隐私焦点从“个人是否同意收集数据”转向“旁人是否被动被记录”的旁观者问题。文章举出的产品包括 Meta 和 Google 的智能眼镜、Apple 的 Audio Intelligence，以及 Amazon 的 Bee 设备。

**「社区讨论」** 在 Hacker News 的讨论中，评论者 toddmorey 描述了自己的亲身处境：如今几乎每场职业会议，包括直属经理与同事之间的一对一谈话，都会被可见或不可见的 AI 参会者录音并上传；他认为自己实际上无法选择退出，否则就可能丢掉工作。另一位评论者 abecedarius 则表示，做好实时转写的设备对失聪和重度听障者可能具有变革意义，并指出本地模型本可以不保存或导出任何内容，但系统一旦存在，就“只差一个 if 语句”便会开始留存数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aiweekly.my/items/46520/tech-companies-are-trying-to-shift-the-concept-of-privacy-again">Tech Companies Are Trying to Shift the Concept of Privacy (Again)</a></li>

</ul>
</details>

**标签**: `#privacy`, `#surveillance`, `#AI policy`, `#digital rights`, `#tech industry`

---

<a id="item-tech-news-5"></a>
### [Project Zero 公布分阶段漏洞披露政策：90→60→30 天](https://projectzero.google/2026/11/disclosure-policy.html) ⭐️ 7.0/10

Google Project Zero 公布的分阶段漏洞披露政策显示，自公告发布起采用“Full 90”，即向厂商报告漏洞 90 天后公开；2027 年 2 月 2 日改为“Full 60”，2028 年 1 月 3 日再改为“Full 30”。公告把时间表明确到具体日期，但 60 天和 30 天仍是未来计划，尚未生效。现有材料未说明是否按漏洞严重程度、厂商响应或补丁状态设置例外。

hackernews · hacb · 11月14日 11:13 · [社区讨论](https://news.ycombinator.com/item?id=50496051)

**「背景」** Project Zero 此前执行“90+30”披露政策：厂商在收到漏洞报告后有 90 天时间提供补丁，补丁发布后用户还有 30 天采纳期；若厂商未在 90 天内修复，Project Zero 会公开漏洞细节。此次调整把完整披露时点改为报告后 90 天，取消了原有的额外 30 天缓冲，并计划之后进一步缩短到 60 天和 30 天。

**「修复窗口收紧」** 对依赖 Project Zero 披露窗口安排补丁响应的运维和安全团队而言，修复周期需要随之压缩：社区评论引述的政策文本显示，披露期先从 90 天缩短到 60 天（2027 年 2 月 2 日），再缩短到 30 天（2028 年 1 月 3 日），因此按 90 天窗口设计的评估、测试和上线排期将不再适用。

**「社区讨论」** 评论者对缩短披露窗口的实际可行性意见不一：有人称 Ubuntu 这类大型项目需要远多于 30 天的时间，也有人主张应尽快公开，否则厂商缺乏修复动力。另有评论提出，发现漏洞的公司应向厂商或开源项目提供复现和修补所需的同等产品访问权限，以免披露政策变成推动采用其自身工具的手段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://googleprojectzero.blogspot.com/p/vulnerability-disclosure-policy.html">Project Zero : Vulnerability Disclosure Policy</a></li>
<li><a href="https://www.escoffer.com/2025/08/16/google-tightens-security-timelines-through-faster-alerts/">Google Tightens Security Timelines Through Faster Alerts</a></li>
<li><a href="https://vulners.com/threatpost/THREATPOST:939B0A82AB99C20FA2E854236CD42DBB">Google Project Zero Cuts Bug Disclosure Timeline to a 30 - Day .</a></li>

</ul>
</details>

**标签**: `#vulnerability disclosure`, `#cybersecurity policy`, `#Google Project Zero`, `#security engineering`, `#vendor patching`

---

<a id="item-tech-news-6"></a>
### [4.5M 参数全开源 TTS「tiny-voca」：CPU 上约 70 倍实时，可在浏览器运行](https://www.reddit.com/r/LocalLLaMA/comments/1xw7zrg/tinyvoca_a_fully_open_45mparameter_tts_code/) ⭐️ 7.0/10

作者 n4ze3m（Reddit 用户 /u/nato\_nob）发布英文语音合成模型 tiny-voca，共 4,537,291 个参数、体积 18 MB（已包含波形生成部分），提供一女一男两个音色，采样率 24 kHz。作者称其在 4 个 CPU 线程上约为实时的 70 倍，可用 PyTorch、ONNX 运行，也能直接在浏览器中推理（演示页称音频不会上传服务器），并在单张 RTX 4090 上从零训练 7.7 小时。项目公开了代码、权重、数据集和训练配方，使用自研音素化器 dizione，且不依赖神经网络声码器，而由小型源-滤波合成器生成波形，这也是其速度来源。限制同样明确：只支持英语和这两个固定音色、不支持声音克隆；训练音频由 Qwen3-TTS 合成，音质上限受此约束；作者也承认声音略偏机械、外来人名和非常规拼写常读错，且 70 倍实时等性能数字为作者自述，尚无独立测量。

reddit · r/LocalLLaMA · /u/nato\_nob · 11月14日 17:26

**「背景」** tiny-voca 的“无神经声码器”设计，是指它跳过常见 TTS 流程中把声学特征转换为波形的神经声码器，改用小型源-滤波合成器直接产生声音，这也是其能在 CPU 上快速推理的原因之一。它的训练音频由 Qwen3-TTS 合成；据 Qwen 团队的项目页，Qwen3-TTS 是支持语音设计、声音克隆和流式生成的系列模型。

**「影响」** 对需要在无 GPU 环境或浏览器端本地合成语音的开发者，18 MB 的完整模型加上 ONNX 导出，使其可直接嵌入网页或端侧应用，无需服务端推理。但英语单语、固定两个音色、无克隆能力，且音质被合成训练数据封顶，因此它不适合直接替代多语种或高质量商用 TTS。作者请使用者重点测试数字、日期、人名和长句，并回报出错的文本与音色；实际采用前应对这些场景先行验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/QwenLM/Qwen3-TTS">GitHub - QwenLM/Qwen3-TTS: Qwen3-TTS is an open-source series ...</a></li>

</ul>
</details>

**标签**: `#text-to-speech`, `#open-source-models`, `#efficient-inference`, `#onnx`, `#browser-ml`

---