# Uncertainty, sensitivity and robustness

Distinguish the questions:

- **Uncertainty**: what inputs, parameters or scenarios are not known exactly?
- **Sensitivity**: how does an output change when one or more inputs change?
- **Robustness**: does the decision or conclusion remain acceptable across plausible changes?

Use local perturbations such as +/-5%, +/-10% and +/-20% only when they are meaningful for the parameter scale. Otherwise use intervals, scenario analysis, bootstrap, Monte Carlo, distributional assumptions or robust optimization with stated provenance.

Predefine the conclusion-stability metric: sign, ranking, feasibility, target attainment, regret, objective loss or policy change. Report ranges/probabilities and threshold crossings, not only curves.

For stochastic algorithms, separate input uncertainty from optimizer randomness. Hold instances and compute budgets fixed, run multiple seeds, and report feasible rate, best/median/worst, dispersion and gap to a baseline or bound.

