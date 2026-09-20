#!/usr/bin/env python3
"""知识库机械层健康检查。

检查项：
  1. 断链：docs/ 下所有 .md 的相对链接是否有效
  2. 孤儿页：wiki/ 下没有任何入链的文章
  3. qa/ 笔记缺 front-matter 必填字段（question/date/tags/sources）
  4. raw/ 文件缺 front-matter 或 status 字段

用法：python3 wiki_lint.py   （在 scripts/ 目录或任意位置运行均可）
退出码：0 通过，1 有错误
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent

LINK_RE = re.compile(r"\]\(([^)#]+?)(#[^)]*)?\)")
FM_RE = re.compile(r"\A---\s*\n(.*?)\n---", re.S)


def load(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def check_links(all_md: list[Path]) -> list[str]:
    errs = []
    for p in all_md:
        for m in LINK_RE.finditer(load(p)):
            target = m.group(1).strip()
            if not target or target.startswith(("http", "mailto:")):
                continue
            if not (p.parent / target).resolve().exists():
                errs.append(f"断链: {p.relative_to(DOCS)} -> {target}")
    return errs


def check_orphans(all_md: list[Path]) -> list[str]:
    wiki = [p for p in (DOCS / "wiki").rglob("*.md") if p.name != "README.md" and p.name != "index.md"]
    inbound: dict[Path, int] = {p: 0 for p in wiki}
    for p in all_md:
        text = load(p)
        for q in wiki:
            if q != p and q.name in text:
                inbound[q] += 1
    return [f"孤儿页(无入链): {q.relative_to(DOCS)}" for q, n in inbound.items() if n == 0]


def check_qa_frontmatter() -> list[str]:
    errs = []
    for p in (DOCS / "wiki" / "qa").glob("*.md"):
        if p.name == "README.md":
            continue
        text = load(p)
        m = FM_RE.match(text)
        if not m:
            errs.append(f"qa 缺 front-matter: {p.relative_to(DOCS)}")
            continue
        block = m.group(1)
        for field in ("question", "date", "tags", "sources"):
            if not re.search(rf"^{field}:", block, re.M):
                errs.append(f"qa 缺字段 {field}: {p.relative_to(DOCS)}")
    return errs


def check_raw_frontmatter() -> list[str]:
    errs = []
    for p in (DOCS / "raw").rglob("*.md"):
        if p.name == "README.md":
            continue
        m = FM_RE.match(load(p))
        if not m or not re.search(r"^status:", m.group(1), re.M):
            errs.append(f"raw 缺 status 头: {p.relative_to(DOCS)}")
    return errs


def main() -> None:
    all_md = sorted(DOCS.rglob("*.md"))
    errors = (
        check_links(all_md)
        + check_orphans(all_md)
        + check_qa_frontmatter()
        + check_raw_frontmatter()
    )
    n_files = len(all_md)
    if errors:
        print(f"[lint] {n_files} 个 md，发现 {len(errors)} 个问题：")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print(f"[lint] {n_files} 个 md，全部通过 ✓")


if __name__ == "__main__":
    main()
