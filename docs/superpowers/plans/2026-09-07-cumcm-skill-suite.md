# CUMCM Skill Suite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and verify a four-Skill CUMCM expert system grounded in 2020–2025 A/B/C problems and excellent-paper evidence, with deeper A-problem coverage.

**Architecture:** Project-scoped Skills live under `.agents/skills/` and exchange explicit problem, model, figure, and thesis contracts. A separate `corpus/` evidence layer stores inventories and structured cards; Skill entrypoints load only the references needed for the current task. Python standard-library-first scripts build and validate the corpus, while focused scientific helpers use installed NumPy, pandas, matplotlib, and scikit-learn only when required.

**Tech Stack:** Markdown/YAML, Python 3.11+, pytest, JSON/JSONL, Poppler (`pdfinfo`, `pdftotext`, `pdftoppm`), pandas, NumPy, matplotlib, scikit-learn.

**Spec:** `docs/superpowers/specs/2026-09-07-cumcm-skill-suite-design.md`

## Global Constraints

- Cover all 18 CUMCM A/B/C problems from 2020 through 2025; prioritize A-problem mechanism, geometry, physics, engineering constraints, numerical solution, and validation.
- Analyze only the ten local 2024 excellent papers (3 A, 3 B, 4 C); read their verified text layers directly and do not use OCR outputs or external-year excellent papers as corpus evidence.
- Treat `math-modeling-skill-pro` as read-only research evidence; do not copy its proprietary cards, code, templates, or wording.
- Keep each `SKILL.md` focused on triggers, workflow, gates, routing, contracts, and reference navigation; put detailed knowledge in references.
- Select models from mathematical structure, data conditions, objective, constraints, scale, interpretability, and uncertainty—not from topic keywords.
- Complex models require a meaningful baseline and validation; every paper number must be traceable to a computation result.
- Use 2025 A as a problem-only hold-out and never read its paper solution or expert review in this implementation.
- Create files with `apply_patch`; preserve all existing problem, attachment, and paper files.
- Finish and verify one Skill before writing the next Skill.
- Commit after every independently testable task.

---

### Task 1: Freeze Evidence Boundaries and Record No-Skill Baselines

**Files:**
- Create: `tests/pressure-scenarios/scenarios.md`
- Create: `tests/baseline-results/cumcm-baseline.md`
- Create: `tests/baseline-results/modeling-baseline.md`
- Create: `tests/baseline-results/visualization-baseline.md`
- Create: `tests/baseline-results/thesis-baseline.md`
- Create: `corpus/source-policy.md`

**Interfaces:**
- Consumes: approved design spec and the ten pressure-test classes in the user brief.
- Produces: immutable baseline responses and failure observations used to author each Skill; source-use rules used by every corpus card.

- [ ] **Step 1: Write the pressure scenarios before any Skill exists**

Define ten compact prompts in `tests/pressure-scenarios/scenarios.md`. Each prompt must contain enough data to expose one behavior:

```markdown
## M1 Simple linear prediction
Given 24 observations with one predictor, near-linear scatter, homoscedastic residuals, and a need for coefficient interpretation, recommend a baseline, a main model, and validation. Do not assume additional data.

## M2 Time-series split
Given 60 monthly observations with trend and annual seasonality, design train/validation/test evaluation and explain why the split is valid.

## M3 Evaluation model
Rank six alternatives on eight partly correlated indicators, including benefit, cost, and interval-preferred indicators. Choose weights and test ranking stability.

## M4 Linear integer optimization
Allocate integer quantities across five facilities under linear capacity, demand, and budget constraints. Choose a solver strategy and baseline.

## M5 Heuristic stability
A nonconvex routing heuristic is proposed. Specify repeated-run, baseline, feasibility, convergence, and stability evidence.

## M6 High R-squared
A regression reports training R-squared of 0.99. Decide whether it is reliable and list the next checks.

## V1 Purpose-free plot
The user says: "把所有字段都画一遍，越炫越好。" Respond with a figure plan.

## T1 Abstract
Write an abstract blueprint for a four-question modeling problem without numerical results.

## T2 Strengths and limitations
Evaluate a capacity-constrained transportation model that assumes deterministic travel times.

## C1 Innovation claim
A solution combines PCA and XGBoost. Decide whether that is an innovation and design a verification test.
```

- [ ] **Step 2: Run fresh agents without access to the new Skills**

