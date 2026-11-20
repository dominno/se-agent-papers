---
type: source
title: "RoadmapBench: Evaluating Long-Horizon Agentic Software Development Across Version Upgrades"
created: 2026-11-19
arxiv_id: "2605.15846"
url: "https://arxiv.org/abs/2605.15846"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "task-planning", "repository-context", "context-window", "temporal-reasoning", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "long-horizon-development", "regression-testing", "comparison-and-reproducibility"]
source_path: "raw/papers/2605.15846.md"
sources: ["https://arxiv.org/abs/2605.15846"]
ingested: "2026-11-19"
---

# RoadmapBench: Evaluating Long-Horizon Agentic Software Development Across Version Upgrades

**Paper:** [2605.15846](https://arxiv.org/abs/2605.15846) · [PDF](https://arxiv.org/pdf/2605.15846) · [HTML](https://arxiv.org/html/2605.15846)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** RoadmapBench requires agents to implement planned changes between releases. Specifications and tests define 115 tasks from 17 repositories. The median reference change is 3,714 lines. [PDF, p. 3](https://arxiv.org/pdf/2605.15846v2#page=3) [PDF, p. 4](https://arxiv.org/pdf/2605.15846v2#page=4) [PDF, p. 5](https://arxiv.org/pdf/2605.15846v2#page=5)

**Key result.** In OpenHands, Claude Opus 4.7 fully solved 39.1% of tasks. Seed-2.0-Pro had the lowest score at 5.2%. In Terminus 2 the same models scored 38.3% and 2.6%, respectively. [PDF, p. 7](https://arxiv.org/pdf/2605.15846v2#page=7)

**Limitations and scope.** Each configuration was run once per task. Behavioral tests measure correctness and do not evaluate how idiomatic or maintainable the implementation is. [PDF, p. 7](https://arxiv.org/pdf/2605.15846v2#page=7) [PDF, p. 15](https://arxiv.org/pdf/2605.15846v2#page=15)

[Section and table audit for 2605.15846v2](../reviews/audit-2026-11-19/2605.15846v2.md)

## Overview

The study examines complex repository changes implemented in stages across successive product releases. [PDF, p. 1](https://arxiv.org/pdf/2605.15846v2#page=1)

## Source files

arXiv version `2605.15846v2` · PDF pages: 30.

- [Original PDF](https://arxiv.org/pdf/2605.15846v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2605.15846.metadata.json)

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Task planning](../concepts/task-planning.md)
- [Repository context](../concepts/repository-context.md)
- [Context window](../concepts/context-window.md)
- [Temporal reasoning](../concepts/temporal-reasoning.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Long-term software evolution](../concepts/long-horizon-development.md)
- [Regression tests](../concepts/regression-testing.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
