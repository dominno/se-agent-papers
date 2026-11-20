---
type: source
title: "Effective Strategies for Asynchronous Software Engineering Agents"
created: 2026-11-19
arxiv_id: "2603.21489"
url: "https://arxiv.org/abs/2603.21489"
review_status: "section_reviewed"
full_text_reviewed: false
tags: ["agent-orchestration", "task-planning", "parallelism", "coding-agents"]
source_path: "raw/papers/2603.21489.md"
sources: ["https://arxiv.org/abs/2603.21489"]
ingested: "2026-11-19"
---

# Effective Strategies for Asynchronous Software Engineering Agents

**Paper** [2603.21489](https://arxiv.org/abs/2603.21489) · [PDF](https://arxiv.org/pdf/2603.21489) · [HTML](https://arxiv.org/html/2603.21489)  
**Review status** `section_reviewed` · **Full-text review passed** No

## Research findings

**Method.** CAID assigns tasks according to dependencies, runs engineer agents in isolated working directories, and merges their changes into a shared branch. [PDF, p. 2](https://arxiv.org/pdf/2603.21489v2#page=2) · [PDF, p. 3](https://arxiv.org/pdf/2603.21489v2#page=3)

**Main result.** For MiniMax 2.5, the authors report a 14.7-percentage-point gain on Commit0-Lite. On PaperBench Code-Dev, they report a 25.6-point gain, whereas the 20 printed pairs in Table 9 yield 0.825 points. These rows reproduce the paired-test result from v1. They do not establish the revised result in v2. [PDF, p. 5](https://arxiv.org/pdf/2603.21489v2#page=5) · [PDF, p. 18](https://arxiv.org/pdf/2603.21489v2#page=18) · [PDF, p. 20](https://arxiv.org/pdf/2603.21489v2#page=20) · [PDF, p. 22](https://arxiv.org/pdf/2603.21489v2#page=22)

**Limitations.** On Commit0-Lite, GLM 4.7 gained 3.6 percentage points (one-sided paired test, *p* = 0.095, 16 repositories). The effect of increasing the engineer count depends on the dependency graph and integration costs. [PDF, p. 7](https://arxiv.org/pdf/2603.21489v2#page=7) · [PDF, p. 18](https://arxiv.org/pdf/2603.21489v2#page=18) · [PDF, p. 19](https://arxiv.org/pdf/2603.21489v2#page=19)

[Version 2603.21489v2 audit of sections and tables](../reviews/audit-2026-11-19/2603.21489v2.md)

## Scope

Compares asynchronous collaboration strategies for coding tasks with multiple dependencies. [PDF, p. 1](https://arxiv.org/pdf/2603.21489v2#page=1)

## Source files

arXiv version `2603.21489v2` · PDF pages: 22.

- [Versioned PDF](https://arxiv.org/pdf/2603.21489v2)
- [Retrieval metadata, authors, license, and SHA-256 checksums (local file)](../raw/metadata/2603.21489.metadata.json)

PDF bookmarks — [Main Results (p. 4)](https://arxiv.org/pdf/2603.21489v2#page=4) · [Limitations and Future Directions (p. 9)](https://arxiv.org/pdf/2603.21489v2#page=9).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Task planning](../concepts/task-planning.md)
- [Parallelism](../concepts/parallelism.md)
- [Coding agents](../concepts/coding-agents.md)

## Review notes

- This card was part of the original 100-paper index.
- **Reason for withholding full-text status.** The 20 PaperBench rows give a 0.825-point gain, while the summary and other tables report 25.6 points. The 20 paired, unrounded grades or an erratum are needed to resolve the discrepancy. [Decision and evidence](../reviews/audit-2026-11-19/2603.21489v2.md)
