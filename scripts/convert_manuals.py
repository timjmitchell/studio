# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pymupdf4llm",
#     "pymupdf",
#     "tomli; python_version < '3.11'",
# ]
# ///
"""Convert every PDF under docs/manuals/<category>/ to markdown and generate a
per-category INDEX.md plus a master INDEX.md.

- Incremental: a PDF is skipped if its .md is already newer than the PDF.
  Pass --force to reconvert everything.
- Metadata (name, vendor, version, source url) comes from docs/manuals/sources.toml,
  keyed by the file's path relative to docs/manuals/.
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import tomllib  # py3.11+
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib  # type: ignore

import pymupdf
import pymupdf4llm

MANUALS = Path(__file__).resolve().parent.parent / "docs" / "manuals"
FORCE = "--force" in sys.argv


def load_sources() -> dict[str, dict]:
    toml_path = MANUALS / "sources.toml"
    if not toml_path.exists():
        return {}
    data = tomllib.loads(toml_path.read_text())
    return {m["file"]: m for m in data.get("manual", [])}


def toc_to_markdown(toc: list[list], max_depth: int = 3) -> str:
    lines = []
    for level, title, page in toc:
        if level > max_depth:
            continue
        indent = "  " * (level - 1)
        lines.append(f"{indent}- {title.strip()} (p. {page})")
    return "\n".join(lines)


def source_line(meta: dict | None, pdf_name: str, size_mb: int) -> str:
    if not meta:
        return f"Source PDF: `{pdf_name}` ({size_mb} MB)"
    vendor = meta.get("vendor", "")
    version = meta.get("version", "")
    url = meta.get("url", "")
    bits = [f"**Vendor:** {vendor}" if vendor else ""]
    if version:
        bits.append(f"**Version:** {version}")
    bits.append(f"**PDF:** `{pdf_name}` ({size_mb} MB)")
    bits.append(f"**Download:** {url}" if url else "**Download:** _(url TBD)_")
    return " · ".join(b for b in bits if b)


def convert_pdf(pdf: Path) -> Path:
    md_path = pdf.with_suffix(".md")
    if md_path.exists() and not FORCE and md_path.stat().st_mtime >= pdf.stat().st_mtime:
        print(f"  = {pdf.relative_to(MANUALS)} (up to date)")
        return md_path
    print(f"  > converting {pdf.relative_to(MANUALS)} ({pdf.stat().st_size // (1024*1024)} MB)...")
    md = pymupdf4llm.to_markdown(str(pdf), show_progress=False)
    md_path.write_text(md)
    print(f"    -> {md_path.name} ({md_path.stat().st_size // 1024} KB)")
    return md_path


def main() -> None:
    sources = load_sources()
    categories = sorted(p for p in MANUALS.iterdir() if p.is_dir())
    master_rows: list[str] = []

    for cat in categories:
        pdfs = sorted(cat.glob("*.pdf"))
        if not pdfs:
            continue
        print(f"\n[{cat.name}] {len(pdfs)} manual(s)")
        sections: list[str] = []
        for pdf in pdfs:
            md_path = convert_pdf(pdf)
            rel = str(pdf.relative_to(MANUALS))
            meta = sources.get(rel)
            name = meta["name"] if meta else pdf.stem

            with pymupdf.open(str(pdf)) as doc:
                toc = doc.get_toc()
            toc_md = toc_to_markdown(toc) if toc else "_(no embedded TOC in PDF)_"
            size_mb = pdf.stat().st_size // (1024 * 1024)

            sections.append(
                f"## [{name}]({md_path.name})\n\n"
                f"{source_line(meta, pdf.name, size_mb)}\n\n"
                f"<details>\n<summary>Table of contents</summary>\n\n{toc_md}\n\n</details>\n"
            )

        title = cat.name.replace("-", " ").title()
        (cat / "INDEX.md").write_text(
            f"# {title}\n\n[← all manuals](../INDEX.md)\n\n" + "\n\n".join(sections) + "\n"
        )
        master_rows.append(f"- [{title}]({cat.name}/INDEX.md) — {len(pdfs)} manual(s)")
        print(f"  wrote {cat.name}/INDEX.md")

    total = sum(len(list(c.glob('*.pdf'))) for c in categories)
    master = (
        "# Manuals\n\n"
        "Software & gear manuals for the studio, converted to markdown.\n"
        "Metadata and download links live in [`sources.toml`](sources.toml).\n\n"
        f"**{total} manuals** across {len(master_rows)} categories:\n\n"
        + "\n".join(master_rows)
        + "\n"
    )
    (MANUALS / "INDEX.md").write_text(master)
    print(f"\nWrote master INDEX.md ({total} manuals, {len(master_rows)} categories)")


if __name__ == "__main__":
    main()
