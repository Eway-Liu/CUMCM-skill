# CUMCM Skill Suite Final Report

Date: 2026-09-08
Branch: `codex/cumcm-skill-suite`
Status: implemented and verified in an isolated worktree

## Outcome

The project now contains four low-coupling, discoverable CUMCM Skills backed by a source inventory, structured problem/paper cards, an explicit bidirectional structure-model index, evidence-linked synthesis, reusable templates/scripts, RED/GREEN pressure tests, a problem-only 2025 A hold-out, a separately isolated post-release paper review, and an independently rewritten hybrid forecast-to-optimization workflow.

The system transfers decision rules rather than memorized topic-to-algorithm mappings: formalize the real event and constraints, choose a structure-compatible baseline, justify added complexity, execute failure-mode-specific validation, design only purpose-led figures, and keep every manuscript claim traceable to a current artifact.

## Skill Tree

```text
.agents/skills/
├── cumcm-global/          # 1 entry + 5 references + 2 templates + metadata
├── cumcm-modeling/        # 1 entry + 8 references + 3 templates + 2 scripts + metadata
├── cumcm-visualization/   # 1 entry + 6 references + 1 template + 2 scripts + metadata
├── cumcm-thesis/          # 1 entry + 7 references + 4 templates + metadata
└── cumcm/                 # internal corpus toolkit; no SKILL.md, so not a fifth Skill
    ├── references/        # evidence-linked 2024 patterns
    └── scripts/           # inventory, retrieval, corpus and suite validation
```

The four entrypoints contain 494, 459, 342 and 365 words respectively. Detailed knowledge stays in conditionally routed references. The suite validator found no broken links/artifacts, scaffold markers, oversized entrypoints, unexpected discoverable Skill, or duplicated detailed entrypoint knowledge.

## Corpus Summary

### Local 2022–2025 inventory

The deterministic source inventory contains **59 files**:

| Class | Count |
| --- | ---: |
| Official problem statements | 12 |
| Attachments/templates | 34 |
| Local 2024 papers | 10 |
| Other format/instruction files | 3 |

Formats: 32 XLSX, 22 PDF, 3 DOC and 2 GIF. Generated files, caches, symlinks and recognized 2025 A solution material are excluded from this reusable inventory.

### Structured evidence

- 18 problem cards cover 2020–2025 A/B/C. The 12 local 2022–2025 statements are supplemented by six 2020–2021 statement cards from a pinned repository mirror; their uninspected attachments remain metadata-only.
- 10 paper cards cover every user-selected local 2024 paper: 3 A, 3 B and 4 C. Together they contain 39 explicit subquestion records; every record exposes Goal, Variables, Assumptions, Data Processing, Baseline, Model, Algorithm, Validation, Visualization and Main Result, followed by separate Strong Points, Weak Points, Transferable Patterns and Problem-Specific Tricks.
- The 2024 papers total 513 pages. Page-aware extraction found readable text on every page; representative equation/result/validation pages were inspected, with unreadable visual details left `unverified`.
- The evidence ledger contains 44 unique records: 18 problem statements, 10 local paper PDFs, 10 local attachment groups and 6 attachment-metadata records.
- `corpus/corpus-analysis.md` and two compact evidence-linked pattern references preserve cross-paper synthesis without copying paper language.
- `.agents/skills/cumcm/references/bidirectional-index.md` supports both problem-structure -> model-family and model-family -> problem-structure lookup, with use/avoid conditions and local evidence; unsupported structures return no corpus case rather than a fabricated analogy.

The user-supplied 2025 A validation paper is deliberately **not** in the reusable paper corpus or search index. Its SHA-256, extraction boundary and findings are isolated in `tests/holdout-2025a/post-release-paper-review.md`.

## Extracted Patterns

