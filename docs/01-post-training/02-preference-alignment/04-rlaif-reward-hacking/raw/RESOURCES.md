# 原始资料 · RLAIF 与 Reward Hacking

> 用法：index.md 是蒸馏版；出处定位如下。

## 必读

| # | 资料 | 定位 | 看什么 |
|---|---|---|---|
| 1 | Constitutional AI | arXiv 2212.08073 | §2（RLAIF 流程）+ 附录 A 的原则清单（写原则的直接模板） |
| 2 | Scaling Laws for RM Overoptimization | arXiv 2210.10760 | 全文短小：KL-性能曲线的形状就是本讲 Goodhart 图的实证来源 |

## 可选

| 资料 | 定位 | 看什么 |
|---|---|---|
| RLAIF：Scaling RL with AI Feedback | 搜标题 | AI 反馈 vs 人类反馈的规模对比 |
| LLM-as-judge 偏差研究 | 搜「Judging LLM-as-a-Judge」 | 位置/长度/自我偏好三大量表偏差 |

## 精读要点

- Gao et al. 的图是「什么时候该停训练」的定量依据：RM 越大越准，same KL 下峰值越高——奖励端的投入直接抬高对齐上限
- 自己业务写 constitution 的建议：从「每周人评发现的 top 失败模式」反推原则，比凭空写更有用
