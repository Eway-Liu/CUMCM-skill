# Evidence-gated innovation design

Use this reference when the user asks for innovations, model improvements, a competition-strength candidate portfolio, or a review of an innovation claim. Innovation is an evidenced repair to a consequential baseline defect, not a synonym for complexity.

## Diagnose before generating

Start from executed baseline evidence or an explicit problem requirement. Look for:

- **information loss:** time, space, network, hierarchy, heterogeneity or uncertainty collapsed away;
- **assumption mismatch:** linearity, independence, stationarity, homogeneity or determinism contradicted by evidence;
- **decision gap:** missing capacity, fairness, reliability, operating cost, policy or risk preference;
- **evaluation gap:** averages hide tails, calibration, stability or decision utility;
- **computational gap:** measured infeasibility, runtime, scale or identifiability bottleneck;
- **actionability gap:** a result cannot be explained, transferred to a decision or bounded by uncertainty.

No observed defect means no supported innovation yet. Keep the baseline and state which diagnostic would establish the opportunity.

## Build and screen a small portfolio

When a portfolio is requested, generate three to five non-duplicate candidates across relevant opportunity families—not necessarily one from each:

| Family | Typical change | Admission evidence |
|---|---|---|
| Structure | regimes, hierarchy, time/space/network dependence | residual, mechanism or question structure shows omission |
| Model chain | forecast-to-decision, mechanism-plus-residual, surrogate optimization | modules are complementary and their handoff is testable |
| Metric/objective | tail risk, fairness, resilience, action cost | new quantity matches the real objective and has interpretable units |
| Constraint/decision | capacity, logic, reliability, implementability | statement, data or defensible operational requirement supports it |
| Data/feature | mechanism features, lags, dimensionless groups, external evidence | available at decision time, traceable and leakage-safe |
| Solver | encoding, decomposition, repair, warm start, exact-heuristic hybrid | a measured runtime, feasibility or gap problem exists |

Screen every candidate on: problem value; genuinely new information; decisive test; data support; implementation risk within the contest budget; interpretability; and whether it clarifies rather than fragments the paper. Reject a candidate when a prerequisite is missing instead of compensating with a fashionable algorithm.

When a portfolio is requested, return both outputs below. Use `unverified` or `N/A` rather than dropping a field.

1. One screening matrix:

| Candidate/family | Baseline defect/evidence | Problem value | New information | Data support | Decisive test | Budget risk | Interpretability | Paper clarity | Risk tier | Verdict/fallback |
|---|---|---|---|---|---|---|---|---|---|---|

2. The complete falsifiable innovation record below for every selected finalist.

Label implementation risk:

- **low:** existing data/model plus a local change and direct check;
- **medium:** a new structure or chain with controllable interfaces and validation;
- **high:** new data, high-capacity learning, bespoke heuristic or several dependent unverified modules.

Risk labels govern schedule and fallback, not perceived novelty.

## Freeze a falsifiable innovation record

```text
Baseline defect and supporting evidence:
Changed mechanism and mathematical location:
Causal path to the expected practical effect:
Required data and prerequisites:
Controlled comparison or ablation:
Primary metric and decision threshold:
Implementation/data/interpretation cost:
Principal failure risk:
Applicability boundary:
Discard and fallback action:
Current evidence level and allowed wording:
```

Keep data split, constraints, metric definitions and compute budget comparable. For a chain, combine per-module ablation with end-to-end evidence and uncertainty propagation.

## Match wording to evidence

| Level | Evidence available | Maximum defensible wording |
|---:|---|---|
| 0 | idea or mathematical proposal only | “propose” or “design”; no benefit claim |
| 1 | mechanism check or hand-worked case | “behaves as intended in the checked case” |
| 2 | fixed cases or scenarios beat the baseline | “improves the reported cases/scenarios” |
| 3 | controlled ablation across splits/seeds with uncertainty | “the added mechanism contributes within the tested domain” |
| 4 | stress, drift or external-domain evidence plus mechanism explanation | “remains effective across the stated boundary tests” |

Statistical significance, practical importance, robustness and generality are separate claims. Evidence for one does not automatically authorize the others. If the predefined threshold fails, report a failed experiment or extension and execute the fallback; do not lower the threshold after seeing results.
