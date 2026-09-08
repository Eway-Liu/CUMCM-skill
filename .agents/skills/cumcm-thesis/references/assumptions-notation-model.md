# Assumptions, notation and model exposition

## Assumptions

Keep only assumptions that are necessary, simplify the model, and have a plausible basis. For each material assumption, record: necessity, supporting basis, affected equation/constraint, likely bias if violated, and an available check or sensitivity test. Remove common knowledge and statements unused by equations or validation. If no check is currently possible, mark the assumption unverified and bound the affected conclusion.

## Notation

- One symbol has one meaning; define it at first use.
- Keep scalar, vector, matrix, index, random-variable and estimator conventions consistent.
- State units and index ranges.
- Do not expose program variable names as mathematical notation.

## Model establishment

Present reality -> mathematical definition -> derivation -> model equation -> variable meaning. Equations need connective reasoning; do not stack formulas without explaining why each follows.

## Solution description

Name the solver/algorithm, parameters, initial conditions, software, seed when relevant, tolerance, stopping condition and repeated-run protocol. Replace “用 Python 求解得到” with enough detail to reproduce the result. Do not claim reproducibility when code, data or environment is missing.