Dispatch one fresh-context subagent per Skill domain. Give it only the relevant scenarios, explicitly state that `.agents/skills/cumcm*` must not be read, and request complete responses plus reasoning. Save responses verbatim under `tests/baseline-results/`.

- [ ] **Step 3: Score observed failures without inventing failures**

Append a table to each baseline file:

```markdown
| Scenario | Observable behavior | Pass/Fail | Failure pattern that guidance must address |
|---|---|---|---|
```

Only mark failures visible in the response. If a scenario already passes, do not add redundant Skill rules for it.

- [ ] **Step 4: Write the source policy**

`corpus/source-policy.md` must define source classes, evidence labels (`observed`, `inferred`, `expert-rule`, `unverified`), OCR limitations, copyright boundaries, URL/file-path provenance, and the 2025 A hold-out embargo.

- [ ] **Step 5: Verify and commit**

Run:

```bash
test ! -e .agents/skills/cumcm/SKILL.md
rg -n "Pass|Fail|observed|inferred|expert-rule|unverified" tests/baseline-results corpus/source-policy.md
git add tests/pressure-scenarios tests/baseline-results corpus/source-policy.md
git commit -m "test: capture CUMCM skill baselines"
```

Expected: Skills do not exist, all ten scenarios appear in baseline evidence, and the commit contains no generated Skill.

### Task 2: Build the Corpus Inventory and Problem Cards

**Files:**
- Create: `.agents/skills/cumcm/scripts/build_inventory.py`
- Create: `tests/python/test_build_inventory.py`
- Create: `corpus/inventory/files.json`
- Create: `corpus/inventory/coverage.md`
- Create: `corpus/problem-cards/2020-a.md` through `corpus/problem-cards/2025-c.md`
- Create: `corpus/evidence-ledger.jsonl`

**Interfaces:**
- Consumes: workspace root path and local/temporary source paths.
- Produces: `build_inventory(root: Path) -> list[dict[str, object]]`; 18 problem cards with stable IDs `YYYY-A`, `YYYY-B`, `YYYY-C`; JSONL provenance records keyed by `evidence_id`.

- [ ] **Step 1: Write the failing inventory test**

```python
from pathlib import Path
from importlib.util import module_from_spec, spec_from_file_location

def load_module(path: Path):
    spec = spec_from_file_location("build_inventory", path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def test_inventory_classifies_problem_paper_and_attachment(tmp_path):
    (tmp_path / "2024试题" / "A题").mkdir(parents=True)
    (tmp_path / "2024试题" / "A题" / "A题.pdf").write_bytes(b"%PDF")
    (tmp_path / "2024试题" / "A题" / "附件.xlsx").write_bytes(b"PK")
    (tmp_path / "2024优秀论文").mkdir()
    (tmp_path / "2024优秀论文" / "A016.pdf").write_bytes(b"%PDF")
    module = load_module(Path(".agents/skills/cumcm/scripts/build_inventory.py"))
    rows = module.build_inventory(tmp_path)
    assert [row["kind"] for row in rows] == ["problem", "attachment", "paper"]
    assert {row["year"] for row in rows} == {2024}
    assert {row["problem"] for row in rows} == {"A"}
```

- [ ] **Step 2: Run the test and confirm the expected failure**

Run: `pytest -q tests/python/test_build_inventory.py`

Expected: FAIL because `build_inventory.py` does not exist.

- [ ] **Step 3: Implement the minimal deterministic scanner**

Implement `build_inventory(root)` with `Path.rglob`, extension classification, year/problem extraction from path parts, POSIX relative paths, byte size, and SHA-256 for files. Sort with `KIND_ORDER = {"problem": 0, "attachment": 1, "paper": 2, "other": 3}` followed by `(year, problem, path)`. CLI arguments: `--root`, `--output`, `--coverage`.

- [ ] **Step 4: Verify the unit test and scan the real workspace**

Run:

```bash
pytest -q tests/python/test_build_inventory.py
python .agents/skills/cumcm/scripts/build_inventory.py --root . --output corpus/inventory/files.json --coverage corpus/inventory/coverage.md
```

Expected: PASS; coverage lists local 2022–2025 problems, ten local 2024 papers, spreadsheets, images, and document-format files without modifying them.

- [ ] **Step 5: Acquire only missing 2020–2021 A/B/C problem sources**

Use the user-provided `CosmicLinks/cumcm-problems` repository in a temporary directory. Read only the six missing problem statements and required attachment metadata; preserve canonical GitHub URLs and commit hashes in `evidence-ledger.jsonl`. Do not commit third-party PDFs, unrelated years, or D/E problems.

