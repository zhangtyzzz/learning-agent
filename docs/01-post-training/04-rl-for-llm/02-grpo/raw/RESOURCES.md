# 原始资料 · GRPO 推导

> 用法：index.md 是蒸馏版；出处定位如下。

## 必读

| # | 资料 | 定位 | 看什么 |
|---|---|---|---|
| 1 | DeepSeekMath | arXiv 2402.03300 | §4.1.4 GRPO 全部（公式 14-16）：组相对 advantage 的原始定义 |
| 2 | RLOO | arXiv 2402.14740 | §2 leave-one-out 推导（两页），与 GRPO 对照读 |

## 可选

| 资料 | 定位 | 看什么 |
|---|---|---|
| DeepSeek-R1 | arXiv 2501.12948 | §4 GRPO 的 RLVR 用法（规则奖励模板） |
| verl `core_algos.py` | https://github.com/volcengine/verl | 工业实现：组归一化的 batch 化写法（P3 实践前读） |

## 精读要点

- DeepSeekMath 的 GRPO 是在「GSM8K 有监督→RL 提升」上验证的：注意其 reward 只有一个正确性信号 + 少量格式约束，朴素到惊人
- 「组内归一化让 reward 的绝对尺度无关」——这是 RLVR 兼容任意 0/1 规则奖励的隐含前提，也是 std 偏置问题的来源
