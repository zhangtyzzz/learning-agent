# 原始资料 · ORM vs PRM

> 用法：index.md 是蒸馏版；出处定位如下。

## 必读

| # | 资料 | 定位 | 看什么 |
|---|---|---|---|
| 1 | Let's Verify Step by Step | arXiv 2305.20050 | §1-2（ORM/PRM 定义与结论）+ Fig.3（BoN 对比曲线） |
| 2 | Math-Shepherd | arXiv 2312.08935 | §3.1：MC rollout 自动标注算法（本讲流程图的原文） |

## 可选

| 资料 | 定位 | 看什么 |
|---|---|---|
| OmegaPRM（MCTS 改进标注） | 搜标题 | 二分搜索式 rollout，降标注成本的后续 |
| PRM800K 数据集 | OpenAI 官方发布 | 人工逐步标注长什么样（吃过苦头才知道自动标注多值） |

## 精读要点

- Let's Verify 的实验设置里有个易漏点：PRM 的收益在「大 N 的 BoN」下最明显——小 N 下 ORM 未必输
- Math-Shepherd 的价值估计和地基课 GAE/MC 回报的关系：同一套蒙特卡洛思想，从「估状态价值」搬到「标过程数据」
