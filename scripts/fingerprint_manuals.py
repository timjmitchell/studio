# /// script
# requires-python = ">=3.11"
# dependencies = ["pypdf"]
# ///
"""Fingerprint PDFs under one or more roots and emit JSON on stdout.

Per file: path, name, size, md5, and for PDFs title, author, producer,
creation_date, page_count. Page count plus embedded title survive renaming,
which md5 misses and filenames lie about.

Usage:
    uv run scripts/fingerprint_manuals.py docs/manuals ~/Desktop > out.json
    uv run scripts/fingerprint_manuals.py --no-pdf-meta <root>   # md5 only

Skips Google Drive stream-only placeholders (apparent size > 0, zero blocks
on disk) rather than forcing them to download; they are reported under
"skipped_placeholders" with their Drive item id where available.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

DRIVE_ID_XATTR = "com.google.drivefs.item-id#S"


def md5(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def drive_item_id(path: Path) -> str | None:
    """Drive for Desktop stamps the file id as an xattr. macOS has no
    os.getxattr, so shell out to /usr/bin/xattr."""
    proc = subprocess.run(
        ["xattr", "-p", DRIVE_ID_XATTR, str(path)],
        capture_output=True, text=True,
    )
    return proc.stdout.strip() or None if proc.returncode == 0 else None


def is_placeholder(st: os.stat_result) -> bool:
    """Dataless file: claims bytes but occupies no blocks."""
    return st.st_size > 0 and st.st_blocks == 0


def pdf_meta(path: Path) -> dict:
    try:
        from pypdf import PdfReader

        reader = PdfReader(path)
        info = reader.metadata or {}

        def field(key: str) -> str | None:
            # pypdf hands back IndirectObject / ByteStringObject for some
            # producers; resolve and stringify so the record stays JSON-safe.
            val = info.get(key)
            if val is None:
                return None
            resolve = getattr(val, "get_object", None)
            if resolve is not None:
                val = resolve()
            if isinstance(val, bytes):
                return val.decode("utf-8", "replace")
            return str(val)

        return {
            "title": field("/Title"),
            "author": field("/Author"),
            "producer": field("/Producer"),
            "creation_date": field("/CreationDate"),
            "page_count": len(reader.pages),
        }
    except Exception as exc:  # corrupt, encrypted, truncated
        return {"pdf_error": f"{type(exc).__name__}: {exc}"}


def walk(root: Path, *, want_meta: bool, exts: set[str] | None) -> tuple[list[dict], list[dict]]:
    files: list[dict] = []
    skipped: list[dict] = []
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        if path.name.startswith("."):
            continue
        if exts and path.suffix.lower().lstrip(".") not in exts:
            continue
        st = path.stat()
        if is_placeholder(st):
            skipped.append(
                {
                    "path": str(path),
                    "name": path.name,
                    "size": st.st_size,
                    "drive_item_id": drive_item_id(path),
                }
            )
            continue
        rec = {
            "root": str(root),
            "path": str(path),
            "name": path.name,
            "size": st.st_size,
            "md5": md5(path),
            # Present on every file under a Drive mount, materialized or not —
            # so a file uploaded from here still reads as living on Drive.
            "drive_item_id": drive_item_id(path),
        }
        if want_meta and path.suffix.lower() == ".pdf":
            rec.update(pdf_meta(path))
        files.append(rec)
    return files, skipped


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("roots", nargs="+", type=Path)
    ap.add_argument("--no-pdf-meta", action="store_true", help="md5 and size only")
    ap.add_argument("--ext", help="comma-separated extensions to include, e.g. pdf,zip")
    args = ap.parse_args()

    exts = {e.strip().lower().lstrip(".") for e in args.ext.split(",")} if args.ext else None
    files: list[dict] = []
    skipped: list[dict] = []
    for raw in args.roots:
        root = raw.expanduser().resolve()
        if not root.is_dir():
            print(f"skipping {root}: not a directory", file=sys.stderr)
            continue
        f, s = walk(root, want_meta=not args.no_pdf_meta, exts=exts)
        print(f"{root}: {len(f)} hashed, {len(s)} placeholders", file=sys.stderr)
        files.extend(f)
        skipped.extend(s)

    json.dump({"files": files, "skipped_placeholders": skipped}, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
