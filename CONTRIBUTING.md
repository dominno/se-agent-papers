# Contributing

You can suggest a paper, correct a finding, or improve the search and import tools. To suggest a paper without editing the wiki, open a GitHub issue with its arXiv link and a sentence about what it adds to the collection. For a correction, link the card and the PDF page that supports your reading.

## Add a paper

Fork the repository, clone your fork, and create a branch. Work in the source checkout so your changes can be included in a pull request. From the repository root, enter the skill directory. Run the remaining Python commands from there.

```sh
cd .claude/skills/se-agent-papers
```

Check the base arXiv ID first. This finds an existing card even if it covers a different revision. If the paper is new, import the revision you checked. Replace the example ID and version with your paper’s.

```sh
python3 scripts/search.py 2211.12588
python3 -m pip install requests
python3 scripts/ingest.py 2211.12588v1
```

Use Python 3.9 or newer and a virtual environment for the import dependency. Open the generated card in `wiki/sources/` and check its title, authors, version, source links and recorded license. The importer updates the index, catalog, graph, review counts and log. Include those changes in the same pull request and update any collection totals quoted in the README and review status page. A new card starts at `catalog_import_only` and can be contributed at that stage.

## Correct or review a finding

Write wiki content in English. Open the version cited by the card and link each finding to the physical PDF page that supports it. For a table result, identify the table, benchmark, model and units. For example, the AgentCoder card identifies the values in Table 9 as *response tokens* and names the two benchmarks in the order used by the authors. [Example card](.claude/skills/se-agent-papers/wiki/sources/arxiv-2312.13010.md) · [AgentCoder v3, page 14](https://arxiv.org/pdf/2312.13010v3#page=14)

If a table and the surrounding text disagree, cite both passages and describe the discrepancy. When a correction affects an audit report, update the report alongside the card and record the change in `wiki/log.md`. Award `fulltext_reviewed` after completing the section, table and appendix checks and documenting an independent check in the version-specific report. [Wiki editing rules](.claude/skills/se-agent-papers/wiki/AGENTS.md) · [Full-text review checklist](.claude/skills/se-agent-papers/wiki/reviews/FULLTEXT_REVIEW_CHECKLIST.md)

Keep downloaded PDFs and full-text extracts in the external cache. Commit your own summaries, provenance and versioned links. [Download and licensing guide](.claude/skills/se-agent-papers/README.md)

## Check and submit

Run the wiki linter and search for your paper by ID. Open the returned card and check that its citations lead to the intended pages. For a change to a script, also run the command whose behavior you changed.

```sh
python3 scripts/wiki_lint.py
python3 scripts/search.py 2211.12588v1 --json
```

Commit your changes, push your branch to your fork, and open a pull request against this repository. Describe what changed and how you checked it. For a paper contribution, include the arXiv version, review status and any open evidence questions.
