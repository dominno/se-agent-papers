# Software Engineering and Agent Papers

Search 173 research papers on software engineering and AI agents with Claude Code or Codex. The `se-agent-papers` skill gives your agent a wiki of paper summaries, review notes and links to the exact PDF pages behind the findings.

**Start here to read the wiki on GitHub.** Open the [wiki index](.claude/skills/se-agent-papers/wiki/index.md) and pick a topic, a benchmark or a paper. Each paper title opens a card you can read immediately. Its PDF links open the recorded version on arXiv.

## Install with the Skills CLI

To use the wiki in an agent, open a terminal in the project where you want to ask questions. You’ll need Claude Code or Codex, Node.js 22.20 or newer for the installer, and Python 3.9 or newer for the search script.

The repository is `dominno/se-agent-papers`. If you already have a local checkout, you can use its absolute path instead. Run the command from your destination project.

```sh
npx skills add dominno/se-agent-papers --skill se-agent-papers -a claude-code -a codex
```

Keep just the `-a` option for the agent you use, or keep both and choose **symlink** when prompted so both agents share one wiki.

<details>
<summary>Install across projects or give each agent its own copy</summary>

Add `-g` to the install command to use the skill across your projects. For two independent copies in the current project, run the command below. Papers imported into one copy will appear only in that copy.

```sh
npx skills add dominno/se-agent-papers --skill se-agent-papers -a claude-code -a codex --copy
```

</details>

## Ask your first question

Open your agent in the project where you installed the skill. Paste the prompt for your application into its chat.

| Application | Prompt |
| --- | --- |
| Claude Code | `/se-agent-papers How many response tokens did AgentCoder use on HumanEval and MBPP? Cite the table and PDF page.` |
| Codex | `$se-agent-papers How many response tokens did AgentCoder use on HumanEval and MBPP? Cite the table and PDF page.` |

You can check the answer yourself. Table 9 reports **56.9K response tokens on HumanEval** and **66.3K on MBPP** for AgentCoder with GPT-4. The table caption identifies the token measure and the order of the benchmarks. [AgentCoder card](.claude/skills/se-agent-papers/wiki/sources/arxiv-2312.13010.md) · [AgentCoder v3, PDF page 14](https://arxiv.org/pdf/2312.13010v3#page=14)

## Explore the collection

- **Follow a topic.** The [knowledge and memory map](.claude/skills/se-agent-papers/wiki/maps/knowledge-and-memory.md) connects memory architectures, benchmarks and papers. The [reading paths](.claude/skills/se-agent-papers/wiki/paths/) suggest where to start.
- **Compare approaches.** The [method comparisons](.claude/skills/se-agent-papers/wiki/comparisons/) identify which papers address similar questions and which benchmarks they use.
- **Check a finding.** Reviewed cards summarize methods, results and limitations. In the November 2026 audit, 160 papers passed full-text review. Five have an open question documented in their reports. Eight later additions are catalogued and await review. [Review status and open questions](.claude/skills/se-agent-papers/wiki/reviews/REVIEW_STATUS.md)

## Read the original papers

The wiki cards and local search work offline as soon as the skill is installed. To read a PDF offline or search the article’s full text, download it separately. The commands below assume you start at the root of this checkout or a project with the Claude Code skill installed. For a Codex-only installation, use `.agents/skills/se-agent-papers` in the first command.

```sh
cd .claude/skills/se-agent-papers
python3 scripts/search.py "agent memory" --limit 5
```

From that skill directory, use a Python virtual environment for the optional download dependencies. This example downloads AgentCoder and searches the available full texts.

```sh
python3 -m pip install requests pymupdf
python3 scripts/fetch_fulltext.py --id 2312.13010
python3 scripts/search.py "response token" --fulltext
```

To download the entire catalog, run `python3 scripts/fetch_fulltext.py --all`. PDFs and page-indexed text are stored outside the project in `~/.local/share/se-agent-papers/fulltext/`. Set `SE_AGENT_PAPERS_FULLTEXT_DIR` to use another external directory. [Download details](.claude/skills/se-agent-papers/README.md#read-the-original-papers)

## Import a paper

From the same skill directory, pass an arXiv ID or link to the importer. The version suffix in this example selects the first revision.

```sh
python3 -m pip install requests
python3 scripts/ingest.py https://arxiv.org/abs/2211.12588v1
```

The paper becomes searchable with status `catalog_import_only`. Its findings still need review. Add `--fulltext` to save the PDF locally as well. Run the import in the source checkout if you intend to contribute the new card to this repository. [Import guide](.claude/skills/se-agent-papers/README.md#import-a-paper) · [Review checklist](.claude/skills/se-agent-papers/wiki/reviews/FULLTEXT_REVIEW_CHECKLIST.md)

## Contributing

To suggest a paper, correct a cited finding, or change a search tool, see the [contribution guide](CONTRIBUTING.md).

## License and source material

The [MIT License](LICENSE) covers the contributors’ original code, skill instructions and wiki notes. The wiki links to the original papers on arXiv. Optional downloads of PDFs and full-text extracts stay on the reader’s disk. Each paper retains its own terms.
