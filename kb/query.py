# /// script
# requires-python = ">=3.10"
# ///
"""Query the local document indexes built by kb/index.py.

Reads kb/indexes/*.json (no source files, no DB) and returns ranked matches by
keyword overlap against title / tags / path / snippet. The logichelp and kb
skills call this to route, then open only the top documents.

Usage:
    uv run kb/query.py "sidechain compressor"              # search all stores
    uv run kb/query.py "space designer" --store manuals    # one store
    uv run kb/query.py "delay time" --limit 5 --json       # machine-readable

Ported from backoffice-pr/kb/query.py so studio shares the same retrieval engine.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX_DIR = REPO_ROOT / "kb" / "indexes"

# field -> weight
WEIGHTS = {"title": 3.0, "tags": 2.0, "rel_path": 1.0, "snippet": 1.0}
TOKEN_RE = re.compile(r"[a-z0-9]+")


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())


def load_indexes(store: str | None) -> list[dict]:
    if not INDEX_DIR.is_dir():
        return []
    indexes = []
    for path in sorted(INDEX_DIR.glob("*.json")):
        idx = json.loads(path.read_text(encoding="utf-8"))
        if store and idx.get("store") != store:
            continue
        indexes.append(idx)
    return indexes


def score_doc(doc: dict, terms: list[str]) -> float:
    fields = {
        "title": doc.get("title", ""),
        "tags": " ".join(str(t) for t in doc.get("tags", [])),
        "rel_path": doc.get("rel_path", ""),
        "snippet": doc.get("snippet", ""),
    }
    field_tokens = {f: set(tokenize(v)) for f, v in fields.items()}
    score = 0.0
    for term in terms:
        for field, weight in WEIGHTS.items():
            if term in field_tokens[field]:
                score += weight
    return score


def search(indexes: list[dict], query: str, limit: int) -> list[dict]:
    terms = tokenize(query)
    results = []
    for idx in indexes:
        for doc in idx.get("docs", []):
            s = score_doc(doc, terms)
            if s > 0:
                results.append({"score": s, "store": idx["store"], **doc})
    results.sort(key=lambda r: (-r["score"], r["store"], r["rel_path"]))
    return results[:limit]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="+", help="Search terms")
    ap.add_argument("--store", help="Restrict to one store")
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--json", action="store_true", help="Emit JSON")
    args = ap.parse_args()

    indexes = load_indexes(args.store)
    if not indexes:
        raise SystemExit(
            "No indexes found in kb/indexes/. Build them first:\n"
            "    uv run kb/index.py"
        )

    query = " ".join(args.query)
    results = search(indexes, query, args.limit)

    if args.json:
        slim = [
            {k: r[k] for k in ("score", "store", "title", "rel_path", "abs_path", "tags", "snippet")}
            for r in results
        ]
        print(json.dumps(slim, indent=2, ensure_ascii=False))
        return

    if not results:
        print(f"No matches for {query!r}. Try fewer/different terms or rebuild the index.")
        return

    print(f"{len(results)} match(es) for {query!r}:\n")
    for r in results:
        tags = f"  [{', '.join(str(t) for t in r['tags'])}]" if r.get("tags") else ""
        print(f"[{r['score']:.0f}] ({r['store']}) {r['title']}{tags}")
        print(f"      {r['abs_path']}")
        if r.get("snippet"):
            print(f"      {r['snippet'][:160]}")
        print()


if __name__ == "__main__":
    main()
