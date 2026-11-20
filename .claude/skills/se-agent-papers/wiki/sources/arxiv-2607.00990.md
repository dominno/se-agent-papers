---
type: source
title: "SWE-Doctor: Guiding Software Engineering Agents with Runtime Diagnosis from Multi-Faceted Bug Reproduction Tests"
created: 2026-11-19
arxiv_id: "2607.00990"
url: "https://arxiv.org/abs/2607.00990"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "debugging", "temporal-reasoning", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2607.00990.md"
sources: ["https://arxiv.org/abs/2607.00990"]
ingested: "2026-11-19"
---

# SWE-Doctor: Guiding Software Engineering Agents with Runtime Diagnosis from Multi-Faceted Bug Reproduction Tests

**Paper:** [2607.00990](https://arxiv.org/abs/2607.00990) · [PDF](https://arxiv.org/pdf/2607.00990) · [HTML](https://arxiv.org/html/2607.00990)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** SWE-Doctor decomposes an issue into requirements, generates tests and collects observations by running them under a debugger. It links diagnoses to code locations and requirements before generating a patch. The main sample covers 436 Verified issues and 107 Pro issues in Python. [PDF, p. 4](https://arxiv.org/pdf/2607.00990v1#page=4) [PDF, p. 5](https://arxiv.org/pdf/2607.00990v1#page=5) [PDF, p. 6](https://arxiv.org/pdf/2607.00990v1#page=6) [PDF, p. 7](https://arxiv.org/pdf/2607.00990v1#page=7)

**Key result.** Averaged across five models, the agents resolved 75.7% of Verified issues and 59.4% of Pro issues. On Pro, mini-SWE-agent achieved 50.5% and live-SWE-agent achieved 51.4%. A separate experiment on 50 Go issues yielded 36% versus 32% and 30%. [PDF, p. 7](https://arxiv.org/pdf/2607.00990v1#page=7) [PDF, p. 10](https://arxiv.org/pdf/2607.00990v1#page=10)

**Limitations and scope.** The evaluation concerns bug repair. Go is represented by one 50-task sample and one model. The repeatability analysis and ablations also use limited samples of 50 tasks. Diagnostics increased the mean cost per issue when averaged over all submitted issues. [PDF, p. 7](https://arxiv.org/pdf/2607.00990v1#page=7) [PDF, p. 8](https://arxiv.org/pdf/2607.00990v1#page=8) [PDF, p. 9](https://arxiv.org/pdf/2607.00990v1#page=9) [PDF, p. 10](https://arxiv.org/pdf/2607.00990v1#page=10)

## Overview

The method uses diverse bug-reproducing tests to improve fault diagnosis and code repair. [PDF, p. 1](https://arxiv.org/pdf/2607.00990v1#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2607.00990v1.md)

## Source files

arXiv version `2607.00990v1` · PDF pages: 12.

- [Original PDF](https://arxiv.org/pdf/2607.00990v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2607.00990.metadata.json)

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Debugging](../concepts/debugging.md)
- [Temporal reasoning](../concepts/temporal-reasoning.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