- [ ] **Step 6: Extract and write all 18 problem cards**

For every card use exactly:

```markdown
---
id: 2024-A
year: 2024
problem: A
title: <verified title>
source_evidence: [<evidence-id>]
---
# 2024 A
## Reality and deliverable
## Questions and dependencies
## Inputs, outputs, variables, parameters
## Objectives, constraints, initial and boundary conditions
## Data structure and file schema
## Mathematical structure tags
## Candidate validation evidence
## Extraction limitations
```

Use verified titles and content from the problem PDF. Do not read the 2025 A solution paper or expert review.

- [ ] **Step 7: Verify coverage and commit**

Run:

```bash
test "$(find corpus/problem-cards -name '20??-?.md' | wc -l | tr -d ' ')" = "18"
rg -L "## Questions and dependencies" corpus/problem-cards/*.md
python .agents/skills/cumcm/scripts/build_inventory.py --root . --output corpus/inventory/files.json --coverage corpus/inventory/coverage.md
git add .agents/skills/cumcm/scripts/build_inventory.py tests/python/test_build_inventory.py corpus/inventory corpus/problem-cards corpus/evidence-ledger.jsonl
git commit -m "feat: index CUMCM problems and sources"
```

Expected: 18 cards; `rg -L` prints nothing; the 2025 A evidence ledger contains problem sources only.

### Task 3: Build Paper Cards and Cross-Corpus Analysis

**Files:**
- Create: `corpus/paper-cards/<year>-<paper-code>.md`
- Create: `corpus/corpus-analysis.md`
- Create: `.agents/skills/cumcm/references/excellent-paper-patterns.md`
- Create: `.agents/skills/cumcm/references/a-problem-patterns.md`
- Modify: `corpus/evidence-ledger.jsonl`

**Interfaces:**
- Consumes: the ten local 2024 text-layer PDFs, targeted page renderings used to verify equations/figures/tables, and the source policy.
- Produces: paper cards keyed by paper code; cross-corpus patterns cited by evidence IDs; an A-focused decision reference.

- [ ] **Step 1: Directly inspect the ten local 2024 papers**

Extract the verified text layer without OCR and retain stable page locators. Render and visually inspect representative pages containing the abstract, model diagram/equations, validation, sensitivity, figures, and conclusion. Mark text-layer extraction errors or unreadable formulas, units, and numbers `unverified`; never reconstruct them from OCR output.

- [ ] **Step 2: Create one structured card per local paper**

Use the paper-card contract from the design spec. Every claim about a method, validation, figure, or result must cite a local PDF evidence ID and mark `observed` or `inferred`.

- [ ] **Step 3: Complete balanced 2024 A/B/C coverage**

Analyze all three local A papers, all three local B papers, and all four local C papers. Give A papers deeper attention to mechanism, geometry, constraints, numerical methods, units, and cross-paper disagreement. Do not add external paper cards.

- [ ] **Step 4: Separate observed patterns from expert rules**

Use the reference repository only as prior architectural inspiration. Do not use its case data as corpus evidence. Each retained paper pattern must resolve to one or more local 2024 paper evidence IDs; general modeling guidance must be labeled `expert-rule`.

- [ ] **Step 5: Synthesize transferable rules**

Write `corpus/corpus-analysis.md` with counts by year/problem/source/access quality, mathematical structure, baseline, validation, sensitivity/robustness, figure purpose, abstract pattern, improvement pattern, and evidence limitations. Separate frequency from validity.

Write `excellent-paper-patterns.md` as concise, evidence-linked decision rules. Write `a-problem-patterns.md` around mechanism construction, units, governing relations, boundary conditions, calibration, numerical error, conservation/extreme-case checks, and targeted improvement.

- [ ] **Step 6: Verify and commit**

Run:

```bash
test "$(find corpus/paper-cards -name '2024-*.md' | wc -l | tr -d ' ')" = "10"
rg -n "observed|inferred" corpus/paper-cards
rg -n "2025-A.*solution|A196|烟幕.*论文" corpus/paper-cards corpus/corpus-analysis.md .agents/skills/cumcm/references || true
git add corpus/paper-cards corpus/corpus-analysis.md corpus/evidence-ledger.jsonl .agents/skills/cumcm/references
git commit -m "feat: distill CUMCM paper evidence"
```

Expected: exactly ten local 2024 cards exist; all paper-pattern evidence resolves to those cards; the hold-out scan contains no 2025 A solution evidence.

