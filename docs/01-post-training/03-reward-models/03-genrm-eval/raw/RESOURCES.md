# 原始资料 · GenRM 与评测

> 用法：index.md 是蒸馏版；出处定位如下。

## 必读

| # | 资料 | 定位 | 看什么 |
|---|---|---|---|
| 1 | Generative Verifiers | arXiv 2408.15240 | §1-2：验证即生成、CoT-Critic 与 soft 判据的构造 |
| 2 | ProcessBench | arXiv 2412.06559 | §2 错误定位任务定义 + §4 各家 PRM/GenRM 的定位准确率差距 |

## 可选

| 资料 | 定位 | 看什么 |
|---|---|---|
| RewardBench | arXiv 2403.13787 | 数据构造（分桶负例怎么造），做内部评测集的模板 |
| Math-Shepherd §4 | arXiv 2312.08935 | PRM 在 BoN 上的端到端收益数据 |

## 精读要点

- GenRM 论文里「评语被 prompt 引导」的现象值得注意：验证会被「提示怎么验证」操纵——judge 也能被 prompt hack
- ProcessBench 公开集中强模型零样本定位已超过不少训出来的 PRM：先建强基线，再决定要不要训
