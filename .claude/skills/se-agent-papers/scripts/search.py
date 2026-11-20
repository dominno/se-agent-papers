#!/usr/bin/env python3
"""Search the research catalog, reviewed notes, and optional local PDF text."""

import argparse
import json
import re
import sys
from paper_storage import FULLTEXT, METADATA, ROOT, WIKI

VERSION = re.compile(r"(?P<id>\d{4}\.\d{4,5})v(?P<number>\d+)")
IDENTIFIER = re.compile(r"(?:arxiv:\s*|https?://arxiv.org/(?:pdf|abs)/)?(\d{4}\.\d{4,5})(v\d+)?(?:\.pdf)?(?:#page=[1-9]\d*)?", re.I)
PAGE = re.compile(r"^## PDF page ([1-9]\d*)\s*$", re.MULTILINE)
LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
NORMALIZE = re.compile(r"[\W_]+", re.UNICODE)
PAGE_LIMIT = 5


def normalize(text):
    return NORMALIZE.sub(" ", text.casefold()).strip()


def match_quality(text, phrase, words):
    """Prefer exact phrases; otherwise require each word in the same passage."""
    normalized = " " + normalize(text) + " "
    if " " + phrase + " " in normalized:
        return 2
    return int(all(" " + word + " " in normalized for word in words))


def report_index():
    reports = {}
    for path in (WIKI / "reviews").glob("**/*.md"):
        match = VERSION.fullmatch(path.stem)
        if match:
            key = int(match["number"]), path
            reports[match["id"]] = max(key, reports.get(match["id"], key))
    return {article: path for article, (_, path) in reports.items()}


def get_version(article, report):
    if report:
        return report.stem
    metadata = METADATA / (article + ".metadata.json")
    if metadata.is_file():
        value = json.loads(metadata.read_text(encoding="utf-8")).get("version", "")
        if VERSION.fullmatch(value) and value.startswith(article + "v"):
            return value
    versions = [match for path in FULLTEXT.glob(article + "v*.pdf")
                if (match := VERSION.fullmatch(path.stem))]
    if versions:
        return max(versions, key=lambda match: int(match["number"])).group()
    capture = FULLTEXT / (article + ".md")
    if capture.is_file():
        with capture.open(encoding="utf-8") as source:
            for line in source:
                if line.startswith("## PDF page "):
                    break
                if line.startswith("Document:"):
                    value = line.removeprefix("Document:").strip()
                    if VERSION.fullmatch(value) and value.startswith(article + "v"):
                        return value
    return None


