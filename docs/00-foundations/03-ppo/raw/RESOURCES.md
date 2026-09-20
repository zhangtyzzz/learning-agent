# 原始资料 · PPO

> 用法：index.md 是蒸馏版。下面是原始出处与精读定位。

## 必读

| # | 资料 | 定位 | 看什么 |
|---|---|---|---|
| 1 | PPO 论文 [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347) | arXiv 1707.06347 | 全文只有 8 页：精读 Eq.(6)(7)（clip 目标）+ 实验节的超参表（今天仍在用） |
| 2 | TRPO 论文（Schulman et al. 2015） | arXiv 1502.05477 | 只读 §1 引言 + Fig.1（小步更新的重要性），数学附录可跳 |
| 3 | Spinning Up · [PPO](https://spinningup.openai.com/en/latest/algorithms/ppo.html) | 免费在线 | 官方伪代码页：把 update 循环和本讲第 2 节逐行对上 |

## 可选深入

| 资料 | 定位 | 看什么 |
|---|---|---|
| Hugging Face 博客 [Illustrated RLHF](https://huggingface.co/blog/rlhf) | 免费在线 | 四模型架构的另一种画法 + InstructGPT 背景，配图直观 |
| InstructGPT 论文 | arXiv 2203.02155 §3 | RLHF 三阶段中 PPO 的具体用法（KL 系数、reward 归一化细节） |
| 周志华/机器学习无关；替代：RLHF Book | https://rlhfbook.com | Nathan Lambert 的免费在线书，PPO 章节带伪代码 |

## 精读要点（对照本讲）

- PPO 论文没提 RLHF，原场景是机器人控制——LLM 社区是「拿来主义」后改造的（叠加 KL、token 级展开），读原文时别找 LLM 内容
- clip 的梯度在边界外**不为零但目标不再增长**：精确说法是「目标平坦化」，本讲为了直觉简化为「梯度消失」
- 4 模型架构在 InstructGPT 论文 Fig.2 是标准出处；verl/OpenRLHF 的实现对照着看显存优化（offload、分桶）
