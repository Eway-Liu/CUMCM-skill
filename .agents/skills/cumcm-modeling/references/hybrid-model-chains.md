# Hybrid model chains

Use this workflow only when the `QUESTION GRAPH` has a hard dependency in which one model's output becomes another model's input. A loose ensemble or two unrelated subquestions is not a hybrid chain.

## 1. Split stages and evidence boundaries

Name each producer and consumer stage. For every stage, state its input, output, assumptions, fitting boundary and validation evidence. Do not let downstream performance conceal an invalid upstream model, or reuse future information through a shared preprocessing step.

## 2. Use only retained evidence

When the fixed shared references contain a relevant precedent, use it only as a conditional design clue. If they contain no structurally matching case, state that no retained historical evidence applies; do not search for or ingest new papers, and do not substitute a topic-name match.

## 3. Layer candidate plans

Use all three layers only when a full plan or candidate comparison is requested:

- **A — robust baseline:** the simplest auditable end-to-end chain.
- **B — competition-strength:** fixes the baseline's main demonstrated limitation without changing everything at once.
- **C — falsifiable innovation:** changes one named mechanism and survives a predefined rejection test.

For a narrow implementation task, keep the requested layer instead of manufacturing three alternatives.

## 4. Freeze every upstream handoff

Create an `UPSTREAM HANDOFF` before building the consumer:

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

The downstream model must reject incompatible units, grain, horizon or version. Save the handoff artifact; prose alone is not reproducible evidence.

## 5. Propagate uncertainty, not only point estimates

Keep a point-estimate chain as the baseline. When uncertainty matters, pass calibrated intervals, weighted trajectory scenarios or a justified uncertainty set. Preserve cross-horizon or spatial dependence; independently sampling every future period usually creates impossible paths. Define how each scenario changes downstream parameters, constraints or objective terms, then compare expected cost, service level, feasibility and regret against the point chain.

## 6. Validate at four layers

1. **Internal correctness:** dimensions, conservation, constraints, solver status and artifact/schema checks.
2. **Stage evidence:** predictive out-of-sample evidence or structural/mechanism checks for each stage.
3. **Comparative evidence:** same-budget baseline comparison plus ablation for each added mechanism.
4. **Uncertainty and end-to-end evidence:** scenario coverage/calibration and downstream decision quality, feasibility, regret or policy stability.

Mark a layer `N/A` only with a reason. A claimed benefit is incomplete when its relevant layer has not been executed.

## 7. Make innovation falsifiable

Use [innovation design](innovation-design.md) for the evidence ladder, screening and falsifiable record. For a chain, the record must also name the changed handoff, propagate its uncertainty, and test both the affected stage and the end-to-end decision.