def capture_pages(article, version):
    capture = FULLTEXT / (article + ".md")
    if capture.is_file():
        try:
            sections = PAGE.split(capture.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            print(f"Cannot read {capture.name} as UTF-8. Use fetch_fulltext.py --id {article} --force.", file=sys.stderr)
            return None
        if len(sections) > 1 and f"Document: {version}" in sections[0].splitlines():
            return zip(sections[1::2], sections[2::2])
    return None


def article_search(record, report, version, phrase, words, identifier, capture):
    article = record["arxiv_id"]
    card = WIKI / "sources" / ("arxiv-" + article + ".md")
    fields = []
    score = 0
    cited_pages = {}
    text_pages = {}

    def add_field(name, weight, quality):
        nonlocal score
        if quality:
            fields.append(name)
            score = max(score, weight + quality)

    if identifier:
        add_field("id", 100, 2)
    else:
        title = record["title"]
        title_weight = 15 if normalize(title.partition(":")[0]) == phrase else 12
        add_field("title", title_weight, match_quality(title, phrase, words))
        catalog_text = " ".join([record.get("category", ""), *record.get("concepts", []),
                                 record.get("summary_en", record.get("summary_pl", ""))])
        add_field("catalog", 8, match_quality(catalog_text, phrase, words))
        for name, path in (("card", card), ("report", report)):
            if not path or not path.is_file():
                continue
            body = path.read_text(encoding="utf-8")
            body = re.sub(r"\A---\n.*?\n---\n", "", body, count=1, flags=re.S)
            best = 0
            for paragraph in re.split(r"\n\s*\n|\n(?=[*-] )", body):
                quality = match_quality(LINK.sub(r"\1", paragraph), phrase, words)
                if quality:
                    best = max(best, quality)
                    for _, href in LINK.findall(paragraph):
                        target, sep, fragment = href.partition("#page=")
                        if sep and fragment.isdigit() and version and target.rstrip("/").split("/")[-1] in (version, version + ".pdf"):
                            page_no = int(fragment)
                            cited_pages[page_no] = max(quality, cited_pages.get(page_no, 0))
            add_field(name, 5, best)
        if capture is not None:
            for number, content in capture:
                quality = match_quality(content, phrase, words)
                if quality:
                    text_pages[int(number)] = quality
            add_field("fulltext", 2, max(text_pages.values(), default=0))

    if not fields:
        return None
    pages = sorted(cited_pages.keys() | text_pages.keys(),
                   key=lambda n: (-max(cited_pages.get(n, 0), text_pages.get(n, 0)),
                                  -(n in text_pages), n))
    pdf_url = "https://arxiv.org/pdf/" + (version or article)
    return score, {
        "arxiv_id": article, "version": version, "title": record["title"],
        "status": record["review_status"], "matched": fields,
        "card": card.relative_to(ROOT).as_posix() if card.is_file() else None,
        "report": report.relative_to(ROOT).as_posix() if report else None,
        "page_count": len(pages),
        "pages": [{"page": n, "link": f"{pdf_url}#page={n}",
                   "evidence": "fulltext" if n in text_pages else "note citation"}
                  for n in pages[:PAGE_LIMIT]],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="+", help="title, arXiv ID, topic, or search phrase")
    parser.add_argument("--status", help="only return records with this exact review status")
    parser.add_argument("--limit", type=int, default=10, help="maximum papers to return (default: 10)")
    parser.add_argument("--fulltext", action="store_true", help="also search available local PDF page captures")
    parser.add_argument("--json", action="store_true", help="print results as a JSON array")
    args = parser.parse_args()
    query = " ".join(args.query).strip()
    phrase = normalize(query)
    if not phrase or args.limit < 1:
        parser.error("provide a nonempty query and a positive --limit")
    reports = report_index()
    words = phrase.split()
    identifier = IDENTIFIER.fullmatch(query)
    results = []
    eligible = searched = 0
    with (WIKI / "catalog/papers.jsonl").open(encoding="utf-8") as records:
        for line in records:
            if not line.strip():
                continue
            record = json.loads(line)
            if args.status and record["review_status"] != args.status:
                continue
            article = record["arxiv_id"]
            report = reports.get(article)
            version = get_version(article, report)
            if identifier and (identifier[1] != article or
                               (identifier[2] and version != article + identifier[2].lower())):
                continue
            capture = None
            if args.fulltext and not identifier:
                eligible += 1
                capture = capture_pages(article, version)
                if capture is not None:
                    searched += 1
            hit = article_search(record, report, version, phrase, words, identifier, capture)
            if hit:
                results.append(hit)
    if searched < eligible:
        print(f"Full-text search covered {searched} of {eligible} eligible papers. "
              "The other papers were searched using the wiki only. "
              "Use fetch_fulltext.py --id ID to retrieve a missing paper.", file=sys.stderr)
    results.sort(key=lambda hit: (-hit[0], hit[1]["title"].casefold(), hit[1]["arxiv_id"]))
    selected = [row for _, row in results[:args.limit]]
    if args.json:
        print(json.dumps(selected, indent=2, ensure_ascii=False))
    elif not selected:
        print("No matching papers.")
    else:
        print(f"Showing {len(selected)} of {len(results)} matching papers.")
        for row in selected:
            print(f"\n{row['version'] or row['arxiv_id']} [{row['status']}] {row['title']}")
            print("  Matched in " + ", ".join(row["matched"]))
            for key in ("card", "report"):
                if row[key]:
                    print(f"  {key.title()}: {row[key]}")
            for page in row["pages"]:
                print(f"  p. {page['page']} ({page['evidence']}): {page['link']}")
            if row["page_count"] > len(row["pages"]):
                print(f"  Showing {len(row['pages'])} of {row['page_count']} matching or cited pages.")


if __name__ == "__main__":
    main()
