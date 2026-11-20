---
type: source
title: "RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems"
created: 2026-11-19
arxiv_id: "2306.03091"
url: "https://arxiv.org/abs/2306.03091"
review_status: "fulltext_reviewed"
full_text_reviewed: true
tags: ["agent-orchestration", "coding-agents", "repository-context", "evaluation-metrics", "benchmarks", "comparison-and-reproducibility"]
source_path: "raw/papers/2306.03091.md"
sources: ["https://arxiv.org/abs/2306.03091"]
ingested: "2026-11-19"
---

# RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems

**Paper:** [2306.03091](https://arxiv.org/abs/2306.03091) · [PDF](https://arxiv.org/pdf/2306.03091) · [HTML](https://arxiv.org/html/2306.03091)  
**Review status:** `fulltext_reviewed` · **Full text reviewed:** **yes**

## Research findings

**Method.** RepoBench separates cross-file code retrieval, next-line prediction and end-to-end evaluation of both stages. [PDF, p. 1](https://arxiv.org/pdf/2306.03091v2#page=1)

**Key result.** For difficult first uses of elements from other files in Python, acc@1 was 10.01% for Jaccard similarity, 7.68% for the edit-based metric and 17.70% for UniXcoder (Table 2). The generator’s benefit from retrieved results also varied with the model. [PDF, p. 6](https://arxiv.org/pdf/2306.03091v2#page=6) [PDF, p. 9](https://arxiv.org/pdf/2306.03091v2#page=9) [PDF, p. 18](https://arxiv.org/pdf/2306.03091v2#page=18)

**Limitations and scope.** The benchmark covers Python and Java, and the generation task is next-line prediction. It does not establish the correctness of a substantial repository change. [PDF, p. 1](https://arxiv.org/pdf/2306.03091v2#page=1)

[Audit report for 2306.03091v2](../reviews/audit-2026-11-19/2306.03091v2.md)

## Overview

The benchmark evaluates code completion that requires cross-file knowledge and retrieval of repository context. [PDF, p. 1](https://arxiv.org/pdf/2306.03091v2#page=1)

## Source files

arXiv version `2306.03091v2` · PDF pages: 18.

- [Original PDF](https://arxiv.org/pdf/2306.03091v2)
- [Authors, license, retrieval metadata and SHA-256 digests](../raw/metadata/2306.03091.metadata.json)

PDF bookmarks — [Experiments (p. 5)](https://arxiv.org/pdf/2306.03091v2#page=5).

## Related concepts

- [Agent orchestration](../concepts/agent-orchestration.md)
- [Coding agents](../concepts/coding-agents.md)
- [Repository context](../concepts/repository-context.md)
- [Evaluation metrics](../concepts/evaluation-metrics.md)
- [Agent and LLM benchmarks](../concepts/benchmarks.md)
- [Benchmark reproducibility](../concepts/comparison-and-reproducibility.md)

## Provenance and review

- This record originated in the initial index of 100 papers.