### Task 4: Implement Corpus Search and Structural Validation

**Files:**
- Create: `.agents/skills/cumcm/scripts/search_cases.py`
- Create: `.agents/skills/cumcm/scripts/validate_corpus.py`
- Create: `tests/python/test_search_cases.py`
- Create: `tests/python/test_validate_corpus.py`

**Interfaces:**
- Produces: `search_cards(cards_dir: Path, query: str, top: int = 6) -> list[dict[str, object]]`; `validate_card(path: Path) -> list[str]`; CLI exit code 0 only when the corpus is valid.

- [ ] **Step 1: Write failing search and validation tests**

```python
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

def load_function(module_name: str, path: str, function_name: str):
    spec = spec_from_file_location(module_name, Path(path))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, function_name)

def write_card(path: Path, body: str) -> None:
    path.write_text(body, encoding="utf-8")

def test_structure_terms_outweigh_topic_words(tmp_path):
    search_cards = load_function("search_cases", ".agents/skills/cumcm/scripts/search_cases.py", "search_cards")
    write_card(tmp_path / "a.md", "---\ntags: [small-sample, nonlinear, regression]\nsource_evidence: [e1]\n---\n# A\nEvidence: observed\nValidation: leave-one-out")
    write_card(tmp_path / "b.md", "---\ntags: [image, deep-learning]\nsource_evidence: [e2]\n---\n# B\nEvidence: observed\nValidation: holdout")
    results = search_cards(tmp_path, "small sample nonlinear prediction", top=1)
    assert results[0]["path"].endswith("a.md")

def test_missing_source_and_evidence_label_are_errors(tmp_path):
    validate_card = load_function("validate_corpus", ".agents/skills/cumcm/scripts/validate_corpus.py", "validate_card")
    card = tmp_path / "paper.md"
    card.write_text("# Card\nModel: ARIMA\n", encoding="utf-8")
    errors = validate_card(card)
    assert "source_evidence" in " ".join(errors)
    assert "evidence label" in " ".join(errors)
```

- [ ] **Step 2: Verify RED**

Run: `pytest -q tests/python/test_search_cases.py tests/python/test_validate_corpus.py`

Expected: FAIL because both modules and functions are absent.

- [ ] **Step 3: Implement minimal structure-aware retrieval and validation**

Use normalized English/Chinese tokens plus explicit boosts for frontmatter tags, problem type, data regime, objective, constraint type, and validation. Topic terms may contribute but must not alone decide the model. Validator checks required headings, source IDs, evidence labels, duplicate IDs, broken local paths, and permanently forbidden 2025 A solution evidence.

- [ ] **Step 4: Run tests and validate the real corpus**

Run:

```bash
pytest -q tests/python/test_search_cases.py tests/python/test_validate_corpus.py
python .agents/skills/cumcm/scripts/validate_corpus.py corpus
python .agents/skills/cumcm/scripts/search_cases.py "小样本 非线性 预测 可解释" --cards corpus/paper-cards --top 6
```

Expected: tests pass, corpus validation exits 0, and search returns evidence IDs rather than model prescriptions.

- [ ] **Step 5: Commit**

```bash
git add .agents/skills/cumcm/scripts/search_cases.py .agents/skills/cumcm/scripts/validate_corpus.py tests/python/test_search_cases.py tests/python/test_validate_corpus.py
git commit -m "feat: add structure-aware corpus retrieval"
```

### Task 5: Implement and Verify the `cumcm` Orchestrator Skill

**Files:**
- Create: `.agents/skills/cumcm/SKILL.md`
- Create: `.agents/skills/cumcm/agents/openai.yaml`
- Create: `.agents/skills/cumcm/references/competition-workflow.md`
- Create: `.agents/skills/cumcm/references/problem-taxonomy.md`
- Create: `.agents/skills/cumcm/references/question-dependency.md`
- Create: `.agents/skills/cumcm/references/final-checklist.md`
- Create: `.agents/skills/cumcm/references/contracts.md`
- Create: `.agents/skills/cumcm/templates/problem-analysis.md`
- Create: `.agents/skills/cumcm/templates/competition-plan.md`
- Create: `tests/skill-results/cumcm.md`

**Interfaces:**
- Consumes: problem cards, corpus search results, and user-selected stage.
- Produces: `PROBLEM BRIEF`, `QUESTION GRAPH`, routed specialist requests, and `FINAL CONSISTENCY REVIEW`.

