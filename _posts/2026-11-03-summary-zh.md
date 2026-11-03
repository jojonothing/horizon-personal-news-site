---
layout: default
title: "Horizon Summary: 2026-11-03 (ZH)"
date: 2026-11-03
lang: zh
---

> 从 24 条内容中筛选出 7 条重要资讯。

---

**科技新闻**
1. [vLLM v0.33.0rc3：升级 PyTorch 2.14，仅发 CUDA 13.0 构建](#item-tech-news-1) ⭐️ 7.0/10
2. [Astra 声称可读写 LLM 权重并提升小型 Qwen 数学表现](#item-tech-news-2) ⭐️ 7.0/10
3. [Ubuntu LTS 内核近三周仍未修补 RCE 漏洞 CVE-2026-98432](#item-tech-news-3) ⭐️ 7.0/10
4. [Cloudflare 称定向 DNS 区域构建将延迟减半、内存降 85%](#item-tech-news-4) ⭐️ 7.0/10
5. [LightMIS：131K 参数医学分割模型](#item-tech-news-5) ⭐️ 7.0/10

**科技博客**
1. [LLM 直接读写权重并非超人类研究](#item-tech-blog-1) ⭐️ 7.0/10
2. [受众捕获：当代理指标悄悄替换你的目标](#item-tech-blog-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [vLLM v0.33.0rc3：升级 PyTorch 2.14，仅发 CUDA 13.0 构建](https://github.com/vllm-project/vllm/releases/tag/v0.33.0rc3) ⭐️ 7.0/10

vLLM 发布 v0.33.0rc3；发布说明按 v0.33.0 撰写，涵盖 927 个提交、389 名贡献者（其中 122 名新贡献者），其中写明升级到 PyTorch 2.14.0、torchvision 0.29.0 与 Triton 3.8.0。发行轮子和镜像转为仅提供 CUDA 13.0：CUDA 12.9 轮子及 \`-cu129\` / \`-cu129-ubuntu2404\` 镜像不再发布，CUDA 轮子改为与 libtorch ABI 稳定的构建；ROCm 默认镜像与轮子移到 ROCm 10.0，7.2 仍以 \`-rocm72\` 标签发布。新增 \`vllm/vllm-openai:v0.33.0-efa\` 镜像（x86\_64 与 aarch64，内含 AWS EFA 库和 EFA 版 Mooncake 传输引擎，用于 KV 传输和多节点服务），并且每个发行镜像同时以更短的 \`vllm/vllm\` 名称发布。破坏性变更包括移除 Medusa 与 MLP speculator、移除旧的 Ray 编译图执行器、NIXL 连接器要求 NIXL 1.5 以上，以及生成暂停期间收到的请求返回 HTTP 503；同时新增了 Reflection Beam-1.0、Yandex AliceAI-Foundation-80B-A3B、Step-5 Preview 等模型的集成，但所给发布说明在 GLM 部分被截断。

github · khluu · 11月2日 10:10

**「背景」** vLLM 是面向大模型推理与 OpenAI 兼容在线服务的高吞吐开源引擎，发布物包括 Python wheel、Docker 镜像，以及 CUDA、ROCm、XPU 和 CPU 等不同后端。这些构建产物与特定 PyTorch、CUDA/ROCm 工具链绑定，因此工具链版本和镜像标签的变化会直接影响用户现有的安装与升级方式。

**「影响」** 仍依赖 CUDA 12.9 产物的部署方需要改用默认的 CUDA 13.0 轮子或镜像，否则应停留在旧版本；使用 NIXL 连接器的集群须先把 NIXL 升级到 1.5 或更高版本，而采用 Medusa/MLP speculator 或旧 Ray 编译图执行器的服务需在升级前改造，否则相关功能将不可用。

**标签**: `#vllm`, `#llm-inference`, `#pytorch`, `#cuda`, `#release-notes`

---

<a id="item-tech-news-2"></a>
### [Astra 声称可读写 LLM 权重并提升小型 Qwen 数学表现](https://rikiyat.github.io/blog/weight-space-programming/) ⭐️ 7.0/10

一篇博客文章及 Hacker News 讨论介绍了一个名为 Astra 的系统，称它能直接读取和修改 LLM 权重，并在一个小型 Qwen 模型上取得数学能力提升（讨论中常被引述为约 5 倍）。目前公开材料是博客或论文式展示，尚无独立复现；参与讨论的研究者也提醒，结果可能被夸大。因此它更应被视为一个待验证的研究主张，不宜当作已确认的通用能力。

hackernews · dbreunig · 11月2日 18:21 · [社区讨论](https://news.ycombinator.com/item?id=50341174)

**「背景：权重空间编程」** 这里所说的“权重空间编程”，是指把模型权重当作可读写的文本对象，让模型直接定位并修改参数，而不是通过梯度训练或外部工具来调参。公开的模型卡和讨论称，Astra 在 Qwen 3.5-0.8B 上先诊断出重复/循环问题，再编辑 131,072 个权重（第 15、19 层 down\_proj 各 64 个 MLP 输出列），约占 0.016%。

**「影响」** 对关注权重空间编辑的研究者而言，实际影响是出现了一个需要按论文细节复现的案例；在核对基线、评测集和改动幅度之前，不宜把“5 倍数学提升”当作能力评估或选型依据，也不宜忽略既有权重编辑、生成和定位方法。

**「社区讨论」** 评论对 Astra 直接改写权重、提升小型 Qwen 数学能力表示震惊，但分歧明显：从事权重空间学习的研究者 yurimo 认为博客和发帖夸大了结果，并指出编辑权重、生成权重和定位权重并非全新能力。另有评论猜测，这可能源于模型训练数据中的权重数据，或属于涌现能力，但这些都只是推测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rikiyat.github.io/blog/weight-space-programming/">Sparks of Weight - Space Programming : LLMs can natively read ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=50341174">Astra can read and write weights to improve Qwen | Hacker News</a></li>
<li><a href="https://huggingface.co/akhaliq/Qwen3.5-0.8B-weight-space-programming">akhaliq/ Qwen 3.5-0.8B- weight - space - programming · Hugging Face</a></li>

</ul>
</details>

**标签**: `#LLM weight editing`, `#weight-space learning`, `#Qwen`, `#AI research`, `#model interpretability`

---

<a id="item-tech-news-3"></a>
### [Ubuntu LTS 内核近三周仍未修补 RCE 漏洞 CVE-2026-98432](https://freenode.net/article/ubuntu-lts-kernels-still-unfixed-for-critical-cve-2026-98432) ⭐️ 7.0/10

截至 11 月 2 日，Ubuntu LTS 内核在相关漏洞公开近三周后仍未获得 CVE-2026-98432 的补丁；该漏洞被描述为关键 Linux 内核远程代码执行漏洞。现有信息没有提供受影响的具体内核版本、触发条件或独立验证结果，因此实际暴露范围仍不明确。讨论重点因此转向临时缓解措施以及 Ubuntu 的响应速度，而不是已确认的修复进展。

hackernews · majorchord · 11月2日 18:39 · [社区讨论](https://news.ycombinator.com/item?id=50341462)

**「背景」** CVE-2026-98432 是一个 CVSS 9.8 的 Linux 内核远程代码执行漏洞；Ubuntu 的安全跟踪页已收录该编号，而 22.04、24.04、26.04 三个 LTS 版本在近三周内仍没有可用的修复内核包。Red Hat 的 RHSB-2026-016 公告提供了临时缓解方案，第三方脚本则据此用包元数据判断补丁状态，并可在确认后启用该缓解。

**「临时缓解措施」** 在 Ubuntu 发布内核更新前，LTS 管理员可部署 nftables 规则，丢弃携带 IP options 的入站 IPv4 TCP 报文；Red Hat 提醒这类规则只能降低暴露面，不能完全阻止利用。使用 firewalld、Docker 或 kube-proxy 的环境应将规则放在独立表中，以免被这些工具刷新掉。

**「社区讨论」** 评论中，一位用户提出可用 iptables/nftables 在 raw PREROUTING 通过 u32 规则丢弃相关流量作为临时缓解；其他人则追问 Ubuntu 为何迟迟不修补且未说明原因，并提到 RHEL 的缓解说明自称只能降低暴露、无法完全阻止，却未解释依据。这些均为社区观点，并非对补丁状态或缓解有效性的独立验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ubuntu.com/security/CVE-2026-98432">CVE-2026-98432 | Ubuntu</a></li>
<li><a href="https://freenode.net/article/ubuntu-lts-kernels-still-unfixed-for-critical-cve-2026-98432">Ubuntu LTS kernels still unfixed for critical CVE-2026-98432</a></li>
<li><a href="https://github.com/soroushneshati/cve-2026-98432-ubuntu-mitigation">GitHub - soroushneshati/cve-2026-98432-ubuntu-mitigation ...</a></li>
<li><a href="https://github.com/akamai/cve-2026-98432-validation-mitigation">GitHub - akamai/ cve - 2026 - 98432 -validation- mitigation : Read-only...</a></li>
<li><a href="https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf">Linux&#x27;s October 2026 TCP Use-After-Free: CVE - 2026 - 98432 — Atlas</a></li>

</ul>
</details>

**标签**: `#Linux kernel`, `#Ubuntu`, `#security vulnerability`, `#CVE-2026-98432`, `#patch management`

---

<a id="item-tech-news-4"></a>
### [Cloudflare 称定向 DNS 区域构建将延迟减半、内存降 85%](https://blog.cloudflare.com/dns-targeted-zone-builds/) ⭐️ 7.0/10

Cloudflare 工程博客介绍了一种“定向 DNS 区域构建”方法，称其将构建延迟减半，并把内存占用降低 85%。这是一项针对 DNS 区域构建流程的性能与内存优化，而非新产品发布或协议变更；上述数字来自 Cloudflare 的自述，目前缺少独立复现。对运行大规模 DNS 基础设施的团队而言，关键问题是这些收益能否在自身变更模式下成立。

hackernews · wondersky · 11月2日 14:47 · [社区讨论](https://news.ycombinator.com/item?id=50337558)

**「背景：此前的全量重建方式」** 此前，Cloudflare 的 DNS 区域在任何设置变更时都会触发整区重建，即使该区域拥有数千万条记录，因此单次改动的代价随区域规模线性上升。据 Cloudflare 工程博客介绍，新的做法是用规划器挑选“最小安全构建”范围，只重建发生变化的部分，并配合统一调度；其报告的整区重建次数下降约 40%，92.95% 的构建不再触发完整重建。

**「社区讨论」** 评论中有人称赞 Cloudflare 的技术博客质量，也有人质疑每秒 700 次变更对其规模是否偏低；另有读者关心这类改动长期会引入哪些缺陷，并讨论在内存紧缺背景下优化内存占用的投入回报。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/dns-targeted-zone-builds/">How we halved DNS build delay and cut memory use by 85%</a></li>
<li><a href="https://daily.dev/posts/how-we-halved-dns-build-delay-and-cut-memory-use-by-85--jhnmypmtx">How we halved DNS build delay and cut memory use by 85%</a></li>

</ul>
</details>

**标签**: `#DNS`, `#performance optimization`, `#memory efficiency`, `#systems engineering`, `#Cloudflare`

---

<a id="item-tech-news-5"></a>
### [LightMIS：131K 参数医学分割模型](https://www.reddit.com/r/MachineLearning/comments/1xm8dbo/lightmis_ultralightweight_medical_image/) ⭐️ 7.0/10

LightMIS 作者发布了一个面向 2D 二值医学图像分割的超轻量模型：它仅有 131K 参数，直接聚合多尺度编码器特征，不使用逐阶段学习的解码器。作者称，在 nnU-Net v2.3.1 的统一训练和评估协议下，该模型覆盖六个数据集和五种成像模态，其模态宏平均 Dice 和 IoU 与 nnWNet 接近，同时参数少 98.14%、GFLOPs 少 94.58%。在 Arm Mali-G52 MC2 GPU 上，完整 LightMIS 的推理速度约为 nnWNet 的 10.5 倍，所有变体均实现 100% GPU 算子覆盖、无 CPU 回退；论文、代码和检查点已公开，但这些对比仍是作者报告、尚未独立验证。

reddit · r/MachineLearning · /u/OkLion2068 · 11月2日 20:22

**「背景」** nnU-Net 是医学图像分割中广泛使用的自配置框架，会依据数据自动确定预处理、网络配置和训练流程，因此常被用作统一实验协议下的比较基线。LightMIS 的作者也在 nnU-Net v2.3.1 下从零训练各模型，并在同一协议下与参考模型 nnWNet 比较，使参数、计算量和精度差异处于相对可控的评测环境中。

**「影响」** 对需要在 Mali-G52 级边缘设备上部署分割模型的开发者，公开的代码、检查点和复现说明提供了可直接测试的基线；但在采用前，应自行复核跨六个数据集的 Dice/IoU 以及 10.5 倍速度结论，因为目前证据来自作者实验，并非独立评测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hal.science/hal-04903826v1/document">Adapted nnU - Net : A Robust Baseline for Cross-Modality Synthesis...</a></li>
<li><a href="https://www.emergentmind.com/topics/nnu-net-segmentation-model">nnU - Net : Self-Configuring Segmentation</a></li>

</ul>
</details>

**标签**: `#medical image segmentation`, `#lightweight models`, `#edge AI`, `#model efficiency`, `#nnU-Net`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [LLM 直接读写权重并非超人类研究](https://seangoedecke.com/llms-are-not-superhuman-at-reading-and-writing-neural-network-weights/) ⭐️ 7.0/10

rss · Sean Goedecke · 11月3日 00:00

**「背景」** 近期一篇论文称，前沿 LLM（文中称 GPT-6 Astra）能直接读取并修改神经网络权重：从一个小网络的权重识别它被训练来玩什么游戏，还通过原生编辑 0.8B Qwen 的权重提升数学能力。作者认为这看似“超人类”，甚至引发递归自我改进的联想，但实际上并没有那么神奇。

**「方案」** 作者逐一拆解了这些结果。识别游戏之所以可行，是因为小网络的输入通道直接对应 8×8 网格的每个格子，且通道带有“智能体”“移动物体”等标签；只需对第一层 32 个权重按通道取 L2 范数，三行 Python 就能画出热图，人看热图也能认出 Breakout 的底部横线或 Pac-Man 的迷宫。Astra 不执行代码而在“脑内”算范数，作者承认这是超人的心算，但不是超人的 AI 研究。更受关注的 Qwen 案例也不是它原本“不会数学”：模型在 32k 个 token 后陷入循环，超过该长度的问题必然失败，而 32k 以内原本都能解。作者说自己会采用 steering/abliteration 式做法：准备循环与不循环的推理文本，比较残差差异，测量各权重贡献并削减高贡献权重；Astra 正是用四对文本做了类似的事，找到阻止循环的补丁，使模型能处理超过 32k 个 token 的数学题。作者因此把直接改权重类比为 LLM 生成机器码或修改编译后的二进制：技巧很酷，但处理二进制仍应写源代码再编译，更新模型权重的最佳方式仍是正常训练。

**「启示」** 作者的结论是，LLM 直接读写权重是一项令人印象深刻的技巧，而非会改变 AI 研究范式的全新能力；智能 LLM 对 AI 研究的真正帮助，应体现在改进训练，而不是魔法般地直接微调权重。

**标签**: `#model interpretability`, `#weight editing`, `#LLM capabilities`, `#ablation`, `#AI research claims`

---

<a id="item-tech-blog-2"></a>
### [受众捕获：当代理指标悄悄替换你的目标](https://seangoedecke.com/audience-capture/) ⭐️ 7.0/10

rss · Sean Goedecke · 11月3日 00:00

**「背景」** 肖恩·戈德克自称有一副“工程师的灵魂”：看到互动量这类指标就想把它做大，而网络写作环境恰好提供了全套便利工具——流量来源随手可查、聚合算法推送最讨喜的文章、平台按互动量付钱。但他认为，把精力放在这些数字上是错误的方向。

**「方案」** 浏览量、点赞和评论只是他真正在乎之事的代理指标：让有见识的人读到并思考他的观点、收到有实际经验的读者反馈、建立谨慎思考者的声誉。一万个人点开文章扫一眼就关掉，与在 Hacker News 上只读标题却留下评论的“点击者”一样，同认真阅读的“读者”几乎不重叠，而指标无法区分二者。他举例说，若“微服务很蠢”这类热点文章带来流量，他便继续写同类内容，数字攀升，认真的读者却悄然流失——看似成功，实则以点击者和嘲讽者替换了原受众。作者把这个框架延伸到工程职业：博客浏览量、漂亮的 Jira 工单指标属于代理游戏，而赢得你尊重的人的尊重、做自己引以为傲的技术工作才是真实游戏，区别在于你是否真的在乎该游戏的目标。为真实游戏而在代理游戏中妥协（比如为了孩子上好学校去讨好不喜欢的人）是健康可取的，最糟的是出于惯性地出卖自己，在换不来任何想要之物的地方让步。因此他坚持写那约 5% 会认真读、思考并来信的读者所喜欢的文章，宁可依赖自己的品味和稀薄的高质量反馈。

**「启示」** 指标本身不是敌人，关键在于清楚自己真正想玩哪个游戏；可以有意识地“出卖”一点以换取真正在乎的东西，但绝不能习惯性地在毫无回报处妥协。

**标签**: `#audience capture`, `#proxy metrics`, `#engineering career`, `#online writing`, `#engagement metrics`

---