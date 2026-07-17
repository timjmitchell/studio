# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6.0"]
# ///
"""Build thin, file-based indexes over studio's local document stores.

Reads kb/stores.yaml, walks each store, and writes one small JSON index per
store to kb/indexes/<name>.json. Skills (logichelp, kb) read the index first and
open individual documents only when they need detail — no database, no
embeddings, no MCP.

Usage:
    uv run kb/index.py                    # build all stores
    uv run kb/index.py --store manuals    # build one store
    uv run kb/index.py --list             # list configured stores
    uv run kb/index.py --status           # show index coverage / freshness

Ported from backoffice-pr/kb/index.py so studio shares the same retrieval engine.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from fnmatch import fnmatch
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
STORES_FILE = REPO_ROOT / "kb" / "stores.yaml"
INDEX_DIR = REPO_ROOT / "kb" / "indexes"

# frontmatter.py sits beside this script; make it importable when run via `uv run`.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from frontmatter import parse_frontmatter  # noqa: E402

HEADING_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
SNIPPET_LEN = 280


def derive_title(fm: dict, body: str, path: Path) -> str:
    title = fm.get("title")
    if isinstance(title, str) and title.strip():
        return title.strip()
    m = HEADING_RE.search(body)
    if m:
        return m.group(1).strip()
    return path.stem


def make_snippet(body: str) -> str:
    """First meaningful prose, stripped of heading marks and blank lines."""
    lines = []
    for line in body.splitlines():
        s = line.strip().lstrip("#").strip()
        if s and not s.startswith(("---", "|", "```")):
            lines.append(s)
        if sum(len(x) for x in lines) >= SNIPPET_LEN:
            break
    return " ".join(lines)[:SNIPPET_LEN]


def scalar_frontmatter(fm: dict) -> dict:
    """Keep only JSON-friendly scalar/list fields for the index."""
    out = {}
    for k, v in fm.items():
        if isinstance(v, (str, int, float, bool)):
            out[k] = v
        elif isinstance(v, list) and all(isinstance(i, (str, int, float)) for i in v):
            out[k] = v
    return out


def iter_files(root: Path, globs: list[str], exclude: list[str]):
    seen: set[Path] = set()
    for pattern in globs:
        for p in sorted(root.glob(pattern)):
            if not p.is_file() or p in seen:
                continue
            rel = p.relative_to(root).as_posix()
            if any(fnmatch(rel, ex) for ex in exclude):
                continue
            seen.add(p)
            yield p, rel


def build_store(store: dict) -> dict:
    name = store["name"]
    root = Path(store["root"]).expanduser()
    if not root.is_absolute():
        root = REPO_ROOT / root
    globs = store.get("globs", ["**/*.md"])
    exclude = store.get("exclude", []) or []

    docs = []
    if root.is_dir():
        for path, rel in iter_files(root, globs, exclude):
            try:
                content = path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            fm, body = parse_frontmatter(content)
            st = path.stat()
            docs.append({
                "rel_path": rel,
                "abs_path": str(path),
                "title": derive_title(fm, body, path),
                "type": fm.get("type"),
                "tags": fm.get("tags") if isinstance(fm.get("tags"), list) else [],
                "frontmatter": scalar_frontmatter(fm),
                "snippet": make_snippet(body),
                "size": st.st_size,
                "mtime": datetime.fromtimestamp(st.st_mtime).isoformat(timespec="seconds"),
            })

    return {
        "store": name,
        "kind": store.get("kind", "markdown"),
        "root": str(root),
        "exists": root.is_dir(),
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "count": len(docs),
        "docs": docs,
    }


def load_stores() -> list[dict]:
    data = yaml.safe_load(STORES_FILE.read_text(encoding="utf-8"))
    return data.get("stores", [])


def write_index(index: dict) -> Path:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    out = INDEX_DIR / f"{index['store']}.json"
    out.write_text(json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")
    return out


def cmd_status(stores: list[dict]) -> None:
    print(f"{'store':<12} {'docs':>6}  {'built':<20} root")
    print("-" * 72)
    for store in stores:
        name = store["name"]
        idx_path = INDEX_DIR / f"{name}.json"
        if idx_path.exists():
            idx = json.loads(idx_path.read_text(encoding="utf-8"))
            built = idx.get("generated_at", "?")
            count = idx.get("count", "?")
            root = idx.get("root", store.get("root"))
        else:
            built, count, root = "(not built)", "-", store.get("root")
        print(f"{name:<12} {str(count):>6}  {built:<20} {root}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--store", help="Build only this store")
    ap.add_argument("--list", action="store_true", help="List configured stores and exit")
    ap.add_argument("--status", action="store_true", help="Show index coverage / freshness and exit")
    args = ap.parse_args()

    stores = load_stores()

    if args.list:
        for s in stores:
            print(f"{s['name']:<12} {s.get('kind',''):<10} {s.get('root')}")
        return
    if args.status:
        cmd_status(stores)
        return

    if args.store:
        stores = [s for s in stores if s["name"] == args.store]
        if not stores:
            raise SystemExit(f"No store named {args.store!r} in {STORES_FILE}")

    for store in stores:
        index = build_store(store)
        out = write_index(index)
        flag = "" if index["exists"] else "  [WARNING: root missing]"
        print(f"indexed {index['count']:>5} docs → {out.relative_to(REPO_ROOT)}{flag}")


if __name__ == "__main__":
    main()
