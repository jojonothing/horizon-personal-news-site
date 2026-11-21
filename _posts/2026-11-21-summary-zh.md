---
layout: default
title: "Horizon Summary: 2026-11-21 (ZH)"
date: 2026-11-21
lang: zh
---

> 从 15 条内容中筛选出 6 条重要资讯。

---

**科技新闻**
1. [Levent Alpöge 声称证明广义黎曼猜想，结果未验证](#item-tech-news-1) ⭐️ 8.0/10
2. [陶哲轩讨论无外力纳维-斯托克斯奇点与广义黎曼猜想](#item-tech-news-2) ⭐️ 8.0/10
3. [Thinking Machines 发布 Inkling 2 Mini 开源循环 Transformer 模型](#item-tech-news-3) ⭐️ 7.0/10
4. [arXiv 论文称语言模型能改写自身权重，引发争议](#item-tech-news-4) ⭐️ 7.0/10
5. [Signal 讨论限制移动端 AI 智能体获取私人数据](#item-tech-news-5) ⭐️ 7.0/10

**科技博客**
1. [输出缓存为何难以节省 LLM 成本](#item-tech-blog-1) ⭐️ 6.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Levent Alpöge 声称证明广义黎曼猜想，结果未验证](https://alpo.ge/remark.pdf) ⭐️ 8.0/10

Levent Alpöge 在 alpo.ge 发布一份 PDF，声称证明了广义黎曼猜想（GRH）。相关 Hacker News 讨论指向一份约 1.3GB、1500 万行的 Lean 形式化证明，以及另一份据称完全由人类完成的证明。所给材料没有包含或评估这些证明本身，因此该声明仍未经验证，不能视为已确认的数学结果。

hackernews · iamronaldo · 11月20日 14:16 · [社区讨论](https://news.ycombinator.com/item?id=50574968)

**「背景」** 广义黎曼猜想（GRH）是黎曼猜想的推广：它把关于黎曼 ζ 函数零点位置的断言，扩展到狄利克雷 L 函数等更广的一类 L 函数。Lean 是交互式定理证明器，把数学证明写成 Lean 代码后可由机器逐步检查；但代码规模本身并不等同于独立验证通过。

**「复核负担落在独立验证上」** 影响首先体现在验证环节：已有报道在介绍这项声明时明确标注其“未经核实”，并指出专家需要先检查什么；而据一位评论者按帖中指令实际拉取的结果，配套的 Lean 归档约为 1.3GB、约 1500 万行，需要分 14 段下载后再合并解压，复核成本因此相当高。与此同时，讨论中还出现了另一份据称完全由人写出的证明，这意味着在接受之前，形式化归档与人工证明两条路径都要经过同行检验；在这些检查完成之前，任何依赖广义黎曼假设的条件性结论都不宜按已确立的结果处理。

**「社区讨论」** 讨论中，djoldman 详细列出了下载和展开 1.3GB Lean 证明的命令，强调其规模；Jaxan 指出另有一份完全由人类完成的证明。dawdler-purge 则声称 Andrew Sutherland（MIT）用 Claude Code 进行的检查已通过多种形式化验证、目前没有疑问，但这些说法来自评论，所附材料并未独立核实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://interestingengineering.com/ai-robotics/anthropic-167-year-old-riemann-hypothesis-claude">Claude helped prove 167-year-old Riemann hypothesis , researcher...</a></li>
<li><a href="https://www.nacionale.com/en/articles/has-riemann-hypothesis-been-proved-levent-alpoge-claude-anthropic-claim-lean">Riemann hypothesis proof claimed with Claude, unverified</a></li>

</ul>
</details>

**标签**: `#Generalized Riemann Hypothesis`, `#Lean formalization`, `#AI mathematics`, `#unverified claim`, `#Hacker News discussion`

---

<a id="item-tech-news-2"></a>
### [陶哲轩讨论无外力纳维-斯托克斯奇点与广义黎曼猜想](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/) ⭐️ 8.0/10

陶哲轩（Terry Tao）在一篇博客文章中讨论了无外力欧拉与纳维-斯托克斯奇点，以及广义黎曼猜想。所提供的条目没有博客正文，因此无法确认文章是否给出新证明、证明复盖范围或形式化验证状态，也不能核实标题所列两项结果之间的具体关系。读者需查看原文以判断其主张。

hackernews · archon1410 · 11月20日 17:21 · [社区讨论](https://news.ycombinator.com/item?id=50578358)

**「背景」** 在流体方程研究中，“奇点形成”指从光滑初值出发的解在正有限时间内失去光滑性（即解爆破）；“无外力”则指方程本身不含外部驱动项。陶哲轩在 2026 年 10 月 4 日的博客中专门讨论过不可压缩流体中的经典解与奇点形成，把目标表述为：初值先在一段正时间内给出唯一的正则演化，随后在某个正有限时刻出现奇点。此次帖子的标题正是把同一类无外力奇点问题与广义黎曼猜想放在一起讨论。

**「社区讨论」** Hacker News 评论主要围绕 AI 辅助证明与 Lean 形式化验证展开：有评论称两个独立内核接受了结果，因而很可能不存在内核漏洞利用；也有评论质疑，大型 Lean 工程通过构建并不等于验证了预期的数学命题，而非某个平凡陈述。上述均为评论者说法，未获条目正文确认。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://terrytao.wordpress.com/2026/10/04/on-classical-solutions-and-singularity-formation-in-incompressible-fluids/">On classical solutions and singularity formation in ...</a></li>

</ul>
</details>

**标签**: `#mathematics`, `#Navier-Stokes`, `#generalized Riemann hypothesis`, `#formal verification`, `#AI-assisted proof`

---

<a id="item-tech-news-3"></a>
### [Thinking Machines 发布 Inkling 2 Mini 开源循环 Transformer 模型](https://thinkingmachines.ai/news/inkling-2-mini/) ⭐️ 7.0/10

Thinking Machines 发布了 Inkling 2 Mini，一款面向本地运行的开源权重循环 Transformer 模型。相关基准和速度数据尚未经过独立验证；早期社区报告称，该模型在 Ryzen 395 上通过 llama.cpp Vulkan 解码约 27 tokens/s，在 32GB M1 Pro 上以 q4 量化运行约 10 tokens/s。这些数字和性能对比来自早期用户测试，不能视为已经复现的结论。

hackernews · jasondavies · 11月20日 20:12 · [社区讨论](https://news.ycombinator.com/item?id=50581260)

**「背景」** Inkling 2 Mini 是 Thinking Machines 推出的 26.4B 参数 MoE 开放权重模型，每个 token 激活 5.4B 参数，可在 32GB 以上内存的 Mac 上本地运行。其“循环 Transformer”并非生成更多 token，而是在中间层重复计算以增加每个 token 的算力；本地部署还需要 llama.cpp、Unsloth 等已支持循环层与逐专家 NVFP4 量化的构建。

**「对本地部署者的影响」** 本地用户目前可通过 Transformers、llama.cpp 和 MLX 运行该模型，SGLang 也提供面向数据中心硬件的首日推理支持。但社区反馈显示，要在 llama.cpp 上获得可用速度，需先合入多个尚未合并的 PR（32694、32657、32429、32704）并打上额外补丁；有用户报告在 Ryzen 395 搭配 Vulkan 上达到约 27 tokens/s，在 32GB M1 Pro 上约为 10 tokens/s。因此，使用稳定版工具链的用户在相关改动合并前，可能遇到吞吐偏低或需要自行编译的问题。

**「社区讨论」** 社区反馈混合但偏正面：有用户报告在 Ryzen 395 的 llama.cpp Vulkan 上达到 27 tokens/s，并称初步编码测试有希望；也有 M1 Pro 用户称简单 Python 任务完成得不错，但其常用的硬币识别测试在约 1.2 万 tokens 后仍未成功。还有评论认为，若基准成立，开源权重的循环架构可能促使更多开放模型采用类似设计，并对这一开放程度下的安全与可解释性提出疑问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/inkling-2-mini/">Introducing Inkling 2 Mini - Thinking Machines Lab</a></li>
<li><a href="https://ollama.com/library/inkling-2-mini">inkling - 2 - mini</a></li>
<li><a href="https://unsloth.ai/docs/models/inkling-2-mini">Inkling 2 Mini - Run Locally Guide | Unsloth Documentation</a></li>
<li><a href="https://huggingface.co/blog/inkling2mini">Welcome Inkling 2 Mini, Cutting-edge Performance for your ...</a></li>
<li><a href="https://unsloth.ai/docs/models/inkling-2">Inkling 2 Small - Run Locally | Unsloth Documentation</a></li>

</ul>
</details>

**标签**: `#open-weight models`, `#local LLM inference`, `#looped transformer`, `#model release`, `#llama.cpp`

---

<a id="item-tech-news-4"></a>
### [arXiv 论文称语言模型能改写自身权重，引发争议](https://arxiv.org/abs/2611.21885) ⭐️ 7.0/10

一篇发布在 arXiv 的论文（编号 2611.21885）声称，语言模型可以仅凭自身推理改写自己的权重并变得更好，全程不使用梯度、也不做训练。据评论中引用的论文描述，模型在练习题上检验自己提交的权重编辑，只保留有效的改动，并在连续八轮会话中准确率持续上升。由于原始论文正文未提供，以上均为论文自述的主张，尚无独立复现或第三方测量结果。讨论者则普遍指出，实际展示出的自我修改范围相当狭窄。

hackernews · lwhsiao · 11月20日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=50577265)

**「背景」** 此前 MIT CSAIL 的“Sparks of Weight-Space Programming”工作已展示，模型可绕过梯度训练，直接读取并编辑网络权重：例如判断一个小型网络被训练来玩哪种游戏，或只修改 Qwen3.5-0.8B 约 0.016% 的权重来修复数学推理中的循环。该工作把这类“权重空间编程”描述为递归自我改进的一条更原生的路径——模型能检查、调试并改进自身或更新模型的权重，而不必先写代码去启动训练任务。

**「影响」** 对 AI 安全研究者来说，直接后果是评估方式需要调整：如果模型能在没有梯度的情况下定向改写权重，那么对齐所依赖的权重和激活层面就需要新的监控手段。评论者 LarsDu88 举例说，自主运行的模型可以先定位对安全行为敏感的激活，再将其抑制，但这是假设性场景，论文并未演示。对普通开发者而言，目前可迁移的结论有限：公开的自我改写收益似乎只来自修复“推理链过长、触发 token 上限”这类明显缺陷，能否带来一般能力提升仍无证据。

**「社区讨论」** 评论者 aesthesia 认为，模型唯一的自我改进是缩短推理链以避免触及 token 上限，并称这与近期一篇 weight-space programming 文章的结论一致——后者发现即使是 Astra 也无法在没有这类明显缺陷的情况下提升性能。Toutouxc 质疑“无梯度、无训练”的说法，认为“只提交有效改动”在实践中很像训练；gavinray 则指出，Google 的 sleep 框架已在离线阶段用自生成样本更新权重。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rikiyat.github.io/blog/weight-space-programming/">Sparks of Weight - Space Programming : LLMs can natively read...</a></li>
<li><a href="https://nathan.rs/posts/weight-space-lp/">Can a Linear Program Do Weight - Space Programming ?</a></li>
<li><a href="https://news.ycombinator.com/item?id=50341174">Astra can read and write weights to improve Qwen | Hacker News</a></li>

</ul>
</details>

**标签**: `#LLM self-modification`, `#weight editing`, `#AI safety`, `#machine learning research`

---

<a id="item-tech-news-5"></a>
### [Signal 讨论限制移动端 AI 智能体获取私人数据](https://signal.org/blog/protecting-your-privacy/) ⭐️ 7.0/10

Signal 发布博客文章，讨论如何限制移动操作系统上的 AI 智能体获取用户私人数据，涉及使用移动通讯应用的用户和开发者。现有材料没有说明具体覆盖哪些操作系统、采用何种限制机制或是否已上线，因此无法确认这是已落地的能力，还是仍在推进的倡议。

hackernews · dotcoma · 11月20日 09:42 · [社区讨论](https://news.ycombinator.com/item?id=50572348)

**「背景」** 移动操作系统内置的 AI 代理（如 Gemini、Siri）能够读取屏幕上显示的内容，这让只针对截图和录屏的防护不再足以保护聊天界面。据 The Verge 报道，Signal 将此次调整描述为阻止这类代理读取 Signal 数据，同时 Meredith Whittaker 承认该做法“不完整”，并未覆盖代理通过设备文件系统获取数据的途径。

**「对用户与平台的影响」** Signal 默认屏蔽截图后，普通用户在需要留存聊天记录的日常场景中（例如在 Windows 桌面版截取对话）将无法直接截图，这类操作需改用其他方式完成。Signal 同时要求 Apple、Google、Microsoft 允许应用完全退出操作系统级 AI 的数据访问，因此该保护能否覆盖系统自带的屏幕读取能力，取决于这三家平台是否采纳这一请求。

**「社区讨论」** 有评论引用 Machine Gods 对 Meredith Whittaker 的访谈称，即使用户自己不安装 AI 应用，只要联系人安装了，也可能让 Signal 聊天被读取。也有评论要求 Signal 公开其“取证调查”的发现，以便其他开发者复用；另有用户报告在 VPN 下添加联系人会反复遇到验证码，认为这与隐私保护目标冲突。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/1038390/signal-blocking-ai-agent-screenshots-mobile-app">Signal is blocking Gemini and Siri AI from reading your... | The Verge</a></li>
<li><a href="https://www.inc.com/aaron-mok/signal-blocks-screenshots-ai-agents-privacy/91440348">Signal Blocks Screenshots Over AI Agent Risks - Inc.com</a></li>
<li><a href="https://cybernews.com/privacy/signal-restricts-screenshots/">Signal blocks screenshots to stop AI agents reading chats</a></li>
<li><a href="https://www.reuters.com/legal/litigation/signal-restricts-screenshots-block-ai-agents-reading-messages-2026-11-20/">EXCLUSIVE: Signal restricts screenshots to block AI agents ...</a></li>

</ul>
</details>

**标签**: `#privacy`, `#mobile-security`, `#ai-agents`, `#signal`, `#platform-policy`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [输出缓存为何难以节省 LLM 成本](https://seangoedecke.com/why-output-caching-doesnt-work/) ⭐️ 6.0/10

rss · Sean Goedecke · 11月21日 00:00

**「背景」** LLM 推理的经济性依赖输入缓存，以避免每轮都重算整个对话历史。输出缓存看起来也能消除智能体反复引用代码、证据文档和样例造成的浪费，而且输出 token 比输入 token 更贵。

**「方案」** 作者设想的做法是微调或提示模型只给出引用，例如“src/script.py:12-15”或对话片段编号，再由智能体框架（harness）展开成实际内容，让用户无感。但作者指出，这只能优化用户可见的输出。按他自己的智能体历史估计，可见输出仅约占总输出 token 的 6%，推理 token 约占 50%，工具调用约占 44%。即使乐观地省掉可见输出的三分之二，按 Amdahl 定律，总输出也只能省约 4%。他还判断前沿模型在内部思维链中很少重复，但承认这一判断只有中等确信度，6% 也来自个人经验。真正的大头是 94% 的不可见输出，而这主要取决于模型智能：更强的模型能用更少的推理和工具调用得到答案，所以单价贵 5 倍、token 少 6 倍时，总成本反而更低。

**「启示」** 输出缓存瞄准的是成本结构中的小头，难以显著降低 LLM 智能体的开销。作者认为，节省输出成本的关键不是压缩可见重复，而是让更聪明的模型用更少的不可见 token 解决问题。

**标签**: `#LLM inference economics`, `#output caching`, `#token costs`, `#Amdahl&\#x27;s law`, `#AI agents`

---