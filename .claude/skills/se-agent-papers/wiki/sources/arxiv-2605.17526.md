---
type: source
title: "SaaSBench: Exploring the Boundaries of Coding Agents in Long-Horizon Enterprise SaaS Engineering"
created: 2026-11-19
arxiv_id: "2605.17526"
url: "https://arxiv.org/abs/2605.17526"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "context-window", "evaluation-metrics", "benchmarks", "long-horizon-development", "comparison-and-reproducibility"]
source_path: "raw/papers/2605.17526.md"
sources: ["https://arxiv.org/abs/2605.17526"]
ingested: "2026-11-19"
---

# SaaSBench: Exploring the Boundaries of Coding Agents in Long-Horizon Enterprise SaaS Engineering

**Paper:** [2605.17526](https://arxiv.org/abs/2605.17526) · [PDF](https://arxiv.org/pdf/2605.17526) · [HTML](https://arxiv.org/html/2605.17526)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** SaaSBench checks dependencies between components using 5,370 validation points across 30 tasks in six SaaS domains. [PDF, p. 1](https://arxiv.org/pdf/2605.17526v1#page=1)

**Key result.** In an analysis of 480 functional units for two agents, 63.5% had an unstable stack and 32.1% were only superficially accessible. In a separate evaluation on 30 tasks, the best configuration earned 20.68% of normalized points for meeting requirements. [PDF, p. 7](https://arxiv.org/pdf/2605.17526v1#page=7) [PDF, p. 9](https://arxiv.org/pdf/2605.17526v1#page=9) [PDF, p. 10](https://arxiv.org/pdf/2605.17526v1#page=10) [PDF, p. 21](https://arxiv.org/pdf/2605.17526v1#page=21) [PDF, p. 22](https://arxiv.org/pdf/2605.17526v1#page=22)

**Limitations and scope.** An early failure prevents observation of later stages. The aggregate score therefore provides limited evidence about the ability to implement business logic itself. [PDF, p. 1](https://arxiv.org/pdf/2605.17526v1#page=1)

[Audit report for 2605.17526v1](../reviews/audit-2026-11-19/2605.17526v1.md)

## Overview

The study evaluates coding agents on long-running tasks that involve building and extending SaaS applications. [PDF, p. 1](https://arxiv.org/pdf/2605.17526v1#page=1)

## Source files

arXiv version `2605.17526v1` · PDF pages: 29.

- [Original PDF](https://arxiv.org/pdf/2605.17526v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2605.17526.metadata.json)

PDF bookmarks — [Experiments (p. 7)](https://arxiv.org/pdf/2605.17526v1#page=7) · [Limitations and Future Work (p. 29)](https://arxiv.org/pdf/2605.17526v1#page=29).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Context window](../concepts/context-window.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Long-term software evolution](../concepts/long-horizon-development.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
