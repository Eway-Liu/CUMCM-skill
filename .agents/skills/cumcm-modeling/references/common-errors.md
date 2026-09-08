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
| Prose, objective and code use different event predicates | Freeze one physical event and test its geometry, time window and Boolean logic |
| Individual coverage durations are added despite overlap | Optimize the union measure unless overlap has explicit additive value |
| A resource limit is indexed inside each target | Expand a small instance and sum across every consumer of the shared resource |
| One flat stochastic trace proves optimality or sensitivity | Treat it as one-run stopping behavior; require baselines, seeds, bounds and separate perturbations |
| A+B is called innovation | Name a defect and isolate the added mechanism by ablation |
| A hybrid chain is retrieved with one broad topic query | Search every stage's structure and the whole chain; preserve no-hit results |
| A point forecast is passed downstream as truth | Pass calibrated trajectory scenarios or a justified uncertainty set and retain the point chain as baseline |
| Innovation has no rejection rule | Predefine the failure risk, decisive test, threshold and discard/fallback action |
| Result is mathematically valid but not interpretable | Translate magnitude, units, constraints and validity range back to reality |
