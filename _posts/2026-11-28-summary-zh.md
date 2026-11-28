---
layout: default
title: "Horizon Summary: 2026-11-28 (ZH)"
date: 2026-11-28
lang: zh
---

> 从 9 条内容中筛选出 6 条重要资讯。

---

**科技新闻**
1. [检查器缺陷可产生虚假验证证明](#item-tech-news-1) ⭐️ 8.0/10
2. [Google DeepCrossAttention 宣称质量相当且最高提速 3 倍](#item-tech-news-2) ⭐️ 7.0/10
3. [购物网站出现利用 WebRTC 的信用卡盗刷脚本](#item-tech-news-3) ⭐️ 7.0/10
4. [Convex 技能被指未经告知上传用户应用想法](#item-tech-news-4) ⭐️ 7.0/10
5. [多州总检察长起诉 SpaceX，要求叫停 Grok 生成儿童性虐待与未经同意图像](#item-tech-news-5) ⭐️ 7.0/10
6. [SemiAnalysis 解读 Trainium3 推理：宣称 TCO 优于 GB300](#item-tech-news-6) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [检查器缺陷可产生虚假验证证明](https://cr.yp.to/proofs/falseccp.html) ⭐️ 8.0/10

一篇技术分析文章讨论证明检查器的可靠性缺陷如何使错误命题获得“计算机已验证”的外观，提醒依赖形式化证明的数学与软件验证用户把检查器本身纳入信任评估。现有材料没有给出新的具体漏洞、受影响版本或已确认的误导案例。文章的重点是检查器的 soundness（可靠性）风险，而不是证明搜索或用户界面问题。

hackernews · \_tk\_ · 11月27日 15:26 · [社区讨论](https://news.ycombinator.com/item?id=50667989)

**「背景」** 计算机检查证明依赖证明助手或独立检查器逐条核验形式化证明，因此检查器自身的健全性（soundness）是整个信任链的前提。Daniel J. Bernstein 在 2026 年 11 月发布该页面时称，它汇总了多个重要证明检查程序中的 199 份健全性缺陷报告，这为讨论“检查通过是否等于证明为真”提供了具体背景。

**「影响」** 对依赖形式化验证的团队，实际动作是不要把单一检查器的“通过”当作最终保证：应确认是否存在独立实现的交叉验证，并保留人工审查来发现形式化目标本身的偏差。即使检查器可靠，若形式化陈述误解了需求，仍可能验证错误的目标。

**「社区讨论」** 评论者主要争论文章是否夸大了单个检查器的风险：twotwotwo 认为要误导数学家需多个检查器同时出错且非形式审查看不出问题，dwheeler 补充 Metamath 主数据库要求 5 个不同语言编写的独立验证器全部通过，gr\_norm 则认为已知 soundness 缺陷少到“能塞进一条推文”，对绝大多数软件足够。andai 还提到另一种失效模式：证明可能针对对需求的错误理解，即使检查器本身可靠也验证了错误目标。

<details><summary>参考链接</summary>
<ul>
<li>Daniel J. Bernstein on X: &quot;Posted new page &quot;False computer-checked ...</li>

</ul>
</details>

**标签**: `#formal verification`, `#proof assistants`, `#soundness bugs`, `#software reliability`

---

<a id="item-tech-news-2"></a>
### [Google DeepCrossAttention 宣称质量相当且最高提速 3 倍](https://research.google/blog/supercharging-transformer-residual-connections/) ⭐️ 7.0/10

Google Research 的一篇博客介绍 DeepCrossAttention，称其通过改进 Transformer 残差连接，在模型质量相当的情况下实现最高 3 倍加速。这属于 Google 的厂商声明，所给材料未包含基准设置、模型规模或独立复现结果，因此尚不能确认该加速在一般工作负载中的可复现性。

hackernews · ComputedCamp995 · 11月27日 23:06 · [社区讨论](https://news.ycombinator.com/item?id=50672565)

**「研究背景」** Transformer 的残差连接通常把前一层输出与当前层输出直接相加，相关研究认为这种简单求和可能稀释关键信息。DeepCrossAttention（DCA）正是为改进这种残差学习方式而提出；arXiv 页面显示该论文于 2025 年 2 月发布，Google Research 在 2026 年 11 月 23 日的博客中称其来自 ICML 2025 论文，并称在参数量增加可忽略的情况下，模型可以最多快 3 倍达到相同质量。

**「采用代价在训练侧」** 对打算采用 DCA 的团队而言，这一改动落在残差连接结构本身，需要在训练前修改模型定义并重新训练，无法作为推理端的加速开关直接套用到已有权重上；论文称其代价仅是参数量的小幅增加，并在相同参数预算和训练时间下取得更低的困惑度。因此评估时应把最高 3 倍的加速视为作者报告的结果，并针对自己的模型规模复现验证。

**「社区讨论」** Hacker News 评论中，有人批评性能对比图不应使用折线图，因为各方法之间没有时间或连续关系；也有人将其与 DenseNet 类比，并有评论者询问能否与 MTP、Dflash 等已有加速方法叠加，把自己过去两年约 10 倍的令牌吞吐提升进一步推到 30 倍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2502.06785">[2502.06785] DeepCrossAttention : Supercharging Transformer ...</a></li>
<li><a href="https://research.google/blog/supercharging-transformer-residual-connections/">Supercharging transformer residual connections</a></li>
<li><a href="https://huggingface.co/papers/2502.06785">Paper page - DeepCrossAttention : Supercharging Transformer ...</a></li>
<li><a href="https://research.google/blog/supercharging-transformer-residual-connections/">Supercharging transformer residual connections</a></li>
<li><a href="https://arxiv.org/html/2502.06785">DeepCrossAttention : Supercharging Transformer Residual...</a></li>
<li><a href="https://www.alphaxiv.org/overview/2502.06785v1">DeepCrossAttention : Supercharging Transformer Residual... | alphaXiv</a></li>

</ul>
</details>

**标签**: `#transformers`, `#model efficiency`, `#deep learning`, `#Google Research`, `#residual connections`

---

<a id="item-tech-news-3"></a>
### [购物网站出现利用 WebRTC 的信用卡盗刷脚本](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer) ⭐️ 7.0/10

一份安全报告称，热门购物网站上发现了使用 WebRTC 的信用卡盗刷脚本，用于把窃取的支付数据外传。报道没有给出受影响站点、脚本数量或攻击者身份，因此目前无法判断暴露范围有多大。该手法被描述为一种规避监控的外传方式，而不是 WebRTC 本身出现了新的安全漏洞。

hackernews · scanr · 11月27日 15:40 · [社区讨论](https://news.ycombinator.com/item?id=50668145)

**「背景」** 网页盗刷（web skimming）并不是新手法：攻击者常把恶意脚本注入合法电商页面，或借第三方脚本/供应商供应链进入结账流程，截取支付卡数据。Visa 披露的 Baka JavaScript 盗刷器会把窃得数据发往一个用受害商户域名解密的外发网关，说明这类攻击的关键环节之一就是隐蔽回传。此次报告描述的是同类脚本转而利用浏览器的 WebRTC 能力回传数据。

**「影响」** 对电商和支付团队来说，直接暴露面是结账页加载的第三方脚本：只要其中任一脚本能执行，它就可能读取支付表单并把数据送走。报告未列出具体商户或脚本，团队无法据此确认自己是否受影响，只能自行清点结账流程中的外部脚本和网络连接。

**「社区讨论」** 有评论者认为，问题核心不是 WebRTC 的技术能力，而是商家允许第三方脚本在结账页执行，且 WebRTC 流量相对较少被监控；他还指出，普通 HTTP 请求同样可以实现类似外传。另有评论者从广告拦截、浏览器不应执行陌生代码以及广告沙箱等角度表达了更激进的看法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/web_skimming">Web skimming — Grokipedia</a></li>
<li><a href="https://usa.visa.com/dam/VCOM/global/support-legal/documents/visa-security-alert-baka-javascript-skimmer.pdf">PFD-20-027-Visa Security Alert-Baka JavaScript Skimmer</a></li>

</ul>
</details>

**标签**: `#web security`, `#credit card skimming`, `#WebRTC`, `#third-party scripts`, `#e-commerce`

---

<a id="item-tech-news-4"></a>
### [Convex 技能被指未经告知上传用户应用想法](https://github.com/convex/convex-backend-skill/issues/64) ⭐️ 7.0/10

一项针对 Convex 后端技能（convex-backend-skill）的 GitHub issue 指称，相关工具会在未明确告知用户的情况下，把用户的应用想法上传到远程服务器。讨论中，Convex CEO Jamie 回应称，该插件中的提示上传用于支持 Convex 的“quickstart”功能，并提到公司已关闭此前的端到端“vibe-coding”产品 Convex Chef。现有材料未说明该上传的触发条件、数据保留方式，以及用户能否关闭该行为，相关隐私影响仍待进一步澄清。

hackernews · MickyTheMouse · 11月27日 18:02 · [社区讨论](https://news.ycombinator.com/item?id=50669765)

**「背景」** Convex 是一个用于构建和托管软件的全栈平台，存储用户的数据和代码，并提供既用于辅助开发、也用于驱动应用内功能的 AI gateway。该公司此前推出了端到端的 vibe-coding 产品 Convex Chef，但已将其关闭；CEO 表示，插件中的提示上传服务于 Convex 的“quickstart”功能，而 quickstart 是 Chef 的精神续作。

**「对开发者的影响」** 使用该插件的开发者应核查 quickstart 流程是否会发送提示内容；在 Convex 说明传输范围、保留期限和退出方式之前，不宜在其中输入未公开的代码或产品构想。

**「社区讨论」** Jamie（Convex CEO）在评论中解释，提示上传用于支持 quickstart，并称前身产品 Convex Chef 已关闭；有评论者据此主张长期应转向可自托管的开放权重模型，也有人指出提示注入比模型自行发起恶意工具调用更常见。

**标签**: `#privacy`, `#AI coding tools`, `#developer tools`, `#transparency`, `#Convex`

---

<a id="item-tech-news-5"></a>
### [多州总检察长起诉 SpaceX，要求叫停 Grok 生成儿童性虐待与未经同意图像](https://www.oag.state.va.us/media-center/news-releases/jay-jones/3162-attorneys-general-jones-and-rayfield-file-suit-against-spacex-parent-company-of-x-xai-and-grok-over-creation-and-promotion-of-child-exploitation-and-non-consensual-images-on-platform) ⭐️ 7.0/10

弗吉尼亚州总检察长办公室发布的新闻稿称，琼斯（Jones）与雷菲尔德（Rayfield）两位州总检察长已对 SpaceX 提起诉讼，指控该公司旗下 xAI 的 Grok 生成儿童性虐待材料以及未经同意的性图像，并请求法院制止这类输出。新闻稿把 SpaceX 表述为 xAI 与 Grok 的母公司，从而将模型输出问题直接归责于母公司，而非仅指向个别使用者。目前可获取的材料只有检方一侧的新闻稿，既无法院裁决，也无独立的第三方核查，因此上述指控仍属未经裁断的主张。

hackernews · DeepLogin · 11月27日 19:42 · [社区讨论](https://news.ycombinator.com/item?id=50670855)

**「背景」** Grok Imagine 是 xAI 在 X/Grok 中提供的图像生成功能，而 SpaceX 是 X 与 xAI 的母公司。11 月 23 日的报道显示，俄勒冈州和弗吉尼亚州已就 Grok Imagine 生成性化图像以及 Grok 的安全声明起诉 SpaceX；当前诉讼正是围绕同一工具和同类指控展开的州级法律行动。

**「可能影响」** 若法院支持检方诉求，Grok 的图像生成功能可能被迫对特定类别提示词直接拒答或加上更严格的过滤，使用该功能的用户和开发者会遇到可用性下降与审核规则变动的风险。诉讼选择起诉母公司 SpaceX 而非单个用户，也意味着责任认定可能上移至平台运营方层面。

**「社区讨论」** 评论者围绕三点展开：lacoolj 疑惑此类内容在各平台早已被禁，Grok 究竟是本身管控很松，还是需要用户刻意“诱导”才会生成；poontanglatits 则追问使用者本人的责任问题。ratelimitsteve 声称最高法院已裁定，为自用而用 AI 生成儿童性虐待材料属于受保护言论，但不得涉及真实儿童——这是评论者的法律主张，未获本条目所提供证据的核实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/11/23/technology/spacex-lawsuit-ai-sexualized-images.html">SpaceX Sued By Oregon and Virginia Over A.I.-Generated Sexualized ...</a></li>
<li><a href="https://www.cnbc.com/2026/11/23/oregon-virginia-spacex-grok-deepfake-lawsuits.html">SpaceX sued by 2 states over AI deepfake porn, Grok safety claims</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#content moderation`, `#generative AI`, `#litigation`, `#xAI/Grok`

---

<a id="item-tech-news-6"></a>
### [SemiAnalysis 解读 Trainium3 推理：宣称 TCO 优于 GB300](https://newsletter.semianalysis.com/p/trainium3-inferencex) ⭐️ 7.0/10

SemiAnalysis 发布了对 AWS Trainium3 推理性能和微架构的深度分析，面向关注 AI 加速器的读者。文章称 Trainium3 相比 NVIDIA GB300 具有更好的性能 TCO，并列出高 MFU/MBU、低延迟、UBenchX 以及基于第一性原理的物理架构等要点。目前可获取的内容只有标题和要点，相关 TCO 与性能数字属于 SemiAnalysis 的宣称和分析，尚未经过独立验证，也未说明测试条件、软件版本或可用性。

rss · Semianalysis · 11月27日 15:54

**「背景」** Trainium 是 AWS 为自家云环境设计的自研 AI 加速器产品线，而 GB300 NVL72 是英伟达面向大规模 AI 工作负载的机架级系统，因此两者在推理场景下的对比，本质上是云厂商定制 ASIC 与商用 GPU 方案之间的性价比之争。SemiAnalysis 此次把每美元推理性能作为核心比较指标，并给出 Trainium3 相对 GB300 NVL72 的 TCO 结论。

**「影响」** 对正在评估推理硬件的团队而言，这篇分析可作为对比 Trainium3 与 GB300 的参考，但在采信其 TCO 结论前应核对基准方法、工作负载和软件栈版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cryptobriefing.com/trainium3-nvidia-gb300-inference-benchmark/">Trainium3 competes with Nvidia GB300 in inference performance ...</a></li>
<li><a href="https://explainx.ai/blog/amazon-trainium3-ultraserver-agentx-performance-per-dollar-claimed-vs-verified-november-2026">Trainium3 2.28x vs GB300: What SemiAnalysis Shows | explainx ...</a></li>

</ul>
</details>

**标签**: `#AWS Trainium`, `#AI accelerators`, `#inference`, `#microarchitecture`, `#hardware`

---