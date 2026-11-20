---
type: concept
title: "GraphRAG vs RAPTOR vs LightRAG"
created: 2026-11-19
tags: ["comparison", "research-map"]
---

# GraphRAG vs RAPTOR vs LightRAG

The approaches use a community graph with aggregation of partial answers, a tree of hierarchical summaries, and combined graph and vector retrieval. They have different objectives and indexing costs. Comparing them requires evaluation on the same corpus.

**Note:** This comparison draws on sources at different stages of review. Its conclusions are a narrative synthesis without an A/B experiment or statistical meta-analysis.

## Publications

- [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](../sources/arxiv-2404.16130.md) — The method builds an entity graph and summarizes graph communities to answer questions that span a large text collection.
- [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](../sources/arxiv-2401.18059.md) — The method builds a hierarchy of summaries and passages to support retrieval at multiple levels of detail.
- [LightRAG: Simple and Fast Retrieval-Augmented Generation](../sources/arxiv-2410.05779.md) — The method combines a relationship graph and vector representations with two-level retrieval and incremental index updates.

## Criteria for a fair comparison

- Use the same task class and data sources for each method.
- Record the costs of indexing, generation and evaluation.
- Check the limitations and versions of the papers.
- Scores from different benchmarks require a common evaluation before direct comparison.
