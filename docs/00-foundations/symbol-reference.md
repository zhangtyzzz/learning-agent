# 符号速查表 · 全课程通用

> 读任何一讲卡在符号时查这里。三部分：希腊字母演员表 → 运算记号 → 公式阅读三步法。
> 想要带讲解的版本（每个符号怎么来的、例子）→ [第 0 讲](00-math-prerequisites/index.md)。

## 一、希腊字母演员表（本课程固定身份）

| 符号 | 惯用名 | 固定身份 | 典型出现 |
|---|---|---|---|
| $\pi$ | pi | **策略 policy**（⚠️ 不是圆周率） | $\pi(a\mid s)$：给定状态选动作的概率 |
| $\theta$ | theta | **模型参数**（被训练的东西） | $\pi_\theta$、$\nabla_\theta J$ |
| $\Sigma$ | sigma 大写 | **求和**（全部加起来） | $\sum_a z_a$ |
| $\sigma$ | sigma 小写 | **sigmoid 函数**（分数→概率）⚠️ 与 Σ 无关 | $\sigma(r_w - r_l)$ |
| $\gamma$ | gamma | 折扣因子（未来奖励打几折，0.99~1） | $G_t = r + \gamma G_{t+1}$ |
| $\lambda$ | lambda | GAE 的信任旋钮（0~1） | $\hat A_t = \delta_t + \gamma\lambda \hat A_{t+1}$ |
| $\beta$ | beta | KL 罚的「税率」 | $r - \beta \cdot KL$、DPO 的 β |
| $\epsilon$ | epsilon | clip 容差（常 0.2） | $\text{clip}(r, 1{-}\epsilon, 1{+}\epsilon)$ |
| $\nabla$ | nabla | **梯度**（上升最快方向） | $\nabla_\theta \log \pi$ |
| $\tau$ | tau | 一条**轨迹**（一局完整 episode） | $\tau \sim \pi_\theta$ |

## 二、运算与记号

| 记号 | 怎么读 | 意思 | 迷你例子 |
|---|---|---|---|
| $x_t$ | x 下标 t | 第 t 个 x（**下标 = 编号**） | $a_1, a_2, a_3$ |
| $a'$ | a prime | **另一个/其他的** a（排除当前） | $\sum_{a'}$：对所有其他 token |
| $x^2,\ e^x$ | 上标 | 乘方 / 指数（**上标 = 乘方**） | $e^{z/T}$ |
| 分数 $\frac{A}{B}$ | A 除以 B | 占比、归一化（算份额） | softmax 的整体结构 |
| $\mid$ 竖线 | 「在…条件下」 | 条件 | $\pi(a\mid s)$：给定 s 时 a 的概率 |
| $\sim$ 波浪 | 「服从 / 采自」 | 从分布里抽样 | $x \sim p$、$\tau \sim \pi_\theta$ |
| $\mathbb{E}[\cdot]$ | 期望 | 按概率加权平均 ≈ 采样求平均 | $\mathbb{E}[G]$ |
| $P(A)$ | A 的概率 | 事件概率 | $P(y_w \succ y_l)$ |
| $\succ$ | 「优于」 | 偏好比较（A 比 B 好） | $y_w \succ y_l$ |
| $\arg\max$ | 「让…最大的那个」 | 取最大值时的选项 | $a^* = \arg\max_a Q(s,a)$ |
| $\propto$ | 「正比于」 | 忽略常数倍 | $\nabla J \propto$ 某向量 |
| $:=$ | 「定义为」 | 定义（不是推出） | $V :=$ 平均回报 |
| $\|\,$ 双竖线 | KL 的分隔写法 | $D_{KL}(p\,\|\,q)$：只是习惯写法，**不是绝对值** | 见第 4 讲 |
| $\log$ | 对数 | e 为底；乘法变加法；概率要取 log | $\log \pi$ |
| $\cdot$ 点乘 | 乘号 | 避免和变量 x 混淆 | $p(x)\cdot \log q(x)$ |
| $\hat A$ | 「A hat」 | A 的**估计值**（帽子 = 估计） | $\hat A_t$：优势的估计 |

## 三、公式阅读三步法

1. **先看结构**：等号左边是「要求什么」，右边最外层是「加 / 乘 / 除 / 平均」哪一种。
2. **符号换中文**：Σ→「全部加起来」，分数→「A 除以 B」，E→「平均」，竖线→「在…条件下」，~→「采自」。
3. **代数字算一遍**：找一个小例子代入（本课程每讲都配了数值例子，就是为了这一步）。

> 实战示范：softmax 公式的逐符号拆解见 [第 0 讲第 7 节](00-math-prerequisites/index.md)。
