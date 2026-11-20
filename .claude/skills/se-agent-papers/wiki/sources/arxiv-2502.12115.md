---
type: source
title: "SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering?"
created: 2026-11-19
arxiv_id: "2502.12115"
url: "https://arxiv.org/abs/2502.12115"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "evaluation-metrics", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2502.12115.md"
sources: ["https://arxiv.org/abs/2502.12115"]
ingested: "2026-11-19"
---

# SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering?

**Paper:** [2502.12115](https://arxiv.org/abs/2502.12115) · [PDF](https://arxiv.org/pdf/2502.12115) · [HTML](https://arxiv.org/html/2502.12115)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** For 1,488 historical jobs associated with Expensify, the authors examined two tasks: implementing changes assessed by engineer-written end-to-end tests, and selecting the proposal historically accepted by a manager. Each task was assigned its historical payout. [PDF, p. 2](https://arxiv.org/pdf/2502.12115v4#page=2) [PDF, p. 3](https://arxiv.org/pdf/2502.12115v4#page=3) [PDF, p. 5](https://arxiv.org/pdf/2502.12115v4#page=5) [PDF, p. 7](https://arxiv.org/pdf/2502.12115v4#page=7)

**Key result.** On Diamond, Claude 3.5 Sonnet achieved 26.2% pass@1 on execution tasks and 44.9% on decision tasks. Overall it scored 36.1% across 502 tasks, earning a simulated $208,050 out of $500,800. [PDF, p. 7](https://arxiv.org/pdf/2502.12115v4#page=7) [PDF, p. 8](https://arxiv.org/pdf/2502.12115v4#page=8)

**Limitations and scope.** The results describe one project in which fixes predominated. The proposal-selection evaluation measures agreement with the manager’s historical decision. An estimate based on the historical payout and an estimate of API execution costs measure different quantities. [PDF, p. 1](https://arxiv.org/pdf/2502.12115v4#page=1) [PDF, p. 5](https://arxiv.org/pdf/2502.12115v4#page=5) [PDF, p. 7](https://arxiv.org/pdf/2502.12115v4#page=7) [PDF, p. 8](https://arxiv.org/pdf/2502.12115v4#page=8) [PDF, p. 29](https://arxiv.org/pdf/2502.12115v4#page=29)

## Overview

The evaluation measures models' ability to perform realistic, priced software-engineering tasks and make technical decisions. [PDF, p. 1](https://arxiv.org/pdf/2502.12115v4#page=1)

[Section and evidence audit](../reviews/audit-2026-11-19/2502.12115v4.md)

## Source files

arXiv version `2502.12115v4` · PDF pages: 39.

- [Original PDF](https://arxiv.org/pdf/2502.12115v4)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2502.12115.metadata.json)

PDF bookmarks — [Experiments and Results (p. 5)](https://arxiv.org/pdf/2502.12115v4#page=5) · [Limitations (p. 8)](https://arxiv.org/pdf/2502.12115v4#page=8).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
