# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "beautifulsoup4", "markdownify"]
# ///
"""Mirror the AbleSet docs (ableset.com/docs) as offline markdown.

AbleSet has no PDF manual; the docs are a Next.js site. This crawls every
/docs/ page reachable from the docs index, strips the page chrome, and writes
one .md per page under data/manuals/daw-video/AbleSet/<page>.md, plus an
INDEX.md. The kb `manuals` store picks these up (it globs **/*.md).

/docs/all (every page concatenated) is skipped; the per-page files cover it.

Usage:
    uv run scripts/fetch_ableset_docs.py [--force]

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

BASE = "https://ableset.com/docs/"
SKIP = {"all"}
ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "data" / "manuals" / "daw-video" / "AbleSet"

session = requests.Session()
session.headers["User-Agent"] = "studio-docs-mirror (personal offline reference)"


def get(url: str) -> BeautifulSoup:
    resp = session.get(url, timeout=30)
    resp.raise_for_status()
    return BeautifulSoup(resp.content, "html.parser")


def page_name(url: str) -> str | None:
    """Doc page slug ('' for the index), or None if not a /docs/ page."""
    p = urlparse(url)
    if p.netloc not in ("", "ableset.com", "www.ableset.com", "ableset.app"):
        return None
    m = re.fullmatch(r"/docs/?([\w-]*)/?", p.path)
    return m.group(1) if m else None


def links(soup: BeautifulSoup, url: str) -> list[str]:
    out = []
    for a in soup.select("a[href]"):
        name = page_name(urljoin(url, a["href"].split("#")[0]))
        if name is not None and name not in SKIP:
            out.append(name)
    return out


def to_markdown(soup: BeautifulSoup, url: str) -> tuple[str, str]:
    h1 = soup.select("h1")[-1]  # the first h1 is the site logo
    main = h1.parent
    for junk in main.select("script, style, nav, a.anchor, span.icon"):
        junk.decompose()
    for img in main.select("img[src]"):
        img["src"] = urljoin(url, img["src"])  # keep images resolvable online
    for a in main.select("a[href]"):
        a["href"] = urljoin(url, a["href"])
    title = h1.get_text(strip=True)
    md = markdownify(str(main), heading_style="ATX")
    # Footer: "This page was last modified on …", "On this page", Previous/Next.
    md = re.split(r"\n\s*This page was last modified on", md)[0]
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return title, f"Source: {url}\n\n{md}\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="re-download existing pages")
    args = ap.parse_args()

    queue, seen = [""], {""}
    rows: list[tuple[str, str]] = []
    while queue:
        name = queue.pop(0)
        url = urljoin(BASE, name)
        md_name = f"{name or 'index'}.md"
        out = DEST / md_name
        try:
            soup = get(url)
        except requests.HTTPError as e:
            print(f"  ! {url}: {e.response.status_code}")  # dead in-doc links
            continue
        if out.exists() and not args.force:
            title = out.read_text().split("\n", 3)[2].lstrip("# ").strip()
        else:
            title, md = to_markdown(soup, url)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(md)
            print(f"  > {md_name}")
        rows.append((md_name, title))
        for link in links(soup, url):
            if link not in seen:
                seen.add(link)
                queue.append(link)
        time.sleep(0.3)  # be polite to ableset.com

    rows.sort()
    (DEST / "INDEX.md").write_text(
        "# AbleSet documentation (offline mirror)\n\n"
        f"Mirrored from {BASE} by `scripts/fetch_ableset_docs.py`. "
        "Re-run with `--force` to refresh.\n\n"
        + "\n".join(f"- [{t}]({p})" for p, t in rows)
        + "\n"
    )
    print(f"\nWrote {DEST.relative_to(ROOT)}/INDEX.md ({len(rows)} pages)")


if __name__ == "__main__":
    main()
