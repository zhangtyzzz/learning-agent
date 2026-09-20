# 原始资料 · RLVR 与 verl

> 用法：index.md 是蒸馏版；出处定位如下。

## 必读

| # | 资料 | 定位 | 看什么 |
|---|---|---|---|
| 1 | DeepSeek-R1 | arXiv 2501.12948 | §4.1 R1-Zero 的奖励模板（RLVR 奖励设计的直接模板） |
| 2 | HybridFlow (verl) | arXiv 2409.19256 | §3 架构：两引擎与控制器抽象（读代码前的地图） |
| 3 | verl 仓库 GSM8K GRPO example | https://github.com/volcengine/verl | P3 实践的入口脚本与配置 |

## 可选

| 资料 | 定位 | 看什么 |
|---|---|---|
| OpenRLHF | arXiv 2405.11143 | 另一架构路线（Ray actor 编排） |
| TRL 文档 · GRPOTrainer | https://huggingface.co/docs/trl | 单卡小规模替代方案 |

## 精读要点

- R1 的奖励函数朴素到只有「答案对 + 格式对」，与其学复杂的 reward shaping，不如把验证器做严
- verl 论文里「混合控制器」的一节解释了为什么不用纯 Ray/纯 SPMD——理解这个设计取舍，评估任何 RL 框架都有了坐标系
