# learning-agent · Agent 算法学习库

> 从 Agent 工程师到 Agent 算法工程师的图文课程库：**后训练（post-training）与 Agentic RL**，33+7 讲，每讲「图 > 表 > 公式 > 文字」，含实践线、论文跟踪与知识图谱。

## 📖 网页阅读（手机友好）

内容在 `docs/` 下，用 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 构建成网站：

- **线上版**：push 到 GitHub 后，Actions 自动构建并发布到 GitHub Pages → `https://<你的用户名>.github.io/learning-agent/`
- **本地预览**：`pip install mkdocs-material && mkdocs serve` → http://localhost:8000

首次部署三步：
1. 在 GitHub 创建仓库并 push 本目录
2. 仓库 **Settings → Pages → Build and deployment → Source 选 `GitHub Actions`**
3. 把 `mkdocs.yml` 里的 `YOUR_USERNAME`（两处）改成你的用户名；之后每次 push 自动更新网页

## 📚 内容在哪

全部课程与工具都在 [`docs/`](docs/index.md)：

- [`docs/ROADMAP.md`](docs/ROADMAP.md) —— 学习路径（Phase 0-4，逐条挂接讲次）
- [`docs/00-foundations/`](docs/00-foundations/README.md) —— 地基 7 讲（含数学符号课与速查表）
- [`docs/01-post-training/`](docs/01-post-training/README.md) —— 后训练主线 20 讲（SFT/偏好/奖励/RL/推理）
- [`docs/02-agentic/`](docs/02-agentic/README.md) —— Agent 算法 13 讲（范式/Agentic RL/记忆/多智能体）
- [`docs/03-practice/`](docs/03-practice/README.md) —— 实践线 P1-P5
- [`docs/04-papers/`](docs/04-papers/README.md) + [`docs/06-tracking/`](docs/06-tracking/README.md) —— 论文库与持续学习
- [`docs/wiki/`](docs/wiki/workflow.md) + [`docs/raw/`](docs/raw/README.md) —— 知识库工作流（LLM 编译/问答沉淀/健康检查，Karpathy 式）
- [`docs/05-knowledge-graph/`](docs/05-knowledge-graph/README.md) —— 知识图谱（`python3 docs/05-knowledge-graph/build_graph.py` 重新生成）

## 🔁 持续迭代

一切都是 markdown（+ SVG 插图）：直接改文件、push 即发布；新讲次加进 `mkdocs.yml` 的 nav 即可出现在站点导航。让 ZCode「把某讲更新/新增一讲/重新生成图谱」然后 commit 即可。

## 文件结构

```
learning-agent/
├── mkdocs.yml            # 站点配置（导航/主题/数学公式/mermaid）
├── docs/                 # 全部内容（网站源文件）
│   ├── index.md          #   站点首页
│   ├── ROADMAP.md        #   学习路径
│   ├── 00-foundations … 06-tracking/
│   └── javascripts/      #   mermaid 初始化
└── .github/workflows/deploy.yml  # push → 自动构建发布 Pages
```