1. **Structure precedes algorithm.** The 2024 A papers formulate geometry/kinematics and collision constraints; B papers formulate sampling and decision/profit graphs; C papers formulate plot-year crop allocations and operational constraints before their search layer.
2. **Solver names are not validity evidence.** Search or heuristic methods occur in all ten papers, but recurrence does not justify a GA/SA/ACO default. Exact/deterministic baselines, feasible encodings, budgets, repeated seeds and bounds remain necessary.
3. **Validation must match the failure mode.** Geometry needs dimensional, boundary, collision/event and refinement checks; stochastic decisions need scenarios or resampling; allocations need constraint replay and objective trade-offs.
4. **Uncertainty is common but assumption-sensitive.** Seven B/C cards add defect, demand, yield, cost, price or interaction uncertainty. Their frequency does not validate a particular distribution, risk coefficient or simulated relationship.
5. **Figures need a decision purpose.** Six cards supported identifiable geometry/state, decision-flow or plan/risk questions. Figure details in the remaining four were not guessed.
6. **Paper claims require artifact parity.** One 2024 A abstract contains a speed-unit conflict. The post-release 2025 review exposed event-predicate, overlap, resource-index, solver-evidence and percentage/figure-text conflicts. These became explicit cross-artifact audit rules, not copied solution methods.

## Skill Responsibilities

| Skill | Owns | Explicit boundary |
| --- | --- | --- |
| `cumcm-global` | complete source reading, `PROBLEM BRIEF`, `QUESTION GRAPH`, stage routing, seven hard gates, final consistency review | does not teach specialist algorithms, style plots or recompute paper results |
| `cumcm-modeling` | data audit, mathematical formalization, model candidates, baseline, solver/implementation, validation, sensitivity, robustness and uncertainty | does not choose manuscript narrative or publication styling |
| `cumcm-visualization` | question-led EDA, chart choice, scientific plots, tables/flows, export and visual audit | does not select/refit the underlying model or plot every field by default |
| `cumcm-thesis` | evidence-traceable structure, abstract/analysis, assumptions/notation, equations, result interpretation, evaluation, LaTeX and review ledger | does not invent, recompute or silently reconcile missing model/results |

Contracts connect the stages: `PROBLEM BRIEF` and `QUESTION GRAPH` -> `MODEL SUMMARY` -> `FIGURE REQUEST`/figure manifest -> traceable paper sections -> `FINAL CONSISTENCY REVIEW`.

## Pressure Test Results

Eleven original scenarios test orchestration, six modeling risks, innovation, visualization and thesis behavior.

| Stage | Result | Interpretation |
| --- | ---: | --- |
| No-Skill RED baseline | 9/11 pass, 2/11 fail | Existing model behavior was already strong on orchestration/modeling and T2; it failed purpose-free visualization V1 and generic abstract T1. No false failures were invented. |
| Four-Skill GREEN | 11/11 pass | The Skills preserved all nine good behaviors and closed V1/T1 without new rationalizations. |
| Post-release H1 regression | 4/4 required defects identified | Before the final refactor, a fresh agent already caught predicate mismatch, interval double counting, mis-indexed shared resources and overclaimed convergence. References were only hardened to make these invariants explicit. |
| Hybrid-chain H2 RED | 2 pass, 3 partial, 1 fail | The baseline lacked stage-plus-chain retrieval, a durable uncertainty handoff, complete candidate layers and an innovation rejection rule. |
| Hybrid-chain H2 GREEN | 6/6 pass | A fresh blind evaluator produced staged retrieval with honest no-hit behavior, A/B/C candidates, versioned trajectory handoff, four-layer validation and a numeric discard rule. |

The final suite contains 24 passing Python tests for inventory, corpus retrieval/validation, mixed-link search with honest no-hit behavior, table profiling, validation helpers, plot helpers and Skill-suite contracts.

## External Reference Boundary

The public `math-modeling-skill-pro` repository was inspected only as a design reference. Its license is proprietary and reserves rights, so no case, template, code scaffold, script or prose was copied. The user-selected general ideas—mixed-link retrieval, candidate layering, forecast uncertainty propagation, four-layer validation and falsifiable innovation—were independently expressed within this suite's existing low-coupling contracts. The source and adoption/rejection boundary are recorded in `docs/reference-audits/2026-09-08-math-modeling-skill-pro.md`.

## 2025 A Hold-out Result

### Pre-release problem-only phase

A fresh agent received only the four Skills, the official 2025 A statement/card and official blank templates. It did not receive solution papers, expert review, corpus analysis or prior test results. The frozen independent artifact has SHA-256 `419431988af12c9c28dd937cd6e7220cedd5ba0b28154cf41fcb94e263101d1d`.

