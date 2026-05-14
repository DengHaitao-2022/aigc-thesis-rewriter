# Output Templates

## Fragment rewrite template

```markdown
## 第 [id] 段：[风险等级]
**问题判断**：[one sentence]

**修改后**
[rewritten paragraph]

**替换建议**：[directly replace / split into two paragraphs / keep citations unchanged / verify with source]
```

## Complete replacement plan template

```markdown
# AIGC 降重逐段替换方案

## 总体判断
[report-level pattern: total risk, number of fragments, most common triggers]

## 处理原则
[3-5 concise rules]

## 片段 [id]（风险：[高/中/低]，概率：[x% if available]）
**原文定位**：[section or first 20-40 characters]
**触发原因**：[template summary / list-heavy / abstract evaluation / etc.]
**修改后**：
[replacement text]
**替换说明**：[what changed and what was preserved]
```

## Report analysis template

```markdown
## AIGC 标记规律

**总体结果**：[risk level, fragment count, image result if relevant]

**高风险规律**：
[patterns with examples]

**中风险规律**：
[why medium differs from high]

**低风险规律**：
[what low-risk text does better]

**下一轮处理策略**：
[chapter priority and rewriting method]
```

## Direct paragraph rewrite template

```markdown
修改后：
[rewritten text]
```

Use the direct template only when the user provides a paragraph and asks for a rewrite without analysis.
