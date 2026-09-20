# 原始资料 · 指令微调

> 用法：index.md 是蒸馏版；出处定位如下。链接失效就搜标题。

## 必读

| # | 资料 | 定位 | 看什么 |
|---|---|---|---|
| 1 | FLAN: Scaling Instruction-Finetuned Models | arXiv 2210.11416 | 只看 §1-2：任务集合与「指令多样性」的设计；实验表扫一眼 |
| 2 | LIMA: Less Is More for Alignment | arXiv 2305.11206 | 精读 §3（1000 条数据怎么挑的）与 §5（失败案例分析）——最实用 |
| 3 | Tulu 3 | arXiv 2411.15124 | §2（数据构成与配比）+ §3（SFT 细节）：现代开源配方的事实标准 |

## 可选

| 资料 | 定位 | 看什么 |
|---|---|---|
| Self-Instruct / Alpaca | arXiv 2212.10560 | 合成指令闭环的原始版本（下一讲细讲） |
| TRL 文档 · SFTTrainer | https://huggingface.co/docs/trl | 第 4 讲实践前过一遍参数：packing、assistant_only_loss |

## 精读要点（对照本讲）

- LIMA 的「超拟人」数据写作规范（§3 的 6 条原则）可以直接当你的业务数据写作指南
- Tulu 3 论文最有价值的是「每一步都做消融」的方法论，而不是最终数字
- 注意：各家对「指令条数」的统计口径不同（对话轮 vs 样本条），横向比较无意义
