# raw/ · 原始资料收纳区（Data Ingest）

> Karpathy 式知识库的第一层：**先收割原文，再谈整理**。这里放「一手材料」的本地副本，由 ZCode 负责编译进课程与 wiki，你几乎不用回来翻。

## 放什么

| 来源 | 怎么收 | 放哪 |
|---|---|---|
| 网页文章 / 博客 | Obsidian Web Clipper 导出 .md（图片一并下载到本地） | `raw/` 根目录 |
| 论文 | pdf 或 arXiv 页面文本快照 | `raw/`（pdf 可直接放，ZCode 能读） |
| 代码仓库 / 项目 | README + 关键源码片段的 md 笔记 | `raw/` |
| 图表截图 | 原图 | `raw/assets/` |

## 约定

- **命名**：`YYYY-MM-DD-来源-短标题.md`，如 `2026-09-21-interconnects-dapo-analysis.md`
- **头信息**（front-matter，ZCode 编译时会维护）：

  ```yaml
  ---
  source: https://…
  author: …
  date: 2026-09-21
  status: 未编译   # 未编译 / 已编译
  ---
  ```

- **只进不改**：原文快照是事实层，编译中的理解写在别处（04-papers/notes 或 wiki/），发现原文错误用 `status` 和批注标记，不直接改写。

## 流程

```
丢进 raw/（手动收藏或让 ZCode 抓取）
  → 对 ZCode 说「编译 raw/ 里的新资料」
  → 产出：论文笔记（04-papers/notes）或概念文章（wiki/concepts）
  → 原文 status 改为「已编译」，保留在原地供溯源
```

与 `04-papers/inbox` 的分工：**inbox 是待读清单**（一行链接，还没读），**raw/ 是已收割原文**（读过/值得留底的本地副本）。
