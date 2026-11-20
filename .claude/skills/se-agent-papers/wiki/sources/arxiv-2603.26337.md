---
type: source
title: "A Benchmark for Evaluating Repository-Level Code Agents with Intermediate Reasoning on Feature Addition Task"
created: 2026-11-19
arxiv_id: "2603.26337"
url: "https://arxiv.org/abs/2603.26337"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "task-planning", "coding-agents", "repository-context", "rag-evaluation", "evaluation-metrics", "llm-as-judge", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2603.26337.md"
sources: ["https://arxiv.org/abs/2603.26337"]
ingested: "2026-11-19"
---

# A Benchmark for Evaluating Repository-Level Code Agents with Intermediate Reasoning on Feature Addition Task

**Paper:** [2603.26337](https://arxiv.org/abs/2603.26337) · [PDF](https://arxiv.org/pdf/2603.26337) · [HTML](https://arxiv.org/html/2603.26337)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** RACE-Bench combines execution-based tests on 528 feature-addition tasks from 12 repositories with an assessment of behavioral agreement with a single accepted implementation. The agent sees tests of the requested new feature. Tests of existing functionality are hidden. [PDF, p. 3](https://arxiv.org/pdf/2603.26337v3#page=3) [PDF, p. 5](https://arxiv.org/pdf/2603.26337v3#page=5) [PDF, p. 6](https://arxiv.org/pdf/2603.26337v3#page=6)

**Key result.** For applied patches that failed tests, the review reproduced the mean relative difference from successful patches. Across nine equally weighted combinations of three agents and three levels (files, tasks and steps), reference coverage was 35.7% lower on average and the share of additional elements was 94.1% higher. [PDF, p. 8](https://arxiv.org/pdf/2603.26337v3#page=8)

**Limitations and scope.** The reference is a single accepted implementation. GPT-5.5 classified 89 of 127 working patches that did not fully match it as reasonable alternative implementations. The authors note that humans did not validate this classification. [PDF, p. 10](https://arxiv.org/pdf/2603.26337v3#page=10)

[Audit of sections, tables and appendices](../reviews/audit-2026-11-19/2603.26337v3.md)

## Overview

The evaluation covers task analysis, file localization and decomposition of the work alongside the final code. [PDF, p. 1](https://arxiv.org/pdf/2603.26337v3#page=1)

## Source files

**Paper license notice.** The arXiv record uses its non-exclusive distribution license. The authors also grant CC BY 4.0 on the first page of this version. [PDF, p. 1](https://arxiv.org/pdf/2603.26337v3#page=1)

arXiv version `2603.26337v3` · PDF pages: 13.

- [Original PDF](https://arxiv.org/pdf/2603.26337v3)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2603.26337.metadata.json)

PDF bookmarks — [4 Results and Analysis (p. 7)](https://arxiv.org/pdf/2603.26337v3#page=7).

The record title follows v1. In v3, the authors changed the title to RACE-Bench: A Reasoning-Augmented Benchmark for Repository-Level Code Agents on Feature Addition.

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Task planning](../concepts/task-planning.md)
- [Coding agents](../concepts/coding-agents.md)
- [Repository context](../concepts/repository-context.md)
- [RAG evaluation](../concepts/rag-evaluation.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [LLM-as-a-Judge](../concepts/llm-as-judge.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
