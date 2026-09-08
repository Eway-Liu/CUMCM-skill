# Mechanism-first modeling

Use for physical, engineering, geometry, kinematics and differential-equation problems.

1. Define coordinates, bodies, state variables, connection/constitutive relations, units, initial conditions and boundary conditions.
2. Derive governing relations from geometry, balance or conservation before choosing a numerical method.
3. Separate model error from solver error. Record discretization/search tolerance, convergence behavior and feasibility tolerance.
4. Estimate only identifiable parameters from named observations. Keep calibration evidence distinct from validation evidence.
5. Validate in this order: hand-checkable configuration; dimensional and conservation checks; limiting/extreme cases; boundary cases near active constraints; grid/tolerance refinement; parameter perturbation.
6. State every realism-reducing assumption and its likely bias. Add complexity only when an observed defect matters to the objective.

The three local 2024 A papers support the reusable pattern “path/geometry -> linked-state propagation -> collision/constraint test -> constrained search”; their reduced collision tests still require boundary checks before transfer. See `../cumcm/references/a-problem-patterns.md` for evidence locators.

