---
layout: default
title: "Horizon Summary: 2026-11-08 (ZH)"
date: 2026-11-08
lang: zh
---

> 从 18 条内容中筛选出 5 条重要资讯。

---

**科技新闻**
1. [MaxxBench 检验 DeepSWE 分数稳健性：小模型跌幅最大](#item-tech-news-1) ⭐️ 8.0/10
2. [内蒙古 800MW 风电 AI 数据中心探访：一年建成 120MW](#item-tech-news-2) ⭐️ 8.0/10
3. [Coldframe：伪装超市冷柜控制器的 Python 蜜罐](#item-tech-news-3) ⭐️ 7.0/10
4. [研究称每台 Mac 内置未公开的亲友关系分类与知识图谱](#item-tech-news-4) ⭐️ 7.0/10
5. [Asahi Linux 第 7.3 期进展报告：Fedora 45 同日发布](#item-tech-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [MaxxBench 检验 DeepSWE 分数稳健性：小模型跌幅最大](https://maxxbench.unlap.ai/research/why-maxxbench/) ⭐️ 8.0/10

MaxxBench 的一项分析检验 DeepSWE 基准分数在任务说明被扰动后是否仍然成立，结论是较小模型的表现下降最明显。该分析关注分数能否泛化，而不是某次榜单排名，因此对依赖 DeepSWE 评估模型能力的读者直接相关。由于来源未提供具体扰动方法、模型清单或数值，这一结论应视为该分析的报告，而非独立复现结果。

hackernews · antiuniverse · 11月7日 17:19 · [社区讨论](https://news.ycombinator.com/item?id=50406222)

**「背景：DeepSWE 与基准有效性检验」** DeepSWE 是面向编码智能体的长程软件工程基准：任务覆盖 91 个代码仓库、5 种语言，并配有手写验证器，用来检验程序行为而非实现细节（tool-1-1、tool-1-2）。MaxxBench 这次做的是基准有效性检验，它在任务本质不变的情况下改动任务规格，再看分数变化有多大，以此判断分数反映的是可泛化的能力，还是对特定表述方式的拟合。

**「影响」** 对使用 DeepSWE 做选型的团队来说，单一总分可能掩盖模型对任务说明措辞的敏感度；在比较小模型时，应把改变任务说明后的复测结果与原始分数一起看，而不是只按榜单分数下结论。

**「社区讨论」** 评论者 kqr 认为，MaxxBench 通过改变任务说明来检验泛化是值得采用的默认做法，并提到自己在私有基准中看到较弱模型的失败未必是答案错误。peri-cl 指出图中跌幅主要集中在带“-flash”的模型和 OpenAI Luna，但提醒 GLM-5.3 与 GLM-5.3-flash 属于不同谱系；Systemerror7A69 则称 DeepSWE 存在多个 bug，并据此对基准可信度更悲观，rao-v 更倾向于把问题归因于实验室构建的 RL 环境不够多样，而非直接照 benchmark 训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepswe.datacurve.ai/">DeepSWE measures frontier coding agents on original, long-horizon...</a></li>
<li><a href="https://deepswe.lol/">DeepSWE — Long-Horizon Software Engineering Benchmark</a></li>

</ul>
</details>

**标签**: `#LLM benchmarks`, `#evaluation methodology`, `#model generalization`, `#AI research`, `#benchmark validity`

---

<a id="item-tech-news-2"></a>
### [内蒙古 800MW 风电 AI 数据中心探访：一年建成 120MW](https://newsletter.semianalysis.com/p/we-visited-chinas-stargate-in-inner) ⭐️ 8.0/10

SemiAnalysis 的实地探访报道记录了中国内蒙古一个由风电供电的大型 AI 数据中心园区：园区规划容量为 800MW，其中 120MW 在一年内建成。报道还称，园区包含一个 5MW 的 SST 原生 800V 直流供电试点，以及不设中央冷水机组的冷却设计。该文属于现场观察与技术分析，并未给出这些方案的长期运行效率、可用性或独立测量结果，因此 800V 直流和免中央冷机设计仍应按试点与设计特征看待。

rss · Semianalysis · 11月7日 19:01

**「背景」** SemiAnalysis 的实地报道探访的是位于内蒙古乌兰察布的 Galaxy 园区，并称该地区是中国增长最快的 AI 数据中心聚集地之一。报道中的 800V DC 试点指在 5MW 规模上采用 SST（固态变压器）原生的 800V 直流配电方案，区别于传统数据中心以交流配电为主的供电链路。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agihunt.info/en/p/1a1b7b3cf36c69b73e277f80a5a">Inside China&#x27;s &#x27;Stargate&#x27;: an 800MW Inner… · AGI Hunt</a></li>
<li><a href="https://explainx.ai/blog/envision-galaxy-campus-wind-powered-ai-data-center-ulanqab-inner-mongolia-2026">Envision Galaxy Campus: Wind AI Site in Inner Mongolia ...</a></li>

</ul>
</details>

**标签**: `#AI data centers`, `#data center power`, `#data center cooling`, `#800V DC`, `#China tech`

---

<a id="item-tech-news-3"></a>
### [Coldframe：伪装超市冷柜控制器的 Python 蜜罐](https://github.com/hedgerow-dev/coldframe) ⭐️ 7.0/10

Coldframe 是一个用单个 Python 文件写成、仅依赖标准库的开源蜜罐，伪装成 Danfoss AK-SM 800A 和 Dixell XWEB 超市制冷控制器。作者称其按 Shodan 上的真实设备记录校准了 HTTP 头顺序、页面标题、证书字段和 TLS 版本，Dixell 页面被填充到精确的 8,202 字节，两个实例被 Shodan 识别为真实设备而非蜜罐。它能识别 CVE-2025-41450（Danfoss“每日代码”登录绕过）并记录提交的代码当天是否正确，还会标记针对另外三个 Danfoss CVE 和 XWEB 漏洞的尝试。项目上线一天的两个实例目前只看到通用扫描器和 Shodan 爬虫 refrigerator.census.shodan.io。

hackernews · hedgerow-dev · 11月7日 17:27 · [社区讨论](https://news.ycombinator.com/item?id=50406292)

**「背景」** CVE-2025-41450 是 Danfoss AK-SM 8xxA 系列 4.2 之前版本中的身份验证绕过漏洞（CVSS 8.2），Danfoss 安全公告建议安装 4.2 版补丁。Coldframe 冒充的 AK-SM 800A 属于该系列，因此它针对“code of the day”登录绕过的识别，对应的是一个已有公开编号和修复版本的漏洞。

**「影响」** 对工业控制系统安全研究者和防守方，这意味着不必拿到实体控制器，也能在标准库环境中观察对方通过默认登录进入假仪表盘后的第二阶段行为，并收集针对上述 Danfoss/XWEB 漏洞的探测记录。蜜罐本身不提供修补或阻断能力，真实冷柜控制器的安全仍需由厂商、安装商或运营方另行处理。

**「社区讨论」** 评论中，supriyo-biswas 质疑用 Shodan 记录校准设备指纹的可靠性，称许多联网设备本身可能就是蜜罐或已被入侵、页面遭替换，并建议拿一台真实漏洞设备来探测。xrd 则追问所谓大规模冷柜被黑是否有定论，指出也有人认为那可能只是大量设备同时收到软件更新；这些都属于评论者提出的质疑，而非已证实结论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/dsa-2025-03-01/">DSA-2025-03-01 | Danfoss</a></li>
<li><a href="https://nvd.nist.gov/vuln/detail/cve-2025-41450">NVD-CVE-2025-41450</a></li>

</ul>
</details>

**标签**: `#honeypot`, `#ICS security`, `#industrial control systems`, `#Python`, `#open source`

---

<a id="item-tech-news-4"></a>
### [研究称每台 Mac 内置未公开的亲友关系分类与知识图谱](https://8rank.ai/game/apple-intelligence-personal-knowledge-graph) ⭐️ 7.0/10

一篇逆向工程研究文章称，自 2022 年起出厂的每台 Mac 都运行着一对未公开的系统守护进程，用途是构建关于用户及其身边人的个人知识图谱，记录用户是谁、认识谁、这些人与用户彼此之间的关系，以及用户与谁沟通、去哪里、做什么、何时做。作者 infwhispers 在 Hacker News 评论区确认自己为该研究作者，并给出后续研究的链接；文章把这些组件归入 Apple Intelligence，同时提出技术与隐私层面的疑问。由于除推送摘要外没有源内容，守护进程名称、文件路径、数据留存方式以及能否关闭等关键细节均未出现，上述说法目前只是该研究的单方面描述，未经独立验证。

hackernews · infwhispers · 11月7日 09:46 · [社区讨论](https://news.ycombinator.com/item?id=50403097)

**「背景」** 个人知识图谱是把联系人、关系、地点和通信记录组织成可供模型查询的结构化网络，为设备端个性化功能提供上下文。此次被调查的是 macOS 中一对未公开说明、负责构建该图谱的守护进程；文章给出的影响范围是 macOS 13 及以上，Intel 和 Apple 芯片 Mac 均包括在内。

**「影响」** 直接后果是，这部分关系数据由未写入公开文档的系统组件在本地生成，用户无法从 Apple 的公开资料中得知系统到底记录了哪些关系，也无从判断如何查看、导出或关闭该能力；因此讨论焦点落在知情同意与可审计性，而非单纯的“是否上传云端”。

**「社区讨论」** 评论者 elgertam 表示并不意外，因为照片应用早已掌握用户亲友乃至宠物的姓名与面孔；aetherspawn 认为这类上下文是本地模型解析“给 James 发消息”“告诉老板我明天不来了”所必需的，否则无法确定指代对象。thomascountz 则从社会层面提出异议：如果交谈内容都会被记住，人际对话赖以成立的那种“不会被记住”的默契就被打破了。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://8rank.ai/game/apple-intelligence-personal-knowledge-graph">Anatomy of Apple &#x27;s Personal Knowledge Graph — Eighth Rank</a></li>

</ul>
</details>

**标签**: `#Apple Intelligence`, `#macOS privacy`, `#personal knowledge graph`, `#reverse engineering`, `#on-device AI`

---

<a id="item-tech-news-5"></a>
### [Asahi Linux 第 7.3 期进展报告：Fedora 45 同日发布](https://asahilinux.org/2026/11/progress-report-7-3/) ⭐️ 7.0/10

Asahi Linux 发布第 7.3 期进展报告，称 Fedora Linux 45 于 11 月 3 日发布当天同步推出 Fedora Asahi Remix，这是项目首次做到与上游 Fedora 同日发布。报告还谈及宽松许可被试图利用的治理与许可担忧，并指出 Linux 在 Apple Silicon 上的硬件支持仍有缺口。

hackernews · ackyshake · 11月7日 05:20 · [社区讨论](https://news.ycombinator.com/item?id=50401867)

**「背景」** Asahi Linux 是为 Apple Silicon（M 系列芯片）Mac 提供 Linux 支持的社区项目，其面向用户的发行版 Fedora Asahi Remix 基于上游 Fedora 构建。该项目过去的 Remix 版本发布通常落后于上游 Fedora 的节奏，而本次进度报告称，Fedora Linux 45 于 11 月 3 日发布当天，Remix 便同步推出，这是首次做到与上游同日发布。

**「影响」** 对 Fedora Asahi Remix 用户而言，最直接的变化是 Fedora 45 发布当日就有对应版本可跟进，不必等待项目另行追赶；但硬件支持限制仍在，升级或安装前应核对自己的 Mac 型号和外设需求。

**「社区讨论」** 评论中，一名用户把 USB-C 外接显示器支持列为暂不安装 Asahi 的主要障碍，并质疑为何新 CPU 支持优先级更高；另一名用户追问报告所称“许可被利用”是否指 Omarchy，但该猜测未获证实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://asahilinux.org/2026/11/progress-report-7-3/">Progress Report: Linux 7.3 - Asahi Linux</a></li>

</ul>
</details>

**标签**: `#Asahi Linux`, `#Apple Silicon`, `#Linux`, `#Fedora`, `#open source`

---