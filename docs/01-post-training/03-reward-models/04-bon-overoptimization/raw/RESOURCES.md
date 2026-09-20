# 原始资料 · Best-of-N 与过度优化

> 用法：index.md 是蒸馏版；出处定位如下。

## 必读

| # | 资料 | 定位 | 看什么 |
|---|---|---|---|
| 1 | Let's Verify §4 | arXiv 2305.20050 | BoN-N 曲线的实证形态（本讲曲线图的数据来源风格） |
| 2 | Scaling Laws for RM Overoptimization | arXiv 2210.10760 | 全文：gold/proxy 曲线 + RM 规模对拐点的影响 |

## 可选

| 资料 | 定位 | 看什么 |
|---|---|---|
| Math-Shepherd §4.2 | arXiv 2312.08935 | PRM 版 BoN 的收益数据 |
| 「Inference Scaling Laws」（Wu et al.） | 搜标题 | BoN/束搜索的推理算力-收益定量刻画 |

## 精读要点

- Overoptimization 论文的「KL 预算」读法：横轴不是步数而是 KL，意思是「偏离多少后开始变坏」——这把 BoN 与 RL 统一到一个坐标系
- 自己业务做 BoN 体检时固定：采样温度、N 序列（1/4/16/64）、RM 版本，三个变量一次只动一个
