# Abstract evidence slots

Use these slots to draft one cohesive paragraph; do not print the slot labels in the final paper.

- Real problem and overall objective: `[来自 PROBLEM BRIEF]`
- Shared structure/dependency: `[来自 QUESTION GRAPH]`
- Baseline and main method choice: `[来自 MODEL SUMMARY]`
- Targeted improvement and defect addressed: `[来自 ablation/validation artifact；若无则删除]`
- Key result: `[由 results.json 的 <key> 写入，单位：<unit>]`
- Validation/robustness evidence: `[由 metrics.json 或 scenario.csv 的 <key> 写入]`
- Practical conclusion and validity boundary: `[由已验证结果和 limitations 写入]`

If a slot has no evidence, leave an explicit artifact-key placeholder in the blueprint or omit the claim. Never replace it with a plausible number or generic “improved” statement.

