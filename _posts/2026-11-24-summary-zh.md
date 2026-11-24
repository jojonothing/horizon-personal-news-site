---
layout: default
title: "Horizon Summary: 2026-11-24 (ZH)"
date: 2026-11-24
lang: zh
---

> 从 16 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [Z.ai 发布 GLM-5.4，首次采用循环 Transformer](#item-tech-news-1) ⭐️ 8.0/10
2. [Ladybird 浏览器发布首个 alpha 版](#item-tech-news-2) ⭐️ 8.0/10

**科技博客**
1. [vLLM 插件实现 ERNIE 5.5 Flash Preview 首日支持](#item-tech-blog-1) ⭐️ 6.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Z.ai 发布 GLM-5.4，首次采用循环 Transformer](https://z.ai/blog/glm-5.4) ⭐️ 8.0/10

中国实验室 Z.ai 发布 GLM-5.4，称这是其首个采用循环 Transformer 架构的模型：一组共享权重的层在一次前向传播中重复运行多次，以前一次的输出继续细化隐藏状态，从而在不增加参数量的情况下加深网络，目标是提升通用编程能力。该模型目前未提供开放权重；据试用者 Simon Willison 报告，GLM-5.4 也不能通过常规 Z.ai API 套餐访问，他需订阅 Coding Plan 才能取得可调用该模型的密钥，而 Coding Plan 与常规 API 共用位于 https://api.z.ai/api/v1 的 OpenAI 兼容 Responses API。Willison 还用“骑自行车的鹈鹕”绘图做了非正式比较，称 5.4 与 5.3 的生成质量相近，但未给出可验证的基准结果；上述架构与能力说法目前尚无独立验证。

hackernews · foohis · 11月23日 10:06 · [社区讨论](https://news.ycombinator.com/item?id=50609685)

**「技术背景」** 常规 Transformer 的每一层在一次前向计算中只运行一次；循环 Transformer 则让一组共享权重的层连续执行多轮，反复精化隐藏状态，从而在不增加参数量的前提下提升网络的有效深度。据 Z.ai 公布的架构细节，GLM-5.4 并非从头训练，而是在沿用 GLM-5 基础模型的前提下，对其中 28 层应用循环、连续执行两次，实际参数约 7500 亿，厂商据此声称其智能水平相当于 2 万亿至 3 万亿参数的模型。这一架构路线近期并非孤例：Thinking Machines Lab 于 11 月 20 日发布的 Inkling 2 Mini 同样采用循环 Transformer，对中间层每个 token 运行三次，并称这能让模型用更少 token 完成智能体编程等推理密集型任务。

**「对开发者的实际影响」** 目前要调用 GLM-5.4，用户必须先订阅 Z.ai 的 Coding Plan，因为常规 API 套餐和 OpenRouter 都还不能访问该模型，并且它也未以开放权重形式发布。Coding Plan 提供的 API key 与常规 key 行为一致，都走同一个 OpenAI 兼容 Responses API（https://api.z.ai/api/v1），所以现有接入代码基本可以复用；但第三方工具仍需适配新模型名，例如 llm-zai 插件目前尚不支持 5.4，测试者不得不另写 llm-glm 插件才能调用。

**「社区讨论」** 有评论者称赞 Zhipu 披露了较多架构细节，认为这比一些西方公司的封闭做法更透明，并把循环 Transformer 视为前沿模型的一个明显方向，尽管仍有问题待解决。另一名用户则抱怨部分中国模型的“马拉松式思考”会在简单任务上反复自我怀疑，导致完成时间明显长于前沿模型，并推测这与基准测试策略有关；这些均属个人体验和推测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://z.ai/blog/glm-5.4">GLM-5.4: Toward Generalized Coding with Our First Loop ...</a></li>
<li><a href="https://www.gate.com/news/detail/zhipu-glm-54-reuses-28-layer-foundation-with-loop-transformer-claims-2-3-25808864">Zhipu GLM-5.4 Reuses 28-Layer Foundation with Loop ...</a></li>

</ul>
</details>

**标签**: `#LLMs`, `#model release`, `#looped transformers`, `#coding models`, `#Zhipu GLM`

---

<a id="item-tech-news-2"></a>
### [Ladybird 浏览器发布首个 alpha 版](https://ladybird.org/posts/alpha/) ⭐️ 8.0/10

Ladybird 项目发布了其从零构建的浏览器的首个 alpha 版，macOS 和 Linux 用户现在可以直接下载安装，无需自行编译。该项目仍使用 HarfBuzz、Skia、ffmpeg 和 SQLite 等少数外部组件，其余核心部分（HTML 解析、CSS 引擎、布局、JavaScript、WebAssembly）为自行实现。官方说明这是 alpha 版，部分网站无法使用且偶尔会崩溃；试用者报告多数网站渲染正常，但也遇到滚动卡顿，以及 Datasette Lite 因缺少 navigator.serviceWorker.startMessages 而无法运行。

hackernews · janvdberg · 11月23日 16:13 · [社区讨论](https://news.ycombinator.com/item?id=50614249)

**「背景」** Ladybird 起源于 SerenityOS 项目，其浏览器引擎的多数核心组件——HTML 解析、CSS、布局、JavaScript 和 WebAssembly——均由项目自行实现，只有文本整形、2D 图形、视频和 SQLite 等少数部分依赖 HarfBuzz、Skia、ffmpeg 与 SQLite 等外部库。在本次 alpha 之前，用户需要自行编译源码才能试用，因此首个可安装版本是把长期开发转为可分发产品的节点。

**「实际影响」** 对希望尝鲜的 macOS 和 Linux 用户，alpha 版提供了可直接安装的构建，但官方提醒部分网站无法使用且可能崩溃；遇到坏站可在浏览器内报告，崩溃后可选择是否发送报告。对 Web 开发者而言，Service Worker 等 API 仍有缺口——Datasette Lite 的失败表明依赖这些接口的应用需要先验证兼容性。

**「社区讨论」** 试用者称多数网站渲染正确，有人表示 NoVNC 在 Ladybird 中比 Firefox 更流畅，但也有人指出页面滚动略显卡顿。评论还争论该项目改用 SQLite、Skia 等成熟库是否偏离早期自研组件的黑客精神，并有人呼吁从设计上加强反指纹与权限控制。

**标签**: `#browser engine`, `#open source`, `#Ladybird`, `#web standards`, `#software release`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [vLLM 插件实现 ERNIE 5.5 Flash Preview 首日支持](https://vllm.ai/blog/2026-11-24-ernie-5-5-flash-preview) ⭐️ 6.0/10

rss · vLLM Blog · 11月24日 00:00

**「背景」** ERNIE 5.5 Flash Preview 是 280B 总参数、每 token 激活 14B 的稀疏 MoE 模型，支持 1M token 上下文、思考与工具调用；新架构和长上下文使推理成本成为核心约束，vLLM 以插件在发布日支持它。

**「方案」** 作者的核心做法是发布独立 vLLM-ERNIE 插件而非 fork：在同一环境安装官方 vllm==0.32.0 和插件后，vLLM 经 vllm.general\_plugins 自动发现，并按架构名懒加载模型代码。插件含模型代码和融合 kernel：VHA 跨头混合、Multi-Router Latent MoE、MultiMax 输出头等被预折叠或合并，作者报告单 kernel 快 1.55×–6.53×，部分结果与未融合实现按位一致。FlashIndexer 用小型路由器按 token 选择稀疏索引头并做阈值预过滤，作者称 1M 上下文有 1.4× 加速；默认检查点将路由专家量化为 MXFP4（W4A8，经 QAT），其余权重与 KV cache 用 FP8。DSpark 是随权重发布的 3 层 MoE 草稿模型，每步最多提议 7 个 token，作者报告真实编程与 Agent 负载上平均接受长度超过 4.0；服务侧支持注意力数据并行加专家并行、TP2/4/8 张量并行、Mooncake PD 分离与 KV cache CPU 卸载。这些数字未附基准方法，应视为作者报告。

**「启示」** 文章最终说明，把模型代码和专用 kernel 放在插件层，可在不等待 vLLM 主干合并的情况下让新模型发布日获得端到端加速；但性能声明仍需独立基准验证。

**标签**: `#LLM inference`, `#vLLM plugins`, `#kernel fusion`, `#quantization`, `#speculative decoding`

---