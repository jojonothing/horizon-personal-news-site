---
layout: default
title: "Horizon Summary: 2026-11-18 (ZH)"
date: 2026-11-18
lang: zh
---

> 从 20 条内容中筛选出 9 条重要资讯。

---

**科技新闻**
1. [OpenAI 发布 GPT‑6.2 Astra 与 Sol，Astra 价格降至前代八成](#item-tech-news-1) ⭐️ 9.0/10
2. [Java4Shell：OpenJDK Base64 处理中的 RCE 漏洞分析](#item-tech-news-2) ⭐️ 8.0/10
3. [Prime Radiant 发布编程智能体外部沙箱三实现](#item-tech-news-3) ⭐️ 8.0/10
4. [微软发布 MAI Code 2 与 Code 2 Flash 代码模型](#item-tech-news-4) ⭐️ 7.0/10
5. [Cloudflare 称 Quad9 退出法国为 DNS 监管警示](#item-tech-news-5) ⭐️ 7.0/10
6. [Phrack 第 73 期发布：Docker 逃逸与 SSH1 漏洞史](#item-tech-news-6) ⭐️ 7.0/10
7. [Solid 2.0 发布，加入服务端 RPC 与实时原语](#item-tech-news-7) ⭐️ 7.0/10
8. [微软 ONNX Runtime 的 GitHub 仓库疑似下线](#item-tech-news-8) ⭐️ 7.0/10
9. [Datasette Lite 重写：在浏览器运行完整 Datasette](#item-tech-news-9) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenAI 发布 GPT‑6.2 Astra 与 Sol，Astra 价格降至前代八成](https://openai.com/index/introducing-gpt-6-2-astra-sol/) ⭐️ 9.0/10

OpenAI 发布两款新模型：面向高难度任务的旗舰模型 GPT‑6.2 Astra，以及面向日常工作的通用模型 GPT‑6.2 Sol，二者已通过 API 以 \`gpt-6.2-astra\` 和 \`gpt-6.2-sol\` 提供；Simon Willison 同步发布支持这两个模型的 LLM 0.38。按 OpenAI 公布的价格，Astra 为每百万 token 输入 8 美元、输出 40 美元，是上一代 GPT‑6 Astra（10/50 美元）的 80%，缓存输入价格从每百万 token 1 美元降至 0.40 美元；Sol 维持 2/10 美元，与 6.1 Sol 和 6 Sol 相同。Willison 的实测显示，两款模型在“把 Yonkers 变成巨型机甲”的 Three.js 动画测试中表现不如 Claude Fable 5.2 和 Gemini 4 Carbon；他还提到 Astra 6.2 在多项基准上低于 Fable 5.2，并且有用户抱怨其沟通方式容易令人困惑。社区给出的成本与基准数字（如 PacBench 得分）来自评论者自测，并非独立验证的官方结果。

hackernews · jasondavies · 11月17日 17:46 · [社区讨论](https://news.ycombinator.com/item?id=50535230)

**「背景」** OpenAI 上一代产品包括 GPT-6 Astra 和 GPT-6.1 Sol：前者定价为每百万 token 输入 10 美元、输出 50 美元，后者为输入 2 美元、输出 10 美元。此次 GPT-6.2 Astra 将标价降至输入 8 美元、输出 40 美元，缓存输入价从每百万 token 1 美元降至 0.40 美元，而 GPT-6.2 Sol 维持 GPT-6.1 Sol 和 GPT-6 Sol 的 2/10 美元价格不变。

**「实际影响」** 对长时间运行的 agent 会话而言，Astra 缓存输入价格降至原来的 40%，直接降低了重复上下文的开销；但开发者需要把代码中的模型 ID 改为 \`gpt-6.2-astra\` 或 \`gpt-6.2-sol\`，工具链也要相应升级（例如 LLM 需 0.38 及以上）。评论者 chriddyp 报告，在其数据分析考试任务中，Astra 的单次成本从约 20 美元降到约 4 美元，Sol 从 2.6 美元降到 1.2 美元，准确率相近，但他也观察到模型有时“提前收尾”而漏掉答案，说明成本下降并不总等于结果等价。

**「社区讨论」** 评论者对降价幅度普遍认可，chriddyp 将其归因于约 20% 的 token 减少和更少的工具调用，并称两款模型是其测试过的最快模型之一；但 Topfi 认为官方展示的幻灯片、工作簿和备忘录示例质量很差，甚至不如两周前单次提示得到的 GPT‑5.6 Sol 结果。thefourthchime 引用的 PacBench 自测显示，Astra 得 92 分、耗时 6.6 分钟、花费 2.04 美元，低于 Kimi K3.1 Pro 的 93 分（11.5 分钟、0.68 美元），失分点在于迷宫页面布局和一个始终不出门的橙色幽灵。mlmonkey 则引用系统卡指出，GPT‑6.2 Astra 比 GPT‑6 Astra 更容易怀疑自己正被测试或处于模拟环境中。

**标签**: `#large language models`, `#OpenAI`, `#model release`, `#benchmarks`, `#AI cost efficiency`

---

<a id="item-tech-news-2"></a>
### [Java4Shell：OpenJDK Base64 处理中的 RCE 漏洞分析](https://calif.io/java4shell/) ⭐️ 8.0/10

一篇技术文章声称，OpenJDK 在处理 Base64 时存在可导致远程代码执行（RCE）的漏洞，并给出了利用路径，其中包括通过公网进行“远程堆 Feng Shui”的堆布局操纵。文章同时指出，该攻击对 RTT 和抖动敏感，稳定且低延迟的网络更有利于提高可靠性，说明利用条件较为苛刻。该发现目前仍是单一研究者的技术披露，尚未看到独立确认或厂商公告；现有材料也没有明确具体受影响版本和修复状态。

hackernews · werrett · 11月17日 21:11 · [社区讨论](https://news.ycombinator.com/item?id=50538240)

**「背景」** Java4Shell 对应编号 CVE-2026-114938。据安全厂商的漏洞整理，Oracle 与 OpenJDK 项目已于 2026 年 11 月 17 日发布修复构建，11 月更新将 Java SE 8、11、17、21、25 和 27 列为受影响版本，CVSS 4.0 评分为 9.2；攻击者无需登录，只要向应用发送构造的 Base64 字符串即可触发内存破坏并最终达到远程代码执行，公开分析提到 Jira、Confluence、Jenkins、Keycloak 等服务器可作为攻击目标（tool-1-3、tool-1-2）。该问题的触发条件与平台相关：早期报告指出，受影响的程序是在 x86 服务器上运行的 Java 应用（tool-1-1）；因此某个部署是否命中该路径，取决于它使用的 JVM 实现和架构。

**「受影响范围与应对」** 按照该写法的判定条件，受影响主机需同时满足：运行 HotSpot 系虚拟机、CPU 支持 AVX-512 VBMI、且 Base64 内建解码启用；作者称 OpenJDK 17.0.6 及更新版本受影响，ARM64 不在其中，而 Oracle 在发布前提供的信息称 JRE8 同样受影响（Semgrep 的检测脚本也把 Oracle JDK、GraalVM JDK 等 HotSpot 构建列入排查范围）。因此运维方应优先排查这类 x86-64 主机并安排升级或打补丁，同时注意 OpenJ9、GCJ、Azul Prime（Zing）等非 HotSpot 实现不产生同样的代码路径，不能因“用了 Java”就一律判定暴露。社区流传的 -XX:UseAVX=2 规避方式尚未得到确认，不宜作为唯一防护手段；在补丁明确前，可用 Semgrep 发布的免费检测脚本按上述前置条件定位暴露面。

**「社区讨论」** 评论中，Semgrep 的 ievans 提供了免费检测脚本，称其检查五个前提条件，并指出只有 HotSpot（包括 OpenJDK、Oracle JDK、GraalVM JDK）会生成相关 stub，而 OpenJ9、GCJ 不受影响；AgentME 则转述未经确认的 Twitter 说法，称可通过 -XX:UseAVX=2 规避 AVX-512 路径。上述均属社区意见或未确认信息，并非漏洞已被独立验证的结论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://orca.security/resources/research/java4shell-critical-openjdk-base64-decoder-flaw-could-allow-unauthenticated-remote-code-execution/">Java 4 Shell CVE -2026-114938: Affected Versions &amp; Mitigation</a></li>
<li><a href="https://www.cyberkendra.com/2026/11/cve-2026-114938-pre-auth-rce-flaw-in-java-17-puts-servers-at-risk.html">Java 4 Shell ( CVE -2026-114938): Java Base 64 Flaw... - Cyber Kendra</a></li>
<li><a href="https://www.aikido.dev/blog/java-17-rce-vulnerability-cve-2026-114938">Java 4 Shell Java 17 RCE ( CVE -2026-114938): Fix &amp; Versions</a></li>
<li><a href="https://orca.security/resources/research/java4shell-critical-openjdk-base64-decoder-flaw-could-allow-unauthenticated-remote-code-execution/">Java 4Shell CVE-2026-114938: Affected Versions &amp; Mitigation</a></li>
<li><a href="https://calif.io/java4shell/">Java 4Shell: Write once, RCE everywhere</a></li>
<li><a href="https://news.ycombinator.com/item?id=50538240">Java 4Shell: RCE in OpenJDK when processing Base 64 | Hacker News</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#openjdk`, `#rce`, `#base64`

---

<a id="item-tech-news-3"></a>
### [Prime Radiant 发布编程智能体外部沙箱三实现](https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/) ⭐️ 8.0/10

Simon Willison 与 Prime Radiant 发布了面向编程智能体的“外部沙箱”模式，并提供了三个服务端实现：external-sandbox-v86 用 Node.js 服务器通过 v86 在 WebAssembly 中运行 Alpine Linux；external-sandbox-container 用 Python Web 服务器在 Apple Containers 实例内运行 Alpine Linux；external-sandbox-quicksand 则基于 Microsoft Quicksand，将 QEMU 与 Alpine Linux 打包进 Python 包。三者暴露相同的 localhost API，可让 Pi、Claude Code 或 Codex 在需要执行代码时调用沙箱；该模式让智能体留在沙箱外，代码在独立环境内运行。实现还带可选的 HTTP/HTTPS 主机白名单代理，并支持凭据替换，使智能体代码能发起经过认证的 API 调用而不直接持有密钥。

rss · Simon Willison · 11月17日 22:52

**「背景」** 编码代理经常需要执行自己生成的代码；一旦模型出错或遭遇提示注入，这些代码可能在开发机上造成破坏。外部沙箱模式因此把代理进程与执行环境分开：代理留在宿主机，代码在独立沙箱中运行，并通过统一的 localhost API 接收执行请求。这一模式可配合 Pi、Claude Code 或 Codex 使用。

**「影响」** 对使用这些智能体的开发者而言，具体可操作的变化是把代码执行端点指向本地沙箱服务，并通过代理白名单限制可访问主机、避免把真实密钥交给模型生成的代码；不过现有材料没有给出隔离强度、性能或逃逸测试结果，部署前仍需自行验证这些实现是否满足生产安全要求。

**标签**: `#AI agents`, `#sandboxing`, `#security`, `#local models`, `#developer tools`

---

<a id="item-tech-news-4"></a>
### [微软发布 MAI Code 2 与 Code 2 Flash 代码模型](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/) ⭐️ 7.0/10

微软发布了 MAI Code 2 和 MAI Code 2 Flash 两款代码模型，面向 AI 辅助编程场景。现有材料仅包含发布公告，未提供模型规模、基准成绩、定价、可用地区或与 GitHub Copilot 的正式集成细节，因此这些模型的实际能力目前仍属于厂商发布信息，尚无可独立验证的结果。

hackernews · lemonish97 · 11月17日 18:25 · [社区讨论](https://news.ycombinator.com/item?id=50535885)

**「背景」** MAI Code 系列此前定位为轻量级编码辅助；微软此次把该系列扩展到可承担复杂的智能体式软件工程任务，并同时发布 MAI Code 2 与 Code 2 Flash 两个版本。两款模型同步上线 GitHub Copilot，成为 Copilot 中可选的新一代 MAI 编码模型。

**「对 Copilot 用户的影响」** GitHub Copilot 已提供 MAI Code 2 和 MAI Code 2 Flash 供选择；GitHub 将 Flash 定位为轻量、低成本的编码模型，适合代码解释、定点修改、日常修复和快速迭代。使用 Copilot 的开发者因此可以按任务切换模型：日常小改动可选用 Flash 以控制成本，更复杂的任务则继续使用 MAI Code 2。

**「社区讨论」** 有评论者报告，在 GitHub Copilot 中切换到 MAI Code 2 后，解决了 Windows WSL/Ubuntu 下的 Python 构建和 Azure Bicep 部署问题，并称体验与 Claude Opus 差别不大；这是个人使用反馈，未经独立验证。另有评论认为 OpenAI 和 Anthropic 的领先优势可能只维持数月，并质疑此类基准能否在真实开发中成立。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.blog/changelog/2026-11-17-mai-code-2-and-mai-code-2-flash-in-github-copilot/">MAI Code 2 and MAI Code 2 Flash in GitHub Copilot</a></li>
<li><a href="https://github.blog/changelog/2026-11-17-mai-code-2-and-mai-code-2-flash-in-github-copilot/">MAI Code 2 and MAI Code 2 Flash in GitHub Copilot</a></li>

</ul>
</details>

**标签**: `#AI coding models`, `#Microsoft`, `#GitHub Copilot`, `#developer tools`, `#model release`

---

<a id="item-tech-news-5"></a>
### [Cloudflare 称 Quad9 退出法国为 DNS 监管警示](https://blog.cloudflare.com/quad9-withdrawal-from-france/) ⭐️ 7.0/10

Cloudflare 的一篇分析文章把 Quad9 退出法国视为 DNS 内容过滤和互联网监管的警示信号。Quad9 是主要公共 DNS 解析器，其退出使法国用户和网络运营者少了一个可选解析服务，并凸显过滤或封锁压力如何影响 DNS 基础设施。文章表达的是 Cloudflare 的立场分析，并非对过滤效果或用户实际影响的独立测量。

hackernews · subset · 11月17日 22:13 · [社区讨论](https://news.ycombinator.com/item?id=50538994)

**「背景」** Quad9 是由瑞士非营利组织运营的免费公共递归 DNS 解析器，主打隐私保护，声称不记录用户 IP、无需账户，并提供内置的恶意软件过滤。\[tool-2-2\] 它面向全球提供递归 DNS 服务，会拦截与恶意软件和钓鱼相关的域名。\[tool-2-1\] 据相关报道，此次事件源于法国方面要求其执行 DNS 域名封锁，而 Quad9 选择退出法国，而不是按命令屏蔽域名。\[tool-2-2\]

**「影响」** 对法国用户和网络运营者来说，直接后果是需要改用其他公共解析器或自建解析，并重新评估本地 DNS 过滤要求是否会波及替代服务。

**「社区讨论」** Quad9 的 CTO johnhtodd 在评论中称，IETF 127 上对其立场“迄今 100% 支持”，并表示业界对 DNS 相关案件普遍忧虑。Cloudflare 未在文中承诺具体行动，driverdan 因此追问其是否会在败诉时同样退出受影响国家。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Quad9">Quad 9 - Wikipedia</a></li>
<li><a href="https://www.techpassion.net/internet/quad9-leaves-france-dns-blocking/2169/">Quad 9 leaves France : DNS blocking order explained - TechPassion</a></li>

</ul>
</details>

**标签**: `#DNS privacy`, `#Internet regulation`, `#France`, `#content blocking`, `#network infrastructure`

---

<a id="item-tech-news-6"></a>
### [Phrack 第 73 期发布：Docker 逃逸与 SSH1 漏洞史](https://phrack.org/issues/73/introduction_md) ⭐️ 7.0/10

Phrack 第 73 期已发布，主要面向安全研究人员和软件工程师。据现有介绍，本期包含一篇 Docker 逃逸利用文章，以及一篇回顾 2000 年 SSH1 漏洞利用历史的文章。公开信息未说明该 Docker 逃逸是否经过负责任披露、是否分配了 CVE，或影响哪些具体版本。

hackernews · notmine1337 · 11月17日 18:31 · [社区讨论](https://news.ycombinator.com/item?id=50535992)

**「背景」** Docker 逃逸指容器内进程突破隔离并取得宿主机访问权限；理解这一概念有助于阅读本期 Phrack 的相关利用文章。Phrack 是长期出版的安全技术刊物，本期另有一篇回顾 2000 年 SSH1 漏洞利用历史的文章，把当前披露放回早期研究脉络中。

**「影响」** 对使用 Docker 的开发和运维团队来说，应把本期逃逸文章当作需要核实的风险信号，检查容器隔离配置与相关补丁状态；但现有材料不足以确认是否存在在野利用、未修复漏洞或特定受影响版本。

**「社区讨论」** 评论区最有实质性的讨论集中在披露规范：一位读者追问本期 Docker 逃逸是否已负责任披露并获得 CVE 编号，还是直接公开，现有评论没有给出答案。另有读者回忆 Phrack 早期文章的非正式风格，并推荐本期关于 SSH RCE 历史的文章。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.startupdefense.io/cyberattacks/docker-escape">Docker Escape : A Technical Guide to Container Security Risks</a></li>

</ul>
</details>

**标签**: `#security`, `#exploits`, `#vulnerability-disclosure`, `#hacker-culture`, `#phrack`

---

<a id="item-tech-news-7"></a>
### [Solid 2.0 发布，加入服务端 RPC 与实时原语](https://www.solidjs.com/blog/solid-2-0-the-long-hold/) ⭐️ 7.0/10

Solid 2.0 已发布，面向使用 Solid 的前端与全栈开发者，新增服务端 RPC 以及 live、broadcast 数据原语，并改进了调试诊断能力。这是一次大版本更新，但现有材料未给出升级兼容性、迁移成本或具体性能数据。

hackernews · pier25 · 11月17日 18:56 · [社区讨论](https://news.ycombinator.com/item?id=50536387)

**「背景」** Solid 2.0 距离 SolidJS 1.0 发布已有五年，是该项目的又一次大版本更新；此前服务端函数等能力由 SolidStart 这一独立元框架承载。此次 2.0 将 server functions 移入核心库，SolidStart 不再作为独立元框架存在，同时重写了响应式核心，使异步数据成为响应式图的一部分。

**「对采用者的实际影响」** 对使用 Solid 的团队而言，2.0 把 server RPC 与 live/broadcast 数据原语纳入框架本身；按社区讨论的说法，这能省去自行搭一层前后端胶水代码，比 LiveView、htmx/datastar 等方案更贴近日常写法。但升级是主版本跳变，现有材料未给出破坏性变更与迁移路径，升级前应核对官方迁移说明；同时 SolidJS 的生态规模仍小于 React、Vue，第三方库覆盖和招聘面较窄是选型时的现实权衡。

**「社区讨论」** Hacker News 评论对 Solid 2.0 的技术方向评价积极：pwmglenn 认为服务端 RPC 与 live、broadcast 的衔接比 LiveView、htmx/datastar 更自然，并将其与 Remix 未能完全填平前后端鸿沟的定位作比较。wk\_end 则指出，“Built to Be Written by Agents”下列出的改进本质上是更好的调试诊断，对手写代码同样有帮助，并认为这与 agentic 开发没有特别直接的关系。上述均为评论者观点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.solidjs.com/blog/solid-2-0-the-long-hold/">Solid 2.0 - The Long Hold - solidjs.com</a></li>
<li><a href="https://codingislove.com/solid-2-0/">Solid 2.0 released: async reactivity, server functions, no ...</a></li>
<li><a href="https://rankite.com/blog/alternatives-to-svelte">Alternatives to Svelte in 2026 : 8 Frameworks Compared</a></li>
<li><a href="https://hiredeveloper.dev/insights/best-frontend-frameworks-comparison-guide/">Best Frontend Frameworks 2026 | Full Guide</a></li>

</ul>
</details>

**标签**: `#javascript`, `#frontend-frameworks`, `#solidjs`, `#reactivity`, `#web-development`

---

<a id="item-tech-news-8"></a>
### [微软 ONNX Runtime 的 GitHub 仓库疑似下线](https://github.com/microsoft/onnxruntime) ⭐️ 7.0/10

微软的 ONNX Runtime GitHub 仓库似乎已无法访问，这个约有 2.2 万星标的机器学习推理运行时项目从 GitHub 上“消失”；目前没有微软的官方说明，也无法确认它是被删除、转为私有还是遭遇临时故障。提交者 nvader 称，其团队当天早上因评估流水线开始失败才发现此事，且没有收到任何提前通知，表明下游使用已经受到影响。社区讨论提出了供应链投毒、遥测争议、后门模型以及改用英特尔 OpenVINO 分支等可能解释，但这些解释均未得到证实。

hackernews · nvader · 11月17日 23:18 · [社区讨论](https://news.ycombinator.com/item?id=50539610)

**「背景」** ONNX Runtime 是微软开源的跨平台机器学习推理与训练加速引擎，仓库地址为 github.com/microsoft/onnxruntime，常被用作模型部署时的运行时依赖。据 AGI Hunt 的报道，该仓库在 GitHub 上已无法访问，疑似被删除或转为私有，目前尚无微软的官方说明。

**「影响」** 至少一名提交者称，其流水线中的评估任务在仓库不可用当天开始失败，且此前没有收到任何预警，说明依赖从 GitHub 获取 ONNX Runtime 的团队已受到直接影响。在微软未作说明的情况下，社区把 Intel 的 onnxruntime 分支视为最接近的替代，但该分支带有 OpenVINO 修改，替换前需验证与现有模型和部署环境的兼容性。

**「社区讨论」** 有评论者声称 ONNX 会自动外传应用数据，除非从源码构建时禁用遥测或阻断 DNS，但该说法在讨论中未提供可验证依据；另一人指出可临时改用带有英特尔 OpenVINO 修改的 intel/onnxruntime 分支。还有评论猜测此次下线与软件包被投毒或后门模型利用有关，这些同样只是猜测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/microsoft/onnxruntime">GitHub - microsoft/onnxruntime: ONNX Runtime: cross-platform ...</a></li>
<li><a href="https://agihunt.info/en/p/1a1ebe81991e04a4ffba110460c">Microsoft&#x27;s ONNX Runtime repo has vanished… · AGI Hunt</a></li>

</ul>
</details>

**标签**: `#onnx-runtime`, `#open-source`, `#machine-learning-infrastructure`, `#supply-chain-security`, `#github`

---

<a id="item-tech-news-9"></a>
### [Datasette Lite 重写：在浏览器运行完整 Datasette](https://simonwillison.net/2026/Nov/17/datasette-lite/) ⭐️ 7.0/10

Simon Willison 发布了 Datasette Lite 的完全重写版，改用 service workers 和 Pyodide，让完整的 Datasette Python 应用在浏览器中运行；作者称其效果已几乎与服务器端版本无异。用户可通过 lite.datasette.io 的 URL 参数加载 SQLite、JSON、CSV 或 SQL 文件，从 PyPI 选择已发布的 Datasette 版本，从 GitHub 加载特定提交、标签或分支，在 100 多个 SQLite 版本间切换，并安装 Datasette 插件或 wheel 文件。加载远程数据库等资源仍要求提供开放 CORS 响应头；这些版本与插件选择旨在让开发者无需搭建 Web 服务器即可分享进行中功能或 bug 的可复现演示。

rss · Simon Willison · 11月17日 16:48

**「背景」** Datasette Lite 最初于 2022 年发布，当时的做法是在 Pyodide Web Worker 中运行 Datasette、模拟请求，再用 innerHTML 把生成的 HTML 注入顶层页面。这个方案对基础页面有效，但 innerHTML 中的 script 标签不会执行，因此依赖 JavaScript 的功能和插件无法正常工作；本次重写改用 service workers，不再沿用 worker 加 innerHTML 的旧路径。

**「影响」** 对 Datasette 开发者和插件作者来说，这使特定 Datasette、SQLite 版本、数据和插件组合可以打包成一个链接，用于复现 bug 或演示未发布功能（文中即用 1.0a42 与 1.0a43 链接对比分页修复）；但远程 SQLite 文件必须提供开放 CORS 头，否则无法直接加载。

**标签**: `#Datasette`, `#Pyodide`, `#WebAssembly`, `#service workers`, `#SQLite`

---