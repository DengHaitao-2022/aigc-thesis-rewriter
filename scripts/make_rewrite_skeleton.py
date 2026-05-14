#!/usr/bin/env python3
"""Create a Markdown rewrite-plan skeleton from extracted AIGC fragments."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def preview(text: str, limit: int = 80) -> str:
    cleaned = " ".join(text.split())
    return cleaned[:limit] + ("..." if len(cleaned) > limit else "")


def make_markdown(items: list[dict[str, Any]]) -> str:
    parts: list[str] = ["# AIGC 降重逐段替换方案", "", "## 总体判断", "", "待补充。", ""]
    for item in items:
        item_id = item.get("id", len(parts))
        risk = item.get("risk", "未标注")
        prob = item.get("probability")
        title = f"## 片段 {item_id}（风险：{risk}"
        if prob is not None:
            title += f"，概率：{prob}%"
        title += "）"
        parts.extend([
            title,
            "",
            f"**原文定位**：{preview(str(item.get('text', '')))}",
            "",
            "**触发原因**：待分析。",
            "",
            "**修改后**：",
            "",
            "待改写。",
            "",
            "**替换说明**：待补充。",
            "",
        ])
    return "\n".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create rewrite skeleton")
    parser.add_argument("input", type=Path, help="JSON produced by extract_aigc_fragments.py")
    parser.add_argument("-o", "--output", type=Path, default=Path("rewrite_plan.md"))
    args = parser.parse_args()

    items = json.loads(args.input.read_text(encoding="utf-8"))
    args.output.write_text(make_markdown(items), encoding="utf-8")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
