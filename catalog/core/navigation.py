"""Stable public routing for canonical concepts.

Purpose: decouple published URLs from source Markdown folder placement.
Context: consumed by the static site and tests; not a package routing API.
Relevance: a knowledge-base reorganization must not break concept bookmarks.
"""
import re
from pathlib import PurePosixPath

CATEGORIES = ("components", "patterns", "features", "foundations", "architecture",
              "guidance", "governance", "other")
ID_CATEGORIES = {"component": "components", "pattern": "patterns", "feature": "features",
                 "foundation": "foundations", "principle": "foundations",
                 "architecture": "architecture", "guidance": "guidance",
                 "governance": "governance"}
PATH_CATEGORIES = {
    "specifications": {"components": "components", "patterns": "patterns", "experiences": "features"},
    "knowledge": {"foundations": "foundations", "architecture": "architecture", "guidance": "guidance"},
}


def category(entry):
    prefix = entry["id"].split(".", 1)[0]
    if prefix in ID_CATEGORIES:
        return ID_CATEGORIES[prefix]
    parts = PurePosixPath(entry["path"]).parts
    if len(parts) > 1 and parts[0] in PATH_CATEGORIES:
        return PATH_CATEGORIES[parts[0]].get(parts[1], "other")
    return parts[0] if parts and parts[0] in CATEGORIES else "other"


def route(entry):
    segment = entry["id"].split(".", 1)[-1].lower()
    slug = re.sub(r"[^a-z0-9-]+", "-", segment).strip("-")
    if not slug:
        raise ValueError("Invalid canonical ID: " + entry["id"])
    return "/catalog/" + category(entry) + "/" + slug + "/"
