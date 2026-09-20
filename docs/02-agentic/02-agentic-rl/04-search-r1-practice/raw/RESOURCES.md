# 原始资料 · Search-R1 复现

> 用法：动手手册的资料入口。

## 必读

| # | 资料 | 定位 |
|---|---|---|
| 1 | Search-R1 | arXiv 2503.09516 —— §3 记号、§4 训练细节、附录超参 |
| 2 | Search-R1 官方仓库 | GitHub 搜「Search-R1」—— 多轮 rollout 与 mask 的实现 |
| 3 | verl 文档 | https://verl.readthedocs.io —— multi-turn rollout 支持 |

## 可选

| 资料 | 看什么 |
|---|---|
| R1-Searcher / ReSearch | 搜标题——同路线的平行复现，超参对照 |
| NQ / HotpotQA 数据卡 | 数据口径与去污染注意点 |

## 精读要点

- 复现报告的共识坑：检索结果很长导致上下文爆炸——各家做法不同（截断/摘要/只取摘要句），Search-R1 的选择要读代码确认，别信记忆
- 「搜索次数」是比奖励曲线更早报警的指标：奖励可 hacking，轮数统计很难撒谎
