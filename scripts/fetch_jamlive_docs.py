# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "beautifulsoup4", "markdownify"]
# ///
"""Mirror the MIDI Guitar 3 docs (jam.live) as offline markdown.

Jam Origin has no PDF manual for MIDI Guitar 3; the docs are an MkDocs site
at jam.live (jamorigin.com/beta redirects there). This crawls every same-site
page reachable from the home page, strips the page chrome, and writes one .md
per page under docs/manuals/plugins/MIDI-Guitar-3/<path>.md, plus an INDEX.md.
The kb `manuals` store picks these up (it globs **/*.md).

Usage:
    uv run scripts/fetch_jamlive_docs.py [--force]

Incremental: pages already on disk are skipped unless --force.
"""
from __future__ import annotations

import argparse
import re
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

BASE = "https://jam.live/"
SKIP = ("shop/",)  # storefront, no docs content
# Old jamorigin.com pages the new site still links to as its DAW setup reference.
EXTRA = {"legacy/mg2-daw-guide.md": "https://www.jamorigin.com/docs/daw/"}
ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "docs" / "manuals" / "plugins" / "MIDI-Guitar-3"

session = requests.Session()
session.headers["User-Agent"] = "studio-docs-mirror (personal offline reference)"


def get(url: str) -> BeautifulSoup:
    resp = session.get(url, timeout=30)
    resp.raise_for_status()
    return BeautifulSoup(resp.content, "html.parser")


def rel_path(url: str) -> str | None:
    """Site-relative page path ('' for home), or None if off-site/not a page."""
    p = urlparse(url)
    if p.netloc not in ("", "jam.live", "www.jam.live"):
        return None
    path = p.path.lstrip("/")
    if path and not path.endswith("/") and not path.endswith(".html"):
        return None  # assets: images, css, zips
    return path


def md_name(path: str) -> str:
    return (path.rstrip("/").removesuffix(".html") or "index") + ".md"


def links(soup: BeautifulSoup, url: str) -> list[str]:
    out = []
    for a in soup.select("a[href]"):
        target = urljoin(url, a["href"].split("#")[0])
        path = rel_path(target)
        if path is not None and not path.startswith(SKIP):
            out.append(path)
    return out


def to_markdown(soup: BeautifulSoup, url: str) -> tuple[str, str]:
    main = (
        soup.select_one("article.md-content__inner")  # jam.live (MkDocs)
        or soup.select_one(".entry-content")  # jamorigin.com (WordPress)
        or soup.select_one("main")
        or soup.body
    )
    for junk in main.select("a.headerlink, script, style"):
        junk.decompose()
    for img in main.select("img[src]"):
        img["src"] = urljoin(url, img["src"])  # keep images resolvable online
    for a in main.select("a[href]"):
        a["href"] = urljoin(url, a["href"])
    h1 = main.find("h1") or soup.title
    title = h1.get_text(strip=True) if h1 else url
    md = markdownify(str(main), heading_style="ATX")
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return title, f"Source: {url}\n\n{md}\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="re-download existing pages")
    args = ap.parse_args()

    queue, seen = [""], {""}
    rows: list[tuple[str, str]] = []
    while queue:
        path = queue.pop(0)
        url = urljoin(BASE, path)
        out = DEST / md_name(path)
        soup = get(url)
        if out.exists() and not args.force:
            title = out.read_text().split("\n", 3)[2].lstrip("# ").strip()
        else:
            title, md = to_markdown(soup, url)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(md)
            print(f"  > {out.relative_to(DEST)}")
        rows.append((md_name(path), title))
        for link in links(soup, url):
            if link not in seen:
                seen.add(link)
                queue.append(link)
        time.sleep(0.3)  # be polite to jam.live

    for name, url in EXTRA.items():
        out = DEST / name
        if out.exists() and not args.force:
            title = out.read_text().split("\n", 3)[2].lstrip("# ").strip()
        else:
            title, md = to_markdown(get(url), url)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(md)
            print(f"  > {name}")
        rows.append((name, f"{title} (legacy MIDI Guitar 2 docs)"))

    rows.sort()
    notes = DEST / "MIDI-Guitar-3-Field-Notes.md"  # hand-written, not mirrored
    see_also = f"See also: [Field Notes]({notes.name}).\n\n" if notes.exists() else ""
    (DEST / "INDEX.md").write_text(
        "# MIDI Guitar 3 documentation (offline mirror)\n\n"
        f"Mirrored from {BASE} by `scripts/fetch_jamlive_docs.py`. "
        "Re-run with `--force` to refresh.\n\n"
        + see_also
        + "\n".join(f"- [{t}]({p})" for p, t in rows)
        + "\n"
    )
    print(f"\nWrote {DEST.relative_to(ROOT)}/INDEX.md ({len(rows)} pages)")


if __name__ == "__main__":
    main()
