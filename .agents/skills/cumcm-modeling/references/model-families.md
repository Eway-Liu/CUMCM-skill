# Model family cards

Use this compact card shape for any candidate: problem solved; formulation; assumptions; use/avoid conditions; inputs/outputs; estimation or solver; validation; strengths/weaknesses; common mistakes; defensible improvement; suitable result requests.

## Regression and structured prediction

- Use linear/regularized regression when effects are approximately additive or coefficient interpretation matters. Avoid unqualified causal claims.
- Use tree ensembles for medium-size structured data with nonlinearities/interactions when out-of-sample prediction matters more than smooth parameter interpretation. Compare with a linear or domain baseline.
- Use neural models only when sample size, representation structure and validation budget justify their capacity; model name is not evidence.

## Time series

Use seasonal naive, regression with time features, ETS, ARIMA-family or state-space candidates according to trend, seasonality, stationarity, exogenous inputs and sample length. Validate chronologically with rolling or expanding windows. Never fit preprocessing or tune on future periods.

## Classification and clustering

For classification, define the positive class, misclassification cost, imbalance handling, calibration need and group/time leakage boundary. For clustering, define distance/representation and stability; visual separation alone is not validation.

## Evaluation and ranking

Use explicit preference weights when stakeholders supply value judgments; objective weighting measures data dispersion, not importance. Handle benefit, cost and interval indicators separately. Examine redundancy and ranking stability. TOPSIS, weighted sums, PCA, fuzzy or grey methods are candidates, not defaults.

## Optimization

Use LP/MILP, convex optimization, network flow, dynamic programming or exact enumeration when their structure applies. Use nonlinear solvers for continuous nonlinear models with stated initialization and optimality checks. Use GA/PSO/SA/ACO only when exact/deterministic methods are unsuitable at the required scale; document encoding, repair, seeds, budget and gaps.

## Simulation and uncertainty

Use Monte Carlo, discrete-event, agent or cellular simulation when randomness/interactions make direct analysis impractical. Define distributions, state transitions, calibration, replications, confidence intervals and scenario validity.

## Graph, differential-equation and geometric models

Define nodes/edges or governing geometry/physics before choosing the solver. Validate topology, units, conservation, boundary cases and numerical refinement. A numerical optimizer is the solution layer, not the governing model.

