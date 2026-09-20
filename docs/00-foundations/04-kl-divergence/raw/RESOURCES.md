# 原始资料 · KL 散度

> 用法：index.md 是蒸馏版。下面是原始出处与精读定位。

## 必读

| # | 资料 | 定位 | 看什么 |
|---|---|---|---|
| 1 | Schulman 博客《Approximating KL Divergence》 | 搜标题（John Schulman, 2020） | k3 估计器的原始出处，2 页，把三种估计（k1/k2/k3）的方差讲透 |
| 2 | InstructGPT 论文 | arXiv 2203.02155 | App. C.2「PPO 每步的 KL 惩罚」：token 级实现与 β 选取的第一手描述 |
| 3 | RLHF Book（Nathan Lambert） | https://rlhfbook.com KL 罚章节 | 系统性梳理 KL 在 RLHF 的各个出场位置，中文读者友好 |

## 可选深入

| 资料 | 定位 | 看什么 |
|---|---|---|
| Minka《Divergence measures and message passing》 | 网上搜标题（Microsoft Research 技术报告） | 正/反向 KL 几何直觉（mode covering vs seeking）的经典出处，只看前 5 页图 |
| TRL 文档 · KL 配置 | https://huggingface.co/docs/trl | 查工程默认值（β、estimator、target-KL 自适应）时用 |

## 精读要点（对照本讲）

- k3 的推导只有三行（Jensen 不等式放缩），值得亲手推一遍——面试常考「为什么不用 logr 直接当 KL」
- 反向 KL 在 RL 里的好处（宁可保守）与本课程 PPO/GRPO 的稳定性直接相关：DPO 家族改成正/反讨论时（如 KTO）再回来看这张图
- 工程 bug 高发区：KL 罚加在 reward 上 vs 加在 loss 上，两者等价性只在特定条件下成立，读框架源码时留意注释
