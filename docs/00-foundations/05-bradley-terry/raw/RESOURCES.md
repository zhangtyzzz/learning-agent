# 原始资料 · Bradley-Terry 模型

> 用法：index.md 是蒸馏版。下面是原始出处与精读定位。

## 必读

| # | 资料 | 定位 | 看什么 |
|---|---|---|---|
| 1 | DPO 论文 §2 | arXiv 2305.18290 | 不是让你读 DPO 全文：只读 §2.1「RLHF 目标」到 §2.3 前的 BT 部分——现代后训练语境下 BT 最好的表述 |
| 2 | RLHF Book（Nathan Lambert） | https://rlhfbook.com 奖励模型章节 | RM 数据、训练、评测的系统梳理，含长度偏置等已知问题的讨论 |
| 3 | InstructGPT 论文 §3.6 | arXiv 2203.02155 | RM 训练的工程细节第一手描述（几万对数据就够、epoch 少而精） |

## 可选深入

| 资料 | 定位 | 看什么 |
|---|---|---|
| Bradley & Terry 原始论文（1952） | 搜「The rank analysis of incomplete block designs」 | 考古兴趣即可，方法部分已被现代文献覆盖 |
| RewardBench 论文 | arXiv 2403.13787 | 想了解「RM 到底可不可靠」时读 §1-2：各家 RM 的失败模式盘点 |

## 精读要点（对照本讲）

- BT 在统计学里的标准名是「成对比较模型」，其「分数差 → sigmoid」与 Elo 等级分同源——换算直觉可以直接搬
- 「绝对分无意义」在 RM 部署时有实锤后果：不同 RM 的分数**不可横向比较**，跨模型评测必须用胜率而不是分数
- RM 过优化的定量规律见 arXiv 2210.10760（Gao et al.），第 1 阶段 reward-models 一讲会精读，此处先收藏
