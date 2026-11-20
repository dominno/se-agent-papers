#!/usr/bin/env python3
"""Add an arXiv publication to the searchable wiki (modern arXiv IDs)."""

import argparse
from contextlib import closing
from datetime import date
import hashlib
from html import escape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sqlite3
import subprocess
import sys
import tempfile
from xml.etree import ElementTree

from fetch_fulltext import fetch
from paper_storage import WIKI

ID = re.compile(r"(?:arxiv:\s*|https?://arxiv\.org/(?:abs|pdf)/)?"
                r"(\d{4}\.\d{4,5})(v[1-9]\d*)?(?:\.pdf)?", re.I)
CATALOG = WIKI / "catalog/papers.jsonl"
STATUS = "catalog_import_only"


class LicenseLink(HTMLParser):
    url = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and attrs.get("title") == "Rights to this article":
            url = attrs.get("href", "")
            if re.fullmatch(r"https?://(?:creativecommons\.org/(?:licenses|publicdomain)|arxiv\.org/licenses)/[\w./-]+", url):
                self.url = url


def read_record(article, requested_version):
    query = article + requested_version
    feed = ElementTree.fromstring(fetch("https://export.arxiv.org/api/query?id_list=" + query).content)
    entry = feed.find("{*}entry")
    if entry is None:
        raise ValueError(f"No arXiv entry for {query}")
    version = entry.findtext("{*}id", "").rsplit("/", 1)[-1]
    if not re.fullmatch(re.escape(article) + r"v[1-9]\d*", version) or (requested_version and version != query):
        raise ValueError(f"arXiv did not return the requested record for {query}")
    url = "https://arxiv.org/abs/" + version
    license_link = LicenseLink()
    license_link.feed(fetch(url).text)
    title = " ".join(entry.findtext("{*}title", "").split())
    authors = [" ".join(node.text.split()) for node in entry.findall("{*}author/{*}name") if node.text]
    if not title or not authors:
        raise ValueError(f"Incomplete arXiv metadata for {version}")
    return dict(arxiv_id=article, version=version, title=title, authors=authors, url=url,
                source_url="https://arxiv.org/pdf/" + version, license_url=license_link.url,
                categories=[node.get("term") for node in entry.findall("{*}category") if node.get("term")],
                published=entry.findtext("{*}published"), updated=entry.findtext("{*}updated"))


def json_text(value, indent=None):
    return json.dumps(value, ensure_ascii=False, indent=indent) + "\n"


def markdown(text):
    return re.sub(r"([\\`*_\[\]])", r"\\\1", escape(text, quote=False))


def appended(path, line):
    return path.read_text(encoding="utf-8").rstrip("\n") + "\n" + line + "\n"


