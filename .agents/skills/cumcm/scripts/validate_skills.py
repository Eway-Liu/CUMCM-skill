#!/usr/bin/env python3
"""Validate the four discoverable CUMCM Skill entrypoints as one suite."""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path


EXPECTED_SKILLS = (
    "cumcm-global",
    "cumcm-modeling",
    "cumcm-visualization",
    "cumcm-thesis",
)
MAX_ENTRY_WORDS = 650
LINK_RE = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
CODE_PATH_RE = re.compile(
    r"`((?:\.\./|scripts/|references/|templates/)[^`\s]+\.(?:py|md|json|ya?ml))`"
)
SCAFFOLD_RE = re.compile(
    r"(?im)^\s*(?:#{1,6}\s*)?(?:todo|tbd|placeholder)(?:\s|:|$)"
)


def _frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    metadata: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip("'\"")
    return metadata, text[end + 5 :]


def _local_link_target(skill_file: Path, target: str) -> Path | None:
    target = target.strip().split("#", 1)[0]
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    return skill_file.parent / target


def _knowledge_lines(body: str) -> set[str]:
    result: set[str] = set()
    for raw in body.splitlines():
        line = re.sub(r"\s+", " ", raw.strip())
        if not line or line.startswith(("#", "```")):
            continue
        line = LINK_RE.sub("", line).strip(" -*`")
        if len(re.findall(r"[A-Za-z0-9_]+|[\u4e00-\u9fff]", line)) >= 12:
            result.add(line.casefold())
    return result


def validate_suite(root: Path) -> list[str]:
    """Return contract violations for the expected project-local Skill suite."""
    root = Path(root)
    errors: list[str] = []
    discovered = {path.parent.name: path for path in root.glob("*/SKILL.md")}

    for name in EXPECTED_SKILLS:
        if name not in discovered:
            errors.append(f"{root}: missing Skill entrypoint {name}/SKILL.md")
    for name in sorted(set(discovered) - set(EXPECTED_SKILLS)):
        errors.append(f"{discovered[name]}: unexpected discoverable Skill {name}")

    line_owners: defaultdict[str, list[str]] = defaultdict(list)
    for name in EXPECTED_SKILLS:
        skill_file = discovered.get(name)
        if skill_file is None:
            continue
        text = skill_file.read_text(encoding="utf-8")
        metadata, body = _frontmatter(text)
        if metadata.get("name") != name:
            errors.append(f"{skill_file}: frontmatter name must be {name}")
        description = metadata.get("description", "")
        if not description.startswith("Use when "):
            errors.append(
                f"{skill_file}: description must be a trigger condition starting with 'Use when '"
            )
        if "\n" in description or len(description.split()) > 45:
            errors.append(f"{skill_file}: description must be concise and single-line")
        word_count = len(re.findall(r"\b[\w'-]+\b", body, flags=re.UNICODE))
        if word_count > MAX_ENTRY_WORDS:
            errors.append(
                f"{skill_file}: entrypoint has {word_count} words; maximum is {MAX_ENTRY_WORDS}"
            )
        if SCAFFOLD_RE.search(body):
            errors.append(f"{skill_file}: scaffold marker remains")
        for target in LINK_RE.findall(body):
            resolved = _local_link_target(skill_file, target)
            if resolved is not None and not resolved.exists():
                errors.append(f"{skill_file}: broken reference {target}")
        for target in CODE_PATH_RE.findall(body):
            if not (skill_file.parent / target).exists():
                errors.append(f"{skill_file}: broken artifact {target}")
        for line in _knowledge_lines(body):
            line_owners[line].append(name)

    for line, owners in sorted(line_owners.items()):
        if len(owners) > 1:
            excerpt = line[:90] + ("..." if len(line) > 90 else "")
            errors.append(
                "duplicated detailed knowledge across "
                f"{', '.join(owners)}: {excerpt}"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skills_root", type=Path)
    args = parser.parse_args()
    errors = validate_suite(args.skills_root)
    if errors:
        for error in errors:
            print(error)
        return 1
    print("skill suite validation: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
