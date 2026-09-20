---
question: 实践中真有人用 LLM judge 当 GRPO 的奖励源吗？是怎么做的？
date: 2026-09-20
tags: [RL, GRPO, agentic-RL, LLM-as-judge, 奖励设计]
sources: ["02-agentic/02-agentic-rl/01-four-challenges/index.md", "01-post-training/04-rl-for-llm/02-grpo/index.md", "arXiv 2411.02337 (WebRL)"]
---
## 结论（3 行内）

有，且是 agentic RL 主流做法之一：GRPO 对奖励来源无感知，judge 只是奖励源。实践分四形态，可靠性递减：**判成败**（封闭问题，≈验证器）＞ judge 造偏好对训 RM ＞ 组内 pairwise win-rate ＞ 直接绝对打分。关键不是「用不用 judge」，而是 judge 被问的问题有多封闭。

## 四种形态

| 形态 | 做法 | 代表 | 风险 |
|---|---|---|---|
| ① 判成败 | 强模型对照任务描述回答「成功了吗」→ 0/1 | WebRL（GPT-4o ORM）、GUI agent 系列、DeepSeek 后期 GenRM | 表演式完成（骗 judge），要求看环境终态 |
| ② 造偏好对→训RM→打分 | judge 只做 pairwise，RM 缓冲噪声 | Self-Rewarding 路线的 GRPO 化 | RM 固化 judge 偏差，但比直连稳 |
| ③ 组内两两比较 | 组内 C(G,2) 比较，win-rate 当分数 | BT 归一化式做法 | 成本 O(G²)；比绝对打分稳 |
| ④ 直接打分 1-10 | judge 每条给分当 r_i | 早期/快速原型 | 尺度漂移、噪声直入 advantage、文风 hacking |

## 关键机理

- **组内归一化天然免疫共同偏差**：judge 对整组「都偏松」，减均值后消掉；真正致命的是**区分错误**（该排前的排后）。所以 judge 优化的目标是「区分对」，不是「分准」。
- **与上一问（全对全错）的统一**：可验证任务上 judge 排名制造假差异 = 危险；不可验证任务上 judge 是唯一奖励源 = 必要。判据是「judge 的问题是否封闭可核实」。
- **成本结构**：judge 每条轨迹一次调用，比训 RM 便宜、比验证器贵；通常选比被训模型强的模型当 judge，且注意自我偏好。

## 回链

- [Agentic RL · 四大难题](../../02-agentic/02-agentic-rl/01-four-challenges/index.md)（难题②奖励设计）
- [GRPO](../../01-post-training/04-rl-for-llm/02-grpo/index.md)、[LLM judge 排名与零梯度](2026-09-20-llm-judge-grpo-zero-gradient.md)（姊妹篇）
- [RLAIF 与 Reward Hacking](../../01-post-training/02-preference-alignment/04-rlaif-reward-hacking/index.md)
