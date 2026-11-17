---
layout: default
title: "Horizon Summary: 2026-11-17 (ZH)"
date: 2026-11-17
lang: zh
---

> 从 23 条内容中筛选出 6 条重要资讯。

---

**科技新闻**
1. [vLLM v0.34.0 默认启用可扩展 KV 缓存并移除 V1](#item-tech-news-1) ⭐️ 8.0/10
2. [Jiff 1.0 发布：Rust 日期时间库](#item-tech-news-2) ⭐️ 8.0/10
3. [卡内基梅隆 CS Learn 免费上线 YouTube](#item-tech-news-3) ⭐️ 7.0/10
4. [Windows 11 被指收集开发工具与编码代理遥测数据](#item-tech-news-4) ⭐️ 7.0/10
5. [Optimizely 被曝入侵，经 Zoom、GitLab 等客户站点传播恶意代码](#item-tech-news-5) ⭐️ 7.0/10
6. [Marimba：单次冻结编码器回答多类语音问题](#item-tech-news-6) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [vLLM v0.34.0 默认启用可扩展 KV 缓存并移除 V1](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 8.0/10

vLLM 发布 v0.34.0，包含来自 412 名贡献者的 1,061 个提交，并新增 Mistral Large 4、MiniMax-M3.1-Flash、Nemotron-3.5-Transcribe 等 10 个模型。该版本默认启用可扩展 KV 缓存：在 CUDA 和 ROCm 上按预热与 CUDA 图捕获后实际可用显存确定缓存大小，发布说明举例称 MiniMax-M3 在 H200 上由 433k 增至 672k tokens，但部分模型在并发 128 时 TPOT 可能上升 6–18%。同时 Model Runner V1 被移除，V2 成为唯一 GPU runner；发布说明还报告 GB200 上最高 1.95 倍 decode、GLM-5.3-Flash 1.6 倍吞吐等测试结果。升级还涉及默认 block size 从 16 改为 64、仅提供 ROCm 10.0 制品以及要求 huggingface\_hub &gt;= 2.0.0 等破坏性变更。

github · khluu · 11月16日 23:22

**「背景」** vLLM 是开源的大模型推理引擎，其 GPU 执行路径此前同时存在 Model Runner V1 与 V2 两套实现；KV cache 容量主要依据显存比例估算预留，默认块大小（block size）为 16，ROCm 侧仍发布 7.2 版本构件。本次升级表列出的破坏性变更正是针对这些旧默认值和旧实现：设置 \`VLLM\_USE\_V2\_MODEL\_RUNNER=0\` 会在启动时失败，需把 V1 的 logits processors 迁移到 \`vllm.v1.worker.gpu.sample.logits\_processor\`，并需改用 ROCm 10.0 的 wheel 与镜像。

**「升级影响」** 升级到 v0.34.0 的部署需要先处理破坏性变更：删除 VLLM\_USE\_V2\_MODEL\_RUNNER=0（否则启动失败），如需保留旧的 16 block size 要显式传入 --block-size 16；若不能接受可扩展 KV 缓存带来的延迟权衡，可用 --gpu-memory-utilization 0.9 或 --no-enable-extensible-kv-cache 回退，ROCm 用户则需改用 10.0 的 wheel 和镜像。

**标签**: `#llm-inference`, `#vllm`, `#kv-cache`, `#gpu-performance`, `#release`

---

<a id="item-tech-news-2"></a>
### [Jiff 1.0 发布：Rust 日期时间库](https://burntsushi.net/jiff/) ⭐️ 8.0/10

Jiff 1.0 已发布，这是一个面向 Rust 开发者的日期时间库，作者为 burntsushi。该版本被讨论为处理日期时间相关任务的新选择，社区关注其 API 设计以及能否改善 Rust 生态中长期存在的日期时间处理痛点。由于原始页面内容未提供，关于具体功能、兼容性和迁移路径的细节尚无法从现有材料确认。

hackernews · burntsushi · 11月16日 16:53 · [社区讨论](https://news.ycombinator.com/item?id=50519744)

**「背景」** 日期时间库需要同时处理绝对时间点与带时区的民用时间，还要应对夏令时和日历运算，这是 Rust 生态长期依赖 chrono 等库的背景。一位自称维护 chrono 约五年的评论者表示，chrono 的 API 稳定性既是用户采用它的原因，也让后续改进面临阻力；Jiff 则是由 burntsushi 开发的 Rust 日期时间库。

**「对 Rust 开发者的影响」** 对 Rust 开发者而言，Jiff 1.0 提供了 chrono 之外的又一个日期时间库选项，但并非可直接替换：曾维护 chrono 约五年的 quodlibetor 在评论中表示，用户长期留在 chrono 的重要原因正是其 API 稳定，因此迁移前需要评估两者的 API 差异。对于需要 TAI 之外时间尺度（如 UT1）或同时兼顾微秒级与百万年尺度精度的用户，评论中的相关提问尚未在给定材料中得到回答，采用前应先确认 Jiff 是否覆盖其场景。

**「社区讨论」** 前 chrono 维护者 quodlibetor 表示，自己接手维护正是因为旧 API 不理想，但改进常遭遇对稳定性的抵触，最终因倦怠停止维护，并对 Jiff 的出现表示感激；另有评论者赞赏项目明确说明 Jiff 并非适用于所有场景，还有用户询问其 TAI、UT1 等时间尺度的处理方式。这些是社区观点与提问，不代表对 Jiff 能力的独立验证。

**标签**: `#Rust`, `#datetime library`, `#open source`, `#time zones`, `#software libraries`

---

<a id="item-tech-news-3"></a>
### [卡内基梅隆 CS Learn 免费上线 YouTube](https://www.cs.cmu.edu/learn/) ⭐️ 7.0/10

卡内基梅隆大学已上线 CS Learn，把当前 CMU 计算机科学课程整学期的讲座免费发布到 YouTube，覆盖多个主题。项目负责人、Griffin 计算机科学学院的 Phillip Compeau 表示，本周每天首播一门课程，明年 1 月还会有更多课程。目前发布的内容是课程讲座。

hackernews · pcompeau · 11月16日 20:43 · [社区讨论](https://news.ycombinator.com/item?id=50522980)

**「背景」** 免费公开大学课程讲座本身并非新做法：CS Learn 负责人 Phillip Compeau 在讨论中承认，MIT 的开放课程资源比这早了约 25 年。CMU 此前也已运营面向高中的免费在线交互式计算机科学课程 CS Academy，包含教师培训和在线教材；此次 CS Learn 的不同之处在于直接发布本校当前课程的完整学期讲座。

**「影响」** 对想系统学习计算机科学的人来说，可以直接观看 CMU 课程教师讲授的完整学期内容，无需付费；但仅有讲座时，练习、项目和反馈仍需另行寻找，学习效果取决于自学者能否补上这部分。

**「社区讨论」** 评论者肯定基础学习的价值，认为把 fundamentals 学扎实后，AI 才会成为强有力的工具；也有人提醒仅有讲座不够，项目、幻灯片和反馈同样关键，并提到课程资料将在后续推出。还有 CMU 校友点名期待 15-259 概率与计算和 Tianqi Chen 的机器学习系统等课程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=hztO5vaBTRs">Demonstration of Carnegie Mellon CS Academy - YouTube</a></li>

</ul>
</details>

**标签**: `#CS education`, `#online courses`, `#Carnegie Mellon`, `#machine learning systems`, `#open educational resources`

---

<a id="item-tech-news-4"></a>
### [Windows 11 被指收集开发工具与编码代理遥测数据](https://xusheng.dev/posts/windows-coding-agent-telemetry/) ⭐️ 7.0/10

一篇发布在 Hacker News 的开发者分析称，Windows 11 会收集用户运行哪些编码代理和开发工具的信息，并可能在启用“可选诊断数据”时上传；讨论中有人指出该选项默认开启。用户可在“设置 → 隐私和安全性 → 诊断和反馈”中关闭相关选项。由于没有原始文章正文可供核对，具体收集范围和默认状态仍应视为文章及讨论中的主张，而非独立验证的结果。

hackernews · cwaffles · 11月16日 22:58 · [社区讨论](https://news.ycombinator.com/item?id=50524736)

**「背景」** Windows 11 的诊断遥测分为两级：一部分为维持系统运行所需的必需诊断数据，另一部分是可选的诊断数据，后者可在「设置 → 隐私和安全性 → 诊断和反馈」中通过关闭「发送可选诊断数据」来停用（tool-1-3）。因此，围绕「遥测是否收集开发者工具信息」的争论，关键前提在于这些信息被归入哪一级数据；文中所述的可关闭部分正是可选诊断数据，而非强制上报的必需数据（tool-1-2）。

**「默认开启的诊断数据要求开发者手动关闭」** 按这篇分析的说法，在 Windows 11 上运行 AI 编码代理和开发工具的开发者，其工具使用情况会随默认开启的诊断数据一并上报，而非由用户主动选择分享；若不想上报，需要手动进入“设置 → 隐私和安全性 → 诊断和反馈”关闭诊断数据，不能只依赖默认配置。

**「社区讨论」** 评论者对隐私与平台需求的看法不一：有人称若主要使用 Web 服务，迁移到 Linux 大约一周即可适应，单机游戏大多可用但多人游戏仍有问题；也有人认为 Windows 缺少成熟的 AI 代理沙箱，MXC 才在 10 月 7 日推出且 Claude Code 尚未支持，因此非侵入式遥测有助于确定功能优先级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/techtips/enable-or-disable-windows-telemetry/">How to Enable or Disable Telemetry in Windows 11 - GeeksforGeeks</a></li>
<li><a href="https://wccftech.com/how-to/disable-the-telemetry-on-windows-11-and-stop-microsoft-from-logging-your-data/">How to Disable Telemetry on Windows 11 and Protect Data Privacy</a></li>

</ul>
</details>

**标签**: `#windows-telemetry`, `#privacy`, `#ai-coding-agents`, `#developer-tools`, `#linux-migration`

---

<a id="item-tech-news-5"></a>
### [Optimizely 被曝入侵，经 Zoom、GitLab 等客户站点传播恶意代码](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/) ⭐️ 7.0/10

据安全博客 Report-URI 报道，第三方网站优化与脚本供应商 Optimizely 遭入侵，攻击者通过包括 Zoom、GitLab 在内的客户站点投放恶意代码。现有信息将事件归类为 Web 供应链攻击，受影响的是嵌入 Optimizely 脚本的网站及其访客。目前公开信息未说明攻击者如何获得跨客户写入权限，也未给出完整受影响名单、恶意代码细节或根因。

hackernews · kristjansson · 11月16日 23:00 · [社区讨论](https://news.ycombinator.com/item?id=50524767)

**「背景」** Optimizely 是第三方实验与个性化平台，客户通过在其网页中嵌入 Optimizely 脚本，让该平台下发并执行测试或功能配置代码。因此，一旦供应商下发的 JavaScript 被篡改，恶意代码就会在加载该脚本的客户站点访问者浏览器中执行，形成波及多家站点的 Web 供应链风险。

**「影响」** 对使用 Optimizely 脚本的网站而言，这意味着页面安全边界延伸到了第三方供应商：供应商脚本一旦被篡改，站点仅靠自身的代码审查无法阻止恶意代码在访客浏览器中执行。相关团队需要审计该脚本的加载范围和权限，并把供应商的发布与访问控制纳入风险管理。

**「社区讨论」** 评论中有人批评 Google Tag Manager 这类让市场团队绕过工程直接添加标签的做法，认为它造成了臃肿的第三方 JavaScript，应借此重新评估；也有人认为 Optimizely 和大型站点缺乏发布冷却、分阶段上线等问责机制。另有评论引用原文称这不是 CDN 缓存投毒、Optimizely 自有站点也受影响，并有人建议用 NoScript 降低暴露面。

**标签**: `#supply-chain-security`, `#web-security`, `#third-party-scripts`, `#malware`, `#Optimizely`

---

<a id="item-tech-news-6"></a>
### [Marimba：单次冻结编码器回答多类语音问题](https://www.reddit.com/r/MachineLearning/comments/1xxsqro/marimba_a_system_one_model_for_speech_r/) ⭐️ 7.0/10

Marimba 提出对每个 8 秒音频窗口只运行一次冻结的 Qwen3-ASR-0.6B 编码器，再用类型化问题（是/否、选项或分数）输出经过校准的概率，覆盖词项、语言、话轮结束、说话人变化与人数。作者在 Reddit 报告中称，在同一组 1,000 道公开问题上，它在 9 项测试中的 6 项匹配或超过 30B-A3B 的 Qwen3-Omni，但在 Speech Commands 上仍落后；语言 ID 在 300 个 FLEURS 片段上达到 100%，说话人变化在 AMI 和 VoxConverse 上 AUROC 为 0.966–0.980。作者同时说明话轮结束读出器在 Smart Turn 数据上训练，因此该行只对其自身是分布内结果；它在 Smart Turn 自身测试集上以 0.930 对 0.982 落后于 Smart Turn v3.2，在 ICSI 会议上为 0.716 对 0.712，基本持平。对未见任务并不泛化：在 CochlScene 场景分类上所有头都只有随机水平；代码、Apache-2.0 权重、演示和 pip 包已发布。

reddit · r/MachineLearning · /u/solanotodesch · 11月16日 15:47

**「背景」** Qwen3-ASR-0.6B 是语音识别模型，通常只负责把音频转写成文本；Qwen3-Omni 这类音频语言模型则用更大的统一模型处理多种音频任务。Marimba 的做法是复用前者的冻结编码器表示，并在单次前向之上接轻量读出层，从而不必为每个问题重新运行大模型。该帖也是作者上周预告之后的论文版发布。

**「影响」** 希望复用 ASR 编码器的开发者可通过 pip install marimba-audio 和 Apache-2.0 权重直接试验多任务读出；但由于话轮结束结果受训练数据分布影响，且模型不泛化到未见任务，部署前应在目标音频域重测，不能把公开基准当作通用保证。

**标签**: `#speech recognition`, `#audio language models`, `#model efficiency`, `#calibration`, `#speaker diarization`

---