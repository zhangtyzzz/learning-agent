# 05 · 知识图谱（Knowledge Graph）

> 用**结构化数据**沉淀学习成果：概念、论文、框架是节点，先修/提出/扩展/对比/应用是边。
> 图谱不只是可视化——`prereq_of`（先修）边经过拓扑排序后就是**学习顺序**，新论文读完挂进图谱，就能看出它在你知识版图的位置。

## 数据格式

`nodes.jsonl`（每行一个 JSON）：

```json
{"id": "grpo", "type": "method", "title": "GRPO", "domain": "rl-for-llm", "status": "learning", "importance": 5, "summary": "组相对策略优化：去 critic，组内相对 advantage"}
```

- `type`：`concept`（概念）/ `method`（算法）/ `paper`（论文）/ `framework`（框架）
- `domain`：与 `04-papers/by-domain` 一致的九个领域
- `status`：⚪ `todo` / 🟡 `learning` / 🟢 `learned`
- `importance`：1-5，影响自测优先级

`edges.jsonl`：

```json
{"src": "ppo", "rel": "prereq_of", "dst": "grpo", "note": "GRPO 是 PPO 的 critic-free 变体"}
```

关系词：`prereq_of`（先修）/ `introduces`（论文提出）/ `extends`（扩展）/ `applied_in`（应用于）/ `compared_to`（对比）/ `implements`（框架实现）/ `related_to`（相关）

## 生成命令

```bash
python3 05-knowledge-graph/build_graph.py
```

自动完成：完整性校验（悬空边/重复 id/非法关系会报错退出）→ 按 `prereq_of` 拓扑排序输出学习顺序 → 生成 [GRAPH.md](GRAPH.md)（mermaid 关系图 + 学习顺序 + 各领域进度统计）。

## 日常维护（让 ZCode 做也行）

- 读完一篇论文：加一个 `paper` 节点 + 2-4 条边（`introduces`/`extends`/`compared_to`）
- 学会一个概念：把 `status` 改 `learned`，重跑脚本看进度统计变化
- 每月回顾：检查是否有「新论文推翻旧连线」的情况，更新 `note`

## 种子内容

已预置 ~50 个节点（核心概念 24 + 关键论文 24 + 框架 4）和 ~50 条边，覆盖全部九个领域——它本身就是一张「必学知识地图」。
