# Paper-writing refinement baseline

## Scenario H3

A fresh evaluator loaded only the pre-refinement `cumcm-thesis` Skill and references routed by it. It did not read the supplied reference documents, tests, reports or git history.

## Verbatim response

### 结果分析

由 `results.json` 可知，基线 A 的平均成本为 100 万元，方案 B 为 96 万元。以 A 为基准，B 的平均成本降低 4%（4 万元），表明在当前结果汇总口径下，B 具有降低平均排程成本的潜力。

但平均值优势并未在全部滚动窗口中稳定出现：12 个窗口中，B 仅有 7 个窗口成本低于 A，占比 58.3%。因此，现有结果只能支持“B 在多数已测试窗口中表现更优”，不能推出其对所有需求情景均占优。进一步地，A、B 的最坏窗口成本分别为 130 万元和 145 万元，B 的最坏表现高出 15 万元（相对 A 的最坏窗口成本约高 11.5%）。这提示 B 可能以部分高成本风险为代价取得平均成本下降；但未提供两个最坏值是否对应同一窗口，不能据此作更强的逐窗口因果比较。

此外，当前未进行统计显著性检验，4% 的平均成本差异尚不能表述为“显著降低”。应将结论限定为：在本次 12 个滚动窗口的计算结果中，方案 B 的平均成本低于基线 A，但其窗口层面的优势并不完全稳定，且最坏窗口成本更高。

### 模型评价

方案 B 相对于 A 的可验证优势是平均成本从 100 万元降至 96 万元，绝对降幅为 4 万元。该结果具有明确的工程含义：若研究所采用的成本统计口径与实际生产排程成本一致，B 可作为降低平均成本的候选方案。

不过，现有证据不足以评价 B 的稳定性和普遍适用性。7/12 的窗口胜率说明其优势仅在多数测试窗口出现；145 万元的最坏窗口成本也表明，对高成本情景的控制不能仅由平均成本判断。由于缺少显著性检验，尚不能区分观察到的平均差异是方案效应还是有限窗口样本下的随机波动。因而，原稿中“B 显著降低成本，具有普遍适用性”的表述应删除。

### 局限性与改进方向

模型将各月需求误差设为相互独立。这一设定忽略了订单季节性、市场波动或产能约束传导等因素可能造成的跨月相关性。若实际需求误差存在连续偏高或连续偏低的情形，独立误差假设可能低估连续冲击下的累计成本与排程风险，使模型在具有明显跨月联动的生产环境中的结论有效范围受限。

目前尚未开展跨月相关性检验，因而不能确认独立性假设是否与数据相符；同时也未进行统计显著性检验，无法判断平均成本差异的统计可靠性。后续应先基于需求误差序列检验跨月相关性；若存在相关性，则在情景生成或需求误差模型中保留该相关结构，并重新比较 A 与 B。对成本比较，可补充与滚动窗口配对结构一致的统计检验及区间估计，并单独报告平均成本、窗口胜率和最坏窗口成本，以同时评价平均收益与尾部风险。

### 交付前审查记录

| 主张/数值 | 来源工件与键 | 证据状态 | 单位/符号检查 | 文本一致性 | 处理 |
|---|---|---|---|---|---|
| A 平均成本 100 万元 | `results.json`：平均成本（字段名未提供） | 已给定 | 单位为万元 | 应与表格、摘要一致 | 保留 |
| B 平均成本 96 万元 | `results.json`：平均成本（字段名未提供） | 已给定 | 单位为万元 | 应与表格、摘要一致 | 保留 |
| B 平均成本降低 4% | 由上述两项计算：`(96-100)/100=-4%` | 可复核 | 基准为 A | 不写成“96%降低” | 保留 |
| B 在 7/12 窗口更优 | `results.json`：滚动窗口比较（字段名未提供） | 已给定 | 比例为 58.3% | 不得改写为“所有窗口” | 保留并限定结论 |
| 最坏窗口成本 A 130 万元、B 145 万元 | `results.json`：最坏窗口成本（字段名未提供） | 已给定 | 差额 15 万元 | 不默认二者对应同一窗口 | 保留并注明限制 |
| “B 显著降低成本” | 未提供显著性检验结果 | 未验证 | 不适用 | 与证据不符 | 删除 |
| “B 具有普遍适用性” | 未提供跨场景、稳健性或外部验证 | 未验证 | 不适用 | 与 7/12 窗口胜率不符 | 删除 |
| 月度需求误差独立性 | 模型假设 | 未验证 | 月度误差定义需与模型一致 | 需在假设与局限性中一致 | 披露并补做相关性检验 |
| B 的稳健性 | 未提供扰动、相关需求情景或尾部风险验证 | 未验证 | 不适用 | 不得使用“稳健”表述 | 作为后续验证项 |

## Baseline score

- Source/units/arithmetic: pass.
- Claim-evidence-limit separation: pass in prose, but not a reusable review-ledger shape.
- Four result questions: partial; the comparison and practical meaning are present, but no explicit reversal condition is recorded.
- Assumption audit: partial; affected bias and a test are present, but necessity and supporting basis are not recorded.
- Evidence needed before recalibration: pass.

Result: **3 pass, 2 partial**. The refinement should preserve the strong behavior and add only the two missing structural slots.
