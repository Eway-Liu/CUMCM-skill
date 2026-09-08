# Model selection decision system

Follow this order:

```text
mathematical structure -> data conditions -> objective -> interpretability
-> variable/constraint type -> scale/budget -> uncertainty
-> candidate set -> baseline and validation design -> selection
```

For each candidate, record prerequisites, exclusions, inputs, outputs, assumptions, estimation/solution method, validation, computational cost, and failure risk. Reject a candidate when a prerequisite is absent; do not merely lower its rank.

## Decision prompts

- Prediction: time-indexed or cross-sectional? Trend/seasonality/exogenous inputs? Nonlinearity/interactions? Sample-to-feature ratio? Causal or predictive interpretation?
- Evaluation: indicator direction and scale? Interval targets? Correlation/redundancy? Preference meaning of weights? Ranking uncertainty?
- Optimization: decision variables, objective, constraints, variable types, linearity/convexity, scale, determinism, and feasible-solution check?
- Simulation: state, transition, stochastic inputs, calibration observations, warm-up, replication count, and output uncertainty?
- Mechanism: governing relation, units, initial/boundary conditions, identifiable parameters, discretization, conservation or limiting cases?

Selection evidence is comparative. Use the same eligible data, leakage boundary, objective/metric, feasibility rules and compute budget. Prefer the simpler candidate when performance differences fall within uncertainty or the complex model loses necessary interpretability.