It passed **10/10 design dimensions**: problem type, dependency graph, candidates/exclusions, baseline, full formulation, algorithm/artifacts, validation, sensitivity/robustness, figure/table plan and paper structure. It modeled trajectories and constraints, distinguished a point-target baseline from a finite-cylinder interpretation, used temporal unions for multi-cloud coverage, audited shared resources, and withheld all unexecuted numerical claims.

This is a blueprint-level pass, not evidence of a correct numeric answer or contest ranking. No optimizer or workbook export was executed.

### User-authorized post-release phase

After the independent artifact existed, the user supplied a 2025 A paper and authorized its use. Only pages 1–24 were considered; pages 25–83 are code and were excluded. Because the usable text layer was only a watermark, local Vision OCR provided navigation and key pages were visually confirmed.

The paper supports the broad kinematic decomposition and suggests inverse feasibility search plus feasibility-aware hybrid heuristics. It also contains visible inconsistencies: shielding predicates differ across prose/equations/pseudocode; multi-cloud durations are summed; a per-UAV resource limit is indexed per missile; one convergence trace is overinterpreted; and Q2 methods/numbers/percentage claims conflict across abstract, prose and Figure 7. The independent blueprint avoids those defects at the formulation/evidence level. Full findings and the small Skill refactor are in `tests/holdout-2025a/post-release-paper-review.md`.

## Skill Discovery Result

OpenAI's current documentation states that Codex scans `.agents/skills` from the current working directory up to the repository root, and that a Skill consists of a `SKILL.md` with `name` and `description` plus optional scripts/references/assets/metadata: <https://learn.chatgpt.com/docs/build-skills>.

Observable runtime checks:

1. A fresh subagent attached to the original main workspace did not list the four Skills, correctly reflecting that they existed only in the isolated worktree at that moment.
2. An ephemeral Codex CLI session launched with the Skill-suite worktree as its working directory listed all four by name and project-local mapped path: `cumcm-global`, `cumcm-modeling`, `cumcm-thesis`, and `cumcm-visualization`.

Therefore project-local discovery is verified, not inferred from file presence. A fresh Codex task launched in the integrated repository will discover them; the already-running desktop task does not retroactively change its startup catalog across a different worktree.

## Verification Evidence

The final integration run passed all of the following before the implementation status was closed:

- corpus validator;
- explicit paper-card schema validation for all 39 A/B/C subquestion records and four transfer/limitation fields per card;
- four-entry Skill-suite validator;
- bundled quick validator for each discoverable Skill;
- full Python test suite with headless matplotlib;
- independent hold-out hash and ten-section structure check;
- reusable-corpus audit confirming no 2025 A solution evidence;
- `git diff --check`; the worktree is required to be clean after the final commit.

## Known Limitations

1. Cross-paper pattern evidence comes from ten local 2024 PDFs, not the full CUMCM literature and not evidence saturation.
2. The six 2020–2021 cards use a pinned public mirror; attachment contents were not downloaded, and official-host identity was not independently confirmed.
3. Five 2024 PDFs lacked usable CJK glyphs in the alternate renderer. Native PDFKit text was readable, but unreviewed equations/tables/figures remain `unverified` and paper code/results were not reproduced.
4. The user-supplied 2025 paper's award/provenance status was not independently verified. Pages 1–24 were OCR-assisted and visually sampled; pages 25–83 were intentionally not analyzed.
5. The 2025 A hold-out is a detailed formulation and verification plan, not an executed numerical solution. Its finite-cylinder shielding convention is a declared modeling choice because the official statement does not supply a complete formula.
6. Structure-aware retrieval honestly returns no cases for unsupported queries; for example, the current ten-paper corpus does not evidence every small-sample nonlinear prediction scenario.
7. Helpers are intentionally small and reusable. They do not replace domain-specific solvers, full uncertainty models, workbook semantics or visual inspection.
8. Work is committed on an isolated branch so the user's unrelated dirty main-workspace changes remain untouched. Integration into the main workspace is a separate branch handoff step.
