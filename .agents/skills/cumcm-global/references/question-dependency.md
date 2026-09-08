# Question dependency analysis

For every pair of subquestions, record whether they share:

- raw or cleaned data;
- definitions, units or preprocessing;
- estimated parameters or calibrated state;
- equations, constraints or reusable code;
- results used as a downstream input;
- validation evidence.

Classify the edge:

- **hard dependency**: downstream work cannot be valid without the upstream output;
- **soft dependency**: a shared artifact can be reused but the question remains independently solvable;
- **independent**: no substantive artifact is shared.

Represent the graph in text or Mermaid only when it clarifies branching. For each edge, name the artifact that flows across it. A bare `Q1 -> Q2` arrow is insufficient.

Use the graph to schedule work and prevent two questions from silently using different parameter estimates, data versions, or units.

