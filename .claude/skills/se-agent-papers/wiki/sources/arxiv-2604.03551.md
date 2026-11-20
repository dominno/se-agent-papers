---
type: source
title: "AgenticFlict: A Large-Scale Dataset of Merge Conflicts in AI Coding Agent Pull Requests on GitHub"
created: 2026-11-19
arxiv_id: "2604.03551"
url: "https://arxiv.org/abs/2604.03551"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "debugging"]
source_path: "raw/papers/2604.03551.md"
sources: ["https://arxiv.org/abs/2604.03551"]
ingested: "2026-11-19"
---

# AgenticFlict: A Large-Scale Dataset of Merge Conflicts in AI Coding Agent Pull Requests on GitHub

**Paper:** [2604.03551](https://arxiv.org/abs/2604.03551) · [PDF](https://arxiv.org/pdf/2604.03551) · [HTML](https://arxiv.org/html/2604.03551)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** The authors selected 142,652 agent-attributed pull requests that were open or had been closed without merging. They simulated merges at fixed commits, classified outcomes per pull request, and measured the extent of conflicts by file and region. [PDF, p. 2](https://arxiv.org/pdf/2604.03551v2#page=2) [PDF, p. 3](https://arxiv.org/pdf/2604.03551v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2604.03551v2#page=4)

**Key result.** Table 1 reports 29,609 conflicting pull requests and 336,380 conflict regions. The reported 27.67% uses a denominator of 107,026, including 1,493 unlabeled errors. Among the 105,533 pull requests labeled as conflicting or conflict-free in the CLEAN data, the rate is 28.06%. [PDF, p. 5](https://arxiv.org/pdf/2604.03551v2#page=5) [Data package](https://zenodo.org/records/20118379)

**Limitations and scope.** The labels concern textual conflicts in open pull requests and those closed without merging. There is no human-authored PR control group. Missing repository history and failed simulations limit coverage. [PDF, p. 2](https://arxiv.org/pdf/2604.03551v2#page=2) [PDF, p. 7](https://arxiv.org/pdf/2604.03551v2#page=7)

[Section and table audit for 2604.03551v2](../reviews/audit-2026-11-19/2604.03551v2.md)

## Overview

The study analyzes merge conflicts that arise when integrating changes made by coding agents. [PDF, p. 1](https://arxiv.org/pdf/2604.03551v2#page=1)

## Source files

arXiv version `2604.03551v2` · PDF pages: 9.

- [Original PDF](https://arxiv.org/pdf/2604.03551v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2604.03551.metadata.json)

PDF bookmarks — [2 Dataset Curation Methodology (p. 2)](https://arxiv.org/pdf/2604.03551v2#page=2) · [4 Exploratory Empirical Analysis (p. 4)](https://arxiv.org/pdf/2604.03551v2#page=4) · [6 Threats to Validity (p. 7)](https://arxiv.org/pdf/2604.03551v2#page=7).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Debugging](../concepts/debugging.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
