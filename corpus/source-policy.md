# Corpus Source Policy

## Scope and purpose

This policy governs every problem card, paper card, evidence-ledger entry, synthesized rule, and hold-out artifact in the CUMCM Skill suite. It separates source discovery from evidence strong enough to support a retained claim.

## Source classes

| Class | Permitted use | Required treatment |
|---|---|---|
| Official problem statements and attachments | Establish problem text, variables, constraints, data, and competition context | Record the official URL or local file path, year, problem letter, and access date |
| Official excellent-paper exhibits and official or expert reviews | Support claims about reported methods, validation, figures, and results | Cite the exact exhibit or review and a page, section, figure, or other locator |
| Local paper PDFs | Support paper-card claims when the relevant content can be inspected | Record the stable local file path, document identity, and page or section locator |
| Public case indexes and repository metadata | Discover candidate cases, structure labels, or coverage gaps | Treat as leads only; independently support retained claims from official/local evidence or label them `unverified` |
| General mathematical-modeling literature and established principles | Support transferable rules not tied to a specific competition paper | Identify the publication or explicitly label the synthesis as `expert-rule` |
| Inaccessible, broken, or OCR-unreliable material | Preserve provenance and known gaps | Do not infer substantive methods or results; label claims `unverified` |

The public `math-modeling-skill-pro` repository may be used only for gap discovery and retrieval-design comparison. Its cards, knowledge documents, scripts, templates, and proprietary wording must not be copied into this project.

## Evidence labels

Every substantive claim about a method, validation procedure, figure, result, or transferable rule must carry exactly one evidence label:

- `observed`: directly confirmed in an inspectable source.
- `inferred`: derived from visible formulas, figures, tables, or a documented method chain, with the inference stated rather than presented as quotation.
- `expert-rule`: a synthesis of multiple sources or an established modeling principle; it is not attributed to a single paper.
- `unverified`: the source is inaccessible, incomplete, or too unreliable to confirm the claim.

An `unverified` claim may document a gap or lead, but it must not become a mandatory Skill rule. Changing a label requires recording the stronger evidence that justifies the change.

## OCR limitations and review

OCR output is an aid, not authoritative evidence. For OCR-derived material, record the source file or URL, page range, OCR tool and version when known, recognition date, and confidence or review status. Equations, subscripts, symbols, units, table cells, figure labels, and Chinese characters that affect meaning require comparison with the rendered page. If the rendered source cannot resolve an ambiguity, quote no uncertain text, make no method/result claim from it, and use `unverified`. OCR completion alone never establishes that a paper, program, or numerical result is reproducible.

## Copyright boundaries

Store bibliographic metadata, compact factual notes, evidence locators, and original summaries. Use only short excerpts when necessary for verification and attribute them precisely. Do not reproduce full papers, substantial passages, complete tables, figure collections, source code, templates, or distinctive proprietary wording. Formulas, tables, and figures may be described analytically; copying them requires a clear permission or license basis. Corpus cards must express transferable structure in original language rather than reconstructing the source.

## URL and file-path provenance

Each evidence record must include, as applicable:

- a stable evidence ID;
- source class, title, author or issuing body, year, and problem letter;
- canonical URL plus access date for remote material;
- repository-relative or stable local file path for local material;
- page, section, table, figure, sheet, or row locator;
- evidence label and a concise statement of what the source supports;
- OCR and manual-review status;
- retrieval failure, link failure, or access restriction when relevant.

URLs and file paths identify where evidence came from; they do not by themselves prove that the stated content was inspected. Mirrors should retain the canonical-source identity, and moved local files must be updated in the ledger rather than silently losing provenance.

## 2025 A hold-out embargo

The 2025 A problem statement and its official attachments may be indexed and used to prepare the independent hold-out input. Until the Task 9 independent solution has been completed, saved under `tests/holdout-2025a/`, and timestamped, no agent, Skill author, corpus process, or test may read or encode any 2025 A solution paper, excellent-paper exhibit, expert review, solution commentary, or source that reveals solution methods.

Before release, the 2025 A evidence ledger may contain problem sources only. The embargo does not apply to 2025 B/C evidence. After the independent solution is immutably saved, Task 9 may release the embargo, inspect at least one official excellent paper and an official or expert review, and record all newly added evidence as post-hold-out. The comparison must judge mathematical structure, constraints, validation, sensitivity, figures, and justification; use of a different model is not a failure by itself.


