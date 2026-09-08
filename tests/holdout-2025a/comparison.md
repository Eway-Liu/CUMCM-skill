# 2025 A pre-release problem-only hold-out assessment

Test date: 2026-09-08
Embargo state at scoring time: retained. This assessment used only the official problem statement, the three official blank result templates, and the independent response produced from the four Skills. No 2025 A solution paper, excellent paper, expert review, hidden solution note, or post-hoc method comparison was read. A later user-authorized paper review is isolated in `post-release-paper-review.md` and does not alter this score.

## Evidence boundary

| Source | Role | SHA-256 |
| --- | --- | --- |
| `2025试题/A题/A题.pdf` | coordinates, motion rules, resources, objectives, five questions | `a37f6aad30b16ea09da9cb320ce194b12d3a28874008cf9ff19549f6c6079447` |
| `2025试题/A题/附件/result1.xlsx` | Q3 output schema | `af04b16e6a4719628971bcf5a03d230c9da6738e67eebac9276d254fdd4df1a7` |
| `2025试题/A题/附件/result2.xlsx` | Q4 output schema | `c681d5e378538f71c77fca199a3ca8303a04dbcfc7bd95f870ae22f01ab69f91` |
| `2025试题/A题/附件/result3.xlsx` | Q5 output schema and missile assignment field | `b648c82d63e459ba6e6b3711ae79875e373521cd543b45571c4d8ff1ad5ec54a` |

The submitted artifact is [independent-solution.md](independent-solution.md), frozen with SHA-256 `419431988af12c9c28dd937cd6e7220cedd5ba0b28154cf41fcb94e263101d1d`. The evidence files are unchanged; hashes match the source inventory.

## Ten-output rubric

| Dimension | Finding | Verdict |
| --- | --- | --- |
| 1. Problem type | Correctly distinguishes Q1 mechanism calculation, Q2 nonsmooth continuous optimization, Q3/Q4 interval-union coordination, and Q5 mixed allocation/trajectory optimization. | Pass |
| 2. Dependency graph | Separates hard shared physics from soft reuse of Q1 checks and Q2 candidate generation; it does not add single-cloud optima for Q3–Q5. | Pass |
| 3. Candidates and exclusions | Gives a point-target baseline, a finite-cylinder main interpretation, deterministic search and candidate-plan MILP; excludes unsupported CFD, learning, TOPSIS, and decorative 3D evidence with reasons tied to the problem. | Pass |
| 4. Baseline | Defines a line-segment distance baseline and transparent greedy extensions for Q3–Q5, so the main model has a falsifiable comparison. | Pass |
| 5. Main model | Defines missile, UAV, projectile, and cloud trajectories; variables, units, objectives, ground/explosion, speed, count, assignment and one-second spacing constraints; uses interval-union duration rather than overlapping sums. | Pass |
| 6. Algorithm and artifacts | Separates the physical evaluator from continuous search and Q5 discrete coverage optimization, lists reproducible outputs, and limits any optimum claim to the candidate library/grid unless a bound is available. | Pass |
| 7. Validation | Includes the exact Q1 release/explosion coordinate anchor, dimensional and endpoint cases, line-versus-segment checks, mesh/time refinement, constraint replay, interval bounds, and solver-gap or multi-seed evidence. | Pass |
| 8. Sensitivity and robustness | Separates parameter uncertainty, sensitivity, and strategy robustness; tests the undefined shielding threshold, Q5 objective choice, assignment interpretation, and timing/position perturbations without inventing probability laws. | Pass |
| 9. Figures and tables | Every proposed figure answers a named geometry, timing, overlap, allocation, convergence, or robustness question; it requires source artifacts, units, accessibility and non-perspective geometry checks. | Pass |
| 10. Paper structure | Follows the actual dependency graph, preserves result-key placeholders, distinguishes official facts from model choices, and includes a claim/evidence consistency review. | Pass |

Structural result: **10/10 rubric dimensions passed**. This score measures whether the four-Skill system generated a complete, problem-specific, auditable solution blueprint under embargo. It is not a score for numerical correctness, contest ranking, or global optimality.

## Constraint audit

- The official missile speed, initial coordinates, target geometry, UAV coordinates, UAV speed range, fixed post-assignment heading/speed, gravity-driven projectile motion, 3 m/s cloud descent, 10 m radius, 20 s lifetime, one-second same-UAV release spacing, per-question UAV/bomb counts, and three template destinations are all represented.
- The Q1 anchor is independently derivable from the statement: release at `(17620, 0, 1800)`, explosion time `5.1 s`, and explosion point `(17188, 0, 1800 - 0.5*g*3.6^2)`. The response correctly labels the optional `g=9.8` substitution as a proposed convention rather than an official result.
- The response does not report a Q1 duration or any optimized strategy because it did not execute the solver. This is honest and keeps the hold-out at blueprint level.
- Template-specific per-row duration ownership and Q5 missile weighting are explicitly marked as interpretations because the statement and blank templates do not define them uniquely.

## Residual risks and limitations

1. The official statement does not define the exact finite-cylinder “effective shielding” predicate. Full visible-surface occlusion, center-line occlusion, and partial occlusion can produce different durations. The response makes this ambiguity visible and proposes threshold sensitivity, but only an adopted convention can be computed.
2. Surface/ray sampling is an approximation. It needs convergence checks or an independent geometric verifier before numerical claims are trusted.
3. The Q5 candidate-plan MILP is exact only for its generated plans and time grid. Candidate enrichment, continuous-time replay, bounds/gaps, and cautious wording remain required.
4. The one-target-per-bomb assignment is justified by the output template, not by physics. The proposed cross-missile incidental-coverage comparison is necessary.
5. No numerical optimizer, workbook export, or figure was executed in this hold-out. Therefore feasibility of an actual returned strategy, output-file validity, achieved duration, robustness, and optimality remain unverified.
6. This embargo-preserving assessment cannot measure similarity to a 2025 A excellent solution or expert review. That comparison is intentionally unavailable and must not be inferred.

## Hold-out conclusion

The system passed the intended design-level hold-out: it transferred general mechanism-first modeling, baseline discipline, interval-union accounting, validation, uncertainty, figure-purpose, and evidence-traceable writing rules to an unseen problem without importing a historical solution recipe. A separate execution test would be required to claim a correct numerical solution.
