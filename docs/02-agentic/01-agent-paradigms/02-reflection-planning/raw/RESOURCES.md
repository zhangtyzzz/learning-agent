# 原始资料 · 反思与规划

> 用法：index.md 是蒸馏版；出处定位如下。

## 必读

| # | 资料 | 定位 | 看什么 |
|---|---|---|---|
| 1 | Reflexion | arXiv 2303.11366 | §2 三组件（actor/evaluator/self-reflection）+ Fig.2 循环 |
| 2 | Tree of Thoughts | arXiv 2305.10601 | §3 两种搜索策略（BFS/DFS）与「评估器提示」设计 |

## 可选

| 资料 | 定位 | 看什么 |
|---|---|---|
| Self-Refine | 搜标题 | 自我修正的极简版（无外部反馈） |
| 推理模型对照实验 | 搜「o1 vs ToT/Reflexion」 | 内化后 scaffold 增益缩小的实证 |

## 精读要点

- Reflexion 的 evaluator 可以是任何信号（单元测试/编译/启发式）——「执行反馈优先」在 2023 年论文里已是明确结论
- ToT 论文的任务（Game of 24）刻意选了「一次性生成几乎不可能解对」的题：评估每条 ToT 论文任务是否同样极端，是判断其现实收益的关键
