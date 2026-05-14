#!/usr/bin/env python3
"""Extract candidate AIGC report fragments from text or PDF files.

This helper is intentionally conservative. It looks for common Chinese report
markers such as 高风险/中风险/低风险, 疑似AIGC, 片段, 概率, and percentages.
It outputs JSON for downstream rewrite-plan generation.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def read_text(path: Path) -> str:
    if path.suffix.lower() == ".pdf":
        try:
            import pdfplumber  # type: ignore
        except Exception as exc:  # pragma: no cover
            raise SystemExit("pdfplumber is required for PDF input: pip install pdfplumber") from exc
        pages: list[str] = []
        with pdfplumber.open(str(path)) as pdf:
            for page in pdf.pages:
                pages.append(page.extract_text() or "")
        return "\n".join(pages)
    return path.read_text(encoding="utf-8", errors="ignore")


def split_fragments(text: str) -> list[dict[str, Any]]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    chunks: list[dict[str, Any]] = []
    current: list[str] = []
    current_meta: dict[str, Any] = {}

    marker_re = re.compile(r"(高风险|中风险|低风险|疑似\s*AIGC|片段\s*\d+|第\s*\d+\s*段)")
    prob_re = re.compile(r"(\d+(?:\.\d+)?)\s*%")

    def flush() -> None:
        nonlocal current, current_meta
        if current:
            body = "\n".join(current).strip()
            if len(body) >= 20:
                item = {"id": len(chunks) + 1, "text": body}
                item.update(current_meta)
                chunks.append(item)
        current = []
        current_meta = {}

    for line in lines:
        if marker_re.search(line) and current:
            flush()
        risk_match = re.search(r"高风险|中风险|低风险", line)
        if risk_match:
            current_meta["risk"] = risk_match.group(0)
        prob_match = prob_re.search(line)
        if prob_match:
            current_meta["probability"] = float(prob_match.group(1))
        current.append(line)
    flush()
    return chunks


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract AIGC report fragments")
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=Path("aigc_fragments.json"))
    args = parser.parse_args()

    text = read_text(args.input)
    fragments = split_fragments(text)
    args.output.write_text(json.dumps(fragments, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"extracted {len(fragments)} fragments -> {args.output}")


if __name__ == "__main__":
    main()
