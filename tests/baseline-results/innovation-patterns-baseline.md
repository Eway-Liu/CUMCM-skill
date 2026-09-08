# Innovation-pattern refinement baseline

## Scenario H4

A fresh evaluator loaded only the pre-refinement `cumcm-modeling` Skill and references routed by it. It did not read the supplied reference documents, tests, reports or git history.

## Observed behavior record

The full response was reviewed. The evidence-bearing decisions are condensed below without changing their meaning.

在 MILP 已可精确求解、且仅剩 48 小时时，不应为了“显得高级”加入 GNN 或 GA。最值得投入的主创新是：在保留精确 MILP 求解的前提下，构建“地块异质产量 + 价格—销量联合不确定性”的情景鲁棒种植模型。它直接修复已知缺陷，且能以有限情景 MILP 继续精确求解。

### 当前基线与已证实缺口

已有模型是可行且精确求解的确定性 MILP，轮作、地块容量、销量等关键约束完整，应作为全篇基线而不是推倒重来。当前可用证据只有：不同地块产量差异明显；未来销量和价格不确定。因此，能够成立的改进方向是将地块产量系数细化到“地块—作物”层面，并把未来价格、销量从单点预测改为联合情景或可信区间。尚未提供历史样本、空间邻接关系、预测标签、概率分布或风险偏好，不能据此声称预测精度、分布概率或真实市场规律。

### 创新候选筛选

| 层级 | 候选 | 修复的明确缺陷 | 前提 | 48 小时结论 |
|---|---|---|---|---|
| B | 地块—作物异质产量系数 | 用统一产量掩盖已诊断出的地块差异 | 能取得或整理各地块、作物的产量数据 | 必做，是模型校正，不宜单独包装为核心创新 |
| C | 有限情景两阶段鲁棒 MILP | 单点价格、销量导致决策对未来波动脆弱 | 有可追溯的价格—销量历史轨迹、预测区间或题设情景 | 选为主创新 |
| 备选 | 概率情景随机/CVaR MILP | 允许控制尾部损失而非只看最坏情景 | 有可信情景权重，且风险偏好可解释 | 只有在概率来源明确时启用 |
| 淘汰 | GNN 预测产量后接 MILP | 表面上处理空间关联 | 明确定义的地块图、充足时序样本、独立验证集 | 缺少节点、边和监督样本；不得加入 |
| 淘汰 | GA 求解或混合 GA-MILP | 无明确缺陷可修复 | 原 MILP 难以精确求解或规模超时 | 已能精确求解，GA 只会失去最优性证据并增加复现实验负担 |

GNN 的前提不是“地块有差异”，而是存在可解释的图结构及足够样本；GA 的前提不是“模型是整数规划”，而是确定性精确方法不适用于目标规模。当前两者都不成立。

### 主创新及最小实验

保留原轮作、地块容量及种植逻辑约束，将统一产量替换为地块—作物产量 (q_{ic})，并以有限的价格—销量联合情景定义各情景利润。主目标最大化所有情景中可保证的最低利润；若原模型保持线性，可继续由精确 MILP 求解器给出 MIP gap 和可行性证据。情景必须保留价格与销量的联合变化，不能逐期独立抽样。

至少比较三组，使用相同数据边界、约束和求解时间上限：A 为原确定性 MILP；B 为仅加入异质产量；C 为 B 加联合情景鲁棒目标。这样可区分数据细化和不确定性机制的贡献。

验证包括：约束回放、求解状态、上下界、MIP gap 和运行时间；各情景利润、最低/平均利润和跨度；最坏情景后悔值；有来源区间内的情景/保守度敏感性；若有有序历史数据，再做时间外测试。概率/CVaR 版本只有在情景权重有来源时启用。

### 可声称、不可声称与放弃规则

实验前只能声称提出了一个可精确求解的异质产量—市场不确定性框架，并在给定有限情景内优化最坏利润。完成对照后，才可在测试情景范围内声称最低利润、后悔值或稳定性改善。不得声称已预测真实未来市场、真实市场必然获利，或 GNN/GA 带来提升。

若四小时内没有可追溯的联合历史、题设区间或专家情景，则退回异质产量模型和透明压力测试；若异质系数无来源则保留原产量并披露限制；若情景模型在同预算下不可行或 gap 不可接受，缩减情景后仍失败则退回 B；若最低利润、后悔值或轻微扰动稳定性没有改善，则不宣称鲁棒决策优势。

## Baseline score

- Gap-first diagnosis and non-algorithm opportunities: pass.
- Relevant cross-category portfolio: pass.
- Explicit seven-dimension screening: partial; most dimensions appear in reasoning but not in a reusable comparison contract.
- Risk and discard/fallback: pass.
- Evidence-strength ladder: partial; pre/post experiment wording is sound, but intermediate evidence levels are not distinguished.
- Falsifiable innovation record: pass for the selected innovation.

Result: **4 pass, 2 partial**. The refinement should preserve the strong rejection of decorative complexity and add only the missing screening and evidence-level structures.
