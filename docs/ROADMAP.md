# ROADMAP · 学习路径

> 目标：从 Agent 工程师 → 掌握 Agent 算法（重点：后训练 / post-training + Agentic RL）。
> 假设投入：每周 10-15 小时；Phase 0-3 约 4-6 个月走完，Phase 4 长期持续。
> 用法：完成一项就把 `[ ]` 改成 `[x]`，并在旁边补上产出物的链接（笔记 / 代码 / 讲稿）。

## 总览

```
Phase 0 地基 ──► Phase 1 后训练主线 ──► Phase 2 推理模型 ──► Phase 3 Agent 算法 ──► Phase 4 前沿(持续)
  1-2 周            4-6 周                 2-3 周              4-6 周
       └──────────── 实践线 P1→P6 与各阶段并行推进 ────────────┘
```

## 「掌握」的定义（每个算法点的过关标准）

写进对应的 concept note，三条都满足才算 🟢：

1. **能推导**：白板写出 objective / loss，并解释每一项为什么存在（比如 PPO 里 clip 和 KL 各自防什么）。
2. **能实现**：读过或写过最小实现，说出工程上最容易踩的 2-3 个坑（如 advantage 归一化、reference model 的显存开销）。
3. **能讲述**：能对没有背景的同事讲 10 分钟，并扛住 3 个追问。

---

## Phase 0 · 地基（1-2 周）

目标：把 RL 和数学的地基补到「能顺畅读懂后训练论文附录」的程度。不用学成 RL 专家。
**已做成 7 讲图文课程**（[00-foundations](00-foundations/README.md)），与下面清单逐条对应，直接开读：

- [ ] 数学基础补丁：期望与采样、softmax/温度、熵与交叉熵、梯度/log/sigmoid → [讲 0](00-foundations/00-math-prerequisites/index.md)
- [ ] RL 形式化：MDP、return、value function、policy → [讲 1](00-foundations/01-mdp/index.md)
- [ ] 策略梯度：REINFORCE → baseline → advantage，推导一遍 → [讲 2](00-foundations/02-policy-gradient/index.md)
- [ ] PPO 原始论文（1707.06347）+ clipped surrogate → [讲 3](00-foundations/03-ppo/index.md)
- [ ] 数学补丁：KL 散度（前向/反向、k3）→ [讲 4](00-foundations/04-kl-divergence/index.md)；Bradley-Terry → [讲 5](00-foundations/05-bradley-terry/index.md)
- [ ] LLM 训练全景图：pretrain → mid-train → post-train 各自解决什么 → [讲 6](00-foundations/06-llm-training-panorama/index.md)
- [ ] 出口自测：白板推导「REINFORCE 为什么方差大 → advantage 怎么减方差 → PPO 为什么 clip」（清单见 [模块 README](00-foundations/README.md)）

每讲附 `raw/RESOURCES.md`（原始出处与精读定位）。深入资源：OpenAI Spinning Up、Sutton & Barto《强化学习导论》、RLHF Book（rlhfbook.com）、3Blue1Brown（数学直觉）。

产出：七讲模块内自测全部通过 + 出口测试；概念笔记可选（模板在 `templates/`）。

## Phase 1 · 后训练主线（4-6 周）★核心

### Week 1-2 · SFT 与数据（→ [模块 01 · 4 讲](01-post-training/01-sft-and-data/README.md)，已建成）

- [x] 指令微调：损失函数、template、FLAN→LIMA→Tulu 3 → [讲①](01-post-training/01-sft-and-data/01-instruction-tuning/index.md)
- [x] 数据工程：质量三件套、合成闭环、配比 → [讲②](01-post-training/01-sft-and-data/02-data-engineering/index.md)
- [x] LoRA/QLoRA → [讲③](01-post-training/01-sft-and-data/03-lora-peft/index.md)
- [x] **实践 P1** 跑通指南 → [讲④](01-post-training/01-sft-and-data/04-sft-practice/index.md)

### Week 3 · 偏好对齐（→ [模块 02 · 4 讲](01-post-training/02-preference-alignment/README.md)，已建成）

