# Post-release regression result

## Scenario H1

After the independent 2025 A artifact was frozen, a fresh agent loaded only `cumcm-global`, `cumcm-modeling`, and their linked references. It did not read the supplied paper, corpus, hold-out output, or prior test results. The adversarial excerpt is recorded in `tests/pressure-scenarios/scenarios.md`.

## Pre-improvement observation

The existing Skills already identified all four required defects:

1. prose, objective and code represented different physical events, and the OR clauses produced false positives;
2. summing individual cloud durations double-counted overlap;
3. `sum_k x[j,k,m] <= 3` reset the shared UAV limit for each missile;
4. one flat stochastic trace established only one-run stopping or stagnation, not global optimality, sensitivity, accuracy or robustness.

It proposed a line-segment/sphere predicate with an activation window, interval-union duration, a UAV-wide sum over bomb and target indices, geometry edge cases, time-step/root-finding cross-checks, multiple seeds, a deterministic baseline, and bounds or small-instance enumeration. Required-observation score: **4/4**.

## Refactor decision

The behavior already passed, so no new algorithm recipe or 2025-specific method was added. The refactor made these high-risk invariants explicit in existing conditional references and final checks: event-predicate parity, overlap aggregation, indexed shared-resource limits, event-time refinement, limits of convergence plots, percentage-versus-ratio arithmetic, and cross-artifact numeric agreement. This is a regression hardening change, not an import of the paper's GA/SA choice.
