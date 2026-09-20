# 原始资料 · MDP 与价值函数

> 用法：本讲 index.md 是蒸馏版。想验证推导细节或深挖时，按下面的定位去查原文。
> 链接如失效，直接搜标题。

## 必读（按顺序）

| # | 资料 | 定位 | 看什么 |
|---|---|---|---|
| 1 | OpenAI Spinning Up · [RL intro](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html) | 免费在线，半小时 | 「The RL Problem」「Agent-Environment Loop」「Rewards」三小节，与本讲第 1-2 节对应 |
| 2 | Sutton & Barto《Reinforcement Learning: An Introduction》2nd（[官方免费 PDF](http://incompleteideas.net/book/the-book-2nd.html)） | §3.1-3.5 | MDP 五元组、return、折扣的形式化定义；§3.3 例子可跳 |
| 3 | Spinning Up · [Kinds of RL Algorithms](https://spinningup.openai.com/en/latest/spinningup/rl_intro2.html) | 免费在线 | 「模型 free vs model-based」与本讲 TIP 呼应，5 分钟扫一遍 |

## 可选深入

| 资料 | 定位 | 看什么 |
|---|---|---|
| Hugging Face [Deep RL Course](https://huggingface.co/learn/deep-rl-course/en/unit0/introduction) Unit 1-2 | 免费在线 | 想要多练手时的补充；Q-learning 部分可跳过（非本课程主线） |

## 精读要点（对照本讲）

- Bellman 方程在书里是「期望」形式；工程实现全是**采样近似**（蒙特卡洛 / TD）——这是「教科书→代码」最大的鸿沟
- LLM RL 里 $s$ 是**越来越长的序列**：这一句话解释了为什么后面所有方法都在跟「上下文长度、注意力开销」搏斗
