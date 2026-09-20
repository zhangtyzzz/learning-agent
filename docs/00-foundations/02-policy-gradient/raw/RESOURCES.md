# 原始资料 · 策略梯度

> 用法：index.md 是蒸馏版。下面是原始出处与精读定位。

## 必读

| # | 资料 | 定位 | 看什么 |
|---|---|---|---|
| 1 | Spinning Up · [Deriving PG](https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html) | 免费在线 | 官方版「策略梯度定理」推导，与本讲第 2 节公式对齐 |
| 2 | Sutton & Barto（[免费 PDF](http://incompleteideas.net/book/the-book-2nd.html)） | §13.1-13.4 | REINFORCE 与 baseline 的定理陈述；13.3 「为什么 baseline 不引入偏差」 |
| 3 | Schulman et al. [GAE 论文](https://arxiv.org/abs/1506.02438)（High-Dimensional Continuous Control Using GAE） | arXiv 1506.02438 | 只读 §3（GAE 的 δ 递推与 λ 的偏差-方差图）；引言可跳 |

## 可选深入

| 资料 | 定位 | 看什么 |
|---|---|---|
| Lilian Weng 博客《Policy Gradient Algorithms》 | https://lilianweng.github.io （站内搜标题） | 事后梳理全家族的地图册，本讲吃透后再读，查漏 |
| RLOO 论文 (Back to Basics) | arXiv 2402.14740 §2 | leave-one-out baseline 的两页推导，直接服务 GRPO |

## 精读要点（对照本讲）

- 策略梯度定理的证明关键只有一步：$\nabla \pi = \pi \nabla \log \pi$（log-derivative trick），别被篇幅吓到
- 采样的「轨迹间独立性」是方差大的根源之一；LLM 里同 prompt 采 N 条组内对比（RLOO/GRPO）就是在压这个方差
- GAE 论文里那张 λ-偏差方差权衡图值得手抄一遍
