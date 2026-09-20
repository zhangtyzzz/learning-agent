# 原始资料 · Test-Time Scaling

> 用法：index.md 是蒸馏版；出处定位如下。

## 必读

| # | 资料 | 定位 | 看什么 |
|---|---|---|---|
| 1 | s1: Simple test-time scaling | arXiv 2501.19393 | §2 budget forcing 的两个操作（Wait 延长 / 截止压缩）+ Fig.4 曲线 |
| 2 | rStar-Math | arXiv 2501.04519 | §1-2：MCTS+PRM+自举的总体设计（细节可跳） |

## 可选

| 资料 | 定位 | 看什么 |
|---|---|---|
| Kimi k1.5 | arXiv 2501.12599 | long2short 训练（本讲 overthinking 的解药出处） |
| Inference Scaling Laws（Wu et al.） | 搜标题 | ①②的算力-收益定量刻画 |

## 精读要点

- s1 全文最值得记的是「1k 数据 + budget forcing」能走多远——test-time scaling 的杠杆比想象中大
- rStar-Math 的自举循环（MCTS 造数据 → 训 PRM → 更强搜索）是 AG 模块 self-improvement 的又一原型