- [ ] **Step 1: Re-read the orchestrator baseline failures**

Extract only observed routing, decomposition, evidence-boundary, or completion-gate failures from `tests/baseline-results/cumcm-baseline.md`.

- [ ] **Step 2: Initialize the Skill after RED evidence exists**

The `cumcm` directory already contains corpus scripts and evidence references, so do not run the initializer over it. Create `SKILL.md` directly and generate `agents/openai.yaml` with the bundled metadata generator. Read `skill-creator/references/openai_yaml.md` immediately before authoring the metadata.

- [ ] **Step 3: Author the minimal orchestrator**

`SKILL.md` must contain: trigger-only description; problem-reading gate; structured problem brief; question dependency classification; task routing; stage override; seven hard gates; specialist input/output contracts; final model/code/result/figure/text/unit/symbol/parameter/conclusion audit; reference navigation.

- [ ] **Step 4: Run the same fresh-agent scenarios with the Skill**

Dispatch a fresh agent with `cumcm` explicitly loaded and the same orchestrator scenarios. Save its response and pass/fail comparison to `tests/skill-results/cumcm.md`. If it creates new rationalizations, update only the relevant guidance and repeat.

- [ ] **Step 5: Validate and commit before starting another Skill**

Run:

```bash
python /Users/eway/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/cumcm
python .agents/skills/cumcm/scripts/validate_corpus.py corpus
git add .agents/skills/cumcm tests/skill-results/cumcm.md
git commit -m "feat: add CUMCM orchestration skill"
```

Expected: validator passes; Skill output formalizes and routes instead of jumping directly to code.

### Task 6: Implement and Verify `cumcm-modeling`

**Files:**
- Create: `.agents/skills/cumcm-modeling/SKILL.md`
- Create: `.agents/skills/cumcm-modeling/agents/openai.yaml`
- Create: `.agents/skills/cumcm-modeling/references/model-selection.md`
- Create: `.agents/skills/cumcm-modeling/references/model-families.md`
- Create: `.agents/skills/cumcm-modeling/references/a-mechanism-modeling.md`
- Create: `.agents/skills/cumcm-modeling/references/baseline-and-validation.md`
- Create: `.agents/skills/cumcm-modeling/references/uncertainty-sensitivity-robustness.md`
- Create: `.agents/skills/cumcm-modeling/references/common-errors.md`
- Create: `.agents/skills/cumcm-modeling/references/python-implementation.md`
- Create: `.agents/skills/cumcm-modeling/templates/modeling-plan.md`
- Create: `.agents/skills/cumcm-modeling/templates/model-comparison.md`
- Create: `.agents/skills/cumcm-modeling/templates/experiment-plan.md`
- Create: `.agents/skills/cumcm-modeling/scripts/data_profile.py`
- Create: `.agents/skills/cumcm-modeling/scripts/validation_utils.py`
- Create: `tests/python/test_data_profile.py`
- Create: `tests/python/test_validation_utils.py`
- Create: `tests/skill-results/modeling.md`

**Interfaces:**
- Consumes: `PROBLEM BRIEF` and `QUESTION GRAPH`.
- Produces: `MODEL SUMMARY` with objective, variables, assumptions, baseline, main model, equations, algorithm, parameters, validation, sensitivity, results, and limitations.

- [ ] **Step 1: Write failing helper tests**

Create `tests/python/test_data_profile.py`:

```python
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import pandas as pd

def load_module(name: str, path: str):
    spec = spec_from_file_location(name, Path(path))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def test_profile_frame_reports_shape_missing_and_duplicates():
    module = load_module("data_profile", ".agents/skills/cumcm-modeling/scripts/data_profile.py")
    frame = pd.DataFrame({"x": [1.0, None, 1.0], "label": ["a", "b", "a"]})
    result = module.profile_frame(frame)
    assert result["shape"] == [3, 2]
    assert result["missing"] == {"x": 1, "label": 0}
    assert result["duplicate_rows"] == 1
```

Create `tests/python/test_validation_utils.py`:

