"""Concept-only editorial policy and diagnostics.

Purpose: ensure canonical knowledge describes the concept rather than the
sequence of PRs, batches, or knowledge-gap tickets that created its prose.
Context: source Markdown and CI, not a visual-site-only presentation filter.
Relevance: the same clean source is consumed by humans, agents and exports.
"""
import re

HISTORY = re.compile(r"(?i)\b(?:batch\s*\d+|phase\s*\d+|PR\s*#\d+|(?:CKG|KG)-\d+|B0[1-9]\b)")
PROCESS = re.compile(r"(?i)^#{1,6}\s+(?:context (?:collected|and coverage) at batch start|shared batch-PR protocol)")


def findings(source):
    """Return (line, excerpt) diagnostics; status/provenance dates are allowed."""
    problems = []
    for number, line in enumerate(source.splitlines(), 1):
        if HISTORY.search(line) or PROCESS.search(line):
            problems.append((number, line.strip()[:140]))
    return problems
