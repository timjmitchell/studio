# /// script
# requires-python = ">=3.10"
# dependencies = ["mido"]
# ///
"""Dump a Standard MIDI File as readable text.

Usage:
    uv run scripts/midi_dump.py <file.mid> [--out <file.txt>]

If no path is given, dumps every .mid in midi/ next to a .txt sibling.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from mido import MidiFile, tempo2bpm

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DIR = ROOT / "midi"


def dump(path: Path) -> str:
    mid = MidiFile(str(path))
    lines = [
        f"# {path.name}",
        f"# format: type={mid.type}  tracks={len(mid.tracks)}  ticks_per_beat={mid.ticks_per_beat}",
        f"# length: {mid.length:.2f}s",
        "",
    ]
    for i, track in enumerate(mid.tracks):
        lines.append(f"## Track {i}: {track.name!r}")
        abs_tick = 0
        for msg in track:
            abs_tick += msg.time
            extra = ""
            if msg.type == "set_tempo":
                extra = f"  # {tempo2bpm(msg.tempo):.2f} BPM"
            lines.append(f"  t={abs_tick:>8}  {msg}{extra}")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", help="Path to .mid file (default: all .mid in midi/)")
    ap.add_argument("--out", help="Write text to this file instead of stdout")
    args = ap.parse_args()

    if args.path:
        targets = [Path(args.path)]
    else:
        targets = sorted(DEFAULT_DIR.glob("*.mid"))
        if not targets:
            print(f"No .mid files in {DEFAULT_DIR}")
            return

    for mid_path in targets:
        text = dump(mid_path)
        if args.out and len(targets) == 1:
            Path(args.out).write_text(text)
            print(f"Wrote {args.out}")
        elif args.path:
            print(text)
        else:
            out = mid_path.with_suffix(".txt")
            out.write_text(text)
            print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
