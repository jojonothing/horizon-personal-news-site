---
layout: default
title: "Horizon Summary: 2026-11-25 (ZH)"
date: 2026-11-25
lang: zh
---

> 从 7 条内容中筛选出 6 条重要资讯。

---

**科技新闻**
1. [OpenAI 预印本声称矩阵乘法指数为 9/4（Θ\(n^2.25\)）](#item-tech-news-1) ⭐️ 9.0/10
2. [Simon Willison 复盘 LLM 与编码代理三大拐点](#item-tech-news-2) ⭐️ 8.0/10
3. [Check Point 管理服务器遭入侵，V8 随机数可预测致会话伪造](#item-tech-news-3) ⭐️ 7.0/10
4. [Ternary Bonsai 2.5 27B：三值量化 27B 模型本地跑 128k 上下文](#item-tech-news-4) ⭐️ 7.0/10
5. [演示称通过兼容层在 Windows 运行 GTA 6](#item-tech-news-5) ⭐️ 7.0/10
6. [GPT-6.2 Astra 用 22 分钟自主破解 1808 年素描本作者](#item-tech-news-6) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenAI 预印本声称矩阵乘法指数为 9/4（Θ\(n^2.25\)）](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf) ⭐️ 9.0/10

OpenAI 在其 GitHub 的 math 仓库发布预印本《The matrix multiplication exponent is nine fourths》，声称矩阵乘法指数 ω 恰好为 9/4，即复杂度为 Θ\(n^2.25\)；该文于 11 月 24 日发布、25 日出现在 Hacker News，未经同行评审，公开信息中也没有证明细节。评论者 brandonb 称，论文证明的是 Ω\(n^2.25\) 的下界，而 2.25 的上界此前已知，近期虽已有达到该复杂度的算法发表，但据其说法距离实用仍很远（该评论在此处被截断）。评论者 zone411 称 OpenAI 这批共四篇论文解决了 Top 500 Open Problems in Math 清单中的 8 个问题，包括强多项式线性规划（Smale 第九问题）、mean-payoff 博弈与 parity 博弈，并称该论文推翻了指数等于 2 的猜想。评论者 orlp 则指出 Hacker News 原标题写作 O\(n^2.25\) 有误，应为 Θ\(n^2.25\) 或原题中的 nine fourths；上述技术结论目前均只来自预印本与讨论，尚待独立验证。

hackernews · E-Reverance · 11月25日 01:19 · [社区讨论](https://news.ycombinator.com/item?id=50637220)

**「背景：矩阵乘法指数」** 矩阵乘法的复杂度通常用指数 ω 衡量：若两个 n×n 矩阵可在 O\(n^ω\) 时间内相乘，ω 就是该问题的渐进指数，精确确定它是计算复杂性理论的核心问题之一。Hacker News 评论指出，2.25 的上界此前已经知道；因此这篇预印本若成立，关键新意在于声称给出了匹配的下界，使指数被确定为 9/4，而非首次提出 O\(n^2.25\) 算法。

**「影响与后续」** 若证明成立，矩阵乘法的下界与已知上界将在 2.25 处闭合，长期被讨论的 ω=2 猜想随之被否定，复杂度理论中这一核心参数将由估计变为确定值。对实际计算则影响有限：brandonb 提到已达 O\(n^2.25\) 的算法距离实用很远，因此数值库和工程实现短期内不会因此改变；更现实的后续动作是同行评审与独立复核，尤其是该预印本并未公开其证明所依赖的方法。

**「社区讨论」** 评论者 mmaunder 提出一种猜测：OpenAI 可能把最强模型留在内部用于研究，再用由此得到的突破反哺更强的模型，从而使公开模型质量停滞；他指出这一结果据称来自一个未发布的模型，且配方未公开。评论者 StableAlkyne 把近期 OpenAI 与 Anthropic 的密集产出类比为贝尔实验室，但认为两家公司缺乏当年那种以公共福利为条件的约束，这些成果对其而言更多是公关。

**标签**: `#matrix multiplication`, `#computational complexity`, `#algorithms`, `#OpenAI`, `#research preprint`

---

<a id="item-tech-news-2"></a>
### [Simon Willison 复盘 LLM 与编码代理三大拐点](https://simonwillison.net/2026/Nov/24/llm-inflection-points/) ⭐️ 8.0/10

Simon Willison 在 AI Engineer Code Summit 演讲及后续文章中，把过去 12 个月 LLM 与编码代理的能力跃迁归纳为三个拐点。第一个是 2025 年 11 月的 Claude Opus 4.5：他称这是首个让 Claude Code 默认结果“通常正确”的模型，OpenAI 的 GPT-5.1 Instant、Thinking、Codex 和 Codex-Max 也让 Codex 变得可靠；第二个是 2026 年 6—7 月的 Claude Fable 5 等“Fable 类模型”，只要给出目标和工具就能自行求解问题，尽管 Mythos 因网络安全能力被 Anthropic 认为过于危险而未发布，Fable 5 也曾受美国出口管制影响。第三个是 2026 年 9—10 月的 3D 建模与游戏开发能力，Opus 5.5 被他称为首个“理解 fun”的模型，能用 12 小时试玩和重平衡把一款 RTS 改得有趣；这些主要是他的个人体验和演讲框架，并非独立基准结论，他还在追问 Fable 5.2 是否也算一个拐点。

rss · Simon Willison · 11月24日 23:02

**「背景」** Claude Code 于 2025 年 2 月 24 日随 Claude 3.7 Sonnet 一同推出；到 2025 年 11 月 24 日 Claude Opus 4.5 发布时，它已有 9 个月历史。作者 Simon Willison 此前没有把 Claude Code 作为日常主力，因为他觉得结果不够可靠、经常需要人工纠正。

**「影响」** 对使用编码代理的开发者，Willison 的判断是评估重点应从“能否生成代码”转向“默认结果是否需要频繁纠正”：他把 Opus 4.5 视为首个可日常依赖的 Claude Code 模型，并称 Fable 类模型已构成他对前沿模型的新基线。若按此标准选型，团队应优先验证模型在自身多系统、模糊需求上的纠错成本；但他给出的主要是个人案例，且 Fable 5 的出口管制经历说明可用性也会随政策变化。

**标签**: `#LLM agents`, `#coding agents`, `#AI engineering`, `#model capabilities`, `#retrospective`

---

<a id="item-tech-news-3"></a>
### [Check Point 管理服务器遭入侵，V8 随机数可预测致会话伪造](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign) ⭐️ 7.0/10

GreyNoise 报告称存在一场针对 Check Point 安全管理服务器的在役入侵活动，攻击者利用 JavaScript V8 引擎 Math.random\(\) 的可预测输出伪造管理员会话 Cookie。按讨论中引用的报告描述，攻击者向 HFS 的 loginSrp1 端点连续发起登录，收集每次返回的、sid 由 Math.random\(\) 生成的签名会话 Cookie，据此重建 V8 PRNG 内部状态、恢复 HFS 会话 Cookie 签名密钥，再伪造已签名的管理员会话。现有材料未说明初始访问路径；评论者推测与 CVE-2026-16232 有关，并把多家 Check Point 客户同时受影响与服务器暴露在互联网上联系起来，但这些都尚未得到确认。该发现目前属 GreyNoise 的单方研究结论，材料中没有 Check Point 官方回应或独立验证。

hackernews · louiereederson · 11月24日 16:32 · [社区讨论](https://news.ycombinator.com/item?id=50630594)

**「背景」** 这类攻击依赖一个前提：Node.js 所基于的 V8 引擎，其 Math.random\(\) 是非密码学安全的伪随机数生成器；攻击者只要拿到足够多连续输出，就能重建其内部状态，从而预测后续取值。若会话标识或签名密钥由此派生，伪造的 cookie 便可能通过校验。GreyNoise 同一份报告称，确认的攻击活动发生在 2026 年 10 月 17 日至 11 月 2 日，至少涉及 22 个组织；Check Point 的支持公告则把 Security Management Server 与 Multi-Domain Security Management Server 中的目录遍历与文件上传问题列为 CVE-2026-93616（CVSS 9.8），并称该漏洞已被在野利用、有少量客户遭到攻击。

**「影响与处置」** 直接后果是：签名密钥一旦被恢复，攻击者无需管理员口令即可持伪造 Cookie 以管理员身份操作 Check Point 管理服务器。对外暴露 HFS 与管理接口的组织应优先排查暴露面并限制访问；讨论中提出的关键疑问正是，受影响客户是否都把管理服务器直接放在了公网上。

**「社区讨论」** 评论者 omh 追问攻击者如何获得初始访问，认为多家 Check Point 客户同时中招指向 CVE-2026-16232，并质疑这些组织是否都将管理服务器暴露于互联网。另一条获附和的意见（20after4）认为根源在于 Math.random\(\) 本身不适合安全用途，主张修随机数生成器，而不是逐个修补用错它的应用；这些均为评论者观点，而非已证实结论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign">An Active Intrusion Campaign Against Check Point Security ...</a></li>
<li><a href="https://support.checkpoint.com/results/sk/sk1000171/">sk1000171 - CVE - 2026 -93616: Directory Traversal and File upload...</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability-exploitation`, `#check-point`, `#prng`, `#nodejs`

---

<a id="item-tech-news-4"></a>
### [Ternary Bonsai 2.5 27B：三值量化 27B 模型本地跑 128k 上下文](https://prismml.com/news/bonsai-2-5-27b) ⭐️ 7.0/10

据 Hacker News 评论者自测，Ternary Bonsai 2.5 27B（三值量化 Q2 GGUF、27B 参数）可在消费级硬件本地运行：在 Mac Mini M5 Pro（24GB 内存、512GB SSD）上生成速度约 22–25 tok/s，首 token 约 2.1 秒，并能轻松把 128k 上下文放进内存。与上一版 Bonsai2 相比，一位用户用自建长程任务基准测得通过数同为 8 项中的 5 项，但步数从 358 降至 296（少 17%），耗时从 107 分钟降至 76 分钟（少 29%），而 tok/s 不变。有评论者称该模型在 SWE-bench Verified 上的得分与 2026 年 2 月发布的 Opus 4.6 相当，但本人明确标注了不确定性。上述数字全部来自评论者自测，帖子未附带官方发布说明或可核实的基准数据，性能结论尚未获得独立验证。

hackernews · b0m · 11月24日 20:08 · [社区讨论](https://news.ycombinator.com/item?id=50633922)

**「背景：三值量化与 Bonsai 2.5」** 三值量化把模型权重压到约 -1、0、+1 三档（配合缩放因子），以大幅降低内存占用；Bonsai 2.5 27B 用约 5.9 GB 的三值权重承载 27B 参数，并支持 262K token 上下文。它是 Bonsai 2 的后续版本，厂商称在相同约 5.9 GB 体积下增强了智能体编码和多轮工具调用能力。

**「本地部署影响」** 对本地开发者而言，最直接的后果是：厂商公布 Bonsai 2.5 27B 的 GGUF 文件仅 5.93 GB，可通过 vLLM 部署并保留 262K 上下文，意味着 27B 级编码代理有机会跑在消费级硬件而非数据中心 GPU 上；不过 SWE-bench Verified 75.6 与 Terminal-Bench 2.1 60.1 均为厂商自报数据，尚待独立验证。兼容性上需留意，官方演示脚本默认下载的仍是 Bonsai 2，要使用 2.5 需显式获取对应的 GGUF 或 MLX 权重。

**「社区讨论」** 讨论焦点是小模型在基准上的高分意味着什么：一位评论者认为，这可能是针对基准的优化、基准本身的漂移，以及小模型以约 6 个月滞后复现前沿行为三者叠加，并承认 SWE-bench Verified 未必具代表性。另有评论者希望看到与同尺寸模型的直接对比，例如 1B–10B 区间流行模型的 Q1/Q2 量化版本，而不是只与前沿模型比较；提出长程任务对比的那位用户也说明其基准为自建，Opus 5.5 在该基准上 8 项全过。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prismml.com/news/bonsai-2-5-27b">PrismML — Introducing Ternary Bonsai 2.5 27B : Powering ...</a></li>
<li><a href="https://docs.prismml.com/models/bonsai-2-5-27b">Ternary Bonsai 2.5 27B - Bonsai - docs. prismml .com</a></li>
<li><a href="https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF">prism-ml/ Ternary - Bonsai - 2 . 5 - 27 B -GGUF · Hugging Face</a></li>
<li><a href="https://github.com/PrismML-Eng/Bonsai-demo">GitHub - PrismML-Eng/ Bonsai -demo: Bonsai Demo · GitHub</a></li>

</ul>
</details>

**标签**: `#ternary quantization`, `#local LLMs`, `#agentic coding`, `#model efficiency`, `#SWE-bench`

---

<a id="item-tech-news-5"></a>
### [演示称通过兼容层在 Windows 运行 GTA 6](https://twitter.com/raul_bs3/status/2125213756238291075) ⭐️ 7.0/10

一则推文演示声称，GTA 6 已能在 Windows 上运行，途径不是官方 PC 版，而是围绕泄露的 Xbox 构建进行的非官方兼容工作。现有材料只有该推文和 Hacker News 讨论，尚无独立验证，也未见可复现步骤或性能数据。评论者 Tiberium 称，现代 Xbox 与 Windows PC 很接近，xcl 和 VIctory 等项目采用类似 Wine 的兼容层，主要需处理兼容性与图形，泄露二进制据称没有特殊 DRM 或混淆。

hackernews · andrem · 11月24日 13:19 · [社区讨论](https://news.ycombinator.com/item?id=50627783)

**「背景」** 此前流出的 Xbox 版《GTA 6》构建为这类尝试提供了可执行文件与资源；讨论称其中没有特殊的 DRM 或混淆，主要难点在兼容层和图形。xcl 自称是面向 Windows 的 Xbox Series 兼容层，VIctory 则是尝试在 PC 上运行《GTA VI》的独立项目，二者都采用类似 Wine 的路线。

**「影响」** 对希望提前在 PC 上体验的玩家来说，这不是可用的官方移植：它依赖泄露构建和仍在解决兼容性、图形问题的非官方项目，稳定性没有保障，并伴随来源不明二进制带来的安全与版权风险。

**「社区讨论」** 讨论的技术焦点集中在为何需要泄露的 Xbox 构建：Tiberium 给出接近 Wine 的兼容路线解释，而 pipes 质疑该构建为何算泄露，并担心未来游戏把关键组件放到云端以阻止反编译。ivraatiems 则认为，即便存在此类非官方运行方式，也不足以威胁 GTA 6 这类大型游戏的制作与盈利。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://victorygta6.wiki/xcl/">XCL GTA 6 PC (ivall/ xcl ): 30 FPS Menus, GitHub &amp; VIctory</a></li>
<li><a href="https://gta.mtwildwood.net/">GTA 6 on PC: XCL and VIctory progress - GTA VI Tracker</a></li>

</ul>
</details>

**标签**: `#reverse engineering`, `#game compatibility`, `#Windows`, `#GTA 6`, `#Wine-like compatibility`

---

<a id="item-tech-news-6"></a>
### [GPT-6.2 Astra 用 22 分钟自主破解 1808 年素描本作者](https://simonwillison.net/2026/Nov/24/astra-historical-mystery/) ⭐️ 7.0/10

历史学教授 Mark Humphries 记述了一个案例：在仅有极少提示的情况下，GPT-6.2 Astra 自主判定耶鲁大学 Beinecke 图书馆所藏一本 1808 年匿名素描本的作者，整个过程耗时 22 分钟，使用的是公开的一手与二手资料。它在一份纸质档案中发现了一条鲜为人知的日记记录——一位名为 vicomte de Chabot 的访客到访的时间，比素描本中提到的附近河流日期早五天——并据此提出假设：Chabot 的旅行日志（只能向克利夫兰州立大学订购）可以证实素描本出自他手。Humphries 称这份日志最终确实提供了确认，而且该史料本身对加拿大史与毛皮贸易史研究具有重要价值。Simon Willison 转述了这一案例；这是单一轶事性报告，相关发现尚未经独立核实。

rss · Simon Willison · 11月24日 16:53

**「背景」** 这本 1808 年速写本现藏于耶鲁大学贝内克图书馆，该馆是耶鲁珍本书、手稿与档案的主要特藏所在地。速写本已经数字化并在馆藏目录中公开，但此前以匿名状态著录，作者身份尚未确定，需要借助馆藏之外的文献证据来考证。

**「实际影响」** 对从事档案研究的历史学者而言，这一案例的具体含义是：代理系统能够自行提出可证伪的假设，并定位到尚未数字化的档案线索；但关键证据仍需人工向克利夫兰州立大学订购并查阅 Chabot 的日志，才能完成验证。Humphries 预计，明年春夏学界将因这类能做人做不到之事的代理系统而出现一轮信心危机，不过他判断其对历史学的冲击会比数学界温和。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://beinecke.library.yale.edu/">Beinecke Library | Yale Library</a></li>

</ul>
</details>

**标签**: `#LLM applications`, `#AI-assisted research`, `#autonomous agents`, `#historical research`

---