# Specialist contracts

## PROBLEM BRIEF

```text
Problem and real-world objective:
Sources read and unresolved gaps:
Subquestion:
Inputs and units:
Outputs and units:
Decision variables:
State variables:
Parameters:
Objective:
Constraints and boundary/initial conditions:
Data source and schema:
Mathematical structure:
Required validation evidence:
```

## QUESTION GRAPH

```text
Nodes: Q1 ... Qn
Edges: producer -> consumer: transferred artifact, schema/version, units/grain, uncertainty, availability/leakage boundary
Shared data/parameters/code:
Independent branches:
Execution order:
```

## UPSTREAM HANDOFF

```text
Producer stage and consumer stage:
Artifact path, schema and version:
Point output:
Uncertainty representation, scenarios and weights:
Units and temporal/spatial grain:
Availability and leakage boundary:
Mapping to downstream variables, constraints or objective:
Fallback and failure behavior:
```

## MODEL SUMMARY

```text
Problem and objective:
Variables and units:
Assumptions:
Baseline:
Main model and equations:
Algorithm and parameters:
Upstream handoffs consumed:
Output artifact, schema and version:
Uncertainty output:
Validation performed, including end-to-end evidence:
Sensitivity/robustness performed:
Saved result artifacts:
Key results:
Limitations:
```

## RESULT_MANIFEST

Producer: `cumcm-modeling`. Consumers: `cumcm-global`, `cumcm-visualization`, and `cumcm-thesis`.

Use the machine-readable [result manifest schema](../../../cumcm-shared/schemas/result-manifest.schema.json). Each artifact has a stable ID, path, format, SHA-256 and verification state. Metrics and validation records reference artifact IDs; uncertainty identifies its representation and backing artifact when present. Missing evidence stays `unverified` rather than receiving a fabricated path or hash.

## FIGURE REQUEST

```text
Purpose/question:
Verified data artifact:
Main message:
Variables and units:
Recommended plot (optional):
Output format:
```

## FIGURE_MANIFEST

Producer: `cumcm-visualization`. Consumers: `cumcm-global` and `cumcm-thesis`.

Use the machine-readable [figure manifest schema](../../../cumcm-shared/schemas/figure-manifest.schema.json). It binds the figure purpose and main message to hashed source result artifacts, visual encodings with units, exported files, and an explicit audit. A failed or incomplete audit remains visible in `audit.status` and `limitations`.

## FINAL CONSISTENCY REVIEW

```text
Model <-> code:
Code <-> result:
Result <-> figure:
Figure <-> text:
Units/symbols/parameters:
Conclusion evidence:
Unresolved blockers or limitations:
```
