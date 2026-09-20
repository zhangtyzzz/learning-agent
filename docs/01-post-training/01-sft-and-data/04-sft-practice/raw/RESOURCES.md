# 原始资料 · SFT 实战

> 用法：动手时的工具手册入口。

## 工具文档（实践时开在手边）

| # | 资料 | 看什么 |
|---|---|---|
| 1 | TRL 文档 · SFTTrainer | https://huggingface.co/docs/trl —— assistant_only_loss、packing、peft_config |
| 2 | LLaMA-Factory | https://github.com/hiyouga/LLaMA-Factory —— 想要零代码 YAML 配置时用 |
| 3 | Axolotl | 搜标题 —— 另一个流行配置式选择 |

## 数据起点

| 资料 | 看什么 |
|---|---|
| Alpaca 数据集（52k） | https://github.com/tatsu-lab/stanford_alpaca —— 首跑数据 |
| Tulu 3 SFT mixture | Hugging Face allenai/tulu-3-sft-mixture —— 现代配方的真实数据形态 |

## 精读要点

- 首跑目标不是效果好，而是**管线可信**：mask 正确、template 正确、曲线正常
- 建议第一组对照：5k Alpaca vs 5k 你的业务数据，同参训——一晚上就能看清「领域数据 vs 通用数据」的差异
