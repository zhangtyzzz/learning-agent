---
question: 用 LLM judge 给 GRPO 组内排名，能否解决全对/全错零梯度问题？
date: 2026-09-20
tags: [RL, GRPO, 奖励设计, reward-hacking, DAPO]
sources: ["01-post-training/04-rl-for-llm/02-grpo/index.md", "01-post-training/02-preference-alignment/04-rlaif-reward-hacking/index.md", "arXiv 2503.14476"]
---
## 结论（3 行内）

不能。全对/全错的本质是「组内无真实差异」，零梯度是奖励在诚实报告无信息量。LLM judge 排名确实能制造差异，但制造的是假差异（opinion + 噪声 + 偏差），等于把 reward hacking 的入口重新打开；无信息组的正确处理是丢弃重采（DAPO dynamic sampling）。

## 论据

- **噪声不可复现**：同一组让 judge 重排，名次会变 → advantage 混入不可复现噪声，训练方差增大。
- **偏差被放大**：judge 的长度/流畅/自我偏好偏差，随训练迭代逐步固化进策略（Goodhart 曲线的机制）。
- **信息论视角**：全错组的真实含义是「没有任何一条包含可学习的相对优劣」——这不是分辨率不足，是信号不存在。
- **打破平局的正确姿势**（有依据的差异）：格式奖励（真实属性，小权重）、PRM 步骤分（测量过程）、MC rollout 步骤价值（统计估计）；以及从源头调任务难度分布（WebRL 式课程）让组内天然混合对错。
- **何时 judge 排名才合理**：主观任务（写作/客服）没有验证器可用时——即 RLAIF / Self-Rewarding 路线，代价是闭环质量 ≤ judge 质量，必须定期人评校准。

## 开放问题

- judge 分数作为「软信号」（如取结论 token 概率）而非硬排名，能否在主观任务上降低噪声？→ 待读 GenRM 相关实证。

## 回链

- [04-rl-for-llm · GRPO](../../01-post-training/04-rl-for-llm/02-grpo/index.md)（四病灶之③）
- [04-rl-for-llm · 变体地图](../../01-post-training/04-rl-for-llm/03-grpo-variants/index.md)（DAPO 动态采样）
- [偏好对齐 · RLAIF 与 Reward Hacking](../../01-post-training/02-preference-alignment/04-rlaif-reward-hacking/index.md)（Goodhart 曲线）
- [Agent · 多智能体 · 自我改进闭环](../../02-agentic/04-multi-agent/01-self-improvement-loop/index.md)（闭环质量 ≤ 评估质量）
