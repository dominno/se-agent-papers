---
type: source
title: "SetupBench: Assessing Software Engineering Agents' Ability to Bootstrap Development Environments"
created: 2026-11-19
arxiv_id: "2507.09063"
url: "https://arxiv.org/abs/2507.09063"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "repository-context", "evaluation-metrics", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2507.09063.md"
sources: ["https://arxiv.org/abs/2507.09063"]
ingested: "2026-11-19"
---

# SetupBench: Assessing Software Engineering Agents' Ability to Bootstrap Development Environments

**Paper:** [2507.09063](https://arxiv.org/abs/2507.09063) · [PDF](https://arxiv.org/pdf/2507.09063) · [HTML](https://arxiv.org/html/2507.09063)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** SetupBench uses a deterministic final command to check whether the development environment works. The sample covers seven language ecosystems and five database engines. [PDF, p. 1](https://arxiv.org/pdf/2507.09063v1#page=1)

**Key result.** Across five OpenHands configurations, repository setup succeeded in 21–31 of 54 cases (38.9–57.4%), and local database setup in 3–8 of 15 (20.0–53.3%). Claude 4 had the best overall result, 58/93. [PDF, p. 2](https://arxiv.org/pdf/2507.09063v1#page=2) [PDF, p. 4](https://arxiv.org/pdf/2507.09063v1#page=4)

**Limitations and scope.** Tasks were selected manually. Ten repositories were used to compare agents’ step counts with a human’s. For example, in the Gunicorn task, the final command verifies that a request receives a response, although the specification also requires automatic restart after failure. [PDF, p. 6](https://arxiv.org/pdf/2507.09063v1#page=6) [PDF, p. 8](https://arxiv.org/pdf/2507.09063v1#page=8) [PDF, p. 18](https://arxiv.org/pdf/2507.09063v1#page=18)

[Audit report for 2507.09063v1](../reviews/audit-2026-11-19/2507.09063v1.md)

## Overview

The study tests whether agents can set up a development environment, install dependencies and run existing repositories. [PDF, p. 1](https://arxiv.org/pdf/2507.09063v1#page=1)

## Source files

arXiv version `2507.09063v1` · PDF pages: 18.

- [Original PDF](https://arxiv.org/pdf/2507.09063v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2507.09063.metadata.json)

PDF bookmarks — [Analysis and Results (p. 4)](https://arxiv.org/pdf/2507.09063v1#page=4) · [Limitations (p. 8)](https://arxiv.org/pdf/2507.09063v1#page=8).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Repository context](../concepts/repository-context.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