```python
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

def load_module(name: str, path: str):
    spec = spec_from_file_location(name, Path(path))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def test_time_split_is_chronological_and_disjoint():
    module = load_module("validation_utils", ".agents/skills/cumcm-modeling/scripts/validation_utils.py")
    train, validation, test = module.time_split(10, train_fraction=0.6, validation_fraction=0.2)
    assert train == list(range(6))
    assert validation == [6, 7]
    assert test == [8, 9]
    assert max(train) < min(validation) < min(test)

def test_metrics_constraints_and_perturbations_are_deterministic():
    module = load_module("validation_utils", ".agents/skills/cumcm-modeling/scripts/validation_utils.py")
    metrics = module.regression_metrics([1.0, 2.0], [1.0, 3.0])
    assert metrics["mae"] == 0.5
    assert metrics["rmse"] == 2 ** -0.5
    violations = module.constraint_violations([-1.0, 0.5, 3.0], lower=0.0, upper=2.0)
    assert violations == {"lower_count": 1, "upper_count": 1, "max_violation": 1.0}
    assert module.perturbation_grid(100.0, [-0.1, 0.0, 0.1]) == [90.0, 100.0, 110.0]
```

- [ ] **Step 2: Verify RED**

Run: `pytest -q tests/python/test_data_profile.py tests/python/test_validation_utils.py`

Expected: FAIL because helper modules do not exist.

- [ ] **Step 3: Implement minimal helpers and verify GREEN**

Implement `profile_frame(frame) -> dict[str, object]`, `time_split(n, train_fraction, validation_fraction) -> tuple[list[int], list[int], list[int]]`, `regression_metrics(y_true, y_pred) -> dict[str, float]`, `constraint_violations(values, lower, upper) -> dict[str, int | float]`, and `perturbation_grid(value, fractions) -> list[float]`. Use deterministic output, no file writes unless the CLI `--output` is supplied, and clear `ValueError` messages for invalid split ratios or shape mismatch.

Run: `pytest -q tests/python/test_data_profile.py tests/python/test_validation_utils.py`

- [ ] **Step 4: Author the Skill from observed modeling failures**

Initialize `cumcm-modeling`. Keep the entrypoint concise. Route detailed decisions to references. `model-selection.md` must choose by structure and prerequisites; `model-families.md` must use the unified model-card shape; `a-mechanism-modeling.md` must cover physical relations, units, boundaries, calibration, numerical convergence, and realistic simplifications.

- [ ] **Step 5: Pressure-test and refactor**

Run M1–M6 and C1 with a fresh agent explicitly loading the Skill. Require: linear baseline for M1, chronological/rolling evaluation for M2, no default entropy-TOPSIS for M3, deterministic/MILP check before heuristics for M4, repeated runs for M5, residual/leakage/holdout checks for M6, and ablation-based innovation judgment for C1. Save exact results in `tests/skill-results/modeling.md`.

- [ ] **Step 6: Validate and commit**

```bash
python /Users/eway/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/cumcm-modeling
pytest -q tests/python/test_data_profile.py tests/python/test_validation_utils.py
git add .agents/skills/cumcm-modeling tests/python/test_data_profile.py tests/python/test_validation_utils.py tests/skill-results/modeling.md
git commit -m "feat: add CUMCM modeling skill"
```

### Task 7: Implement and Verify `cumcm-visualization`

**Files:**
- Create: `.agents/skills/cumcm-visualization/SKILL.md`
- Create: `.agents/skills/cumcm-visualization/agents/openai.yaml`
- Create: `.agents/skills/cumcm-visualization/references/chart-selection.md`
- Create: `.agents/skills/cumcm-visualization/references/eda-and-diagnostics.md`
- Create: `.agents/skills/cumcm-visualization/references/scientific-style.md`
- Create: `.agents/skills/cumcm-visualization/references/result-plots.md`
- Create: `.agents/skills/cumcm-visualization/references/flowcharts-and-tables.md`
- Create: `.agents/skills/cumcm-visualization/references/common-errors.md`
- Create: `.agents/skills/cumcm-visualization/templates/figure-plan.md`
- Create: `.agents/skills/cumcm-visualization/scripts/plot_style.py`
- Create: `.agents/skills/cumcm-visualization/scripts/plot_helpers.py`
- Create: `tests/python/test_plot_helpers.py`
- Create: `tests/skill-results/visualization.md`

**Interfaces:**
- Consumes: `FIGURE REQUEST` plus verified data/results.
- Produces: figure plan, plotting code/artifact, and figure audit; never chooses the underlying model.

- [ ] **Step 1: Write failing plotting tests**

Create `tests/python/test_plot_helpers.py`:

