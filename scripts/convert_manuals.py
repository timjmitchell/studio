# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pymupdf4llm",
#     "pymupdf",
# ]
# ///
"""Convert PDFs in docs/manuals/ to markdown and generate INDEX.md."""
from __future__ import annotations

from pathlib import Path

import pymupdf
import pymupdf4llm

MANUALS = Path(__file__).resolve().parent.parent / "docs" / "manuals"


def toc_to_markdown(toc: list[list], max_depth: int = 3) -> str:
    lines = []
    for level, title, page in toc:
        if level > max_depth:
            continue
        indent = "  " * (level - 1)
        lines.append(f"{indent}- {title.strip()} (p. {page})")
    return "\n".join(lines)


def main() -> None:
    pdfs = sorted(MANUALS.glob("*.pdf"))
    if not pdfs:
        print(f"No PDFs in {MANUALS}")
        return

    sections: list[str] = []
    for pdf in pdfs:
        md_path = pdf.with_suffix(".md")
        print(f"Converting {pdf.name} ({pdf.stat().st_size // (1024 * 1024)} MB)...")
        md = pymupdf4llm.to_markdown(str(pdf), show_progress=True)
        md_path.write_text(md)

        with pymupdf.open(str(pdf)) as doc:
            toc = doc.get_toc()
        toc_md = toc_to_markdown(toc) if toc else "_(no TOC in PDF)_"

        size_mb = pdf.stat().st_size // (1024 * 1024)
        sections.append(
            f"## [{pdf.stem}]({md_path.name})\n\n"
            f"Source: `{pdf.name}` ({size_mb} MB)\n\n"
            f"### Table of contents\n\n{toc_md}\n"
        )
        print(f"  -> {md_path.name} ({md_path.stat().st_size // 1024} KB)")

    index = MANUALS / "INDEX.md"
    index.write_text("# Manuals\n\n" + "\n\n".join(sections) + "\n")
    print(f"\nWrote {index.relative_to(MANUALS.parent.parent)}")


if __name__ == "__main__":
    main()
