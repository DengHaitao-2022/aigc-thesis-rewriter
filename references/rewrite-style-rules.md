# Chinese Rewrite Style Rules

## Target style

Produce professional Chinese thesis prose that is slightly more explanatory than the original, but not obviously colloquial. Keep the length close to the original. The rewrite should look like a student or developer explaining a real system, not like a polished generic AI summary.

## Length control

- Aim for 90% to 110% of the original length by default.
- If the original is already long, do not add a new concluding sentence.
- Replace abstract claims with concrete mechanisms instead of appending extra explanation.

## Preferred wording shifts

Use these shifts selectively. Do not force every occurrence.

- “采用 / 使用” → “选用 / 运用 / 把……作为……来使用”
- “基于” → “围绕 / 依托 / 在……基础上”
- “利用” → “借助 / 运用 / 凭借”
- “通过” → “借助 / 依靠 / 凭借”
- “并” → “并且 / 同时 / 还”
- “和 / 及 / 与” → “以及” when listing multiple items
- “管理” → “开展……管理 / 进行管理” when the sentence needs a fuller action phrase
- “处理” → “处理……工作 / 对……进行处理”
- “配置” → “进行配置”
- “实现” → “实现 / 得以实现 / 用来实现” depending on rhythm
- “特点” → “特性”
- “符合” → “契合”
- “适合” → “适宜”
- “立即” → “马上” only in non-formal operational contexts

## Avoid overusing these words

Reduce repeated occurrences of:

- “提升”, “提高”, “增强”, “降低”, “保障”, “支撑”, “赋能”
- “具有重要意义”, “具有较强价值”, “提供参考”, “奠定基础”
- “综合来看”, “由此可见”, “这说明”

When one is needed, attach it to a mechanism:

- Weak: “提高了可追溯性。”
- Better: “NodeRun 保存节点输入输出，Artifact 保留不同版本产物，因此后续能够查看生成过程。”

## Bracket handling

- Integrate explanatory brackets into the sentence when useful:
  - “ORM（对象关系映射）” → “ORM，即对象关系映射”
  - “功能（如 ORM、Admin）” → “功能，例如 ORM、Admin”
- For code identifiers, do not translate or alter the identifier:
  - “视图 (views.py)” → “视图 views.py” or “视图，即 views.py”
- Do not remove brackets if they contain necessary citation numbers, formula references, figure/table references, or exact technical disambiguation.

## Sentence rhythm

- Avoid making every paragraph follow “背景—问题—方案—意义”.
- Replace some “第一、第二、第三” lists with process order or module responsibility.
- Use “把” sentences where natural, but keep academic tone.
- Use conditional wording naturally: “如果……就……”, “当……时……”, “在……之后……”.
- Do not use “至于 xxx 呢”, “xxx 呢”, internet slang, or obvious spoken fillers.

## Technical preservation checklist

Before finalizing a rewrite, compare with the original and preserve:

- technical terms and English identifiers;
- API paths and HTTP methods;
- class, function, table, and field names;
- citations, reference ranges, figure/table numbers;
- data values, percentages, counts, and dates;
- stated module boundaries and implementation facts.
