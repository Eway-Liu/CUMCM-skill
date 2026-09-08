# Common modeling errors

| Error | Correction |
|---|---|
| Topic keyword directly selects an algorithm | Reconstruct the mathematical structure and prerequisites |
| Complex model has no baseline | Compare under the same split, metric and budget |
| Time series is randomly shuffled | Use forward chronological validation |
| Entropy weight is treated as importance | Separate data dispersion from stakeholder preference |
| Metaheuristic is used for a tractable MILP | Try an exact solver and report the bound/gap |
| Best stochastic run is reported alone | Report seeds, feasible rate, distribution and fair baseline |
| High training R-squared is called reliable | Audit leakage, residuals and out-of-sample behavior |
| Calibration is called validation | Reserve independent cases or structural checks |
| A+B is called innovation | Name a defect and isolate the added mechanism by ablation |
| Result is mathematically valid but not interpretable | Translate magnitude, units, constraints and validity range back to reality |

