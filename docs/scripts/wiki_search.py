#!/usr/bin/env python3
"""知识库极简检索（给人和给 LLM 的 CLI 工具）。

用法：python3 wiki_search.py 词1 [词2 …]   （多词 = AND，大小写不敏感）
输出：匹配文件 + 行号 + 行内容（每文件最多 5 行）
"""
from __future__ import annotations

import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
MAX_PER_FILE = 5


def main() -> None:
    terms = [t.lower() for t in sys.argv[1:]]
    if not terms:
        print(__doc__)
        sys.exit(1)
    hits = 0
    for p in sorted(DOCS.rglob("*.md")):
        lines = p.read_text(encoding="utf-8").splitlines()
        shown = 0
        for i, line in enumerate(lines, 1):
            low = line.lower()
            if all(t in low for t in terms):
                rel = p.relative_to(DOCS)
                print(f"{rel}:{i}: {line.strip()[:120]}")
                shown += 1
                hits += 1
                if shown >= MAX_PER_FILE:
                    print(f"{rel}: …（更多匹配省略）")
                    break
    print(f"\n[{hits} 处匹配，检索词: {' + '.join(terms)}]")


if __name__ == "__main__":
    main()
