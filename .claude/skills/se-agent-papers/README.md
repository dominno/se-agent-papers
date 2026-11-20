# Software Engineering and Agent Papers

[Skill instructions](SKILL.md) · [Wiki index](wiki/index.md)

## Import a paper

From the skill directory, give the importer a modern arXiv ID or abstract/PDF URL. An explicit version pins that revision. An unversioned ID selects the version returned by arXiv at import time.

```sh
python3 -m pip install requests
python3 scripts/ingest.py https://arxiv.org/abs/2211.12588v1
```

Add `--fulltext` to download the PDF and extract its pages into the external cache (requires `pymupdf`). Import creates the searchable card and provenance record, updates the index, graph, catalog, counts and log, and assigns `catalog_import_only`. Existing cards keep their reviewed version. To contribute the addition upstream, run the importer in the source checkout. Running it in an installed skill updates that local copy.

## Read the original papers

Each card links to the arXiv record and cites physical pages of the reviewed PDF version. The repository includes the cards, audit reports and [per-paper metadata](wiki/raw/metadata/). Downloading papers is optional. To fetch AgentCoder directly from arXiv for local reading or research, run these commands in a Python virtual environment.

```sh
python3 -m pip install requests pymupdf
python3 scripts/fetch_fulltext.py --id 2312.13010
python3 scripts/search.py "test designer" --fulltext
```

The default download directory is `~/.local/share/se-agent-papers/fulltext/`. Set `SE_AGENT_PAPERS_FULLTEXT_DIR` to an external directory to use a different disk. Search and download use the same setting. The downloader extracts numbered pages for offline search. For a paper with an audit digest it checks the PDF against the recorded SHA-256 before saving it. Different PyMuPDF versions can produce slightly different text from the same verified PDF. [Retrieval script](scripts/fetch_fulltext.py)

To restore all catalogued versions, run `python3 scripts/fetch_fulltext.py --all`. The batch runs sequentially against `export.arxiv.org`, waits at least three seconds between downloads, and skips existing copies. Run one download process at a time. The arXiv search API supplies metadata and PDF links. The catalog already records those links and versions, so restoration can fetch the PDFs directly. arXiv permits local storage for personal or research use. [API manual](https://info.arxiv.org/help/api/user-manual.html) · [arXiv terms of use](https://info.arxiv.org/help/api/tou.html) · [Programmatic access](https://info.arxiv.org/help/bulk_data.html)

## License and source material

The [MIT License](LICENSE) covers the contributors’ original code, skill instructions and wiki notes. The wiki links to the original papers on arXiv. Optional downloads of PDFs and full-text extracts stay on the reader’s disk. Each paper retains its own terms.
