# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "beautifulsoup4", "markdownify"]
# ///
"""Mirror the music21 docs (music21.org/music21docs) as offline markdown.

music21 has no PDF manual, so this fetches the Sphinx HTML for the User's
Guide, Module Reference, and Installing sections, strips the page chrome, and
writes one .md per page under docs/manuals/libraries/music21/<section>/, plus
an INDEX.md. The kb `manuals` store picks these up (it globs **/*.md).

Usage:
    uv run scripts/fetch_music21_docs.py [--force]

Incremental: pages already on disk are skipped unless --force.
"""
from __future__ import annotations

import argparse
import re
import time
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

BASE = "https://music21.org/music21docs/"
SECTIONS = ["usersGuide", "moduleReference", "installing"]
ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "docs" / "manuals" / "libraries" / "music21"

session = requests.Session()
session.headers["User-Agent"] = "studio-docs-mirror (personal offline reference)"


def get(url: str) -> BeautifulSoup:
    resp = session.get(url, timeout=30)
    resp.raise_for_status()
    return BeautifulSoup(resp.content, "html.parser")


def page_links(section: str, soup: BeautifulSoup) -> list[str]:
    """Same-section .html pages linked from a section index, in page order."""
    seen: list[str] = []
    for a in soup.select('div[role="main"] a[href]'):
        href = a["href"].split("#")[0]
        if href.endswith(".html") and "/" not in href and href != "index.html" and href not in seen:
            seen.append(href)
    return seen


def to_markdown(soup: BeautifulSoup, url: str) -> tuple[str, str]:
    main = soup.select_one('div[role="main"]') or soup.body
    for junk in main.select("a.headerlink, script, style"):
        junk.decompose()
    title = (main.find(["h1"]) or soup.title).get_text(strip=True)
    md = markdownify(str(main), heading_style="ATX", code_language="python")
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return title, f"Source: {url}\n\n{md}\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="re-download existing pages")
    args = ap.parse_args()

    index_sections: list[str] = []
    for section in SECTIONS:
        index_url = urljoin(BASE, f"{section}/index.html")
        index_soup = get(index_url)
        out_dir = DEST / section
        out_dir.mkdir(parents=True, exist_ok=True)

        pages = ["index.html", *page_links(section, index_soup)]
        print(f"[{section}] {len(pages)} page(s)")
        rows: list[str] = []
        for name in pages:
            url = urljoin(index_url, name)
            md_path = out_dir / (Path(name).stem + ".md")
            if md_path.exists() and not args.force:
                title = md_path.read_text().split("\n", 3)[2].lstrip("# ").strip()
            else:
                soup = index_soup if name == "index.html" else get(url)
                title, md = to_markdown(soup, url)
                md_path.write_text(md)
                print(f"  > {section}/{md_path.name}")
                time.sleep(0.3)  # be polite to music21.org
            rows.append(f"- [{title}]({section}/{md_path.name})")
        index_sections.append(f"## {section}\n\n" + "\n".join(rows))

    (DEST / "INDEX.md").write_text(
        "# music21 documentation (offline mirror)\n\n"
        f"Mirrored from {BASE} by `scripts/fetch_music21_docs.py`. "
        "Re-run with `--force` to refresh.\n\n" + "\n\n".join(index_sections) + "\n"
    )
    print(f"\nWrote {DEST.relative_to(ROOT)}/INDEX.md")


if __name__ == "__main__":
    main()