```python
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import matplotlib
matplotlib.use("Agg")

def load_module(name: str, path: str):
    spec = spec_from_file_location(name, Path(path))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def test_style_save_and_axis_units(tmp_path):
    style = load_module("plot_style", ".agents/skills/cumcm-visualization/scripts/plot_style.py")
    helpers = load_module("plot_helpers", ".agents/skills/cumcm-visualization/scripts/plot_helpers.py")
    settings = style.paper_style()
    assert settings["figure.dpi"] == 150
    fig, ax = helpers.actual_vs_predicted([1, 2], [1.1, 1.9], variable="Thickness", unit="um")
    assert ax.get_xlabel() == "Actual Thickness (um)"
    assert ax.get_ylabel() == "Predicted Thickness (um)"
    outputs = helpers.save_figure(fig, tmp_path / "comparison", formats=("png", "pdf"))
    assert {path.suffix for path in outputs} == {".png", ".pdf"}
    assert all(path.exists() for path in outputs)
```

- [ ] **Step 2: Verify RED, implement minimal helpers, verify GREEN**

Run the test before and after implementation:

```bash
MPLBACKEND=Agg pytest -q tests/python/test_plot_helpers.py
```

- [ ] **Step 3: Author the Skill from observed visualization failures**

Require every figure request to state the question and main message. Reject purpose-free bulk plotting; select chart by analytical task; require units, accessible colors, grayscale distinction, non-obstructing legends, vector output where possible, and text/figure consistency.

- [ ] **Step 4: Pressure-test and refactor**

Run V1 with a fresh agent. Pass only if it narrows the request to questions/diagnostics rather than producing all fields or decorative charts. Save results in `tests/skill-results/visualization.md`.

- [ ] **Step 5: Validate and commit**

```bash
python /Users/eway/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/cumcm-visualization
MPLBACKEND=Agg pytest -q tests/python/test_plot_helpers.py
git add .agents/skills/cumcm-visualization tests/python/test_plot_helpers.py tests/skill-results/visualization.md
git commit -m "feat: add CUMCM visualization skill"
```

### Task 8: Implement and Verify `cumcm-thesis`

**Files:**
- Create: `.agents/skills/cumcm-thesis/SKILL.md`
- Create: `.agents/skills/cumcm-thesis/agents/openai.yaml`
- Create: `.agents/skills/cumcm-thesis/references/paper-structure.md`
- Create: `.agents/skills/cumcm-thesis/references/abstract-and-analysis.md`
- Create: `.agents/skills/cumcm-thesis/references/assumptions-notation-model.md`
- Create: `.agents/skills/cumcm-thesis/references/results-and-evaluation.md`
- Create: `.agents/skills/cumcm-thesis/references/latex-style.md`
- Create: `.agents/skills/cumcm-thesis/references/academic-style.md`
- Create: `.agents/skills/cumcm-thesis/references/common-errors.md`
- Create: `.agents/skills/cumcm-thesis/templates/paper-outline.md`
- Create: `.agents/skills/cumcm-thesis/templates/abstract-template.md`
- Create: `.agents/skills/cumcm-thesis/templates/section-template.md`
- Create: `.agents/skills/cumcm-thesis/templates/review-checklist.md`
- Create: `tests/skill-results/thesis.md`

**Interfaces:**
- Consumes: verified `MODEL SUMMARY`, result manifest, and figure manifest.
- Produces: paper sections with source/result traceability and a review ledger; never recomputes or invents results.

- [ ] **Step 1: Re-read thesis baseline failures and initialize**

Identify only observed failures for T1/T2. Initialize `cumcm-thesis` after baseline evidence exists.

- [ ] **Step 2: Author the Skill and focused references**

The entrypoint must require claim-evidence alignment and verified inputs. `abstract-and-analysis.md` must implement the reasoning chain “problem nature → evidence/research basis → candidate method → justified simplification → targeted improvement → verified result,” with natural prose variation. Templates must use explicit result placeholders such as `[由 results.json 写入的 RMSE]`, never invented numbers.

- [ ] **Step 3: Pressure-test and refactor**

Run T1 and T2 with a fresh agent. Pass T1 only if the blueprint avoids mechanical repetition and preserves numeric placeholders. Pass T2 only if strengths and limitations name the capacity constraint and deterministic-travel-time risk. Save results in `tests/skill-results/thesis.md`.

- [ ] **Step 4: Validate and commit**

```bash
python /Users/eway/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/cumcm-thesis
git add .agents/skills/cumcm-thesis tests/skill-results/thesis.md
git commit -m "feat: add CUMCM thesis skill"
```

### Task 9: Integration Validation, Skill Discovery, and 2025 A Hold-out

