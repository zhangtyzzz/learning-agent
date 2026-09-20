# 原始资料 · RLHF 三阶段

> 用法：index.md 是蒸馏版；出处定位如下。

## 必读

| # | 资料 | 定位 | 看什么 |
|---|---|---|---|
| 1 | InstructGPT | arXiv 2203.02155 | §3 全部 + Fig.2（三阶段流程图原型）：每一步的数据量、标注规范、消融都写透了 |
| 2 | RLHF Book | https://rlhfbook.com | 「Alignment 与 RLHF 总览」章节：现代视角的体系化重述 |

## 可选

| 资料 | 定位 | 看什么 |
|---|---|---|
| Anthropic HH 论文 | 搜「Training a Helpful and Harmless Assistant」 | 偏好数据规模化的另一条平行路线 |
| Hugging Face 博客 Illustrated RLHF | https://huggingface.co/blog/rlhf | 配图直觉版，当本讲的另一种画法 |

## 精读要点

- InstructGPT 的标注指南（附录）是所有偏好标注规范的祖师爷：注意他们对「标注者分歧」的处理
- 论文的消融表证明：RM 质量 > PPO 细节——奖励端一错，全盘皆错（第 3 模块的主题）
