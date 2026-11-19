"""Intent-to-concept lookup adapter; never defines normative guidance.

Purpose: map user phrasing to existing canonical IDs without duplicating specs.
Context: shared by CLI search and the static search-card enrichment.
Relevance: user goals should retrieve patterns before users know UI vocabulary.
"""
import json
import re
from pathlib import Path


def normalize(value):
    return " ".join(re.findall(r"[^\W_]+", value.casefold()))


def load_tasks(root):
    source = Path(root) / "tasks" / "index.json"
    tasks = json.loads(source.read_text(encoding="utf-8"))["tasks"]
    ids = [task["id"] for task in tasks]
    if len(set(ids)) != len(ids):
        raise ValueError("Duplicate task IDs")
    return tasks


def validate_tasks(tasks, entries):
    ids = {item["id"] for item in entries}
    seen = set()
    for task in tasks:
        if task["id"] in seen:
            raise ValueError("Duplicate task ID: " + task["id"])
        seen.add(task["id"])
        if not task.get("title") or not task.get("summary") or not task.get("intent_phrases"):
            raise ValueError("Incomplete user task: " + task["id"])
        refs = [task["primary_id"], *task.get("related_ids", [])]
        if len(set(refs)) != len(refs) or not all(value in ids for value in refs):
            raise ValueError("Invalid canonical task reference: " + task["id"])


def terms_by_concept(tasks):
    output = {}
    for task in tasks:
        terms = [task["title"], *task["intent_phrases"]]
        for concept_id in [task["primary_id"], *task.get("related_ids", [])]:
            output.setdefault(concept_id, []).extend(terms)
    return output


def task_relevance(concept_id, phrase, tasks):
    """Exact goal / synonym wins over fuzzy text, but not exact concept aliases."""
    query = normalize(phrase)
    if not query:
        return -1
    for task in tasks:
        if query in {normalize(v) for v in [task["title"], *task["intent_phrases"]]}:
            if concept_id == task["primary_id"]:
                return 85
            if concept_id in task.get("related_ids", []):
                return 35
    return -1
