# Hybrid forecast-to-optimization baseline

## Isolation

A fresh evaluator loaded only the current `cumcm-global` and `cumcm-modeling` Skills plus references they routed to. It did not read tests, corpus analysis, final reports, git history, or the external reference repository. The run used the H2 prompt in `tests/pressure-scenarios/scenarios.md` before the hybrid-chain improvement was written.

## Verbatim response

> 不建议因“显得创新”直接上深度模型：72小时仅约3个日周期，TFT、LSTM、N-BEATS等很容易过拟合，无法形成可信优势。更稳妥的路线是“小样本预测 + 精确排程 + 风险闭环”。
>
> **问题结构**
>
> 这是“预测驱动优化”的混合问题：
>
> 需求与外生变量 → 未来12小时预测/情景 → 整数生产排程。
>
> 目前缺少实际表、单位、初始库存、逐时产能、生产/库存/缺货成本，以及未来天气、价格和促销是否已知。暂按单产品、外生变量在决策时可获得、缺货视为损失销售建模；若允许延期交付或价格/促销也是决策变量，方程需调整。
>
> **预测候选**
>
> | 方案 | 定位 | 判断 |
> |---|---|---|
> | 24小时季节朴素法 | 必做基线 | 样本极小时稳定 |
> | Ridge/ElasticNet-ARX | 建议主模型 | 使用1、2、3、24阶滞后、小时周期、价格、天气、促销；正则化抑制过拟合 |
> | SARIMAX | 统计候选 | 可解释，但72点下参数必须严格压缩 |
> | 浅层GBDT | 非线性候选 | 仅在滚动验证稳定胜出时采用 |
> | TFT/LSTM等 | 暂不采用 | 样本量不足，模型名不能替代证据 |
>
> 所有缺失填补、标准化和调参只能在各训练窗口内完成；促销峰值不能未经核查当异常值删除。未来天气回测必须使用当时可获得的天气预报，使用事后实况会泄漏。
>
> **排程模型**
>
> 令 \(x_h\in\mathbb Z_+\) 为第 \(h\) 小时产量，\(I_h\ge0\) 为库存，\(s_h\ge0\) 为缺货量：
>
> \[
> I_h=I_{h-1}+x_h-\hat d_h+s_h,\qquad
> 0\le x_h\le C_h
> \]
>
> \[
> \min\sum_{h=1}^{12}(c_h^px_h+c_h^II_h+c_h^ss_h)
> \]
>
> 补充 \(s_h\le\hat d_h\) 和期末库存要求。该问题是小规模MILP，应优先用精确求解器，并报告可行性、最优间隙和约束残差，不必使用遗传算法。
>
> 真正可检验的创新可设为“残差情景驱动的风险排程”：从滚动回测得到12小时误差路径，构造需求情景，在各情景共享生产决策，引入缺货损失的CVaR。它修复“点预测忽略尾部需求、排程易缺货”的缺陷。只有与“同一预测 + 确定性MILP”消融比较后，才能称为创新。实际运行采用滚动时域：每小时更新库存和预测，仅执行当前小时决策。
>
> **验证计划**
>
> 最后12小时封存测试；此前采用扩展窗口滚动回测，绝不随机划分。预测报告MAE、RMSE、WAPE、分预测步误差及区间覆盖率，并与季节朴素法比较。端到端验证更重要：在每个历史起点重新训练、预测、排程，再用真实需求结算总成本、缺货率、服务水平、平均库存和产能利用率。对缺货惩罚、产能、初始库存及预测误差做情景扰动；风险模型与确定性模型使用相同数据和成本。由于样本极少，结论必须标注为短期、小样本有效，不能泛化到周季节性。
>
> **论文呈现**
>
> 按“问题抽象—数据审计—预测比较—MILP建立—风险扩展—滚动联合验证—敏感性—局限性”组织。核心图仅保留：需求与外生变量时序、滚动预测及区间、各预测步误差、12小时产量/库存/缺货排程、风险系数下成本—缺货权衡。核心表包括模型比较、预测指标、排程结果和鲁棒性结果。摘要中的提升幅度、成本和服务水平暂用结果文件占位，拿到数据并实际运行前不填写任何数字。

## Evidence-based score

| Requirement | Result | Evidence |
| --- | --- | --- |
| Stage separation and evidence boundary | Pass | It separates forecasting and MILP scheduling and lists missing data/assumptions. |
| Stage and chain retrieval | Fail | It neither performs focused retrieval nor records honest no-hit results. |
| Candidate layering | Partial | Prediction candidates have baseline/main/alternative roles, but no end-to-end baseline/competition/innovation ladder. |
| Uncertainty handoff | Partial | Residual paths are conceptually propagated, but no named artifact schema, units/grain/version, availability boundary, or fallback is returned. |
| Four-layer validation | Pass | It covers internal MILP checks, rolling forecast evidence, baseline comparison, and end-to-end scenario sensitivity. |
| Falsifiable innovation | Partial | It names the defect, mechanism and ablation, but omits explicit failure risk and discard threshold. |

Observed result: **2 pass, 3 partial, 1 fail**. The improvement should preserve its strong small-sample reasoning and add structure only where the response omitted reusable interfaces.
