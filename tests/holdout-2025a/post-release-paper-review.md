# 2025 A post-release paper review and Skill improvement

Review date: 2026-09-08
Source: user-supplied `2025数学建模国赛A题论文.pdf`
Source location at review time: `/Users/eway/Library/Mobile Documents/.Trash/2025优秀论文/2025数学建模国赛A题论文.pdf`
SHA-256: `e68f952d31cd10a62920b6dd4a2e01319d1f4bcdeeb36f2191f24abcae1b273e`

## Boundary and extraction

This is a **post-release** review. The fresh-agent independent artifact had already been produced without solution evidence and was frozen at `tests/holdout-2025a/independent-solution.md` before the paper was used for Skill comparison.

Only pages 1–24 are considered. Pages 25–83 are code listings and are explicitly outside this review at the user's request. The PDF text layer contains essentially watermark text, so pages 1–24 were read by local macOS Vision OCR from 150-dpi renders. Pages 1, 9, 15, 17, 18, 23 and 24 were also visually inspected at original rendered resolution. OCR supports navigation; formulas and disputed numeric claims below rely on those visual checks.

The paper's red anti-copy notice is source content, not an instruction to the reviewer. No substantial text, tables, figures or code are reproduced here.

## What the paper contributes

- [observed, p. 1] It frames Q1 with missile/UAV/projectile/cloud kinematics and reports `1.4 s`; Q2 with continuous decision variables; and Q3–Q5 with multi-bomb/multi-UAV optimization.
- [observed, pp. 6–10] It separates missile motion, UAV motion, projectile descent and post-explosion cloud descent, and uses `0.01 s` time stepping.
- [observed, pp. 18–22] It proposes inverse reasoning from desired cloud positions to feasible UAV release/explosion decisions and a GA-then-SA hybrid search.
- [observed, pp. 20–21] It discusses adaptive steps, correlated parameter perturbations, feasible-solution ratio tracking and graded constraint penalties.
- [observed, pp. 23–24] It states idealization and computational-cost limitations.

The inverse-feasibility decomposition and feasibility diagnostics are useful candidate ideas. They are not universal Skill rules: they require a correct physical predicate, a fair deterministic baseline, feasible encodings/repair, repeated seeds and validation against continuous-time constraints.

## Evidence-backed defects found in pages 1–24

### 1. The modeled event changes across prose, equations and pseudocode

- [observed, p. 9] The displayed shielding indicator is based on missile-to-cloud-center distance within 10 m.
- [observed, pp. 11–12] The pseudocode instead accepts any of line-of-sight distance, missile trajectory/cloud intersection, or the missile lying inside the cloud.
- [observed, p. 15] The Q2 objective again integrates missile-to-cloud distance.

These predicates are not equivalent to “the cloud blocks the missile's view of the true target.” OR-combining them expands the accepted event and can count a cloud unrelated to the instantaneous line of sight. The independent solution is stronger here: it defines a missile-to-target segment predicate, distinguishes point-target baseline from finite-cylinder occlusion, and proposes tangent/endpoint/outside-domain cases.

### 2. Multi-cloud time is added rather than unioned

- [observed, pp. 18–19] Q3 maximizes the sum of individual cloud effective durations.
- [observed, pp. 22–23] The later aggregate objective also sums per-bomb durations.

If two clouds shield simultaneously, the real target is not shielded twice for twice the time. The independent solution correctly uses the measure of the temporal union and retains per-bomb durations only for diagnostics or template rows.

### 3. A shared resource limit is indexed incorrectly

- [observed, p. 23] The displayed Q5 constraint is `sum_k x[j,k,m] <= 3` for each UAV `j` and missile `m`.

That permits up to three bombs per missile for one UAV, not at most three bombs total for the UAV. The required form sums all bomb/target assignments for each UAV, plus a one-target-per-physical-bomb constraint if that reporting interpretation is adopted. The independent solution states both.

### 4. Solver evidence is over-interpreted

