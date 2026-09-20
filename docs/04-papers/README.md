# 04 · 论文库（持续更新）

> 论文是这条学习线的第一手材料。本目录管理「待读 → 精读 → 归档」的全流程。

## 目录与流程

```
inbox/            待读：pdf 或链接先丢这里（顺手在文件名/开头标来源）
  ↓ 每周筛选 1-3 篇精读
notes/            精读笔记：templates/paper-note.md 模板，命名 <arxiv-id>-<短名>.md
  ↓ 归档
by-domain/<领域>/  放一行链接式索引或精简摘要（好文放摘要，普文放链接）
```

领域分类与知识图谱、目录结构对齐：

`sft-data` · `preference-alignment` · `reward-models` · `rl-for-llm` · `reasoning` · `agent-paradigms` · `agentic-rl` · `memory-long-horizon` · `multi-agent-self-improve`

## 精读 vs 粗读

- **精读**（1-2 篇/周）：公式逐行过，按模板出笔记，回填图谱连线
- **粗读**（3-5 篇/周）：只抓三件事——解决什么问题 / 方法一句话 / 结论是否改变旧认知；粗读结果记进周报即可

## 索引

- 全部已读论文的索引表：[PAPER-INDEX.md](PAPER-INDEX.md)（新读一篇加一行）
- 初始必读清单已分散在各领域 README 的表格里，按 ROADMAP 顺序消化

## 处理新论文的标准动作

1. 入 inbox（pdf 或 arXiv 链接 + 一句话为什么值得读）
2. 精读后：笔记进 `notes/`、索引进 `PAPER-INDEX.md`、归档行进 `by-domain/<领域>/`
3. 图谱增量：新节点（论文/概念）与连线 → `05-knowledge-graph/`，重跑生成脚本
4. 状态流转：inbox ⚪ → learning 🟡 → learned 🟢
