---
type: source
title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
created: 2026-11-19
arxiv_id: "2405.15793"
url: "https://arxiv.org/abs/2405.15793"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "debugging", "benchmarks"]
source_path: "raw/papers/2405.15793.md"
sources: ["https://arxiv.org/abs/2405.15793"]
ingested: "2026-11-19"
---

# SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**Paper:** [2405.15793](https://arxiv.org/abs/2405.15793) · [PDF](https://arxiv.org/pdf/2405.15793) · [HTML](https://arxiv.org/html/2405.15793)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** SWE-agent gives the model tools for repository navigation, editing with feedback and testing. The ablations change features including the file view, editing interface and history management. [PDF, p. 3](https://arxiv.org/pdf/2405.15793v3#page=3) [PDF, p. 4](https://arxiv.org/pdf/2405.15793v3#page=4) [PDF, p. 6](https://arxiv.org/pdf/2405.15793v3#page=6)

**Key result.** GPT-4 Turbo with SWE-agent solved 286/2,294 SWE-bench tasks (12.47%). Static RAG with the same GPT-4 Turbo achieved 1.31%. The 3.79% figure is for RAG with Claude 3 Opus. [PDF, p. 5](https://arxiv.org/pdf/2405.15793v3#page=5) [PDF, p. 6](https://arxiv.org/pdf/2405.15793v3#page=6) [PDF, p. 37](https://arxiv.org/pdf/2405.15793v3#page=37) [PDF, p. 38](https://arxiv.org/pdf/2405.15793v3#page=38)

**Limitations and scope.** The main evaluation covers 12 Python projects. Interface ablations used the 300 Lite tasks. Across six runs, average pass@1 was 17.94% and pass@6 was 32.67%. [PDF, p. 4](https://arxiv.org/pdf/2405.15793v3#page=4) [PDF, p. 6](https://arxiv.org/pdf/2405.15793v3#page=6) [PDF, p. 35](https://arxiv.org/pdf/2405.15793v3#page=35) [PDF, p. 37](https://arxiv.org/pdf/2405.15793v3#page=37)

[Section and table audit for 2405.15793v3](../reviews/audit-2026-11-19/2405.15793v3.md)

## Overview

The paper shows how file access, terminal interaction and test execution affect coding-agent performance. [PDF, p. 1](https://arxiv.org/pdf/2405.15793v3#page=1)

## Source files

arXiv version `2405.15793v3` · PDF pages: 118.

- [Original PDF](https://arxiv.org/pdf/2405.15793v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2405.15793.metadata.json)

PDF bookmarks — [Results (p. 5)](https://arxiv.org/pdf/2405.15793v3#page=5).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Debugging](../concepts/debugging.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
