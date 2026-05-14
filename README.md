# AIGC Thesis Rewriter

A reusable ChatGPT Skill for analyzing Chinese AIGC detection reports and rewriting thesis or technical-document fragments into a less template-like, more project-grounded academic style.

## Contents

- `SKILL.md` - skill entrypoint and workflow instructions
- `agents/openai.yaml` - ChatGPT skill UI metadata
- `references/` - rewrite rules, risk patterns, and output templates
- `scripts/` - optional helpers for extracting report fragments and generating rewrite-plan skeletons

## Typical use

Use this skill when working with Chinese undergraduate theses, technical documents, or AIGC detection reports and the task involves:

- 降重
- 去 AI 味
- 降 AIGC 率
- 逐段替换方案
- 高/中/低风险片段分析
- 论文或技术文档改写

The skill preserves technical identifiers, citations, numbers, API paths, class names, field names, and core logic while changing overly template-like expression patterns.
