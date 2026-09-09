# A-problem patterns: mechanism-first modeling

## Observed 2024 A evidence

- [observed] All three A papers model the Bench Dragon with an equal-pitch spiral, rigid linked benches/handles, position and velocity propagation, collision restrictions, and a tangent-arc turnaround. [ev-paper-2024-a-geometry-path, pp. 1-4; ev-paper-2024-a-dynamic-search-route, p. 1; ev-paper-2024-a-objective-optimization-form, pp. 1-3]
- [observed] The papers use geometric reductions to selected corners/distances or rectangular regions with a separating-axis collision test. [ev-paper-2024-a-geometry-path, pp. 1, 4; ev-paper-2024-a-dynamic-search-route, pp. 1, 13; ev-paper-2024-a-objective-optimization-form, pp. 1-3]
- [observed] The objective-optimization paper includes sensitivity and collision model-check sections, but its abstract contains a speed-unit inconsistency. [ev-paper-2024-a-objective-optimization-form, pp. 1-3, 16-17, 28-29]
- [observed] The third A paper also uses polar spiral kinematics, collision-distance screening, variable-step/bracket search, and targeted validation sections. [ev-paper-2024-a-dynamic-search-route, pp. 1, 13, 16-17, 26, 28-29]

## Mechanism construction checklist

1. [expert-rule] Define coordinates, bodies, connection constraints, initial/boundary conditions, and the quantity whose units are being optimized before choosing a numerical method.
2. [expert-rule] Derive the governing relation from geometry or conservation first. For a linked path, this means path parameterization plus rigid-link closure; for a physical A problem, it means balance/constitutive relations plus boundary and initial conditions.
3. [expert-rule] Maintain a unit table and check every equation dimensionally. Convert inputs once at the boundary and label output units in tables/figures.
4. [expert-rule] Calibrate only identifiable parameters against named observations. Hold out a check configuration when data permit; never treat calibration residual alone as mechanism validation.
5. [expert-rule] Separate the solver from the model: report discretization/search tolerance, feasibility tolerance, numerical error checks, and whether a result changes under refinement.
6. [expert-rule] Test conservation laws where applicable, then limiting/extreme cases (zero speed, straight/large-radius limit, zero forcing, or binding constraint) and perturb material parameters/geometry.
7. [expert-rule] Improve a baseline only by locating a demonstrated defect: a missing boundary condition, overlap test, loss mechanism, or uncertainty source. Re-run both models under identical cases and compare constraint violations as well as objectives.

## Practical validation order

- [expert-rule] Start with a hand-checkable small configuration; then perform full-geometry or full-balance validation near binding constraints; then run sensitivity and robustness experiments. This ordering makes a favorable optimization result auditable rather than merely plausible.
- [expert-rule] If a source's equations, subscripts, table headers, or units cannot be visually confirmed, label the point `unverified` and do not import it as a rule.