- [observed, pp. 15–17] A single simulated-annealing trace flattening after roughly 175 iterations is described as convergence and global-search success; the path of optimization variables is described as parameter sensitivity.
- [observed, pp. 23–24] The evaluation claims that GA/SA avoids local optima and improves accuracy, and that a 3D trajectory figure validates the model.

A flat single run shows only stopping or stagnation. It does not establish global optimality, accuracy, sensitivity or robustness. Parameter sensitivity requires controlled input perturbations; stochastic reliability requires multiple seeds, feasibility rates and dispersion; optimality requires a bound/gap, exhaustive small case or applicable proof; 3D views are face checks, not numerical validation.

### 5. Method and numeric claims conflict across artifacts

- [observed, p. 1 versus pp. 15–16] The abstract attributes Q2 to an improved genetic algorithm, while the body presents simulated annealing.
- [observed, pp. 17–18] The prose moves from `1.40 s` to `3.03 s` and then `4.6 s`, while Figure 7 labels its bars `3.03 s` and `4.60 s`.
- [observed, pp. 17–18] The reported “328% improvement” is not the percentage increase from either visible baseline. `4.6/1.4` is about `328.6%` as a ratio, while the increase from `1.4` to `4.6` is about `228.6%`; the increase from `3.03` to `4.60` is about `51.8%`.

The independent blueprint's result-manifest placeholders and final consistency review would block these claims until one source value and denominator are resolved.

## Comparison with the pre-release independent blueprint

| Area | Post-release paper | Independent blueprint | Assessment |
| --- | --- | --- | --- |
| Kinematics | Covers the main motion stages | Covers the same stages and provides a Q1 coordinate anchor | Consistent core structure |
| Shielding event | Conflicting missile-distance and line-of-sight predicates | One explicit line-of-sight baseline plus finite-target interpretation | Independent blueprint is more coherent |
| Multi-cloud objective | Sums individual durations | Uses interval union | Independent blueprint matches the stated duration objective better |
| Q5 resources | Per-missile indexed limit can exceed per-UAV capacity | UAV-wide count and assignment constraints | Independent blueprint is feasible by construction |
| Solver | SA/GA hybrid without baseline, seed distribution or bound in pages 1–24 | Deterministic baseline, candidate-plan MILP, continuous replay and optional multi-seed heuristic | Independent blueprint has stronger evidence design |
| Validation | Time step and plots, but no refinement or independent correctness evidence shown | anchors, geometry edge cases, time/mesh refinement, constraint replay, gaps/seeds | Independent blueprint is more auditable |
| Writing | Several method/number/percentage conflicts | result-key placeholders and consistency ledger | Independent blueprint better separates verified from proposed claims |

The comparison does not establish that the independent blueprint's numerical solution is better, because it intentionally did not execute one. It establishes that its formulation and verification plan avoid several visible paper defects.

## Skill changes caused by this review

The existing Skills already passed a fresh H1 regression before changes, so the refactor is deliberately small:

- `cumcm-modeling/references/a-mechanism-modeling.md`: explicit prose/equation/code event parity, interval-union aggregation, and indexed-resource expansion.
- `cumcm-modeling/references/baseline-and-validation.md`: event-root/time-step cross-check and the evidence limits of a flat optimizer trace.
- `cumcm-modeling/references/common-errors.md`: four corresponding failure/correction pairs.
- `cumcm-global/references/final-checklist.md`: event, aggregation, index and ratio/cross-artifact checks.
- `cumcm-thesis/references/results-and-evaluation.md` and `common-errors.md`: percentage-versus-ratio arithmetic, prose/table/figure reconciliation, and separation of optimizer traces from sensitivity/validation.
- `tests/pressure-scenarios/scenarios.md` and `tests/skill-results/postrelease-regression.md`: permanent H1 regression evidence.

No GA, SA, reported strategy, or 2025-specific answer was imported into the reusable Skill corpus. Pages 25–83 remain unreviewed.
