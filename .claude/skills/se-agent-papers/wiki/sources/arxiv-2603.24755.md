---
type: source
title: "SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks"
created: 2026-11-19
arxiv_id: "2603.24755"
url: "https://arxiv.org/abs/2603.24755"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "context-window", "evaluation-metrics", "benchmarks", "long-horizon-development", "architecture-erosion", "comparison-and-reproducibility"]
source_path: "raw/papers/2603.24755.md"
sources: ["https://arxiv.org/abs/2603.24755"]
ingested: "2026-11-19"
---

# SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks

**Paper:** [2603.24755](https://arxiv.org/abs/2603.24755) · [PDF](https://arxiv.org/pdf/2603.24755) · [HTML](https://arxiv.org/html/2603.24755)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** In SlopCodeBench, agents repeatedly extend their own solutions. The authors measure complexity concentration and redundant code across 196 checkpoints in 36 problems. [PDF, p. 1](https://arxiv.org/pdf/2603.24755v2#page=1)

**Key result.** Structural erosion increased in 77% of trajectories and redundancy in 75.5%. The highest stage pass rate under the full criterion was 14.8% across 196 stages. Scores were higher when the evaluator checked only the current requirement. [PDF, p. 6](https://arxiv.org/pdf/2603.24755v2#page=6) [PDF, p. 7](https://arxiv.org/pdf/2603.24755v2#page=7)

**Limitations and scope.** The study measured quality using two structural metrics. Neither directly measures the time a human would subsequently spend maintaining the code. [PDF, p. 1](https://arxiv.org/pdf/2603.24755v2#page=1)

[Audit report for 2603.24755v2](../reviews/audit-2026-11-19/2603.24755v2.md)

## Overview

The study tracks degradation in code quality and structure as agents repeatedly extend the same project. [PDF, p. 1](https://arxiv.org/pdf/2603.24755v2#page=1)

## Source files

arXiv version `2603.24755v2` · PDF pages: 26.

- [Original PDF](https://arxiv.org/pdf/2603.24755v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2603.24755.metadata.json)

PDF bookmarks — [Iterative Evaluation of Coding Agents (p. 5)](https://arxiv.org/pdf/2603.24755v2#page=5).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Context window](../concepts/context-window.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Long-term software evolution](../concepts/long-horizon-development.md)
- [Architectural erosion](../concepts/architecture-erosion.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
