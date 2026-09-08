# Corpus Source Policy

## Scope and purpose

This policy governs every problem card, paper card, evidence-ledger entry, synthesized rule, and hold-out artifact in the CUMCM Skill suite. It separates source discovery from evidence strong enough to support a retained claim.

## Source classes

| Class | Permitted use | Required treatment |
|---|---|---|
| Official problem statements and attachments | Establish problem text, variables, constraints, data, and competition context | Record the official URL or local file path, year, problem letter, and access date |
| Ten local 2024 paper PDFs | Support paper-card claims when the relevant text-layer page can be inspected directly | Record the stable local file path, document identity, and page or section locator; do not use OCR to fill unreadable content |
| Public case indexes and repository metadata | Discover candidate cases, structure labels, or coverage gaps | Treat as leads only; independently support retained claims from official/local evidence or label them `unverified` |
| General mathematical-modeling literature and established principles | Support transferable rules not tied to a specific competition paper | Identify the publication or explicitly label the synthesis as `expert-rule` |
| Inaccessible, broken, or OCR-unreliable material | Preserve provenance and known gaps | Do not infer substantive methods or results; label claims `unverified` |

The public `math-modeling-skill-pro` repository may be used only for architecture and retrieval-design comparison. Its case data are not corpus evidence; its cards, knowledge documents, scripts, templates, and proprietary wording must not be copied into this project.

## Evidence labels

Every substantive claim about a method, validation procedure, figure, result, or transferable rule must carry exactly one evidence label:

- `observed`: directly confirmed in an inspectable source.
- `inferred`: derived from visible formulas, figures, tables, or a documented method chain, with the inference stated rather than presented as quotation.
- `expert-rule`: a synthesis of multiple sources or an established modeling principle; it is not attributed to a single paper.
- `unverified`: the source is inaccessible, incomplete, or too unreliable to confirm the claim.

An `unverified` claim may document a gap or lead, but it must not become a mandatory Skill rule. Changing a label requires recording the stronger evidence that justifies the change.

## Text-layer and visual-verification limitations

All ten selected PDFs have a directly extractable text layer on every page. OCR output is outside the selected corpus workflow and must not support any retained claim. Use page-aware text extraction for analysis and inspect rendered pages for equations, subscripts, symbols, units, table cells, and figure labels. Content that cannot be confirmed reliably must be labeled `unverified`; do not reconstruct it from OCR caches. Text extraction or visual inspection alone never establishes that a paper's program or numerical result is reproducible.

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
- text-layer extraction and targeted visual-review status;
- retrieval failure, link failure, or access restriction when relevant.

URLs and file paths identify where evidence came from; they do not by themselves prove that the stated content was inspected. Mirrors should retain the canonical-source identity, and moved local files must be updated in the ledger rather than silently losing provenance.

## 2025 A hold-out release protocol

Before the independent artifact was completed, the 2025 A problem statement and its official attachments were the only permitted 2025 A sources. No solution paper, excellent-paper exhibit, expert review, commentary, hidden corpus note, or source revealing solution methods was read or encoded during solution generation.

The independent artifact was completed in a fresh context and frozen as `tests/holdout-2025a/independent-solution.md` before solution evidence was released. On 2026-09-08 the user explicitly supplied and authorized a 2025 A paper for post-release validation and Skill improvement. That paper may be used only in clearly labeled post-release comparison artifacts; it must not be added to `corpus/paper-cards`, indexed by `search_cases.py`, or retroactively presented as input to the independent solution.

The 2025 A evidence ledger remains problem-only so `validate_corpus.py` can enforce the reusable corpus boundary. Post-release validation records must state the paper hash, inspected page range, extraction limitations, and which Skill changes were made. Pre-release problem-only scoring and post-release paper comparison are separate results.
