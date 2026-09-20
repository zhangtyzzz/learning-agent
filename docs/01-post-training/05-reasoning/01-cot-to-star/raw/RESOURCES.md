# 原始资料 · 前史：CoT 到 STaR

> 用法：index.md 是蒸馏版；出处定位如下。

## 必读

| # | 资料 | 定位 | 看什么 |
|---|---|---|---|
| 1 | CoT | arXiv 2201.11903 | 只看 §1-2 与 few-shot 例子（10 分钟，知道原点即可） |
| 2 | STaR | arXiv 2203.14465 | §2 两个机制（RFT 与 rationalization）+ Fig.1 流程 |
| 3 | Self-Consistency | arXiv 2203.11171 | 只看方法一节（采样-投票） |

## 可选

| 资料 | 定位 | 看什么 |
|---|---|---|
| Quiet-STaR | arXiv 2403.09629 | 引言与 Fig.1（token 级思考的思想实验） |
| RFT 论文（Yuan et al.） | 搜「Scaling Relationship RFT」 | 「推理路径数 vs 提升」的定量关系 |

## 精读要点

- STaR 论文 2022 年就用了「hint 挽回」，与 R1 蒸馏数据、拒绝采样思想一脉相承——经典论文的 idea 半衰期很长
- Self-Consistency 的成本-收益可以立刻在你业务上验证（不用训练）：先测它，再谈训练
