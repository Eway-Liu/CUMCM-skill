# Baseline and validation

## Baseline choices

- Regression: mean/domain rule, then interpretable linear or regularized model.
- Time series: last value, drift, or seasonal naive as structure permits.
- Classification: majority/rate rule plus a simple calibrated classifier.
- Optimization: feasible rule/greedy, relaxation, small-instance enumeration or exact bound.
- Evaluation: equal-weight standardized score before complex weighting/ranking.
- Mechanism: hand-calculable reduced case before the full numerical solver.

## Match validation to failure mode

- Regression: held-out or cross-validated MAE/RMSE/R-squared plus residual, influence and subgroup checks.
- Classification: precision/recall/F1, ROC or PR-AUC as appropriate, confusion matrix and calibration; respect cost and imbalance.
- Time series: chronological rolling/expanding evaluation; no random split.
- Optimization: automatic constraint substitution, bound/gap, infeasibility cases and repeated runs for stochastic solvers.
- Ranking: weight/data perturbation, indicator deletion, method comparison and rank correlation/probability.
- Simulation: replication confidence intervals, calibration/face checks and extreme scenarios.
- Mechanism: dimensions, conservation, limiting cases, boundary conditions and numerical refinement.

For indicator-event durations, compare time-step halving with event-boundary root finding where possible. A flat optimizer trace is only stopping or stagnation evidence; sensitivity needs controlled parameter perturbations, robustness needs executed scenarios, and global optimality needs a bound, gap, exhaustive small case, or applicable proof.

Fit preprocessing, feature selection and tuning only inside training folds. Keep a sealed test set when it affects model choice. Training fit and calibration residuals alone do not validate future or external behavior.

## Four-layer validation for model chains

For an upstream-to-downstream chain, report four distinct layers: (1) internal correctness, including dimensions, constraints, solver status and artifact schema; (2) predictive out-of-sample or structural evidence for every stage; (3) same-budget baseline comparison and ablation; and (4) uncertainty coverage plus end-to-end decision quality, feasibility, regret or policy stability. Mark a layer `N/A` only with a reason. Do not substitute a good downstream objective for missing upstream evidence.
