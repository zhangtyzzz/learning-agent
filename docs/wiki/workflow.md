# wiki/ · 知识沉淀区（LLM 编译层）

> 借鉴 Karpathy 的 LLM Knowledge Base 工作流：**课程（00-02 目录）是「教材」，这里是「你自己的知识库」**——由 ZCode 写作和维护，你负责读和提问。

## 分工

- **ZCode**：维护本目录的一切——概念文章、问答沉淀、索引、回链。你说需求，我来写。
- **你**：阅读、提问、指出错误。不直接编辑（改了也行，我会以下一版为准）。

## 四步循环

```
① ingest   原文进 ../raw/
② compile  「编译 raw/ 里的新资料」→ 沉淀成 concepts/ 文章或 04-papers/notes
③ Q&A      「就 XX 问题研究全库」→ 结论按格式存进 qa/，探索成果不流失
④ lint     机械检查跑 scripts/wiki_lint.py；语义检查（不一致/缺源/新文章候选）让 ZCode 跑
```

## 目录

| 目录 | 内容 | 格式 |
|---|---|---|
| `concepts/` | 概念文章（比课程讲次更细、更个人化，含回链） | 头信息：`tags` / `status` / `related` |
| `qa/` | 问答与研究结论的沉淀，命名 `YYYY-MM-DD-主题.md` | 头信息：`question` / `date` / `tags` / `sources` |
| `index.md` | 全部文章的索引与一句话摘要（ZCode 维护） | — |

## Q&A 沉淀格式（qa/）

```markdown
---
question: DAPO 的 clip-higher 为什么能防熵坍缩？
date: 2026-09-21
tags: [RL, GRPO变体, DAPO]
sources: ["01-post-training/04-rl-for-llm/03-grpo-variants/index.md", "arXiv 2503.14476"]
---
## 结论（3 行内）
…
## 论据
…
## 开放问题（可选）
…
```

幻灯片类产出用 **Marp** 格式（头部加 `marp: true`），文件放 `qa/`，文件名带 `-slides`。

## 对 ZCode 说的常用指令

| 你说 | 我做 |
|---|---|
| 「编译 raw/ 里的新资料」 | 读原文 → 写笔记/概念文章 → 更新 index 与回链 → 原文标记已编译 |
| 「就 XX 问题研究全库，沉淀成 qa 笔记」 | 跨课程检索+推理，产出 qa/ 文章并回填索引 |
| 「跑一次知识库健康检查」 | wiki_lint.py + 语义层：找不一致、缺来源、候选新文章 |
| 「把这个结论做成幻灯片」 | 生成 Marp md 存 qa/，可导出 pptx/pdf |

## 与知识图谱的关系

wiki 是**人读层**，`05-knowledge-graph/` 是**结构层**：qa/concepts 里出现的新概念与新连线，会同步写进 `nodes.jsonl / edges.jsonl`（图谱的学习顺序与进度统计因此保持最新）。
