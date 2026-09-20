# 第 3 讲 · DPO 变体家族：都在补同一块短板

> [!NOTE]
> ⏱ 30 分钟 ｜ 前置：[第 2 讲 DPO 推导](../02-dpo-derivation/index.md) ｜ 下一讲：[04 · RLAIF 与 Reward Hacking](../04-rlaif-reward-hacking/index.md)
> 🔤 卡在符号？→ [符号速查表](../../../00-foundations/symbol-reference.md)
>
> 学完你能回答：**IPO/KTO/SimPO/ORPO 各自改了 DPO 的哪一项、为了解决什么？**

---

## 1. 一张图看懂：家族树

| 变体 | 改动的「部位」 | 一句话动机 |
|---|---|---|
| DPO（基线） | — | 离线偏好优化 |
| IPO | 损失形状 | 修「在偏好对上过拟合」 |
| KTO | 数据形态 | 只要 👍/👎，不要成对 |
| SimPO | 去掉 π_ref | 省一半显存，长度归一防偏 |
| ORPO | 融进 SFT | 一阶段完成 SFT+偏好 |

## 2. 逐个看 diff（都对着 DPO 公式改）

**DPO 基线**：$\mathcal{L} = -\log \sigma\Big(\beta \big[\underbrace{\log \tfrac{\pi(y_w)}{\pi_{ref}(y_w)}}_{l_w} - \underbrace{\log \tfrac{\pi(y_l)}{\pi_{ref}(y_l)}}_{l_l}\big]\Big)$

| 变体 | 公式改动 | 解决什么 | 代价 |
|---|---|---|---|
| IPO | sigmoid 换平方：$(l_w - l_l - \tfrac{1}{2\beta})^2$ | DPO 在偏好对上 loss 可压到 0 → 过拟合；IPO 目标不可完全满足 → 持续正则 | 收敛更慢 |
| KTO | 拆成 👍 与 👎 两个独立项（前景理论：亏的权重更大） | 成对数据贵且难维护；线上只有单个回答的打分 | 信息量略降 |
| SimPO | 去掉 $\pi_{ref}$；$l$ 改为**长度归一**的 log 概率；加 margin $\gamma$：$(\tilde{l}_w - \tilde{l}_l \ge \gamma)$ | 省掉 ref 模型；长度归一防「越长分越高」 | 对超参更敏感 |
| ORPO | odds ratio 惩罚项直接加进 SFT 损失 | 一步到位，无需先 SFT 再对齐 | 与 SFT 耦合，不好单独调 |

> [!IMPORTANT]
> 变体共同的靶子是上一讲的结论：**DPO 是离线的、且 loss 可被「背答案」压到零**。
> 理解顺序建议：先用熟 DPO，遇到具体症状再换药——过拟合 → IPO；只有 👍👎 数据 → KTO；显存紧张 → SimPO；想省阶段 → ORPO。

## 3. 对你的工作意味着什么

- 选型速查：**默认 DPO** → 症状驱动升级；所有变体的评估方式与 DPO 相同（隐式奖励曲线 + 人评）
- KTO 特别适合业务：线上反馈天然是单点 👍/👎（用户点赞/采纳），不用专门造对
- 警惕「变体玄学」：论文间的收益差异常在噪声内，**在你自己的数据上做 A/B 才算数**

## 4. 自测

<details markdown="1"><summary>① DPO 过拟合的机制，IPO 怎么修？</summary>
DPO 的 sigmoid loss 在 l_w − l_l → ∞ 时趋于 0，模型可以无限拉开差距（背数据）。IPO 把目标改成不可满足的回归形式（差值收敛到有限目标），持续提供正则梯度。
</details>

<details markdown="1"><summary>② SimPO 去掉 π_ref 后靠什么防跑偏？</summary>
长度归一化消除「长度偏好」这条最容易被钻的空子 + margin 强制一个明确的偏好间隔。但 KL 约束确实没了，所以更依赖数据质量与早停。
</details>

<details markdown="1"><summary>③ 把 KTO 的直觉翻译成中文。</summary>
「被点赞的回答，推高其概率；被点踩的，压低其概率；且压低的力度更大（损失厌恶）」。
</details>

## 5. 原始资料

见 [raw/RESOURCES.md](raw/RESOURCES.md)。
