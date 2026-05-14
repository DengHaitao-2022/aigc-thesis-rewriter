# AIGC Risk Patterns for Chinese Thesis Text

## How to interpret detector labels

Treat 高/中/低 labels as signals about expression style, not proof of authorship. Different platforms can disagree strongly. Analyze the writing pattern that the detector likely reacted to, then rewrite only as much as needed.

## High-risk patterns

High-risk fragments commonly contain several of these features:

1. **Template thesis rhythm**
   - “随着……不断发展……逐渐……”
   - “针对这一问题，本文设计并实现……”
   - “从……角度来看……”
   - “综合来看 / 由此可见 / 这说明……”

2. **Background-problem-solution-value in one smooth paragraph**
   - The paragraph moves from broad background to problem, then system design, then value claim without concrete project evidence.

3. **List-heavy feature enumeration**
   - Many parallel nouns: “认证鉴权、工作流编排、链式执行、门控恢复、产物追踪以及结果回放”.
   - Many abstract qualities: “可控性、可追溯性、可恢复性、可扩展性”.

4. **Evaluation without mechanism**
   - “提升生成质量”, “增强可解释性”, “降低风险”, “提供基础”, “形成闭环” without saying which table, state, interface, node, or artifact causes it.

5. **Literature review smoothing**
   - “某某等提出……这类研究说明……” repeated across multiple papers.
   - Weak contrast between sources; no statement about what the current thesis adopts or does not adopt.

6. **Textbook-style definition**
   - “所谓……指的是……其核心在于……” when not tied to the actual system.

7. **Conclusion-like closure**
   - A paragraph ends with a broad polished sentence such as “为后续研究和应用提供参考”.

## Medium-risk patterns

Medium-risk fragments usually have a template structure but include some concrete project information. They may use “第一、第二、第三” or broad lists, but the list contains specific technical objects such as `Provider`, `Gate`, `Artifact`, `WorkflowRun`, or `JSON Schema`.

Rewrite medium-risk text by varying the order, replacing generic transitions, and connecting each abstract claim to one concrete project object.

## Low-risk patterns

Low-risk fragments usually describe implementation facts:

- specific fields, tables, states, paths, or interfaces;
- clear frontend/backend responsibility split;
- explicit validation, persistence, rollback, or recovery behavior;
- fewer value adjectives and more operational verbs.

Do not over-edit low-risk fragments. Keep the technical density and only smooth repeated wording.

## Practical rewrite direction

Use this conversion rule:

- Before: “系统通过 Gate、Trace 和 Artifact 机制增强了人机协同能力和过程可追溯性。”
- After: “当任务进入 Gate 状态后，后端会保存待确认内容和对应检查点；用户提交处理意见后，系统再从该节点继续执行。Trace 展示节点时间线，Artifact 保存提纲、草稿和终稿等产物版本。”

The second version is better because it replaces abstract evaluation with observable system behavior.
