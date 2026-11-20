#!/usr/bin/env python3
"""Check wiki page frontmatter, index coverage and local Markdown links."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
PAGE_DIRS = ("sources", "concepts", "entities", "comparisons", "maps", "paths")
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")

def main():
    pages = {p for directory in PAGE_DIRS for p in (WIKI / directory).rglob("*.md")}
    documents = pages | {WIKI / name for name in ("index.md", "log.md", "AGENTS.md")}
    documents.update(ROOT.glob("*.md"))
    for directory in ("reviews", "graph", "raw/papers"):
        documents.update(p for p in (WIKI / directory).rglob("*.md")
                         if not p.is_relative_to(WIKI / "reviews/drafts"))
    errors = []
    index = (WIKI / "index.md").read_text(encoding="utf-8")
    for path in sorted(documents):
        body = path.read_text(encoding="utf-8")
        if path in pages:
            if not body.startswith("---\n") or not all(
                re.search(rf"^{key}:", body, re.MULTILINE) for key in ("type", "title", "created")
            ):
                errors.append((path, "missing required frontmatter"))
            if path.relative_to(WIKI).as_posix() not in index:
                errors.append((path, "missing from the wiki index"))
        for href in LINK.findall(body):
            if href.startswith(("https://", "http://", "#", "mailto:")):
                continue
            if not (path.parent / href.partition("#")[0]).exists():
                errors.append((path, f"broken link {href}"))
    print(f"Checked {len(documents)} documents including {len(pages)} indexed pages. Errors: {len(errors)}.")
    for path, message in errors:
        print(f"  {path.relative_to(ROOT)}: {message}")
    return int(bool(errors))

if __name__ == "__main__":
    raise SystemExit(main())
