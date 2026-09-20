# 03 · 实践线（Practice）

> 原则：**每个算法点都配一个最小可跑的实现**。看懂 ≠ 会，跑通并改动过才算。
> 所有实验记录放本目录（notebooks / mini-impl / reproduction），每个实验一个子文件夹，内含 README 记录动机-设置-结果-结论。

## 实践总表

| # | 实践 | 对应学习阶段 | 放哪 | 交付物 / 验收 |
|---|---|---|---|---|
| P1 | SFT 小模型（TRL 或 LLaMA-Factory） | Phase 1 Week 1-2 | `notebooks/p1-sft/` | loss 曲线 + 训练前后 10 例对比 |
| P2 | 手写 mini-DPO（~200 行，不借 TRL loss） | Phase 1 Week 3 | `mini-impl/p2-mini-dpo/` | 代码 + margin/KL 曲线 + 前后对比 |
| P3 | verl 跑 GRPO on GSM8K + 源码走读笔记 | Phase 1 Week 5-6 | `reproduction/p3-verl-grpo/` | reward 曲线 + `core_algos` 逐行注释笔记 |
| P4 | mini-R1 countdown 复现（TinyZero 风格） | Phase 2 | `reproduction/p4-mini-r1/` | 响应长度/涌现行为实验记录 |
| P5 | Search-R1 风格多轮工具 RL | Phase 3 Week 2-3 | `reproduction/p5-search-r1/` | multi-turn mask 细节笔记 + 曲线 + 消融 |
| P6 | 训 RM/PRM + Best-of-N 评估 | Phase 1 Week 4 | `notebooks/p6-rm-bon/` | BoN vs greedy 的 N-准确率曲线 |

## 环境

- 模型档位：0.5B / 1.5B / 3B（Qwen2.5 或 SmolLM 系），单卡 24GB 可跑（LoRA + gradient checkpointing）；P3-P5 建议有 40GB+ 或多卡更从容
- 框架：TRL（P1/P2 参照）、verl（P3/P4/P5 主力）、LLaMA-Factory（快速 SFT）、vLLM（rollout）
- 没有本地卡：Colab/Kaggle/公司资源，实践不可省

## 实验记录规范

每个实验目录一个 README.md，固定五段：

```markdown
# P3 · verl GRPO on GSM8K
## 动机        （对应 ROADMAP 哪个知识点）
## 设置        （模型/数据/超参/硬件，能复现的程度）
## 结果        （关键曲线截图 + 3 条以内的观察）
## 结论        （验证/推翻了什么预期）
## 下一步      （一个具体的消融或改进）
```

## 已知坑位清单（随实践补充）

- SFT 忘记 prompt masking → loss 虚低
- DPO 的 ref model 显存翻倍 → 用 LoRA 的冻结侧或 adapter 共享
- GRPO 全对/全错组零梯度 → 动态采样（DAPO）
- rollout 与训练引擎 logprob 数值不一致 → fp32 重算 / tolerances
- 多轮 RL 的截断策略悄悄改变任务分布