- [x] RLHF 三阶段 → [讲①](01-post-training/02-preference-alignment/01-rlhf-three-stages/index.md)
- [x] DPO 完整推导 ★ → [讲②](01-post-training/02-preference-alignment/02-dpo-derivation/index.md)
- [x] 变体家族 IPO/KTO/SimPO/ORPO → [讲③](01-post-training/02-preference-alignment/03-dpo-family/index.md)
- [x] RLAIF 与 reward hacking → [讲④](01-post-training/02-preference-alignment/04-rlaif-reward-hacking/index.md)
- [ ] **实践 P2** 手写 mini-DPO（指南在模块内，记录到 [03-practice](03-practice/README.md)）

### Week 4 · 奖励模型（→ [模块 03 · 4 讲](01-post-training/03-reward-models/README.md)，已建成）

- [x] RM 全景与坑 → [讲①](01-post-training/03-reward-models/01-rm-basics/index.md)
- [x] ORM vs PRM、MC rollout 标注 → [讲②](01-post-training/03-reward-models/02-orm-vs-prm/index.md)
- [x] GenRM 与评测 → [讲③](01-post-training/03-reward-models/03-genrm-eval/index.md)
- [x] BoN 与过度优化 → [讲④](01-post-training/03-reward-models/04-bon-overoptimization/index.md)
- [ ] **实践 P6** 训 RM + BoN 评估

### Week 5-6 · LLM 强化学习（→ [模块 04 · 4 讲](01-post-training/04-rl-for-llm/README.md) ★，已建成）

- [x] PPO-for-LLM 管线 → [讲①](01-post-training/04-rl-for-llm/01-ppo-for-llm/index.md)
- [x] GRPO 推导 ★ → [讲②](01-post-training/04-rl-for-llm/02-grpo/index.md)
- [x] 变体地图（Dr.GRPO/DAPO/VAPO…）→ [讲③](01-post-training/04-rl-for-llm/03-grpo-variants/index.md)
- [x] RLVR 与 verl → [讲④](01-post-training/04-rl-for-llm/04-rlvr-and-verl/index.md)
- [ ] **实践 P3** verl 跑 GRPO + 源码笔记

产出：各讲自测通过 + P1/P2/P3/P6 实验记录。**里程碑：能给别人做一次 45 分钟的「从 SFT 到 GRPO」分享。**

## Phase 2 · 推理模型（2-3 周）（→ [模块 05 · 4 讲](01-post-training/05-reasoning/README.md)，已建成）

- [x] 前史：STaR / Quiet-STaR → [讲①](01-post-training/05-reasoning/01-cot-to-star/index.md)
- [x] DeepSeek-R1 精读 ★ → [讲②](01-post-training/05-reasoning/02-deepseek-r1/index.md)
- [x] Test-time scaling 全景 → [讲③](01-post-training/05-reasoning/03-test-time-scaling/index.md)
- [x] **实践 P4** mini-R1 复现指南 → [讲④](01-post-training/05-reasoning/04-mini-r1-practice/index.md)

里程碑：能讲清「RLVR 训练出来的推理能力 vs 蒸馏出来的，差异在哪」。

## Phase 3 · Agent 算法（4-6 周）

### Week 1 · Agent 范式（→ [模块 01 · 3 讲](02-agentic/01-agent-paradigms/README.md)，已建成）

- [x] ReAct 与轨迹视角（prompt=塑形轨迹分布）→ [讲①](02-agentic/01-agent-paradigms/01-react-trajectory/index.md)
- [x] 反思与规划（Reflexion/ToT 与推理模型的合流）→ [讲②](02-agentic/01-agent-paradigms/02-reflection-planning/index.md)
- [x] 工具调用训练（数据自举、执行反馈=奖励）→ [讲③](02-agentic/01-agent-paradigms/03-tool-learning/index.md)

### Week 2-3 · Agentic RL ★（→ [模块 02 · 4 讲](02-agentic/02-agentic-rl/README.md)，已建成）

- [x] 四大难题框架 → [讲①](02-agentic/02-agentic-rl/01-four-challenges/index.md)
- [x] 三代发展线（WebGPT→AgentGym）→ [讲②](02-agentic/02-agentic-rl/02-sft-to-rl-timeline/index.md)
- [x] 前沿算法（GiGPO/ARPO/WebRL）→ [讲③](02-agentic/02-agentic-rl/03-frontier-methods/index.md)
- [x] **实践 P5** Search-R1 复现指南 → [讲④](02-agentic/02-agentic-rl/04-search-r1-practice/index.md)

