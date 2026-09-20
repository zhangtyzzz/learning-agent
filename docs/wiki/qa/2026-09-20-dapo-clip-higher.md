---
question: DAPO 的 clip-higher 为什么能防熵坍缩？
date: 2026-09-20
tags: [RL, GRPO变体, DAPO, 熵]
sources: ["01-post-training/04-rl-for-llm/03-grpo-variants/index.md", "arXiv 2503.14476"]
---
## 结论（3 行内）

标准 PPO/GRPO 的 clip 是对称的 (1±ε)：低概率 token 即使是好动作，其重要性比 ρ 很快顶到上限 1+ε，梯度被封死，永远「抬不起来」→ 策略分布越来越尖 → 熵坍缩、探索消失。DAPO 把上界放宽为 ε_high > ε_low，给低概率好 token 留出被推高的通道。

## 论据

- 推高一个 token 的概率需要多次更新；对称 clip 下每次更新只允许 ρ 增长到 1+ε（如 1.2），而压低方向用 1−ε，同样的更新次数下「变确定」比「保持多样」快得多——训练天然偏向坍缩。
- DAPO 论文的消融：去掉 clip-higher 后训练后期熵快速跌向 0，采样多样性丧失；加上后熵曲线平稳。
- 日常对应的体检指标：训练中监控策略熵 / 不同回答的多样性；熵骤降 = 该把 ε_high 调大（如 ε=0.2 → ε_high=0.28）。

## 开放问题

- clip-higher 与 KL 正则（对 π_ref）同时存在时，谁主导熵的动态？两者是否冗余？（待在 P3 实验里消融）

## 回链

- 课程：[04-rl-for-llm · 变体地图](../../01-post-training/04-rl-for-llm/03-grpo-variants/index.md)
- 相关概念：熵坍缩、探索-利用、DAPO
