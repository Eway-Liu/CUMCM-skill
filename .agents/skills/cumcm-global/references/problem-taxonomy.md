# Problem taxonomy

Classify each subquestion, not just the whole problem. Mixed questions may require more than one label.

| Type | Structural signal | Questions to answer before routing |
|---|---|---|
| Mechanism-driven | Geometry, physics, conservation, differential relations | Governing relation? Initial/boundary conditions? Identifiable parameters? |
| Data-driven | Observed features and a prediction, classification, grouping or inference target | Sampling unit? Leakage path? Sample size? Time/spatial dependence? |
| Optimization-driven | Controllable variables, objective and feasible set | Variable type? Linearity/convexity? Scale? Deterministic or stochastic? |
| Evaluation/decision | Multiple indicators, ranking or choice | Indicator direction? Redundancy? Weight meaning? Ranking stability? |
| Simulation-driven | Random or interacting process without convenient closed form | State transition? Random inputs? Replications? Calibration? |
| Mixed | One layer produces inputs or constraints for another | Which layer owns each assumption and validation check? |

Do not map a label directly to one algorithm. Route the structure and constraints to `cumcm-modeling` for candidate comparison.