### Week 4 · 记忆与长程（→ [模块 03 · 3 讲](02-agentic/03-memory-and-tools/README.md)，已建成）

- [x] 记忆分类学四格诊断 → [讲①](02-agentic/03-memory-and-tools/01-memory-taxonomy/index.md)
- [x] MemGPT 自管理记忆（可 RL 化链路）→ [讲②](02-agentic/03-memory-and-tools/02-memgpt-self-editing/index.md)
- [x] Context Engineering 与回访评测 → [讲③](02-agentic/03-memory-and-tools/03-context-engineering/index.md)

### Week 5 · 多智能体与自我改进（→ [模块 04 · 3 讲](02-agentic/04-multi-agent/README.md)，已建成）

- [x] 自我改进闭环（Self-Rewarding/SPIN/SCoRe）→ [讲①](02-agentic/04-multi-agent/01-self-improvement-loop/index.md)
- [x] 编排模式与误差传播 → [讲②](02-agentic/04-multi-agent/02-orchestration-patterns/index.md)
- [x] 训练还是编排（全课程收官框架）→ [讲③](02-agentic/04-multi-agent/03-train-vs-orchestrate/index.md)

里程碑：能设计一个 agentic RL 训练方案（环境、reward、算法、评估）并说出 3 个已知风险。**这是你的岗位核心差异化能力。**

## Phase 4 · 前沿追踪与体系化（持续，每周固定投入）

- [ ] 每周从信息源筛 1-3 篇精读（流程见 README「持续学习闭环」）
- [ ] 每月给知识图谱做一次「连线回顾」：这一个月的新论文改变了哪些旧结论
- [ ] 季度产出一份领域 survey（如《Agentic RL 2026 综述》）或一次组内分享
- [ ] 自选深耕方向（候选：world models for agents、continual learning、post-train safety、数据自举），做出可对外讲的东西

---

## 实践线（与阶段并行，全部在 `03-practice/`）

| # | 实践 | 对应阶段 | 交付物 |
|---|---|---|---|
| P1 | SFT 小模型（TRL / LLaMA-Factory） | Phase 1 | 训练记录 + eval 样例 |
| P2 | 手写 mini-DPO（~200 行） | Phase 1 | 代码 + 训练前后对比 |
| P3 | verl 跑 GRPO on GSM8K + 源码笔记 | Phase 1 | reward 曲线 + 源码走读笔记 |
| P4 | mini-R1 countdown 复现（TinyZero 风格） | Phase 2 | 涌现行为的实验记录 |
| P5 | Search-R1 风格多轮工具 RL | Phase 3 | multi-turn 细节笔记 + 曲线 |
| P6 | 训 RM/PRM + Best-of-N 评估 | Phase 1 | BoN vs greedy 对比实验 |

硬件参考：单卡 24GB 起（LoRA / gradient checkpointing），模型选 0.5B-3B；P3-P5 建议 1.5B 模型。没卡就先用 Colab/Kaggle 或公司资源，实践不可省。

## 节奏建议（每周 10-15h）

- 精读 1-2 篇（按模板出笔记，公式逐行过）+ 粗读 3-5 篇（只抓问题/方法/结论）
- 实践 4-6h：当前阶段的 P# 推进一格就记录
- 周日晚 30-60min：周报 + 图谱增量（`06-tracking/weekly/`）
- 每阶段结束：给假想听众讲一次 30-45 分钟，讲不顺的地方就是下一个要补的洞

## 检查点（自我验收）

- [ ] Phase 0：白板推导 REINFORCE → PPO 全程无卡顿
- [ ] Phase 1：完成 45 分钟「从 SFT 到 GRPO」分享稿
- [ ] Phase 2：讲清「RLVR vs 蒸馏」的本质差异，附 P4 实验证据
- [ ] Phase 3：独立写出一份 agentic RL 训练方案设计文档
- [ ] Phase 4（每季度）：一份对外可读的 survey / 分享
