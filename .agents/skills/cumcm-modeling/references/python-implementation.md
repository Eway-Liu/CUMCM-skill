# Python implementation contract

Before coding, freeze the formulation and output schema. Then:

- keep source paths and result paths in one configuration block;
- set and record random seeds where randomness exists;
- separate data loading, model logic, solver logic, validation and export;
- centralize parameters, units, tolerances and stopping conditions;
- avoid magic numbers and silent coercion;
- save key results as CSV or JSON and figures separately;
- make constraint and metric checks executable;
- record package/runtime versions when they affect reproducibility.

Prefer the standard library and already-installed NumPy, SciPy, pandas, matplotlib, scikit-learn, statsmodels, NetworkX, SymPy, PuLP/OR-Tools or specialized solvers only when the model requires them. A library's availability is not a reason to use its model.

Use `scripts/data_profile.py` for a read-only first pass over one table. Use `scripts/validation_utils.py` for chronological index splits, regression errors, scalar bound violations and deterministic perturbation grids. These helpers are deliberately small; domain-specific validation stays with the solution.

