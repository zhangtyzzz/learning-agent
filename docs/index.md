# learning-agent · Agent 算法学习库

> 定位：Agent 工程师 → Agent 算法工程师的转型学习库。
> 主线是**后训练（post-training）算法**与 **Agentic RL**。验收标准：每个核心算法**能推导、能实现、能讲清楚**。

## 目录结构

```
learning-agent/                # 仓库根（docs/ 即网站源文件）
├── mkdocs.yml                 # 站点配置（导航/主题/公式/mermaid）
├── docs/
│   ├── index.md               # 站点首页（本文件）
│   ├── ROADMAP.md             # 学习路径（Phase 0-4，主线，先读这个）
│   ├── 00-foundations/        # 地基课程：7 讲图文教程（含数学符号课）
│   │   ├── 00-math … 06-panorama  #   每讲 = index.md（图解正文）+ assets/（SVG）+ raw/（原始资料）
│   │   └── symbol-reference.md    #   全课程符号速查表（希腊字母 + 运算记号）
│   ├── 01-post-training/      # 后训练主线（核心）
│   │   ├── 01-sft-and-data/       #   SFT 与数据工程
│   │   ├── 02-preference-alignment/ # RLHF / DPO 及其变体
│   │   ├── 03-reward-models/      #   奖励模型：RM / PRM / GenRM
│   │   ├── 04-rl-for-llm/         #   LLM 强化学习：PPO / GRPO 家族 / RLVR
│   │   └── 05-reasoning/          #   推理模型：R1 范式 / test-time scaling
│   ├── 02-agentic/            # Agent 算法专题
│   │   ├── 01-agent-paradigms/    #   ReAct / 反思规划 / 工具学习
│   │   ├── 02-agentic-rl/         #   多轮 RL / 工具 RL / 环境 scaling（重点）
│   │   ├── 03-memory-and-tools/   #   记忆 / 长程任务 / context engineering
│   │   └── 04-multi-agent/        #   多智能体 / 自我改进 / 训练vs编排
│   ├── 03-practice/           # 实践线：mini 实现与复现（与学习并行）
│   ├── 04-papers/             # 论文库（持续更新）：inbox / notes / by-domain
│   ├── 05-knowledge-graph/    # 知识图谱：概念/论文节点 + 关系 + 学习顺序
│   ├── 06-tracking/           # 持续学习：信息源清单 + 每周论文跟踪
│   └── templates/             # 笔记模板：论文笔记 / 概念笔记 / 周报
└── .github/workflows/         # push → 自动构建发布网页（GitHub Pages）
```

## 三条主线

1. **学习路径**：`ROADMAP.md` 是主线，按 Phase 0 → 4 推进，勾选 checklist 记录进度。
2. **持续学习**：新论文进 `04-papers/inbox/` → 按模板写笔记 → 归类到 `by-domain/` → 每周在 `06-tracking/weekly/` 写周报。
3. **知识沉淀**：概念和论文进入 `05-knowledge-graph/` 的图谱数据，脚本自动生成**学习顺序（拓扑排序）**和可视化关系图。
4. **知识库工作流**：原文进 `raw/` → 由 ZCode 编译进 `wiki/`（概念文章与问答沉淀）→ 探索成果回填，见 [wiki/workflow.md](wiki/workflow.md)。

## 持续学习闭环（每周一次，约 1-2 小时维护）

```
收集（06-tracking/sources.md 的信息源 + 日常刷到的好文章）
  → 入 inbox/
  → 每周筛选出 1-3 篇精读
  → templates/paper-note.md 写笔记 → 存 04-papers/notes/
  → 归档到 by-domain/<领域>/
  → 新概念/新连线 → 更新 05-knowledge-graph/nodes.jsonl + edges.jsonl
  → templates/weekly-digest.md 写周报 → 06-tracking/weekly/
```

## 和 ZCode 协作的常用指令

| 你说 | 我做 |
|---|---|
| 「把这篇论文按模板写笔记」 | 读取 inbox 里的 pdf/链接，产出笔记并归类、建议图谱连线 |
| 「把 XX 概念加入知识图谱，和 YY、ZZ 连线」 | 更新 nodes.jsonl / edges.jsonl 并重新生成 GRAPH.md |
| 「重新生成图谱」 | 运行 `python3 05-knowledge-graph/build_graph.py` |
| 「根据 ROADMAP 和我的进度生成本周计划」 | 结合 checklist 状态输出本周任务清单 |
| 「针对 01-post-training/04-rl-for-llm 出 10 道白板题考我」 | 生成自测题并批改 |
| 「本周 agentic RL 有什么新论文」 | 搜索更新到 inbox 并给出筛选建议 |
| 「讲讲 GRPO，按费曼式」 | 按概念笔记模板现场推导讲解 |

## 约定

- **内容模式**：每个学习单元 = `index.md`（整理后的图文讲解，图 > 表 > 公式 > 文字，控制文字密度）+ `raw/`（原始资料索引与出处定位）+ `assets/`（SVG 插图源文件）
- **状态标记**（全库统一，与图谱一致）：🟢 learned / 🟡 learning / ⚪ todo
- **论文笔记命名**：`04-papers/notes/<arxiv-id>-<短名>.md`，如 `2501.12948-deepseek-r1.md`
- **每篇论文笔记末尾必须回填**：图谱节点 id 与新增连线建议（没有就写 none）
- **论文信息以原文为准**：README 里列的 arXiv 号如有出入，以你查到的为准并顺手修正
- **一切以输出论英雄**：推导、笔记、mini 实现、内部分享，至少每周产出一个可见 artifact

## 从这里开始

1. 直接进 [00-foundations/README.md](00-foundations/README.md) —— 6 讲图文地基课程，今天就能开始读
2. 学完对照出口测试；同时浏览 [ROADMAP.md](ROADMAP.md) 了解全程安排
3. 本周（W38）从 `06-tracking/weekly/2026-W38.md` 开始第一个学习周期
