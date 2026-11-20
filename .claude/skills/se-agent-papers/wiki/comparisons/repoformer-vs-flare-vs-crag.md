---
type: concept
title: "Repoformer vs FLARE vs CRAG"
created: 2026-11-19
tags: ["comparison", "research-map"]
---

# Repoformer vs FLARE vs CRAG

Deciding whether to retrieve, choosing when to retrieve during generation and evaluating the retrieved documents are distinct steps.

**Note:** This comparison draws on sources at different stages of review. Its conclusions are a narrative synthesis without an A/B experiment or statistical meta-analysis.

## Publications

- [Repoformer: Selective Retrieval for Repository-Level Code Completion](../sources/arxiv-2403.10059.md) — The method retrieves context selectively when it is expected to help code generation, reducing noise and unnecessary cost.
- [Active Retrieval Augmented Generation](../sources/arxiv-2305.06983.md) — FLARE investigates when to retrieve additional information during long-form generation.
- [Corrective Retrieval Augmented Generation](../sources/arxiv-2401.15884.md) — CRAG assesses retrieved documents and takes corrective action when the retrieved evidence is of poor quality.

## Criteria for a fair comparison

- Use the same task class and data sources for each method.
- Record the costs of indexing, generation and evaluation.
- Check the limitations and versions of the papers.
- Scores from different benchmarks require a common evaluation before direct comparison.
