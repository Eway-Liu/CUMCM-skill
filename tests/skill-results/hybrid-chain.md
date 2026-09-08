# Hybrid-chain pressure-test result

## Scenario H2

A fresh-context evaluator received the 30-month demand-forecast-to-CVaR-scheduling prompt and loaded only `cumcm-global`, `cumcm-modeling`, and references explicitly routed by them. It did not inspect tests, baseline results, the external reference repository, the audit, or this report.

## RED baseline

The pre-improvement evaluator separated forecasting and scheduling and proposed rolling validation, residual scenarios, CVaR scheduling and one plausible innovation. It did not perform stage-plus-chain retrieval; candidate layering was incomplete; the uncertainty handoff lacked an artifact/schema/grain/version/fallback contract; and the innovation lacked an explicit rejection threshold. Score: **2 pass, 3 partial, 1 fail** across the six H2 checks.

## GREEN observation

1. **Stage and evidence boundaries — pass.** It produced `data audit -> forecast -> joint scenarios -> stochastic scheduling -> end-to-end replay`, with explicit leakage and availability boundaries.
2. **Mixed-link retrieval — pass.** It supplied separate forecast and decision queries plus a whole-chain query, inspected per-stage results first, and explicitly reported that the small-sample monthly forecast stage might have no direct corpus evidence.
3. **Candidate layering — pass.** A was seasonal-naive/point deterministic scheduling, B was a low-capacity dynamic or structural time-series model plus scenario MILP/CVaR, and C changed one decision-aware model-selection mechanism.
4. **Uncertainty handoff — pass.** The versioned handoff named forecast cutoff, six-month grain, point demand, joint scenario vectors and weights, price/promotion paths, units, schema/model versions and consumer rejection conditions. It preserved cross-month dependence rather than independently sampling horizons.
5. **Four-layer validation — pass.** It separated forecast and scenario evidence, optimization internal checks, same-budget comparisons/ablation, and historical end-to-end replay with cost, service, feasibility, regret and empirical CVaR.
6. **Falsifiable innovation — pass.** It named the baseline defect, causal mechanism and small-window overfitting risk; set improvement, prevalence, predictive-degradation, feasibility, stability and compute thresholds; and required fallback to tier B when they failed.

Verdict: **6/6 pass**. No new rationalization was observed.
