# `cumcm-modeling` pressure-test results

The seven scenarios match `tests/pressure-scenarios/scenarios.md`. Three fresh-context evaluators loaded the completed Skill and only conditionally routed references. No files were edited by evaluators.

## RED baseline

All M1–M6 and C1 no-Skill baselines passed. The Skill therefore preserves those behaviors and adds a reusable decision contract; no fabricated failure was encoded.

## GREEN observations

### M1 — simple linear prediction

The evaluator selected an intercept-only mean baseline and one-predictor OLS, interpreted the slope with units and no causal overclaim, used LOOCV or small-k cross-validation for MAE/RMSE, and requested residual, Q-Q, leverage and Cook-distance checks. It rejected an unsupported high-capacity model for 24 observations.

### M2 — time-series split

The evaluator used a chronological 36/12/12 split, an expanding-origin validation loop, a sealed final 12-month test, seasonal-naive baseline, and training-window-only preprocessing/tuning. It explicitly rejected random shuffling as leakage.

### M3 — evaluation model

The evaluator did not default to entropy-weight TOPSIS. It separated benefit, cost and interval-preferred transformations; distinguished dispersion from importance; handled semantic/correlation redundancy; used stakeholder swing weights or equal construct weights; retained a simple weighted-score baseline; and proposed weight/data/indicator/method perturbations with rank-stability measures.

### M4 — linear integer optimization

The evaluator formulated ILP/MILP, preferred branch-and-bound/cuts with enumeration or dynamic programming as a small-instance check, rejected an unsupported metaheuristic, compared with a feasible deterministic rule, and required integrality, constraint slack, solver status, relaxation bound, optimality gap and scenario checks.

### M5 — heuristic stability

The evaluator required documented multiple seeds, feasible-solution rate, automated route checks, best/median/worst and dispersion, equal-budget greedy/exact-or-bound comparisons, convergence traces, stopping rules and meaningful input perturbations. It separated optimizer randomness from input uncertainty.

### M6 — high training R-squared

The evaluator rejected training R-squared as reliability evidence and required leakage/duplicate/dependence audits, appropriate held-out or cross-validation design, fold-local preprocessing/tuning, simple baselines, out-of-sample errors and dispersion, residual/influence/subgroup checks, and distribution-shift sensitivity.

### C1 — PCA plus XGBoost innovation

The evaluator rejected model-name stacking as innovation. It required a named baseline defect, leakage-safe fold-local PCA, identical-fold/budget comparison with raw-feature XGBoost and simpler baselines, repeated resampling, paired uncertainty, cost/stability reporting and a PCA ablation tied to the claimed benefit.

## Verdict

Pass: M1–M6 and C1 all satisfied the observable requirements. The evaluators reported no new rationalization, so no additional exception or prohibition was added.

