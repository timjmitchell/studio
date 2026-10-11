# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "beautifulsoup4", "markdownify"]
# ///
"""Mirror the UAD Console for Apollo manual (help.uaudio.com) as offline markdown.

UA publishes the Console manual only as Zendesk help-center articles, no PDF.
The Zendesk API returns every article in the section, in manual order, with its
HTML body and an updated_at stamp, so this needs no crawling. Writes one .md per
article under docs/manuals/controllers-interfaces/UAD-Console/NN-<slug>.md plus
an INDEX.md. The kb `manuals` store picks these up (it globs **/*.md).

Usage:
    uv run scripts/fetch_uad_console_docs.py [--force]

Incremental: an article is re-fetched only when UA's updated_at is newer than
the one recorded in the file, or with --force.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

SECTION = 25052396869908  # "UAD Console for Apollo Manual"
API = f"https://help.uaudio.com/api/v2/help_center/en-us/sections/{SECTION}/articles.json"
SECTION_URL = f"https://help.uaudio.com/hc/en-us/sections/{SECTION}"
ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "docs" / "manuals" / "controllers-interfaces" / "UAD-Console"

session = requests.Session()
session.headers["User-Agent"] = "studio-docs-mirror (personal offline reference)"


def articles() -> list[dict]:
    out, url = [], f"{API}?per_page=100&sort_by=position&sort_order=asc"
    while url:
        resp = session.get(url, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        out += data["articles"]
        url = data.get("next_page")
    return sorted(out, key=lambda a: a["position"])


def slug(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def to_markdown(article: dict) -> str:
    soup = BeautifulSoup(article["body"] or "", "html.parser")
    for junk in soup.select("script, style"):
        junk.decompose()
    md = markdownify(str(soup), heading_style="ATX")
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return (
        f"Source: {article['html_url']}\n"
        f"Updated: {article['updated_at']}\n\n"
        f"# {article['title']}\n\n{md}\n"
    )


def recorded_update(path: Path) -> str:
    if not path.exists():
        return ""
    m = re.search(r"^Updated: (\S+)", path.read_text(), re.M)
    return m.group(1) if m else ""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="re-write every article")
    args = ap.parse_args()

    DEST.mkdir(parents=True, exist_ok=True)
    rows = []
    for i, art in enumerate(articles()):
        name = f"{i:02d}-{slug(art['title'])}.md"
        out = DEST / name
        if args.force or recorded_update(out) < art["updated_at"]:
            out.write_text(to_markdown(art))
            print(f"  > {name}")
        rows.append((name, art["title"], art["updated_at"][:10]))

    notes = DEST / "UAD-Console-Field-Notes.md"  # hand-written, not mirrored
    see_also = f"See also: [Field Notes]({notes.name}).\n\n" if notes.exists() else ""
    (DEST / "INDEX.md").write_text(
        "# UAD Console for Apollo manual (offline mirror)\n\n"
        f"Mirrored from {SECTION_URL} by `scripts/fetch_uad_console_docs.py` "
        "via the Zendesk API. Re-run to pick up updated articles.\n\n"
        + see_also
        + "\n".join(f"- [{t}]({p}) · updated {d}" for p, t, d in rows)
        + "\n"
    )
    print(f"\nWrote {DEST.relative_to(ROOT)}/INDEX.md ({len(rows)} articles)")


if __name__ == "__main__":
    main()
