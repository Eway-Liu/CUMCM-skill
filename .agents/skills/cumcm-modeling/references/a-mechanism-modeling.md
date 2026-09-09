# Mechanism-first modeling

Use for physical, engineering, geometry, kinematics and differential-equation problems.

1. Define coordinates, bodies, state variables, connection/constitutive relations, units, initial conditions and boundary conditions.
2. Derive governing relations from geometry, balance or conservation before choosing a numerical method.
3. Define the physical event before its indicator function. For visibility, collision, coverage, detection or availability, make prose, equation and code use the same objects, segment/domain, activation window and logical operators. Test positive, tangent, endpoint, outside-domain and inactive cases.
4. For multiple actors or intervals, derive aggregation from the real objective. Use the measure of a union for “covered at least once”; sum individual durations only when overlap truly has additive value.
5. Audit every indexed constraint by expanding one small instance. A limit on each vehicle, period or resource must sum over every consuming target and item, not accidentally reset inside another index.
6. Separate model error from solver error. Record discretization/search tolerance, convergence behavior and feasibility tolerance.
7. Estimate only identifiable parameters from named observations. Keep calibration evidence distinct from validation evidence.
8. Validate in this order: hand-checkable configuration; dimensional and conservation checks; limiting/extreme cases; boundary cases near active constraints; grid/tolerance refinement; parameter perturbation.
9. State every realism-reducing assumption and its likely bias. Add complexity only when an observed defect matters to the objective.

The three inspected 2024 A papers support the reusable pattern “path/geometry -> linked-state propagation -> collision/constraint test -> constrained search”; their reduced collision tests still require boundary checks before transfer. See [A-problem patterns](../../../cumcm-shared/references/a-problem-patterns.md) for the frozen evidence locators.