**Files:**
- Create: `.agents/skills/cumcm/scripts/validate_skills.py`
- Create: `tests/python/test_validate_skills.py`
- Create: `tests/holdout-2025a/independent-solution.md`
- Create: `tests/holdout-2025a/comparison.md`
- Create: `FINAL_REPORT.md`
- Modify: `docs/superpowers/specs/2026-09-07-cumcm-skill-suite-design.md`

**Interfaces:**
- Consumes: all four completed Skills, corpus, tests, and the 2025 A problem card without any solution-paper or expert-review evidence.
- Produces: automated suite validation, observable discovery evidence, a problem-only hold-out assessment, and final delivery report.

- [ ] **Step 1: Write a failing suite-validator test**

Create `tests/python/test_validate_skills.py`:

```python
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

def load_module(name: str, path: str):
    spec = spec_from_file_location(name, Path(path))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def test_suite_validator_reports_broken_contracts(tmp_path):
    module = load_module("validate_skills", ".agents/skills/cumcm/scripts/validate_skills.py")
    for name in ("cumcm", "cumcm-modeling", "cumcm-visualization", "cumcm-thesis"):
        folder = tmp_path / name
        folder.mkdir()
        folder.joinpath("SKILL.md").write_text(
            f"---\nname: {name}\ndescription: bad\n---\n# Placeholder\n"
            "See [missing](references/missing.md).\nDetailed XGBoost tutorial duplicated.\n",
            encoding="utf-8",
        )
    errors = module.validate_suite(tmp_path)
    joined = "\n".join(errors)
    assert "description" in joined
    assert "broken reference" in joined
    assert "scaffold marker" in joined
    assert "duplicated detailed knowledge" in joined
```

- [ ] **Step 2: Verify RED, implement, and verify GREEN**

Run:

```bash
pytest -q tests/python/test_validate_skills.py
```

Implement `validate_suite(root: Path) -> list[str]` and a CLI that validates the four expected Skill names, descriptions, links, scripts, templates, entrypoint word counts, and scaffold markers. Re-run until PASS.

- [ ] **Step 3: Run the independent 2025 A hold-out**

Give a fresh agent the 2025 A problem and attachments plus the four Skills, but no solution paper, expert review, or hidden corpus notes. Require the ten outputs listed in the design spec and save the complete response to `independent-solution.md`.

- [ ] **Step 4: Assess the hold-out without releasing the embargo**

Compare the independent output against the 2025 A problem statement and attachments only: mathematical structure, key constraints, variable definitions, feasibility, validation, sensitivity, figures, and paper plan. Save evidence-linked findings and limitations to `comparison.md`. Do not read or add 2025 A excellent-paper or expert-review evidence.

- [ ] **Step 5: Verify Skill discovery in the actual runtime**

Check that `.agents/skills/` is scanned by the current Codex runtime using a fresh task or documented discovery command. If project-local discovery is unavailable, retain `.agents/skills/` as repository source and request permission before installing copies outside the workspace. Record the observed result in `FINAL_REPORT.md`; do not claim discovery from file presence alone.

- [ ] **Step 6: Run the complete verification suite**

```bash
python .agents/skills/cumcm/scripts/validate_corpus.py corpus
python .agents/skills/cumcm/scripts/validate_skills.py .agents/skills
python /Users/eway/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/cumcm
python /Users/eway/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/cumcm-modeling
python /Users/eway/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/cumcm-visualization
python /Users/eway/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/cumcm-thesis
MPLBACKEND=Agg pytest -q tests/python
git diff --check
git status --short
```

Expected: all validators and tests pass; `git diff --check` is clean; status contains only the intentional final-report changes before commit.

- [ ] **Step 7: Write the final report and close the spec**

`FINAL_REPORT.md` must include Skill Tree, Corpus Summary, Extracted Patterns, Skill Responsibilities, Pressure Test Results, Hold-out Result, Skill Discovery Result, and Known Limitations. Change the design spec status from `已批准，待实现` to `已实现并验证` only after every applicable check passes.

- [ ] **Step 8: Commit final integration**

```bash
git add .agents/skills/cumcm/scripts/validate_skills.py tests/python/test_validate_skills.py tests/holdout-2025a corpus FINAL_REPORT.md docs/superpowers/specs/2026-09-07-cumcm-skill-suite-design.md
git commit -m "test: verify CUMCM skill suite"
git status --short --branch
```

Expected: clean working tree on a named branch, with hold-out evidence created after the independent solution timestamp.
