"""Deterministic, read-only inventory of source files in a CUMCM workspace.

Generated corpus/docs/tests and hidden tooling trees are excluded so rerunning
the scanner does not index its own output. Symlinks are not followed.
"""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re


KIND_ORDER = {"problem": 0, "attachment": 1, "paper": 2, "other": 3}
GENERATED_DIRS = {"corpus", "docs", "tests", "tmp", "output", "outputs", "node_modules", "__pycache__"}
ATTACHMENT_EXTENSIONS = {".xlsx", ".xls", ".csv", ".tsv", ".gif", ".png", ".jpg", ".jpeg", ".bmp", ".zip", ".rar", ".mat"}


def identify(path: Path):
    year_match = re.search(r"(?<!\d)(20\d{2})(?!\d)", path.as_posix())
    year = int(year_match[1]) if year_match else None
    problem = None
    for part in reversed(path.parts):
        match = re.search(r"([A-E])(?:题|\d{3})", part, re.IGNORECASE)
        if not match:
            match = re.fullmatch(r"(?:cumcm)?20\d{2}([a-e])(?:\.[^.]+)?", part, re.IGNORECASE)
        if match:
            problem = match[1].upper()
            break
    is_paper = any("论文" in part or "点评" in part for part in path.parts)
    if is_paper and path.suffix.lower() == ".pdf":
        kind = "paper"
    elif path.suffix.lower() in {".pdf", ".doc", ".docx"} and (
        re.fullmatch(r"[A-E]题", path.stem, re.IGNORECASE)
        or re.fullmatch(r"cumcm20\d{2}[a-e]", path.stem, re.IGNORECASE)
    ):
        kind = "problem"
    elif path.suffix.lower() in ATTACHMENT_EXTENSIONS:
        kind = "attachment"
    else:
        kind = "other"
    return year, problem, kind


def build_inventory(root: Path) -> list[dict[str, object]]:
    root = Path(root).resolve()
    if not root.is_dir():
        raise ValueError(f"Inventory root is not a directory: {root}")
    rows = []
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if any(part.startswith(".") or part in GENERATED_DIRS for part in relative.parts):
            continue
        if path.is_symlink() or not path.is_file():
            continue
        year, problem, kind = identify(relative)
        # Pre-hold-out: do not open or hash a 2025 A paper/review.
        if year == 2025 and problem == "A" and kind == "paper":
            continue
        digest = hashlib.sha256()
        with path.open("rb") as source:
            for chunk in iter(lambda: source.read(1024 * 1024), b""):
                digest.update(chunk)
        rows.append({
            "path": relative.as_posix(), "kind": kind, "year": year,
            "problem": problem, "extension": path.suffix.lower(),
            "size_bytes": path.stat().st_size, "sha256": digest.hexdigest(),
        })
    return sorted(rows, key=lambda row: (
        KIND_ORDER[row["kind"]], row["year"] or 0, row["problem"] or "", row["path"]
    ))


def coverage_markdown(rows):
    counts = Counter(row["kind"] for row in rows)
    extensions = Counter(row["extension"] for row in rows)
    lines = ["# Local source coverage", "", "Deterministic source-only inventory; no source file is modified.", "",
             "| Year | Problem statements | Papers | Attachments | Other |", "|---|---|---:|---:|---:|"]
    years = sorted({row["year"] for row in rows if row["year"] is not None} | set(range(2020, 2026)))
    for year in years:
        subset = [row for row in rows if row["year"] == year]
        local = sorted({row["problem"] for row in subset if row["kind"] == "problem" and row["problem"]})
        grouped = Counter(row["kind"] for row in subset)
        lines.append(f"| {year} | {', '.join(local) or 'none locally'} | {grouped['paper']} | {grouped['attachment']} | {grouped['other']} |")
    lines += ["", "## Totals", ""]
    lines += [f"- {kind}: {counts[kind]}" for kind in KIND_ORDER]
    lines += ["", "## File formats", ""]
    lines += [f"- `{extension or '(no extension)'}`: {count}" for extension, count in sorted(extensions.items())]
    lines += ["", "## Scope and gaps", "",
              "2020–2021 statements acquired temporarily are documented in the evidence ledger, not copied into the local source inventory.",
              "The inventory records bytes and provenance identity, not extraction completeness or scientific validity.",
              "Hidden files/directories, generated corpus/docs/tests/output trees, dependency caches and symlinks are excluded.",
              "2025 A paper/review PDFs recognized by path are excluded before content access under the hold-out embargo.", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--coverage", type=Path, required=True)
    args = parser.parse_args()
    rows = build_inventory(args.root)
    for target in (args.output, args.coverage):
        target.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.coverage.write_text(coverage_markdown(rows), encoding="utf-8")
    print(f"Indexed {len(rows)} source files")


if __name__ == "__main__":
    main()
