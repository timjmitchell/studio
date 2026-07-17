"""YAML-frontmatter reader for markdown files.

The kb index uses this to pull `title` / `tags` / `type` and any scalar
frontmatter off a doc before indexing its body. Kept deliberately small — real
YAML (not a flat line-splitter) so nested mappings and list fields parse
correctly.

Ported from backoffice-pr's src/frontmatter.py so studio's kb/ engine matches
the one the /kb command uses over there. See ../README (kb section) and
../../backoffice-pr for the shared pattern.
"""

from __future__ import annotations

import re

import yaml

# Leading, optional YAML block delimited by --- lines. Captures the YAML content.
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n?---\r?\n?", re.DOTALL)


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body). Empty dict if no/empty/invalid block."""
    m = FRONTMATTER_RE.match(content)
    if not m:
        return {}, content
    raw = m.group(1).strip()
    body = content[m.end():]
    if not raw:
        return {}, body
    try:
        parsed = yaml.safe_load(raw)
    except yaml.YAMLError:
        return {}, body
    return (parsed if isinstance(parsed, dict) else {}), body
