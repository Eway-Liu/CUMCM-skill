# Results and model evaluation

## Result analysis

Do not repeat every table cell. State the comparison or change, quantify it with a traceable key, give the unit/denominator, and explain what it means in the real problem. Distinguish statistical, numerical and practical significance.

For each conclusion, preserve a compact **claim -> evidence -> limit** chain. Ask four questions: which subquestion does this answer; how does it compare with the baseline, theory or reality; is the difference practically meaningful; and under what observed or plausible condition would it reverse or stop applying? A reversal condition is a boundary to test, not permission to invent a threshold.

Recompute percentage change as `(new - old) / old`; do not call the ratio `new / old` an increase. Resolve disagreements among abstract, prose, table labels and figure annotations before writing a conclusion. An optimizer parameter path is not a sensitivity experiment, and a 3D trajectory illustration is not geometric or numerical validation.

## Strengths

Name the mechanism that creates the advantage. Example: an explicit capacity constraint makes the transport plan executable because no route exceeds available load; this is stronger than “the model is reasonable.”

## Limitations

Name the assumption, its consequence and bias direction, and the affected validity range. State which data or test could challenge it and what must be recalibrated before deployment. Example: deterministic travel time can make tight schedules infeasible under peak congestion and can overstate resource utilization.

## Improvements

Target the named limitation: time-dependent travel times, scenario/stochastic or robust optimization, safety margins, new measurements, or boundary validation. Do not append unrelated advanced algorithms.

Claims of accuracy require held-out/structural checks; robustness requires executed perturbations/scenarios; innovation requires a named baseline defect and ablation.
