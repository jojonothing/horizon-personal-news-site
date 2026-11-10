---
layout: default
title: "Horizon Summary: 2026-11-10 (ZH)"
date: 2026-11-10
lang: zh
---

> 从 26 条内容中筛选出 6 条重要资讯。

---

**科技新闻**
1. [Google 发布面向 Agent 时代的 TPU 8tx 与 8i Max](#item-tech-news-1) ⭐️ 7.0/10
2. [E-means 宣称以十分之一轮次达到 k-means 聚类效果](#item-tech-news-2) ⭐️ 7.0/10
3. [Show HN：watched.earth 查询卫星过境并调取实拍图像](#item-tech-news-3) ⭐️ 7.0/10
4. [消费者 Gemini 被指将个人文件与邮件送交人工审核](#item-tech-news-4) ⭐️ 7.0/10
5. [用 Claude Code 打造 Beep Locator，多设备定位神秘蜂鸣声](#item-tech-news-5) ⭐️ 7.0/10
6. [LingBot-Touch：用潜空间预测替代重建的触觉预训练](#item-tech-news-6) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Google 发布面向 Agent 时代的 TPU 8tx 与 8i Max](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/) ⭐️ 7.0/10

Google 在官方博客发文，发布两款新张量处理单元：TPU 8tx 与 TPU 8i Max，并将它们定位为面向“agentic 时代”（智能体时代）的加速器。目前可获得的材料只给出了名称与定位，没有披露具体规格、算力数字、功耗、定价、上市时间或与现有型号的对比数据，也没有说明第三方独立测得的性能结果。因此现阶段无法判断这两款芯片相对既有 TPU 或英伟达同类产品有何实际差异。

hackernews · \_benx\_ · 11月9日 21:56 · [社区讨论](https://news.ycombinator.com/item?id=50432831)

**「背景」** 据 Google Cloud 博客，Google 在今年 4 月的 Cloud Next 上已推出同代的 TPU 8t 和 8i，分别面向大规模训练与实时推理，并称两者相较上一代 TPU 分别带来最高 2.7 倍训练性能和 80% 的推理性价比提升。此次的 8tx 与 8i Max 是在这一产品线上的扩展：8tx 面向需要加密和安全处理的 AI 负载，8i Max 面向更高容量推理与大上下文企业应用。

**「社区讨论」** Hacker News 上的评论主要集中在缺失的量化信息：有用户直接追问每款芯片的“瓦特/token”和“美元/token”指标，以及它们与英伟达对应产品的价格性能比较。另有评论指出 Google Colab 上可用的最强 TPU 仍是 v6e-1，对严肃工作而言规模太小，并有人追问 Google 为何不直接对外销售这些芯片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.google.com/blog/topics/ai-infrastructure/tpu-8tx-and-tpu-8i-max">Introducing TPU 8tx and TPU 8i Max | Google Cloud Blog</a></li>
<li><a href="https://www.datacenterknowledge.com/data-center-chips/google-adds-tpu-8tx-8i-max-for-enterprise-ai">Google Adds TPU 8tx, 8i Max for Enterprise AI</a></li>

</ul>
</details>

**标签**: `#Google TPU`, `#AI hardware`, `#datacenter accelerators`, `#agentic AI`, `#cloud infrastructure`

---

<a id="item-tech-news-2"></a>
### [E-means 宣称以十分之一轮次达到 k-means 聚类效果](https://e-means.github.io/) ⭐️ 7.0/10

E-means 项目提出一种 k-means 替代聚类方法，宣称能在约十分之一 epoch（轮次）内取得与 k-means 相当的结果，目标是减少对大型数据集的重复遍历。现有材料没有提供独立基准、实现细节或代码发布状态，因此性能说法仍属项目方主张。HN 评论者则报告了实际试验：有人将其改造用于 GPU 上的 IVF 索引，称获得 146 倍加速；另一人用于索引批量重建，称分片拆分等全量重建快 2.5 倍，但常规增量插入耗时变化不大。

hackernews · porridgeraisin · 11月9日 18:45 · [社区讨论](https://news.ycombinator.com/item?id=50429734)

**「背景」** k-means 的经典实现是 Lloyd 算法：反复把样本分配给最近的质心，再用各簇样本均值更新质心，直到收敛。Meta FAIR 开源的 e-means 被定位为这一经典方法的现代、稳健替代方案；其项目页面以 epoch、CPU 时间和 GPU 时间与 Lloyd&\#x27;s k-means 对比，并声称所需 epoch 约为后者的十分之一。

**「影响」** 对需要全量重聚类或重建索引的系统，评论中的案例显示该方法可能显著加快 GPU IVF 构建和分片拆分后的重建，但它主要替换批量聚类步骤，常规增量写入不一定受益。采用前应在自身数据分布上，与现有 Lloyd&\#x27;s/k-means 实现做对照测试。

**「社区讨论」** 评论者报告了分化明显的结果：real\_faxenoff 称把方法改造到 GPU 上的 IVF 索引后获得 146 倍加速，kingcauchy 称全量重建索引快 2.5 倍但常规增量插入耗时变化不大，而 jlhawn 实测用于球面等面积网格松弛时反而不如 Lloyd&\#x27;s 算法。shiandow 则从理论上讨论其更新规则可理解为带摩擦项的 EM 或模拟退火，并强调质心保持在凸包内是关键性质。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://e-means.github.io/">Modern optimization and scaling laws for k - means clustering</a></li>

</ul>
</details>

**标签**: `#clustering`, `#k-means`, `#machine-learning-algorithms`, `#performance-optimization`, `#GPU-acceleration`

---

<a id="item-tech-news-3"></a>
### [Show HN：watched.earth 查询卫星过境并调取实拍图像](https://www.watched.earth/) ⭐️ 7.0/10

开发者发布了开源网页工具 watched.earth；用户输入任意地点后，它会在浏览器中根据 CelesTrak 目录，用 SGP4 找出过去 7 天内所有卫星过境，作者称耗时约半秒。工具随后调取这些过境对应的 Sentinel-2、Landsat 和 NASA 实际图像，并且只有在真实图像存在时才标注为“watched”。作者还称，约 1.7 万个在轨目标都由 GPU 逐帧求解开普勒方程绘制，Sentinel-2 时间戳常与实际过境时刻相差 5–10 分钟的问题也已处理。代码已在 GitHub 开源，工具不存储用户位置。

hackernews · a585gupt · 11月9日 17:51 · [社区讨论](https://news.ycombinator.com/item?id=50428907)

**「背景」** 卫星过境查询依赖轨道预报：SGP4 根据 CelesTrak 提供的轨道根数推算卫星在某一时刻的位置，再判断其星下点是否经过目标地点。Sentinel-2 和 Landsat 等对地观测卫星的影像通常公开可用，但要把某次过境与具体影像对应起来，还需要处理拍摄时间与过境时间的偏差。

**「影响」** 对需要核查某地近期卫星影像的用户而言，这一工具把“哪些卫星经过”和“它们拍到了什么”放在同一界面中，并以真实图像存在作为“watched”标记的条件，从而降低把未成像过境误当成已观测结果的风险。

**「社区讨论」** 评论中，地理空间从业者 sixtyj 表示，能直接看到卫星拍摄的具体图像很有用；wnissen 则报告说，用它规划背包旅行比 Copernicus 更方便、覆盖更多。

**标签**: `#satellites`, `#geospatial`, `#orbital-mechanics`, `#web-applications`, `#open-source`

---

<a id="item-tech-news-4"></a>
### [消费者 Gemini 被指将个人文件与邮件送交人工审核](https://github.com/thisisme6598/gemini_files/) ⭐️ 7.0/10

Hacker News 上的一项帖子和项目页面声称，消费者版 Google Gemini 在启用 Connected Apps 后，可能将个人 Drive 文件和 Gmail 邮件交给人工标注者查看；目前提供的材料主要是讨论摘要与评论，未给出可独立核实的细节。评论者补充说，这一范围针对消费者 Gemini，Workspace Gemini 的相关文档仍声称不受人工审核。该帖因此把争议集中在用户授权连接应用后，个人数据是否会被人工查看或用于模型改进。

hackernews · gf74918 · 11月9日 18:24 · [社区讨论](https://news.ycombinator.com/item?id=50429426)

**「背景：Connected Apps 与人工审核机制」** Connected Apps 是 Gemini 应用连接 Gmail、Google Drive 等 Google 应用及第三方服务的机制；用户授权后，Gemini 可调用这些工具读取相应内容。据 Proton 的说明，Gemini Apps Activity 开启时，用户与 Gemini 的交互可能被人工审核、保存最长三年并用于 AI 训练。讨论中的评论还强调，这一人工审核争议针对消费者版 Gemini，Workspace 版 Gemini 仍声称不受同类人工审核约束。

**「对用户的实际影响」** 对于授权了 Connected Apps 的消费级 Gemini 用户，后果是 Gmail、Drive 等个人内容可能进入人工审核流程；而评论区引用的 Google Workspace 管理员文档则称 Workspace 版 Gemini 不受人工审核约束。因此，需要让个人数据避开人工审阅的用户应断开 Connected Apps 授权或改用 Workspace 账号，但第三方事实核查也指出，具体保留与审核范围取决于所适用的是消费级、Workspace 还是 API 条款，用户需按自己的账号类型逐一核对。

**「社区讨论」** 评论中最有用的区分是消费者版 Gemini 与 Workspace Gemini 的适用范围：bri3d 指出 Workspace Gemini 仍声称不受人工审核，而 hek2sch 等人担心启用 Gmail 等连接应用后，数据可能被随机审核者查看或用于训练。rustyhancock 还描述 Gemini 的回答似乎参考了自己收到的邮件，但这属于个人体验，未获独立验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.google.com/gemini/answer/13594961?hl=en">Gemini Apps Privacy Hub - Gemini Apps Help</a></li>
<li><a href="https://proton.me/blog/turn-off-gemini-on-android">Google AI is watching: How to turn off Gemini on Android | Proton</a></li>
<li><a href="https://support.google.com/gemini/answer/13594961?hl=en">Gemini Apps Privacy Hub - Gemini Apps Help</a></li>
<li><a href="https://factually.co/fact-checks/technology/can-signed-out-web-gemini-be-human-reviewed-google-privacy-policy-vs-gemini-apps-abe5cd">Can Gemini Used While Signed Out in a Browser Be Human ...</a></li>

</ul>
</details>

**标签**: `#Google Gemini`, `#data privacy`, `#AI assistants`, `#human annotation`, `#connected apps`

---

<a id="item-tech-news-5"></a>
### [用 Claude Code 打造 Beep Locator，多设备定位神秘蜂鸣声](https://simonwillison.net/2026/Nov/9/mysterious-beeps/) ⭐️ 7.0/10

Simon Willison 用 Claude Code 构建并开源了 Beep Locator：由一台设备运行 Python 服务器，其他手机、平板和笔记本通过浏览器 WebAudio 和 WebSocket 加入，作为分布式麦克风对房间内的间歇蜂鸣进行三角定位。系统让各设备录制包含校准 chirp 的音频片段，并用 FFT 和高通滤波检测蜂鸣；在实际使用中，它把声源定位到约 40 厘米范围内，帮助 Willison 找到一个需要更换电池的旧一氧化碳探测器。Willison 表示，项目最初是在 iPhone 上通过 Claude Code Cloud 配合 Opus 5.5 的 Extra thinking 模式启动的；由于设备之间靠互相播放声音自动定位的效果不佳，后来加入了靠手动拖动图标来标明大致位置的“Rough mode”。

rss · Simon Willison · 11月9日 23:57

**「背景」** 对于间歇性蜂鸣，单靠人耳在堆满箱子的房间里很难判断方向；多麦克风系统可以通过比较同一声音到达各设备的时间差来进行三角定位。该项目的实现参考了 2007 年的论文 BeepBeep，这篇论文利用商用设备的扬声器、麦克风和设备间通信来进行声学测距与定位。

**「影响」** 如果要复现，需要准备多台能访问同一服务器的设备，并允许浏览器使用麦克风；系统会重放各设备录下的片段供用户确认，并在到达时间不符合物理规律时提示可能是回声或另一种声音。

**标签**: `#Claude Code`, `#AI-assisted development`, `#audio triangulation`, `#distributed sensing`, `#open source`

---

<a id="item-tech-news-6"></a>
### [LingBot-Touch：用潜空间预测替代重建的触觉预训练](https://www.reddit.com/r/MachineLearning/comments/1xs05uo/latent_prediction_beats_reconstruction_for/) ⭐️ 7.0/10

Robbyant 发布自监督触觉编码器 LingBot-Touch，采用 JEPA 式做法：预测被掩码接触的潜表示，而不是重建原始传感器信号，并已公开推理代码与检查点。据该帖给出的同数据、同规模对比，触觉到视频的 top-5 召回在 1K 小时数据上为 32.1%（JEPA）、5.6%（MAE）、4.4%（VAE）；到 4K 小时 JEPA 升至 49.3%，MAE 仍低于 9%，VAE 反而降到 3.1%。作者把这归因于触觉片段大部分是接近零的背景，重建损失可以在没学到真实接触信息的情况下下降；上述数字均为作者自述，目前仅见于此 Reddit 帖，尚无独立复现。设计上，掩码比例在 300 步内从 40% 预热到 80%，以避免稀疏信号中接触 taxel 被全部遮蔽而引发梯度爆炸；磁性、压阻、视触觉三类传感器经统一指尖坐标与 5D RoPE（时间、手指、3D 位置）输入同一个共享 Transformer。

reddit · r/MachineLearning · /u/Zealousideal-War7154 · 11月9日 18:52

**「背景」** Robbyant 此前公开的 LingBot 系列以 LingBot-VLA 等具身动作模型为主，LingBot-Touch 则把这一命名延伸到触觉表征学习。JEPA 式预训练让编码器根据可见部分预测被遮挡区域的潜在表征，而不是像 MAE/VAE 那样重建原始传感器信号；触觉数据中接触信号稀疏、背景接近零，因此重建目标可能在尚未学到接触特征时就压低损失。

**「影响」** 对灵巧操作的使用者而言，最直接的含义是冻结的触觉编码器特征可能比微调更划算：在 26 个真实机器人任务、4 种策略构成的 104 个策略-任务组合中，冻结特征在其中 89 个取得最高分；在预训练中从未见过的磁性手上，LingBot-VLA 的成绩从 57.21 提升到 75.04。由于目前只放出推理代码和检查点，训练流程尚不能直接复现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.robbyant.com/">Robbyant - Building One Brain for All Robots</a></li>

</ul>
</details>

**标签**: `#tactile sensing`, `#self-supervised learning`, `#JEPA`, `#dexterous manipulation`, `#representation learning`

---