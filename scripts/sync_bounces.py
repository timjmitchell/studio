# /// script
# requires-python = ">=3.10"
# ///
"""Add new listening bounces to each song doc's Recordings table.

Bounces live in one Google Drive folder, synced locally by Drive for Desktop:
    My Drive/Hot Fog/New- 3rd Album/Bounces/

Name each bounce  <song-slug>_<YYYY-MM-DD>_<tag>.mp3, e.g.
    arbitrary-overlord_2026-10-10_timmix.mp3
<song-slug> is the song doc's filename (docs/hot-fog/**/<song-slug>.md). The date
and tag are optional; a missing date falls back to the file's modified date.

For each bounce not yet mentioned in its song doc, this appends a row to the
doc's **Recordings** table with a Drive link. The Drive file ID comes from the
`com.google.drivefs.item-id#S` xattr; a file that hasn't finished uploading has
no real ID yet and is skipped until the next run.

Usage:
    uv run scripts/sync_bounces.py [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import subprocess
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SONGS = ROOT / "docs" / "hot-fog"
BOUNCES = (
    Path.home()
    / "Library/CloudStorage/GoogleDrive-sasakimitchell@gmail.com/My Drive"
    / "Hot Fog/New- 3rd Album/Bounces"
)
AUDIO = {".mp3", ".m4a", ".wav", ".aif", ".aiff"}
NAME = re.compile(r"^(?P<slug>[a-z0-9-]+)(?:_(?P<date>\d{4}-\d{2}-\d{2}))?(?:_(?P<tag>.+))?$")


def drive_id(path: Path) -> str | None:
    out = subprocess.run(
        ["xattr", "-p", "com.google.drivefs.item-id#S", str(path)],
        capture_output=True, text=True,
    )
    file_id = out.stdout.strip()
    return file_id if out.returncode == 0 and file_id and not file_id.startswith("local") else None


def song_docs() -> dict[str, Path]:
    docs = {}
    for md in SONGS.rglob("*.md"):
        if re.search(r"^type:\s*song\s*$", md.read_text(), re.M):
            docs[md.stem] = md
    return docs


def add_row(doc: Path, row: str) -> str:
    """Insert row at the end of the table that follows the **Recordings** heading."""
    lines = doc.read_text().split("\n")
    start = next(i for i, l in enumerate(lines) if l.startswith("**Recordings**"))
    i = start + 1
    while i < len(lines) and not lines[i].startswith("|"):
        i += 1
    while i < len(lines) and lines[i].startswith("|"):
        i += 1
    lines.insert(i, row)
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="show rows without writing")
    args = ap.parse_args()

    docs = song_docs()
    for f in sorted(p for p in BOUNCES.iterdir() if p.suffix.lower() in AUDIO):
        m = NAME.match(f.stem)
        doc = docs.get(m["slug"]) if m else None
        if doc is None:
            print(f"? {f.name}: no song doc matches; expected <song-slug>_<YYYY-MM-DD>_<tag>")
            continue
        if f.name in doc.read_text():
            continue
        file_id = drive_id(f)
        if file_id is None:
            print(f"… {f.name}: not uploaded yet, skipping")
            continue
        day = m["date"] or date.fromtimestamp(f.stat().st_mtime).isoformat()
        tag = (m["tag"] or "bounce").replace("-", " ")
        row = f"| {day} | {tag} | [Drive](https://drive.google.com/file/d/{file_id}/view) · `{f.name}` |"
        print(f"+ {doc.relative_to(ROOT)}: {row}")
        if not args.dry_run:
            doc.write_text(add_row(doc, row))


if __name__ == "__main__":
    main()
