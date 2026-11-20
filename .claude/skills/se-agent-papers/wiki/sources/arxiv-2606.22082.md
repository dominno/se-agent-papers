---
type: source
title: "CodeTeam: An LLM-Powered Multi-Agent Framework for Repository-Level Code Generation"
created: 2026-11-19
arxiv_id: "2606.22082"
url: "https://arxiv.org/abs/2606.22082"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "agent-roles", "task-planning", "coding-agents", "repository-context", "agent-communication"]
source_path: "raw/papers/2606.22082.md"
sources: ["https://arxiv.org/abs/2606.22082"]
ingested: "2026-11-19"
---

# CodeTeam: An LLM-Powered Multi-Agent Framework for Repository-Level Code Generation

**Paper:** [2606.22082](https://arxiv.org/abs/2606.22082) · [PDF](https://arxiv.org/pdf/2606.22082) · [HTML](https://arxiv.org/html/2606.22082)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Competing architectural designs yield a contract specifying files, responsibilities and interfaces. A scheduler assigns tasks according to dependencies, while QA checks changes and initiates repairs. [PDF, p. 8](https://arxiv.org/pdf/2606.22082v1#page=8) [PDF, p. 10](https://arxiv.org/pdf/2606.22082v1#page=10) [PDF, p. 11](https://arxiv.org/pdf/2606.22082v1#page=11)

**Key result.** Across 104 NL2Repo-Bench tasks, the mean test pass rate was 34.6 ± 1.3% for PE and 42.3 ± 1.1% for SFT (three seeds). The proportions of fully solved repositories were 5.1% and 6.1%, respectively (pass@1). [PDF, p. 22](https://arxiv.org/pdf/2606.22082v1#page=22)

**Limitations and scope.** SketchBLEU in SketchEval measures similarity to a reference. Execution correctness was therefore tested separately on NL2Repo-Bench. The samples comprised 19 repositories and 104 tasks, respectively. [PDF, p. 18](https://arxiv.org/pdf/2606.22082v1#page=18) [PDF, p. 22](https://arxiv.org/pdf/2606.22082v1#page=22) [PDF, p. 31](https://arxiv.org/pdf/2606.22082v1#page=31) [PDF, p. 32](https://arxiv.org/pdf/2606.22082v1#page=32)

[Section and table audit for 2606.22082v1](../reviews/audit-2026-11-19/2606.22082v1.md)

## Overview

The paper describes a team of agents that builds complete repositories from architectural plans and contracts. [PDF, p. 1](https://arxiv.org/pdf/2606.22082v1#page=1)

## Source files

**Paper license notice.** The arXiv record lists CC BY 4.0. The first page also carries an ACM notice on personal and classroom copying and other uses. [PDF, p. 1](https://arxiv.org/pdf/2606.22082v1#page=1)

arXiv version `2606.22082v1` · PDF pages: 36.

- [Original PDF](https://arxiv.org/pdf/2606.22082v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2606.22082.metadata.json)

PDF bookmarks — [4 Results (p. 16)](https://arxiv.org/pdf/2606.22082v1#page=16) · [6 Threats to Validity (p. 31)](https://arxiv.org/pdf/2606.22082v1#page=31).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Agent roles](../concepts/agent-roles.md)
- [Task planning](../concepts/task-planning.md)
- [Coding agents](../concepts/coding-agents.md)
- [Repository context](../concepts/repository-context.md)
- [Agent communication](../concepts/agent-communication.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
