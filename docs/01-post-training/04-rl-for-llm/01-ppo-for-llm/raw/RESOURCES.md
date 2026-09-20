# 原始资料 · PPO-for-LLM

> 用法：index.md 是蒸馏版；出处定位如下。

## 必读

| # | 资料 | 定位 | 看什么 |
|---|---|---|---|
| 1 | InstructGPT App. C | arXiv 2203.02155 | token 级 KL 罚与 advantage 计算的原始表述 |
| 2 | TRL 文档 · PPOTrainer | https://huggingface.co/docs/trl | 源码级对照：score 与 reward 的区别（KL 加进去之后才叫 reward） |

## 可选

| 资料 | 定位 | 看什么 |
|---|---|---|
| Schulman 博客《Approximating KL Divergence》 | 搜标题 | k3 的出处（地基第 4 讲已给） |
| OpenRLHF 论文 | arXiv 2405.11143 | 工程侧：Ray 分布式下四模型的摆放 |

## 精读要点

- 「KL 加在 reward 还是 loss」各框架不同时期答案不同：读任何代码先确认这一点，否则超参不可迁移
- GAE 的 λ 在 LLM RL 常取 0.95~1.0：回答短、critic 弱时更接近纯 MC（λ=1）