def changes(meta, records):
    article, version, title = (meta[key] for key in ("arxiv_id", "version", "title"))
    today = date.today().isoformat()
    card = f"sources/arxiv-{article}.md"
    raw = f"raw/papers/{article}.md"
    metadata = f"raw/metadata/{article}.metadata.json"
    for name in (card, raw, metadata):
        if (WIKI / name).exists():
            raise ValueError(f"Uncatalogued file already exists: wiki/{name}")
    label = markdown(title)
    reference = f"[{version}]({meta['url']}) · [PDF]({meta['source_url']})"
    license_note = f"[Recorded license]({meta['license_url']})" if meta["license_url"] else "License requires verification."
    fields = dict(type="source", title=title, created=today, arxiv_id=article, url=meta["url"],
                  review_status=STATUS, full_text_reviewed=False, tags=[], source_path=raw,
                  sources=[meta["url"]], ingested=today)
    frontmatter = "\n".join(f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in fields.items())
    source = (f"---\n{frontmatter}\n---\n\n# {label}\n\n{reference}\n\n"
              f"**Authors.** {markdown(', '.join(meta['authors']))}\n\n"
              f"**Review status.** `{STATUS}`. Methods, results and limitations await review.\n\n"
              f"{license_note} · [Source metadata](../{metadata})\n")
    record = dict(schema_version=1, arxiv_id=article, title=title, url=meta["url"],
                  category=", ".join(meta["categories"]), catalog_date=today, original_index=False,
                  concepts=[], review_status=STATUS, summary_en="")
    graph = WIKI / "graph/nodes.jsonl"
    index = WIKI / "index.md"
    progress = WIKI / "catalog/review_progress.json"
    counts = dict.fromkeys(json.loads(progress.read_text()), 0)
    for row in [*records, record]:
        key = row["review_status"]
        counts[key] = counts.get(key, 0) + 1
    counts["total"] = len(records) + 1
    return {
        WIKI / card: source,
        WIKI / raw: f"# Source record\n\n{label}\n\n{reference} · [Publication card](../../{card})\n",
        WIKI / metadata: json_text(meta, 2),
        index: appended(index, f"- [{label}]({card}) · {reference} · `{STATUS}` #paper"),
        WIKI / "log.md": appended(WIKI / "log.md", f"\n## [{today}] Imported {version}\n\n[{label}]({card}) · `{STATUS}`"),
        graph: appended(graph, json_text(dict(id="arxiv:" + article, type="paper", title=title)).rstrip()),
        progress: json_text(counts, 2),
        CATALOG: appended(CATALOG, json_text(record).rstrip()),
    }


def publish(pending):
    # A stopped import can finish the remaining atomic replacements on its next run.
    for src in sorted(pending.rglob("*")):
        if src.is_file():
            src.replace(WIKI / src.relative_to(pending))
    for folder in sorted(pending.rglob("*"), reverse=True):
        folder.rmdir()
    pending.rmdir()


def ingest(article, suffix):
    # Serialize local writers using the OS's SQLite file locking on all platforms.
    key = hashlib.sha256(str(WIKI.resolve()).encode()).hexdigest()
    lock = Path(tempfile.gettempdir()) / f"se-agent-papers-{key}.sqlite3"
    with closing(sqlite3.connect(lock, timeout=180)) as connection:
        connection.execute("BEGIN IMMEDIATE")
        pending = WIKI / ".ingest-pending"
        if pending.exists():
            publish(pending)
        records = [json.loads(line) for line in CATALOG.read_text().splitlines() if line.strip()]
        if any(row["arxiv_id"] == article for row in records):
            stored = json.loads((WIKI / f"raw/metadata/{article}.metadata.json").read_text())["version"]
            if suffix and stored != article + suffix:
                raise ValueError(f"Already catalogued as {stored}. Updating a paper version requires review.")
            return f"Already catalogued: {stored}"
        meta = read_record(article, suffix)
        updates = changes(meta, records)
        with tempfile.TemporaryDirectory(dir=WIKI, prefix=".ingest-") as staging:
            for target, content in updates.items():
                staged = Path(staging) / target.relative_to(WIKI)
                staged.parent.mkdir(parents=True, exist_ok=True)
                staged.write_text(content, encoding="utf-8")
            Path(staging).rename(pending)
            publish(pending)
        return f"Added {meta['version']} to wiki/sources/arxiv-{article}.md ({STATUS})"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="arXiv ID or abstract/PDF URL, optionally versioned")
    parser.add_argument("--fulltext", action="store_true", help="also download the pinned PDF to the external cache")
    args = parser.parse_args()
    match = ID.fullmatch(args.source.strip())
    if not match:
        parser.error("expected a modern arXiv ID or arxiv.org abstract/PDF URL")
    try:
        print(ingest(match[1], (match[2] or "").lower()), flush=True)
        if args.fulltext:
            return subprocess.run([sys.executable, Path(__file__).with_name("fetch_fulltext.py"),
                                   "--id", match[1]]).returncode
    except Exception as error:
        print(f"Ingest failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
