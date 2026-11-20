---
type: source
title: "SWE-Cycle: Benchmarking Code Agents across the Complete Issue Resolution Cycle"
created: 2026-11-19
arxiv_id: "2605.13139"
url: "https://arxiv.org/abs/2605.13139"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "evaluation-metrics", "benchmarks", "long-horizon-development", "comparison-and-reproducibility"]
source_path: "raw/papers/2605.13139.md"
sources: ["https://arxiv.org/abs/2605.13139"]
ingested: "2026-11-19"
---

# SWE-Cycle: Benchmarking Code Agents across the Complete Issue Resolution Cycle

**Paper:** [2605.13139](https://arxiv.org/abs/2605.13139) · [PDF](https://arxiv.org/pdf/2605.13139) · [HTML](https://arxiv.org/html/2605.13139)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** Across 489 issues in nine languages, six models configured the environment, implemented changes and wrote tests. The authors compared individual tasks with the full development cycle using both static checks and execution. [PDF, p. 4](https://arxiv.org/pdf/2605.13139v1#page=4) [PDF, p. 5](https://arxiv.org/pdf/2605.13139v1#page=5) [PDF, p. 6](https://arxiv.org/pdf/2605.13139v1#page=6) [PDF, p. 8](https://arxiv.org/pdf/2605.13139v1#page=8) [PDF, p. 13](https://arxiv.org/pdf/2605.13139v1#page=13)

**Key result.** GLM-5.1 leads on FullCycle with 81.49% of available points and 13.50% fully solved. Sonnet 4.6 achieved 80.52% and 12.27%, respectively. [PDF, p. 8](https://arxiv.org/pdf/2605.13139v1#page=8)

**Limitations and scope.** Agreement with human judgments was measured on 946 submissions using task-specific rubrics and tolerances. Python accounts for 68.9% of the dataset. Results also depend on whether the reference patch is available to the evaluator. [PDF, p. 13](https://arxiv.org/pdf/2605.13139v1#page=13) [PDF, p. 16](https://arxiv.org/pdf/2605.13139v1#page=16) [PDF, p. 24](https://arxiv.org/pdf/2605.13139v1#page=24)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2605.13139v1.md)

## Overview

The evaluation covers the entire coding task, from setting up the environment to implementation and testing. [PDF, p. 1](https://arxiv.org/pdf/2605.13139v1#page=1)

## Source files

arXiv version `2605.13139v1` · PDF pages: 26.

- [Original PDF](https://arxiv.org/pdf/2605.13139v1)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2605.13139.metadata.json)

PDF bookmarks — [Methodology (p. 3)](https://arxiv.org/pdf/2605.13139v1#page=3) · [Experiments (p. 6)](https://arxiv.org/pdf/2605.13139v1#page=6) · [Conclusions & Limitations (p. 9)](https://arxiv.org/pdf/2605.13139v1#page=9).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Long-term software evolution](../concepts/long-horizon-development.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
