---
layout: default
title: "Horizon Summary: 2026-11-14 (ZH)"
date: 2026-11-14
lang: zh
---

> 从 19 条内容中筛选出 1 条重要资讯。

---

**科技新闻**
1. [TorchTitan 在 384 块 GH200 上训练 1T MoE](#item-tech-news-1) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [TorchTitan 在 384 块 GH200 上训练 1T MoE](https://www.reddit.com/r/MachineLearning/comments/1xvce5h/scaling_to_1t_moe_on_torchtitan_p/) ⭐️ 8.0/10

一份实践者报告称，其团队与 TorchTitan、PyTorch 维护者合作，在 JUPITER 超算的 384 块 GH200 上把约 1T 参数 MoE 的训练吞吐提升到每 GPU 约 1,300 tokens/s，较起点快 14 倍。报告称起步时单步耗时 84 秒，其中 68 秒耗在节点间网络等待上；团队采用 384 路 FSDP 加 4 路专家并行（EP 严格限制在节点内），并用全量激活检查点、将检查点卸载到 Grace、以 Muon 替代 Adam 等方式把序列长度推到 64k tokens。报告还列举了按完整专家分片以避免 Muon 的 Newton-Schulz 跨节点通信、把专家梯度归约改为 bf16 all-to-all 并在本地以 fp32 累加，以及修复缓存分配器侧流占用显存等优化。上述数字来自实践者自述，而非独立基准测试。

reddit · r/MachineLearning · /u/f14-bertolotti · 11月13日 16:28

**「背景」** MoE 把部分前馈层拆成多个专家，训练时需要在 GPU 间路由 token；FSDP 则把每层权重切片到所有 rank，并在计算前即时汇聚。GH200 的节点内 NVLink 与 Grace-Hopper C2C 链路带宽远高于 JUPITER 的节点间 InfiniBand（报告给出的每 GPU 约 25 GB/s），因此如何分片以及减少跨节点通信成为这类训练的核心约束。

**「影响」** 对在 Hopper 集群上训练大 MoE 的团队，这份报告给出的直接可复用项包括：用 FlexShard 按完整专家分片以在本地执行 Newton-Schulz、把专家梯度归约改为 bf16 all-to-all 后本地 fp32 累加，以及避免在 FSDP 侧流上分配大块临时缓冲；其中 GPU 上的 Newton-Schulz 修复已贡献到 TorchTitan，相关 FSDP2 开关正在被推进为公开 API。

**标签**: `#large-scale training`, `#Mixture-of-Experts`, `#TorchTitan`, `#distributed training`, `#PyTorch`

---