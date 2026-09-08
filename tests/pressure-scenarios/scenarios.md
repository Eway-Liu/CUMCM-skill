# CUMCM Pressure Scenarios

## M1 Simple linear prediction
Given 24 observations with one predictor, near-linear scatter, homoscedastic residuals, and a need for coefficient interpretation, recommend a baseline, a main model, and validation. Do not assume additional data.

## M2 Time-series split
Given 60 monthly observations with trend and annual seasonality, design train/validation/test evaluation and explain why the split is valid.

## M3 Evaluation model
Rank six alternatives on eight partly correlated indicators, including benefit, cost, and interval-preferred indicators. Choose weights and test ranking stability.

## M4 Linear integer optimization
Allocate integer quantities across five facilities under linear capacity, demand, and budget constraints. Choose a solver strategy and baseline.

## M5 Heuristic stability
A nonconvex routing heuristic is proposed. Specify repeated-run, baseline, feasibility, convergence, and stability evidence.

## M6 High R-squared
A regression reports training R-squared of 0.99. Decide whether it is reliable and list the next checks.

## V1 Purpose-free plot
The user says: "把所有字段都画一遍，越炫越好。" Respond with a figure plan.

## T1 Abstract
Write an abstract blueprint for a four-question modeling problem without numerical results.

## T2 Strengths and limitations
Evaluate a capacity-constrained transportation model that assumes deterministic travel times.

## C1 Innovation claim
A solution combines PCA and XGBoost. Decide whether that is an innovation and design a verification test.

## O1 Orchestration and stage gates
请帮我分析一道四问的 CUMCM 题。题目正文和 Excel 附件已经提供，但我还没有说明要先建模、写代码还是写论文。你拿到材料后的第一轮工作应该输出什么？哪些条件满足后才能进入代码、作图和论文定稿？

## H1 Cross-artifact event and aggregation audit
A draft defines shielding in prose as a cloud blocking the missile-to-target line of sight, in its objective as missile-to-cloud distance within the radius, and in code as the OR of line distance, missile distance and path intersection. It sums individual cloud durations, encodes “at most three bombs per UAV” as `sum_k x[j,k,m] <= 3` for every UAV and missile, and uses one flat stochastic convergence trace to claim global optimality, sensitivity, accuracy and robustness. Audit the model and give the minimum corrected mathematics and evidence.

## H2 Forecast-to-optimization chain
There are 72 hourly demand observations with price, weather and promotion fields. Forecast the next 12 hours, then feed the forecast into an integer production schedule with inventory balance, capacity and shortage penalties. No actual table has been supplied. Under contest time pressure, the user asks for the most advanced model and an innovative-looking solution. Provide a complete plan, candidate comparison, validation and paper presentation. Check whether the response: (1) separates the two stages and their evidence boundaries; (2) retrieves analogues per stage and for the chain without inventing no-hit evidence; (3) distinguishes baseline, competition-strength and falsifiable-innovation candidates; (4) passes a named forecast artifact with grain, units and uncertainty into optimization; (5) validates internal correctness, stage evidence, comparative gain and uncertainty/end-to-end decisions; and (6) gives every innovation a baseline defect, changed mechanism, expected benefit, failure risk, test and discard rule.

## H3 Claim-evidence-limit writing
A production-scheduling paper compares baseline A with plan B. `results.json` reports mean cost 100 versus 96 ten-thousand yuan, B wins 7 of 12 rolling windows, and worst-window cost is 130 versus 145. Demand errors are assumed independent, but no cross-month correlation or significance test was run. Rewrite the draft claim “B significantly reduces cost and is universally applicable,” the result analysis, model evaluation, limitations and delivery review. Check whether the response: (1) preserves source and units and computes change correctly; (2) separates claim, evidence and limit; (3) asks what the result answers, how it compares, its practical meaning and when it reverses; (4) records each material assumption's necessity/basis, affected relation or bias, and validation; and (5) names data or tests needed before recalibration instead of inventing support.
