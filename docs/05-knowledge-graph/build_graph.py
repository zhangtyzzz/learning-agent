#!/usr/bin/env python3
"""知识图谱生成器：从 nodes.jsonl + edges.jsonl 生成 GRAPH.md。

功能：
  1. 校验：节点 id 唯一、边的端点存在、关系词/领域/状态合法
  2. 拓扑排序：按 prereq_of 边输出「学习顺序」，检测环
  3. 生成 GRAPH.md：mermaid 关系图（按领域分组）+ 学习顺序 + 进度统计

用法：python3 build_graph.py
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict, deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
NODES_FILE = HERE / "nodes.jsonl"
EDGES_FILE = HERE / "edges.jsonl"
OUT_FILE = HERE / "GRAPH.md"

DOMAINS = {
    "foundations": "地基（RL 与数学）",
    "sft-data": "SFT 与数据",
    "preference-alignment": "偏好对齐（RLHF/DPO）",
    "reward-models": "奖励模型",
    "rl-for-llm": "LLM 强化学习",
    "reasoning": "推理模型",
    "agent-paradigms": "Agent 范式",
    "agentic-rl": "Agentic RL",
    "memory-long-horizon": "记忆与长程",
    "multi-agent-self-improve": "多智能体与自我改进",
}

TYPES = {"concept", "method", "paper", "framework"}
STATUSES = ("todo", "learning", "learned")
STATUS_MARK = {"todo": "⚪", "learning": "🟡", "learned": "🟢"}

RELS = {"prereq_of", "introduces", "extends", "applied_in", "compared_to", "implements", "related_to"}
REL_LABEL = {
    "prereq_of": "先修",
    "introduces": "提出",
    "extends": "扩展",
    "applied_in": "应用",
    "compared_to": "对比",
    "implements": "实现",
    "related_to": "相关",
}
REL_ARROW = {
    "prereq_of": "-->",
    "introduces": "-.->",
    "extends": "==>",
    "applied_in": "-.->",
    "compared_to": "---",
    "implements": "-.->",
    "related_to": "---",
}
TYPE_PREFIX = {"concept": "", "method": "⚙ ", "paper": "📄 ", "framework": "🛠 "}


def load_jsonl(path: Path) -> list[tuple[int, dict]]:
    rows = []
    with path.open(encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                rows.append((lineno, json.loads(line)))
            except json.JSONDecodeError as exc:
                sys.exit(f"[错误] {path.name}:{lineno} 不是合法 JSON：{exc}")
    return rows


def validate(nodes: dict[str, dict], edges: list[dict]) -> None:
    errors = []
    for nid, node in nodes.items():
        if node.get("type") not in TYPES:
            errors.append(f"节点 {nid}: 非法 type {node.get('type')!r}")
        if node.get("domain") not in DOMAINS:
            errors.append(f"节点 {nid}: 非法 domain {node.get('domain')!r}")
        if node.get("status") not in STATUSES:
            errors.append(f"节点 {nid}: 非法 status {node.get('status')!r}")
        if "title" not in node:
            errors.append(f"节点 {nid}: 缺少 title")
    for i, edge in enumerate(edges, 1):
        if edge.get("rel") not in RELS:
            errors.append(f"边 #{i}: 非法关系 {edge.get('rel')!r}")
        for key in ("src", "dst"):
            if edge.get(key) not in nodes:
                errors.append(f"边 #{i}: {key}={edge.get(key)!r} 不存在于节点表（悬空边）")
    if errors:
        sys.exit("[错误] 图谱数据校验失败：\n  " + "\n  ".join(errors))


TYPE_RANK = {"concept": 0, "method": 1, "framework": 2, "paper": 3}


def topo_order(nodes: dict[str, dict], edges: list[dict]) -> tuple[list[str], list[tuple[str, str]]]:
    """Kahn 拓扑排序，只看 prereq_of 边（src 先修于 dst）。返回 (顺序, 环上的节点对)。"""
    indeg = {nid: 0 for nid in nodes}
    adj: dict[str, list[str]] = defaultdict(list)
    for e in edges:
        if e["rel"] == "prereq_of":
            adj[e["src"]].append(e["dst"])
            indeg[e["dst"]] += 1
    queue = deque(sorted((nid for nid, d in indeg.items() if d == 0), key=lambda n: nodes[n]["title"]))
    order = []
    while queue:
        nid = queue.popleft()
        order.append(nid)
        for nxt in adj[nid]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                queue.append(nxt)
    if len(order) != len(nodes):
        cyclic = sorted(nid for nid, d in indeg.items() if d > 0)
        return order, [(nid, "?") for nid in cyclic]
    return order, []


def learning_sequence(nodes: dict[str, dict], edges: list[dict]) -> list[str]:
    """领域为主线（按 DOMAINS 顺序），领域内按 prereq_of 分层（Kahn），层内概念/算法在前、论文在后。"""
    intra: dict[str, list[str]] = defaultdict(list)
    indeg: dict[str, int] = defaultdict(int)

    def sort_key(nid: str) -> tuple:
        n = nodes[nid]
        return (TYPE_RANK[n["type"]], n["title"])

    for e in edges:
        if e["rel"] == "prereq_of" and nodes[e["src"]]["domain"] == nodes[e["dst"]]["domain"]:
            intra[e["src"]].append(e["dst"])
            indeg[e["dst"]] += 1

    sequence: list[str] = []
    for domain_key in DOMAINS:
        ids = [nid for nid in nodes if nodes[nid]["domain"] == domain_key]
        indeg_d = {nid: indeg[nid] for nid in ids}
        layer = sorted((nid for nid in ids if indeg_d[nid] == 0), key=sort_key)
        while layer:
            sequence.extend(layer)
            nxt = []
            for nid in layer:
                for dst in intra[nid]:
                    indeg_d[dst] -= 1
                    if indeg_d[dst] == 0:
                        nxt.append(dst)
            layer = sorted(nxt, key=sort_key)
        leftovers = sorted((nid for nid in ids if indeg_d[nid] > 0), key=sort_key)  # 环内节点兜底
        sequence.extend(leftovers)
    return sequence


def render(nodes: dict[str, dict], edges: list[dict], sequence: list[str], cyclic: list[tuple[str, str]]) -> str:
    lines: list[str] = []
    lines.append("# KNOWLEDGE GRAPH · 知识图谱")
    lines.append("")
    lines.append("> 本文件由 `build_graph.py` 自动生成，请勿手改；改 `nodes.jsonl` / `edges.jsonl` 后重跑脚本。")
    lines.append("")

    # 进度统计
    total = len(nodes)
    learned = sum(1 for n in nodes.values() if n["status"] == "learned")
    learning = sum(1 for n in nodes.values() if n["status"] == "learning")
    lines.append(f"**进度**：{STATUS_MARK['learned']} learned {learned} · {STATUS_MARK['learning']} learning {learning} · {STATUS_MARK['todo']} todo {total - learned - learning} · 共 {total} 节点 / {len(edges)} 边")
    lines.append("")
    lines.append("| 领域 | 节点 | 🟢 learned | 🟡 learning | ⚪ todo |")
    lines.append("|---|---|---|---|---|")
    for domain_key, domain_name in DOMAINS.items():
        group = [n for n in nodes.values() if n["domain"] == domain_key]
        if not group:
            continue
        c = {s: sum(1 for n in group if n["status"] == s) for s in STATUSES}
        lines.append(f"| {domain_name} | {len(group)} | {c['learned']} | {c['learning']} | {c['todo']} |")
    lines.append("")

    # 学习顺序（领域主线 + 领域内先修分层）
    lines.append("## 学习顺序（领域为主线，领域内按先修分层）")
    lines.append("")
    if cyclic:
        lines.append(f"> ⚠️ 检测到先修环，涉及：{', '.join(n for n, _ in cyclic)}")
        lines.append("")
    lines.append("按领域顺序往下学；同波次内概念/算法在前、论文在后，可按兴趣穿插。")
    lines.append("")
    prev_domain = None
    for i, nid in enumerate(sequence, 1):
        n = nodes[nid]
        if n["domain"] != prev_domain:
            lines.append(f"**—— {DOMAINS[n['domain']]} ——**")
            lines.append("")
            prev_domain = n["domain"]
        lines.append(f"{i}. {STATUS_MARK[n['status']]} **{n['title']}** `{n['type']}` — {n['summary']}")
    lines.append("")

    # mermaid 关系图
    lines.append("## 关系图（mermaid）")
    lines.append("")
    lines.append("```mermaid")
    lines.append("graph TD")
    for domain_key, domain_name in DOMAINS.items():
        group = sorted((nid for nid, n in nodes.items() if n["domain"] == domain_key),
                       key=lambda nid: nodes[nid]["title"])
        if not group:
            continue
        lines.append(f"  subgraph {domain_key}[\"{domain_name}\"]")
        for nid in group:
            n = nodes[nid]
            label = f"{TYPE_PREFIX[n['type']]}{n['title']}"
            lines.append(f"    {nid}[\"{label}\"]")
        lines.append("  end")
    lines.append("  classDef learned fill:#d9ead3,stroke:#38761d,color:#1c1c1c;")
    lines.append("  classDef learning fill:#fff2cc,stroke:#bf9000,color:#1c1c1c;")
    lines.append("  classDef todo fill:#f3f3f3,stroke:#999999,color:#1c1c1c;")
    for status in STATUSES:
        ids = [nid for nid, n in nodes.items() if n["status"] == status]
        if ids:
            lines.append(f"  class {','.join(ids)} {status};")
    seen = set()
    for e in edges:
        key = (e["src"], e["rel"], e["dst"])
        if key in seen:
            continue
        seen.add(key)
        arrow = REL_ARROW[e["rel"]]
        lines.append(f"  {e['src']} {arrow}|{REL_LABEL[e['rel']]}| {e['dst']}")
    lines.append("```")
    lines.append("")
    lines.append("## 图例")
    lines.append("")
    lines.append("节点：⚙ 算法 · 📄 论文 · 🛠 框架 ·（无前缀）概念；颜色：绿=learned，黄=learning，灰=todo。")
    lines.append("")
    lines.append("边：`先修`（prereq_of，决定学习顺序）· `提出`（论文→概念/算法）· `扩展` · `应用` · `对比` · `实现`（框架→算法）· `相关`。")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    if not NODES_FILE.exists() or not EDGES_FILE.exists():
        sys.exit(f"[错误] 缺少 {NODES_FILE.name} 或 {EDGES_FILE.name}")

    node_rows = load_jsonl(NODES_FILE)
    edge_rows = load_jsonl(EDGES_FILE)

    nodes: dict[str, dict] = {}
    for lineno, node in node_rows:
        nid = node.get("id")
        if not nid:
            sys.exit(f"[错误] nodes.jsonl:{lineno} 缺少 id")
        if nid in nodes:
            sys.exit(f"[错误] nodes.jsonl:{lineno} 节点 id 重复：{nid}")
        nodes[nid] = node

    edges = [edge for _, edge in edge_rows]
    validate(nodes, edges)
    _, cyclic = topo_order(nodes, edges)
    sequence = learning_sequence(nodes, edges)

    out = render(nodes, edges, sequence, cyclic)
    OUT_FILE.write_text(out, encoding="utf-8")

    learned = sum(1 for n in nodes.values() if n["status"] == "learned")
    print(f"[完成] 节点 {len(nodes)} · 边 {len(edges)} · 已学会 {learned}")
    print(f"[完成] 学习顺序 {len(sequence)} 项，环 {len(cyclic)} 个")
    print(f"[完成] 已生成 {OUT_FILE}")


if __name__ == "__main__":
    main()
